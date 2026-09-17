---
type: source
tags: [aeo]
date_published: 2026-09-17
date_ingested: 2026-09-17
origin: raw/articles/konitzny-chatgpt-retrieval-leak-engine-list-2026.md
---

# The Complete List: Every Search Engine Hidden Inside ChatGPT's Retrieval Leak (Konitzny)

**Citation:** Konitzny, David. "The Complete List: Every Search Engine Hidden
Inside ChatGPT's Retrieval Leak." LinkedIn Pulse. Published 2026-09-17.
https://www.linkedin.com/pulse/complete-list-every-search-engine-hidden-inside-leak-david-konitzny-uwofe/

**What it is:** an enumeration of **69 named retrieval engines** extracted from a
ChatGPT server-sent-events (SSE) leak originally uncovered by Metehan
Yesilyurt. For each engine the source gives four config fields: `source`, `tags`,
`result_types`, `rewriter_name`. Konitzny is at Peec AI, already cited in this
wiki via [[peec-ai-rerankers-geo-aeo-2026]] and
[[peec-ai-chatgpt-query-fanouts-2026]].

**Methodology note (rigor caveat):** this is a **configuration dump, not a
study**. Single practitioner, unverified leak, no published extraction
methodology, no sample size, no replication, and — critically — **no call
frequency per engine** (a commenter asks this directly and it goes unanswered).
An enumerated registry routinely contains legacy, deprecated, dark-launched, or
experiment-gated entries that never fire in production, so every entry is
evidence of "exists," not "matters." Engine semantics (`fortis`, `synthetic`,
`aixiv`) are inferred from names, not documented. The `mai-news-beta` tag proves
the registry was mid-rollout at capture, so it will drift. Treat as a
**structural map** of retrieval routing, with low confidence on the weight of
any individual path. Same treatment given to other credible-practitioner,
undisclosed-methodology sources in this wiki.

## Key takeaways

- **Retrieval is a vertical-engine fan-out, not one web search.** Engines split
  internal (`labrador`, `labrador-web` — ~47 of 69) vs. external, with dedicated
  paths per content type and topic: Wikipedia, arXiv, STEM, Reddit, news, legal
  (text *and* PDF), medical (text *and* PDF), finance, local/places, web-PDF,
  web-YouTube, and images. Content format is a **routing decision made before
  any relevance scoring**, not merely a ranking signal.
