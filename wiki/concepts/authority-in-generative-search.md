---
type: concept
tags: [aeo, seo]
updated: 2026-10-05
---

# Authority in Generative Search

How source authority shapes which content AI search engines consider and
cite. The working model is that authority acts **as a filter, not a score**.
It works early in the pipeline and decides whether a source is suitable for a
query at all. How strictly it's applied depends on how much harm a wrong
answer could do.

The framing comes from [[lumar-authority-filter-not-score]], a vendor
framework with no published data. It rests here because several independent
lines of evidence already in the wiki point the same way (see
"Corroborating evidence" below). This page deals with *source suitability
for a query*. It is related to, but separate from:

- [[e-e-a-t-and-page-quality]] — Google's rater framework, which defines
  E-E-A-T and YMYL.
- [[topical-authority-in-ai-search]] — which brands *own* a topic in AI
  answers.
- [[ai-visibility-correlation-factors]] — which brand metrics correlate with
  being *mentioned*.

## Filter, not score

In classic SEO, authority is a comparative quantity (Domain Rating, link
equity) that moves a page up or down. In the generative model:

- authority is applied **early**, before passages are compared, at the
  candidate-selection stage ([[ai-search-reranking-pipeline]]);
- it can **exclude** a source outright, so a better explanation on an
  unsuitable domain never gets compared at all;
- that would explain why some highly relevant pages never surface while
  certain domains appear over and over for certain query types.

## Enforcement scales with the stakes of the query

Lumar's query-class model ("observed behavior," with no method published):

| Query type | Authority role | Behavior |
|---|---|---|
| Medical / legal / mechanical (YMYL) | Hard gate | Non-authoritative pages often excluded |
| Technical specs (manufacturer topics) | Hard preference | Official sources dominate |
| General educational | Strong filter | Boosts but doesn't exclude |
| Exploratory / lifestyle | Soft filter | Relevance dominates |
| Opinion / creative | Minimal | Authority often irrelevant |

The scaling principle matches Google's official position. Google's systems
give more weight to strong E-E-A-T on topics that could significantly affect
health, financial stability, safety or the welfare of society. YMYL is a
spectrum, not a yes/no flag ([[e-e-a-t-and-page-quality]]), which fits a
graded filter better than a binary one.

## Which signals count as authority

Lumar's self-rated confidence, with what the wiki's evidence adds:

| Signal | Lumar confidence | Wiki evidence |
|---|---|---|
| **Source provenance** (official docs, regulators, institutional publishers, manufacturer sources) | Very high | Corroborated: ChatGPT `site:`-targets `.gov` for YMYL and brand domains for specs ([[lilyray-chatgpt-fanout-queries-2026]]) |
| Consistency with trusted sources; citation overlap | Medium | No direct test in the wiki yet |
| Topic ownership; historical trust | Medium | Partly measured: leadership is sticky once earned ([[topical-authority-in-ai-search]]) |
| Author credentials | Lower / medium | Mixed: author **schema** showed no citation lift ([[otterly-ai-keyword-research-2026]]), but named-individual authorship dominates LinkedIn citations, ~92% vs. ~8% ([[otterly-linkedin-ai-citations-study-2026]]) |
| `author` / `reviewedBy` structured data | Lower | Consistent with the author-schema null result above |
| Engagement metrics | Lower | Corroborated: likes and comments correlate near zero with citation ([[otterly-linkedin-ai-citations-study-2026]]) |
| Link volume / brand popularity | "Tells us much less" | Mixed. Backlinks and Domain Rating correlate weakly with AI visibility ([[ai-visibility-correlation-factors]]). But branded web mentions correlate strongly with being *mentioned*, a different outcome from being an *eligible cited source* |

Exact weighting is unknown, and Lumar rates its own confidence in it as low.

## Corroborating evidence already in the wiki

- **`site:` gating by query type:** ChatGPT's `site:` use in fan-outs rose
  from 0.3% to 23%. Legal and health queries targeted `.gov` domains
  exclusively in some tests, and product spec and pricing queries targeted
  brand domains ([[lilyray-chatgpt-fanout-queries-2026]], filed on
  [[ai-citation-landscape]]). This is the clearest visible mechanism for a
  hard gate.
