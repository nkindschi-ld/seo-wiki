---
type: source
tags: [seo, aeo]
date_published:
date_ingested: 2026-07-23
origin: raw/articles/google-generative-ai-performance-report.md
---

# Generative AI Performance Report (Search) — Search Console Help

**Citation:** Google Search Console Help. "Generative AI performance
report (Search)."
https://support.google.com/webmasters/answer/16984139?hl=en

No "last updated" date was recoverable from the fetched page; treat as
current guidance as of ingestion (2026-07-23).

## Key takeaways

- Google Search Console has a **dedicated** "Generative AI Performance
  Report," distinct from the general Performance report — purpose-built
  to track impressions from **AI Overviews** and **AI Mode** specifically
  (excludes Search Labs experiments, which remain under active
  development).
- **Dimensions**: pages (canonical URL), countries, dates
  (daily/weekly/monthly, Pacific Time), and devices (desktop/tablet/
  mobile) — the same slicing site owners expect from the standard
  Performance report.
- **Rollout is gradual and threshold-gated**: sites need "sufficient"
  impressions in AI features to see the report, and not all properties
  have access yet.
- Preliminary data is marked with dotted lines and can still shift within
  hours of being shown.
- Only covers impressions, not clicks/CTR explicitly (the summary doesn't
  mention a click metric) — unconfirmed whether click data is included;
  flag for follow-up if a fuller walkthrough source is ingested later.

## What this updates in the wiki

**Refines, does not contradict**, the existing claim (from
[[google-ai-features-appearance-guide]], ingested 2026-07-07) that
AI-feature traffic "shows up in Search Console's Performance report
under the 'Web' search type." Google appears to have since shipped a
**separate, dedicated** report for this rather than requiring site
owners to filter the general Performance report — a more specific
tool than what was documented previously. The general "Web" search-type
filter Google described earlier may still work, but this dedicated
report is now the more precise measurement path.

- Updated [[generative-engine-optimization]] — "Appearing & measuring
  performance" section now mentions the dedicated report.
- Updated [[controlling-ai-feature-inclusion]] — "Measuring the effect"
  section now points to the dedicated report as the preferred tool.
- Updated [[ai-visibility-measurement-methodology]] — noted that the
  "measurement gap" is now partially closed for Google's own AI surfaces
  specifically (AI Overviews/AI Mode), while the gap remains fully open
  for third-party engines (ChatGPT, Claude, Gemini standalone,
  Perplexity), which still expose no native impression data.
- No conflicts — this is a first-party tooling update, not a competing
  claim.
