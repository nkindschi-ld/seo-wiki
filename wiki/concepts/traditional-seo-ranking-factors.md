---
type: concept
tags: [seo]
updated: 2026-07-07
---

# Traditional SEO Ranking Factors

Empirical correlation data for **classic organic SERP ranking**
(pre-AI-answer, links-and-positions search) — distinct from
[[ai-citation-landscape]] and [[ai-visibility-correlation-factors]],
which cover AI-answer citation/mention visibility specifically. Based on
[[semrush-ranking-factors-study-2024]]: 16,298 keywords, 300,000 organic
positions, US mobile SERPs, Spearman correlation — explicitly excluding
SGE/AI features.

## Strongest correlates with ranking

- **Text relevance** (topical coverage of the query and related
  subtopics): the single strongest correlate, ~90.6% average for top-10.
  For the *scoring mechanics* beneath this finding — how term frequency,
  rarity (IDF), saturation, and length normalization actually turn words
  into a relevance score — see [[lexical-ranking-tf-idf-bm25]].
- **Domain/Page Authority Score** (backlink-derived): correlates at 0.21
  / 0.19 — meaningful but far from dominant, with an acknowledged
  chicken-or-egg confound (ranking higher can itself generate more
  backlinks).
- **Reviews/star ratings**: correlate meaningfully with rankings,
  explicitly tied by the study to E-E-A-T Trust (see
  [[e-e-a-t-and-page-quality]]).
- **User signals** (direct traffic share ~31%, branded search traffic
  share ~24%): support a brand-building takeaway, similar in spirit to
  [[ai-visibility-correlation-factors]]'s branded-search-volume finding
  for AI visibility.

## What barely correlates

- **Keyword-in-title/meta-description**: minimal correlation — semantic
  (embedding-based) similarity to the topic correlates better than
  literal keyword presence.
- **Content length/word count**: no correlation — content *quality*
  correlates, volume does not. Independently confirms
  [[ai-visibility-correlation-factors]]'s near-zero content-volume
  finding and aligns with [[e-e-a-t-and-page-quality]]'s Scaled Content
  Abuse framing, this time from a classic-SERP dataset rather than an
  AI-citation one.
- **Schema.org markup**: very little correlation — "don't go overboard
  with Schema... it can bring on a penalty if you're seen as using it to
  manipulate rankings."
- **Core Web Vitals / HTTPS / technical UX factors**: weak correlation,
  framed as a likely tie-breaker rather than a primary ranking lever.
- **Author/Person schema markup specifically**: weak correlation on its
  own, though the study notes author experience/expertise is still
  explicitly named as a rating factor in the Search Quality Evaluator
  Guidelines regardless of whether it's marked up with schema.

## Classic SERP correlates vs. AI-citation correlates: a comparison

| Factor | Classic SERP ranking | AI-mention visibility ([[ai-visibility-correlation-factors]]) |
|---|---|---|
| Topical/content relevance | Strongest correlate (~0.91) | Not directly measured by that source |
| Backlinks/Domain authority | Moderate (0.19–0.21) | Weakest correlates measured (0.19–0.33) |
| Branded search/traffic | Meaningful (direct/branded traffic share) | Meaningful (0.35–0.47 branded search volume) |
| Content volume | No correlation | Near-zero correlation |
| Video presence (e.g. YouTube) | Excluded from dataset entirely | Strongest correlate (~0.737) |

The video-presence row is the most striking contrast: classic SERP
methodology in this study *excluded* YouTube positions entirely to avoid
skew, while YouTube mentions are the single strongest predictor of
AI-mention visibility. This suggests video/YouTube presence may be a
distinctly AI-era signal rather than a carryover from classic SEO.

## Other findings

- URLs ranking #1 for a given term tend to also rank for ~4x as many
  other terms as position-20 pages do — breadth of topical coverage
  compounds rather than being purely query-specific.
- Moving from position 2 to position 1 is associated with roughly +50%
  more organic traffic.

## Caveats

Correlation, not causation, per the study itself: "It would be a
mistake to interpret these findings as 'do this and you'll rank.'"
US-mobile-only data; excludes navigational and branded queries;
excludes SGE/AI features entirely (collected before AI Overviews were
widely live).

## See also

- [[classic-seo-ranking-factors]] — the actionable playbook version of
  this data.
- [[ai-visibility-correlation-factors]] — the AI-citation-era equivalent
  study, useful for the classic-vs-AI comparison above.
- [[e-e-a-t-and-page-quality]] — the qualitative framework this study's
  reviews/trust findings independently confirm.
- [[bardas-white-hat-seo-llm-2025]] — a research-stage technique
  targeting the same kind of classic ad hoc retrieval ranking functions
  (LambdaMART, embedding cosine similarity) this page covers, using an
  LLM as the document-editing tool rather than manual optimization.
- [[lexical-ranking-tf-idf-bm25]] — the TF-IDF/BM25 scoring mechanics
  underlying the text-relevance correlate.
