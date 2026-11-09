import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))

from common import parse_ledger, parse_seed  # noqa: E402
from seed_rules import evaluate  # noqa: E402

SEED = """# Seed sources

## Curated
### Industry research
- key: ahrefs | name: Ahrefs | url: https://ahrefs.com/blog/ | note: x
- key: curatedsite | name: Curated Site | url: https://curated.example | note: x
- key: tryprofound | name: Profound | url: https://www.tryprofound.com/blog | note: x
- key: arxiv-cs-ir | name: arXiv cs.IR | url: https://arxiv.org/list/cs.IR/recent | note: x
- key: chris-long | name: Chris Long | url: https://www.linkedin.com/in/chris-long/ | note: x

## Discovered
- key: discoveredlab | name: Discovered Lab | lane: industry | added: 2026-10-01 | evidence: https://d.example/s

## Caution
- key: thedigitalbloom | name: The Digital Bloom | added: 2026-08-03 | reason: secondary aggregations
"""


def line(date, verdict, key, url="https://x.example/s", title="T"):
    return f"{date} | {verdict} | {key} | {title} | {url} | r"


def run(*lines, run_date=None):
    return evaluate(parse_ledger("\n".join(lines)), parse_seed(SEED), run_date)


class SeedRuleTests(unittest.TestCase):
    def test_single_pass_rigor4_promotes(self):
        ch = run(line("2026-11-09", "pass:4", "newlab", url="https://newlab.example/a"))
        self.assertEqual(ch.promote[0][0], "newlab")
        self.assertEqual(ch.promote[0][2], "https://newlab.example/a")

    def test_single_pass_rigor3_does_not_promote(self):
        self.assertEqual(run(line("2026-11-09", "pass:3", "newlab")).promote, [])

    def test_passes_on_two_dates_promote(self):
        ch = run(line("2026-11-02", "pass:2", "newlab"), line("2026-11-09", "pass:3", "newlab"))
        self.assertEqual([p[0] for p in ch.promote], ["newlab"])

    def test_same_day_passes_do_not_promote(self):
        ch = run(line("2026-11-09", "pass:3", "newlab"), line("2026-11-09", "pass:3", "newlab"))
        self.assertEqual(ch.promote, [])

    def test_listed_key_not_promoted(self):
        ch = run(line("2026-11-09", "pass:5", "ahrefs"), line("2026-11-09", "pass:5", "discoveredlab"))
        self.assertEqual(ch.promote, [])

    def test_unverified_never_counts(self):
        ch = run(line("2026-11-02", "unverified", "newlab"), line("2026-11-09", "unverified", "newlab"))
        self.assertEqual(ch.promote, [])
        self.assertEqual(ch.caution, [])

    def test_g1_g3_rejects_on_two_dates_caution(self):
        ch = run(line("2026-11-02", "reject:g1", "roundupsite"), line("2026-11-09", "reject:g3", "roundupsite"))
        self.assertEqual(ch.caution[0][0], "roundupsite")

    def test_g4_rejects_never_caution(self):
        ch = run(line("2026-11-02", "reject:g4", "roundupsite"), line("2026-11-09", "reject:g4", "roundupsite"))
        self.assertEqual(ch.caution, [])

    def test_discovered_moves_to_caution(self):
        ch = run(line("2026-11-02", "reject:g2", "discoveredlab"), line("2026-11-09", "reject:g1", "discoveredlab"))
        self.assertEqual([c[0] for c in ch.caution], ["discoveredlab"])

    def test_curated_flagged_not_cautioned(self):
        ch = run(line("2026-11-02", "reject:g1", "curatedsite"), line("2026-11-09", "reject:g1", "curatedsite"))
        self.assertEqual([f[0] for f in ch.flag_curated], ["curatedsite"])
        self.assertEqual(ch.caution, [])

    def test_already_caution_not_repeated(self):
        ch = run(line("2026-11-02", "reject:g1", "thedigitalbloom"), line("2026-11-09", "reject:g1", "thedigitalbloom"))
        self.assertEqual(ch.caution, [])
        self.assertEqual(ch.flag_curated, [])

    def test_promote_beats_caution(self):
        ch = run(
            line("2026-11-02", "reject:g1", "mixedlab"),
            line("2026-11-09", "reject:g1", "mixedlab"),
            line("2026-11-09", "pass:4", "mixedlab"),
        )
        self.assertEqual([p[0] for p in ch.promote], ["mixedlab"])
        self.assertEqual(ch.caution, [])

    def test_keys_normalize_across_spellings(self):
        ch = run(line("2026-11-02", "pass:3", "Search Engine Land"), line("2026-11-09", "pass:2", "search-engine-land"))
        self.assertEqual([p[0] for p in ch.promote], ["search-engine-land"])

    def test_old_evidence_does_not_repromote(self):
        # user deleted a Discovered entry; no new evidence this run → no re-add
        ch = run(line("2026-11-02", "pass:4", "newlab"), run_date="2026-11-09")
        self.assertEqual(ch.promote, [])

    def test_old_fails_do_not_recaution(self):
        ch = run(line("2026-11-02", "reject:g1", "roundupsite"), line("2026-11-09", "reject:g1", "roundupsite"),
                 run_date="2026-11-16")
        self.assertEqual(ch.caution, [])

    def test_alias_key_maps_to_seed_by_domain(self):
        ch = run(line("2026-11-09", "pass:5", "profound", url="https://www.tryprofound.com/blog/new-study"))
        self.assertEqual(ch.promote, [])

    def test_alias_key_curated_flagged_not_cautioned(self):
        u = "https://tryprofound.com/blog/roundup"
        ch = run(line("2026-11-02", "reject:g1", "profound", url=u), line("2026-11-09", "reject:g2", "profound", url=u))
        self.assertEqual(ch.caution, [])
        self.assertEqual([f[0] for f in ch.flag_curated], ["tryprofound"])

    def test_hub_domains_do_not_map(self):
        ch = run(line("2026-11-09", "pass:4", "newlab", url="https://arxiv.org/abs/2611.00001"),
                 line("2026-11-09", "pass:4", "someone", url="https://www.linkedin.com/posts/someone-study"))
        self.assertEqual(sorted(p[0] for p in ch.promote), ["newlab", "someone"])


if __name__ == "__main__":
    unittest.main()
