---
type: concept
tags: [seo, aeo]
updated: 2026-07-22
---

# AI Citation Landscape

Empirical patterns in what generative AI answer engines actually cite in
practice, as distinct from [[generative-engine-optimization]] (which
covers *tactics* for increasing citation-stage visibility). Based on
[[muckrack-generative-pulse-ai-reading-may-2026]], an analysis of 25M+
citation links across ChatGPT, Claude, and Gemini; [[sej-the-consensus-gap]]
(3.7M URL citations, ChatGPT/Perplexity/Google AI Overviews); and
[[brightedge-ai-search-same-brands-different-sources]] (ChatGPT,
Perplexity, Gemini, Google AI Mode, Google AI Overviews).

## Non-paid, earned media dominates

~99% of citations come from non-paid sources; paid/advertorial content is
just 0.3% of all citations. Journalism accounts for 27% of citations
overall; earned media broadly (journalism, academic/research, government/
NGO, encyclopedic, social, third-party corporate content) accounts for
~84%, with owned + paid content making up the remaining ~16%.

## Providers are three separate information environments

ChatGPT, Claude, and Gemini cite very differently, both in *how often*
and *how much*, and pull from largely non-overlapping sources:

- **ChatGPT**: cites in 96% of responses, ~5 citations each — a
  near-universal but concise citer.
- **Gemini**: cites in 82% of responses, ~8 citations each.
- **Claude**: cites in only 55% of responses (leans on training
  knowledge more), but averages **13** citations when it does go to the
  web — more than twice ChatGPT's depth.

Cross-provider overlap in top cited domains is minimal — Wikipedia is
the only domain that appears near the top for all three. Among
journalism outlets specifically, only Forbes appears in more than one
provider's top 5. Practical implication: optimizing for "generative
engines" as a monolith is misleading — tactics may need to be
provider-specific.

This is independently corroborated at much larger scale by
[[sej-the-consensus-gap]] (3.7M URL citations, ChatGPT/Perplexity/
Google AI Overviews): only **2.35-2.45%** of cited URLs for the same
prompt appear in all three engines, and **91%** appear in only one —
stable across four samples spanning a full year (Q3 2025–Q1 2026). Even
Wikipedia (16,073 citations) is universal in only 1.3% of cases; Reddit
(14,267 citations) in 0.1%; Reuters (1,202 citations) in 0.0%. That
source calls this **"the consensus gap"**: engines draw from largely
disjoint source pools rather than ranking a shared pool differently.

## Measure presence, portability, and concentration separately

Per [[sej-the-consensus-gap]], a single blended "AI visibility" score
hides the finding that matters — that engines barely share source
pools. Three separate metrics are more useful:

- **Presence** — % of tracked prompts where you appear in *any* engine
  (does visibility exist at all).
- **Portability** — % of your cited URLs that appear in *all* engines
  (does visibility survive across platforms, or is it one engine's
  idiosyncratic pick).
- **Concentration** — % of your citations coming from a single engine
  (which platform your visibility dashboard actually depends on).

Content type affects portability more than expected but stays low in
absolute terms: guides/tutorials portability 2.3% (highest) > blogs
1.8% > category pages 1.6% > product pages 1.2% > homepages 1.1%.
Explanatory, utility-driven content travels best; brand-centric and
transactional pages travel worst.

**Independent corroboration, different metric**: per
[[otterly-url-ai-citations-study-2026]] (1.03M URLs, 1.93M citations,
6 engines), raw citation *frequency* by page type ranks in the same
order — guides 2.7 average citations (+42% vs. baseline), blog/help
pages 2.0 (+5%), news 1.7 (-11%), product/service 1.6 (-16%), pricing
1.5 (-21%). Two differently-sourced studies, different engines,
different metrics (cross-engine portability vs. raw citation count),
same content-type ranking — reference/explanatory content consistently
outperforms transactional content.

## Engines have distinct sourcing "personalities" (authority vs. UGC mix)

[[brightedge-ai-search-same-brands-different-sources]] classifies every
citation by source type (authority, commercial/editorial, UGC) across a
5-engine set (ChatGPT, Perplexity, Gemini, Google AI Mode, Google AI
Overviews) and finds sharply different authority-vs-UGC mixes:

