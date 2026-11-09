# Research Scout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A project skill that, once a week, finds recent credible SEO/AEO/GEO/AI-search/LLM-retrieval studies, vets their methodology, and writes a ranked digest with links into `research-digests/`, without touching `wiki/` or `raw/`.

**Architecture:** `.claude/skills/research-scout/SKILL.md` orchestrates three parallel lane subagents (academic, industry, practitioner) that return JSON candidate records; the main agent judges them. The deterministic parts are small stdlib-Python scripts with unittest tests: duplicate matching (`dedupe.py`), seed-list promotion and caution counting (`seed_rules.py`), and a post-run output validator (`check_run.py`). The judgment parts (gate, rigor score, wiki fit) live in markdown (`rubric.md`, `lanes.md`). A local scheduled task runs the skill on Mondays at 11:00 a.m.

**Tech Stack:** Claude Code project skill (markdown), Python 3.9 stdlib only (no pytest; tests use `unittest`), git (read-only at run time), Claude desktop scheduled tasks.

**Spec:** `docs/superpowers/specs/2026-11-09-research-scout-design.md`

## Global Constraints

- The agent never edits `wiki/` or `raw/`.
- At run time the agent changes only `research-digests/YYYY-MM-DD.md`, `research-digests/seen.md`, `.claude/skills/research-scout/seed-sources.md`, and the gitignored `research-digests/.work/`.
- No state-changing git commands at run time: no commit, switch, stash, reset, restore or push.
- Default search window: **last 14 days**; a run argument `window=<days>` overrides it (60 for testing).
- Each lane returns **at most 8** records.
- Hard gate: all four criteria (primary research; stated methodology; identifiable, credible author; in scope and new).
- Rigor score is 1–5, gate passes only. Every entry carries a conflict-of-interest note ("none apparent" is valid).
- Promote to Discovered: one pass with rigor **≥ 4**, or passes on **2 distinct run dates**. Move to Caution: gate-1/2/3 rejections on **2 distinct run dates**. Curated is never edited by the agent; a Curated source meeting the caution rule is flagged in the digest instead. `unverified` never counts toward promotion.
- Schedule: local scheduled task `seo-research-scout`, cron `0 11 * * 1` (Mondays 11:00 a.m. local), enabled only after Task 6 passes.
- Python 3.9 stdlib only. Run the tests with `python3 -m unittest discover -s .claude/skills/research-scout/tests -v` from the repo root.

**Spec refinements this plan pins down** (gaps the spec left open; no change to behavior):
- Ledger verdict values are `pass:<1-5>`, `reject:g<1-4>` (which gate criterion failed) and `unverified`. Recording the score and the failed criterion makes the seed rules computable. `reject:g4` (out of scope, out of window, or already in the wiki) never counts toward Caution.
- Ledger publisher field is a **key**: the seed-list key if the source is listed, otherwise a lowercase hyphenated slug of the organization or lead author.
- A second run on the same date writes `YYYY-MM-DD-2.md` (then `-3`, …). Seed rules count distinct dates, so a same-day rerun never counts as a second run.

## Review Focus

1. **The same publisher under two keys across weeks** ("Search Engine Land" vs `search-engine-land`). The seed rules should still count them together. Pinned in Task 2 (`test_keys_normalize_across_spellings`).
2. **One study at several URL variants** (utm params, `http`/`https`, `www.`, trailing slash, arXiv `abs` vs `pdf` vs `v2`). It should be recognized as a duplicate. Pinned in Task 1 (`test_url_variants_match`, `test_arxiv_variants_match`).
3. **The user has uncommitted edits when the run starts**, elsewhere in the repo or in Curated. The run shouldn't fail validation or be blamed for the user's changes. Pinned in Task 3 (`test_preexisting_dirty_files_allowed`, `test_curated_compared_to_snapshot_not_head`).
4. **Two runs on the same day** (a manual run plus the scheduled one). The second shouldn't overwrite the first digest or double-count toward promotion. Pinned in Task 2 (`test_same_day_passes_do_not_promote`) and Task 3 (`test_suffixed_digest_name_accepted`).
5. **A quiet week with zero candidates.** It should still produce a valid digest. Pinned in Task 3 (`test_empty_week_digest_valid`).

