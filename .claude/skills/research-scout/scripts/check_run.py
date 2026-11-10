"""Validate one research-scout run's outputs.

Before the run:  python3 check_run.py --snapshot --repo <root> --work <work-dir>
  writes status-before.txt, hashes-before.json, seen-before.md and curated-snapshot.md into <work-dir>
After the run:   python3 check_run.py --repo <root> --digest <path> --run-date YYYY-MM-DD --work <work-dir>
  prints OK (exit 0) or one error per line (exit 1)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import parse_ledger, parse_seed, section_text  # noqa: E402

SEED_PATH = ".claude/skills/research-scout/seed-sources.md"
SEEN_PATH = "research-digests/seen.md"
WORK_PREFIX = "research-digests/.work/"
SECTIONS = ["Studies", "Couldn't verify", "Rejected", "Seed list changes"]
ENTRY_LABELS = ["Link", "Type", "Rigor", "Method", "Key findings", "Conflicts of interest", "Wiki fit"]
NO_STUDIES = "_No studies passed the gate this run._"
NONE = "_None._"
HEADER_RE = re.compile(
    r"\*\*Window:\*\*.*\*\*Passed:\*\*\s*(\d+).*\*\*Rejected:\*\*\s*(\d+).*\*\*Couldn't verify:\*\*\s*(\d+)"
)


def _sections(text: str) -> list[tuple[str, list[str]]]:
    out: list[tuple[str, list[str]]] = []
    for line in text.splitlines():
        if line.startswith("## "):
            out.append((line[3:].strip(), []))
        elif out:
            out[-1][1].append(line)
    return out


def header_counts(text: str):
    m = HEADER_RE.search(text)
    return tuple(int(g) for g in m.groups()) if m else None


def check_digest(text: str, run_date: str) -> list[str]:
    errs = []
    lines = text.splitlines()
    if not lines or lines[0].strip() != f"# Research digest — {run_date}":
        errs.append(f"first line must be '# Research digest — {run_date}'")
    counts = header_counts(text)
    if counts is None:
        errs.append("missing summary line with **Window:**, **Passed:**, **Rejected:**, **Couldn't verify:**")
        return errs
    passed, rejected, unverified = counts
    lanes = next((l for l in lines if l.startswith("**Lanes:**")), "")
    for lane in ("academic", "industry", "practitioner"):
        if lane not in lanes:
            errs.append(f"**Lanes:** line must name {lane}")

    secs = _sections(text)
    names = [n for n, _ in secs]
    if names != SECTIONS:
        errs.append(f"H2 sections must be {SECTIONS} in order; found {names}")
        return errs
    body = dict(secs)

    studies = body["Studies"]
    entries: list[list[str]] = []
    for line in studies:
        if line.startswith("### "):
            entries.append([line])
        elif entries:
            entries[-1].append(line)
    if len(entries) != passed:
        errs.append(f"Studies has {len(entries)} entries but **Passed:** is {passed}")
    if passed == 0 and NO_STUDIES not in "\n".join(studies):
        errs.append(f"empty Studies section must contain {NO_STUDIES}")
    for entry in entries:
        block = "\n".join(entry)
        title = entry[0][4:].strip()
        for label in ENTRY_LABELS:
            if f"**{label}:**" not in block:
                errs.append(f"study '{title}' is missing **{label}:**")
        if not re.search(r"\*\*Link:\*\*\s*https?://", block):
            errs.append(f"study '{title}' has no http(s) link")
        m = re.search(r"\*\*Rigor:\*\*\s*(\d+)/5", block)
        if not m or not 1 <= int(m.group(1)) <= 5:
            errs.append(f"study '{title}' needs **Rigor:** 1-5/5")

    for name, expected in (("Couldn't verify", unverified), ("Rejected", rejected)):
        sec = body[name]
        bullets = [l for l in sec if l.startswith("- ")]
        if len(bullets) != expected:
            errs.append(f"{name} has {len(bullets)} bullets but header says {expected}")
        if expected == 0 and NONE not in "\n".join(sec):
            errs.append(f"empty {name} section must contain {NONE}")
    return errs


def check_ledger_for_run(ledger_text: str, before_text: str, run_date: str,
                         passed: int, rejected: int, unverified: int) -> list[str]:
    """seen.md must be append-only; count only the lines this run appended."""
    if not ledger_text.startswith(before_text.rstrip("\n")):
        return ["seen.md is append-only, but lines that existed before the run were changed or removed"]
    try:
        entries = [e for e in parse_ledger(ledger_text[len(before_text.rstrip("\n")):]) if e.date == run_date]
    except ValueError as exc:
        return [f"seen.md (lines added this run): {exc}"]
    got = (
        sum(e.verdict.startswith("pass:") for e in entries),
        sum(e.verdict.startswith("reject:") for e in entries),
        sum(e.verdict == "unverified" for e in entries),
    )
    if got != (passed, rejected, unverified):
        return [f"seen.md lines added this run have pass/reject/unverified {got}, digest says {(passed, rejected, unverified)}"]
    return []


def check_curated_unchanged(seed_text: str, snapshot_text: str) -> list[str]:
    try:
        parse_seed(seed_text)
    except ValueError as exc:
        return [f"seed-sources.md: {exc}"]
    if section_text(seed_text, "Curated").strip() != snapshot_text.strip():
        return ["Curated section of seed-sources.md changed during the run"]
    return []


def _paths(status: str) -> dict[str, str]:
    out = {}
    for line in status.splitlines():
        if len(line) < 4:
            continue
        path = line[3:].split(" -> ")[-1].strip().strip('"')
        out[path] = line
    return out


def check_git_paths(status_before: str, status_after: str, allowed: list[str],
                    hashes_before: dict | None = None, hashes_after: dict | None = None) -> list[str]:
    before = _paths(status_before)
    hashes_before = hashes_before or {}
    hashes_after = hashes_after or {}
    errs = []
    for path, line in _paths(status_after).items():
        if path in allowed or path.startswith(WORK_PREFIX):
            continue
        if before.get(path) == line and hashes_before.get(path) == hashes_after.get(path):
            continue
        errs.append(f"unexpected change outside allowed files: {path} "
                    "(agent edit, or a concurrent edit by the user; never revert it, report it)")
    return errs


def file_hashes(repo: Path, status: str) -> dict:
    out = {}
    for path in _paths(status):
        f = repo / path
        out[path] = hashlib.sha256(f.read_bytes()).hexdigest() if f.is_file() else None
    return out


def git_status(repo: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), "status", "--porcelain", "--untracked-files=all"],
        capture_output=True, text=True, check=True,
    ).stdout


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--snapshot", action="store_true")
    ap.add_argument("--digest")
    ap.add_argument("--run-date")
    args = ap.parse_args(argv)
    repo = Path(args.repo)
    work = Path(args.work)

    if args.snapshot:
        work.mkdir(parents=True, exist_ok=True)
        status = git_status(repo)
        (work / "status-before.txt").write_text(status)
        (work / "hashes-before.json").write_text(json.dumps(file_hashes(repo, status), indent=1))
        seen = repo / SEEN_PATH
        (work / "seen-before.md").write_text(seen.read_text() if seen.is_file() else "")
        (work / "curated-snapshot.md").write_text(section_text((repo / SEED_PATH).read_text(), "Curated"))
        print("OK snapshot")
        return 0

    if not args.digest or not args.run_date:
        ap.error("--digest and --run-date are required unless --snapshot")
    digest_path = Path(args.digest)
    digest_rel = digest_path.relative_to(repo).as_posix() if digest_path.is_absolute() else digest_path.as_posix()
    if not re.match(rf"^research-digests/{re.escape(args.run_date)}(-\d+)?\.md$", digest_rel):
        print(f"digest path must be research-digests/{args.run_date}[-N].md, got {digest_rel}")
        return 1
    text = (repo / digest_rel).read_text()
    errs = check_digest(text, args.run_date)
    counts = header_counts(text)
    if counts:
        errs += check_ledger_for_run((repo / SEEN_PATH).read_text(), (work / "seen-before.md").read_text(),
                                     args.run_date, *counts)
    errs += check_curated_unchanged((repo / SEED_PATH).read_text(), (work / "curated-snapshot.md").read_text())
    status_before = (work / "status-before.txt").read_text()
    status_after = git_status(repo)
    errs += check_git_paths(status_before, status_after, [digest_rel, SEEN_PATH, SEED_PATH],
                            json.loads((work / "hashes-before.json").read_text()),
                            file_hashes(repo, status_before))
    if errs:
        print("\n".join(errs))
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