- **Gemini** — "formal institutional recommender": 26% authority
  (gov/academic/institutional), only 0.2% UGC (130:1 ratio), highest
  .gov (13%) and .org (23%) share.
- **Perplexity** — "research librarian": 22% authority, 1.5% UGC,
  concentrates on institutional medical/government/encyclopedic
  sources (30% combined), highest .edu (3.2%) and international ccTLD
  (4.4%) share, and names brands earliest of any engine — 86% land by
  position 5.
- **ChatGPT** — "long-tail editorial engine": 18% authority, only 0.5%
  UGC, flattest source distribution of all five (top 10 domains = only
  18.5% of citations).
- **Google AI Mode** — "broad commercial aggregator": 14% authority, 7%
  UGC, widest unique domain catalog, most even distribution across
  source types.
- **Google AI Overviews** — "UGC-first engine": only 10% authority but
  ~17.5-18% UGC (35x ChatGPT's UGC share) — a single video platform
  alone accounts for 10.6% of its citations, a single forum for 2.9%.

Pairwise source overlap (top-100 lists, Jaccard similarity) ranges
16%-59% across engine pairs — wide and inconsistent. Notably, "Google
AI" is not one thing: AI Mode and AI Overviews (both search-embedded)
share 59% overlap with each other, but Gemini overlaps *more* with
ChatGPT (39%) than with either Google surface (27-34%).

Brand sentiment is overwhelmingly positive across all five engines
(78-96% positive, ≤2.1% negative) regardless of these sourcing
differences.

**A single-platform lens, LinkedIn (2026-07-22 addendum)**: per
[[otterly-linkedin-ai-citations-study-2026]] (2.06M citation records,
6 engines, Jan-Jun 2026), LinkedIn-specific citation share splits
unevenly across engines — **Perplexity alone captures 43.3% of all
LinkedIn citations**, followed by Google AI Overviews (22.2%), ChatGPT
(18.7%), Google AI Mode (9.0%), Microsoft Copilot (6.8%), and Gemini
(essentially zero — 38 citations total). Copilot leans hardest on
long-form Pulse articles specifically (90.2% of its LinkedIn
citations) vs. ~70-74% for the other major engines. This is a
narrower, single-platform data point rather than a challenge to the
broader authority/UGC-mix personalities above — LinkedIn Pulse
articles read as professional long-form publishing rather than
classic UGC, so Perplexity's heavy LinkedIn reliance doesn't
contradict its "research librarian," low-UGC profile above.

## Cited-source sets are volatile month to month

Per [[sel-what-is-generative-engine-optimization-geo-2026]] — a
different dimension than the composition/overlap data above: **40-60%
of cited sources change from one month to the next.** The domain-level
and source-type patterns above describe aggregate tendencies that hold
reasonably stable, but which *specific* URLs/sources get cited for a
given query churns substantially over short timeframes. Practical
implication: track citation performance on a recurring cadence rather
than treating a single snapshot as a durable result, and don't read too
much into losing (or gaining) a citation in any single month without
a trend across several.

## Same source-type layers everywhere, different weighting

Despite the sourcing-personality differences above,
[[brightedge-ai-search-same-brands-different-sources]] finds all five
engines draw from the same three layers, just weighted differently:

1. **Authority** — government, academic, major industry institutions,
   trade associations, analyst firms, standards bodies.
2. **Commercial & Editorial** — review sites, comparison content, trade
   press, news media, finance data, retailer listings. The largest
   layer everywhere: **37-51%** of citations across all five engines.
3. **UGC** — video platforms, forums, community sites, social networks,
   creator coverage.

Practical implication: "authority" should be treated as
category-relative (which trade associations/analyst firms/vertical
experts actually get cited in *your* category), not a fixed domain
list like .gov/.edu.

## Wikipedia, Reddit, and YouTube diverge sharply by provider

- **Wikipedia** is a top-3 cited domain in 12/17 industries for ChatGPT,
  8/17 for Claude, but only 3/17 for Gemini. Investment in Wikipedia
  presence benefits ChatGPT and Claude visibility much more than Gemini.
- **Reddit** is Gemini's single most-cited domain (2.4% of all its
  citations) but essentially absent from ChatGPT (~0.003%) and Claude
  (0%).
- **YouTube**: Claude never cites it (0%); it's ~2% of citations for
  both ChatGPT and Gemini.

## The Axios anomaly