---

## File structure

```
.claude/skills/research-scout/
  SKILL.md                 # Task 5 — orchestrator
  lanes.md                 # Task 4 — lane briefs, topic scope, record schema
  rubric.md                # Task 4 — gate, rigor score, COI note
  seed-sources.md          # Task 4 — Curated / Discovered / Caution
  scripts/
    common.py              # Task 1 — shared parsers for seen.md and seed-sources.md
    dedupe.py              # Task 1
    seed_rules.py          # Task 2
    check_run.py           # Task 3
  tests/
    fixtures/repo/         # Task 1 — tiny fake repo (wiki/sources, raw, research-digests)
    test_dedupe.py         # Task 1
    test_seed_rules.py     # Task 2
    test_check_run.py      # Task 3
research-digests/
  seen.md                  # Task 4 — header only
  .work/                   # gitignored scratch per run (Task 1 adds to .gitignore)
```

### Shared formats (used by Tasks 1–5)

**`seen.md` line** (one per candidate, below a header):
```
YYYY-MM-DD | <verdict> | <publisher-key> | <title> | <url> | <reason>
```
`<verdict>` matches `pass:[1-5]`, `reject:g[1-4]` or `unverified`. Lines not starting with a date are ignored (header and comments).

**`seed-sources.md`:** three H2 sections in this order: `## Curated`, `## Discovered`, `## Caution`. Curated has H3 lane subsections (`### Academic`, `### Industry research`, `### Practitioner`). Entry lines:
```
- key: <key> | name: <display name> | url: <url> | note: <text>                                   (Curated)
- key: <key> | name: <name> | lane: <academic|industry|practitioner> | added: YYYY-MM-DD | evidence: <url>   (Discovered)
- key: <key> | name: <name> | added: YYYY-MM-DD | reason: <text>                                 (Caution)
```

**Lane record** (JSON object; lanes return a JSON array of them):
```json
{"title": "", "url": "", "publisher_key": "", "publisher_name": "", "authors": [""],
 "date_published": "YYYY-MM-DD", "study_type": "", "method": "", "sample_size": "",
 "study_period": "", "key_findings": [""], "coi": "", "lane": "academic|industry|practitioner",
 "lane_verdict": "pass|reject|unverified", "lane_reason": ""}
```

---

### Task 1: Scaffold + shared parsers + duplicate matching

**Files:**
- Create: `.claude/skills/research-scout/scripts/common.py`, `.claude/skills/research-scout/scripts/dedupe.py`
- Create: `.claude/skills/research-scout/tests/test_dedupe.py`, `.claude/skills/research-scout/tests/fixtures/repo/…`
- Modify: `.gitignore` (append `research-digests/.work/`)

**Interfaces:**
- Produces (`common.py`):
  - `LedgerEntry` dataclass: `date: str, verdict: str, key: str, title: str, url: str, reason: str`
  - `parse_ledger(text: str) -> list[LedgerEntry]`: raises `ValueError(f"line {n}: …")` on a dated line with the wrong field count or an invalid verdict
  - `SeedEntry` dataclass: `section: str ("curated"|"discovered"|"caution"), key: str, fields: dict[str, str]`
  - `parse_seed(text: str) -> list[SeedEntry]`: raises `ValueError` if the three H2 sections are missing or out of order
  - `section_text(text: str, heading: str) -> str`: raw text of one H2 section (used for the Curated snapshot)
  - `normalize_key(s: str) -> str`: lowercase; `&`→`and`; non-alphanumerics → `-`; collapse and strip `-`
