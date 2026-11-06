# Merge Parallel GitHub Wiki Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring every page, source and log entry from the parallel wiki at `github.com/nealkindschi/seo-wiki` (`origin/main`) into the local wiki, then reconcile the claims on each side the way an ingest would.

**Architecture:** The two wikis are **one git history that diverged**, not two separate wikis. They share the root commit `aa0d262`, and the local repo already has the parallel wiki as its `origin` remote. They were merged once before (`d220044`, 2026-09-14, "reconcile 12 conflicts"), and the Lumar checklist was merged again on 2026-09-17 (`fa41c0d`). So this is a `git merge origin/main` with hand-resolved conflicts, plus a semantic reconciliation pass, **not** a re-ingest of each source from scratch. The parallel wiki's sources were already read, discussed and filed in their own sessions; their `raw/` files and `date_ingested:` values carry over unchanged.

**Tech Stack:** git, markdown, Obsidian `[[wikilinks]]`, shell checks (grep/comm).

**Spec:** `CLAUDE.md` (schema, conflict handling, log/timeline formats) and `docs/superpowers/specs/2026-07-07-seo-aeo-llm-wiki-design.md`. Precedent for how conflicts were resolved last time: `git show d220044`.

## What is being merged (measured 2026-11-06)

| | Local (`HEAD` = `claude/chatgpt-retrieval-engines-ingest`) | Parallel (`origin/main`) |
|---|---|---|
| Commits since merge base `fa3822c` (2026-09-14) | 21 | 14 (7 ingest/update commits + PR merges) |
| Files added / modified | 237 A, 44 M, 1 D | 89 A, 23 M |
| New source pages | ~60 | 24 |
| New concept pages | — | 8: `agent-experience-ax`, `ai-answer-volatility`, `ai-mode-response-markup`, `glossary-pages-for-seo`, `grounding-snippets`, `niche-selection-and-validation`, `parametric-memory-vs-grounding`, `query-fanout` |
| New playbook pages | — | 5: `ai-visibility-content-gap-audit`, `ai-visibility-four-layer-diagnostic`, `editorial-link-integration`, `glossary-page-build-checklist`, `niche-validation-playbook` |

Parallel-side commits being brought in: Lumar GEO checklist (already in local via `fa41c0d`), ora "AX is the New AEO", DEJAN link building for AI search, niche research and AI-visibility batch (7), glossary-page SEO batch (4), Detailed AI answer-volatility study, house rule "title tag and H1 never identical" (in `seo-copywriting`), DEJAN AI multi-topic batch (10).

**Collision checks already run:** no path was added on both sides; none of the 24 parallel source slugs or publishers (DEJAN, Detailed, HubSpot, ora, Gekhman, Airfleet, Goodspeed, Surnex, Diggity) already exists locally as a source, so no source is duplicated. Semrush exists on both sides, but as different articles. None of the 13 new concept/playbook slugs collides with a local slug.

**Dry-run merge (`git merge-tree`): 14 conflicted files, 29 hunks:**

| File | Hunks |
|---|---|
| `wiki/concepts/ai-citation-landscape.md` | 6 |
| `wiki/index.md` | 4 |
| `wiki/concepts/agentic-web-optimization.md`, `generative-engine-optimization.md` | 2 each |
| `wiki/playbooks/geo-content-optimization-tactics.md`, `geo-diagnostic-checklist.md`, `seo-reporting.md` | 2 each |
| `wiki/concepts/ai-overview-grounding-and-fidelity.md`, `ai-visibility-correlation-factors.md`, `listicles-in-ai-search.md`, `robots-txt-strategy.md` | 1 each |
| `wiki/playbooks/optimizing-for-the-agentic-web.md`, `wiki/log.md`, `wiki/timeline.md` | 1 each |

## Global Constraints

