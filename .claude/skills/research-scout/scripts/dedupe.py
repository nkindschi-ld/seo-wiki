"""Match research-scout candidates against wiki sources and the seen.md ledger.

CLI: python3 dedupe.py --repo <root> --candidates <in.json> --out <out.json>
Adds "duplicate_of": "wiki:<slug>" | "seen:<date>" | null to each record.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import normalize_key, parse_ledger  # noqa: E402

URL_RE = re.compile(r"https?://[^\s)>\]\"'<]+")
ARXIV_RE = re.compile(r"^arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?$")
TEXT_ORIGINS = {".md", ".html", ".htm", ".txt"}


@dataclass
class IndexEntry:
    origin: str
    title: str
    urls: set = field(default_factory=set)
    key: str = ""


def normalize_url(url: str) -> str:
    url = url.strip().rstrip(".,;")
    if "://" not in url:
        url = "http://" + url
    parts = urlsplit(url)
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    norm = (host + parts.path).rstrip("/")
    m = ARXIV_RE.match(norm)
    if m:
        return f"arxiv.org/abs/{m.group(1)}"
    return norm


def normalize_title(title: str) -> str:
    t = title.lower().strip()
    t = re.sub(r"\s*\([^)]*\)\s*$", "", t)
    t = re.sub(r"[^\w\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def _urls_in(text: str) -> set:
    return {normalize_url(u) for u in URL_RE.findall(text)}


def _frontmatter_value(text: str, name: str) -> str:
    m = re.search(rf"^{name}:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def build_index(repo_root: Path) -> list[IndexEntry]:
    repo_root = Path(repo_root)
    index = []
    for page in sorted((repo_root / "wiki" / "sources").glob("*.md")):
        text = page.read_text(errors="replace")
        h1 = next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), "")
        urls = _urls_in(text)
        origin = _frontmatter_value(text, "origin")
        if origin:
            raw = repo_root / origin
            if raw.suffix.lower() in TEXT_ORIGINS and raw.is_file():
                urls |= _urls_in(raw.read_text(errors="replace"))
        slug = page.stem
        index.append(IndexEntry(f"wiki:{slug}", h1, urls, normalize_key(slug.split("-")[0])))
    seen = repo_root / "research-digests" / "seen.md"
    if seen.is_file():
        for e in parse_ledger(seen.read_text()):
            index.append(IndexEntry(f"seen:{e.date}", e.title, {normalize_url(e.url)}, normalize_key(e.key)))
    return index


def find_match(index: list[IndexEntry], url: str, title: str, publisher_key: str):
    nurl = normalize_url(url) if url else ""
    if nurl:
        for e in index:
            if nurl in e.urls:
                return e.origin
    ntitle = normalize_title(title)
    nkey = normalize_key(publisher_key)
    if ntitle and nkey:
        for e in index:
            if e.key == nkey and normalize_title(e.title) == ntitle:
                return e.origin
    return None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--candidates", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    index = build_index(Path(args.repo))
    records = json.loads(Path(args.candidates).read_text())
    for r in records:
        r["duplicate_of"] = find_match(index, r.get("url", ""), r.get("title", ""), r.get("publisher_key", ""))
    Path(args.out).write_text(json.dumps(records, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
