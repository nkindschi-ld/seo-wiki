---
type: source
tags: [aeo]
date_published: 2024-01-21
date_ingested: 2026-09-04
origin: raw/articles/malte-landwehr-llmo-geo-aio-guide.md
---

Malte Landwehr, "The Ultimate Guide to LLMO, GEO & AIO" (LinkedIn,
published 2024-01-21).

## Key takeaways

- Early (Jan 2024, pre-dating [[geo-generative-engine-optimization-aggarwal-2023]]'s
  wider industry adoption) attempt to name and unify LLMO/GEO/AIO as one
  discipline — useful as a snapshot of how practitioners were framing
  the problem before Google AI Overviews existed at scale.
- **Co-occurrence** as the core mechanism for influencing brand
  association in LLM outputs: strategically pairing a brand with target
  keywords/topics on authoritative sites so training data links them
  together. Illustrated with the Tesla-whistle example — a PR stunt
  created enough "Tesla" + "whistle" co-occurrence in media coverage
  that ChatGPT's autocomplete began associating the two terms. This is
  a *training-data-influence* mechanism, distinct from
  [[geo-content-optimization-tactics]]'s citation-visibility tactics,
  which operate on retrieval-augmented (RAG) systems reading live
  content rather than baked-in training associations.
- Concrete authoritative-site target list for co-occurrence building:
  heavily-moderated community sites (Wikipedia, Reddit, Quora), database
  platforms (Crunchbase, Yelp, IMDB), major editorial outlets (NYT,
  Bloomberg, Reuters, Forbes), and explicitly Google's Knowledge Graph
  source list (~63k sites) — overlaps heavily with
  [[brand-entity-seo-strategy]]'s Knowledge-Graph-data-source list.
- Explicit operational tactic largely absent from this wiki's other GEO
  sources: **monitor robots.txt for accidental blocking of LLM
  crawlers** (GPTBot, CCBot, Google-Extended, Anthropic-ai, omgilibot)
  — a pure downside-avoidance check, complementary to
  [[robots-txt-strategy]]'s per-bot user-agent table.
- Named limitation still broadly true: LLM training-data sources are
  undisclosed per-model, models retrain at wildly different cadences
  (SGE ~24h vs. some models "never"), and small/niche sites can
  sometimes outperform dominant brands in LLM answers — an early,
  independently-arrived-at version of
  [[generative-engine-optimization]]'s "GEO disproportionately helps
  lower-ranked content" finding.

## Updated

- [[generative-engine-optimization]] — added a note on co-occurrence/
  training-data-influence as a distinct mechanism from citation-stage
  RAG visibility, plus the authoritative-source target list.
- [[geo-content-optimization-tactics]] — added the robots.txt/LLM-bot-
  blocking check as an explicit tactic.

## No conflicts

Consistent with existing GEO sources — offers an earlier, narrower-
scope version of ideas the wiki already has more rigorous later
evidence for ([[geo-generative-engine-optimization-aggarwal-2023]],
[[wix-generative-engine-optimization]]). Treated as corroborating/
supplementary, not authoritative on its own for any claim where a later
empirical source disagrees.