- Produces (`dedupe.py`):
  - `normalize_url(url: str) -> str`
  - `normalize_title(title: str) -> str`: lowercase, strip punctuation, collapse whitespace, drop a trailing `(…)` parenthetical
  - `IndexEntry` dataclass: `origin: str ("wiki:<slug>"|"seen:<date>"), title: str, urls: set[str], key: str`
  - `build_index(repo_root: Path) -> list[IndexEntry]`
  - `find_match(index, url: str, title: str, publisher_key: str) -> str | None`: returns the matching entry's `origin`
  - CLI: `python3 dedupe.py --repo <root> --candidates <in.json> --out <out.json>` copies each record and adds `"duplicate_of": <origin or null>`

- [ ] **Step 1: Build the fixture repo** at `tests/fixtures/repo/`:
  - `wiki/sources/ahrefs-why-chatgpt-cites-pages-2026.md`: H1 `# Why ChatGPT Cites One Page Over Another (Ahrefs)`, body contains `https://ahrefs.com/blog/why-chatgpt-cites-pages/`
  - `wiki/sources/no-url-in-page-2026.md`: H1 `# Measuring Google AI Overviews`, `origin: raw/studies/no-url-in-page-2026.md`, no URL in the page
  - `raw/studies/no-url-in-page-2026.md`: contains `https://arxiv.org/abs/2601.01234`
  - `wiki/sources/pdf-origin-2026.md`: H1 `# A PDF Study`, `origin: raw/studies/pdf-origin-2026.pdf` (the PDF file is absent; the indexer must not crash)
  - `research-digests/seen.md`: header line plus `2026-11-02 | reject:g1 | thedigitalbloom | AI Citation Report | https://thedigitalbloom.com/report | g1: secondary aggregation`

- [ ] **Step 2: Write failing tests** in `tests/test_dedupe.py` (add `scripts/` to `sys.path`):
  - `test_url_variants_match`: `normalize_url` gives equal results for `https://www.ahrefs.com/blog/why-chatgpt-cites-pages/?utm_source=x#top`, `http://ahrefs.com/blog/why-chatgpt-cites-pages` and `https://ahrefs.com/blog/why-chatgpt-cites-pages/`
  - `test_arxiv_variants_match`: `arxiv.org/abs/2601.01234`, `arxiv.org/abs/2601.01234v2` and `arxiv.org/pdf/2601.01234v1.pdf` all normalize to `arxiv.org/abs/2601.01234`
  - `test_match_url_in_wiki_page`: `find_match(idx, "https://ahrefs.com/blog/why-chatgpt-cites-pages", "x", "ahrefs") == "wiki:ahrefs-why-chatgpt-cites-pages-2026"`
  - `test_match_url_in_raw_origin`: an arXiv pdf URL matches `"wiki:no-url-in-page-2026"`
  - `test_match_title_and_key_without_url`: `find_match(idx, "https://other.example/x", "Why ChatGPT cites one page over another", "ahrefs")` matches. The same title with key `"semrush"` returns `None` (title alone is not enough).
  - `test_match_seen_ledger`: the thedigitalbloom URL returns `"seen:2026-11-02"`
  - `test_pdf_origin_does_not_crash`: `build_index` includes `wiki:pdf-origin-2026` with an empty `urls`
  - `test_cli_annotates_candidates`: write two records to a temp JSON, run the CLI via `subprocess`, and assert one gets `duplicate_of` set and the other gets `null`
  - `test_parse_ledger_rejects_bad_verdict`: `parse_ledger("2026-11-02 | maybe | k | t | u | r")` raises `ValueError`

- [ ] **Step 3: Run the tests to verify they fail**
  Run: `python3 -m unittest discover -s .claude/skills/research-scout/tests -v`
  Expected: errors with `ModuleNotFoundError: No module named 'dedupe'`

- [ ] **Step 4: Implement `common.py` and `dedupe.py`** with the signatures above. In `normalize_url`, drop the scheme, `www.`, query, fragment and trailing `/`, and lowercase the host. For arXiv, map `abs|pdf/<id>(vN)?(.pdf)?` to `arxiv.org/abs/<id>`. `build_index` reads every `wiki/sources/*.md` (title from the first `# ` line; URLs from the page body, plus the `origin` file when it is `.md`, `.html` or `.txt` and exists), then every dated line of `research-digests/seen.md`. Wiki entries get the key `normalize_key` of the slug's first hyphen segment, which is enough for the title+key fallback because wiki slugs begin with the publisher. `find_match` tries the normalized URL first, then `normalize_title` equality with the same `normalize_key(publisher_key)`.

