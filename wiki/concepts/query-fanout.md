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
  sub-queries per prompt, ChatGPT ~2.1 (April 2026 baseline — later
  reported at 7.61, see Conflicting Evidence), Grok ~6.8; ChatGPT injects
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
  Console** as such (Bing exposes a generalized view — see Conflicting
  Evidence), so the vocabulary that decides retrieval is missing from
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

## Conflicting Evidence

- **Claim**: ChatGPT issues ~2.1 sub-queries per prompt.
  - Supported by: [[peec-ai-chatgpt-query-fanouts-2026]] (published
    2026-07-07, April 2026 data).
  - Contradicted by: [[lilyray-chatgpt-fanout-queries-2026]]
    (2026-08-17) — average fan-out queries per prompt rose from 2.17 to
    7.61, alongside `site:` use rising from 0.3% to 23% (also on
    [[ai-citation-landscape]]).
  - **Current best guess**: a change over time, not incompatible
    measurements. Read 2.1 as the April 2026 baseline and 7.61 as the
    later, **directional** figure (secondary writeup, undisclosed
    method). Flagged **unresolved** until a primary dataset confirms it.
- **Claim**: fan-out sub-queries are invisible in your analytics.
  - Supported by: [[dejan-new-tail-keyword-research]] (2026-07-27) —
    they "never reach Search Console".
  - Contradicted by: [[bing-ai-performance-report]] (first-party
    Microsoft help page, undated) — exposes generalized "grounding
    queries" behind Copilot citations; and the `site:`-impressions
    monitoring tactic in [[geo-content-optimization-tactics]]
    ([[lilyray-chatgpt-fanout-queries-2026]], 2026-08-17).
  - **Current best guess**: **mostly invisible** — Google Search Console
    doesn't show fan-out queries as such; Bing's grounding queries are a
    partial, generalized view (the first-party source is the strongest
    evidence here). The Search Console `site:` tactic is an untested
    hypothesis. Flagged **unresolved**. (Both filed during the
    2026-11-06 wiki merge.)

## See also

- [[grounding-snippets]] — what gets extracted once fanout has retrieved
  a page.
- [[parametric-memory-vs-grounding]] — where retrieval sits next to the
  model's own recall.
- [[listicles-in-ai-search]] — why "best of" fanout injection favours
  listicles.
- [[generative-engine-optimization]] — the broader discipline.
- [[ai-search-reranking-pipeline]] — the staged pipeline fanout feeds (engine selection → hybrid retrieval → rerank → generation).
- [[chatgpt-vertical-retrieval-engines]] — where ChatGPT's sub-queries go: ~69 engines, each with a query rewriter.