- **ChatGPT's web backend is plural, not just Bing.** Four distinct external
  web/news backends appear side by side: `bing`, **`serpapi_auto_web` /
  `_news` / `_image`** (SerpAPI being a commercial *Google*-SERP scraping API —
  implying Google SERP data reaches ChatGPT via an intermediary),
  `mai_grounding` / `mai_grounding_news` (Microsoft's MAI grounding service),
  and the unidentified `fortis` / `fortis_barebone`. The common practitioner
  shorthand "ChatGPT search is Bing-powered" understates the surface.
- **`bing_query` is the dominant query rewriter — even for OpenAI's own internal
  engines.** Sub-queries are reformulated into Bing-style syntax before hitting
  `labrador`. This is the mechanical explanation for the 0.3% → 23% surge in
  `site:` operator usage in fan-outs measured by
  [[lilyray-chatgpt-fanout-queries-2026]]. Vertical rewriters also exist:
  `literature_search_query`, `finance_search_query`, `legal_search_query`,
  `image_query`.
- **News freshness is path selection, not a ranking tweak.** `news-1d`,
  `news-7d`, and `news-all` are *separate engines*. A query routed to the
  24-hour index never sees week-old content at all, regardless of its quality.
  A `-news-google-redirect-fallback` path exists at every tier.
- **Retrieval breadth scales with reasoning tier.** `system1` and `system2`
  variants have non-equivalent coverage: system2 reaches **Reddit, web-PDF, and
  web-YouTube**, which system1 never touches. Implication: visibility can depend
  on the user's reasoning mode — a PDF or video asset may be unreachable in a
  fast-mode answer and retrievable in a thinking-mode answer. Plausible
  mechanism under the "ChatGPT 5.6 retrieves more" shift in
  [[lilyray-chatgpt-fanout-queries-2026]].
- **Local/business retrieval runs on Yelp and Foursquare.** Both are the only
  external business sources (`result_types: null`, no rewriter — suggesting
  structured lookup rather than rewritten search), alongside internal
  `labrador-local` → `places`. **No Google Business Profile path appears
  anywhere in the registry.**
- **Legal and medical are the only verticals with paired text + PDF engines** —
  the two highest-stakes YMYL domains, where authoritative material (statutes,
  filings, clinical guidelines) is disproportionately PDF-shaped.
- **`labrador-web-fallback` is tagged `external` while `labrador-web` is tagged
  `internal`** — the same index reached by two paths with different
  trust/fallback semantics.
- **Getty is a distinct licensed-image source** (`getty-image`), separate from
  `bing-image` and `serpapi-image`.
- **Unexplained entries:** `labrador-synthetic` / `labrador-synthetic-index`
  (names suggest an OpenAI-generated derived index layer — if real, it would
  decouple what the model retrieves from what you publish; **speculative**),
  `fortis` / `fortis_barebone`, `labrador-aixiv` (distinct from `-arxiv`), and
  `labrador-images-nocache`.

## Caution logged: retrieval path ≠ citation value

The source's most-liked comment (Jayson DeMers) argues the separate Reddit
engine proves how much weight Reddit threads carry. **That inference conflicts
with citation data already in the wiki** and is recorded as a caution on
[[chatgpt-vertical-retrieval-engines]] rather than as a source-vs-source
conflict, since it is a reader inference rather than a claim Konitzny makes:

- Reddit has *two* dedicated engines (`labrador-reddit-web`, `system2-reddit`).
- Reddit is cited at 1.93% in ChatGPT and is 67.8% of *non-cited* retrieved URLs
  ([[ahrefs-why-chatgpt-cites-pages-2026]]); ~99% of Reddit retrievals are
  discarded ([[lilyray-chatgpt-fanout-queries-2026]]).

Both hold simultaneously. A dedicated engine evidences retrieval volume and
routing intent; citation is decided two stages later at the reranker
([[ai-search-reranking-pipeline]]).

## Relationship to existing wiki content

**Extends, does not conflict.** This is the mechanism layer beneath several
existing empirical findings: it supplies the engine-selection stage that
[[ai-search-reranking-pipeline]] described only as "hybrid retrieval," and it
explains *why* the `site:` operators and fan-out escalation in
[[lilyray-chatgpt-fanout-queries-2026]] look the way they do. The multi-backend
finding is new territory rather than a contradiction — the wiki carried no page
asserting a Bing-only ChatGPT backend. The Yelp/Foursquare local finding sits
beside, not against, the Google Maps reliance documented for AI Overviews in
[[ai-citation-landscape]] (different engine, different provider).

**Gap surfaced, not filled:** local/business AI visibility via Yelp and
Foursquare listing accuracy is actionable and has no playbook in this wiki. One
unverified source is not a sufficient basis to build one — noted on
[[chatgpt-vertical-retrieval-engines]] for a future pass.

## What this updated

- **New:** [[chatgpt-vertical-retrieval-engines]] — the full engine map, the
  system1/system2 tiering, the rewriter layer, and the retrieval-path-≠-
  citation-value caution.
- [[ai-search-reranking-pipeline]] — stage 2 gains the engine-selection substage.
- [[ai-citation-landscape]] — added "ChatGPT's retrieval backend is plural"
  section.
- [[geo-content-optimization-tactics]] — added vertical retrieval-path
  eligibility tactics.
- [[pdf-seo-optimization]] — confirmed a dedicated `web-pdf` retrieval path,
  reachable only at the system2 reasoning tier.
- [[wiki/timeline.md]] — logged the 2026-09-17 publication of the engine registry.

No conflicts logged.
