---
type: concept
tags: [aeo, seo]
updated: 2026-11-06
---

# Query Fanout

**Query fanout** is the step where an AI search system rewrites one user
prompt into several single-intent sub-queries, retrieves sources for
each, and combines the results before generating an answer. It is why a
page can be retrieved for one angle of a question and be absent for
another, and why the queries that actually decide AI visibility are
mostly ones no human typed.

This page pulls together fanout material that was previously spread
across other pages. Detailed engine-level statistics stay where they
were first filed; this page summarises and links to them.

## How it works today (text fanout)

- **Prompt → sub-queries → retrieval → grounding → synthesis.** An LLM
  writes the sub-queries as text; each is embedded or searched and
  returns its own set of sources, typically 5–20 per sub-query
  ([[dejan-grounding-snippets-2026]]). Extracted snippets from those
  sources form the model's context; see [[grounding-snippets]].
- **Google confirms the mechanism** for AI Overviews/AI Mode: fanout
  runs over the existing index rather than a separate ranking system
  ([[google-ai-optimization-guide]]).
- **Volume and injected wording vary by engine** — Perplexity ~1.4
  sub-queries per prompt, ChatGPT ~2.1, Grok ~6.8; ChatGPT injects
  "best", "top", "comparison", "reviews" and the current year even when
  the user didn't. Results are merged with Reciprocal Rank Fusion, so
  content surfacing across several sub-queries wins. Full detail in
  [[ai-citation-landscape]] § Query fanout mechanics
  ([[peec-ai-chatgpt-query-fanouts-2026]]).
- **Content implications are about focus, not completeness**: pages
  covering 26–50% of a query's fanout subtopics were cited more than
  pages covering all of them ([[airops-fan-out-effect-2026]]); see
  [[geo-content-optimization-tactics]].

## Fanout is invisible in your analytics

- Sub-queries are written by the assistant and **never reach Search
  Console**, so the vocabulary that decides retrieval is missing from
  analytics as well as from the page ([[dejan-new-tail-keyword-research]]).
- **Implicit queries** — searches formed from on-device context such as a
  photo, screenshot, or open page — have no typed wording at all.
- Practical response: cover the angles and attribute vocabulary a
  question splits into (human surveys plus repeated model sampling for
  the same prompt), rather than one literal phrasing. See
  [[keyword-research]].

## Textless fanout (research, not production)

Google Research's R4T-Diffusion paper (Jiang et al., arXiv 2603.06397,
March 2026) skips the text step: the query is encoded once and a 53.9M-
parameter diffusion model generates the sub-query **vectors** directly —
about 20× faster than a 4B LLM writing text sub-queries (0.07 s vs.
1.46 s per batch of 8), at a small diversity cost
([[dejan-textless-query-fanout-explainer-2026]]). DEJAN reproduced it
without the RL step and published a model trained on Google's e-commerce
taxonomy ([[dejan-fanout-vectors-2026]]).

- **Scope**: tested on fashion outfits and music playlists, not web
  search. Nothing says Google uses it in Search, AI Overviews, or AI
  Mode.
- **If it ever ships**: there would be no readable sub-queries to track
  or reverse-engineer; matching would be vector-to-vector, so broad
  topical and entity coverage would matter more than exact phrasing.
  Fanout-tracking tools that rely on observed sub-query text would lose
  their input.
- **Status**: speculative — a direction to watch, not a reason to change
  tactics now.

## See also

- [[grounding-snippets]] — what gets extracted once fanout has retrieved
  a page.
- [[parametric-memory-vs-grounding]] — where retrieval sits next to the
  model's own recall.
- [[listicles-in-ai-search]] — why "best of" fanout injection favours
  listicles.
- [[generative-engine-optimization]] — the broader discipline.
