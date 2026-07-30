---
type: playbook
tags: [seo]
updated: 2026-07-24
---

Why / when to use this: before investing in content or internal linking,
confirm each priority page has a clear, non-overlapping keyword
assignment. Keyword mapping turns "which page should rank for this
query" from a guess into a maintained record, and is the diagnostic tool
for keyword cannibalization (see [[link-and-anchor-text-best-practices]]
for the internal-linking side of site structure, and
[[entity-based-seo-implementation]] for the entity-level version of the
same cannibalization problem).

## What keyword mapping is

Pairing target keywords to their intended landing pages, so the right
page ranks for the right — ideally conversion-relevant — keyword.
Benefits: informs internal linking, gives precise SEO measurement,
supports stakeholder reporting, and speeds up diagnosis when a page's
rankings drop.

## Build process

1. **Identify priority pages** — pull ~12 months of organic
   landing-page data from Google Analytics (sessions, conversions,
   conversion rate), filtered to target-country organic traffic. Strip
   non-business-critical pages (testimonials, policy pages, irrelevant
   blog posts). Land on roughly 20 priority pages.
2. **Establish one seed keyword per page** — usually visible in the
   URL. Validate against Google Search Console top queries, a keyword
   research tool (volume/difficulty/intent), and PPC search-term data.
   Balance volume, difficulty, and conversion potential rather than
   chasing raw volume.
3. **Expand to ~10 keyword variations per page** — mine Google Ads
   search-term reports and GSC ranking queries, then cluster with
   Ahrefs/Semrush. Check the SERP for each variation: does intent match
   the page, do competitors hold those spots, is ad density high
   (a commercial-intent signal worth prioritizing)?
4. **Build and maintain the map** — one spreadsheet (or rank-tracker
   tags) per keyword group per page. Track group-level performance
   trends, not individual keyword rank in isolation — a single keyword
   dipping while the group holds is noise; the group trending down is
   signal.
5. **Turn gaps into an optimization roadmap** (see below).

**Topic/pillar-first variant** (Semrush): instead of starting from
existing GA traffic, start from broad topic areas for your niche, then
cluster keywords under a pillar-page/subpage structure (Semrush's
Keyword Strategy Builder automates this), filter by search
intent/volume/KD%, and assign each pillar/subpage a target URL —
marking it "To optimize" (page exists) or "To create" (gap). Same
outcome as steps 1-5 above, useful when you're mapping a site/section
from scratch rather than auditing existing traffic.

**On-page + internal-linking tactics once a page is mapped**: place the
primary keyword in the title tag, meta description, H1, and body;
secondary keywords naturally in body copy and subheadings. When adding
internal links, reference the keyword map so anchor text stays
keyword-relevant and doesn't inadvertently point multiple pages at the
same query (see [[link-and-anchor-text-best-practices]]).

## Diagnostic roadmap: three failure modes

- **Missing content** — an important keyword in the map has no
  dedicated page. Create one rather than trying to force an
  unrelated existing page to rank for it.
- **Non-ranking content** — a page exists and is mapped but isn't
  ranking. Work through, in order: technical audit (robots.txt
  blocks, stray `noindex`, non-200 responses, page-experience issues —
  see [[technical-seo-audit-checklist]]), content-relevancy review
  against the mapped keyword's intent, internal-linking gaps (does
  anything link to this page with relevant anchor text? see
  [[link-and-anchor-text-best-practices]]), and competitive
  content benchmarking against ranking pages.
- **Keyword cannibalization** — multiple pages are mapped to (or
  independently ranking for) the same query. Either consolidate the
  weaker page into the stronger one (redirect), or deliberately
  reoptimize one page toward a distinct long-tail variant so the two
  stop competing. This is the same failure mode
  [[entity-based-seo-implementation]] addresses at the entity level:
  one authoritative page per entity/topic, not several splitting
  authority.

## New-feature launch content: don't seed-keyword on the product name

When mapping keywords for a new/branded feature-launch page (e.g. a
product blog post or explainer for a just-launched capability), check
actual search volume on the literal feature name before using it as the
seed keyword — it's often near-zero for months or years after launch,
consistent with [[seo-aeo-geo-search-demand-trends]]'s finding that
newly-named disciplines start at ~zero volume. Map the page instead to
the broader category terms buyers are already searching (e.g. a
prompt/model optimization feature should target "prompt optimization,"
"llm evals"/"llm as a judge," or "guardrails ai," not just its own
product name) — keep the product name as an entity mentioned throughout
the page, not the primary target keyword, and revisit the seed keyword
once/if the feature name itself starts accruing volume.

## Tools referenced

Rank tracking: Semrush, Ahrefs, SEOmonitor. Analytics: Google Analytics,
Google Search Console. Keyword research/clustering: Ahrefs, Semrush.
Technical audit: Screaming Frog.

See [[riseatseven-keyword-mapping-guide]] and [[semrush-keyword-mapping]]
for the full source writeups.