- [ ] **Step 5: Run the tests to verify they pass**
  Run: `python3 -m unittest discover -s .claude/skills/research-scout/tests -v`
  Expected: all `test_dedupe` tests pass

- [ ] **Step 6: Smoke-test against the real wiki**
  Run: `python3 -c "import sys; sys.path.insert(0,'.claude/skills/research-scout/scripts'); from dedupe import build_index; from pathlib import Path; i=build_index(Path('.')); print(len(i), sum(1 for e in i if e.urls))"`
  Expected: first number ≥ 215; second number ≥ 150 (most sources resolve to at least one URL)

- [ ] **Step 7: Commit**
```bash
git add .gitignore .claude/skills/research-scout/scripts/common.py .claude/skills/research-scout/scripts/dedupe.py .claude/skills/research-scout/tests
git commit -m "Add research-scout duplicate matching with tests"
```

---

### Task 2: Seed-list rules

**Files:**
- Create: `.claude/skills/research-scout/scripts/seed_rules.py`, `.claude/skills/research-scout/tests/test_seed_rules.py`

**Interfaces:**
- Consumes: `parse_ledger`, `parse_seed`, `normalize_key` from `common.py`
- Produces:
  - `Changes` dataclass: `promote: list[tuple[str, str, str]]` (key, reason, evidence_url), `caution: list[tuple[str, str]]` (key, reason; covers unlisted keys and Discovered keys), `flag_curated: list[tuple[str, str]]` (key, reason)
  - `evaluate(ledger: list[LedgerEntry], seed: list[SeedEntry]) -> Changes`
  - CLI: `python3 seed_rules.py --seen <seen.md> --seed <seed-sources.md>` prints `Changes` as JSON

- [ ] **Step 1: Write failing tests** in `tests/test_seed_rules.py`, building ledgers and seeds from inline strings with `parse_ledger` and `parse_seed`:
  - `test_single_pass_rigor4_promotes`: an unlisted `newlab` with one `pass:4` → `promote[0][0] == "newlab"` and evidence equal to that entry's URL
  - `test_single_pass_rigor3_does_not_promote`: one `pass:3` → `promote == []`
  - `test_passes_on_two_dates_promote`: `pass:2` on 2026-11-02 and `pass:3` on 2026-11-09 → promoted
  - `test_same_day_passes_do_not_promote`: two `pass:3` both dated 2026-11-09 → not promoted
  - `test_listed_key_not_promoted`: a key already in Curated or Discovered with `pass:5` → not in `promote`
  - `test_unverified_never_counts`: `unverified` on two dates plus nothing else → no promote, no caution
  - `test_g1_g3_rejects_on_two_dates_caution`: `reject:g1` on 2026-11-02 and `reject:g3` on 2026-11-09 for unlisted `roundupsite` → `caution[0][0] == "roundupsite"`
  - `test_g4_rejects_never_caution`: `reject:g4` on two dates → `caution == []`
  - `test_discovered_moves_to_caution`: a Discovered key meeting the caution rule → in `caution`
  - `test_curated_flagged_not_cautioned`: a Curated key meeting the caution rule → in `flag_curated`, not in `caution`
  - `test_already_caution_not_repeated`: a key already in Caution → in neither list
  - `test_promote_beats_caution`: unlisted key with `pass:4` and `reject:g1` on two dates → in `promote`, not in `caution`
  - `test_keys_normalize_across_spellings`: ledger keys `Search Engine Land` (2026-11-02, `pass:3`) and `search-engine-land` (2026-11-09, `pass:2`) → one promotion, key `search-engine-land`

- [ ] **Step 2: Run the tests to verify they fail**
  Run: `python3 -m unittest discover -s .claude/skills/research-scout/tests -p 'test_seed_rules.py' -v`
  Expected: `ModuleNotFoundError: No module named 'seed_rules'`

