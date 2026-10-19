---
type: playbook
tags: [seo, aeo]
updated: 2026-10-05
---

# GEO Diagnostic Checklist

**Why/when to use this:** Run this *before* reaching for
[[geo-content-optimization-tactics]]. A page that isn't getting cited
can be failing at several different, unrelated layers — throwing tactics
at it without diagnosing which layer is broken risks polishing a page
that was never eligible to be retrieved in the first place, or
chunking content that was already fine. Per
[[lumar-geo-diagnostic-checklist]], ranking position alone doesn't tell
you which failure mode you're dealing with.

## 0. Retrieval-path routing (added 2026-09-17, not in the source checklist)

Run this *before* check 1. Lumar's six checks are all content-side — they assume
the engine is searching an index your page could plausibly be in. But engine
selection happens **before** retrieval: per
[[chatgpt-vertical-retrieval-engines]], ChatGPT routes sub-queries to ~69
specialized engines by content type and vertical, so format and topic decide
*which index gets searched at all*.

- [ ] Is the content in a format with a retrieval path for this query type —
      HTML, or a format with its own engine (PDF, YouTube, images)?
- [ ] If the asset is a PDF or video, does an **HTML equivalent** exist? Those
      paths are gated to the deeper-reasoning tier, so a fast-mode answer may
      never reach them.
- [ ] For local/business queries, are **Yelp and Foursquare** listings accurate?
      They are the only external business sources in the registry.
- [ ] For time-sensitive queries, can you publish inside the recency window?
      News runs as *separate* 1-day/7-day/all-time indexes, so a late piece
      isn't down-ranked — it's never searched.

If routing is the failure, none of checks 1–6 will fix it: the page never
entered the candidate pool. *(Caveat: the engine registry behind this check is a
single unverified practitioner source — treat it as a structural prompt, not a
measured ranking factor.)*

## 1. Candidate page eligibility

- [ ] Can you describe the page's primary topic in one sentence?
- [ ] Does the title reflect the topic and match query intent?
- [ ] Does the page stay focused, or does it drift into loosely related
      subjects? *(Disputed for Google surfaces, see below.)*
- [ ] Do the title, H1 and headings contain the query's key terms, exactly
      or nearly? Lexical matching still feeds candidate selection
      ([[lumar-candidate-page-selection]]).
- [ ] Does freshness matter for this query class? News and product updates
      favor recent sources, while evergreen topics tolerate age.
- [ ] Is this a query where precision favors a specialist or official
      source? ("How oil changes work" vs. "Honda Civic oil drain torque.")
      If so, see check 5 before investing.

Meeting basic indexing/snippet eligibility (see
[[how-google-search-works]]) doesn't guarantee generative AI inclusion
on its own — it's necessary but not sufficient.

Candidate selection is a page-level gate *before* passages are scored. Rank
tracking can't see it, since a page can rank and never enter the pool. See
the candidate-selection section of [[ai-search-reranking-pipeline]]. Whether
multi-topic pages are really weaker candidates is an open conflict: Google
says its systems handle several topics on a page. See that page's
Conflicting Evidence section.

## 2. Clear aboutness signals

- [ ] Is the core concept introduced early?
- [ ] Does the opening content stand alone, without depending on
      information introduced later in the page?
- [ ] Do secondary sections actually support the main topic, rather
      than wander into tangents?

Long introductions, extensive background, or loosely related sections
dilute how clearly a page communicates its main topic to a retrieval
system.

## 3. Chunk retrievability

- [ ] Does each section cover one focused topic?
- [ ] Is related information grouped together rather than scattered?
- [ ] Is the information a query would need self-contained within a
      coherent section?

Generative features retrieve specific passages/chunks from the index,
not whole pages — see the chunk-level ("Fraggle") optimization section
of [[geo-content-optimization-tactics]] for the retrieval mechanics
this check is diagnosing against.

Checks 3–4 together cover the four pillars of [[chunkability]]: topical
cohesion and boundary clarity (check 3), answer density and self-contained
meaning (check 4). Patterns to look for:

- [ ] A long introduction delays the answer.
- [ ] Several FAQ questions or topics are grouped into one section.
- [ ] Steps or instructions are split across several headings.
- [ ] A table depends on explanation elsewhere on the page.