- **YMYL retrieval paths:** legal and medical are the only verticals with
  paired text + PDF engines in ChatGPT's registry, which reflects how much
  authoritative YMYL material comes as PDFs
  ([[chatgpt-vertical-retrieval-engines]]).
- **Google AI Overview claim fidelity is highest in YMYL categories** (Health
  94.8%), consistent with stricter guardrails where stakes are high
  ([[ai-citation-landscape]]). One caveat for Lumar's table: Autos is among
  the *lowest*-fidelity categories (80.7%), even though Lumar puts
  "mechanical" queries in the hard-gate row.
- **Authority is relative to the topic**: competitor share of citations
  swings from 33.5% to 7% between topics in the same category
  ([[growth-memo-topics-matter-for-third-party-authority]]). That fits a
  per-query filter better than a fixed domain score.

## Smaller sites and authority gaps

The filter isn't absolute. Where authoritative sources don't cover a query
well, typically niche, operational or long-tail queries, other sources can
compete. In those cases semantic precision and [[chunkability]] decide the
outcome. This matches the reranker finding that **weaker-authority pages can
hold the clearest extractable answer and win the citation**
([[ai-search-reranking-pipeline]]). Lumar's caveat is that this only works if
the gap really exists. On well-covered YMYL head terms, relevance and
structure may not be enough.

Strategic reading: **authority sets the ceiling on where you can compete;
relevance and chunkability decide what happens once you're there.** For a
less established site:

- map which target queries are YMYL or spec-like (hard gate or hard
  preference) and which are educational, exploratory or opinion (softer
  filter);
- deprioritize head terms already well served by official or institutional
  sources;
- target gaps where existing authoritative sources don't fully answer the
  query.

The "choose where to compete" step in check 5 of [[geo-diagnostic-checklist]]
makes this operational.

For a first-party vendor (e.g. a SaaS company's own docs), the same model is
an advantage. On "how does *our product* do X" or spec queries, the official
docs are the provenance signal, which is one reason docs pages tend to
out-cite marketing pages (see the reference-beats-transactional pattern in
[[ai-citation-landscape]]).

## Conflicting Evidence

- **Claim:** for technical-spec and first-party factual queries, official
  sources "dominate" (a hard preference).
  - Supported by: [[lumar-authority-filter-not-score]] (2026-09-02, no
    data); ChatGPT `site:`-targeting of brand domains for specs and pricing
    ([[lilyray-chatgpt-fanout-queries-2026]], 2026-08, directional).
  - Partly contradicted by: [[tryprofound-ai-pricing-visibility-2026]]
    (2026-09-03, ~7,600 responses, Cloud 100, 6 engines). Owned pricing
    pages appear in 46% of pricing answers but are the **first** citation in
    only 12%. Vendr, Reddit and G2 dominate. ChatGPT is the exception at 38%
    owned-first, which fits its `site:` behavior.
- **Current best guess:** unresolved, leaning query-class nuance. Pricing
  isn't a pure spec query, because it invites user-reported "real cost"
  sources, so it may sit nearer the "general educational" row than the
  "technical specs" row. Being *present* is also a weaker test than being
  *dominant*. Even so, the only measured data on a first-party factual query
  class shows official sources failing to dominate on most engines, so treat
  Lumar's "hard preference" row as engine-dependent (strongest on ChatGPT)
  until there's measured data on true spec queries.

## See also

- [[e-e-a-t-and-page-quality]] — the official E-E-A-T and YMYL definitions
  this model borrows; E-E-A-T as a way of thinking, not a formula.
- [[ai-search-reranking-pipeline]] — where the filter sits (candidate
  selection, before passage reranking).
- [[chunkability]] — the passage-level lever that matters most once a source
  gets past the filter, and for authority-gap queries.
- [[geo-diagnostic-checklist]] — check 5, authority constraints.
- [[topical-authority-in-ai-search]] — topic ownership, one of the
  medium-confidence signals here, measured.
- [[ai-visibility-correlation-factors]] — brand-metric correlations with AI
  *mentions*; read alongside the link-volume row above.
- [[generative-engine-optimization]] — the umbrella concept and its "authority
  as a retrieval-eligibility gate" framing.
