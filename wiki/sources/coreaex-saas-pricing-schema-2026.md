---
type: source
tags: [seo, aeo]
date_published: 2026-08-29
date_ingested: 2026-11-04
origin: raw/articles/coreaex-saas-pricing-schema-2026.md
---

# Schema for SaaS Pricing Pages: What It Establishes and What It Doesn't (CoreAEX, 2026-08-29)

**Citation:** Zivkovic, Zarko. "Schema for SaaS Pricing Pages: What It
Establishes and What It Doesn't." CoreAEX Resources (Technical SEO),
published 2026-08-29, last reviewed 2026-08-30.
https://coreaex.com/resources/saas-pricing-schema.html

**Rigor: high for a consultancy page.** CoreAEX is a one-person B2B SaaS
technical SEO / AEO consultancy and the page ends in a "Book a Session"
pitch. But it labels each claim either **Documented** (quoted from
Google or Schema.org docs, with last-updated dates) or
**Recommendation** (CoreAEX's own choice), never pools numbers across
studies, gives every study's sample, vendor status and limits, and has
a "What this cluster does not claim" section. It's the hub of a
six-page cluster. The sub-guides and CoreAEX's own layer-test page
were **not** captured; the 0-of-9 result below is as summarized on the
hub.

## Key takeaways

- **Google's position, quoted.** Google's AI optimization guide
  (updated 2026-07-10), in a bullet titled "Overfocusing on structured
  data", says structured data isn't required for generative AI search
  and there's no special schema.org markup to add, but to keep using it
  for rich-result eligibility. The AI features page (2025-12-10) says
  the same and lists "structured data matches the visible text" as a
  fundamental that still matters. CoreAEX's point: those two statements
  must be quoted together. "Not required" isn't "pointless", and
  "parity matters" isn't "schema helps AI visibility". Consistent with
  [[google-ai-optimization-guide]] and [[google-succeeding-in-ai-search-2025-05]].
- **"Does schema help?" is six questions** with different evidence:
  1. validity (does it parse and use the vocabulary correctly);
  2. Google eligibility (meets a named feature's documented requirements);
  3. rich-result appearance (actually shown for a query);
  4. retrieval (a system accessed the page);
  5. citation (linked as a source);
  6. price accuracy (amount, currency, unit, period, commitment match the
     page today).
  Passing one says nothing about the next. A correct citation of a page
  quoting a price you stopped charging is failure mode 6, and no
  standard report shows it.
- **The evidence on schema and AI citation, as CoreAEX reads it**
  (secondhand here; none of these studies is ingested yet):
  - **Ahrefs** (Linehan & Guan, 2026-05-11): 1,885 pages that added
    JSON-LD (Aug 2025–Mar 2026) vs. ~4,000 matched controls, 30 days
    before/after. AI Overviews citations −4.6% (significant, unexplained,
    not to be read as schema harming), AI Mode +2.4% and ChatGPT +2.2%
    (both indistinguishable from zero). Sample was already heavily cited
    pages (100+ AIO citations/month). Cited pages were ~3× likelier to
    carry JSON-LD, which the authors read as a site-quality confound.
  - **Marshal** (Fischman, 2026-02-12; working paper, not peer
    reviewed): 730 citations, 75 commercial queries, 1,006 pages,
    ChatGPT and Gemini. Schema alone: no effect (OR 0.678, p = .296).
    Google rank dominated (OR 0.762 per position, p < .001; rank 1
    cited in 43% of the queries it appeared for vs. 5% at rank 7).
    **Exception:** attribute-rich Product/Review schema with concrete
    fields 61.7% vs. 41.6% for generic types (p = .012), strongest at
    DR ≤ 60. Single-source, observational.
  - **Volpini et al.** (arXiv 2603.10700, 2026-03-11; preprint, authors
    sell schema): JSON-LD alone gave "only modest improvements" in a
    constructed RAG corpus; the +29.6%/+29.8% gains came from an
    "enhanced entity page" that changed several things at once.
  - **searchVIU** (tested 2025-10-30, published 2025-12-02): one page,
    eight product variants, each price in a different layer. A €8.99
    price that existed **only in JSON-LD** was returned by none of
    ChatGPT, Claude, Gemini, Perplexity and Google AI Mode.
  - Three of the four are from vendors; the fourth is a one-page test.
    They measure different outcomes and shouldn't be pooled.
- **CoreAEX's own controlled test (summarized on the hub):** 3 AI
  systems × 4 fictional pricing pages on 2026-08-30. A price present
  only in JSON-LD was reproduced in **0 of 9 runs**. Where visible text
  and JSON-LD disagreed, every returned price matched the **visible**
  one. An observational cohort study of real SaaS pricing pages hasn't
  run yet.
- **Working conclusion:** where a commercial fact exists only in
  markup, current evidence doesn't show it will be extracted reliably.
  Lead with visible, crawlable, current pricing; schema is a consistency
  layer on top.
- **Choosing the type (Documented):**
  - `SoftwareApplication` descends from `CreativeWork`, not `Product`;
    `Service` sits under `Intangible`. Schema.org's `Product` definition
    text nonetheless covers services. The hierarchy and the definition
    disagree, so say which you chose and why.
  - `AggregateOffer` is vocabulary-valid for a tiered table, but separate
    `Offer` nodes keep each plan's name, URL, price and terms.
  - The **Software App rich result requires a rating or review**. A SaaS
    pricing page without ratings isn't eligible; accept it rather than
    manufacture reviews.
  - FAQ is **no longer listed in Google's structured-data search gallery**
    (as of its 2026-06-15 update; checked during this ingest, the gallery
    page updated 2026-10-16 links no FAQ page). Product and Software app
    still are. `FAQPage` remains a core Schema.org type: a dropped Google
    feature isn't a withdrawn vocabulary term.
- **Modelling commercial terms:**
  - `billingDuration`, `billingStart` and the `priceType` enumeration are
    marked "new" in Schema.org v30.0. No Google doc says Google consumes
    `billingDuration`, `billingIncrement`, `billingStart` or
    `CompoundPriceSpecification`: **unknown, not irrelevant**.
  - `billingDuration` is **how long a price is billed for, not how often
    payment recurs**. Payment frequency has no clear property; put it in
    visible copy (Recommendation).
- **Keeping it true:** generate visible pricing and structured data from
  one pricing model so a price change can't update one and not the other
  (Recommendation). Google says JS-generated Product markup "can make
  Shopping crawls less frequent and less reliable" for fast-changing
  price data; that caveat is scoped to Shopping crawls, not AI crawlers.
- **Four tests, four different proofs:** parses/vocabulary; meets a
  named feature's requirements; the rendered page contains what you
  think; markup matches what a reader sees. Validators check syntax and
  field presence, not truth.
- **When AI gets your price wrong, don't start by fixing schema.** Find
  the first layer where the current fact stops being available: absent
  from the page, present but inaccessible, contradicted elsewhere on the
  site, stale in a cache or index, ambiguous between plans or currencies,
  or transformed in the answer.
- **Measurement traps (Documented):** Search Console rich-result reports
  show detection and validity, not appearance. The Generative AI
  performance report (partial rollout) shows AIO + AI Mode **impressions
  only**: no clicks, CTR, position or queries; AI clicks fold into "Web".
- **No credible figure exists for how often AI answers misstate SaaS
  prices**, per CoreAEX's search. (The wiki does have one vendor figure:
  pricing is 24% of inaccurate claims in
  [[tryprofound-where-inaccurate-ai-claims-come-from]], a FactCheck
  customer dataset rather than a SaaS-pricing error rate.)
- **Non-Google systems:** no first-party statement on schema.org
  consumption located in OpenAI, Perplexity or Anthropic crawler docs.
  OpenAI's structured pricing input is provider feeds, not on-page
  markup. The "Microsoft confirmed schema helps its LLMs" line traces to
  a relayed conference remark: unverified.

## What this updated in the wiki

- New [[structured-data-and-ai-search]] concept (hub source), including
  three Conflicting Evidence entries.
- New [[saas-pricing-page-checklist]] playbook (schema model, parity,
  visible-price rule).
- [[ai-pricing-visibility-audit]]: new schema step and the layered
  wrong-price diagnosis.
- [[geo-content-optimization-tactics]], [[writer-checklist-blog-posts]],
  [[open-graph-protocol]]: schema/FAQ-schema claims qualified.

## Follow-ups

Primary sources worth ingesting directly: the Ahrefs schema study, the
searchVIU layer test, and CoreAEX's "which layer does an AI answer read
a price from" results page.
