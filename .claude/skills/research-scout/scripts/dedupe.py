"""Match research-scout candidates against wiki sources and the seen.md ledger.

CLI:
  python3 dedupe.py --repo <root> --candidates <in.json> --out <out.json>
      Adds "duplicate_of": "wiki:<slug>" | "seen:<date>" | null to each record.
  python3 dedupe.py --repo <root> --skip-titles <YYYY-MM-DD>
      Prints the title of every wiki source with date_published on or after the date.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import normalize_key, parse_ledger  # noqa: E402

URL_RE = re.compile(r"https?://[^\s)>\]\"'<]+")
ARXIV_RE = re.compile(r"^arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})(?:v\d+)?(?:\.pdf)?$")
ARXIV_TOKEN_RE = re.compile(r"arXiv:\s*(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
CITATION_TITLE_RE = re.compile(r"[\"“]([^\"”]{8,}?)[,.]?[\"”]")
TEXT_ORIGINS = {".md", ".html", ".htm", ".txt"}
TRACKING_PARAMS = {"gclid", "fbclid", "ref", "source", "mkt_tok"}
TRACKING_PREFIXES = ("utm_", "mc_")
TITLE_ONLY_MIN_WORDS = 5


@dataclass
class IndexEntry:
    origin: str
    title: str
    urls: set = field(default_factory=set)
    key: str = ""
    date_published: str = ""


def normalize_url(url: str) -> str:
    url = url.strip().rstrip(".,;")
    if "://" not in url:
        url = "http://" + url
    parts = urlsplit(url)
    host = parts.netloc.lower()
    for prefix in ("www.", "export."):
        if host.startswith(prefix):
            host = host[len(prefix):]
    norm = (host + parts.path).rstrip("/")
    m = ARXIV_RE.match(norm)
    if m:
        return f"arxiv.org/abs/{m.group(1)}"
    query = sorted(
        (k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if k.lower() not in TRACKING_PARAMS and not k.lower().startswith(TRACKING_PREFIXES)
    )
    return f"{norm}?{urlencode(query)}" if query else norm


def normalize_title(title: str) -> str:
    t = (title or "").lower().strip()
    t = re.sub(r"\s*\([^)]*\)\s*$", "", t)
    t = re.sub(r"[^\w\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def _urls_in(text: str) -> set:
    urls = {normalize_url(u) for u in URL_RE.findall(text)}
    urls |= {f"arxiv.org/abs/{m}" for m in ARXIV_TOKEN_RE.findall(text)}
    return urls


def _frontmatter_value(text: str, name: str) -> str:
    m = re.search(rf"^{name}:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def _page_title(text: str) -> str:
    h1 = next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), "")
    if h1:
        return h1
    m = re.search(r"\*\*Citation:\*\*(.*?)(?:\n\s*\n|\Z)", text, re.DOTALL)
    if not m:  # older pages: the citation is the first paragraph after the frontmatter
        body = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.DOTALL).strip()
        m = re.match(r"(.*?)(?:\n\s*\n|\Z)", body, re.DOTALL)
    if m:
        t = CITATION_TITLE_RE.search(" ".join(m.group(1).split()))
        if t:
            return t.group(1).strip()
    return ""


def _origin_texts(repo_root: Path, origin: str) -> list[str]:
    raw = repo_root / origin
    candidates = [raw] if raw.suffix.lower() in TEXT_ORIGINS else [raw.with_suffix(".txt"), raw.with_suffix(".md")]
    return [c.read_text(errors="replace") for c in candidates if c.is_file()]


def build_index(repo_root: Path) -> list[IndexEntry]:
    repo_root = Path(repo_root)
    index = []
    for page in sorted((repo_root / "wiki" / "sources").glob("*.md")):
        text = page.read_text(errors="replace")
        urls = _urls_in(text)
        origin = _frontmatter_value(text, "origin")
        if origin:
            for raw_text in _origin_texts(repo_root, origin):
                urls |= _urls_in(raw_text)
        slug = page.stem
        index.append(IndexEntry(f"wiki:{slug}", _page_title(text), urls,
                                normalize_key(slug.split("-")[0]), _frontmatter_value(text, "date_published")))
    seen = repo_root / "research-digests" / "seen.md"
    if seen.is_file():
        for e in parse_ledger(seen.read_text()):
            index.append(IndexEntry(f"seen:{e.date}", e.title, {normalize_url(e.url)}, normalize_key(e.key)))
    return index


def find_match(index: list[IndexEntry], url, title, publisher_key):
    nurl = normalize_url(url) if url else ""
    if nurl:
        for e in index:
            if nurl in e.urls:
                return e.origin
    ntitle = normalize_title(title or "")
    nkey = normalize_key(publisher_key or "")
    if ntitle:
        long_title = len(ntitle.split()) >= TITLE_ONLY_MIN_WORDS
        for e in index:
            if normalize_title(e.title) == ntitle and (long_title or (nkey and e.key == nkey)):
                return e.origin
    return None


def skip_titles(index: list[IndexEntry], since: str) -> list[str]:
    return [e.title or e.origin[5:] for e in index
            if e.origin.startswith("wiki:") and re.match(r"^\d{4}-\d{2}-\d{2}$", e.date_published)
            and e.date_published >= since]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--candidates")
    ap.add_argument("--out")
    ap.add_argument("--skip-titles", metavar="YYYY-MM-DD")
    args = ap.parse_args(argv)
    index = build_index(Path(args.repo))
    if args.skip_titles:
        print("\n".join(skip_titles(index, args.skip_titles)))
        return 0
    if not args.candidates or not args.out:
        ap.error("--candidates and --out are required unless --skip-titles")
    records = json.loads(Path(args.candidates).read_text())
    for r in records:
        r["duplicate_of"] = find_match(index, r.get("url") or "", r.get("title") or "", r.get("publisher_key") or "")
    Path(args.out).write_text(json.dumps(records, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
