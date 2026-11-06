---
type: source
tags: [aeo]
date_published: 2026-07-30
date_ingested: 2026-10-02
origin: raw/articles/tryprofound-where-ai-citations-come-from.md
---

# Where do AI citations come from? (Profound)

**Citation:** Singh, Jasman. "Where do AI citations come from?"
Profound Blog, 2026-07-30.
https://www.tryprofound.com/blog/where-do-ai-citations-come-from

**Data:** 11.84B citations from the Profound citations API, across 8
engines: ChatGPT, Claude, Google AI Mode, Google AI Overviews, Gemini,
Grok, Copilot and Perplexity.
- 8,061 Profound customer categories were tracked from 2026-04-16 to
  07-16. 7,542 of them had 100+ citations.
- Each category was assigned to one of 29 industries by an LLM judge,
  based on the category owner.
- Medians are computed per category, so high-volume brands don't
  dominate.
- Four charts are saved to `raw/assets/`.

This is a different post from
[[tryprofound-ai-platform-citation-patterns]] (680M citations,
2024–25).

## Taxonomy (matters for comparisons)

Every cited domain was classified into one of three buckets using a
3.02M-domain map, which covers 98.3% of citation volume:

- **Brand:** company-operated web properties of *any* company, not only
  the category owner's. This includes corporate and product sites and
  company blogs and docs. The industry chart splits it into "branded,
  owned" (the category owner) and "branded, third-party" (every other
  company).
- **Earned:** third-party editorial coverage, institutional sources and
  PR wire.
- **Social:** social and UGC platforms, such as Reddit and YouTube.

"Other" plus unmapped domains make up 2–7% per industry.

## Key takeaways

- **Company websites are the biggest citation source.** About 57% of
  citations across all models are brand sites. Brand is the largest
  bucket for the median customer in 24 of 29 industries. Press, Reddit
  and YouTube are each smaller.
- **But it's mostly *other* companies' sites.** The category owner's
  own site is only 2–6% of citations in every industry charted. The
  rest of the brand share is competitors, adjacent vendors and partners.
  The text glosses over this; it's visible only in the chart. Example:
  software is 6% owned, 73% other companies, 12% earned, 13% social.
- **The mix varies by industry.** Median earned share runs from
  government (about 61%) and pharma (59%) down to SaaS/software (11.4%)
  and marketing (about 11%). The text puts brand share between 74%
  (cybersecurity) and 15.9% (government and nonprofit). Pharma's tilt
  toward earned media holds on every consumer engine. The authors
  explain it with compliance friction on owned content.
- **The mix also varies by engine.** Brand / earned / social shares,
  with values marked ~ read off unlabeled bars:

  | Engine | Brand | Earned | Social |
  |---|---|---|---|
  | ChatGPT | 47% | 30% | ~11% |
  | Google AI Overviews | ~60% | 17.0% | 15.3% |
  | Google AI Mode | ~60% | ~18% | 14.4% |
  | Perplexity | ~53% | ~25% | ~10% |
  | Copilot | ~57% | ~28% | ~3.5% |
  | Grok | ~57% | ~27% | ~8% |
  | Claude | ~66% | ~23% | ~4% |
  | Gemini | 69% | ~21% | ~4.5% |

  ChatGPT has the lowest brand share and the highest earned share.
  Gemini has the highest brand share. Google's engines cite social
  about 1.3x as often as ChatGPT and 4x as often as Copilot. On fashion
  queries, AI Overviews' social share is 25.2% vs. Copilot's 1.7%
  (15x); the gap is 5–15x across six consumer industries.
- **Data access is one explanation.** ChatGPT has paid data-licensing
  deals (e.g. Reddit) that Anthropic hasn't made, and "LLMs cannot cite
  what they cannot see."
- **Industry sets the baseline, not the ceiling.** Within one industry,
  earned share at the 25th and 75th percentiles can differ by up to 43
  points. Benchmark against your industry median. A 30% earned share
  is far behind in pharma (median 59%) but well ahead in fintech
  (median about 15%; the chart shows about 21.5%).

## Caveats

- The data comes from a vendor (Profound sells this benchmark), and the
  sample is Profound customers' categories.
- Industry labels were assigned by an LLM judge. The domain map is
  point-in-time.
- The text and charts don't always match:
  - Marketing brand share is 72% in the text vs. 76% in the chart
    (5 + 71).
  - "Software" appears twice on the earned-share chart (about 30% and
    about 11.5%). The text's 11.4% suggests the 30% row is mislabeled.
  - The fintech median is about 15% in the text vs. about 21.5% in the
    chart.
- Most per-engine values were read off unlabeled bars and are
  approximate.
- No region, language or query-type breakdown.

## Relationship to existing wiki claims

- **Apparent conflict with** [[muckrack-generative-pulse-ai-reading-may-2026]]
  in [[ai-citation-landscape]] ("earned media ~84%, owned + paid
  ~16%"). Profound's headline is that company websites are about 57%.
  The difference is most likely taxonomy: Muck Rack counts
  "third-party corporate content" as earned, while Profound counts
  every company's site as "brand." On the owner's own site the two
  roughly agree (Profound 2–6% owned vs. Muck Rack ~16% owned + paid).
  Logged as a Conflicting Evidence entry, with the current best guess
  "definitional, likely reconcilable."
- **Corroborates** [[otterly-claude-ai-citation-study-2026]]'s profile
  of Claude: about 66% brand and about 4% social here, vs. Otterly's
  64% first-party, 0.9% social and zero Reddit. It also offers a reason
  (no Reddit licensing deal).
- **Corroborates** the "separate information environments" and engine
  "sourcing personalities" findings. ChatGPT having the highest earned
  share fits its "long-tail editorial" profile. Copilot's very low
  social share fits Otterly's Copilot YouTube figure of 0.5%.
- **Extends** the "Query type and sector shape citation mix" and
  "Topic-specific source trust" sections with an industry-level
  breakdown across all three buckets.
- **Complements** the three-layer source strategy in
  [[geo-content-optimization-tactics]]. This source adds industry
  medians to benchmark against.

## Updated pages

- [[ai-citation-landscape]]
- [[geo-content-optimization-tactics]]
- [[ai-entity-footprint-audit]]
