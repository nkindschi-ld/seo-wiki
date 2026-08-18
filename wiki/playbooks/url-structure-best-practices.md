---
type: playbook
tags: [seo, aeo]
updated: 2026-08-11
---

# URL Structure Best Practices

**Why/when to use this:** Reach for this when designing a new site's URL
architecture, planning a migration, or auditing an existing structure. URL
architecture is **among the hardest website decisions to reverse** — every URL
change is a redirect hop that dilutes link equity *even when done correctly* —
so the goal is to get it durable the first time, not to micro-optimize the
strings. Based on [[visively-url-structure-fundamentals]] (Pedro Dias, ex-Google
Search). The retrieval/canonicalization mechanics behind this live in
[[how-google-search-works]]; the AI-citation-correlation evidence lives in
[[otterly-url-ai-citations-study-2026]]; site-structure/siloing/internal-linking
lives in [[link-and-anchor-text-best-practices]].

## The core principle: design for persistence

The central design question is **"how long will this architecture last without
requiring changes?"** Migrations are costly: PageRank dissipates through
redirect chains, each URL change adding a hop that dilutes link equity. So
prefer structures you won't have to change.

- **Separate volatile information from stable identifiers.** Product *names*,
  campaign names, and category labels change; IDs don't.
  - Fragile: `/summer-collection/beach-dress-blue` — breaks on category rename.
  - Resilient: `/products/beach-dress-blue-1234` — persists through taxonomy
    changes because the stable ID carries the identity.
- **Avoid dates in evergreen-content URLs** (`/2025/guide` ages the URL and
  invites a future migration). Reserve dated paths for genuinely
  time-bound content.
- **Plan for expansion without restructuring existing URLs** — leave room to add
  sections/categories later without renaming what's already live.

## Flat vs. hierarchical — and the flat-architecture myth

**URL depth is not a ranking factor.** The common belief that "flat" URLs rank
better inverts cause and effect: shallow pages aren't important *because* they're
shallow — *"they're shallow because they're important and linked accordingly."*
What actually drives ranking/crawl behavior is **internal linking patterns,
content relevance, and page authority** — not the number of path segments. (This
is the same lesson as [[otterly-url-ai-citations-study-2026]]'s null result:
path depth correlates r ≈ +0.002 with AI citations.)

Choose structure by site size/diversity, not by an imagined depth penalty:

- **Flat** suits small, niche sites where topical context is implicit
  (a single-topic store).
- **Hierarchical** suits large, diverse sites that need to *communicate*
  structure. Make paths **hackable** — a user can strip a trailing segment to
  navigate up a level and land somewhere valid.

### Nielsen usability heuristics (and their tensions)

The six heuristics originate in Jakob Nielsen's "URL as UI"
([[nngroup-url-as-ui-1999]]): memorable+spellable domain · short · easy-to-type
(no special characters) · visualizes structure · hackable · persistent. These
**conflict on purpose**: "short" pulls flat, while "visualize structure" and
"hackable" pull hierarchical. Resolve the tension by site type rather than
chasing all six at once.

Two concrete rules from the same source:

- **Use all-lowercase URLs.** Users can't reliably recall or reproduce
  capitalization, so mixed-case invites failed recall and typos. (Also avoids
  case-sensitivity duplication on some servers.)
- **Never move pages** — permanent URLs prevent linkrot; reserve redirects for
  genuinely temporary→permanent pointers. (The usability-side statement of the
  design-for-persistence principle above.)

**Why readable URLs matter to humans, not just crawlers:** a 2007 Microsoft
Research eye-tracking study (via [[nngroup-url-as-ui-1999]]) found users spend
**~24% of their gaze time on the URL** in a search result, especially when
judging whether the destination is credible. Clean, readable URLs earned clicks
on human-credibility grounds long before they correlated with AI citations
(the +24%-citations-for-clean-canonical-URLs finding in
[[otterly-url-ai-citations-study-2026]]).

## Trailing slashes

Google **treats trailing-slash and non-trailing-slash URLs as separate but
equal** — a file/directory distinction, not a ranking one. The risk is
*duplication*, not ranking: the same content on both variants splits signals.

- **Pick one convention and apply it consistently**; 301-redirect the other
  variant to the canonical form.
- User mental model to keep in mind: trailing slash reads as
  directory/container; no slash reads as file/document; a file extension reads
  as an explicit file type.
- Note server defaults: Apache auto-redirects slash-less directory requests to
  add the slash — make sure your chosen convention matches server behavior so
  you don't create redirects you didn't intend.

## Eliminate internal redirects — link straight to canonicals

**Every internal link must point directly to the canonical URL.** Internal
redirects (linking to a URL that 301s to the real one) cause three problems:

1. **Waste crawl budget** — the crawler spends a fetch on the redirect.
2. **Dilute link equity** — each hop decays PageRank.
3. **Slow page loads** — an extra round trip for users.

This is the link-side complement to the canonicalization guidance in
[[technical-seo-audit-checklist]] (consolidate duplicate URL variants, fix
redirect chains) — that page audits redirects server-side; this rule prevents
you from *authoring* internal redirects in the first place.

## Keywords and category paths in URLs

- **Keywords in URLs give only minor relevance signals** — use **descriptive
  slugs, but don't keyword-stuff.** Corroborated from the AI side by
  [[otterly-url-ai-citations-study-2026]] (length, hyphens, digits, and
  question/comparison keyword patterns all near-zero correlation with citation)
  and mechanistically by [[lexical-ranking-tf-idf-bm25]] (a term's payoff
  saturates; the URL isn't where TF accumulates).
- **Category paths in product URLs** — either including or omitting them works;
  decide by **how often your taxonomy changes.** Frequently-reorganized
  catalogs favor stable-ID URLs (`/products/…-1234`) that survive recategorization; stable taxonomies can afford descriptive category paths.

## Checklist

- [ ] Chosen a trailing-slash convention and 301-redirected the other variant.
- [ ] URLs built on stable identifiers, with volatile names/dates kept out of
      evergreen paths.
- [ ] Structure (flat vs. hierarchical) chosen by site size/diversity, not a
      depth-penalty myth; hierarchical paths are hackable.
- [ ] All internal links point directly to canonical URLs (no internal
      redirects).
- [ ] Descriptive, non-stuffed slugs; **all-lowercase**.
- [ ] Product-URL category-path decision made against taxonomy-change frequency.
- [ ] Migration plan (if any) minimizes redirect hops and avoids chains.

## See also

- [[how-google-search-works]] — canonicalization and the crawl/index/serve
  pipeline these URL rules serve.
- [[otterly-url-ai-citations-study-2026]] — 1M+-URL empirical evidence that URL
  micro-structure barely correlates with AI citations, while clean canonical
  URLs (no query strings) get ~24% more — the AI-era corroboration of "design,
  don't micro-optimize."
- [[technical-seo-audit-checklist]] — server-side canonicalization/redirect
  auditing that complements this authoring-side guidance.
- [[link-and-anchor-text-best-practices]] — internal linking, siloing, and
  topic clusters (the actual drivers of crawl/authority that URL depth is often
  mistaken for).
- [[content-pruning-playbook]] — redirect discipline when removing/consolidating
  pages.
- [[nngroup-url-as-ui-1999]] — Jakob Nielsen's foundational "URL as UI"; the
  primary source for the usability heuristics, the all-lowercase rule, and the
  URL-credibility gaze-time data.