- Never edit files in `raw/`. Parallel-side `raw/` files come in through the merge byte-for-byte.
- Links are `[[wikilinks]]` only, never relative markdown paths.
- Conflicts are resolved as a **union or a reconciled rewrite, never by taking one side** (the `d220044` precedent). No claim from either history is dropped.
- Contradicting claims go in one **Conflicting Evidence** section per page, using the exact format in `CLAUDE.md`. Never silently overwrite.
- `updated:` frontmatter conflicts: keep the later date. After a real content edit in Task 3, set it to `2026-11-06`.
- `log.md` and `timeline.md` are append-only. Merge them as a union, with no entry dropped or reworded.
- Commit attribution: end commit messages with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Don't push to either remote until the user picks the target in Task 5.

## Review Focus

1. **Git eats a heading:** when both sides add a section at the same spot, the conflict hunk can swallow a `##` heading or leave two `## Conflicting Evidence` headings. Expect exactly one per page; Task 2's duplicate-heading check pins this.
2. **Index entries both sides rewrote:** a union that keeps both lines for one slug gives a doubled index row. Expect one row per slug, carrying both descriptions; Task 2's index check pins this.
3. **Textual merges that are semantically wrong:** files git merged cleanly (e.g. `seo-copywriting.md` getting the title≠H1 house rule) may now contradict local claims elsewhere. Expect them to be surfaced as conflicts, not left silent; Task 3's pairing review covers this.
4. **Each side blind to the other's new pages:** local pages discuss query fan-out in 18 concept/playbook pages but can't link `[[query-fanout]]`, because it didn't exist locally. Expect the new hubs to get inbound links; Task 4's orphan check pins this.
5. **Timeline entries for parallel-side sources lost in the union:** expect every parallel-side source with a real-world date to keep its `timeline.md` entry; Task 2's count check pins this.

---

### Task 1: Pre-flight and start the merge

**Files:** none modified yet (git state only)

**Interfaces:**
- Produces: branch `claude/merge-parallel-wiki-2026-11` with an in-progress merge of `origin/main`, and the 14 conflicted files above.

- [ ] **Step 1: Confirm a clean tree and fresh remotes**

Run: `git status --porcelain && git fetch origin && git fetch ld`
Expected: no output from status; fetch succeeds.

- [ ] **Step 2: Re-measure divergence, in case either side moved since this plan**

Run: `git rev-list --left-right --count HEAD...origin/main`
Expected: `21	14`. If the counts differ, re-run the dry-run (`git merge-tree --write-tree --name-only HEAD origin/main`) and update the conflict table before going on.

- [ ] **Step 3: Branch from the current local tip (it has 8 commits not yet on `ld`)**

Run: `git switch -c claude/merge-parallel-wiki-2026-11`

- [ ] **Step 4: Start the merge without committing**

Run: `git merge --no-commit --no-ff origin/main`
Expected: "Automatic merge failed" listing exactly the 14 files in the table.

### Task 2: Resolve the mechanical conflicts (`log.md`, `timeline.md`, `index.md`)

**Files:**
- Modify: `wiki/log.md`, `wiki/timeline.md`, `wiki/index.md`

**Interfaces:**
- Consumes: the in-progress merge from Task 1.
- Produces: the three files with no conflict markers, which Tasks 3 and 4 append to.

- [ ] **Step 1: `log.md`: union the two sides' entry blocks**

An entry block runs from one `## [` heading to the next. Interleave the two sides' blocks by the date in the heading. Within the same date, local blocks go first. Don't change any text.

- [ ] **Step 2: `timeline.md`: union the same way, keyed on the `## YYYY-MM-DD` event date**

Neither file is strictly sorted today (both have disorder from earlier merges). Only the conflicted hunk gets interleaved; don't re-sort the rest of the file.

- [ ] **Step 3: `index.md`: union entries per section (concepts, playbooks, sources)**

For a slug both sides edited, write one row that carries both descriptions.

- [ ] **Step 4: Verify**

