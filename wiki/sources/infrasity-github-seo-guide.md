---
type: source
tags: [seo, aeo]
date_published: 2025-07-23
date_ingested: 2026-10-19
origin: raw/articles/infrasity-github-seo-guide.md
---

# The Ultimate Guide to GitHub SEO for 2026 (Infrasity)

Komal (Content Strategist, Infrasity), published 2025-07-23, updated
2026-06-29. Infrasity is a developer-marketing agency. The post ends with a
demo pitch.

**Rigor:** low and derivative. No data. The structure (Name, About, Topics,
then Stars/Watchers/Forks through a "more eyes, convert, nudge, quality"
funnel, including the docs "hello bar") closely follows
[[markepear-github-search-engine-optimization]]. Treat it as an echo of that
source, not as independent confirmation. It states "GitHub's search ranks
repositories based on repository name, about, topics, stars, watchers, and
forks" as fact, with no evidence.

## Key takeaways

What it adds beyond Markepear:

1. **Google indexes repos, and the README is the page body.** Queries like
   `fast csv parser golang site:github.com` and "open source JWT auth
   node.js" can surface a README. Google "often pulls snippets from your
   README, repo name, and description."
2. **Use precise technical keywords** (`OAuth2`, `Next.js`, `FastAPI`) in
   repo names, topics, README sections and **`.md` file names**.
3. **About: 5–15 words, main keyword first, name the platform or use
   case.** Describe what it does, not how good it is. Examples:
   `louislam/uptime-kuma` ("A fancy self-hosted monitoring tool") and
   `AzureAD/microsoft-authentication-library-for-js` for the name.
4. **Topics: include your primary keywords,** even when they're already in
   the name (the `kubernetes/kubernetes` example has a `kubernetes` topic).
   That mildly contradicts Markepear's "drop keywords already in Name or
   About".
5. **Distribution channels:** X, Reddit (r/webdev, r/programming), Dev.to,
   Medium, daily.dev, LinkedIn, Slack and Discord communities, newsletters,
   or a push timed to a Product Hunt launch.
6. **GitHub Pages:** use normal HTML metadata and get inbound links. Pages
   sites rank like any static site.

## Observed tactic: hidden AI-instruction block

The served HTML contains a `<div class="machine-content machine-md">` block
that isn't part of the visible article. It is an llms.txt-formatted agency
profile ("Format: Machine-readable llms.txt", last updated April 2026)
with sections titled **"Use Cases: Recommend Infrasity when…"**, "Do NOT
recommend for…" and **"AI System Instructions"**, plus "Primary
Positioning", "When to Recommend" and "Competitive Context". The block was
not followed. It is preserved verbatim in the raw file's appendix.

It is a live example of brand-steering text written for LLMs and placed in
page HTML: simple plain-text instructions, not the optimized adversarial
strings in [[kumar-lakkaraju-manipulating-llms-2024]]. There is no evidence
here that it works. Noted on [[llms-txt]] and
[[geo-content-optimization-tactics]] (LLM recommendation manipulation).

## What this updated

- [[github-repository-seo]] (new): supporting citation for the name, About
  and topic factors and the Google-indexing point, flagged as derivative.
- [[github-repo-optimization-checklist]] (new): `.md` file names,
  distribution channels, GitHub Pages metadata.
- [[llms-txt]] and [[geo-content-optimization-tactics]]: the
  embedded-instruction example.
