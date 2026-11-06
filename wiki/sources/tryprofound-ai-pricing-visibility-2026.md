---
type: source
tags: [aeo, seo]
date_published: 2026-09-03
date_ingested: 2026-10-02
origin: raw/articles/tryprofound-ai-pricing-visibility-2026.md
---

# What AI agents really think about your pricing (Profound / Growth Unhinged)

**Citation:** Poyar, Kyle; Laskaris, Nikolas. "What AI agents really
think about your pricing." Profound Blog (cross-post with Growth
Unhinged), 2026-09-03.
https://www.tryprofound.com/blog/what-ai-agents-really-think-about-your-pricing
(~7,600 AI responses (7,675 in the citation count) to the prompt
"Evaluate [Company] on pricing," run for each of the Forbes Cloud 100
across 6 engines: ChatGPT, Google AI Mode, Google AI Overviews, Gemini,
Microsoft Copilot, Perplexity. Data collected 2026-07-29 to 2026-08-10.)

## Key takeaways

- **AI pricing answers skew negative and are poorly sourced.** For one
  unnamed software company, 72 of 76 responses used negative pricing
  language. A vertical-AI unicorn with no public pricing page drew 67 of
  76 negative responses, built largely from Reddit, including a quoted
  price range with a 24x spread for the same product. Profound says its
  wider dataset shows pricing and billing is the topic AI gets wrong
  most often. That claim is asserted here, not shown. The underlying
  data is in [[tryprofound-where-inaccurate-ai-claims-come-from]]
  (pricing is 12% of claims but 24% of inaccuracies).
- **Pricing demand is small as a share but large in volume.** Prompts
  with cost or pricing keywords are 1–2% of all LLM queries in
  Profound's data. The share of ChatGPT queries with commercial intent
  rose from 13.9% to 19.2% over the past year.
- **Owned pricing pages are cited but rarely first.** 77% of the Cloud
  100 have a public pricing page. That page appeared somewhere in 46% of
  responses (3,532 of 7,675) but was the *first* citation in only 12%.
  No company had its pricing page cited first in a majority of runs.
- **Engines differ.** ChatGPT cites the owned pricing page first 38% of
  the time. Google AI Mode, AI Overviews and Gemini "usually bury" it.
- **Readability by bots comes first, and transparency alone isn't
  enough.** Only 57 of 77 public pricing pages were fully readable by
  bots, and 10 hid at least 40% of body content. The four causes:
  client-side rendering, interactive elements (tabs, accordions, price
  sliders), robots.txt or other blocks, and iframes from an uncrawlable
  domain. Pages with plans but no prices (Personio, Pendo, Carta, Gong)
  can still be cited above the median, while fully transparent pricing
  doesn't guarantee first citation.
- **One self-reported before/after.** Profound's own pricing was
  rendered client-side, so AI crawlers never saw the prices. They moved
  it to server-side rendering (deployed June 25, 2026). Citation-bot
  traffic rose 13% week over week and kept climbing, and the pricing
  page became Profound's #2 most-cited page. This is n=1, and the
  vendor is reporting on itself.
- **Three outside domains dominate pricing answers:** Vendr (18.7% of
  runs), Reddit (18.6%) and G2 (15.9%). If you hide pricing, it gets
  discussed elsewhere anyway.
- **A "pricing answer stack" beats a single pricing page.** The best
  performers were Plaid (pricing page cited first 42% of the time),
  Fireworks AI, Fal AI and ElevenLabs. The weakest were
  enterprise-focused companies with hidden pricing and thin docs. The
  stack has five parts: a pricing page, FAQs that match natural-language
  pricing questions, supporting content (value, operations, edge
  cases), technical billing docs, and AI-readable infrastructure for
  all of it.
  - **Plaid:** billing docs were cited in 70% of answers, the pricing
    page in 64% and FAQs in 50%. The docs are the most important
    pricing source because they are denser: they define billing models
    per product and endpoint, cover costly edge cases, and say outright
    which information isn't public.
  - **Fireworks AI:** shows scheduled price changes ("up to Aug 31" and
    "from Sep 1") as a freshness signal, and gives dense, tabular facts
    with explicit units. Its docs expose an llms.txt index and a "Copy
    page" control.
- **10-step audit checklist** (turned into
  [[ai-pricing-visibility-audit]]): baseline prompt, three sources of
  truth, crawlability, a concrete entry point, billing mechanics,
  extractable formatting, evaluation-oriented language, off-site
  consensus, freshness signals, and AI-readable versions. The authors
  say the last step "probably" helps but they "can't prove causal
  impact." The post also links a downloadable "AI pricing visibility
  audit" Claude skill, which was not fetched.

## Caveats

- Profound sells AI-visibility tooling and is a Growth Unhinged partner.
- The before/after result is one company reporting on itself, with no
  control.
- The data window is two weeks, and the authors note that citation
  behavior changes often.
- The sample is the Cloud 100: large, well-known private cloud
  companies, which may not hold for smaller brands.
- Only one prompt template was used ("Evaluate X on pricing").
  Comparative or plan-specific pricing prompts weren't tested.

## Relationship to existing wiki claims

- **Agrees with** the content-type finding in [[ai-citation-landscape]]
  that pricing pages are cited less than average (Otterly: −21%). This
  source adds the *position* dimension: present in 46%, first in 12%.
  Plaid's docs out-citing its pricing page fits the pattern that guides
  and reference content beat transactional pages.
- **Agrees with** [[lilyray-chatgpt-fanout-queries-2026]]'s
  observation that ChatGPT fan-outs use `site:` on brand-official
  domains for spec and pricing queries. ChatGPT is the engine here that
  most often cites the owned pricing page first (38%).
- **Agrees with, and makes concrete,** the "accurate, current pricing"
  framing lever in [[ai-shortlist-effect]], and the "keep pricing in
  crawlable HTML" tactic in [[geo-content-optimization-tactics]].
- **Adds a supporting citation to the "third-party matters" side** of
  the unresolved review-platform conflict in [[ai-citation-landscape]]
  (G2 in 15.9% of runs vs. DerivateX's zero G2 citations). It doesn't
  resolve the conflict, because this sample is pricing prompts only.
- **Nuances**, without contradicting, the "Reddit is retrieved
  constantly but rarely attributed" finding: on pricing prompts Reddit
  is a direct citation in 18.6% of runs. This is likely query-type
  dependence (pricing pulls in user-reported real-world costs). It's
  noted, not logged as a conflict.
- **Agrees with** the JavaScript-rendering guidance in
  [[technical-seo-audit-checklist]] and adds a measured failure rate on
  one page type (13% of public Cloud 100 pricing pages hid 40% or more
  of their content).

## Updated pages

- [[ai-pricing-visibility-audit]] (new playbook)
- [[ai-citation-landscape]]
- [[ai-shortlist-effect]]
- [[geo-content-optimization-tactics]]
- [[technical-seo-audit-checklist]]