- [ ] **Step 3: Implement `seed_rules.py`.** Group the ledger by `normalize_key(key)`. Pass dates are the distinct dates with a `pass:N` verdict; caution dates are the distinct dates with `reject:g1`–`g3`. Look up each key's seed section after `normalize_key`. Promote applies only to unlisted keys; it is checked first and wins over caution. Evidence is the highest-scoring pass's URL (latest date on ties). Reasons are human-readable, e.g. `"pass rigor 4 on 2026-11-09"` or `"gate fails on 2026-11-02, 2026-11-09 (g1, g3)"`.

- [ ] **Step 4: Run the tests to verify they pass**
  Run: `python3 -m unittest discover -s .claude/skills/research-scout/tests -v`
  Expected: all `test_dedupe` and `test_seed_rules` tests pass

- [ ] **Step 5: Commit**
```bash
git add .claude/skills/research-scout/scripts/seed_rules.py .claude/skills/research-scout/tests/test_seed_rules.py
git commit -m "Add research-scout seed-list promotion and caution rules"
```

---

### Task 3: Post-run output validator

**Files:**
- Create: `.claude/skills/research-scout/scripts/check_run.py`, `.claude/skills/research-scout/tests/test_check_run.py`

**Interfaces:**
- Consumes: `parse_ledger`, `parse_seed`, `section_text` from `common.py`
- Produces:
  - `check_digest(text: str, run_date: str) -> list[str]` (error messages; empty means valid)
  - `check_ledger_for_run(ledger_text: str, run_date: str, passed: int, rejected: int, unverified: int) -> list[str]`
  - `check_curated_unchanged(seed_text: str, snapshot_text: str) -> list[str]`
  - `check_git_paths(status_before: str, status_after: str, allowed: list[str]) -> list[str]`: arguments are `git status --porcelain` outputs; any path in `after` that is not in `before`, not in `allowed`, and not under `research-digests/.work/` is an error
  - CLI: `python3 check_run.py --repo <root> --digest <path> --run-date YYYY-MM-DD --work <research-digests/.work/<run-id>>` reads `curated-snapshot.md` and `status-before.txt` from `--work`, runs all checks, prints `OK` and exits 0, or prints one error per line and exits 1

Digest rules enforced by `check_digest`, mirroring the spec's digest format:
- First line `# Research digest — <run_date>`
- A line containing `**Window:**`, `**Passed:** <n>`, `**Rejected:** <n>` and `**Couldn't verify:** <n>`
- A line starting `**Lanes:**` that names `academic`, `industry` and `practitioner`
- H2 sections in order: `## Studies`, `## Couldn't verify`, `## Rejected`, `## Seed list changes`
- Under Studies: exactly `<Passed>` H3 entries, each with the lines `**Link:**` (with an `http` URL), `**Type:**`, `**Rigor:** <1-5>/5`, `**Method:**`, `**Key findings:**`, `**Conflicts of interest:**` and `**Wiki fit:**`. With 0 passed, Studies holds the line `_No studies passed the gate this run._`
- Bullet counts under Couldn't verify and Rejected equal the header counts (a section with 0 holds `_None._`)

- [ ] **Step 1: Write failing tests** in `tests/test_check_run.py`, using a valid sample digest string built in the test (two studies, one rejected, one unverified) as the base and mutating it:
  - `test_valid_digest_passes`: `check_digest(sample, "2026-11-16") == []`
  - `test_missing_wiki_fit_fails`: remove one `**Wiki fit:**` line → an error mentioning `Wiki fit`
  - `test_passed_count_mismatch_fails`: header says 3, two entries → error
  - `test_rigor_out_of_range_fails`: `**Rigor:** 6/5` → error
  - `test_empty_week_digest_valid`: all counts 0 with the `_No studies…_` and `_None._` placeholders → `[]`
  - `test_suffixed_digest_name_accepted`: the CLI accepts `--digest research-digests/2026-11-16-2.md` with `--run-date 2026-11-16`
  - `test_ledger_count_mismatch_fails`: the ledger has 3 lines dated the run date but counts are 2+1+1 → error
  - `test_curated_compared_to_snapshot_not_head`: the seed file's Curated equals the snapshot → `[]`; one changed Curated line → error
  - `test_preexisting_dirty_files_allowed`: `before = " M wiki/index.md"`, `after = " M wiki/index.md\n?? research-digests/2026-11-16.md"`, allowed contains the digest → `[]`
  - `test_new_wiki_change_fails`: `after` adds ` M wiki/concepts/x.md` not present in `before` → error naming that path
  - `test_work_dir_ignored`: `?? research-digests/.work/2026-11-16/x.json` in `after` → `[]`