Journalism citations are spread across 20,000+ distinct outlets with no
single dominant publication — except Axios, which appears in ChatGPT's
top-3 cited domains across 13 of 17 industries, a level of cross-sector
breakthrough no other outlet or provider combination matches. By
contrast, Reuters and The New York Times don't appear in the top 3 for
any industry, for any provider, and Claude's top journalism outlet
(CNBC) only cracks the top 3 in a single industry. This is consistent
with Axios's short-form, cross-topic coverage model.

## Recency matters

Among journalism citations with a known publish date, 57% were published
within the past 12 months, accelerating from 50%/11 months measured in
Muck Rack's December 2025 report. Citation volume peaks sharply in the
first month after publication and decays quickly through month six,
though a long tail past three years still accounts for a meaningful
share.

## Query type and sector shape citation mix

"Industry Trend" queries cite journalism at 46% — more than twice the
rate of How-To or Comparative queries (~18-19%) — and drive nearly all
press-release citations (1.16% of Industry Trend responses vs. 0.09% for
How To). Journalism citation rate also varies by sector: highest in
Media/Entertainment (36%) and Finance/Insurance (32%), lowest in
Education and Industrial/Manufacturing (~19% each).

## Citations vs. brand mentions

Per [[similarweb-how-to-be-the-brand-ai-recommends-2026]] — a
conceptual distinction not previously made explicit in this wiki. A
**mention** is the AI saying a brand's name; a **citation** is the AI
pointing to a brand's content as a retrieved source (the brand's
website "gets the footnote"). This maps onto two different underlying
data sources AI draws from:

| | Training data | Live retrieval |
|---|---|---|
| What it is | Frozen snapshot baked in at training time | Real-time web retrieval |
| Update cycle | Months to years | Real time |
| Brand discovery | Only brands present before the training cutoff | Any brand with a crawlable presence |
| Confidence | High — deep, consistent signal | Lower — thinner profile |

**Citations only come from retrieval.** **Mentions** can come from
*either* training data (the model learned to associate a brand with a
topic over time) *or* live retrieval. This reframes
[[airops-fan-out-effect-2026]]'s "memory citations" finding (6,371
citations with no corresponding search result) as, in this framing, a
training-data-sourced mention rather than a true retrieval citation.

**Practical stakes**: citations drive traffic (per
[[aio-ctr-impact]]'s citation-premium data); mentions build presence
even when the user never clicks — relevant given most AI interactions
end without a click (see [[ai-traffic-scale-vs-hype]]). This "mentions
build presence" claim now has direct measured backing: per
[[similarweb-downstream-impact-of-ai-visibility-2026]], brands
recommended (mentioned) by ChatGPT are 2.5x more likely to receive a
site visit within 7 days than a non-recommended competitor — even
though 55.9% of that resulting traffic arrives via a subsequent branded
search rather than a direct AI referral link, meaning a mention's
downstream effect is largely invisible to referral-based traffic
attribution. Per [[tryprofound-ai-mention-effect]] (2M+ AI
conversations), this attribution gap is even starker than the 55.9%
figure suggests: only ~2.5% of downstream visits carry any trackable
AI-referral parameter at all. See [[aio-ctr-impact]] for the full
writeup.

**Different signals drive each**:
- **Recommendation/mention signals**: frequent co-occurrence with the
  brand's category, high branded search volume (humans searching for a
  brand teaches AI it matters), presence in core knowledge sources
  (Wikipedia, Wikidata, major publications), consistent positive
  co-mentions with the category across the web.
- **Citation signals**: unique data points not found elsewhere
  (information gain, not repetition), content freshness (recency is a
  major retrieval weight in RAG systems), clear extractable structure
  (headers, bullets, schema), and co-citation (multiple independent
  sources pointing to the same brand as the answer).

## Citation-slot concentration (unsourced, directional)

Per [[superlines-geo-guide]] (vendor content, no disclosed methodology):
LLM answers reportedly cite only **2-7 domains per response**, versus
Google's traditional 10 blue links — a claim of fewer available
"citation slots" than classic SERP ranking, making visibility more
competitive. Directionally consistent with, but not independently
confirmed by, this page's existing concentration findings (e.g.
[[ahrefs-b2b-seo-statistics-2025]]'s 28.9%-of-AI-Overview-citations-
to-top-50-brands figure) — treat the specific 2-7 range as unverified
until a source with disclosed sampling confirms it.

