---
type: source
tags: [seo]
date_published: 2022-09-12
date_ingested: 2026-09-23
origin: raw/articles/searchatlas-open-graph-tags-best-practices.md
---

# Open Graph Tags: Implementation & Best Practices (Search Atlas)

**Citation:** Bhan, Manick. "Open Graph Tags Implementation & Best
Practices." Search Atlas blog. Published 2022-09-12, updated 2026-01-26.
https://searchatlas.com/blog/open-graph-tags/

**Rigor note:** a vendor blog (Search Atlas sells an SEO platform). There's
no primary data. The client case studies shown on the page (e.g. +472%
organic traffic) are unrelated to OG and ignored here. The platform list
still includes Google+, so the 2026 update was light.

## Key takeaways

- **"Open Graph is not a ranking factor"** for Google. Its benefit is
  indirect: better share cards → more engagement → more chances to earn
  links.
- Specs as given:
  - Title: 40–60 chars
  - Description: 120–160 chars
  - Image: 1.91:1 with width/height tags
  - `og:type`: `article` for blogs, `website` for other pages
  - `og:locale`: set for non-English pages
- Most common errors: tags missing entirely, and character counts outside
  the recommended range.
- Implementation: a CMS plugin (Yoast on WordPress; Wix and Shopify
  equivalents) or manual edits to the page head.

## What this updated

- [[open-graph-protocol]]: the "not a ranking factor" position. It's the
  "contradicted by" side of the social-signals conflict and the
  alternative spec set in the length/image conflict (both against
  [[stream-open-graph-protocol-glossary]]).
