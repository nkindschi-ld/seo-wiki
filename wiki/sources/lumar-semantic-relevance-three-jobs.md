---
type: source
tags: [aeo]
date_published: 2026-08-21
date_ingested: 2026-10-05
origin: raw/articles/lumar-semantic-relevance-three-jobs.md
---

# Semantic Relevance Isn't One Metric — It Has Three Jobs (Lumar)

Lumar Editorial Team, Lumar blog, published 2026-08-21 (modified
2026-09-09). Part 3 of Lumar's GEO series, after
[[lumar-candidate-page-selection]].

**Rigor:** a framework piece with no data. The three-role model is Lumar's
own way of describing a production retrieval system, not a documented engine
architecture.

## Key takeaways

1. **Relevance is asked three different questions** at three stages:

   | Role | Question | What it optimizes |
   |---|---|---|
   | Candidate selection | Is this page about the query? | Topical clarity |
   | Chunk retrieval | Which passage best answers it? | Answer match |
   | Citation | Is this chunk safe and precise enough to cite? | Self-contained facts |

2. **Page level is about "aboutness."** A page can be a candidate without
   holding the best answer. It is a weaker candidate when it covers several
   unrelated subjects, opens with a long intro, or has vague titles and
   headings.
3. **Passage level is about precision.** Entities, units, exact phrasing and
   clearly defined steps decide which passage wins.
4. **Citation is about standing alone.** A relevant passage that has the
   right answer can still go uncited if it uses ambiguous wording, leaves
   out units, depends on earlier paragraphs, or spreads instructions across
   sections.
5. **One page-level similarity score is misleading**, because it blurs the
   three stages and makes it easy to optimize the wrong one.

## What this updated

- [[ai-search-reranking-pipeline]]: the three-jobs table, under the
  candidate-selection section. It sharpens that page's existing "don't trust
  one relevance score" advice, which [[peec-ai-rerankers-geo-aeo-2026]]
  backed with the cross-family reranker disagreement finding.
- [[chunkability]]: the citation-stage "safe and precise enough to cite"
  framing.
- Supporting claim for the Conflicting Evidence entry on multi-topic pages in
  [[ai-search-reranking-pipeline]].
