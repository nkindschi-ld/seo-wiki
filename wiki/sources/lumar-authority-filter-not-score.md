---
type: source
tags: [aeo, seo]
date_published: 2026-09-02
date_ingested: 2026-10-05
origin: raw/articles/lumar-authority-filter-not-score.md
---

# Authority in GEO: It's A Filter, Not a Score (Lumar)

Lumar Editorial Team, Lumar blog, published 2026-09-02 (modified
2026-09-10). Part 5 of Lumar's GEO series, after [[lumar-chunkability]]. It
closes the series with a four-part framework: **Eligibility** (candidate
selection), **Precision** (semantic relevance), **Citability**
(chunkability) and **Safety** (authority).

**Rigor:** no data, sample sizes or method. The query-class table is labeled
"Observed Behavior," but the observations aren't described. The confidence
ratings are Lumar's own self-assessment, not measured effect sizes. Its one
external anchor is Google's E-E-A-T/YMYL weighting statement.

## Key takeaways

1. **Filter, not score.** In SEO, authority is usually treated as a
   comparative score. In generative search, Lumar argues, the question is
   whether a source is suitable to trust for *this* query, and that is
   decided early. A better explanation can't compete if its source was
   excluded before passages were looked at.
2. **The role depends on the query, scaled to how much harm a wrong answer
   could do:**

   | Query type | Authority role | Behavior |
   |---|---|---|
   | Medical / legal / mechanical (YMYL) | Hard gate | Non-authoritative pages often excluded |
   | Technical specs (manufacturer topics) | Hard preference | Official sources dominate |
   | General educational | Strong filter | Boosts but doesn't exclude |
   | Exploratory / lifestyle | Soft filter | Relevance dominates |
   | Opinion / creative | Minimal | Authority often irrelevant |

3. **Signals by Lumar's confidence:**
   - *High:* source provenance (official docs, regulators, institutional
     publishers, first-party manufacturer sources).
   - *Medium:* consistency with trusted sources, citation overlap, topic
     ownership, historical trust.
   - *Lower:* author credentials, `author`/`reviewedBy` structured data,
     engagement. If these count, they are expected to be secondary to
     domain-level trust.

   Its self-rated confidence: authority as an eligibility filter **high**;
   domain-level provenance **very high**; query-dependent enforcement
   **high**; author-credential impact **medium**; exact weighting **low**.
4. **E-E-A-T is a way of thinking, not a formula.** The closest parallels are
   trust and provenance. Brand popularity or link volume alone say little
   about whether a source suits a query.
5. **Smaller sites can still break through** where authoritative coverage
   has a gap, especially on niche or operational queries, where precision,
   semantic uniqueness and chunkability matter more. That only works if the
   gap actually exists.
6. **Strategy:** authority sets the ceiling on where you can compete, and
   relevance and chunkability decide what happens once you're there. Pick
   gaps rather than YMYL head terms you can't optimize your way into.

## What this updated

- New concept page [[authority-in-generative-search]], built around the
  query-class table and the signal-confidence tiers, with this wiki's
  independent corroborating evidence attached.
- [[geo-diagnostic-checklist]]: check 5 now uses the query-class table and
  adds a "choose where to compete" step.
- [[e-e-a-t-and-page-quality]]: a See-also link for how YMYL weighting shows
  up in generative retrieval.

No conflict logged. "Brand popularity says little" sits next to Ahrefs'
strong correlation between branded mentions and AI *mentions*
([[ai-visibility-correlation-factors]]), but the two measure different
outcomes (suitability as a cited source vs. being named in the answer). The
distinction is written up on [[authority-in-generative-search]].
