---
type: concept
tags: [seo, aeo]
updated: 2026-09-10
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
  web — more than twice ChatGPT's depth. **Additional detail
  (2026-07-23)** per [[otterly-claude-ai-citation-study-2026]] (379K
  citations, June 2026): Claude's citations are dominated by first-party
  brand/company-owned content (64% of all citations), news/media (14.9%),
  and long-tail sources — sharply different from the ChatGPT/Gemini/
  Perplexity mix dominated by third-party reviews/forums. Social media is
  nearly absent (0.9%, almost entirely LinkedIn; Reddit 0%).

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

## Citation selection vs. absorption

Per [[citation-selection-vs-absorption-geo-framework-2026]] (602
prompts, 21,143 citations, ChatGPT/Google AI Overview/Perplexity) — a
complementary measurement axis to presence/portability/concentration
above. Where that framework asks *whether and where* a source appears
across a citation landscape, this one asks *how much a given citation
actually shapes a single answer* — a genuinely different property:

- **Citation breadth and depth diverge sharply by platform.**
  Perplexity cites the broadest source set (16.35 sources/answer avg)
  but each source has the lowest average "influence" (0.0646).
  ChatGPT cites the fewest sources (6.88 avg) but each cited source
  carries roughly 4x higher influence (0.2713) than Perplexity's. Being
  cited widely and being cited *deeply* are separate achievements.
- **Influence ("absorption") is measured by**: repeated reference
  within the answer, early appearance, coverage across multiple answer
  paragraphs, TF-IDF similarity to the answer text, and n-gram overlap
  — not just whether a citation link appears.
- **High-influence pages are structurally denser**: 11.4x more words,
  12.5x more headings, 8.94x denser lists than low-influence pages, and
  a moderate semantic-alignment correlation (r=0.43) with LLM-judged
  relevance.
- **Evidence genre drives absorption more than formatting wrapper
  alone**: definitions (+57%), comparisons (+55%), and code (+77%)
  measurably raise influence; Q&A-style formatting by itself, without
  real evidence density, actually shows a *negative* relative effect
  (-5.74%) — formatting isn't a substitute for substance.
- **News is cited often but absorbed weakly** (0.0726 influence) vs.
  **encyclopedic content** (0.2144) — a concrete example of the
  selection/absorption gap: frequency of citation doesn't predict depth
  of use.

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

**Independently corroborated (2026-08-12 addendum)**: a second LinkedIn
study, [[semrush-linkedin-ai-visibility-study-2026]] (89K LinkedIn URLs,
325K prompts, 3 engines, Jan–Feb 2026), independently finds LinkedIn is
~#2 source at **~11% of AI responses**, that **long-form original
articles dominate** (95% of citations original; articles 50–66%), and
that **engagement/follower count don't drive citation** (median cited
post 15–25 reactions; <500-follower authors cited equally or more) —
replicating the Otterly findings on a different sample and engine set. It
adds a **posting-consistency** signal (75% of cited authors post 5+ times
in four weeks). One divergence on company-vs-individual mix is logged
under Conflicting Evidence below. (Note the two studies' per-engine
percentages aren't directly comparable: Semrush's Perplexity 5.3% is *%
of responses citing LinkedIn*, whereas Otterly's Perplexity 43.3% is
*share of all LinkedIn citations captured by that engine* — different
denominators, not a conflict.)

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
  **Note (2026-07-23)**: Wikipedia appears in 8/17 for Claude, but per
  [[otterly-claude-ai-citation-study-2026]], Claude's citations are 64%
  brand/company-owned first-party content; Wikipedia is an institutional
  outlier in Claude's citation pattern, not representative of typical
  Claude sourcing.
- **Reddit** is Gemini's single most-cited domain (2.4% of all its
  citations) but essentially absent from ChatGPT (~0.003%) and Claude
  (0%). **Quantified per (2026-07-23)** [[otterly-claude-ai-citation-study-2026]]:
  Reddit was cited **0 times** across 379K Claude citations — not a rounding
  artifact but a hard zero.
- **YouTube**: Claude never cites it (0%); an earlier estimate put it at
  ~2% of citations for both ChatGPT and Gemini. **Context (2026-07-23)**:
  YouTube, Reddit, and other social platforms together represent only 0.9%
  of Claude's citations, making them immaterial to Claude strategy.
  **Sharper, larger-scale data (2026-07-23)**: per
  [[otterly-youtube-ai-citation-study-2026]] (100M+ citation instances,
  6 engines, 30-day window), YouTube's share of a platform's citations
  is highly uneven and *not* symmetric across ChatGPT and Gemini as the
  earlier "~2% for both" figure implied — ChatGPT 4.4% (same order of
  magnitude as before), but Gemini only 0.2% (an order of magnitude
  lower, not "roughly on par with ChatGPT"). Perplexity (38.7%) and
  Google AI Overviews (36.6%) are by far the heaviest YouTube citers;
  Google AI Mode 19.6%; Copilot 0.5%. **Unresolved discrepancy on the
  Gemini figure specifically** — not logged as a full Conflicting
  Evidence entry since the ChatGPT figure is directionally consistent
  and only the Gemini number diverges sharply, but flagged here pending
  a source that reconciles the two.

### Profound's ChatGPT/Google AI Overviews/Perplexity citation breakdown (2026-07-23 addendum)

Per [[tryprofound-ai-platform-citation-patterns]] (680M citations,
Aug 2024–Jun 2025) — a different platform trio (ChatGPT, Google AI
Overviews, Perplexity) than most of this section's Wikipedia/Reddit/
YouTube data, but the same underlying pattern:

