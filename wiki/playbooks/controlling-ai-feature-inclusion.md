---
type: playbook
tags: [seo]
updated: 2026-07-23
---

# Controlling AI Feature Inclusion (Google Search)

**Why/when to use this:** Use this when you want to *limit or exclude*
your content from Google's AI Overviews/AI Mode — the opposite goal of
[[geo-content-optimization-tactics]], which is about maximizing
inclusion. Relevant if you have content you don't want summarized/quoted
directly in an AI-generated answer (e.g. to preserve click-through, or
for licensing/legal reasons).

Per [[google-ai-features-appearance-guide]] (and the earlier
[[google-succeeding-in-ai-search-2025-05]], which states the same
guidance), these are the available controls:

## Options, from most to least aggressive

1. **`noindex`** — removes the page from Google Search entirely,
   including AI features. Use only if you don't want the page in Search
   at all, not just excluded from AI summaries.
2. **`robots.txt` disallow** — blocks Googlebot from crawling the page
   entirely. Also removes it from regular Search results, not just AI
   features.
3. **`nosnippet`** — prevents Google from showing any text/video snippet
   for the page anywhere in Search, including AI features, while the page
   can still be indexed and linked to.
4. **`data-nosnippet`** — HTML attribute for excluding specific sections
   of a page from snippets, without affecting the rest of the page.
5. **`max-snippet:[number]`** — caps the snippet length Google can show,
   including within AI features, without fully disabling snippets.

## Checklist

- [ ] Do you want the page out of Search entirely, or just out of
      AI-generated summaries? (`noindex`/`robots.txt` vs. `nosnippet`)
- [ ] Is it the whole page or just specific sections that shouldn't be
      quoted? (`nosnippet` vs. `data-nosnippet`)
- [ ] Would capping snippet length (`max-snippet`) meet your goal instead
      of a full block, preserving more visibility?

## Measuring the effect

Per [[google-ai-features-appearance-guide]], AI-feature traffic shows up
in Search Console's Performance report under the **"Web"** search type —
use this to check whether your control directives are having the
intended effect, and to see baseline AI-feature click volume before
applying any restriction.

**Preferred tool as of [[google-generative-ai-performance-report]]**:
Search Console's dedicated **Generative AI Performance Report** tracks
AI Overviews/AI Mode impressions specifically (by page, country, date,
device), giving a cleaner before/after read on a control directive's
effect than filtering the general Performance report. Availability is
gradual and gated on sufficient AI-feature impressions.

## See also

- [[technical-seo-audit-checklist]] — the opposite goal: verifying AI
  crawlers (GPTBot, ChatGPT-User, Claude-Web, etc.) *aren't
  accidentally* blocked in robots.txt, for sites that want inclusion
  rather than exclusion.
