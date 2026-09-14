---
type: playbook
tags: [seo]
updated: 2026-09-10
---

# Link and Anchor Text Best Practices

Why/when to use this: apply during content authoring, template/CMS
audits, and technical SEO reviews — link markup and anchor text quality
directly affect whether Google can discover a page at all (see
[[how-google-search-works]]'s crawling stage) and how it interprets what
the linked page is about. Based on [[google-links-crawlable]],
[[ahrefs-internal-links-for-seo]], [[yoast-internal-linking-for-seo]], and
[[ahrefs-beginner-guide-technical-seo]].

## 1. Make links crawlable

Google only reliably crawls a link if it is a real `<a>` HTML element
with an `href` attribute containing a resolvable URL.

**Use:**
- `<a href="https://example.com/stuff">`
- `<a href="/products">` or `<a href="./products/category/shoes">`
- `<a href="/products.php?id=123">`
- JS-inserted links are fine *if* they render as real `<a href>` markup
  — verify with the URL Inspection Tool.

**Avoid:**
- `<span href="...">` or other non-anchor elements styled as links.
- Framework-specific routing attributes alone, e.g. `<a routerLink="...">`
  with no `href`.
- `onclick`-only navigation with no `href`.
- `javascript:` pseudo-URLs (`href="javascript:goTo('products')"`).

## 2. Write good anchor text

- **Test**: read the anchor text alone, out of context — it should still
  make sense and describe the destination.
- Be descriptive, reasonably concise, and relevant to both the page it's
  on and the page it links to.
- **Avoid** generic text: "click here," "read more," "website,"
  "article."
- **Avoid** keyword stuffing — write naturally; ask whether the reader
  actually needs each keyword to understand the next page.
- **Vary anchor text** across multiple links to the same page using
  natural phrasing variations (e.g. "email marketing strategies,"
  "building subscriber lists," "effective email campaigns" all pointing
  to the same guide) rather than repeating one exact phrase.
- **Avoid** excessive length — trim to the specific, load-bearing part
  of the sentence.
- **Avoid** chaining multiple adjacent links with no separating context
  (readers can't tell them apart, and each loses its own descriptive
  text).

## 3. Anchor text fallbacks

- Empty link text → Google falls back to the `title` attribute if
  present.
- Image links → Google uses the image's `alt` attribute as anchor text.
  Always write descriptive `alt` text on linked images, not `alt=""`.

## Backlink anchor text: don't manipulate it

Per [[ahrefs-anchor-text-2020]] (384,614 pages / 19,840 keywords study
+ a 16,000-page follow-up) — distinct from the internal-linking
guidance above, this covers **external/backlink** anchor text
specifically:

- **Every anchor-text type shows weak-to-negligible ranking
  correlation**, even exact-match (Spearman ~0.14-0.19). Random/
  generic anchors and keyword-relevant *surrounding* link text
  correlate even less (down to a slight negative). Don't expect
  building keyword-rich backlink anchors to move rankings much even if
  you could do it safely.
- **Core rule: don't try to manipulate your backlink anchor text ratio
  at all.** Legitimate, naturally-earned backlinks give you little to
  no control over anchor text anyway — sites link to you in their own
  words. Attempting to engineer a specific anchor-text mix at scale
  typically requires manipulative tactics (e.g. PBNs) and risks a
  Penguin-style penalty (Google's 2012 Penguin update specifically
  targeted overly-aggressive exact-match anchor link building).
- **Exception: guest blogging.** Since you write the anchor text
  yourself there, deliberately choose a branded or generic anchor over
  a keyword-rich one — a keyword-rich self-placed anchor is a common
  manipulation signal.
- **Don't over-index on one target keyword's anchor text anyway** —
  on average only ~22% of a page's organic traffic comes from its
  single main target keyword; most comes from long-tail variations
  Google matches independently of exact anchor phrasing.

## Link recovery and discovery: High-impact quick wins

Per [[ahrefs-beginner-guide-technical-seo]], two specific tactics deliver
disproportionate value and are worth high priority:

**Reclaim lost links via 301 redirects** (highest-impact single tactic)
- When old URLs die or are moved, a 301 redirect to the current equivalent
  URL transfers link equity and restores broken backlinks.
- A single redirect can restore hundreds of links from multiple domains
  that were pointing to the old URL.
- Priority: audit any URL restructures, product name changes, or content
  consolidations in the past 2+ years for missed redirect opportunities.

**Add contextual internal links to content you already rank for**
- Identify pages where you rank well but get little traffic (e.g., a page
  at position 3-5 in search results for a keyword that gets few clicks).
- Find contextual opportunities to link to that page from your other pages
  on related topics, using natural anchor text on keywords you already rank
  for on the source page.
- Tools like Ahrefs Site Audit's "Internal Link Opportunities" feature can
  identify these systematically.

## 4. Internal linking

- Every page you care about should have a link from at least one other
  page on the site — orphan pages are a discovery risk (see
  [[how-google-search-works]]'s URL-discovery step) and get no PageRank
  distribution.
- Link contextually: point to resources on the site that actually help
  the reader understand the current page. Gael Breton: "as long as it
  contextually makes sense to link to another page of your site, you
  should do it."
- **Site structure**: use a top-down pyramid hierarchy — homepage → main
  category → subcategory → individual page — keeping every page within
  ~3 clicks of the homepage. John Mueller: this "helps us a lot more to
  understand the context of individual pages within the site." Reinforce
  with breadcrumbs (Google treats breadcrumbs as normal links for
  PageRank purposes).
- **Siloing + topic clusters, combined**: use clean folder-based URL
  structure (silos) but don't let it block contextual cross-topic
  linking — strict silos that forbid inter-topic links sacrifice
  authority distribution and relevance. Layer topic clusters (pillar
  pages reciprocally linked to subtopic pages) on top.
- **Link placement ("reasonable surfer" model)** — *contested, see
  Conflicting Evidence*: link value is often said to correlate with
  click likelihood, giving in-content/editorial links (highest) >
  navigation/breadcrumbs (medium) > footer/deep sidebar links (lowest).
  Google's John Mueller has since said Google does *not* differentiate
  by placement. Practical guidance either way is unchanged: put your
  most important links early in the content and above the fold, since
  that's better for readers regardless — but don't treat footer links
  as worthless (see [[footer-optimization]]).
- **Prioritize high-value pages**: identify pages that represent core
  business value (key products, cornerstone content) and link to them
  prominently and often.
- **Cornerstone content, two-way linking**: designate your most
  comprehensive article on a topic as cornerstone content. Link shorter/
  supporting posts *to* it, and link back *from* it to the relevant
  supporting posts — not just one-directional cluster→pillar linking.
- **Taxonomies as linking hubs**: category and tag pages can serve as
  internal-linking hubs alongside pillar pages, signaling topical
  structure to Google (e.g. linking into a "Technical SEO" tag page).
- **Related/popular posts modules**: end-of-article "related posts"
  sections and sidebar/footer "popular posts" widgets distribute link
  equity to top-performing pages and reduce bounce rate.
- **Link count**: no numeric target — follow Google's guidance (see
  "Conflicting Evidence" below) and link as much as genuinely serves the
  reader. Don't cap at an arbitrary count like Ahrefs' "3-5."
- **During content refreshes**: add links from newly published content
  back to (and from) relevant older pages; use high-authority "power
  pages" to pass authority to newer or underperforming pages; build
  topic clusters retroactively by establishing a pillar page with
  reciprocal links once enough content exists on a subject.
- **When to split a long-form page into a topic cluster**: diagnose with
  Google Search Console by mapping which keywords rank against which
  section of the page — if rankings degrade sharply deeper into the
  article (e.g. the first section capturing the large majority of
  top-10 keyword rankings, later sections capturing few or none), that
  section is a candidate to split into its own subpage rather than stay
  buried in the long-form original. Case study (Schmitt, 2020/2023):
  splitting a 3,500-word tutorial into a 5-page pillar+subpage cluster
  took weekly pageviews from ~50-80 to ~2,000 (1000% growth, 16,000
  pageviews over 5 months); one subpage that had zero top-10 rankings
  as part of the original article became a top performer once split
  out — evidence that page format/structure, not just content quality,
  drives visibility. Build workflow: map keywords to sections (GSC) →
  keyword-gap research → rewrite titles/headings around the keyword
  data → hierarchical URLs (`/pillar-topic/subtopic/`) → bidirectional
  pillar↔subpage linking → publish and 301-redirect the original URL to
  the new pillar. Best suited to tutorial-style content with distinct,
  separable search intents per section — not every long-form page
  benefits from splitting. See [[samuelschmitt-topic-cluster-case-study]].
  For the full build-from-scratch process (not just the split-an-
  existing-page path), see [[topic-cluster-strategy]].
- **Pagination**: use real `<a href>` elements, never JS-only buttons or
  `onclick` handlers (crawlers struggle to execute JS reliably — see
  §1). Each paginated page should canonicalize to itself, never to page
  1, since paginated pages contain different content.
- **Crawler accessibility**: keep internal links dofollow by default.
  Reasonable exceptions: login pages, admin sections, and filter/facet
  URLs that would otherwise create duplicate-content URL bloat. Audit
  for accidental nofollow on internal links.

### Internal link auditing workflow

1. **Fix broken internal links**: find 4XX pages with internal
   references (site-crawl tooling); 301-redirect if the page has
   external backlinks, otherwise just remove/repoint the link.
2. **Find orphan pages**: pages with zero inbound internal links —
   prioritize fixing ones that already get organic traffic (via
   sitemap/external links) since internal linking can amplify existing
   performance.
3. **Find new internal-link opportunities**: keyword/topic-overlap
   analysis between existing pages can surface non-obvious, contextually
   relevant linking opportunities to important pages.

### Pre-deployment evaluation of internal-link interventions

Before publishing a batch of new internal links, it's possible to
evaluate the proposed changes against a multi-objective score instead
of relying on manual judgment alone or waiting for a live A/B test to
reveal the effect:

- Model the site as a directed link graph, embedded within its larger
  host/link-ecosystem context (not evaluated in isolation) — authority
  propagation from a batch of new links interacts with the site's
  existing external-link environment.
- Score each candidate batch of links jointly across at least: authority
  yield (marginal gain per link), authority volatility (how stable the
  predicted effect is), the down/up ratio (are you concentrating
  authority gains by draining it from other pages, or genuinely growing
  it), and semantic-coherence change (topical relevance between newly
  linked pages) — no single metric is sufficient on its own.
- **Expect a real tradeoff, not a free win:** research on this method
  found automated link-candidate selection produces stronger authority
  redistribution but at a semantic-coherence cost, while human/expert
  selection better preserves topical coherence — and *every* tested
  intervention, including expert-selected ones, produced some negative
  coherence change. Adding links beyond a site's original architecture
  has an inherent cost; the question is how much you're willing to pay
  for how much authority gain.
- Treat this as pre-deployment triage, not a replacement for editorial
  review — the framework this is drawn from explicitly excludes
  behavioral signals (clicks, impressions, crawl frequency) and hasn't
  been validated against live ranking/traffic outcomes.
- Full methodology: [[webknograph-gnn-internal-linking-2026]].

## 5. External linking

- Don't avoid linking out — external links to good sources (citations)
  help establish trustworthiness.
- `rel` attribute usage:
  - `nofollow` — for sources you don't trust or don't want to vouch for.
    Not meant to be applied blanket to every external link.
  - `sponsored` — for any paid/compensated link.
  - `ugc` — for user-generated content links (forum posts, comments,
    Q&A answers).

## Checklist

- [ ] All important links render as real `<a href="...">` markup (check
      rendered DOM for JS-inserted links).
- [ ] No links depend solely on `onclick` or `javascript:` hrefs.
- [ ] Anchor text is descriptive and makes sense out of context — no
      "click here" / "read more."
- [ ] No keyword-stuffed or excessively long anchor text; varied phrasing
      across multiple links to the same page.
- [ ] No unbroken chains of adjacent links.
- [ ] Linked images have descriptive `alt` text.
- [ ] Every important page has at least one internal inbound link (no
      orphan pages).
- [ ] Site structure keeps important pages within ~3 clicks of the
      homepage; breadcrumbs present.
- [ ] Priority links placed early/in-content (reader-first; placement
      weighting itself is contested — see Conflicting Evidence).
- [ ] Footer is not utility-links-only and doesn't merely duplicate the
      top nav — see [[footer-optimization]].
- [ ] Pagination uses real `<a href>` links, each page self-canonicalized.
- [ ] Internal links are dofollow except login/admin/duplicate-filter
      URLs.
- [ ] No broken (4XX) internal links.
- [ ] Paid links marked `sponsored`; untrusted/UGC links marked
      `nofollow`/`ugc` as appropriate.

## Conflicting Evidence

- **Claim**: there is (or isn't) an ideal/target number of internal
  links per page.
  - Supported by (numeric target): [[ahrefs-internal-links-for-seo]]
    (2026-03-10) — "3-5 contextual links per article" as the "optimal"
    density, justified via a simplified PageRank-dilution argument.
  - Contradicted by: [[google-links-crawlable]] (Google Search Central,
    no date shown) — "There's no magical ideal number of links a given
    page should contain. However, if you think it's too much, then it
    probably is."
  - **Resolved (2026-07-07, user preference)**: defer to Google — no
    numeric cap. Google is the primary, ranking-authoritative source and
    deliberately avoids a numeric target, framing it as reader-judgment
    ("if you think it's too much, then it probably is") instead. Ahrefs'
    "3-5" is a third-party simplification and should not be treated as a
    rule to design content around. Link as much as genuinely serves the
    reader, including well beyond 5 links on longer/more comprehensive
    pages.

- **Claim**: Google discounts boilerplate links (footer, sidebar,
  navigation) relative to in-content editorial links.
  - Supported by: the **reasonable surfer** model — a Google patent
    **filed in 2004** that weights links by click likelihood — as
    relayed by [[ahrefs-internal-links-for-seo]] (2026-03-10) and
    [[yoast-internal-linking-for-seo]] (2025-11-12), and used as a link
    *quality* criterion in [[link-building]] via [[ahrefs-link-building]].
  - Contradicted by: **John Mueller**, quoted in
    [[growth-memo-show-me-your-footer]] (2023-07-31) — "We don't really
    differentiate there… It's not the case that we would say, Oh, like
    links in a footer have less weight or are not as useful… we
    essentially just see them as links on a page," and "whether they're
    in the header or in the footer or the sidebar or the main content,
    that doesn't really change anything for us."
  - **Current best guess (unresolved)**: lean toward Mueller for
    *internal* links, on the wiki's standing preference for official
    Google guidance over third-party SEO blogs (the same principle that
    resolved the link-count conflict above), and because the
    reasonable-surfer patent is from 2004 — Indig notes Google
    registered a **User-Sensitive PageRank** patent in 2016 that folds
    user behavior and trust into link weights, superseding the simple
    click-likelihood story. Two caveats keep this open: (1) Mueller is
    describing how Google *treats links it finds*, which is not a claim
    that a footer link produces the same practical outcome as an
    in-content one; (2) the placement hierarchy is still sound advice
    for *acquired backlinks* (see [[link-building]]), where an editorial
    in-content placement genuinely signals more than a sitewide footer
    link. The practical recommendation is unchanged — lead with
    in-content links because readers use them — but "footer links don't
    count" should not be stated as fact.

## See also

- [[webknograph-gnn-internal-linking-2026]] — the pre-deployment
  evaluation methodology and authority-vs-coherence tradeoff above.
- [[how-google-search-works]] — links are how Google discovers URLs in
  the first place (crawling stage).
- [[traditional-seo-ranking-factors]] — backlinks as a classic ranking
  signal.
- [[classic-seo-ranking-factors]] — broader classic-SEO tactic list this
  playbook complements.
- [[generative-engine-optimization]] — internal links as context signals
  for AI/generative search systems, not just classic Google Search.
- [[ahrefs-anchor-text-2020]] — the backlink anchor-text correlation
  data and Penguin history above.
- [[topic-cluster-strategy]] — the dedicated cluster-build playbook
  (discovery, pillar/subpage creation, cluster-level measurement) this
  page's "when to split" subsection feeds into.
- [[footer-optimization]] — the footer as a dedicated sitewide internal
  link surface, and the footer-density conflict.
- [[broken-link-building]] and [[digital-pr-strategy]] — external
  link-earning tactics that complement this page's internal-linking and
  link-recovery focus.
