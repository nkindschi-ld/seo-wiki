---
type: source
tags: [seo, aeo]
date_published: 2026-05-07
date_ingested: 2026-07-22
origin: raw/articles/otterly-url-ai-citations-study-2026.md
---

# The URL AI Citation Study 2026 (Otterly.ai)

**Citation:** Rick Tousseyn. "The URL AI Citation Study 2026." Otterly.ai
Blog, 2026-05-07. https://otterly.ai/blog/url-ai-citations-study/

## What this source is

A large-scale, disclosed-methodology study of **1,028,959 unique URLs**
generating **1,932,200 citation instances** across six AI surfaces
(ChatGPT, Google AI Overviews, Google AI Mode, Perplexity, Gemini,
Microsoft Copilot) over a 24-hour observation window. Uses Pearson
correlation for continuous URL attributes (length, path depth, hyphen
count) and average-citation comparison for categorical attributes (page
type, TLD, query-string presence).

## Key findings

- **URL structural mechanics show near-zero correlation with
  citation frequency**: URL length r = -0.025, domain length r = -0.007,
  path depth r = +0.002, hyphen count r = -0.013. Average cited URLs run
  63 characters, but 40-character and 120-character URLs cite at nearly
  identical rates.
- **Page type is the strongest measured signal**: guide pages average
  2.7 citations (42% above the 1.9 baseline), blog posts and help pages
  2.0 (+5%), news 1.7 (-11%), product/service 1.6 (-16%), pricing 1.5
  (-21%).
- **Clean canonical URLs (no query strings) get 24% more citations**:
  2.1 average citations vs. 1.6 for URLs with query strings. URLs
  containing digits show a similar gap (2.0 vs. 1.6).
- **TLD mostly doesn't matter**: most TLDs cluster at 1.5-1.7 citations
  (.com — 51.3% of the sample — .org, .io, .ai all ~1.7). One outlier,
  .uk at 3.0, is flagged by the study itself as needing longer-term
  validation before treating it as real.
- **Citations follow a steep power law**: median 1 citation per URL,
  mean 1.9, max 965 (a single URL). **15.8% of URLs generate 50% of all
  citations; 20% generate 54%.**
- **Common SEO URL conventions show no citation lift**: year-in-URL,
  question patterns (how-to/what-is), comparison patterns (vs./best-/
  top-), and homepage status were all non-predictive.

## Relationship to existing wiki claims

- **Corroborates, with a different metric, an existing ranking**:
  [[ai-citation-landscape]] already found content-type *portability*
  (cross-engine citation survival) ranks guides/tutorials (2.3%) >
  blogs (1.8%) > category pages (1.6%) > product pages (1.2%) >
  homepages (1.1%) — per [[sej-the-consensus-gap]]. This study's page-type
  *citation-frequency* ranking (guide > blog/help > news > product >
  pricing) lands in the same order using an entirely different
  dataset, metric, and engine set. Independent corroboration, not a
  duplicate measurement.
- **Upgrades an existing unsourced claim**: [[superlines-geo-guide]]
  (no disclosed methodology) claimed AI answers cite only "2-7 domains
  per response," flagged in [[ai-citation-landscape]] as unverified.
  This study's disclosed power-law concentration data (15.8% of URLs →
  50% of citations) is a differently-shaped but much more rigorously
  sourced concentration finding — doesn't confirm the specific 2-7
  number, but gives independent, disclosed-methodology support to the
  general "citations concentrate heavily" claim.
- **Nuance, not a clean contradiction, on URL wording**:
  [[ahrefs-why-chatgpt-cites-pages-2026]] (1.4M ChatGPT prompts) found
  natural-language URL slugs correlate with higher citation (89.78% vs.
  81.11% for non-natural-language URLs). This study found URL
  *structural* mechanics (length, hyphens, digits) don't correlate, and
  specifically that *question-pattern* wording (how-to/what-is) is
  non-predictive — a similar-in-spirit but not identical measurement to
  "natural language." Both could be true simultaneously: whether a
  slug *reads* as natural language (Ahrefs' measurement) may matter
  independently of specific keyword patterns or raw length (this
  study's measurements). Not logged as a formal conflict, but flagged
  as a real nuance worth watching — this study is larger (6 engines vs.
  ChatGPT-only) and its null result on structural mechanics is
  strongly powered (n > 1M URLs).

## Practical takeaway

Don't over-invest in URL micro-optimization (length, hyphens, keyword
stuffing patterns, adding "how-to"/"best"/years). Do invest in: page
*type* (reference/guide content over transactional), clean canonical
URLs without query-string clutter, and reducing duplicate/parameterized
URL variants competing for the same citation.

## See also

- [[ai-citation-landscape]] — the content-type portability ranking this
  study corroborates, and the citation-concentration/natural-language-URL
  sections this study updates.
- [[geo-content-optimization-tactics]] — the actionable tactics this
  study adds (clean canonical URLs) and tempers (URL micro-optimization).
- [[ahrefs-why-chatgpt-cites-pages-2026]] — source of the natural-language-
  URL-slug finding this study nuances.
- [[superlines-geo-guide]] — source of the unsourced "2-7 domains per
  response" claim this study's power-law data indirectly strengthens.
