"""Decide seed-list changes from the seen.md ledger.

CLI: python3 seed_rules.py --seen <seen.md> --seed <seed-sources.md>
Prints {"promote": [[key, reason, evidence_url]], "caution": [[key, reason]], "flag_curated": [[key, reason]]}.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import LedgerEntry, SeedEntry, normalize_key, parse_ledger, parse_seed  # noqa: E402

PROMOTE_MIN_SCORE = 4
MIN_DISTINCT_DATES = 2
CAUTION_GATES = {"reject:g1", "reject:g2", "reject:g3"}


@dataclass
class Changes:
    promote: list = field(default_factory=list)
    caution: list = field(default_factory=list)
    flag_curated: list = field(default_factory=list)


def evaluate(ledger: list[LedgerEntry], seed: list[SeedEntry]) -> Changes:
    section_of = {normalize_key(e.key): e.section for e in seed}
    by_key: dict[str, list[LedgerEntry]] = defaultdict(list)
    for e in ledger:
        by_key[normalize_key(e.key)].append(e)

    changes = Changes()
    for key in sorted(by_key):
        entries = by_key[key]
        section = section_of.get(key)
        passes = [e for e in entries if e.verdict.startswith("pass:")]
        pass_dates = sorted({e.date for e in passes})
        fails = [e for e in entries if e.verdict in CAUTION_GATES]
        fail_dates = sorted({e.date for e in fails})

        if section is None and passes:
            best = max(passes, key=lambda e: (int(e.verdict.split(":")[1]), e.date))
            score = int(best.verdict.split(":")[1])
            if score >= PROMOTE_MIN_SCORE:
                changes.promote.append((key, f"pass rigor {score} on {best.date}", best.url))
                continue
            if len(pass_dates) >= MIN_DISTINCT_DATES:
                changes.promote.append((key, f"gate passes on {', '.join(pass_dates)}", best.url))
                continue

        if len(fail_dates) >= MIN_DISTINCT_DATES and section != "caution":
            gates = ", ".join(sorted({e.verdict.split(':')[1] for e in fails}))
            reason = f"gate fails on {', '.join(fail_dates)} ({gates})"
            if section == "curated":
                changes.flag_curated.append((key, reason))
            else:
                changes.caution.append((key, reason))
    return changes


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seen", required=True)
    ap.add_argument("--seed", required=True)
    args = ap.parse_args(argv)
    ch = evaluate(parse_ledger(Path(args.seen).read_text()), parse_seed(Path(args.seed).read_text()))
    print(json.dumps(asdict(ch), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
