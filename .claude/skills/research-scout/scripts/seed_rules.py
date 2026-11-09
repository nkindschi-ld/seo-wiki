"""Decide seed-list changes from the seen.md ledger.

CLI: python3 seed_rules.py --seen <seen.md> --seed <seed-sources.md> --run-date YYYY-MM-DD
A rule fires only when this run added qualifying evidence, so a user's removal sticks.
Prints {"promote": [[key, reason, evidence_url]], "caution": [[key, reason]], "flag_curated": [[key, reason]]}.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import LedgerEntry, SeedEntry, normalize_key, parse_ledger, parse_seed  # noqa: E402

PROMOTE_MIN_SCORE = 4
MIN_DISTINCT_DATES = 2
CAUTION_GATES = {"reject:g1", "reject:g2", "reject:g3"}
# Hosts that publish many unrelated authors: never map a ledger entry to a seed key by these.
HUB_DOMAINS = {"arxiv.org", "aclanthology.org", "semanticscholar.org", "openreview.net", "sigir.org",
               "linkedin.com", "youtube.com", "medium.com", "substack.com", "github.com", "x.com", "twitter.com"}


def _domain(url: str) -> str:
    host = urlsplit(url if "://" in url else "http://" + url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def _domain_keys(seed: list[SeedEntry]) -> dict:
    """Domain → seed key, for domains that belong to exactly one seed entry."""
    owners: dict[str, set] = defaultdict(set)
    for e in seed:
        url = e.fields.get("url", "")
        d = _domain(url) if url else ""
        if d and d not in HUB_DOMAINS:
            owners[d].add(normalize_key(e.key))
    return {d: next(iter(keys)) for d, keys in owners.items() if len(keys) == 1}


@dataclass
class Changes:
    promote: list = field(default_factory=list)
    caution: list = field(default_factory=list)
    flag_curated: list = field(default_factory=list)


def evaluate(ledger: list[LedgerEntry], seed: list[SeedEntry], run_date: str | None = None) -> Changes:
    section_of = {normalize_key(e.key): e.section for e in seed}
    domain_key = _domain_keys(seed)
    run_date = run_date or max((e.date for e in ledger), default="")
    by_key: dict[str, list[LedgerEntry]] = defaultdict(list)
    for e in ledger:
        key = normalize_key(e.key)
        if key not in section_of:
            key = domain_key.get(_domain(e.url), key)
        by_key[key].append(e)

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
            strong_now = [e for e in passes if e.date == run_date and int(e.verdict.split(":")[1]) >= PROMOTE_MIN_SCORE]
            if strong_now:
                best = max(strong_now, key=lambda e: int(e.verdict.split(":")[1]))
                changes.promote.append((key, f"pass rigor {best.verdict.split(':')[1]} on {run_date}", best.url))
                continue
            if len(pass_dates) >= MIN_DISTINCT_DATES and run_date in pass_dates:
                changes.promote.append((key, f"gate passes on {', '.join(pass_dates)}", best.url))
                continue

        if len(fail_dates) >= MIN_DISTINCT_DATES and run_date in fail_dates and section != "caution":
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
    ap.add_argument("--run-date", required=True)
    args = ap.parse_args(argv)
    ch = evaluate(parse_ledger(Path(args.seen).read_text()), parse_seed(Path(args.seed).read_text()), args.run_date)
    print(json.dumps(asdict(ch), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
