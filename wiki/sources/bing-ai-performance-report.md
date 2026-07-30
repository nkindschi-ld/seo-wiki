---
type: source
tags: [seo, aeo]
date_published:
date_ingested: 2026-07-23
origin: raw/articles/bing-ai-performance-report.md
---

# AI Performance in Bing Webmaster Tools — Bing Help Documentation

**Citation:** Bing Webmaster Tools Help. "AI Performance in Bing
Webmaster Tools."
https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c

No "last updated" date was recoverable from the fetched page; treat as
current guidance as of ingestion (2026-07-23). Note: the URL doesn't
match Bing's typical help-article slug pattern and an initial automated
fetch returned no body content — the substance here comes from HTML the
user pasted directly, not an independently re-verified fetch.

## Key takeaways

- Bing Webmaster Tools has a dedicated **AI Performance Report**
  tracking how content is used in AI-generated answers across
  **Microsoft Copilot, AI-generated summaries in Bing, and select
  partner AI integrations**.
- Core metric is **citations**, not impressions — "Total Citations,"
  "Cited Pages," "Average Cited Pages," sliceable by page and by
  "grounding query" (a grouped/generalized phrase representing the
  query context that surfaced the citation, not a literal user prompt).
- Explicitly measures citation frequency only — **not** rankings,
  authority, importance, or a page's role within a given answer.
- Data is sampled/aggregated, not a complete citation log — very
  low/infrequent citations may not surface, and totals can differ
  slightly across views (pages vs. grounding queries vs. time-series)
  because each is independently sampled.
- Citations explicitly **do not represent clicks, traffic, or
  engagement** — a distinct signal from traditional Bing/Search Console
  metrics.
- Four **preview capabilities** extend the report beyond raw counts:
  - **Intents** — classifies grounding queries by query-intent taxonomy
    (Informational, Commercial, Research, Comparison, Planning, etc.)
  - **Topics** — groups related grounding queries into thematic
    clusters (e.g. "Solar Energy")
  - **Citation Share** — your site's % of citations among *all* cited
    sources for a given grounding query (a relative-visibility metric,
    distinct from total-citation volume); does not reveal competitor
    identities
  - **Compare** — overlays a prior time period on the current view for
    before/after trend comparison
- Content best-practices Bing recommends based on this data: align with
  user intent, deepen subject coverage, improve structure/clarity
  (headings, tables, FAQs), support claims with evidence, keep content
  fresh, and maintain cross-format consistency (text/image/other media
  describing the same entities).
- Respects `robots.txt` and other content-owner controls — only
  indexing-eligible content can appear.

## What this updates in the wiki

**Corrects** a prior blanket claim in
[[ai-visibility-measurement-methodology]] that "Bing Webmaster Tools
provide[s] no native AI-impression tracking" — that's no longer
accurate; Bing now has a dedicated first-party tool, paralleling
[[google-generative-ai-performance-report]] for Google.

**Notable divergence from Google's report** (not a conflict, a
methodology difference worth tracking): Google's Generative AI
Performance Report tracks **impressions**; Bing's tracks **citations**
(visible reference/use in an answer) and is explicit that citations are
not clicks/traffic. These are related but distinct units — "how often
you were shown" vs. "how often you were used as a cited source" — and
the wiki should not treat Google-impressions and Bing-citations as
interchangeable when comparing cross-engine visibility.

- Updated [[ai-visibility-measurement-methodology]] — corrected the
  Bing claim, added a Bing-specific native-measurement section parallel
  to the Google one, and flagged the impressions-vs-citations
  terminology distinction.
- Updated [[geo-content-optimization-tactics]] — added a Bing/Copilot
  entry to "Provider-specific tactics," corroborating (not contradicting)
  existing tactics with an official first-party source, plus the
  Intents/Topics/Citation Share framing as new diagnostic angles.
- No claims contradicted beyond the correction above — the "align
  intent / deepen coverage / structure / evidence / freshness /
  consistency" guidance agrees with tactics already catalogued in
  [[geo-content-optimization-tactics]].
