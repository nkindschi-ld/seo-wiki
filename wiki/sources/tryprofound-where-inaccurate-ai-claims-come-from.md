---
type: source
tags: [aeo]
date_published: 2026-08-17
date_ingested: 2026-10-02
origin: raw/articles/tryprofound-where-inaccurate-ai-claims-come-from.md
---

# Where do inaccurate AI claims come from? (Profound)

**Citation:** Kopinski, Lucas. "Where do inaccurate AI claims come
from?" Profound Blog, 2026-08-17.
https://www.tryprofound.com/blog/where-do-inaccurate-ai-claims-come-from
(158,000+ claims from Profound's FactCheck product, April–August 2026,
snapshot as of 2026-08-14. Each claim is judged accurate or inaccurate
against the brand's records. Charts saved to `raw/assets/`.)

## Key takeaways

- **Inaccuracy rate by the type of source cited** (~76K claim-source
  pairs, all models):
  - Competitor sites: 4.68%
  - Earned media (third-party publications): 4.62%
  - Social / UGC: 3.45%
  - The brand's own site: 2.40%
- **Owned content is not error-free.** 54% of brands had at least one
  inaccurate claim citing their *own* site, and 51% had at least one
  citing earned media. The authors call auditing owned content "an
  immediate lever."
- **Earned-media errors are scattered and brand-specific.** The top 10
  domains account for 13% of earned-media inaccuracies and the top 100
  for 40%. A typical affected brand's errors come from about 4 sites,
  often unique to that brand. A generic outreach list won't work; each
  brand has to find its own problem domains.
- **Pricing and billing is the most error-prone topic.** It's 12% of
  evaluated claims but 24% of inaccurate ones. The next topic,
  eligibility and terms, is 4% of inaccurate claims.
  - For 66% of brands with 10+ evaluated pricing claims, pricing is
    their highest-inaccuracy topic.
  - Pricing is 35% of all earned-media inaccuracies. The top 10 domains
    behind pricing errors account for only 15% of them.
  - On pricing, error rates by source (read off the chart, approximate)
    are: earned media ~12.3%, social ~10.4%, competitor ~10.2%, brand
    site ~4.8%. The brand site's rate is lowest but still well above
    zero.
  - The authors offer two explanations: a selection effect (structured
    facts are easier to check) and how often prices, offers and
    eligibility change.
- **Inaccuracy rate by model** (~490K model-claim evaluations):
  - Microsoft Copilot: 6.8%
  - Claude: 5.7%
  - Gemini: 5.5%
  - Google AI Mode: 5.2%
  - Google AI Overviews: 5.0%
  - ChatGPT: 4.3%
  - Perplexity: 4.3%

  Claude is about 1.3x ChatGPT, despite ranking highest for
  trustworthiness in a July consumer survey.
- **Models get different things wrong.** On the same questions, ChatGPT
  and Claude overlap on 12.5% of returned claims and 11% of inaccurate
  ones. Accuracy has to be tracked and fixed engine by engine.
- **Recommendations:** monitor continuously, prioritize earned-media
  outreach to the specific pages behind your errors, and keep pricing
  and other frequently changing details current and consistent on your
  own site. Your site is an authoritative source, and stale facts on it
  "reinforce inaccurate answers elsewhere."

## Caveats

- The post promotes Profound's FactCheck product.
- The sample is FactCheck customers, not a random set of brands.
- The post doesn't say how verdicts are reached, beyond "final verdict
  of accurate or inaccurate" against brand records.
- The counts don't line up across figures: 158K claims, ~76K
  claim-source pairs, ~13K pairs in the topic chart, ~490K model-claim
  evaluations. They're probably different units and filters, but this
  isn't explained.
- Results are observational. The authors acknowledge the pricing
  selection effect themselves.
- Per-topic values were read off a bar chart and are approximate.

## Relationship to existing wiki claims

- **Gives the data behind** [[tryprofound-ai-pricing-visibility-2026]]'s
  unsupported line that AI gets pricing wrong more than any other topic.
  This is the underlying dataset, by the same vendor.
- **Distinct from, not in conflict with,**
  [[xu-measuring-google-ai-overviews-2026]]'s finding that fidelity is
  independent of source quality (r≈0.045):
  - Xu measures **grounding**: is the claim supported by the page the
    AI Overview cites? Source quality there means domain credibility.
  - Profound measures **factual accuracy**: is the claim true according
    to the brand's records? Source here means source *type*.

  A perfectly grounded summary of a stale earned-media page is accurate
  in Xu's sense and an error in Profound's. The two together suggest
  that the AI repeats errors in its sources *and* adds errors of its
  own. Not logged as a conflict.
- **Extends** the claim-fidelity section of [[ai-citation-landscape]]
  beyond Google AI Overviews to seven engines. It's the first
  cross-engine accuracy data in the wiki.
- **Adds weight to** the "each engine is a separate information
  environment" theme in [[ai-citation-landscape]]: an 11–12.5% overlap
  in claims between ChatGPT and Claude is the claim-level counterpart of
  their known source divergence.
- **Refines** step 8 (off-site pricing consensus) in
  [[ai-pricing-visibility-audit]]. That step named the domains that
  dominate pricing citations (Vendr, Reddit, G2). This source says the
  domains behind pricing *errors* are scattered and brand-specific, so
  each brand needs to find its own.

## Updated pages

- [[ai-citation-landscape]]
- [[ai-overview-grounding-and-fidelity]]
- [[ai-pricing-visibility-audit]]
- [[ai-entity-footprint-audit]]
- [[tryprofound-ai-pricing-visibility-2026]] (cross-link)