```bash
grep -c '^<<<<<<<\|^>>>>>>>\|^=======$' wiki/log.md wiki/timeline.md wiki/index.md   # expect 0 for each
grep -oE '^\- \[\[[^]]+' wiki/index.md | sort | uniq -d                               # expect no output
# every parallel-side log/timeline heading survived:
git show origin/main:wiki/log.md      | grep '^## \[' | sort > /tmp/o; grep '^## \[' wiki/log.md      | sort | comm -23 /tmp/o -   # expect no output
git show origin/main:wiki/timeline.md | grep '^## [0-9]' | sort > /tmp/o; grep '^## [0-9]' wiki/timeline.md | sort | comm -23 /tmp/o -   # expect no output
# and every local one:
git show HEAD:wiki/log.md             | grep '^## \[' | sort > /tmp/o; grep '^## \[' wiki/log.md      | sort | comm -23 /tmp/o -   # expect no output
```

Adjust the index-row regex to the index's actual bullet format if it differs. Run the same local-side check for `timeline.md`.

### Task 3: Resolve the 11 concept and playbook conflicts

**Files:**
- Modify: the 7 concept and 4 playbook files in the conflict table.

**Interfaces:**
- Consumes: Task 2's resolved `index.md` (one row per slug).
- Produces: merged pages. Each Conflicting Evidence bullet added here becomes one `conflict` log entry in Task 5.

- [ ] **Step 1: Resolve each file as a union**

Keep both sides' new sections and citations. Restore any heading the hunk swallowed. Collapse duplicate `## Conflicting Evidence` headings into one section, keeping every bullet. For `updated:`, keep the later date.

- [ ] **Step 2: Where the two sides make incompatible claims in the same hunk, write a Conflicting Evidence bullet**

Use the `CLAUDE.md` format, citing the source on each side and its date. Give a "Current best guess" and flag it unresolved. Keep a list of these for the user.

- [ ] **Step 3: Verify each file**

```bash
F="wiki/concepts/agentic-web-optimization.md wiki/concepts/ai-citation-landscape.md wiki/concepts/ai-overview-grounding-and-fidelity.md wiki/concepts/ai-visibility-correlation-factors.md wiki/concepts/generative-engine-optimization.md wiki/concepts/listicles-in-ai-search.md wiki/concepts/robots-txt-strategy.md wiki/playbooks/geo-content-optimization-tactics.md wiki/playbooks/geo-diagnostic-checklist.md wiki/playbooks/optimizing-for-the-agentic-web.md wiki/playbooks/seo-reporting.md"
grep -l '^<<<<<<<\|^>>>>>>>\|^=======$' $F                       # expect no output
for f in $F; do grep '^## ' $f | sort | uniq -d | sed "s|^|$f: |"; done   # expect no output (no duplicate H2s)
for f in $F; do head -1 $f | grep -qx -- '---' || echo "bad frontmatter: $f"; done   # expect no output
# no citation lost: every [[link]] either side had is still present
for f in $F; do for side in HEAD origin/main; do git show $side:$f | grep -oE '\[\[[^]|#]+' | sort -u | comm -23 - <(grep -oE '\[\[[^]|#]+' $f | sort -u) | sed "s|^|$f lost from $side: |"; done; done   # expect no output
```

- [ ] **Step 4: Commit the merge**

```bash
git add -A
git commit -m "Merge origin/main: bring in parallel wiki (24 sources, 8 concepts, 5 playbooks)"
```

Write the message body like `d220044`'s: say how each file class was resolved and list any Conflicting Evidence bullets added.

### Task 4: Reconcile what each side has never seen

The textual merge only reconciles lines both sides touched. The parallel side's 24 sources were never checked against local's ~60 new sources, or the reverse. This task is the ingest workflow's conflict-handling step, run across the two sides.

**Files:**
- Modify: pages in the pairing table below, `wiki/index.md` (if rows change)

**Interfaces:**
- Consumes: the merge commit from Task 3.
- Produces: cross-links and Conflicting Evidence bullets. A list of conflicts for the user goes to Task 5.

**Topic pairings to review** (parallel-side new page ↔ local pages covering the same ground):

