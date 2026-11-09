import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))

from check_run import (  # noqa: E402
    check_curated_unchanged,
    check_digest,
    check_git_paths,
    check_ledger_for_run,
)

RUN = "2026-11-16"


def study(n):
    return f"""### {n}. Study {n} — Lab (Author), 2026-11-12
**Link:** https://lab.example/study-{n} · **Type:** controlled experiment · **Rigor:** 4/5
**Method:** 12,000 prompts across ChatGPT and Perplexity, Sept–Oct 2026
**Key findings:** • a • b • c
**Conflicts of interest:** none apparent
**Wiki fit:** extends [[ai-citation-landscape]]
"""


def digest(passed=2, rejected=1, unverified=1, studies=None):
    studies = [study(i) for i in range(1, passed + 1)] if studies is None else studies
    body = "\n".join(studies) if studies else "_No studies passed the gate this run._\n"
    unv = "\n".join(f"- Gated {i} — https://g.example/{i} — gated PDF" for i in range(unverified)) or "_None._"
    rej = "\n".join(f"- Roundup {i} — https://r.example/{i} — g1: secondary aggregation" for i in range(rejected)) or "_None._"
    return f"""# Research digest — {RUN}

**Window:** 2026-11-02 to {RUN} · **Passed:** {passed} · **Rejected:** {rejected} · **Couldn't verify:** {unverified}
**Lanes:** academic ✓ · industry ✓ · practitioner ✓

## Studies

{body}
## Couldn't verify
{unv}

## Rejected
{rej}

## Seed list changes
_None._
"""


SEED = """# Seed sources

## Curated
### Industry research
- key: ahrefs | name: Ahrefs | url: https://ahrefs.com/blog/ | note: x

## Discovered

## Caution
- key: thedigitalbloom | name: The Digital Bloom | added: 2026-08-03 | reason: roundups
"""


class DigestTests(unittest.TestCase):
    def test_valid_digest_passes(self):
        self.assertEqual(check_digest(digest(), RUN), [])

    def test_missing_wiki_fit_fails(self):
        text = digest().replace("**Wiki fit:** extends [[ai-citation-landscape]]\n", "", 1)
        errs = check_digest(text, RUN)
        self.assertTrue(any("Wiki fit" in e for e in errs), errs)

    def test_passed_count_mismatch_fails(self):
        text = digest().replace("**Passed:** 2", "**Passed:** 3")
        self.assertNotEqual(check_digest(text, RUN), [])

    def test_rigor_out_of_range_fails(self):
        text = digest().replace("**Rigor:** 4/5", "**Rigor:** 6/5", 1)
        self.assertNotEqual(check_digest(text, RUN), [])

    def test_empty_week_digest_valid(self):
        self.assertEqual(check_digest(digest(0, 0, 0), RUN), [])


class LedgerTests(unittest.TestCase):
    def test_ledger_count_mismatch_fails(self):
        ledger = "\n".join(f"{RUN} | pass:4 | lab | T{i} | https://x/{i} | r" for i in range(3))
        self.assertNotEqual(check_ledger_for_run(ledger, "", RUN, 2, 1, 1), [])

    def test_ledger_count_match_passes(self):
        lines = [f"{RUN} | pass:4 | lab | T{i} | https://x/{i} | r" for i in range(2)]
        lines += [f"{RUN} | reject:g1 | r | R | https://r/0 | g1", f"{RUN} | unverified | g | G | https://g/0 | gated"]
        lines += ["2026-11-09 | pass:3 | old | O | https://o | r"]
        self.assertEqual(check_ledger_for_run("\n".join(lines), "", RUN, 2, 1, 1), [])


    def test_ledger_counts_only_appended_lines(self):
        before = f"# ledger\n{RUN} | reject:g1 | r | Earlier run | https://r/old | g1"
        after = before + f"\n{RUN} | pass:4 | lab | New | https://x/new | r"
        self.assertEqual(check_ledger_for_run(after, before, RUN, 1, 0, 0), [])

    def test_ledger_rewrite_detected(self):
        before = f"# ledger\n{RUN} | reject:g1 | r | Earlier run | https://r/old | g1"
        after = f"# ledger\n{RUN} | pass:4 | lab | New | https://x/new | r"
        errs = check_ledger_for_run(after, before, RUN, 1, 0, 0)
        self.assertTrue(any("append" in e for e in errs), errs)


class CuratedTests(unittest.TestCase):
    def test_curated_compared_to_snapshot_not_head(self):
        snapshot = "### Industry research\n- key: ahrefs | name: Ahrefs | url: https://ahrefs.com/blog/ | note: x"
        self.assertEqual(check_curated_unchanged(SEED, snapshot), [])
        changed = SEED.replace("note: x", "note: edited")
        self.assertNotEqual(check_curated_unchanged(changed, snapshot), [])


