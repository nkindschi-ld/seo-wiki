---
type: source
tags: [aeo, geo]
date_published: 2026-06-09
date_ingested: 2026-08-06
origin: raw/studies/geosurge-model-memory-predicts-search-2026.md
---

# geoSurge — Model memory predicts which brands get searched

**Citation:** geoSurge, "Model memory predicts which brands get searched"
(no explicit byline/publish date on page; study period May 29 – June 9,
2026). https://geosurge.ai/posts/model-memory-predicts-which-brands-get-searched
· Ingested 2026-08-06.

Vendor study from geoSurge (a GEO/AI-visibility tooling company). Tests
whether a brand's presence in an AI model's **training memory** predicts
whether the model **searches for it** (issues a live-retrieval query
naming it) when answering a buyer question.

## Why it matters

This is the first source in the wiki to link the two data sources AI
draws from as a *causal chain into the retrieval step itself*: not just
"training memory produces mentions and live retrieval produces citations"
(the [[ai-citation-landscape]] / [[similarweb-how-to-be-the-brand-ai-recommends-2026]]
framing), but **training memory shaping which brands the model chooses to
search for at query time.** It reframes AirOps' "memory citations"
finding (see [[airops-fan-out-effect-2026]]) — memory doesn't only let
the model answer *without* searching; it also biases *what it searches
for* when it does go to the web.

## Key takeaways

- **The 3.2× effect:** a brand in the model's **top-10 training memory
  was searched 55.7%** of the time vs. **17.4%** for a not-remembered
  brand — a 3.2× gap across 1,416 brand-level observations (492
  remembered, 924 not).
- **Memory strength is graded, not binary:** top-5 recalled brands 67%
  search rate, rest of top-10 39%, not-remembered 17%. Deeper recall →
  more likely to be searched.
- **Search composition:** 69% of the model's fan-out queries were generic
  *category* searches, only 31% named a specific brand — and of those
  brand-named queries, 63% named a top-5 remembered brand. The model's
  brand-specific curiosity concentrates on what it already knows.
- **Two category regimes:** *memory-led* categories (Automotive, Finance)
  where searches tightly track recalled brands, vs. *search-led*
  categories where strong live web presence surfaces unremembered brands.
  Pattern held across all 9 industries (not-remembered 9–23%, remembered
  41–82%).
- **Recommendation:** build *memory* (sustained category authority via
  analyst/press coverage, partnership signals, consistent category
  association) as an upstream precondition — in memory-bound categories,
  being remembered is "close to a precondition for being searched"; in
  search-led categories, "strong live content can carry a brand."

## Methodology

- 9 industries, 66 US buyer-style questions, ~4,000 responses, 13,281
  fan-out queries, 12 days (May 29 – Jun 9 2026).
- **Memory** measured via geoSurge's proprietary methodology on a
  *separate* model; **search** measured on **Gemini 3.5 Flash**
  production queries. Each prompt answered 60 times, 5 iterations daily.
- Only brands with ≥1 mention or search result counted.

## Rigor caveats

- **Vendor source** (geoSurge sells GEO tooling) — directional interest
  in "build authority for AI visibility" conclusions.
- **Explicitly associational, not causal** (the authors say so).
- **Brand-prominence confound** acknowledged: prominent brands are both
  more remembered *and* more searched, so memory may be a proxy rather
  than a driver.
- **Undisclosed proprietary "memory" methodology** — can't be audited or
  reproduced.
- **Single search model** (Gemini 3.5 Flash); memory measured on a
  different, unnamed model — cross-model transfer of the "memory" signal
  is assumed, not shown.
- **Thin per-industry samples** — some industry figures rest on as few as
  6 prompts (indicative only).

## Pages created / updated

- Updated [[ai-citation-landscape]] — added the memory-drives-retrieval
  mechanism to the training-data-vs-live-retrieval section.
- Updated [[topical-authority-in-ai-search]] — memory as the upstream
  input to the mention/ownership funnel.
- Updated [[geo-content-optimization-tactics]] — reinforces the
  build-memory / third-party-authority tactics with a retrieval-stage
  rationale.
