---
type: concept
tags: [seo, aeo]
updated: 2026-11-04
---

# Structured Data (Schema.org) and AI Search

**What it is:** Schema.org markup, usually JSON-LD, that states what a
page is (Article, Product, SoftwareApplication, FAQPage…) and its facts
(price, author, dates) in machine-readable form. In classic SEO it's an
**eligibility** mechanism for named Google rich results. The open
question for AEO is whether AI systems read it, cite pages because of
it, or quote facts from it. Until this page, the wiki's schema evidence
was scattered across a dozen pages; this is the hub.

## Current best understanding (2026-11)

1. **Google: not required for AI features, still worth doing for rich
   results, and it must match visible text.** No special markup is
   needed for AI Overviews or AI Mode, but keep using structured data
   for rich-result eligibility, and make sure it matches what's on the
   page ([[google-ai-optimization-guide]],
   [[google-succeeding-in-ai-search-2025-05]], quoted in full in
   [[coreaex-saas-pricing-schema-2026]]). "Not required" isn't
   "pointless", and "parity matters" isn't "schema helps AI visibility".
2. **No general AI-citation lift has been shown under a matched design.**
   Ahrefs' matched before/after study of 1,885 pages found no
   significant citation gain in AI Mode or ChatGPT (and an unexplained
   −4.6% in AI Overviews). Marshal found schema alone had no effect
   once Google rank was accounted for. Both are summarized secondhand in
   [[coreaex-saas-pricing-schema-2026]]. The positive numbers in the wiki
   are correlational or uncontrolled (see Conflicting Evidence). An
   earlier Ahrefs piece already said schema "isn't itself read as an
   LLM-citation signal" ([[ahrefs-llm-optimization]]), and author schema
   showed no lift in an Otterly test ([[otterly-ai-keyword-research-2026]]).
3. **Facts that exist only in markup aren't reliably extracted.** In two
   small layer tests, a price present only in JSON-LD was returned by 0
   of 5 AI systems (searchVIU) and in 0 of 9 runs (CoreAEX). When markup
   and visible text disagreed, answers used the visible value
   ([[coreaex-saas-pricing-schema-2026]]). Small samples, but they agree
   with the wiki's broader finding that most AI crawlers read the
   rendered HTML text ([[technical-seo-audit-checklist]]). **Put every
   fact you want quoted in visible text first.**
4. **Possible exception: attribute-rich Product/Review schema.** Marshal
   found Product and Review markup with concrete fields cited at 61.7%
   vs. 41.6% for generic types (p = .012), strongest on DR ≤ 60 domains.
   Single, observational, unreplicated. Treat as "don't rule out", not
   "do this for AI".
5. **Rich-result eligibility is narrower and less stable than it
   looks.**
   - FAQ rich results limited to authoritative government and health
     sites since August 2023
     ([[storylane-saas-pricing-page-design-2026]]); FAQ no longer in
     Google's structured-data gallery by 2026-06-15 (checked 2026-11-04).
     `FAQPage` is still a valid Schema.org type: a dropped Google feature
     isn't a withdrawn vocabulary.
   - The Software App rich result requires a rating or review, so a SaaS
     page without ratings isn't eligible.
   - Search Console rich-result reports show detection and validity,
     not whether the result was ever shown.
6. **What schema is still good for:** rich results where eligible; entity
   identity (`Organization` + `sameAs`, see [[brand-entity-seo-strategy]]
   and [[entity-based-seo-implementation]]); keeping a machine-readable
   copy of facts that matches the page. Classic organic ranking
   correlation is weak ([[traditional-seo-ranking-factors]]).

## "Does schema help?" is six questions

From [[coreaex-saas-pricing-schema-2026]]. Say which one a claim or tool
is answering:

| Question | What it means | How you'd check |
|---|---|---|
| Validity | Parses, uses the vocabulary correctly | Schema Markup Validator |
| Eligibility | Meets a named Google feature's documented requirements | Rich Results Test, GSC enhancement reports |
| Appearance | An enhanced result was actually shown for a query | Live SERPs, GSC Search appearance filter |
| Retrieval | An AI system accessed the page while answering | Server logs |
| Citation | The page appeared as a linked source | AI visibility tracking ([[ai-visibility-measurement-methodology]]) |
| Fact accuracy | The answer's price/unit/date matches the page today | Manual answer audits ([[ai-pricing-visibility-audit]]) |

Passing one doesn't imply the next. Most "schema works" claims measure
validity or eligibility and report it as citation.

## Implementation rules the sources agree on

