---
type: source
tags: [seo, aeo]
date_published: 2025-04-24
date_ingested: 2026-07-22
origin: raw/articles/ahrefs-llm-optimization.md
---

# LLMO: 10 Ways to Work Your Brand Into AI Answers (Ahrefs)

**Citation:** Louise Linehan, Ahrefs Blog, "LLMO: 10 Ways to Work Your
Brand Into AI Answers," updated 2025-04-24.
https://ahrefs.com/blog/llm-optimization/

## Key takeaways

- Defines LLMO (positioning a brand for mentions/links/native inclusion
  in LLM answers) and the self-contained-vs-RAG LLM distinction, already
  covered in this wiki via [[generative-engine-optimization]]'s LLM
  taxonomy.
- **Semantic proximity mechanism**: LLMs map brand/topic associations via
  token embeddings and cosine similarity — the mechanistic basis for
  "which brands get recommended for a given topic," with a worked example
  (Herman Miller's PR-driven association with "ergonomic").
- **A 10,000-query search-augmented-LLM (Bing/Google) study** reports
  visibility-uplift/relevance-score numbers for Quotes, Statistics,
  Fluency, Citations, Technical terms, Easy-to-understand, Authoritative
  tone, Unique words, No optimization, and Keyword stuffing — the same
  tactic set as [[geo-generative-engine-optimization-aggarwal-2023]]'s
  Tier 1-3 tactics already in [[geo-content-optimization-tactics]],
  reported with different exact figures (not independently confirmed
  whether this is the same underlying study cited differently or a
  separate replication).
- **Entity research tools**: Google's Natural Language API, Inlinks'
  Entity Analyzer, Ahrefs' AI Content Helper — plus Google's "3 Pillars
  of Ranking" (body text / anchor text / user interactions) and
  site-level entity signals (site embeddings, site focus score, site
  radius).
- **Wikipedia's four listing requirements**: notability, verifiability,
  neutral point of view, and avoiding conflict of interest — operational
  detail behind this wiki's existing "Wikipedia matters for
  ChatGPT/Claude visibility" tactic.
- **Reddit UGC investment** (AMAs, community building, influencer
  partnerships) as a tactic, citing Reddit's own S-1 filing describing
  its content as "foundational to how leading LLMs have been trained."
- **LLM feedback (thumbs up/down)** corrects static-model brand
  perception — corroborates the existing feedback-loop tactic from
  [[wix-generative-engine-optimization]].
- **Seer Interactive study** (10,000 finance/SaaS purchase-intent
  queries, GPT-4o API vs. Google/Bing SERPs): organic rankings correlate
  with LLM brand mentions at ~0.65 strength; **backlinks show a
  surprisingly neutral impact** — corroborates the "ranking well in
  classic search is close to a prerequisite for AI citation" pattern
  already established by [[airops-fan-out-effect-2026]] and
  [[ahrefs-why-chatgpt-cites-pages-2026]], and adds a new
  backlinks-don't-help data point to
  [[ai-visibility-correlation-factors]]'s unresolved authority-correlation
  conflict.
- **Black-hat warning**: a Harvard study, "Manipulating Large Language
  Models to Increase Product Visibility," describes Strategic Text
  Sequencing (~40% of evaluations shifted product ranking) and
  preference-manipulation prompt injection (raised a fake product's
  recommendation rate from 34% to 59.4%, a 2.5x selection increase) —
  new adversarial-manipulation territory not previously in this wiki.
- Correction noted in the source itself: AI crawlers only read HTML, not
  client-rendered content or schema — schema markup is not itself a
  direct LLM-visibility lever (still valuable for classic
  rich-result/entity purposes).

## What this updated in the wiki

- Added a "Brand-building LLMO tactics" section to
  [[geo-content-optimization-tactics]] (semantic-proximity PR, entity
  research tools, Wikipedia's four requirements, Reddit UGC investment,
  brand-question research) and a new "Known adversarial risk: LLM
  recommendation manipulation" awareness note (prompt-injection attacks
  on brand-recommendation outputs — not a tactic to use, a risk to
  monitor for).
- Added the Seer Interactive organic-rank/backlink-neutral data point to
  [[ai-visibility-correlation-factors]]'s Conflicting Evidence section as
  further corroboration of the AirOps-aligned side.
- No conflicts created — corroborates and operationalizes existing
  findings; the black-hat section is net-new but doesn't contradict
  anything already in the wiki.

## Correction (2026-07-22)

The primary paper behind this source's "Harvard study" black-hat
warning has now been directly ingested:
[[kumar-lakkaraju-manipulating-llms-2024]]. Its "34% to 59.4%"
recommendation-rate figure, cited above and previously repeated in
[[geo-content-optimization-tactics]], **does not appear anywhere in the
primary paper** — likely a misattribution in this Ahrefs article. The
*existence* of the vulnerability is confirmed by the primary source;
the specific numbers have been corrected on
[[geo-content-optimization-tactics]] to the verified figures (~40%→~95%
rank-advantage rate depending on order-robust optimization). This entry
is left as-is (documenting what Ahrefs actually said) per this wiki's
practice of not editing what a source page records a source as
claiming — the correction lives on the pages that cited the figure as
fact.
