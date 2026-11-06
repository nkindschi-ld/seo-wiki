---
type: source
tags: [aeo, seo]
date_published: 2026-08-12
date_ingested: 2026-10-05
origin: raw/articles/lumar-candidate-page-selection.md
---

# Candidate Page Selection: The Stage SEO Tools Don't Measure (Lumar)

Lumar Editorial Team, Lumar blog, published 2026-08-12 (modified
2026-09-10). Part 2 of Lumar's GEO series, which also includes
[[lumar-semantic-relevance-three-jobs]], [[lumar-chunkability]],
[[lumar-authority-filter-not-score]] and the later
[[lumar-geo-diagnostic-checklist]].

**Rigor:** a vendor framework piece with no data, tests or citations. Lumar
calls candidate selection "a concept we use at Lumar," and the claims are
hedged with "appears" and "from what we've seen." The series builds toward a
pitch for a GEO analytics stack, so "SEO tools can't measure this stage" is
partly a product argument.

## Key takeaways

1. **Candidate selection decides eligibility, not position.** It is the
   page-level step where a system decides whether a page is a possible
   source for this query at all, before any passage is scored. A page can
   rank well in classic search and still never enter the pool.
2. **Why the stage exists:** scoring every passage of every indexed page per
   query isn't practical, so the system first narrows the search space with
   page-level signals.
3. **Four signal families, weighted by query:**
   - *Lexical:* exact or near-exact matches in the title, H1, headings and
     anchor text are still strong topical cues.
   - *Semantic:* whether the page is genuinely *about* the topic, not just
     mentioning it.
   - *Authority/trust:* weighted most for YMYL. Official documentation,
     government guidance and established publishers are favored.
   - *Freshness:* query-dependent. Evergreen topics tolerate age, while news
     and product updates favor recent sources.
4. **Query-dependent example:** a general car blog can be a candidate for
   "how oil changes work" but is unlikely to be one for "Honda Civic oil drain
   torque," where precision favors manufacturer or specialist sources.
5. **Order of work:** make the page's topic clear, align titles, H1s and
   headings with real queries, establish credibility, and *then* optimize
   passages.

## What this updated

- [[ai-search-reranking-pipeline]]: new "Candidate page selection" section
  mapping this page-level gate onto the retrieval stage, plus the new
  Conflicting Evidence entry on multi-topic pages (this source vs.
  [[google-ai-optimization-guide]]).
- [[geo-diagnostic-checklist]]: check 1 now covers lexical alignment and
  query-dependent freshness.
- [[authority-in-generative-search]]: the YMYL and manufacturer
  ("Civic torque") examples.