- [ ] **Step 2: Run the tests to verify they fail**
  Run: `python3 -m unittest discover -s .claude/skills/research-scout/tests -v`
  Expected: `ModuleNotFoundError: No module named 'check_run'`

- [ ] **Step 3: Implement `check_run.py`** with the signatures above. The CLI builds `allowed` as `[<digest path>, "research-digests/seen.md", ".claude/skills/research-scout/seed-sources.md"]`, takes the counts from the digest header for the ledger check, and gets `status_after` from `git -C <repo> status --porcelain` (read-only).

- [ ] **Step 4: Run the tests to verify they pass**
  Run: `python3 -m unittest discover -s .claude/skills/research-scout/tests -v`
  Expected: all tests in all three files pass

- [ ] **Step 5: Commit**
```bash
git add .claude/skills/research-scout/scripts/check_run.py .claude/skills/research-scout/tests/test_check_run.py
git commit -m "Add research-scout run-output validator"
```

---

### Task 4: Rubric, lanes, seed list, empty ledger

**Files:**
- Create: `.claude/skills/research-scout/rubric.md`, `.claude/skills/research-scout/lanes.md`, `.claude/skills/research-scout/seed-sources.md`, `research-digests/seen.md`

**Interfaces:**
- Consumes: the shared formats above; `parse_seed` and `parse_ledger` to validate
- Produces: the files SKILL.md (Task 5) loads and passes to the lanes

- [ ] **Step 1: Write `rubric.md`.** Copy the spec's hard gate (criteria numbered 1–4 so they map to `g1`–`g4`), the rigor-score table, and the conflict-of-interest rule verbatim. Add the ledger verdict values and when to use each. Add two worked examples taken from project memory: thedigitalbloom "AI Citation Position & Revenue Report 2026" → `reject:g1` (secondary aggregation, no original research), and the JISEM MCP-documentation paper → `reject:g2` (no quantitative results).

- [ ] **Step 2: Write `lanes.md`** with:
  - the spec's topic scope, verbatim
  - one section per lane (Academic, Industry research, Practitioner/independent) listing where to search, using the spec's lane definitions plus query patterns (topic terms × "study", "analysis", "we analyzed", "dataset", "methodology"; arXiv listing pages for cs.IR/cs.CL; the seed sources' blog and research URLs)
  - the instruction to read each candidate in full, extract the methodology, apply the gate from `rubric.md`, return **at most 8** records as one fenced JSON array in the lane record format, and use the seed `key` as `publisher_key` when the source is listed
  - the instruction that a candidate whose page or PDF can't be read is returned with `lane_verdict: "unverified"` and the reason, never guessed at

- [ ] **Step 3: Write `seed-sources.md`.** Build it from the wiki's citation counts. Run `ls wiki/sources | sed -E 's/-[0-9]{4}$//; s/\.md$//' | cut -d- -f1 | sort | uniq -c | sort -rn` and list every publisher with ≥ 2 sources in Curated under its lane, using the publisher's research or blog URL. Expected at minimum: semrush, ahrefs, google (Search Central), dejan, search-engine-land, otterly, profound, search-engine-journal, peec, lumar, amplifying, similarweb, ipullrank, zyppy, nngroup, vercel, github, gofishdigital, rankability. Add sparktoro, brightedge, seer-interactive and mintlify under Industry research. Under Academic add arxiv-cs-ir, arxiv-cs-cl, acl-anthology, sigir and the-web-conference. Under Practitioner add named individuals the wiki already cites (check source citation lines with `grep -h "^\*\*Citation:\*\*" -A2 wiki/sources/*.md`). Leave Discovered empty. Caution gets `thedigitalbloom` and `jisem`, with the reasons from memory.

