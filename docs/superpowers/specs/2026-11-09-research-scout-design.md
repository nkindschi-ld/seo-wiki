# Research Scout — Weekly Study Discovery Agent (Design)

**Date:** 2026-11-09
**Status:** Approved in brainstorming; pending spec review

## Purpose

A weekly agent that searches the web for recent, credible studies on SEO,
AEO/GEO, AI search, and LLM retrieval, vets each one's methodology, and
writes a ranked digest with links. The user reviews the digest, clicks
through to the studies, and picks which to ingest using the existing
Ingest workflow in `CLAUDE.md`.

The agent **never edits `wiki/` or `raw/`**. That keeps the wiki's rule to
"discuss key takeaways with the user before filing anything" intact: the
digest feeds ingest, it doesn't replace it.

## Decisions

| Question | Decision |
|---|---|
| How autonomous | Digest only, with a direct link to every study for manual review |
| Where the digest goes | `research-digests/YYYY-MM-DD.md` in this repo, beside `wiki/` (not in the Obsidian vault) |
| Quality bar | Hard gate (all four criteria) plus a 1–5 rigor score; secondary roundups and opinion pieces dropped |
| Where it runs | Local scheduled task in the Claude desktop app, Mondays at 11:00 a.m. local time |
| Architecture | Three parallel lane subagents (search and read), then one judge (dedupe, gate, score, write) |
| Seed list | Updated automatically by the agent under fixed promotion and caution rules |

## Topic scope

SEO; AEO/GEO; AI search and Google AI Overviews/AI Mode; LLM retrieval,
RAG and reranking; AI citation behavior; AI coding-agent tool selection
and instruction files (`agents.md`, `CLAUDE.md`); agentic-web optimization
(making sites usable by AI agents). The last two are standing in-scope
subdomains of this wiki.

## Components

```
.claude/skills/research-scout/
  SKILL.md            # orchestrator: load context → lanes → judge → write (no commit)
  lanes.md            # brief for each of the 3 lane subagents, plus the topic scope
  rubric.md           # hard gate, rigor score, conflict-of-interest note
  seed-sources.md     # trusted publishers/researchers by lane: Curated, Discovered, Caution
research-digests/
  YYYY-MM-DD.md       # one digest per run, named for the run date
  seen.md             # ledger: every candidate ever considered, with verdict and reason
```

- **`SKILL.md`** is the only entry point. The scheduled task's prompt is
  "Run the research-scout skill." The user can also run it by hand.
- **`lanes.md`** defines the three lanes:
  - **Academic:** arXiv (cs.IR, cs.CL), ACL, SIGIR, WWW, and other IR/NLP
    venues; Semantic Scholar.
  - **Industry research:** vendor and research-team publications (Semrush,
    Ahrefs, SparkToro, Profound, BrightEdge, Seer, Similarweb, Mintlify,
    DEJAN, and others on the seed list).
  - **Practitioner/independent:** named individual researchers and
    newsletters, plus open web search on the topic terms.
- **`rubric.md`** holds the scoring rules, so they can be tuned without
  touching the orchestration logic.
- **`seed-sources.md`** starts from the publishers this wiki already cites
  most (Semrush, Ahrefs, Google, DEJAN, Search Engine Land, Otterly,
  Profound, Search Engine Journal, Peec, Lumar, Amplifying, Similarweb,
  iPullRank, Zyppy, NN/g, and others), plus academic venues and known
  independent researchers. Its Caution section starts with
  thedigitalbloom.com (secondary aggregations) and JISEM (low-rigor
  journal), taken from project memory. The seed list is where lanes look
  first; it is not a whitelist. A source not on it can still get into the
  digest by passing the gate.
- **`seen.md`** is the dedupe ledger and also counts gate passes and
  failures for the seed-list rules. One line per candidate:
  `YYYY-MM-DD | verdict (pass/reject/unverified) | publisher | title | URL | reason`.

## Weekly run

1. **Load context.** Read `seed-sources.md`, `rubric.md` and `seen.md`, and
   build a skip list from `wiki/sources/`: each page's slug and title, plus
   any source URL found in the page or in the `raw/` file its `origin`
   names. Dedupe matches on URL first, then on a normalized title plus
   publisher.
2. **Fan out.** Start the three lane subagents in parallel. Each one gets
   its lane brief, the seed sources for its lane (Curated and Discovered,
   with Caution marked), the topic scope, and the URLs to skip (ledger and
   wiki). Each lane:
   - searches for work **published in the last 14 days** (the overlap
     with last week is deliberate, because studies surface late; the
     ledger stops duplicates),
   - reads each promising candidate in full, focusing on the methodology,
   - returns **at most 8** structured records: title, URL, author or
     organization, publish date, study type, method summary, sample size,
     study period, 3–5 key findings with numbers, a conflict-of-interest
     note, and its own gate verdict with reason. A candidate it could not
     read is returned with verdict `unverified` and the reason.
3. **Judge (main agent).** Merge the records; dedupe across lanes, the
   ledger and `wiki/sources/`; check the authors' credentials; apply the
   hard gate; give a rigor score to each study that passes; and, by
   checking `wiki/index.md`, add one line on wiki fit (which concept page
   it would affect, and whether it agrees, extends or conflicts).
4. **Update the seed list** (rules below).
5. **Write.** Create `research-digests/YYYY-MM-DD.md` and append every
   candidate considered (pass, reject, unverified) to `seen.md`.