- **ChatGPT**: Wikipedia leads at 7.8% of total citations (47.9% of its
  top 10) — consistent with the "long-tail editorial engine," Wikipedia-
  heavy characterization above. Reddit is a minor secondary source at
  1.8% — same order of magnitude as [[ahrefs-why-chatgpt-cites-pages-2026]]'s
  1.93% Reddit citation-rate figure below, via an independent
  methodology.
- **Perplexity**: Reddit leads at 6.6% of total citations (46.7% of its
  top 10) — a **"community-driven information"** profile that reads as
  in tension with brightedge's "research librarian," low-UGC (1.5%)
  characterization of Perplexity above. Not logged as a full
  Conflicting Evidence entry — different time periods and citation
  definitions (aggregate share of 680M raw citations vs. a
  source-type-classified sample) could both be locally accurate without
  contradicting each other, but it's a real magnitude tension worth
  tracking if a reconciling source appears.
- **Google AI Overviews**: Reddit (2.2%) and YouTube (1.9%) lead, with
  Quora (1.5%) and LinkedIn (1.3%) close behind — a "balanced
  social-professional mix." This is directionally consistent with
  brightedge's "UGC-first engine" characterization, but the magnitudes
  diverge sharply: brightedge put a single video platform at 10.6% of
  AI Overviews citations and a single forum at 2.9%, vs. Profound's
  1.9%/2.2% here. **Unresolved discrepancy** — flagged rather than
  reconciled, likely reflecting different sampling windows/methodology
  rather than a real behavior change, but not confirmed either way.
- **Domain TLD mix** (aggregate across all three platforms, not
  broken out per-engine): .com 80.41%, .org 11.29%, country-specific
  ccTLDs (.uk/.au/.br/.ca) ~3.5% combined, with .io/.ai tech TLDs
  described as "growing" despite newer/smaller base rates. A coarser
  lens than brightedge's per-engine .gov/.edu/.org shares above, but a
  useful aggregate sanity check.
- **Strategic framing**: explicitly argues "a one-size-fits-all
  approach to AI visibility cannot succeed" given these platform-
  specific sourcing preferences — the same practical conclusion this
  wiki has already reached independently via brightedge's "sourcing
  personalities" and the provider-specific tactics in
  [[geo-content-optimization-tactics]].

### YouTube citation structure (2026-07-23 addendum)

Per the same source — video-level structural findings distinct from the
per-provider share above:

- **Long-form dominates overwhelmingly**: 94% of AI citations go to
  long-form videos, only 5.7% to Shorts.
- **Timestamps are a Google-exclusive citation mechanism**: timestamped/
  chapter-level citations appear only in Google AI Overviews (73% of
  timestamped citations) and Google AI Mode (27%) — zero in ChatGPT,
  Gemini, Copilot, or Perplexity. Only 31% of cited videos carry
  timestamp signals, but 78% of those get cited repeatedly across 2-5
  different chapters, multiplying one video's effective citation
  surface area on Google surfaces specifically.
- **Popularity doesn't predict citation, same as elsewhere in this
  wiki**: view count (r = -0.03), likes (r = -0.02), subscriber count
  (r = -0.03), and channel total views (r = -0.03) are all
  uncorrelated with citation frequency — 40.83% of cited videos have
  under 1,000 views and 35% come from channels under 10k subscribers.
  Consistent with [[otterly-linkedin-ai-citations-study-2026]]'s
  near-zero engagement correlations on LinkedIn and
  [[airops-fan-out-effect-2026]]'s no-authority-correlation finding —
  a third platform showing the same pattern (structure/relevance beats
  popularity/authority as a citation predictor).
- **Weak positive correlates**: description length (r = 0.31) and
  description hashtags (r = 0.20) — treat descriptions as
  machine-readable metadata (summaries, entities, chapters) rather than
  marketing copy.

### Reddit community engagement (2026-07-23 addendum)

Per [[otterly-reddit-geo-ai-search-citations-2026]] (8,167 citations,
60-day controlled experiment, 126 subreddits, 5 engines) — a causal
(experimental) finding on what drives Reddit citations, complementing
the earlier observational finding that Reddit is "retrieved heavily but
rarely cited" from [[ahrefs-why-chatgpt-cites-pages-2026]]:

- **Active community engagement drives a 9x citation multiplier**:
  subreddits with managed engagement (+10 replies, +20 upvotes per post)
  received 9x more AI citations than identical posts in zero-engagement
  control subreddits — the strongest platform-specific lever measured in
  any Otterly study to date.
- **Comments drive more citations than upvotes or post length**: replies
  to a post matter more than vote count or word count. Distinct from
  "engagement doesn't predict citation" findings on other platforms
  ([[otterly-linkedin-ai-citations-study-2026]]) because this measures
  *active discussion* (replies/comments as a signal of community interest
  in the topic), not passive metrics (likes, emojis).
- **Community size (subscribers) is not predictive**: larger subreddits
  don't systematically get cited more — consistent with the
  YouTube-channel-size and LinkedIn-brand-size null findings.
- **Citation distribution smoothens across active communities**: engagement
  activity spreads citations more evenly across multiple posts, rather
  than concentrating on a few winner-take-all posts — suggesting
  engagement signals that a community is actively discussing the topic
  at breadth, not just spotlighting one piece.
- **SEO bonus from Reddit activity**: the same engagement treatment
  showed x18 impact on traditional search rankings — Reddit activity
  improves both AI citations *and* Google organic ranking for the same
  content, making Reddit participation a dual-channel lever.
- **Maintenance is lightweight**: ~30 minutes daily engagement over 60
  days achieves the multiplier; extrapolates to ~15 hours monthly to
  sustain. This is tractable for content teams as an active-community
  strategy.

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

