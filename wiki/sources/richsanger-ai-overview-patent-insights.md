---
type: source
tags: [seo, aeo]
date_published: 2024-11-19
date_ingested: 2026-07-11
origin: raw/articles/richsanger-ai-overview-patent-insights.md
---

Rich Sanger, "AI Overview Optimization: Insights from Google's Patent" (Rich Sanger SEO, updated 2024-11-19, referencing US patent 11769017B1).

## Key takeaways

- **Two-stage selection mechanism**: an initial summary is drafted from
  direct-match query results, then each candidate link/citation is
  separately verified via **embedding distance** (semantic similarity
  between the generated summary statement and the source text) before
  inclusion — a more mechanistic patent-based account of why
  [[ipullrank-optimize-for-sge]]'s "Fraggle"/chunk-retrieval framing and
  [[ahrefs-why-chatgpt-cites-pages-2026]]'s semantic-similarity finding
  both hold: citation is a two-step retrieve-then-verify process, not a
  single relevance pass.
- **AI Overviews reuse pre-ranked index results rather than re-crawling/
  re-scoring in real time** — reinforces the wiki's existing
  "retrieval-eligibility is a prerequisite" framing
  ([[how-google-search-works]], [[airops-fan-out-effect-2026]]): you
  cannot get into an AI Overview without first ranking well enough to
  be a retrieval candidate at all.
  **Nuance, not contradiction (2026-08-03)**: [[derivatex-two-googles-one-query-aio-vs-serp-2026]]
  found 65% of AIO citations don't appear in Google's *top-10* organic.
  This doesn't overturn the "reuses pre-ranked results" claim — a page
  can be a ranked retrieval candidate (e.g. position 20) without
  cracking the visible top-10 — but it does bound it: "must be a
  retrieval candidate" is not the same as "must rank top-10," and the
  AIO clearly draws from a wider (and differently-weighted, e.g.
  video-heavy) pool than the top-10 shown beneath it. See that source's
  entry in [[ai-citation-landscape]]'s AIO↔SERP divergence section.
- **Concrete positional-inclusion data**: ranking position 1 for the
  primary query → 53% link-inclusion rate in the AI Overview; position 2
  → ~50%; inclusion drops further down. This is a different, complementary
  metric to [[aio-ctr-impact]]'s query-format AIO-*trigger* rates — that
  table says *which query formats* are likely to show an AIO at all,
  this source says *which rank position* gets linked *within* an AIO
  once triggered.
- **Related/reformulated-query pathway is the bigger lever**: targeting
  adjacent, less-competitive related queries (not just the primary
  keyword) raised link-inclusion from 46% to over 67% in the cited
  research — a concrete number supporting the wiki's existing
  query-fanout-angle guidance
  ([[peec-ai-chatgpt-query-fanouts-2026]]) with Google-AI-Overview-
  specific data.
- **YouTube as a third pathway**, alongside direct-match and related-
  query text ranking — consistent with [[ai-visibility-correlation-factors]]'s
  finding that YouTube mentions correlate strongest with AI-mention
  visibility generally.
- **Evaluation-signal taxonomy** (query-dependent, query-independent,
  user-dependent, related-query/context) gives a structured checklist
  of what the patent claims the system weighs — domain authority,
  inbound link quality, freshness, and source diversity are named
  query-independent factors; author credibility is named explicitly,
  reinforcing [[e-e-a-t-and-page-quality]].
- **Sector concentration**: Health, Finance, and Education show up in
  AI Overviews disproportionately (informational-query-heavy),
  dominated by YouTube/Wikipedia/Investopedia as linked sources for
  informational queries — a concrete example of the wiki's existing
  three-layer source strategy in a specific vertical.

## Updated

- [[geo-content-optimization-tactics]] — added a "patent-based selection
  mechanics" section: two-stage embedding-distance verification,
  position-1/2 inclusion-rate data, and the related-query pathway's
  46%→67% inclusion lift.