6. **Don't commit.** The agent leaves its three changed files uncommitted
   in whatever branch is checked out. It never switches branches, so a
   Monday run can't disrupt in-progress work. The user commits the files
   along with their next ingest or on their own.

## Hard gate (all four required)

1. **Primary research.** The author collected or analyzed the data
   themselves. Secondary roundups, listicles of other people's statistics,
   and opinion or prediction posts fail.
2. **Stated methodology.** It states what was measured and how: data
   source, sample size, and study period. Vague sizes ("thousands of
   queries") fail.
3. **Identifiable, credible author.** A named person or organization with
   a track record in the field: earlier published research, a known
   research team, or an academic post. Anonymous content-farm pages fail.
4. **In scope and new.** On-topic, published within the 14-day window, and
   not already in `seen.md` or `wiki/sources/`.

## Rigor score (gate passes only)

| Score | Criteria |
|---|---|
| 5 | Peer-reviewed or preprint with a reproducible method; controlled experiment or large sample; data or code released |
| 4 | Large-sample industry study with full method details (sampling, engines, dates, definitions) and stated limitations |
| 3 | Reasonable sample with a method described, but a key detail missing (prompt selection, engine version) |
| 2 | Small sample or single case study, with the method described |
| 1 | Passes the gate but the method is only just adequate; include it and treat it with caution |

**Conflict-of-interest note:** required on every entry ("none apparent" is
a valid value). It says what the publisher sells and how that could bias
the result. Vendor studies are not penalized in the score.

## Seed-list maintenance

`seed-sources.md` has three sections:

- **Curated:** the user's entries. The agent never edits or removes them.
- **Discovered:** maintained by the agent. A publisher or researcher not
  yet on the list is added when one of its studies passes the gate with a
  **rigor score of 4 or higher**, or when its studies pass the gate in
  **two separate runs** (counted from `seen.md`). Each entry records its
  lane, the date added, and the URL of the study that earned the spot.
- **Caution:** sources whose candidates failed the gate in **two separate
  runs**, each with the reason. Lanes still see these sources but treat
  them skeptically. A Curated source is never moved to Caution
  automatically; the digest flags it for the user instead.

Sources whose studies were `unverified` are never promoted. Every change
is listed in the digest's **Seed list changes** section and shows up as an
uncommitted diff to `seed-sources.md`, so the user can review it, or
revert it with `git restore`, before committing. The user makes a Discovered
entry permanent by moving it to Curated, and removes one by deleting it.

## Digest format

```markdown
# Research digest — YYYY-MM-DD

**Window:** YYYY-MM-DD to YYYY-MM-DD · **Passed:** N · **Rejected:** N · **Couldn't verify:** N
**Lanes:** academic ✓ · industry ✓ · practitioner ✗ (reason)

## Studies

### 1. <Title> — <Organization> (<Author>), YYYY-MM-DD
**Link:** <URL> · **Type:** <study type> · **Rigor:** 4/5
**Method:** <data source, sample size, period, approach>
**Key findings:** • … • … • …
**Conflicts of interest:** <note>
**Wiki fit:** extends [[concept]]; possible conflict with [[concept]] on <claim>

## Couldn't verify
- <Title> — <URL> — <reason, e.g. gated PDF>

## Rejected
- <Title> — <URL> — <failed gate criterion>

## Seed list changes
- Added to Discovered: <source> (<lane>) — <reason, study URL>
- Moved to Caution: <source> — <reason>
```

Studies are ranked by rigor score, then by how much they would add to the
wiki. When nothing passes, the digest is still written, with the summary
line and the Rejected and Couldn't-verify lists, so a quiet week is
distinguishable from a failed run.

## Error handling

- **A lane fails or returns nothing:** the judge continues with the other
  lanes; the summary line names the failed lane and the reason.
- **A page can't be fetched** (paywall, gated PDF, blocked): the candidate
  is listed under Couldn't verify with its URL and reason, and is logged
  in `seen.md` as `unverified`. It is not retried automatically.
- **Git:** the agent runs no git commands that change state (no commit,
  switch, stash, reset, restore or push). It only writes its three files.
- **Unreviewed digests pile up:** if earlier digests are still uncommitted,
  the new run still writes normally; `seen.md` keeps dedupe correct either
  way.
- **Run-level failure:** shown in the scheduled task's run history.

## Scheduling

Local scheduled task `seo-research-scout`, working directory
`~/Claude Code/SEO Wiki`, **Mondays 11:00 a.m. local time**, prompt "Run
the research-scout skill." A run missed while the Mac is asleep fires at
the next opportunity. The schedule is turned on only after testing passes.

## Testing (before enabling the schedule)

1. **Backfill dry run:** run the skill by hand with a 60-day window. Check
   that it finds studies the user knows about, skips the ones already in
   `wiki/sources/`, and rejects secondary roundups such as thedigitalbloom
   reports.
2. **Dedupe check:** run it again straight away; it should report almost
   nothing new.
3. **Tune** `rubric.md`, `lanes.md` and `seed-sources.md` from the results,
   then enable the schedule.

The 60-day window is a run-time override for testing only; the default
stays at 14 days.

## Out of scope

- Ingesting into `wiki/` or saving sources into `raw/` (the user ingests
  from the digest using the existing workflow).
- Committing, branching, pushing to GitHub, or opening PRs.
- Slack or email delivery.
- Semrush or other paid-API lookups for publisher authority.
- RSS/arXiv collector scripts.
