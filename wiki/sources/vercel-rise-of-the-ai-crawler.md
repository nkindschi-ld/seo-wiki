---
type: source
tags: [seo, aeo]
date_published: 2024-12-17
date_ingested: 2026-07-23
origin: raw/articles/vercel-rise-of-the-ai-crawler.md
---

# The Rise of the AI Crawler (Vercel, 2024-12-17)

**Citation:** Zecchini, Giacomo; Moore, Alice Alexandra; Ubl, Malte;
Siddle, Ryan. "The Rise of the AI Crawler." Vercel Blog, 2024-12-17.
https://vercel.com/blog/the-rise-of-the-ai-crawler

Vercel-first-party dataset: one month of real crawler traffic observed
across Vercel's own hosting network — an actual traffic-log study, not
a vendor survey/opinion piece, though scoped to sites hosted on Vercel.

## Key takeaways

- **Traffic volume** (one month, Vercel network): GPTBot 569M requests,
  Claude 370M, AppleBot 314M, PerplexityBot 24.4M, vs. Googlebot 4.5B —
  combined AI-crawler traffic ≈28% of Googlebot's volume.
- **JavaScript rendering — confirms and quantifies** the existing wiki
  claim that most AI crawlers don't render JS: ChatGPT and Claude fetch
  JS files (11.50% and 23.84% of requests respectively) but never
  execute them. **AppleBot and Gemini are the exceptions**, rendering
  JS via browser-based execution comparable to Googlebot.
- **Geographic operations**: all measured AI crawlers (ChatGPT, Claude)
  operate from U.S. data centers only (ChatGPT: Des Moines, Phoenix;
  Claude: Columbus) — vs. Google's seven-region crawl infrastructure.
  Relevant for IP-allowlisting decisions in WAF/CDN configuration.
- **Content-type preferences**: ChatGPT fetches mostly HTML (57.70%);
  Claude fetches a notably higher share of images (35.17%).
- **Crawl inefficiency**: ChatGPT and Claude hit 404s on ~35% of
  requests (34.82% / 34.16%) and ChatGPT wastes 14.36% of requests on
  redirects — vs. Googlebot's 8.22% 404 rate and 1.49% redirect rate.
  AI crawlers are meaningfully less efficient at navigating sites than
  Googlebot.

## What this updates in the wiki

Agrees with and substantially strengthens existing claims — no
conflicts, but a confidence upgrade is warranted.

- Updated [[technical-seo-audit-checklist]] §5 — the JS-rendering claim
  was previously sourced to
  [[sel-ai-optimization-content-for-search-and-agents]] and flagged
  "undisclosed methodology, treat directionally." This first-party
  traffic-log study **independently confirms** the same
  Gemini/AppleBot-render-JS-others-don't pattern, so the claim is now
  corroborated by two independent sources. Added the crawl-inefficiency
  finding (404/redirect waste) as a new audit item, and the U.S.-only
  data-center geography as a note relevant to IP allowlisting.
- No changes needed to [[robots-txt-strategy]]'s bot-name table (this
  source doesn't rename or add bots), but the data-center geography is
  cross-referenced there for anyone implementing IP-based allowlisting
  rather than user-agent-based rules.
