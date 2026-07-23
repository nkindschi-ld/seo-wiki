---
type: concept
tags: [seo, aeo]
updated: 2026-07-22
---

# AI Visibility Correlation Factors

Which brand/SEO metrics *correlate* with a brand being mentioned in AI
answers (ChatGPT, AI Mode, AI Overviews) — distinct from
[[ai-citation-landscape]] (what source domains/media types get cited)
and [[generative-engine-optimization]] (content-level tactics tested for
causal effect). Based on
[[ahrefs-ai-brand-visibility-correlations]], a Spearman-correlation study
of 75,000 brands using Ahrefs Brand Radar. **Correlational, not causal**
— the source itself is explicit about this: "correlation isn't
causation... that doesn't mean improving these metrics will
automatically boost your AI visibility."

## Correlation rankings

From strongest to weakest correlation with AI-mention visibility, across
ChatGPT/AI Mode/AI Overviews:

| Factor | Correlation (approx. range) |
|---|---|
| YouTube mentions | ~0.737 (strongest of all factors) |
| Branded web mentions | 0.656–0.709 |
| Branded anchors (clickable link text featuring the brand name) | 0.511–0.628 |
| Branded search volume | 0.352–0.466 |
| Domain Rating | 0.266–0.326 |
| Number of backlinks | 0.194–0.275 |

**Nuance, not a contradiction, on YouTube specifically (2026-07-22)**:
this YouTube-*mentions* correlation is brand-level and correlational —
it measures whether a brand is discussed/mentioned on YouTube broadly,
not whether publishing your own YouTube content gets that specific
content cited. Per [[otterly-ai-keyword-research-2026]] (OtterlyAI's
2025 experiment), publishing YouTube content showed **no measurable
citation lift** at the page level. These aren't necessarily
incompatible: a brand can benefit from being talked about on YouTube
by others while a single company-published video still fails to get
directly cited by an AI engine — brand-level mention-correlation and
page-level citation-tactic-effectiveness are different questions. But
they point in different directions on "should I invest in producing
YouTube content," so don't treat the 0.737 correlation above as
evidence that *publishing* video content is itself a citation tactic.

Three weaker factors from an earlier, AI-Overviews-only version of this
same study ([[ahrefs-ai-brand-visibility-correlations]]'s May 2025
predecessor article): referring domains (0.295), URL Rating (0.18), and
site pages (0.17). That earlier version also found a **visibility
cliff**: brands in the top 25% by web mentions averaged 169 AI Overview
mentions — 10x the 50-75th percentile (14 mentions) — and that **26% of
the 75,000 brands studied had zero AI Overview mentions at all**,
consistent with this page's winner-takes-all framing below.

Notably, **content volume showed almost no correlation** with AI
visibility — publishing more content is not, by itself, associated with
higher AI-mention visibility. This is consistent with
[[ai-citation-landscape]]'s Axios finding (breakthrough tied to a
specific short-form *format*, not sheer publishing volume), and Google's
own policy explains a likely mechanism: per
[[e-e-a-t-and-page-quality]]'s Scaled Content Abuse policy, low-effort
content produced at scale (including via generative AI) is an explicit
Lowest-quality penalty target, not just a non-factor.

## Platforms weight these factors differently

- **AI Mode** correlates most strongly with traditional brand-authority
  signals — the source describes it as acting "as a sort of consensus
  engine, recommending brands that most people already know and search
  for."
- **ChatGPT** correlates weakest with classic SEO authority metrics, but
  correlates *most* with advertising metrics (ad traffic 0.286, ad cost
  0.273) — though this likely reflects heavy advertisers dominating the
  kind of content ChatGPT draws from, not a direct reward for ad spend.
  Practical implication: ChatGPT may be the most accessible AI surface
  for brands that don't yet have established authority.
- **AI Overviews** leans slightly more on Domain Rating than the other
  two.

## Conflicting Evidence — authority correlation with AI citation

- **Claim**: Domain/brand authority metrics (Domain Rating, Authority
  Score) positively correlate with AI-mention/citation visibility.
  - Supported by: this page's own Ahrefs data (Domain Rating,
    0.266–0.326 correlation with AI-mention visibility across 75,000
    brands), [[growth-memo-topics-matter-for-third-party-authority]]
    (Authority Score, 0.65 Pearson correlation, 1,000-domain sample),
    and [[firstpagesage-searchgpt-optimization-2025-guide]] (no
    disclosed methodology — claims SearchGPT/ChatGPT references top
    Google results directly, so classic Google-ranking authority feeds
    AI visibility).
  - Contradicted by: [[airops-fan-out-effect-2026]] (16,851 queries,
    353,799 pages, ChatGPT), which found domain authority and backlinks
    show **no positive correlation with citation, and are slightly
    inversely correlated** — always-cited pages averaged DA 53 vs. 56
    for never-cited pages, and high-DA platforms diverge wildly (YouTube
    DA 100 → 2.4% citation; Wikipedia DA 95 → 59.2% citation).
