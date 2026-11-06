---
type: concept
tags: [seo]
updated: 2026-10-08
---

# Link Building

Link building is the practice of acquiring hyperlinks from external
websites that point back to your own pages. Search engines treat these
links as two things at once: a **discovery mechanism** (how a crawler
finds a page it doesn't yet know about) and a **ranking signal** (a "vote
of confidence" from the linking site, per Google's original PageRank
model). See [[how-google-search-works]] for the crawling side and
[[traditional-seo-ranking-factors]] / [[classic-seo-ranking-factors]] for
where backlinks sit among classic ranking correlates (moderate — weaker
than topical text relevance, but meaningful).

Link building sits alongside technical SEO, on-page optimization, content
quality, and UX as one of the core pillars of classic SEO — it does not
substitute for the others. Manipulative link-acquisition tactics (link
farms, exact-match anchor schemes, paid links at scale) triggered Google's
Penguin updates (2012+), which specifically penalize low-quality and
over-optimized link building. See [[ahrefs-anchor-text-2020]] for why
even legitimate anchor-text engineering barely moves rankings and risks a
penalty.

## The four ways links get built

Per [[ahrefs-link-building]]:

1. **Adding links** — manually placed on social profiles, directories,
   review sites, forums. Low effort, minimal SEO value individually, but
   useful as "foundational links" for a brand-new site with no link
   profile yet ("a few dozen foundational links" as a starting point).
2. **Asking for links** — outreach-driven: guest posting, the Skyscraper
   technique, resource-page requests, broken link building, image
   attribution requests, HARO/journalist-request contributions, unlinked
   brand-mention conversion, PR-driven coverage. See
   [[link-building-outreach-tactics]] for the tactical playbook.
3. **Buying links** — paying for placement. Risky: violates Google's spam
   policies, can trigger manual/algorithmic penalties, and often wastes
   spend on links that don't move rankings anyway.
4. **Earning links** — organic backlinks that accrue because the content
   itself is genuinely link-worthy: proprietary research/data, original
   experiments, thought leadership, industry surveys, breaking news.
   [[moz-beginners-guide-link-building]]'s core framing: "people link to
   web pages that are interesting and useful," and all link building
   requires "something of value to build links to" in the first place —
   outreach amplifies a linkable asset, it doesn't manufacture one from
   nothing.

## Five link quality metrics

Per [[ahrefs-link-building]], not all links are worth the same:

- **Authority** — links from established, well-known sites carry more
  ranking weight (Domain Rating and similar third-party metrics
  approximate this).
- **Relevance** — topical alignment matters (a fitness-source link
  benefits a health site more than an automotive-source link would),
  though sensible cross-topic links still have value.
- **Anchor text** — see [[link-and-anchor-text-best-practices]]'s
  backlink-anchor-text section: every anchor type shows weak-to-negligible
  ranking correlation on its own, and *manipulating* your anchor-text
  ratio is the actual risk, not the anchor wording itself.
- **Placement** — in-content/editorial links carry more weight than
  footer or sidebar placements, tracking with click-through likelihood
  (the "reasonable surfer" model — see
  [[link-and-anchor-text-best-practices]]). This still holds for
  *acquired backlinks*, where an editorial in-content placement signals
  genuine endorsement and a sitewide footer link does not. For a site's
  own *internal* links the same hierarchy is contested — John Mueller
  says Google doesn't differentiate by placement; see that playbook's
  Conflicting Evidence section and [[footer-optimization]].
- **Destination** — homepage links are the easiest to acquire; getting
  links (or link equity) to deeper "money pages" typically requires
  earning links to a linkable asset and then routing authority internally
  — see [[link-and-anchor-text-best-practices]]'s internal-linking
  section.

## Realistic expectations

- Cold outreach success rates are low: **~5% reply/placement rate from
  100 emails** is a typical professional benchmark
  ([[ahrefs-link-building]]).
- Prior relationships dramatically outperform cold outreach — this is
  echoed independently in [[crawling-mondays-link-building-outreach-2020]]
  as a "key to outreach success."
- A link's SEO/authority value and its referral-traffic value are
  separate things and don't always correlate — a single high-authority
  placement (e.g. a major publication) can generate very little direct
  click traffic while still being valuable for authority transfer. This
  tension came up directly in viewer discussion of
  [[crawling-mondays-link-building-outreach-2020]].

## Conflicting Evidence

- **Claim**: third-party authority metrics (DR/DA and similar) are a
  meaningful measure of link quality and a sensible prospect filter.
  - Supported by: [[ahrefs-link-building]] (authority as the first of
    five quality metrics) and [[pitchbox-link-prospecting-hacks]]
    (metrics standards as qualification question #1).
  - Contradicted by: [[dejan-link-building-outreach-ai-search]]
    (2026-10-06) — DA/PA-style scores are "made up by a SaaS company,"
    approximate Google's link authority "at best," and cause good links
    to be refused; integration quality is what determines a placed
    link's value.
  - **Current best guess (unresolved)**: both sides have a point. These
    metrics are vendor proxies, not Google signals (note Ahrefs sells
    one), so don't reject a relevant, well-integrated link on score
    alone. But DEJAN is a single practitioner selling an alternative
    tool. Use authority metrics as a coarse filter, not a gate, and
    weight integration/relevance at least as heavily.

- **Claim**: outreach-acquired links are productive (at a ~5% cold
  success rate) and worth pursuing at scale.
  - Supported by: [[ahrefs-link-building]],
    [[link-building-outreach-tactics]] benchmarks.
  - Contradicted by: [[dejan-link-building-outreach-ai-search]]
    (2026-10-06) — "most outreach-based links are ignored, or treated
    as a small negative signal," because poor integration is
    detectable by Google's spam team and algorithms.
  - **Current best guess (unresolved)**: these aren't strictly
    incompatible — Ahrefs measures placement *rate*, DEJAN asserts
    placement *value*. DEJAN's claim is unmeasured (no ranking data,
    proprietary detector with an admitted false positive), but it
    aligns with Google's long-standing link-spam stance. Treat
    integration quality as the deciding factor in whether an outreach
    link is worth having; see [[editorial-link-integration]].

## See also

- [[editorial-link-integration]] — making a placed link read as
  editorial: the "who wanted the link?" test, four rules, link-desire
  placement.

- [[link-building-outreach-tactics]] — the actionable playbook: prospecting
  hacks, outreach process, and common mistakes to avoid.
- [[link-and-anchor-text-best-practices]] — link markup, anchor text
  writing, and internal linking mechanics (a different layer: what you do
  with a link once you have it, or with links within your own site).
- [[traditional-seo-ranking-factors]] / [[classic-seo-ranking-factors]] —
  backlinks' measured place among classic ranking signals.
- [[ahrefs-anchor-text-2020]] — why anchor-text engineering doesn't work
  and risks penalty.
