---
type: playbook
tags: [seo, aeo]
updated: 2026-09-10
---

Why / when to use this: apply when planning a new content area from
scratch, or when [[link-and-anchor-text-best-practices]]'s
GSC-keyword-degradation diagnostic flags an existing long-form page as
a split candidate. Topic clusters are the structural implementation of
"topical authority" — this playbook is the dedicated how-to; the
internal-linking mechanics of clusters (pillar↔subpage linking,
siloing) live in [[link-and-anchor-text-best-practices]], and this page
cross-links rather than duplicates that content.

## What a topic cluster is

Three components, consistent across all three sources:
- **Pillar page** — a comprehensive, broad-overview page covering
  short-tail keywords for the whole topic (typically 2,500+ words per
  [[surferseo-topic-clusters]]).
- **Cluster / subpages** — detailed pages on individual subtopics,
  targeting long-tail keywords, each with a distinct non-overlapping
  keyword set to avoid cannibalization.
- **Internal links** connecting them, reciprocally.

Per [[sitebulb-topic-clusters]], a fourth tier is worth tracking
separately: **target pages** — decision-stage, conversion-focused pages
(product/service pages) that sit downstream of the cluster, mapped to
the buyer journey's awareness → consideration → decision stages rather
than to the pillar/subpage informational structure.

**Keyword vs. topic** ([[surferseo-topic-clusters]]): keywords are
specific terms placed strategically (titles, URLs, headers, meta, body);
topics are the broader subject that should drive the overall content
plan. Build the cluster around the topic, then fit keywords to pages —
not the reverse.

## Why it works

Reflects Google's post-Hummingbird shift from keyword-matching to
intent/concept understanding — clusters demonstrate topical authority
and support E-E-A-T ([[e-e-a-t-and-page-quality]]) by covering a subject
comprehensively rather than in isolated, disconnected posts. Also
expands AI-prompt coverage: multiple interlinked, comprehensive pages
give generative engines more surface area to draw citations from per
[[generative-engine-optimization]].

## Build process

1. **Choose a core topic.** Brainstorm on brand relevance, past content
   performance, audience interest, and competitor coverage. Pick a
   topic broad enough for multiple subpages but focused enough to stay
   coherent. New/smaller sites: go deep on **one** cluster before
   starting a second — per [[surferseo-topic-clusters]]'s Dino Digital
   case study, concentrated depth-first investment produced a 17x
   organic traffic increase, vs. spreading effort thin across many
   shallow clusters.