**Stronger, disclosed-methodology support for the general claim (2026-07-22)**:
[[otterly-url-ai-citations-study-2026]] (1.03M URLs, 1.93M citation
instances, 6 engines, Pearson-correlation methodology) independently
finds a steep citation power law: median 1 citation per URL, but
**15.8% of URLs generate 50% of all citations** (20% generate 54%), and
one URL alone accumulated 965 citations. This doesn't confirm
Superlines' specific "2-7 domains per response" figure, but it's a
rigorously-sourced data point supporting the same underlying claim —
AI citations concentrate heavily among a small minority of URLs.

**An even steeper concentration on a single platform**: per
[[otterly-linkedin-ai-citations-study-2026]] (same author/methodology
family, LinkedIn-only), the power law is sharper within LinkedIn
specifically — top 1% of URLs draw 30.2% of all citations, top 5% draw
54.6%, top 25% draw 83.3%, and **87.4% of LinkedIn URLs are cited only
once** across all six engines combined. Consistent direction, steeper
slope than the general-web figure above — plausibly because LinkedIn's
content pool is itself more skewed toward a small set of established
thought-leadership authors than the open web is.

## Engagement metrics don't predict AI citation

Per [[otterly-linkedin-ai-citations-study-2026]] — the first source in
this wiki to directly test surface engagement signals against AI
citation likelihood (rather than volume, as in
[[ai-visibility-correlation-factors]]'s existing "content volume shows
almost no correlation" finding): likes (r = -0.06), comments (r =
-0.04), emojis (r = -0.02), and hashtags (r = -0.02) all show near-zero
correlation with citation count. Media presence shows *no* citation
advantage either — posts with video averaged *fewer* citations than
posts without (5.85 vs. 7.87); same pattern for images (7.14 vs. 8.23).
The study's own framing: "what gets a post liked does not get it
cited." Consistent with this wiki's broader pattern that AI citation
selection tracks extractability/authority signals rather than
popularity signals — see also [[airops-fan-out-effect-2026]]'s finding
that domain authority doesn't positively correlate with ChatGPT
citation either.

## A correlational, cause-unexamined gender disparity in citation

Per the same source: among LinkedIn authors it could identify as
individuals (88.5% of URLs, gender inferred from names/pronouns/profile
signals for a subset), **men received 76.4% of citations vs. 23.5% for
women**, consistent (23-24% for women) across every major engine
studied. The study does not test or establish a cause. A plausible
confound it doesn't rule out: this could reflect the underlying gender
composition of who publishes long-form Pulse articles/thought-leadership
content on LinkedIn in the first place, rather than a citation-selection
bias introduced by the AI engines themselves. Recorded here as a
factual, correlational finding with an unexamined cause — not evidence
of algorithmic bias one way or the other — because it's a concrete,
disclosed-methodology number future sources on AI-citation demographics
can be compared against.

## Retrieval rank as the primary citation gatekeeper

Per [[airops-fan-out-effect-2026]] (16,851 queries, 353,799 pages
analyzed, ChatGPT) — a mechanism not previously covered anywhere in this
wiki: **where a page lands in ChatGPT's internal retrieval results
dominates whether it gets cited at all**, ahead of any content-quality
signal. Position 1 in retrieval = 58.4% citation rate vs. 14.2% at
position 10 — a 4x gap. Even pages with strong heading-query relevance
(≥0.8 similarity) drop from 79.6% citation at rank 1 to 21.5% at rank
11+. This reframes "citation-worthy content" as a two-stage problem:
first get retrieved/ranked highly by the underlying search step, *then*
compete on content signals — content quality cannot compensate for a
poor retrieval rank.

**Independently corroborated via a controlled experiment (2026-07-22)**:
per [[c-seo-bench-2025]] (NeurIPS 2025), randomly assigning a document
to position 1 in an LLM's context window produced citation-rank gains
several times larger than any content-level tactic tested (across 6
domains, 4 models) — the same conclusion as AirOps' observational
finding above, now shown causally rather than only correlationally.
See [[geo-content-optimization-tactics]]'s "C-SEO Bench" section and
[[generative-engine-optimization]]'s Conflicting Evidence section for
the fuller picture, including that most white-hat content tactics
tested showed no significant citation-rank benefit at all.