**Training memory also drives *what the model searches for* (2026-08-06):**
the two data sources aren't cleanly independent — per
[[geosurge-model-memory-predicts-search-2026]] (geoSurge; 9 industries,
66 buyer questions, 1,416 brand observations; memory measured on a
separate model, search on Gemini 3.5 Flash), **a brand in the model's
top-10 training memory was live-searched 55.7% of the time vs. 17.4% for
a not-remembered brand — a 3.2× gap**, graded by recall depth (top-5
67%, rest of top-10 39%, not-remembered 17%). And 69% of the model's
fan-out queries were generic *category* searches; of the 31% that named
a specific brand, 63% named a top-5 remembered brand. So training memory
isn't just a *separate* mention pathway alongside retrieval — it biases
which brands the model bothers to *retrieve* in the first place, making
memory an upstream input to the citation pathway too, not only the
mention pathway. Two category regimes emerged: *memory-led* (Automotive,
Finance — searches track recalled brands tightly) vs. *search-led*
(strong live content can surface unremembered brands). **Caveats:**
vendor source, explicitly associational (brand prominence is an
acknowledged confound — prominent brands are both more remembered *and*
more searched), undisclosed proprietary memory metric, single search
model, some per-industry figures rest on as few as 6 prompts. Treat as a
directional mechanism, not a measured effect size.

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

**Empirical measurement of the decoupling (2026-07-30)**: this
mention/citation split is not just conceptual — it is now measured at
scale. Per [[semrush-chatgpt-topic-authority-study]] (Semrush × Kevin
Indig, 1,094 ChatGPT categories, 600K+ citations), only **21%** of the
most-*cited* domains in a category were also the most-*mentioned* brand,
and the two correlate **slightly negatively (-0.229)**. The source
ChatGPT quotes and the brand ChatGPT recommends are largely different
entities. This matters for prioritization because mention share sits
closest to selection: per Kevin Indig's earlier Growth Memo research,
**74% of users chose the top-mentioned brand as their final pick** (see
[[ai-shortlist-effect]] for the selection-stage data, and
[[topical-authority-in-ai-search]] for the full topic-ownership study).

**Citations almost never point to a brand's own domain (2026-07-30)**:
per [[victorious-q2-2026-quarterly-search-report]] (175 brands, 8
platforms, 49,391 citations), **99.99%** of category-research citations
pointed to *third-party* websites rather than the brand's own site —
only 4 of 150 brands earned a citation to their own domain. And the
mention/citation split is stage-dependent: on *problem-awareness*
prompts, brands were named in just **0.10%** of answers even though
their educational content was being cited (the model uses your content
but omits your name), rising **>12x** on down-funnel *category-research*
prompts. Practical read: winning the *citation* (your content is the
source) and winning the *mention* (you are the recommended brand) are
distinct, and self-citation is a losing game — mentionability is earned
through third-party footprint (see [[ai-visibility-correlation-factors]]
and [[geo-content-optimization-tactics]]'s third-party-authority
tactics).

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

**Unreconciled secondhand figure (2026-08-20)**: [[zyppy-fan-out-framework-2026]]
attributes to AirOps a different number — "ChatGPT cited the #1-ranked
page 43.2% of the time" — with no link or methodology given. This
wiki's own ingest of the AirOps report contains no 43.2% figure; the
only rank-1 citation rate on record is the 58.4% above (ChatGPT's
*internal retrieval* rank). A plausible but unconfirmed reconciliation:
Shepard's figure may describe *Google's organic rank 1* → ChatGPT
citation likelihood, a different metric than AirOps's retrieval-rank
framing — but the wiki's source ingest has no such breakdown to verify
this against. Flagged as an unreconciled discrepancy, not adopted.

**Another data point, milder magnitude (2026-08-20)**: per
[[commoncrawl-web-graph-ai-ranking-signals-2026]] (secondhand,
attributed to "Brie Moreau's analysis," 2M citations / 177M sources,
undisclosed methodology — treat as directional), Google organic
position 1 correlates with a 46-48% AI citation probability, dropping to
~37% at position 2 and ~19-20% at position 10. Same direction as
AirOps's 58.4%/14.2% rank-1/rank-10 figures above, but a gentler
falloff — plausibly because this dataset isn't segmented by engine or
reference type the way AirOps's ChatGPT-only, internal-retrieval-rank
figures are (this one appears to measure *Google organic* rank, not
internal AI-retrieval rank). Not logged as a conflict given the
undisclosed methodology and likely metric difference.

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

## Perplexity and semantic homogeneity as a citation mechanism

Per [[goliath-david-generative-search-perplexity-2025]] (4,060 queries,
98,477 sites, Google AI Overview vs. conventional search) — a
different, complementary axis from the semantic-relevance finding
above, focused on *why* generative engines prefer the sources they do
at a linguistic level, not just a topical one:

- **Lower perplexity (more linguistically predictable text) raises
  citation odds**: a one-standard-deviation decrease in a page's
  perplexity raises its citation probability from ~47% to ~56%. This
  is a property of how "easy" the text is for the underlying language
  model to process, distinct from topical/semantic relevance to the
  query.
- **Cited source sets are more semantically homogeneous with each
  other** than a conventional SERP's top results are — generative
  engines appear to prefer an internally coherent set of sources, not
  just individually relevant ones.
- **The preference is intrinsic to the LLM, not Google-specific
  engineering**: the same low-perplexity/homogeneity citation pattern
  reproduced in an independent RAG pipeline built directly on Gemini's
  API, outside Google Search's production system.