- [ ] **Step 4: Write `research-digests/seen.md`** with a header that explains the line format and verdict values, and no data lines.

- [ ] **Step 5: Validate the formats**
  Run: `python3 -c "import sys; sys.path.insert(0,'.claude/skills/research-scout/scripts'); from common import parse_seed, parse_ledger; s=parse_seed(open('.claude/skills/research-scout/seed-sources.md').read()); print(len(s), sorted({e.section for e in s})); print(len(parse_ledger(open('research-digests/seen.md').read())))"`
  Expected: first line ≥ 25 entries and `['caution', 'curated']`; second line `0`

- [ ] **Step 6: Commit**
```bash
git add .claude/skills/research-scout/rubric.md .claude/skills/research-scout/lanes.md .claude/skills/research-scout/seed-sources.md research-digests/seen.md
git commit -m "Add research-scout rubric, lane briefs, seed sources and ledger"
```

---

### Task 5: Orchestrator skill

**Files:**
- Create: `.claude/skills/research-scout/SKILL.md`

**Interfaces:**
- Consumes: every script CLI (Tasks 1–3) and every content file (Task 4)
- Produces: the entry point the scheduled task invokes; accepts the optional argument `window=<days>`

- [ ] **Step 1: Write `SKILL.md`.** Frontmatter `name: research-scout`, plus a description that triggers on "run research-scout", "weekly research digest" and "find new SEO/AEO studies". The body has the following numbered steps; each step names the exact command or file:
  0. **Set up.** `run_date` = today. Run id = `run_date`, or `run_date-2`, `-3`… if `research-digests/<id>.md` already exists. Create `research-digests/.work/<run-id>/` and save `git status --porcelain` to `status-before.txt` and the Curated section of `seed-sources.md` to `curated-snapshot.md`. Window = `window` argument or 14 days.
  1. **Load context.** Read `rubric.md`, `lanes.md`, `seed-sources.md` and `wiki/index.md`.
  2. **Fan out.** Start three general-purpose subagents **in one message** (parallel). Each prompt contains its lane section from `lanes.md`, the full `rubric.md`, its lane's seed entries plus all Caution entries (labeled), the window dates, and the instruction to return only the fenced JSON array. Save each reply to `.work/<run-id>/lane-<lane>.json`. A lane that errors or returns invalid JSON is recorded as failed, with the reason; the run continues.
  3. **Dedupe.** Merge the lane files into `.work/<run-id>/candidates.json`, then run `python3 .claude/skills/research-scout/scripts/dedupe.py --repo . --candidates … --out .work/<run-id>/deduped.json`. Records with `duplicate_of` starting `seen:` are dropped silently (already logged). Records with `duplicate_of` starting `wiki:` become `reject:g4` with the reason "already in wiki as <slug>". Duplicates across lanes are merged, keeping the more complete record.
  4. **Judge.** For each remaining record, re-apply the `rubric.md` gate (overriding the lane's verdict where needed), verify the authors' credentials with a quick search where they're unfamiliar, give passes a rigor score, and write a wiki-fit line from `wiki/index.md` that names the `[[concept]]` and says agrees, extends or possible conflict.
  5. **Write the ledger.** Append one `seen.md` line per judged record (format in `common.py`).
  6. **Seed rules.** Run `seed_rules.py --seen research-digests/seen.md --seed .claude/skills/research-scout/seed-sources.md`. Apply `promote` (append to Discovered with the lane from the evidence record) and `caution` (append to Caution, removing the key from Discovered if it's there). Never edit Curated; put `flag_curated` items in the digest only.
  7. **Write the digest** to `research-digests/<run-id>.md` in the spec's digest format, with studies ranked by rigor, then wiki value. Include the empty-section placeholders `_No studies passed the gate this run._` and `_None._`.
  8. **Validate.** Run `check_run.py --repo . --digest research-digests/<run-id>.md --run-date <run_date> --work research-digests/.work/<run-id>`. On errors, fix the digest or ledger and rerun until it prints `OK`. If it still fails after 2 fixes, put a `> Validation errors:` block at the top of the digest listing them.
  9. **Hard rules** (stated near the top as well as here): never edit `wiki/` or `raw/`; no state-changing git commands; never push.

- [ ] **Step 2: Check that every referenced path exists**
  Run: `grep -oE '\.claude/skills/research-scout/[A-Za-z_./-]+|scripts/[a-z_]+\.py|[a-z-]+\.md' .claude/skills/research-scout/SKILL.md | sort -u`, then confirm each listed script and content file is present with `ls`.
  Expected: every path resolves; no references to files that don't exist

- [ ] **Step 3: Commit**
```bash
git add .claude/skills/research-scout/SKILL.md
git commit -m "Add research-scout orchestrator skill"
```

---

### Task 6: Backfill dry run, dedupe rerun, tuning

**Files:**
- Modify (tuning only, as needed): `rubric.md`, `lanes.md`, `seed-sources.md` (Curated)
- Produced by the runs (not committed in this task): `research-digests/<date>.md`, `research-digests/seen.md`, `seed-sources.md`

- [ ] **Step 1: Run the skill by hand with `window=60`** in a fresh session in this repo: "Run the research-scout skill with window=60."
  Expected: the run ends with `check_run.py` printing `OK`; `git status` shows changes only to the digest, `seen.md` and possibly `seed-sources.md`

- [ ] **Step 2: Check recall and precision with the user.** Show the digest. Confirm with the user that: studies they know from the last 60 days appear or are correctly rejected; wiki-ingested studies from the window (check `grep date_published wiki/sources/*.md`) appear as `reject:g4` in `seen.md` and never under Studies; and any secondary roundup is rejected under `g1`.
  Expected: the user accepts the result, or names misses to fix

- [ ] **Step 3: Dedupe rerun.** Run the skill again immediately with `window=60`.
  Expected: the new digest is `<date>-2.md`; Passed is 0 or only genuinely new finds; `seed_rules` makes no new promotions from same-day passes

- [ ] **Step 4: Tune** `lanes.md`, `rubric.md` or Curated based on the misses from Step 2, then rerun the test suite.
  Run: `python3 -m unittest discover -s .claude/skills/research-scout/tests -v`
  Expected: all pass

- [ ] **Step 5: Commit the tuning and, if the user wants them kept, the test-run outputs**
```bash
git add .claude/skills/research-scout research-digests
git commit -m "Tune research-scout after backfill dry run"
```

---

### Task 7: Weekly schedule

**Files:** none in the repo. Creates `~/.claude/scheduled-tasks/seo-research-scout/SKILL.md` through the scheduled-tasks tool.

- [ ] **Step 1: Confirm with the user** that Task 6 is accepted and that scheduling should be turned on now.

- [ ] **Step 2: Create the task** with `mcp__scheduled-tasks__create_scheduled_task`:
  - `taskId`: `seo-research-scout`; `title`: `Weekly SEO research digest`
  - `cronExpression`: `0 11 * * 1`
  - `description`: `Find and vet new SEO/AEO/GEO/AI-search studies; write a digest to the SEO Wiki`
  - `prompt` (self-contained): work in `/Users/neal/Claude Code/SEO Wiki`; read and follow `/Users/neal/Claude Code/SEO Wiki/.claude/skills/research-scout/SKILL.md` exactly with the default window; never edit `wiki/` or `raw/`; run no state-changing git commands; finish by reporting the digest path and its summary line.

- [ ] **Step 3: Verify**
  Run: `mcp__scheduled-tasks__list_scheduled_tasks`
  Expected: `seo-research-scout` is enabled, cron `0 11 * * 1`, with `nextRunAt` on the coming Monday at 11:00 local time. Tell the user it runs only while the app is open and catches up on the next launch.