Citation distribution is **bimodal**, not a smooth curve: 58% of pages
in the dataset were never cited, 25% always cited, only 17%
intermittently cited — and on-page signals (word count, headings,
readability) show almost no difference between the always-cited and
never-cited groups, reinforcing that retrieval rank, not content
quality, is the real separator between the two populations.

Within retrieved pages, **heading-query match is the strongest content
signal measured**: 41.0% citation at 0.90+ heading-similarity vs.
29-30.2% for weak matches (<0.50). Counterintuitively, **comprehensive
topic coverage underperforms focused coverage** when relevance is held
constant — pages covering 26-50% of a query's fan-out subtopics cited
more often (38.2%) than pages covering 100% (34.0%), and matching 3-4
distinct subheadings reduced citation 6pp versus matching only 0-1.

**"Memory citations"** — 6,371 citations in the dataset had no
corresponding search result at all, meaning ChatGPT cited from training
data directly rather than live retrieval. These memory-cited pages had
content profiles statistically identical to search-cited pages,
suggesting no separate quality bar for training-data citation.

## Citation rate by source type and semantic relevance (ChatGPT)

Per [[ahrefs-why-chatgpt-cites-pages-2026]] (1.4M ChatGPT prompts,
Feb 2025, cosine-similarity semantic analysis) — a more granular
breakdown of ChatGPT's citation behavior than previously in this wiki,
segmented by reference type rather than treated as one aggregate pool:

- **Citation rate varies enormously by source type**: Search 88.46%,
  News 12.01%, Reddit 1.93%, YouTube 0.51%, Academia 0.40%. About 88%
  of all ChatGPT citations come from the search-index reference type
  specifically — ranking in the search index is close to a
  prerequisite for citation.
- **Reddit is retrieved heavily but almost never cited**: 67.8% of all
  non-cited URLs are Reddit — ChatGPT uses it extensively as
  background context/consensus-gauging but rarely attributes to it
  directly.
- **Semantic relevance (cosine similarity) is the strongest measured
  differentiator within a retrieval set**: cited pages score 0.602 on
  prompt-title similarity vs. 0.484 for non-cited pages, and score
  even higher (0.656) against ChatGPT's internal fanout sub-queries —
  direct evidence supporting
  [[peec-ai-chatgpt-query-fanouts-2026]]'s claim that content should
  target the engine's hidden fanout sub-questions, not just the
  surface-level prompt.
- **Natural-language URL slugs correlate with higher citation**:
  89.78% vs. 81.11% for non-natural-language URLs.
  **Nuance, not a clean contradiction (2026-07-22)**: a much larger,
  6-engine study, [[otterly-url-ai-citations-study-2026]] (1.03M URLs,
  n > 1M), found URL *structural* mechanics — length, hyphen count,
  digit presence, path depth — all correlate with citation at
  essentially zero (r = -0.007 to -0.025), and that *question-pattern*
  wording (how-to/what-is) specifically is non-predictive. These aren't
  necessarily incompatible: Ahrefs measured whether a slug *reads* as
  natural language (ChatGPT only), while Otterly measured structural
  proxies and specific keyword patterns (across 6 engines) — a slug
  could be "natural-sounding" independent of its length or whether it
  contains "how-to." But the two studies point in different directions
  on how much URL wording matters overall, and Otterly's null result is
  much more strongly powered. Treat URL-slug wording as a minor,
  possibly ChatGPT-specific lever rather than a broadly reliable one
  until reconciled further.

## Query fanout mechanics

Per [[peec-ai-chatgpt-query-fanouts-2026]] (5M query fanouts across
ChatGPT/Perplexity/Grok, April 2026) — explains the mechanism behind
the "query fan-out" term used elsewhere in this wiki
([[generative-engine-optimization]]), distinct from
[[airops-fan-out-effect-2026]]'s finding about *content* subtopic
coverage: this is about what the *engine itself* injects into hidden
sub-queries before retrieval happens.

- **Fanout volume varies sharply by engine**: Perplexity 1.4
  subqueries/query (minimal expansion), ChatGPT 2.1/query (adds
  brands, comparisons, review keywords), Grok 6.8/query — over 3x
  ChatGPT's rate, treating the prompt as a research brief and
  progressively narrowing by year/brand/trusted domain.