2. **Discover subtopics — combine multiple sources, don't rely on one:**
   - Pivot from *existing* keyword research: group already-researched
     keywords by theme; group names become candidate pillar topics
     ([[sitebulb-topic-clusters]]).
   - Mine Google Search Console for existing site content, using
     automated clustering tools (e.g. Surfer's Domain Map) to find
     coverage gaps ([[surferseo-topic-clusters]]).
   - Google's own Related Searches and Autocomplete, plus keyword
     browser extensions ([[surferseo-topic-clusters]]).
   - Real user questions from support teams, sales calls, and surveys —
     not just keyword tools — to keep the cluster genuinely useful
     rather than link-stuffed ([[sitebulb-topic-clusters]]).
3. **Cluster by shared search intent.** Use AI-assisted keyword-strategy
   tools to identify pillar/subpage candidates automatically; prioritize
   by intent alignment, volume, and difficulty balance
   ([[semrush-topic-clusters]]).
4. **Build the pillar page first, designed with subpages in mind.**
   Comprehensive overview (2,500+ words per Surfer), clear H2/H3
   hierarchy, table of contents, natural keyword placement in title/
   meta/H1/opening paragraph, contextual internal links with descriptive
   anchors (see [[link-and-anchor-text-best-practices]] for anchor-text
   rules).
5. **Build subpages with non-overlapping keyword sets.** Each subpage
   should own a distinct long-tail keyword group; check that no two
   subpages target the same intent (keyword cannibalization — see
   [[keyword-mapping-and-cannibalization]]).
6. **Link the cluster together.** All subpages link up to the pillar;
   subpages also link to each other sequentially (A↔B, B↔C) to spread
   link-juice flow, not just hub-and-spoke ([[surferseo-topic-clusters]]).
   Use folder-based URLs (`example.com/topic/cluster/`) for structural
   clarity ([[sitebulb-topic-clusters]]).
7. **Publish, then iterate.** Identify remaining content gaps; avoid
   repetition across subpages; return to research as new subtopics
   emerge.
8. **Measure at the cluster level, not just per-page.** Track Google
   rankings *and* AI/LLM appearance (e.g. ChatGPT) for the cluster's
   keyword group as one unit, tagged together; expand high performers,
   revise underperformers ([[semrush-topic-clusters]]).
9. **Audit internal links on a cadence.** Clusters decay — dead or
   irrelevant cross-links accumulate as content changes. Use
   crawl-visualization tooling periodically to catch this
   ([[sitebulb-topic-clusters]]).

## When to retrofit an existing long-form page into a cluster

See [[link-and-anchor-text-best-practices]]'s GSC-keyword-degradation
diagnostic and the Schmitt case study (1000% pageview growth from
splitting one tutorial into a 5-page cluster) — that content lives there
rather than being duplicated here, since it's fundamentally an
internal-linking/site-structure decision.

## Worked examples

- Healthline: "Everything You Need to Know About Allergies" pillar +
  symptom/cause/treatment subpages.
- Petcube: "Puppy Care 101" pillar + training/adoption/supplies
  subpages.
- Wistia: video-marketing-guide pillar + funnel-stage/example/promotion
  subpages, video-enhanced.
- Shopify: "Ultimate Guide to Dropshipping" pillar + private-labeling/
  print-on-demand/niche-selection subpages.
- Help Scout: "Acquiring customers using email" pillar.
- HubSpot: PR-campaign cluster article.
- Dino Digital (HR SaaS): 17x organic traffic via one deep cluster
  before expanding.

## Checklist

- [ ] One core topic chosen, scoped for coherent (not sprawling)
      coverage.
- [ ] Subtopics sourced from at least two of: existing keyword research,
      GSC/site-content clustering, Google Related Searches/Autocomplete,
      real user questions (support/sales/surveys).
- [ ] Pillar page comprehensive (2,500+ words guideline), with TOC and
      clear heading hierarchy.
- [ ] Each subpage has a distinct, non-overlapping keyword set (no
      cannibalization — cross-check against
      [[keyword-mapping-and-cannibalization]]).
- [ ] Reciprocal pillar↔subpage links, plus sequential subpage↔subpage
      links.
- [ ] Folder-based URL structure.
- [ ] Cluster-level tracking set up for both Google rank and AI/LLM
      appearance.
- [ ] Internal-link audit scheduled on a recurring cadence.

## See also

- [[link-and-anchor-text-best-practices]] — internal-linking mechanics,
  siloing, cornerstone content, and the GSC-based "when to split into a
  cluster" diagnostic with the Schmitt case study.
- [[keyword-mapping-and-cannibalization]] — the cannibalization
  diagnostic referenced in step 5.
- [[generative-engine-optimization]] and [[geo-content-optimization-tactics]]
  — why comprehensive, interlinked coverage also expands AI-citation
  surface area.
- [[e-e-a-t-and-page-quality]] — the Google quality framework clusters
  are built to satisfy.
- [[content-marketing-strategy]] — broader content-planning context
  clusters fit into.

See [[semrush-topic-clusters]], [[surferseo-topic-clusters]], and
[[sitebulb-topic-clusters]] for the full source writeups.

Before rolling out a large batch of pillar↔subpage links, see
[[webknograph-gnn-internal-linking-2026]] (in
[[link-and-anchor-text-best-practices]]) for a pre-deployment
evaluation method that scores proposed link batches on authority gain
and semantic-coherence cost before publishing them.
