---
type: source
tags: [seo]
date_published: 2023-08-31
date_ingested: 2026-07-08
origin: raw/studies/ahrefs-site-audit-study-2023.md
---

# We Studied Over 1 Million Domains to Find the Most Common Technical SEO Issues (Ahrefs)

**Citation:** Stox, Patrick (reviewed by Joshua Hardwick). "We Studied
Over 1 Million Domains to Find the Most Common Technical SEO Issues."
Ahrefs Blog. Published 2023-08-31.
https://ahrefs.com/blog/site-audit-study/
(Methodology: 1,002,165 domains, Ahrefs Site Audit tool; percentages =
share of domains with the issue on at least one page.)

## Key takeaways

- Ranks the 15 most prevalent technical SEO issues by domain
  prevalence: 3XX redirects (95.2%), HTTP→HTTPS redirects (88%),
  missing alt attributes (80.4%), missing/empty meta descriptions
  (72.9%), slow pages (72.3%), title/SERP mismatch (68.5%), pages with
  only one dofollow internal link (66.2%), overlong titles (63.2%),
  links pointing to a redirect rather than the final URL (62.7%),
  missing/empty H1 (59.5%), meta description too short (59.2%),
  incomplete Open Graph tags (56%), meta description too long (54.5%),
  multiple H1 tags (51.3%), missing meta description on non-indexable
  pages (50.8%).
- **Prevalence ≠ priority**: near-universal issues (redirects, HTTPS)
  are mostly benign at low counts; the real risk is redirect
  chains/loops beyond ~10 hops breaking signal consolidation, or a
  misdirected HTTPS→HTTP redirect (>6% of sites).
- **Meta descriptions are not a ranking factor** — Google rewrites
  them in the SERP ~62.78% of the time regardless — so the
  recommendation is targeted fixes on high-traffic/high-differentiation
  pages, not a blanket site-wide rewrite.
- **Multiple/missing H1 tags are low-severity**: multiple H1s have
  been valid HTML5 since 2014 and Google has stated this isn't a
  problem; a missing H1 is a minor issue, not a critical one.
- **Open Graph tags are a social/CTR lever, not an SEO ranking
  factor** — matters only for pages that get shared. Now cross-cited on
  [[open-graph-protocol]].
- Recommends an **impact-effort prioritization matrix**, explicitly
  noting the right call is sometimes to fix nothing if the cost
  outweighs the benefit.

## What this updated

- [[technical-seo-audit-checklist]] — added prevalence data and
  priority calibration (which of these common issues are actually
  worth fixing) to §1 (crawling/indexing) and §4 (code/config).

No conflicts — this reinforces the existing checklist's Semrush-based
guidance with independent large-scale prevalence data and explicit
priority calibration (several commonly-flagged issues, e.g. multiple
H1s and incomplete Open Graph tags, are here explicitly downgraded to
low-priority/non-ranking-factor status). Note this source predates
(2023) most of the wiki's other technical-SEO material (2026) but its
findings are structural/HTML-level, not AI-search-specific, so
recency isn't a concern here.
