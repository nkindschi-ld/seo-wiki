"""Shared parsers for research-scout's ledger (seen.md) and seed list (seed-sources.md)."""
from __future__ import annotations

import re
from dataclasses import dataclass, field

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
VERDICT_RE = re.compile(r"^(pass:[1-5]|reject:g[1-4]|unverified)$")
SEED_SECTIONS = ["curated", "discovered", "caution"]


@dataclass
class LedgerEntry:
    date: str
    verdict: str
    key: str
    title: str
    url: str
    reason: str


@dataclass
class SeedEntry:
    section: str
    key: str
    fields: dict = field(default_factory=dict)


def normalize_key(s: str) -> str:
    s = s.lower().replace("&", "and")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def parse_ledger(text: str) -> list[LedgerEntry]:
    entries = []
    for n, line in enumerate(text.splitlines(), 1):
        if not re.match(r"^\d{4}-\d{2}-\d{2}", line):
            continue
        parts = [p.strip() for p in line.split(" | ")]
        if len(parts) != 6:
            raise ValueError(f"line {n}: expected 6 fields separated by ' | ', got {len(parts)}")
        date, verdict, key, title, url, reason = parts
        if not DATE_RE.match(date):
            raise ValueError(f"line {n}: bad date {date!r}")
        if not VERDICT_RE.match(verdict):
            raise ValueError(f"line {n}: bad verdict {verdict!r}")
        entries.append(LedgerEntry(date, verdict, key, title, url, reason))
    return entries


def _h2_sections(text: str) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    for line in text.splitlines():
        if line.startswith("## "):
            sections.append((line[3:].strip(), []))
        elif sections:
            sections[-1][1].append(line)
    return sections


def section_text(text: str, heading: str) -> str:
    for name, lines in _h2_sections(text):
        if name.lower() == heading.lower():
            return "\n".join(lines).strip()
    return ""


def parse_seed(text: str) -> list[SeedEntry]:
    sections = _h2_sections(text)
    names = [name.lower() for name, _ in sections]
    if [n for n in names if n in SEED_SECTIONS] != SEED_SECTIONS:
        raise ValueError(f"seed list needs H2 sections {SEED_SECTIONS} in order; found {names}")
    entries = []
    for name, lines in sections:
        sec = name.lower()
        if sec not in SEED_SECTIONS:
            continue
        for line in lines:
            if not line.startswith("- key:"):
                continue
            fields = {}
            for part in line[2:].split(" | "):
                k, _, v = part.partition(":")
                fields[k.strip()] = v.strip()
            entries.append(SeedEntry(sec, fields.get("key", ""), fields))
    return entries