| Parallel-side page | Local pages to check against |
|---|---|
| `query-fanout`, `parametric-memory-vs-grounding`, `grounding-snippets` | `ai-search-reranking-pipeline`, `chunkability`, `lexical-ranking-tf-idf-bm25`, `topical-authority-in-ai-search`, `ai-overview-grounding-and-fidelity` (local mentions fan-out in 18 concept/playbook pages) |
| `ai-answer-volatility` (Detailed study) | `ai-visibility-measurement-methodology`, `seo-aeo-geo-search-demand-trends`, `aio-ctr-impact` |
| `agent-experience-ax`, `ai-mode-response-markup` | `agentic-web-optimization`, `structured-data-and-ai-search`, local llms.txt and Markdown-for-agents pages |
| `ai-visibility-content-gap-audit`, `ai-visibility-four-layer-diagnostic` | `ai-visibility-measurement-methodology`, `geo-diagnostic-checklist`, local Lumar GEO series parts 2–5 sources |
| `editorial-link-integration`, DEJAN link building | `link-building`, `link-and-anchor-text-best-practices`, local `semrush-digital-pr`, `semrush-broken-link-building` |
| `glossary-pages-for-seo`, `niche-*` | `topic-cluster-strategy`, `keyword-research`, local SaaS SEO pages |
| title≠H1 house rule in `seo-copywriting` | local title/meta guidance in any concept or playbook |

- [ ] **Step 1: For each pairing, read both sides and decide whether they agree, extend or conflict**

Agree/extend: add a supporting citation and cross-`[[link]]` in both directions, and bump `updated:`. Conflict: add a Conflicting Evidence bullet. Never rewrite the older claim away.

- [ ] **Step 2: Present the conflicts to the user before committing them**

`CLAUDE.md` says conflicts are surfaced, not quietly resolved. Show each one with the proposed "current best guess" and wait for their go-ahead.

- [ ] **Step 3: Run the structural lint**

```bash
ls wiki/concepts wiki/playbooks wiki/sources | sed 's/\.md$//' | sort -u > /tmp/pages
# broken links (the 5 names below are pre-existing literal examples in log/CLAUDE text, not real links)
grep -rhoE '\[\[[^]|#]+' wiki | sed 's/\[\[//' | sort -u | comm -23 - /tmp/pages | grep -vxE 'index|log|timeline|concept-slug|source-slug|wikilink|wiki/index.md|wiki/timeline.md'   # expect no output
# orphans: pages with no inbound link from any other page
for p in $(cat /tmp/pages); do n=$(grep -rlF "[[$p" wiki --include=*.md | grep -v "/$p.md$" | wc -l); [ $n -eq 0 ] && echo "orphan: $p"; done   # expect no output
# index completeness
for p in $(cat /tmp/pages); do grep -qF "[[$p" wiki/index.md || echo "not in index: $p"; done   # expect no output
# no relative-path links crept in
grep -rnE '\]\((\.\./|\./)?[a-z-]+\.md\)' wiki   # expect no output
```

- [ ] **Step 4: Commit**

```bash
git add wiki
git commit -m "Reconcile merged wiki: cross-link parallel-side hubs, record cross-side conflicts"
```

### Task 5: Log, push and retire the fork

**Files:**
- Modify: `wiki/log.md`

- [ ] **Step 1: Append log entries**

Add one `## [2026-11-06] lint | Merge parallel wiki (origin/main): <N> files reconciled, <M> cross-side conflicts` entry, plus one `## [2026-11-06] conflict | <topic> — <line>` per conflict approved in Task 4. Commit.

- [ ] **Step 2: User decides the canonical remote**

Right now `origin` = `nealkindschi/seo-wiki` (personal; the parallel wiki) and `ld` = `nkindschi-ld/seo-wiki` (work; what this checkout tracks). Options: push the branch to `ld` and open a PR there; also push to `origin` and open a PR so both stay in sync; or make one canonical and archive the other. The fork has diverged twice now (September and November), so picking one canonical repo is what keeps this from happening again.

- [ ] **Step 3: Push and open the PR(s) on the chosen remote(s); bind with `ccd_pr`**