class GitPathTests(unittest.TestCase):
    ALLOWED = ["research-digests/2026-11-16.md", "research-digests/seen.md",
               ".claude/skills/research-scout/seed-sources.md"]

    def test_preexisting_dirty_files_allowed(self):
        before = " M wiki/index.md"
        after = " M wiki/index.md\n?? research-digests/2026-11-16.md"
        self.assertEqual(check_git_paths(before, after, self.ALLOWED), [])

    def test_new_wiki_change_fails(self):
        errs = check_git_paths("", " M wiki/concepts/x.md", self.ALLOWED)
        self.assertTrue(any("wiki/concepts/x.md" in e for e in errs), errs)

    def test_edit_to_already_dirty_file_detected(self):
        status = " M wiki/index.md"
        errs = check_git_paths(status, status, self.ALLOWED,
                               {"wiki/index.md": "aaa"}, {"wiki/index.md": "bbb"})
        self.assertTrue(any("wiki/index.md" in e for e in errs), errs)

    def test_unchanged_dirty_file_hash_passes(self):
        status = " M wiki/index.md"
        self.assertEqual(check_git_paths(status, status, self.ALLOWED,
                                         {"wiki/index.md": "aaa"}, {"wiki/index.md": "aaa"}), [])

    def test_work_dir_ignored(self):
        self.assertEqual(check_git_paths("", "?? research-digests/.work/2026-11-16/x.json", self.ALLOWED), [])


class CliTests(unittest.TestCase):
    def test_snapshot_mode_writes_status_and_curated(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            seed = repo / ".claude/skills/research-scout/seed-sources.md"
            seed.parent.mkdir(parents=True)
            seed.write_text(SEED)
            (repo / "notes").mkdir()
            (repo / "notes/draft.md").write_text("x")
            work = repo / "w"
            subprocess.run([sys.executable, str(SCRIPTS / "check_run.py"), "--snapshot",
                            "--repo", str(repo), "--work", str(work)], check=True, capture_output=True)
            status = (work / "status-before.txt").read_text()
            self.assertIn("notes/draft.md", status)  # untracked files listed individually
            self.assertIn("key: ahrefs", (work / "curated-snapshot.md").read_text())
            self.assertNotIn("thedigitalbloom", (work / "curated-snapshot.md").read_text())

    def _repo_with_first_run(self, tmp):
        repo = Path(tmp)
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        seed = repo / ".claude/skills/research-scout/seed-sources.md"
        seed.parent.mkdir(parents=True)
        seed.write_text(SEED)
        (repo / "research-digests").mkdir()
        (repo / "research-digests/seen.md").write_text(
            f"# ledger\n{RUN} | reject:g1 | r | Earlier | https://r/old | g1: roundup\n")
        (repo / "wiki").mkdir()
        (repo / "wiki/index.md").write_text("index\n")
        subprocess.run(["git", "-C", str(repo), "add", "."], check=True)
        subprocess.run(["git", "-C", str(repo), "-c", "user.email=t@t", "-c", "user.name=t",
                        "commit", "-qm", "init"], check=True)
        return repo

    def _check(self, repo, work, digest_rel):
        return subprocess.run(
            [sys.executable, str(SCRIPTS / "check_run.py"), "--repo", str(repo),
             "--digest", digest_rel, "--run-date", RUN, "--work", str(work)],
            capture_output=True, text=True,
        )

    def _snapshot(self, repo, work):
        subprocess.run([sys.executable, str(SCRIPTS / "check_run.py"), "--snapshot",
                        "--repo", str(repo), "--work", str(work)], check=True, capture_output=True)

    def test_second_run_same_day_validates(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo_with_first_run(tmp)
            work = repo / "research-digests/.work" / f"{RUN}-2"
            self._snapshot(repo, work)
            (repo / f"research-digests/{RUN}-2.md").write_text(digest(0, 0, 0))
            res = self._check(repo, work, f"research-digests/{RUN}-2.md")
            self.assertEqual(res.returncode, 0, res.stdout + res.stderr)

    def test_agent_edit_to_user_dirty_file_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo_with_first_run(tmp)
            (repo / "wiki/index.md").write_text("user edit\n")
            work = repo / "research-digests/.work" / RUN
            self._snapshot(repo, work)
            (repo / "wiki/index.md").write_text("user edit\nAGENT\n")
            (repo / f"research-digests/{RUN}-2.md").write_text(digest(0, 0, 0))
            res = self._check(repo, work, f"research-digests/{RUN}-2.md")
            self.assertEqual(res.returncode, 1)
            self.assertIn("wiki/index.md", res.stdout)

    def test_suffixed_digest_name_accepted(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo_with_first_run(tmp)
            work = repo / "research-digests/.work" / f"{RUN}-2"
            self._snapshot(repo, work)
            (repo / f"research-digests/{RUN}-2.md").write_text(digest(0, 0, 0))
            res = self._check(repo, work, f"research-digests/{RUN}-2.md")
            self.assertEqual(res.returncode, 0, res.stdout + res.stderr)
            self.assertIn("OK", res.stdout)


if __name__ == "__main__":
    unittest.main()