Fix with targeted edits, not rewrites: split multi-topic sections, move key
facts into the passage that needs them, and build each section around one
question.

## 4. Standalone passage context

- [ ] Can individual passages be understood independently, out of
      page order?
- [ ] Are references like "this" or "it" resolvable without the
      surrounding paragraph?
- [ ] Do passages include the entities, units, and constraints needed
      to stand alone (not just "it costs $50" but "the Model X costs
      $50/month")?
- [ ] Are there "as mentioned above" or "see the previous section" cross
      references that a lifted passage would lose?

## 5. Authority constraints

- [ ] Is the query sensitive or safety-critical (health, finance,
      safety)?
- [ ] Are authoritative sources consistently cited on the page?
- [ ] How does your authority compare to competitors already being
      cited for this query?

Authority acts as **a filter, not a score** — its influence varies by
query type rather than uniformly boosting every page. This matches
[[generative-engine-optimization]]'s "authority as retrieval-eligibility
gate, not citation-stage ranking factor" framing.

Classify the query first ([[authority-in-generative-search]], from
[[lumar-authority-filter-not-score]]; Lumar's "observed behavior," with no
data):

| Query type | Authority role |
|---|---|
| Medical / legal / mechanical (YMYL) | Hard gate: non-authoritative pages often excluded |
| Technical specs (manufacturer topics) | Hard preference: official sources dominate *(disputed for pricing queries)* |
| General educational | Strong filter: boosts but doesn't exclude |
| Exploratory / lifestyle | Soft filter: relevance dominates |
| Opinion / creative | Minimal |

- [ ] **Choose where to compete.** If the query is a hard-gate head term
      already well served by official or institutional sources, structure
      and relevance work probably won't get you past the filter. Redirect
      the effort to niche or operational queries where authoritative
      coverage has a gap, where precision and chunkability decide the
      outcome.
- [ ] For your own product's docs and spec queries, is the official page
      the clearest, most self-contained answer? First-party provenance is
      the strongest authority signal, so don't waste it on a weak passage.
- [ ] Don't spend on low-confidence signals first: author/`reviewedBy`
      schema and engagement metrics are rated low by Lumar and have null
      results elsewhere in the wiki.

## 6. Problem-solution alignment

- [ ] What specific problem, from checks 1-5, are you actually
      addressing?
- [ ] Does the change you're about to make directly target that
      diagnosed problem?
- [ ] Are you making a generic "AI-friendly" change with no clear
      rationale tied to a diagnosed failure?

Improving one area of a page won't necessarily resolve an issue
elsewhere — treat each check as diagnosing a distinct, independent
failure mode rather than assuming a single fix cascades to fix all six.

## Summary — six questions (plus the routing pre-check)

0. Does a retrieval path to this content even exist? *(added, see above)*
1. Is the page a likely candidate?
2. Does it clearly communicate its topic?
3. Is information organized into retrievable passages?
4. Do passages contain standalone context?
5. Could authority limit visibility?
6. Do changes address the identified problem?

## See also

- [[geo-content-optimization-tactics]] — the tactic list to apply once
  a diagnosis from this checklist identifies which layer needs work.
- [[generative-engine-optimization]] — the underlying concept,
  including the retrieval-eligibility-vs-citation-stage distinction
  this checklist operationalizes into six checks.
- [[lumar-geo-diagnostic-checklist]] — source for checks 1–6.
- [[chatgpt-vertical-retrieval-engines]] — source for check 0, the
  engine-selection layer that precedes every content-side check here.
- [[ai-search-reranking-pipeline]] — the five-stage model these checks map onto;
  its failure-stage diagnostic is the concept-level version of this playbook.
- [[chunkability]] — the concept behind checks 3–4: the four pillars and
  low-chunkability patterns.
- [[authority-in-generative-search]] — the concept behind check 5: the
  query-class table, signal confidence and authority-gap strategy.
- Lumar GEO series deep-dives behind checks 1–5:
  [[lumar-candidate-page-selection]],
  [[lumar-semantic-relevance-three-jobs]], [[lumar-chunkability]],
  [[lumar-authority-filter-not-score]].