- **ChatGPT's most-injected words**: "best" (into 24.3% of
  advice-style questions, even when the user never used the word),
  "top," "comparison," "reviews" (3rd most common — pulls in
  unrequested review-platform content from Glassdoor/G2/Sitejabber
  and similar), "tools," "software," "features."
- **Ranking mechanism**: ChatGPT combines fanout subquery results via
  Reciprocal Rank Fusion (RRF) — content surfacing across multiple
  fanout subqueries outranks content matching only one, adding a
  concrete mechanism beneath the general "get retrieved across
  multiple angles" intuition.
- **Freshness signal**: a current-year token is injected into 5.44%
  of prompts.
- **Grok explicitly targets trusted domains** via site-operator
  searches in 18.3% of chats; Reddit appears in 10.5% of chats (~90%
  deliberately site-directed, not organic); Wirecutter and Consumer
  Reports are injected by Grok at a 100% rate regardless of whether
  the user asked for them.

**Practical implication**: listicle ("best of"/comparison/review)
framing structurally matches the dominant fanout injection pattern —
offered as a mechanism explaining why listicle content dominates AI
answer results. See [[listicles-in-ai-search]] for the full listicle
picture built on this mechanism.

## Listicles: rank effects, self-promotion, and the recommendation filter

Moved to its own concept page (2026-07-08 lint pass) as listicle
studies accumulated: see [[listicles-in-ai-search]] for the listicle
rank effect ([[peec-ai-listicle-rank-effect-2026]]), self-promotional-
listicle citation rates
([[peec-ai-self-promotional-listicles-2026]]), and the
citation-vs-recommendation decoupling in Google AI Overviews
([[sej-why-calling-yourself-the-best-2026]]), plus the reconciliation
of the latter two findings.

## AI Overview citation composition and the citation-without-ranking gap

Per [[ahrefs-b2b-seo-statistics-2025]] — a small set of B2B-context
stats that add useful texture to the citation-composition findings
above:

- **76% of AI Overview citations pull from Google's own top-10 organic
  results** — reinforcing [[airops-fan-out-effect-2026]]'s
  retrieval-rank-as-gatekeeper finding specifically within Google's
  own AIO surface, alongside the ChatGPT-specific "~88% of citations
  come from the search-index reference type" finding in
  [[ahrefs-why-chatgpt-cites-pages-2026]] above — a consistent pattern
  across both Google's and OpenAI's systems that ranking well in
  classic search remains close to a prerequisite for AI citation.
- **28.9% of AI Overview citations concentrate on just the top 50
  brands** in a category, and **26% of brands get zero AI Overview
  mentions at all** — a visibility-concentration pattern consistent
  with this page's "presence/portability/concentration" framing above.
- **Citation doesn't require organic visibility**: 28% of ChatGPT's
  most-cited pages have **zero Google organic visibility** — a genuine
  nuance on the "ranking is close to a prerequisite" finding above.
  Plausible reconciliation (not directly tested by either source):
  this likely reflects the non-search reference types
  ([[ahrefs-why-chatgpt-cites-pages-2026]]'s News/Reddit/Academia
  categories) or memory-citation behavior
  (see the "Retrieval rank as the primary citation gatekeeper" section
  above), which don't require the cited page to rank organically at
  all. Not logged as a formal conflict since it's a minority-share
  nuance on an already-probabilistic claim, not a direct contradiction.
- **Unverified temporal-decline claim (2026-07-22)**: this "76%
  top-10" figure describes a static snapshot. [[rankability-where-seo-is-going-2026]]
  asserts the overlap between top-10 Google rankings and AI-answer
  citations "collapsed from ~75% in mid-2025 to 17-38% by early 2026,"
  which — if true — would mean this 76% figure and
  [[ipullrank-optimize-for-sge]]'s "93.8% of AIO citations weren't in
  top-10" figure are both compatible snapshots of a fast-moving trend
  rather than a genuine contradiction. However, the Rankability report
  gives **no inline source for this specific figure**, and its own
  primary dataset (a keyword-demand panel) doesn't measure citation
  composition at all — so this doesn't count as independent
  verification. Flagged as an unverified claim worth watching for
  corroboration, not treated as resolving the existing tension between
  the 76%/93.8% figures.
  - **A contradicting unverified counter-claim (2026-07-22)**: per
    [[otterly-how-to-optimize-content-for-ai-search-2026]], citing
    BrightEdge with no link given, this same overlap reportedly *grew*
    from 32.3% to 54.5% — the opposite trend from Rankability's claim
    directly above. Like that figure, this one has no disclosed
    methodology either, so it doesn't resolve anything — it's a second
    unverified voice pointing the opposite direction from the first.
    For what it's worth, 54.5% sits closer to the better-sourced
    76%-top-10 figure from [[ahrefs-b2b-seo-statistics-2025]] than
    Rankability's 17-38% range does, though none of these three
    studies are directly comparable. Treat "is ranking/citation
    overlap rising or falling over time" as genuinely open until a
    disclosed-methodology source measures it directly.

