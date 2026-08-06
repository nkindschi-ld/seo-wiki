# Model memory predicts which brands get searched

Source: https://geosurge.ai/posts/model-memory-predicts-which-brands-get-searched
Publisher: geoSurge (GEO/AI-visibility tooling vendor)
Study period: May 29 – June 9, 2026 (12 days)
Captured: 2026-08-06 (via WebFetch extraction — not a verbatim HTML mirror;
no explicit byline or publish date shown on the page)

---

## Core thesis

"A brand the model remembers from training is searched about 3x as often
as one it doesn't." A brand's presence in an AI model's training memory
predicts whether the model later *searches for it* (live web retrieval)
when answering a user question.

## Methodology

- Nine industries: Travel, Automotive, Finance, Business Software,
  Education, Food & Restaurants, Luxury, Fitness & Wellness, Fashion.
- 66 U.S. buyer-style questions.
- ~4,000 model responses; 13,281 fan-out queries.
- 1,416 brand-level observations (492 remembered, 924 not-remembered);
  only brands receiving at least one mention or search result counted.
- Memory measured via geoSurge's proprietary methodology on a SEPARATE
  model from the search model.
- Search measured on Gemini 3.5 Flash production queries.
- Each prompt answered 60 times; 5 iterations daily over the 12-day window.

## Key findings

Primary statistic:
- A brand in the model's top-10 memory was searched at 3.2x the rate of
  one it did not remember: 55.7% vs. 17.4% (across 1,416 observations).

Memory-strength gradient:
- Top-5 recalled brands: 67% search rate
- Rest of top-10: 39% search rate
- Not remembered: 17% search rate

Search-query composition:
- 31% of queries name specific brands; 69% are generic category searches.
- Of brand-specific queries, 63% name the model's top-5 remembered brands.

Industry consistency:
- Pattern held across all nine industries.
- Not-remembered search rates ranged 9–23%; remembered rates 41–82%.

Two behavioral patterns:
- "Memory-led" categories (e.g., Automotive, Finance): searching closely
  tracks recalled brands; top-recalled brands dominate searches.
- "Search-led" categories: the model searches beyond its memory; strong
  live web presence can surface unremembered brands.
- Even in memory-led categories, unremembered brands occasionally surface
  via strong web presence.

## Recommendations

- Prioritize "building memory" through sustained category authority so a
  brand is present in model recall before query time.
- Establish presence via analyst and press coverage, partnership signals,
  and consistent category association / comparison content.
- In memory-bound categories, entry into model recall is "close to a
  precondition for being searched."
- In search-led categories, "strong live content can carry a brand"
  despite weaker recall.

## Limitations (stated by the authors)

- Measures "an association in exploratory data, not a proven cause."
- Brand prominence is a potential confound (prominent brands both get
  remembered and get searched).
- Per-industry figures rest on as few as 6 prompts — indicative, not
  conclusive.
- Magnitude is scope-dependent; directional relationship expected to hold.