- **Positional bias**: content placed near the beginning of a document
  gets preferential consideration by the retrieval/generation process
  — reinforcing (from a different angle) the inverted-pyramid,
  lead-with-the-answer guidance in [[seo-copywriting]] and the
  chunk-level optimization guidance in
  [[geo-content-optimization-tactics]].
- **Content-polishing paradox**: LLM-based rewriting to reduce
  perplexity was expected to homogenize what gets cited, but instead
  *increased* citation diversity in AI summaries (+1-2 additional
  sources on average) — lowering perplexity widens the pool of
  citable content rather than narrowing it to a few "ideal" sources.

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

### ChatGPT fan-out escalation and `site:` operator targeting (2026-08-20 addendum)

Per [[lilyray-chatgpt-fanout-queries-2026]] (secondary aggregation of
~7 independent researchers/tools, undisclosed methodology throughout —
treat as directional) — a substantial escalation of the fan-out
behavior above, apparently tied to a ChatGPT model update ("ChatGPT
5.6," not independently confirmed):

- **Fan-out volume jumped well past the April-2026 baseline**:
  single-fan-out-query share dropped from 94.0% to 43.5%, average
  retrieved sources roughly doubled (~12 → ~24 pages), and average
  fan-out queries per prompt rose from 2.17 to 7.61 (Chris Long) —
  more than 3x the 2.1/query ChatGPT figure recorded above, now closer
  to Grok's 6.8/query "research brief" style than to ChatGPT's earlier
  narrower fan-out pattern.
- **`site:` operator usage in ChatGPT fan-outs rose from 0.3% to 23%**
  of fan-outs — the trusted-domain site-targeting behavior previously
  documented above as Grok-specific (18.3% of chats) appears to be
  spreading into ChatGPT's own default retrieval behavior. Targeting is
  query-type-dependent: opinions/reviews → Reddit/specific subreddits;
  legal/health (YMYL) → `.gov` domains exclusively in some tests;
  product specs/pricing → brand official domains (e.g.
  `site:sephora.com`, `site:costco.com`).
- **Retrieval and citation are diverging, not scaling together**: even
  as retrieved-page volume roughly doubled, unique domains cited per
  response *dropped* (19 → 15) — citations are concentrating on fewer
  domains despite a wider retrieval net, sharpening this page's broader
  concentration findings (see "Citation-slot concentration" above).
- **"Decides before it searches," now quantified at the citation
  level**: brands named in ChatGPT's initial fan-out query get cited
  68.9% of the time, vs. 2.1% for brands whose pages were merely
  fetched without being named in the query (Suganthan Mohanadasan);
  initial queries contained brand names the user never mentioned in 21
  of 27 product-category tests. This sharpens
  [[geosurge-model-memory-predicts-search-2026]]'s training-memory-
  predicts-search-frequency finding into a training-memory-predicts-
  citation-outcome finding — being in the model's pre-retrieval
  "shortlist" doesn't just make a brand more likely to be searched for,
  it makes it far more likely to be cited once retrieval happens.
- **Domain confusion is a live risk as `site:`-restricted retrieval
  grows**: ChatGPT has constructed `site:` queries against the wrong
  domain entirely — e.g. `site:census.com` for the startup Census,
  which actually operates at `getcensus.com` (Malte Landwehr). A
  security-adjacent variant of the same failure mode: Netcraft found
  ~1/3 of brand login links generated by LLMs pointed to domains the
  brand didn't own, and ~29% targeted unregistered/parked domains.
  Practical implication: as more retrieval becomes `site:`-gated, a
  wrong-domain association isn't just a mis-citation risk but a
  full-channel invisibility risk for that brand.
- **Reddit's retrieve-heavy/cite-rarely pattern, sharper number**: Dan
  Petrovic reports ChatGPT discards Reddit retrievals ~99% of the time
  — directionally consistent with, and starker than,
  [[ahrefs-why-chatgpt-cites-pages-2026]]'s 1.93% Reddit citation-rate /
  67.8%-of-non-cited-URLs-are-Reddit finding above. Not logged as a
  conflict — same direction, undisclosed sample behind the newer
  figure.
- **Possible early counter-signal on listicles**: product pages now
  comprise 16.39% of retrieved pages while listicles/how-to/comparison
  pages are reportedly losing retrieval share — not yet a citation-rate
  comparison, and not corroborated elsewhere in this wiki, so treat as
  a watch item against [[listicles-in-ai-search]]'s listicle-dominance
  findings rather than a contradiction of them.

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

### AIO ↔ SERP divergence: a disclosed-methodology mid-range data point (2026-08-03)

Per [[derivatex-two-googles-one-query-aio-vs-serp-2026]] (DerivateX,
Apoorv Sharma; 100 B2B-software buyer-intent queries, 1,259 AIO
citations vs. 1,000 top-10 SERP results, single-session captures
June–July 2026; methodology fully disclosed, limitations acknowledged —
B2B-software-only and non-deterministic, so treat as directional). This
measures the same quantity as the disputed figures above — the share of
AIO citations that also appear in Google's own top-10 — and lands
**squarely in the middle of the existing spread at 35%** (vs.
[[ahrefs-b2b-seo-statistics-2025]] 76%, [[ipullrank-optimize-for-sge]]
6.2%, [[rankability-where-seo-is-going-2026]] 17–38%, and
[[otterly-how-to-optimize-content-for-ai-search-2026]]'s 54.5%). It
doesn't resolve the open question, but it's one of the better-documented
points in it. New, distinctive contributions beyond the overlap number:

- **65% of AIO citations are AIO-exclusive** (don't rank in Google's own
  top-10), and the relationship is **asymmetric**: only 42% of Google's
  top-10 domains get cited in the AIO shown above them. The two surfaces
  behave as "separate discovery layers with separate content
  preferences," not one ranked list feeding the other.
- **Ranking is necessary-but-not-sufficient, and specifically top-5.**
  When a source *does* appear on both surfaces, 72% rank in Google's
  **top-5** (median position #4); only 2 of the shared instances came
  from positions #9–10. Page-2 rankings essentially never cross over.
  This refines [[richsanger-ai-overview-patent-insights]]'s position-1/2
  inclusion-rate finding and the retrieval-rank-gatekeeper theme above:
  ranking well concentrates presence in the shared corpus, but can't by
  itself buy into the AIO-exclusive 65%.
- **Product-recommendation overlap is even lower — 28%** (72% of
  AIO-recommended products don't rank in SERP for the same query),
  ranging 0% (32/100 queries) to 100% (5/100).
- **Source-type mix diverges within Google itself:** AIO over-indexes on
  third-party listicles (63.4% vs. 55.4% SERP) and video (9.0% vs. 2.3%)
  and under-indexes on Reddit/forums (4.7% vs. 11.0%) and review sites
  like G2/Gartner (5.0% vs. 9.9%). The **YouTube–Reddit inversion** is
  the largest structural gap: AIO cites YouTube 7.3× more often than SERP
  ranks it (51 vs. 7 of 100 queries), while SERP ranks Reddit 1.9× more
  often than AIO cites it — corroborating the heavy Google-AIO YouTube
  reliance in [[otterly-youtube-ai-citation-study-2026]] (36.6%) and the
  "YouTube as first-class AIO source" finding, now *within* a direct
  same-query AIO-vs-SERP comparison. See the YouTube/Reddit provider
  section above.
- **Category divergence tracks listicle-ecosystem maturity:** overlap
  ranged from ~20% (help desk, project management) to 62% (QuickBooks
  hosting, the one category strongly tracking Google). Categories with
  mature third-party "best-of" listicle ecosystems diverge most from
  Google rankings; thin-listicle categories converge on them.

**Rigorous academic corroboration (2026-08-06):** per
[[xu-measuring-google-ai-overviews-2026]] (Xu, Iqbal & Montgomery / WashU;
55,393 trending queries, 7,583 AIOs, 61,212 references) — the most
rigorously-sourced measurement of AIO↔SERP overlap in the wiki, and it
lands in the same mid-range: only **41.4% of AIO-cited domains appear in
the query's top-10 organic results** (25.0% at top-5), rising to 70.2%
across the *full* first page — so **29.8% of AIO-cited domains are
"off-page,"** absent from the first-page SERP entirely. The authors
conclude AIO source selection is "a mechanism distinct from Google's
ranking algorithm." Two further findings sharpen the picture: the
off-page references are *higher* quality than the on-page ones (PC1
credibility 0.758 vs 0.724, UGC 3.4% vs 18.5%), and AIO-cited domains
overall are more credible than the co-displayed first-page results (PC1
0.732 vs 0.645, p≪0.001) — Google's AIO doesn't just re-rank the SERP, it
reaches for a distinct, higher-authority, lower-UGC source pool. This is
independent academic confirmation of the "separate discovery layers"
reading, at the top-10 level closest to DerivateX's 35% and Otterly's
54.5% (and far from Ahrefs' 76%/iPullRank's 6.2% ends of the spread).

**AIO suppresses UGC relative to the SERP — not a contradiction of
"UGC-first engine."** The same source finds AIO's UGC share is **14.2%
vs 41.4%** on the co-displayed first page (−27.25pp, p<0.001) — AIO cites
*less* user-generated content than Google's own organic ranking does.
This sits against BrightEdge's characterization of Google AI Overviews as
the most UGC-heavy of the five engines ("UGC-first engine," ~17.5-18%
UGC) — but the two use different baselines and aren't in conflict: AIO
uses more UGC than *ChatGPT/Gemini/Perplexity* (BrightEdge's cross-engine
comparison) while still using less UGC than *Google's own first-page
SERP* (this paper's within-Google comparison). Both can be true. And the
top-cited-domain data is consistent with the heavy-YouTube finding
elsewhere on this page — youtube.com is AIO's single most-cited domain
(5.49%) even as aggregate UGC is suppressed.

**Practical implication (reinforces existing guidance):** track AIO
citations and Google rankings as **separate KPIs** — don't use one as a
proxy for the other — and pursue top-5 SERP rank *and* third-party
listicle/YouTube presence as distinct pathways into the AIO.

**Two more unverified secondhand data points (2026-08-20)**: per
[[zyppy-fan-out-framework-2026]] (no links or methodology given for
either figure) — "Ahrefs: 38% of AIO citations come from Google's
top-10" and "Semrush: Perplexity showed 82% overlap with Google's
top-10." The 38% figure sits at the upper edge of
[[rankability-where-seo-is-going-2026]]'s already-logged 17-38% range
for this same metric, but is attributed here to *Ahrefs*, which
elsewhere in this wiki ([[ahrefs-b2b-seo-statistics-2025]]) is on record
with a **76%** figure for the same top-10-overlap metric — the two
can't both be Ahrefs' current number for the same thing. Rather than
treat this as a fresh Ahrefs contradiction, it's logged as an
additional unverified data point in the existing open spread (pending a
source that either confirms 38% as a real, more recent Ahrefs figure or
reveals it as a mislabeled citation of Rankability's number). The 82%
Perplexity-vs-Google-top-10 figure is new to the wiki and measures a
different pairing (a non-Google engine against Google's own SERP,
rather than AIO against Google's own SERP) — added as an unverified,
not-yet-corroborated data point rather than folded into the AIO-specific
spread above.

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

## Chinese-language generative search engines

Everything above draws on ChatGPT/Claude/Gemini/Perplexity/Google
data. Per
[[chinese-generative-search-citation-study-2026]] (614 queries, 8
platform interfaces, 160,860-citation dataset), the same broad patterns
show up in the Chinese-language ecosystem — DeepSeek, Doubao, Tencent
Yuanbao, Qwen (Tongyi Qianwen) — with some distinct findings:

- **Third-party content dominates here too**: News Media (28.8%),
  Vertical Industry Portals (24.1%), and Social/independent creators
  (16.4%) account for ~69% of citations; brand/corporate official sites
  are only 12.9%, spread across 6,589 domains (highly dispersed, not
  concentrated).
- **A classic SEO/site-quality composite score was not the leading
  predictor of AI citation absorption in any model tested** — only a
  moderate positive predictor of brand selection specifically. This
  corroborates, in a completely different market, the wiki's broader
  finding that classic ranking-factor strength doesn't reliably
  predict AI-citation behavior (see [[traditional-seo-ranking-factors]]
  and the airops authority-correlation Conflicting Evidence in
  [[ai-visibility-correlation-factors]]).
- **Silent citations are large and quantified: 39.3%** of listed
  citations never appear inline in the answer body at all — the
  clearest quantification in this wiki of "listed as a source" vs.
  "actually used" as genuinely separate outcomes, aligned with
  [[citation-selection-vs-absorption-geo-framework-2026]]'s
  selection-vs-absorption framing.
- **Brand exposure narrows sharply from citation**: only 8.3% of brands
  present in a citation pool made it into the visible answer text —
  cross-source occurrence count (how many different sources mention the
  same brand) was the strongest predictor of which brands got through.
- **Freshness decay corroborated in a new market**: citation half-life
  ~39 days for high-timeliness queries vs. ~68 days for low-timeliness
  queries — consistent in direction (though not magnitude, different
  study/market) with [[airops-fan-out-effect-2026]]'s freshness-by-
  vertical finding.
- **App and Web interfaces of the same platform return meaningfully
  different sources** — mean domain-level overlap ranged from just 0.19
  (Qwen) to 0.51 (DeepSeek); no platform had identical App/Web source
  sets. Which access surface you're measuring matters more than which
  industry vertical you're in (platform-level variance: 0.32 vs.
  industry-level variance: 0.06) — a caution for anyone building an
  AI-visibility measurement/monitoring setup.

## Citations change what the model actually says

Not just a visibility/attribution mechanism: enabling web citations can
change the substantive correctness of an answer, not just add sources to
an otherwise-fixed response. Example from the source: asked for the
worst MLB team ever, a model without citations answered with an outdated
fact (1962 Mets), while with citations enabled it correctly cited a more
recent record-holder (2024 White Sox). This reinforces
[[google-ai-optimization-guide]]'s framing of generative answers as
grounded in retrieval (RAG), not a static trained "understanding."

## Being cited ≠ being represented accurately (claim fidelity)

A dimension the wiki hadn't measured until now: even when your content is
cited, the AI may not represent it faithfully. Per
[[xu-measuring-google-ai-overviews-2026]] (WashU academic audit; 98,020
atomic claims decomposed from 7,491 Google AI Overviews, verified by a
human-validated LLM pipeline at 95.6% accuracy), **11.0% of AIO claims
are *not supported* by the pages they cite** (89.0% Consistent). The
failure is dominated by **omission (7.0%)** — the AIO drops or overstates
what the source actually says — rather than outright contradiction
(Incorrect 2.66%, Ambiguous 1.39%); omission outweighs contradiction
~2.6:1.

Three findings matter for GEO strategy:

- **Fidelity is independent of source quality** (r≈0.045). Being a
  high-authority cited source does *not* protect you from being
  misrepresented — curating better sources doesn't fix the unsupported-
  claim rate. The authors call unsupported claims "inherent to generative
  AI at its current state," with a ~5.3% residual floor even under the
  most generous assumptions (counting all uncrawled-UGC-sourced claims as
  supported).
- **Fidelity is highest in YMYL categories** — Health 94.8%, Politics
  93.7%, Science 91.8% — and lowest in Autos (80.7%), Sports (81.9%), and
  Jobs & Education (76.9%). Consistent with Google applying more
  guardrails where errors are most consequential (see
  [[e-e-a-t-and-page-quality]]'s YMYL framing).
- **Practical takeaway**: because omission is the dominant failure mode,
  content that states its key facts *self-containedly and unambiguously*
  (rather than relying on surrounding context the AIO won't carry over)
  is less likely to be truncated into an unsupported claim — the same
  extractability discipline behind [[geo-content-optimization-tactics]]'s
  chunk-level ("Fraggle") and answer-first guidance, now with an accuracy
  rationale on top of the citation-rate one. And it's a reason to
  *monitor how AI surfaces paraphrase you*, not just whether they cite you
  (see [[similarweb-how-to-win-the-race-for-gen-ai-search-2026]]'s
  sentiment-monitoring/correction guidance).

This is distinct from the "citation-without-recommendation" decoupling
(being cited but not recommended) in [[listicles-in-ai-search]] and the
citations-vs-mentions split above: here the citation *exists and points
to you*, but the sentence it supports misstates or omits what your page
said.

## AIO source selection, measured against the first page as control

Per [[arxiv-measuring-google-ai-overviews-2026]] — the only source in
this wiki that compares AIO citations against the *co-displayed
first-page results for the same query*, which turns several
widely-repeated AIO characterizations on their head. 7,583 AIOs,
61,212 cited URLs, 308,407 first-page URLs, Mar–Apr 2026.

**AIO citation is broad where the SERP is concentrated.** The top 10
hostnames take 29.7% of AIO citations but 49.6% of first-page
citations; 56.3% of AIO-cited hosts appeared exactly once across 40
days, versus 42.1% of first-page hosts — despite the first-page pool
having more than twice as many unique hosts (15,394 vs. 7,479).
"Source breadth, not concentration, is the dominant shape of AIO
citation." This sits alongside, not against, the
concentration findings above ([[ahrefs-b2b-seo-statistics-2025]]'s
"28.9% of AIO citations go to the top 50 brands"): brand-level
concentration and host-level long-tail breadth are compatible.

**AIO-cited domains are more credible than the organic results
directly beneath them** — mean PC1 domain-credibility 0.732 vs. 0.645,
significant in 14 of 19 categories with **no significant reversal in
any category**. The authors note this "directly contradicts prior work
suggesting that AIOs draw on lower-quality sources than traditional
results."

**AIOs cite less UGC than the SERP does, in every category**: 14.2% of
AIO references vs. 41.4% of first-page URLs. Four platforms are 96.5%
of the AIO UGC share — YouTube 5.49%, Facebook 3.68%, Instagram 3.65%,
Reddit 0.87%. Category spread is 3x: Climate 9.3% and Health 10.7% at
the low end, Beauty & Fashion 28.9% and Autos & Vehicles 27.4% at the
high end.

This **nuances** [[brightedge-ai-search-same-brands-different-sources]]'s
"Google AI Overviews is a UGC-first engine" framing above. Both can be
true — AIO is UGC-heavy *relative to other AI engines* and UGC-light
*relative to Google's own organic results* — but the magnitudes differ
between the two sources (14.2% vs. ~17.5–18% UGC; YouTube 5.49% vs.
10.6%), plausibly a query-mix difference (trending/news-heavy corpus
vs. brand-tracking corpus). Treat "UGC-first" as a between-engine
statement only.

**Roughly 30% of AIO citations come from outside the first page —
and they're the better ones.** Averaged per AIO, AIO reference domains
overlap 25.0% with the top 5, 41.4% with the top 10, and 70.2% with
the full first page; **29.8% of AIO-cited domains appear nowhere on
the corresponding first page** (28.5% at URL level). Those off-page
citations score *higher* on credibility (PC1 0.758 vs. 0.724) and
carry far less UGC (3.4% vs. 18.5%) than the AIO citations that do
also rank.

Practical implication: AIO citation and first-page ranking are
different selection mechanisms operating on the same index, not one
mechanism re-ranked. Ranking on page 1 remains the highest-probability
path into an AIO, but roughly three in ten cited domains get there
without it — so "we don't rank for this query" is not a reason to
exclude a page from AIO-citation monitoring. As the authors put it,
"publishers whose content informs an AIO are not necessarily the same
publishers whose pages users would encounter by scrolling past it."

## Conflicting Evidence

- **Claim**: whether AI engines (Perplexity specifically) cite LinkedIn
  *Company Pages* or *individual creators* more.
  - Supported by (individuals dominate): [[otterly-linkedin-ai-citations-study-2026]]
    (384K URLs, 6 engines, Jan–Jun 2026) — named individuals draw
    **91.7%** of LinkedIn citations vs. 8.3% for company/unattributed,
    aggregate across engines.
  - Contradicted by (for Perplexity): [[semrush-linkedin-ai-visibility-study-2026]]
    (89K URLs, 3 engines, Jan–Feb 2026) — **Perplexity cites 59% Company
    Pages**, while ChatGPT (59% individual) and Google AI Mode (59%
    individual) agree with Otterly. Because Otterly also found Perplexity
    drives the largest single share of LinkedIn citations (43.3%), a
    strong Perplexity company-tilt is hard to reconcile with a
    91.7%-individual aggregate.
  - **Current best guess**: individual/named-author content dominates on
    ChatGPT and Google AI Mode (both studies agree). Perplexity's
    company-vs-individual split is genuinely unresolved — most likely a
    **definitional difference** (Semrush "Company Pages" vs. Otterly's
    "company/unattributed" bucket; a Company-Page-published post vs. an
    individual's Pulse article are classified differently) compounded by
    different engine sets (3 vs. 6) and time windows (Jan–Feb vs.
    Jan–Jun). Flagged as unresolved; doesn't change the wiki's
    named-author tactic, which both studies support in aggregate. Otterly
    is larger/more recent/more engines, so its aggregate individual-dominance
    finding carries more weight where the two disagree.

- **Claim**: how much AI Overview citation depends on ranking in
  Google's own top 10.
  - Supported by: [[ahrefs-b2b-seo-statistics-2025]] — "76% of AI
    Overview citations pull from Google's own top-10 organic results"
    (see "AI Overview citation composition" above), the basis for this
    wiki's "ranking well is close to a prerequisite for AI citation"
    framing.
  - Contradicted by: [[arxiv-measuring-google-ai-overviews-2026]]
    (2026-05-13) — measured per-AIO domain overlap of **41.4% at
    top-10** and 70.2% across the *entire* first page, with 29.8% of
    cited domains appearing nowhere on the first page at all. Even the
    full-first-page figure (70.2%) sits below the claimed top-10
    figure (76%).
  - **Current best guess**: partly a unit-of-analysis difference,
    partly a real gap. The arXiv study measures *domains* averaged
    per-AIO on a trending-query corpus; the Ahrefs stat is a
    citation-weighted share on a B2B corpus. Citation-weighting would
    push the arXiv number up (frequently-cited hosts also tend to
    rank), and a B2B/commercial query mix likely has tighter
    AIO-to-SERP coupling than trending news and sports do. But the
    arXiv figure is the better-specified measurement — it publishes
    its overlap definition, sample sizes and control pool, where the
    Ahrefs figure is a headline statistic. Leaning toward: **top-10
    ranking is a strong but far-from-sufficient predictor of AIO
    citation, and the "~76% comes from the top 10" figure is an
    upper bound that does not generalize across query mixes.** Flagged
    as **unresolved** — neither source replicates the other's corpus.

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

- **Claim**: do third-party review platforms (G2, Capterra) or a vendor's
  own self-description drive AI *recommendations*?
  - Supported by (third-party matters): the review-platform-presence
    tactic in [[geo-content-optimization-tactics]]; [[peec-ai-chatgpt-query-fanouts-2026]]
    (ChatGPT injects "reviews" and actively searches review content);
    [[victorious-q2-2026-quarterly-search-report]] (99.99% of
    category-research *citations* went to third-party domains; mentions
    correlate with referring-domains 0.49 / third-party-mentions 0.45);
    and [[derivatex-two-googles-one-query-aio-vs-serp-2026]] (review
    sites 5.0% of AIO citations — low but nonzero).
  - Contradicted by: [[derivatex-4cs-explainable-to-ai-2026]]'s
    "Authority Inversion" study (233 ChatGPT recommendations, 40
    categories) — 84% of citations came from vendor self-descriptions or
    niche sites, and **G2 and Capterra were cited zero times**;
    contradictory descriptions were "actively harmful" because models
    built answers from single clear pages.
  - **Current best guess**: likely a *recommendations-vs-citations* and
    *engine/sample* difference rather than a true contradiction. The
    DerivateX finding is ChatGPT-specific, small (n=233), measures which
    source the *recommendation text* was built from (favoring one
    legible page), and buckets "vendor self-description **or** niche
    sites" together — whereas the third-party-authority evidence is about
    what earns *mentions/citations* across engines at scale. The two are
    compatible if a vendor's own legible page drives the recommendation
    *wording* while third-party footprint drives whether the brand is
    *surfaced/mentioned* at all. Flagged **unresolved**; practical
    takeaway until resolved — do both: keep third-party/review-platform
    presence (mention-side) *and* make your own primary pages maximally
    legible per [[explainable-to-ai-4cs]] (recommendation-wording side).
    Don't drop review-platform work on the strength of one small
    ChatGPT-only study.

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
- [[chinese-generative-search-citation-study-2026]] — the
  Chinese-language generative-search citation data above, including
  the silent-citation, brand-exposure, and cross-interface findings.
- [[citation-selection-vs-absorption-geo-framework-2026]] — the
  selection-vs-absorption measurement framework and per-platform
  citation-breadth-vs-depth divergence above.
- [[goliath-david-generative-search-perplexity-2025]] — the
  perplexity/semantic-homogeneity citation mechanism and positional-
  bias/content-polishing findings above.
- [[ai-mediated-commercial-persuasion]] — a distinct, harder-to-audit
  visibility risk: sponsored placement in AI chat can actively
  disparage non-sponsored alternatives via hedging language, not just
  omit them, and users rarely detect it even with disclosure labels.
- [[llm-as-judge-behavioral-grounding]] — a mechanism study suggesting
  citation/ranking behavior in AI systems isn't purely a function of
  semantic relevance to the query as written — behavioral/engagement
  signals from similar prior queries plausibly factor in too.
- [[ai-overview-grounding-and-fidelity]] — the companion half of
  [[arxiv-measuring-google-ai-overviews-2026]]: once a source is cited,
  whether the AIO's claims are actually supported by it (~11% are not).
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
- [[otterly-youtube-ai-citation-study-2026]] — the YouTube-by-provider
  data update and video-structure findings above, plus the flagged
  Gemini-figure discrepancy.
- [[otterly-reddit-geo-ai-search-citations-2026]] — the Reddit-community-
  engagement findings above (9x citation multiplier from active
  engagement, comments > upvotes, community size not predictive).
- [[otterly-claude-ai-citation-study-2026]] — the Claude-specific citation
  mix above (64% brand-content dominance, 0.9% social media, Reddit 0%).
- [[geosurge-model-memory-predicts-search-2026]] — the training-memory-
  drives-live-search finding above (3.2× search-rate gap), linking the
  training-data and live-retrieval pathways rather than treating them as
  independent.
- [[xu-measuring-google-ai-overviews-2026]] — the WashU academic audit
  behind the 29.8%-off-page AIO↔SERP-divergence corroboration, the
  AIO-vs-SERP UGC-suppression finding, and the claim-fidelity section
  above (11% of AIO claims unsupported, omission-dominant).
- [[lilyray-chatgpt-fanout-queries-2026]] — the ChatGPT fan-out
  escalation and `site:` operator targeting addendum above (fan-out
  volume jump, retrieval-vs-citation divergence, the quantified
  decides-before-it-searches citation rate, and the domain-confusion/
  phishing risk).
- [[zyppy-fan-out-framework-2026]] — the two unverified secondhand
  AIO/SERP-overlap data points above (Ahrefs 38%, Semrush Perplexity
  82%) and the unreconciled AirOps 43.2%-vs-58.4% retrieval-rank
  discrepancy; the fan-out discovery-and-optimization workflow itself
  lives in [[geo-content-optimization-tactics]].
- [[commoncrawl-web-graph-ai-ranking-signals-2026]] — the Google-
  position-vs-citation-probability data point above (46-48%/37%/
  19-20% at positions 1/2/10), plus the Common Crawl training-data-
  provenance figures in [[how-google-search-works]] and the Harmonic
  Centrality/PageRank domain-benchmarking tactic in
  [[geo-content-optimization-tactics]].