- Markup must match visible content (Google; every source here).
- Generate visible facts and markup from **one source of truth** (a
  pricing model, a CMS field), so they can't drift. Stale markup is
  "confidently wrong at scale" ([[coreaex-saas-pricing-schema-2026]]).
- Don't invent values: leave `price` off an enterprise Offer with no
  public price instead of using 0
  ([[storylane-saas-pricing-page-design-2026]]); don't manufacture
  reviews to unlock a rich result.
- Validators check syntax and field presence, not truth. Test four
  things separately: parses; meets feature requirements; rendered page
  contains it; matches what readers see.
- JS-injected markup is processed by Google Search, but Google warns it
  can make Shopping crawls of fast-changing price data less reliable.
- Type modelling for SaaS: see [[saas-pricing-page-checklist]].

## Conflicting Evidence

- **Claim**: FAQ schema substantially increases AI citations.
  - Supported by: [[otterly-how-to-optimize-content-for-ai-search-2026]]
    (2026-02-16), Otterly's own experiment: +350% (2,379 vs. 529
    citations). No control group, page count or isolation of markup
    from the FAQ content itself is described.
  - Supported by: [[technotize-pricing-page-seo-b2b-saas-2026]]
    (2025-10, updated 2026-08), asserted, no data.
  - Contradicted by: Ahrefs (2026-05-11) and Marshal (2026-02-12) via
    [[coreaex-saas-pricing-schema-2026]]: no general citation effect
    from schema under matched or regression designs. FAQ rich results
    are also gone for SaaS sites (Google, 2023 and 2026).
  - **Current best guess**: the FAQ *content* (natural-language
    questions with direct answers) is the likely lever; the markup's
    separate effect is unproven. Add FAQPage only as a mirror of visible
    Q&A, and don't promise a citation lift. Unresolved: no study
    isolates FAQ markup from FAQ content.
- **Claim**: JSON-LD gives a citation advantage (+6.5 pp overall;
  MedicalWebPage, BreadcrumbList, FAQPage strongest).
  - Supported by: [[airops-fan-out-effect-2026]] (2026-04-13),
    observational across 353,799 pages.
  - Contradicted by: Ahrefs' matched difference-in-differences
    (2026-05-11, via [[coreaex-saas-pricing-schema-2026]]), which found
    the same raw pattern (cited pages ~3× likelier to have JSON-LD) but
    no lift when pages *added* schema; its authors attribute the
    correlation to site quality.
  - **Current best guess**: the +6.5 pp is a correlation explained by
    better-built sites, not a schema effect. The matched design is the
    stronger evidence, though it covered only already-heavily-cited
    pages, so a page with no AI visibility is untested. Unresolved.
- **Claim**: AI engines extract Offer/price data directly from schema.
  - Supported by: [[technotize-pricing-page-seo-b2b-saas-2026]],
    asserted; implied by "schema is the meaning layer for AI"
    ([[siteimprove-open-graph-ai-search-visibility-2026]], asserted) and
    the Product-schema advice in [[optimizing-for-the-agentic-web]].
  - Contradicted by: searchVIU (one page, 5 systems, 2025-10-30) and
    CoreAEX (4 pages, 3 systems, 9 runs, 2026-08-30), both via
    [[coreaex-saas-pricing-schema-2026]]: JSON-LD-only prices weren't
    returned, and visible text won every conflict.
  - **Current best guess**: don't rely on markup to carry any fact that
    isn't also visible. The layer tests are tiny and say nothing about
    what systems take from indexes or training data, and shopping
    feeds (OpenAI's structured pricing input) are a separate channel.
    Leaning "visible text wins", flagged unresolved until larger tests
    exist.

## Related

- [[saas-pricing-page-checklist]] — schema model for a SaaS pricing page.
- [[ai-pricing-visibility-audit]] — when AI answers get your pricing wrong.
- [[open-graph-protocol]] — OG vs. meta description vs. schema.
- [[entity-oriented-search-fundamentals]] — why entity markup exists.
- [[geo-content-optimization-tactics]] — where the AirOps and Otterly
  numbers are used.

## Sources

[[coreaex-saas-pricing-schema-2026]] (hub: Google quotes, Ahrefs,
Marshal, Volpini et al., searchVIU, CoreAEX layer test),
[[storylane-saas-pricing-page-design-2026]],
[[technotize-pricing-page-seo-b2b-saas-2026]],
[[airops-fan-out-effect-2026]],
[[otterly-how-to-optimize-content-for-ai-search-2026]],
[[otterly-ai-keyword-research-2026]], [[ahrefs-llm-optimization]],
[[google-ai-optimization-guide]],
[[google-succeeding-in-ai-search-2025-05]],
[[siteimprove-open-graph-ai-search-visibility-2026]].
