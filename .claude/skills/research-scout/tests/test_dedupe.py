import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))

from common import parse_ledger  # noqa: E402
from dedupe import build_index, find_match, normalize_url  # noqa: E402

FIXTURE = HERE / "fixtures" / "repo"


class DedupeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.idx = build_index(FIXTURE)

    def test_url_variants_match(self):
        a = normalize_url("https://www.ahrefs.com/blog/why-chatgpt-cites-pages/?utm_source=x#top")
        b = normalize_url("http://ahrefs.com/blog/why-chatgpt-cites-pages")
        c = normalize_url("https://ahrefs.com/blog/why-chatgpt-cites-pages/")
        self.assertEqual(a, b)
        self.assertEqual(b, c)

    def test_arxiv_variants_match(self):
        for u in (
            "https://arxiv.org/abs/2601.01234",
            "https://arxiv.org/abs/2601.01234v2",
            "https://arxiv.org/pdf/2601.01234v1.pdf",
        ):
            self.assertEqual(normalize_url(u), "arxiv.org/abs/2601.01234", u)

    def test_match_url_in_wiki_page(self):
        self.assertEqual(
            find_match(self.idx, "https://ahrefs.com/blog/why-chatgpt-cites-pages", "x", "ahrefs"),
            "wiki:ahrefs-why-chatgpt-cites-pages-2026",
        )

    def test_match_url_in_raw_origin(self):
        self.assertEqual(
            find_match(self.idx, "https://arxiv.org/pdf/2601.01234v3", "whatever", "someone"),
            "wiki:no-url-in-page-2026",
        )

    def test_match_title_and_key_without_url(self):
        title = "Why ChatGPT cites one page over another"
        self.assertEqual(
            find_match(self.idx, "https://other.example/x", title, "ahrefs"),
            "wiki:ahrefs-why-chatgpt-cites-pages-2026",
        )
        self.assertIsNone(find_match(self.idx, "https://other.example/x", title, "semrush"))

    def test_match_seen_ledger(self):
        self.assertEqual(
            find_match(self.idx, "https://thedigitalbloom.com/report/", "t", "k"),
            "seen:2026-11-02",
        )

    def test_pdf_origin_does_not_crash(self):
        entries = [e for e in self.idx if e.origin == "wiki:pdf-origin-2026"]
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].urls, set())

    def test_cli_annotates_candidates(self):
        records = [
            {"title": "x", "url": "https://ahrefs.com/blog/why-chatgpt-cites-pages/", "publisher_key": "ahrefs"},
            {"title": "Brand new study", "url": "https://new.example/study", "publisher_key": "newlab"},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            inp = Path(tmp) / "in.json"
            out = Path(tmp) / "out.json"
            inp.write_text(json.dumps(records))
            subprocess.run(
                [sys.executable, str(SCRIPTS / "dedupe.py"), "--repo", str(FIXTURE),
                 "--candidates", str(inp), "--out", str(out)],
                check=True,
            )
            result = json.loads(out.read_text())
        self.assertEqual(result[0]["duplicate_of"], "wiki:ahrefs-why-chatgpt-cites-pages-2026")
        self.assertIsNone(result[1]["duplicate_of"])
        self.assertEqual(result[1]["title"], "Brand new study")

    def test_parse_ledger_rejects_bad_verdict(self):
        with self.assertRaises(ValueError):
            parse_ledger("2026-11-02 | maybe | k | t | u | r")


if __name__ == "__main__":
    unittest.main()
