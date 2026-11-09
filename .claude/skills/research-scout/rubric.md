# Research scout rubric

Apply this to every candidate. Lanes apply it first; the judge re-applies
it and has the final say.

## Hard gate (all four required)

A candidate that fails any criterion is rejected. Record the **first**
criterion it fails as `reject:g<N>`.

1. **Primary research (g1).** The author collected or analyzed the data
   themselves. Secondary roundups, listicles of other people's statistics,
   and opinion or prediction posts fail.
2. **Stated methodology (g2).** It states what was measured and how: data
   source, sample size, and study period. Vague sizes ("thousands of
   queries", "over 130 respondents") fail.
   - **Study period, loosened:** if the data-collection period isn't
     stated, the publish month counts as the period when the data is
     clearly current (e.g. a live tool snapshot, current model versions, a
     survey of current platform use). Such a study passes g2, but its
     rigor score is **capped at 3**, and the entry's Method line says
     "collection period not stated".
   - A controlled lab experiment that names the exact model versions it
     tested may treat those versions as its period (no cap).
   - Data that is old or undated in a way that matters (e.g. no way to
     tell which model generation produced it) still fails g2.
3. **Identifiable, credible author (g3).** A named person or organization
   with a track record in the field: earlier published research, a known
   research team, or an academic post. Anonymous content-farm pages fail.
4. **In scope and new (g4).** On-topic (see the topic scope in
   `lanes.md`), published within the run's window, and not already in
   `research-digests/seen.md` or `wiki/sources/`.

## Rigor score (gate passes only)

| Score | Criteria |
|---|---|
| 5 | Peer-reviewed or preprint with a reproducible method; controlled experiment or large sample; data or code released |
| 4 | Large-sample industry study with full method details (sampling, engines, dates, definitions) and stated limitations |
| 3 | Reasonable sample with a method described, but a key detail missing (prompt selection, engine version) |
| 2 | Small sample or single case study, with the method described |
| 1 | Passes the gate but the method is only just adequate; include it and treat it with caution |

## Conflict-of-interest note

Required on every entry ("none apparent" is a valid value). Say what the
publisher sells and how that could bias the result, e.g. "vendor sells AI
visibility tracking; study measures the problem its product solves."
Vendor studies are **not** penalized in the score: Semrush, Ahrefs and
Profound are among this wiki's strongest sources.

## Ledger verdicts (`research-digests/seen.md`)

| Verdict | Use when |
|---|---|
| `pass:<1-5>` | Passed the gate; the number is the rigor score |
| `reject:g1` … `reject:g4` | Failed the gate; the number is the first failed criterion |
| `unverified` | The page or PDF couldn't be read (paywall, gated, blocked), so the gate couldn't be applied |

`reject:g4` never counts toward moving a source to Caution, because being
already in the wiki or outside the window says nothing about rigor.

## Worked examples (from this wiki's history)

- **thedigitalbloom.com, "AI Citation Position & Revenue Report 2026"** →
  `reject:g1`. It aggregates 30+ other studies and states that it "does not
  conduct original research." Its headline 680M-citation figure is
  Profound's, which the wiki already holds firsthand.
- **JISEM, MCP-documentation retrieval paper (2025)** → `reject:g2`. An
  architecture article presented as research, with zero quantitative
  results: no sample sizes, no measured values, and an assessment
  section that reports no findings.
