---
type: playbook
tags: [seo]
updated: 2026-09-04
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

## Map keywords to funnel stage (ToFu/MoFu/BoFu)

Per [[sel-mofu-keywords-2025]] — a funnel-intent layer on top of the mapping
process above. When assigning a query to a page, also tag its **funnel stage**,
since intent-stage determines the content format and CTA, not just the target
URL. Middle-of-funnel (evaluation-stage) keywords are the highest-leverage but
most-neglected band: more volume than bottom-of-funnel branded terms, better
conversion than top-of-funnel awareness terms, and typically lower CPC than BOFU
(a CPC gap between two related terms is itself a useful MoFu-vs-BoFu signal).

- **Five MOFU keyword patterns to look for** when clustering: comparison
  ("X vs Y"), best-of lists ("best X for Y"), feature-driven ("CRM with WhatsApp
  integration"), industry-specific ("accounting software for freelancers"), and
  pain-solution ("how to reduce churn in SaaS"). This generalizes the
  SaaS-specific comparison/features/industries/alternatives taxonomy in
  [[gofishdigital-seo-for-saas]] and [[semrush-saas-seo]] to any vertical — the
  same page types the wiki's listicle/comparison guidance already favors for AI
  citation (see [[listicles-in-ai-search]]), now framed by buyer stage.
- **Link across funnel stages deliberately**: from a MoFu page, link *down* to
  BoFu product/pricing pages, *up* to ToFu educational content, and *laterally*
  to related MoFu pages — a stage-aware application of the internal-linking
  guidance in [[link-and-anchor-text-best-practices]].
- **Measure MoFu on assisted conversions, not direct ones.** MoFu content rarely
  converts on the same visit (evaluation runs days-to-months), so use GA4 Path
  Exploration (enter MoFu page titles at Step +1 to see downstream conversion
  paths) and a multi-touch attribution model (time-decay / position-based /
  data-driven) rather than last-click. Expect higher time-on-page, lower bounce,
  and deeper scroll than ToFu as the MoFu-health signal.

## Tools referenced

Rank tracking: Semrush, Ahrefs, SEOmonitor. Analytics: Google Analytics,
Google Search Console. Keyword research/clustering: Ahrefs, Semrush.
Technical audit: Screaming Frog.

## See also

- [[keyword-research]] — run *before* this playbook to discover and
  prioritize which keywords belong on the map in the first place
  (including AI-era discovery methods like query fan-out and first-
  party-data mining); this playbook assumes the list already exists and
  focuses on page assignment/cannibalization.
- [[topic-cluster-strategy]] — the pillar/subpage structural pattern
  the "topic/pillar-first variant" above is drawn from.
- [[seo-competitive-analysis]] — competitor keyword-gap analysis that
  can surface additional map entries.
- [[search-intent-and-needs-met]] — the parent concept: mapping is
  fundamentally an intent-matching exercise, and most cannibalization
  is two pages competing to serve the same intent.


See [[riseatseven-keyword-mapping-guide]] and [[semrush-keyword-mapping]]
for the full source writeups.