## Topic-specific source trust

Per [[growth-memo-topics-matter-for-third-party-authority]], trusted-source
mix varies sharply not just by *engine* (see "personalities" above) but by
*topic within the same engine*: competitor domains account for 33.5% of
citations on invoicing queries but only 7% on business-startup queries.
This sharpens the "authority is category-relative, not a fixed domain
list" finding above — it isn't just industry-relative, it can shift
topic-by-topic within one category, so a source map has to be built per
topic, not assumed to carry over from an adjacent one.

## Local queries lean on Google Maps, not articles

For "best of" local queries (best hotels, restaurants, services),
ChatGPT systematically cites Google Maps search results — 188 citations
per 1,000 such queries, averaging ~7 map pins per response — rather than
reviews or editorial content. Claude cited Google Maps only once in the
entire study.

## Citations change what the model actually says

Not just a visibility/attribution mechanism: enabling web citations can
change the substantive correctness of an answer, not just add sources to
an otherwise-fixed response. Example from the source: asked for the
worst MLB team ever, a model without citations answered with an outdated
fact (1962 Mets), while with citations enabled it correctly cited a more
recent record-holder (2024 White Sox). This reinforces
[[google-ai-optimization-guide]]'s framing of generative answers as
grounded in retrieval (RAG), not a static trained "understanding."

## Conflicting Evidence

- **Claim**: optimal content age for AI citation.
  - Supported by: [[airops-fan-out-effect-2026]] (via
    [[geo-content-optimization-tactics]]'s "Freshness by vertical"
    section) — optimal content age is 30-89 days, with citation
    declining for content over 2 years old. Additional data points on
    this side: [[ahrefs-b2b-seo-statistics-2025]] reports AI platforms
    show a 25.7% stronger fresh-content preference than traditional
    search (aggregate, not source-type-segmented), and
    [[muckrack-generative-pulse-ai-reading-may-2026]]'s recency finding
    (57% of journalism citations under 12 months old — though that's
    news-media-specific, consistent with the news-vertical carve-out
    below). A further, secondhand data point:
    [[otterly-how-to-optimize-content-for-ai-search-2026]] cites Monash
    University (no link given) for "sources cited in AI responses are
    26% fresher than traditional search results" — undisclosed
    methodology, so treat as directional support rather than
    independent confirmation.
  - Contradicted by: [[ahrefs-why-chatgpt-cites-pages-2026]], which
    finds that within search-result retrieval sets specifically,
    older/established content (median ~500 days, some pages 2,700+
    days old) is cited *more* than fresher content — the opposite
    direction. The same source's news-vertical data (fresher articles,
    ~200 vs. ~300 days, cited more) is at least directionally
    consistent with AirOps's freshness preference, but only within
    that one source type.
- **Current best guess**: likely a reference-type/segmentation
  difference rather than a true contradiction — AirOps's dataset isn't
  broken out by source type the way Ahrefs's is, so its "30-89 days
  optimal" finding may be an average across a source mix (including
  news, where freshness does help) that masks a different pattern in
  pure search-result citations (where relevance/authority of an
  established page can outweigh recency). Flagged as **unresolved**
  since neither source directly tests the other's segmentation; until
  resolved, treat freshness guidance as vertical/source-type-dependent
  rather than a single universal age curve.

## Conflicting Evidence — resolved