- **Current best guess**: plausibly not a true contradiction, but
  **different units of analysis and different citation stages**,
  parallel to the source-vs-brand-overlap resolution below — flagged as
  **unresolved** since no single source in this wiki tests both at once:
  - The Ahrefs/Growth Memo studies measure whether a **brand** gets
    mentioned at all (brand-level, aggregated across many pages/domains,
    correlational). AirOps measures whether a **specific page** gets
    cited **given it was already retrieved** for a specific query
    (page-level, causal-adjacent — it isolates retrieval rank and
    relevance as covariates). A brand could show a positive
    authority-visibility correlation in aggregate while, within any
    single retrieved candidate set, the *specific page* that wins the
    citation is chosen on relevance/rank rather than authority — these
    aren't necessarily incompatible.
  - AirOps studies only ChatGPT; Ahrefs studies ChatGPT + AI Mode + AI
    Overviews together; the Growth Memo Authority Score study doesn't
    specify which engine(s). Engine-specific mechanics could differ (per
    [[ai-citation-landscape]]'s "engines are separate information
    environments" finding) — the contradiction may partly be an
    engine-mix artifact rather than a true disagreement.
  - **Residual caveat**: Authority Score, Domain Rating, and DA are three
    different metrics from different platforms/methodologies, not the
    same measurement — some of the apparent disagreement could be
    metric-construction noise rather than a substantive finding either
    way.
  - **Additional brand-level evidence (2026-07-08)**:
    [[sej-why-calling-yourself-the-best-2026]] found that pre-existing
    brand authority (Domain Rating, backlinks, established AI-mention
    frequency) moderates whether a self-promotional listicle survives
    Google AI Overviews' citation-to-recommendation filter — high-
    authority brands are sometimes exempted from the exclusion pattern
    that consistently hits lesser-known brands. A concrete mechanism
    where brand-level authority visibly changes an AI outcome,
    consistent with the brand-level side of this conflict (and with the
    unit-of-analysis reconciliation above), though it measures
    recommendation filtering rather than citation correlation, so it
    narrows but doesn't resolve the conflict.
  - **Additional page-level corroboration (2026-07-22)**: per
    [[ahrefs-llm-optimization]] (citing a Seer Interactive study, 10,000
    finance/SaaS purchase-intent queries, GPT-4o-measured brand mentions
    vs. Google/Bing SERP rank), organic ranking correlates with LLM brand
    mentions at ~0.65 strength while **backlinks show a surprisingly
    neutral impact** — another data point on the AirOps-aligned side
    (ranking/relevance drive citation more than backlink-based authority),
    though it measures organic rank rather than Domain Rating/backlink
    count directly, so it doesn't fully resolve the brand-vs-page-level
    reconciliation above either.
  - **Practical implication until resolved**: don't treat authority-
    building (backlinks, DR/DA/Authority Score) as a reliable lever for
    winning a *specific* citation on a *specific* page — AirOps' larger,
    more controlled page-level dataset is the stronger evidence for that
    narrower claim. But don't abandon authority-building as a brand-level
    strategy either — the Ahrefs/Growth Memo brand-level correlations
    remain the best evidence for that broader claim. These are different
    decisions with different evidence bases.

## Conflicting Evidence — resolved

- **Claim**: The three major AI answer surfaces (ChatGPT, AI Mode, AI
  Overviews) operate as largely independent, non-overlapping information
  environments.
  - Supported by: [[muckrack-generative-pulse-ai-reading-may-2026]],
    which found minimal overlap in the specific *source domains* each
    provider cites (e.g., Wikipedia matters for ChatGPT/Claude but not
    Gemini; Reddit matters for Gemini but not the others). Independently
    corroborated by [[sej-the-consensus-gap]] (different engine set —
    ChatGPT/Perplexity/Google AI Overviews — 3.7M citations, ~2.35-2.45%
    universal URL overlap, stable across a full year).
  - Apparently contradicted by: [[ahrefs-ai-brand-visibility-correlations]],
    which found *high* correlation (0.75–0.82) in *which brands* get
    mentioned across AI Overviews, AI Mode, and ChatGPT.
- **Resolved (2026-07-07)**: not a true contradiction — these studies
  measure **different units of analysis**, and this is no longer just a
  plausible inference:
  - Muck Rack/SEJ measure **which specific source URLs/domains** get
    cited (citation-level granularity) — and find these differ a lot by
    provider.
  - Ahrefs measures **whether a given brand gets mentioned at all**
    (brand-level granularity, regardless of which specific page or
    domain was the source) — and finds this correlates highly across
    providers.
  - **Direct confirmation**: [[brightedge-ai-search-same-brands-different-sources]]
    tests both halves at once on the same 5-engine dataset (ChatGPT,
    Perplexity, Gemini, Google AI Mode, Google AI Overviews) and finds
    exactly this pattern — pairwise *source* overlap (16-59%) is
    measurably wider and more inconsistent than pairwise *brand*
    overlap (36-55%), across every engine pair tested. A well-known
    brand does get mentioned across systems even as each system pulls
    from a different specific page/domain to justify the mention.
  - **Residual caveat, not a contradiction**: BrightEdge's overlap
    percentages (both source and brand) read considerably higher than
    SEJ's ~2.35-2.45% figure. This is a granularity difference —
    BrightEdge compares aggregate top-100 lists across many queries per
    engine (Jaccard similarity), while SEJ measures exact-URL overlap
    for the *same individual prompt* across engines. Aggregate top-N
    list overlap structurally reads higher than per-prompt exact-URL
    overlap even when underlying fragmentation is severe — both can be
    true simultaneously.

## Authority Score correlation (separate study, caveat on comparability)

Per [[growth-memo-topics-matter-for-third-party-authority]], a separate
1,000-domain analysis found **Authority Score** to be the strongest
correlate of AI mentions measured, at 0.65 Pearson. This reads much
stronger than this page's Domain Rating figures (0.266–0.326) above, but
**the two aren't directly comparable**: Authority Score and Domain
Rating are different metrics (different platforms/methodologies) on
different-sized samples (1,000 domains vs. 75,000 brands), and Pearson
vs. Spearman correlation coefficients aren't strictly interchangeable
either. Treat this as a second data point suggesting authority-type
metrics matter, not as a direct refinement of the Domain Rating figure
above.

## From appearing to being chosen

This page's correlations measure what makes a brand *appear* in AI
answers at all. Per [[ai-shortlist-effect]] — a distinct, newer data
type — appearing is not the finish line: share of voice also correlates
with actually being *selected* once a user is comparing options inside
ChatGPT (0.57 overall, ranging from 0.97 in grocery to -0.98 in
coaching). See that page for the full purchase-decision-stage findings,
including the four framing levers (grid inclusion, "best for X" labels,
pricing accuracy, disclosed downsides) that shape selection independent
of raw visibility.

## Practical implications

See [[geo-content-optimization-tactics]] for the actionable version of
these findings (YouTube presence, earning genuine mentions, and
ChatGPT-targeting guidance for smaller/challenger brands).

## See also

- [[traditional-seo-ranking-factors]] — the classic-SERP equivalent
  correlation study, with a direct side-by-side comparison table. Most
  strikingly, backlinks/Domain Rating are meaningful for classic SERP
  ranking but among the *weakest* correlates of AI-mention visibility,
  while video/YouTube presence is the strongest AI-visibility correlate
  but wasn't part of the classic-SERP dataset at all.
- [[brightedge-ai-search-same-brands-different-sources]] — the source
  that resolves the Conflicting Evidence above by testing source-level
  and brand-level overlap on the same 5-engine dataset.
- [[ai-citation-landscape]] — citation-level (not brand-level) empirical
  patterns; also carries the resolved Conflicting Evidence writeup.
- [[growth-memo-topics-matter-for-third-party-authority]] — the Authority
  Score correlation figure discussed above, plus topic-specific source
  trust data and tiered authority-accumulation guidance.
- [[airops-fan-out-effect-2026]] — the page-level, no-authority-
  correlation finding that generated the unresolved Conflicting Evidence
  section above, plus the retrieval-rank-as-gatekeeper mechanism in
  [[ai-citation-landscape]].
- [[ai-shortlist-effect]] — the downstream visibility-to-purchase-
  selection correlation data (0.57 overall) and comparison-grid framing
  levers that extend this page's appearance-only correlations.
- [[otterly-ai-keyword-research-2026]] — source of the YouTube-content-
  no-lift nuance above.
