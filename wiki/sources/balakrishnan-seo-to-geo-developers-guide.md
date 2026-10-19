---
type: source
tags: [aeo, seo]
date_published: 2025-11-02
date_ingested: 2026-10-19
origin: raw/articles/balakrishnan-seo-to-geo-developers-guide.md
---

# From SEO to GEO: A Developer's Guide to Optimizing for AI Search (Balakrishnan)

Somanath Balakrishnan (H4Tech), LinkedIn Pulse, published 2025-11-02
(modified 2026-04-10). Links to a companion boilerplate repo and a Part 2 on
Medium (not ingested).

**Rigor:** low. A how-to with code samples and no data. Its "AI models love
X" claims aren't sourced. The React 18 vs. 19 benchmark table is an
**illustrative template**, not real results, so don't cite it. It is ingested
as a supporting citation only. Almost everything here is already in
[[geo-content-optimization-tactics]] with better evidence.

## Key takeaways

1. **The framing:** SEO optimizes for clicks, GEO for citations ("be the
   best source, not the best result"). Technical SEO basics (schema, clean
   HTML, speed) still apply.
2. **Seven tactics for developer content:** semantic HTML5 with
   `<time>`/`rel="author"`; `TechArticle` JSON-LD with a `citation`
   array; FAQ sections marked up with `FAQPage` microdata; self-documenting
   code examples (descriptive names, JSDoc, `@example`); API reference pages
   with endpoint, request, response, error and usage code; `HowTo` schema
   for tutorials; and **original benchmarks**, which you'll be cited for
   "every time" if you're the only source.
3. **How to test:** ask the assistants directly, watch AI referral traffic,
   track brand mentions (Brand24, Mention) and validate schema (Rich Results
   Test, Schema Markup Validator).

## How it fits the wiki

- The **benchmark** advice agrees with the stronger evidence in
  [[geo-content-optimization-tactics]] ("Publish citation-ready primary
  research/benchmarks", from
  [[growth-memo-why-most-original-data-never-gets-cited]]). Added as
  support.
- The schema advice is broadly consistent with the correlational schema
  lift in [[airops-fan-out-effect-2026]]. The page doesn't mention that
  Google cut back FAQ and HowTo *rich results* in August 2023 (FAQ limited
  to authoritative government and health sites, HowTo dropped). That comes
  from general background, not an ingested source, and the wiki doesn't
  cover it yet: a gap for the next lint. The markup can still help as
  machine-readable structure, so no conflict was logged.
- The code-example and API-doc advice overlaps with what makes docs usable
  by coding agents ([[optimizing-for-coding-agent-recommendations]], point
  3), from a citation angle instead of an agent-execution angle.

## What this updated

- [[geo-content-optimization-tactics]]: supporting citation on the
  benchmark section.
- [[github-repository-seo]]: listed under "See also" for developer-content
  GEO beyond the repo itself.
