---
type: source
tags: [seo, aeo]
date_published: 2025-03-25
date_ingested: 2026-07-23
origin: raw/articles/seoclarity-track-ai-search-traffic.md
---

# How to Track AI Search Traffic to Your Site in GA4 (seoClarity, Mark Traphagen)

**Citation:** Traphagen, Mark. "How to Track AI Search Traffic to Your
Site in GA4." seoClarity Blog, 2025-03-25.
https://www.seoclarity.net/blog/track-ai-search-traffic

## Key takeaways

- Cites "some industries experiencing over a 700% spike" in AI-search
  referral traffic — no industry/timeframe specifics given, so treat as
  a directional/anecdotal figure, not a rigorous benchmark.
- Walks through a concrete **GA4 UI method** for isolating AI-referral
  traffic: build a Traffic Acquisition detail report, add a
  Session Source/Medium column, and apply a **"Matches Partial Regex"**
  filter with AI engine names joined by `|`. Names ChatGPT, Perplexity,
  Claude, and Gemini as the sources to track, but does **not** supply an
  exact regex string or source/medium values — less specific than the
  regex pattern already in the wiki from [[sel-integrate-geo-with-seo]].
- Describes **seoClarity's "AI Search Visibility"** report (part of its
  "Clarity ArcAI" platform) as a third commercial tool in this space: it
  benchmarks brand presence in AI search results per topic against
  competitors and surfaces content gaps where the brand isn't surfacing
  — same category as [[wholewhale-ai-brand-footprint-measurement]]'s
  Trakkr/Evertune, but vendor content promoting seoClarity's own product,
  so treat feature claims as directional/marketing rather than
  independently verified.

## What this updates in the wiki

Agrees with and extends existing guidance — no conflicts.

- Updated [[geo-content-optimization-tactics]] — added this source's
  GA4 report-building walkthrough (a UI-level "how," complementing the
  existing regex-string "what") and the 700%-spike anecdote to
  "AI-referral traffic and citation-monitoring automation."
- Updated [[ai-visibility-measurement-methodology]] — added seoClarity's
  AI Search Visibility to the Tool Landscape section alongside
  Trakkr/Evertune.