- **Claim**: The three major AI answer surfaces operate as largely
  independent, non-overlapping information environments (per "Providers
  are three separate information environments" above).
  - Supported by: this page's own domain-level citation-overlap findings
    from [[muckrack-generative-pulse-ai-reading-may-2026]] (covering
    ChatGPT/Claude/Gemini), independently corroborated by
    [[sej-the-consensus-gap]] (covering ChatGPT/Perplexity/Google AI
    Overviews, 3.7M citations, four samples over a full year).
  - Apparently contradicted by: [[ahrefs-ai-brand-visibility-correlations]]
    (covering ChatGPT/AI Mode/AI Overviews), which found high
    correlation (0.75–0.82) in *which brands* get mentioned across all
    three.
  - **Resolved (2026-07-07)** by
    [[brightedge-ai-search-same-brands-different-sources]], which tests
    both halves directly on the same 5-engine dataset: pairwise
    *source*-overlap (16-59%) is measurably wider/more inconsistent than
    pairwise *brand*-overlap (36-55%) across every engine pair studied.
    Different engines really do cite different specific sources
    (confirming the Muck Rack/SEJ side) while still converging on
    largely the same brands (confirming the Ahrefs side) — not a
    contradiction, but two true findings at different units of
    analysis, now empirically linked rather than just plausibly
    inferred. See [[ai-visibility-correlation-factors]] for the full
    writeup, including a residual methodology caveat (BrightEdge's
    aggregate top-100-list overlap numbers read higher than SEJ's
    per-prompt exact-URL overlap — a granularity difference, not a
    contradiction).

## See also

- [[sel-what-is-generative-engine-optimization-geo-2026]] — the source
  for the 40-60% month-to-month citation volatility figure above.
- [[growth-memo-topics-matter-for-third-party-authority]] — the
  topic-vs-competitor-domain-share data point cited above, plus tiered
  authority-accumulation and named-author findings covered in
  [[geo-content-optimization-tactics]].
- [[airops-fan-out-effect-2026]] — the retrieval-rank-as-gatekeeper
  mechanism above, plus the authority-correlation Conflicting Evidence
  writeup in [[ai-visibility-correlation-factors]].
- [[similarweb-how-to-be-the-brand-ai-recommends-2026]] — the
  citations-vs-mentions distinction and two-data-source framing above,
  plus corroborating data in [[geo-content-optimization-tactics]] and
  [[aio-ctr-impact]].
- [[sej-the-consensus-gap]] — the independent, large-scale confirmation
  of citation-level cross-engine fragmentation cited throughout this
  page, plus the presence/portability/concentration measurement
  framework.
- [[brightedge-ai-search-same-brands-different-sources]] — the 5-engine
  source-vs-brand overlap comparison that resolves the Conflicting
  Evidence above, plus the engine personality profiles and three-layer
  source framework.
- [[generative-engine-optimization]] — tactics for increasing citation
  visibility once retrieved.
- [[ai-visibility-correlation-factors]] — which brand/SEO metrics
  correlate with AI-mention visibility, and the full reconciliation of
  the Conflicting Evidence above.
- [[geo-content-optimization-tactics]] — actionable playbook, now
  including provider-specific guidance drawn from this landscape data.
- [[peec-ai-chatgpt-query-fanouts-2026]] — the query-fanout injection
  mechanics above (engine-side hidden subquery behavior), distinct
  from and complementary to [[airops-fan-out-effect-2026]]'s
  content-coverage finding.
- [[listicles-in-ai-search]] — the listicle rank effect,
  self-promotional-listicle citation rates, and the
  citation-vs-recommendation decoupling, split out of this page.
- [[ahrefs-why-chatgpt-cites-pages-2026]] — the source-type citation-
  rate breakdown, semantic-relevance data, and unresolved content-age
  Conflicting Evidence above.
- [[ahrefs-b2b-seo-statistics-2025]] — the AI Overview citation-
  composition and citation-without-organic-visibility data above.
- [[rankability-where-seo-is-going-2026]] — source of the unverified
  75%→17-38% ranking/citation overlap decline claim above.
- [[otterly-url-ai-citations-study-2026]] — the page-type citation-
  frequency corroboration, power-law concentration data, and
  URL-slug-wording nuance above.
- [[otterly-linkedin-ai-citations-study-2026]] — the LinkedIn-specific
  platform-split, steeper concentration, engagement-null-correlation,
  and gender-disparity findings above.
- [[otterly-how-to-optimize-content-for-ai-search-2026]] — the
  contradicting overlap-growth counter-claim and freshness data point
  above.
