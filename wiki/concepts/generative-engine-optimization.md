---
type: concept
tags: [seo, aeo]
updated: 2026-08-20
---

# Generative Engine Optimization (GEO / AEO)

**Generative Engines (GEs)** are systems — BingChat, Google's SGE,
Perplexity.ai, and by extension ChatGPT/Claude-style answer engines —
that satisfy a query by retrieving sources and generating a single
synthesized, cited answer, rather than returning a ranked list of links.
**Generative Engine Optimization (GEO)** is the practice of optimizing
content to increase its visibility (how much it's used and cited) inside
those generated answers.

This wiki treats **GEO and AEO as the same underlying idea** — GEO is the
term coined by the founding academic paper on the topic
([[geo-generative-engine-optimization-aggarwal-2023|source]]); AEO
("Answer Engine Optimization") is the term that stuck in industry usage.
Pages in this wiki may use either term depending on the source being
cited.

## GEO (LLM chat optimization) vs. AI Overview optimization — distinct disciplines

Per [[wix-generative-engine-optimization]] — this wiki's tactics have so
far mostly concerned Google's AI Overviews and citation behavior inside
generative engines generally, but **optimizing for LLM chat products
(ChatGPT, Gemini, Perplexity, Claude) is a genuinely separate discipline
from optimizing for Google AI Overviews**, with a different user
journey:

| | LLMs for search | AI Overviews in Google Search |
|---|---|---|
| Entry | Users choose to use the LLM | Users happen upon it (doesn't trigger for every query) |
| Interaction | Users interact, ask follow-ups, go deeper | Users passively receive the generated content |
| Control | Users control which LLM/content they engage with | Generated according to system needs, no opt-in |

Treat "get cited in an LLM chat answer" and "get cited in a Google AI
Overview" as separate targets requiring separate tactics, not one
generic "AI search visibility" goal.

### A finer LLM taxonomy (three categories, not just training/indexing/retrieval bots)

Beyond the training/indexing/retrieval crawler taxonomy in
[[how-google-search-works]], LLM *products* themselves split into three
categories relevant to optimization strategy:

1. **Static pre-trained-data LLMs** (Claude 3-3.5, GPT-3, Gemini 1.5,
   NotebookLM, the Copilot app) — answers come from a fixed training
   set; links are often absent. Optimize for **brand mentions, not
   links** — track via bulk brand/entity queries rather than expecting
   referral traffic. Visibility only changes when the training set is
   updated (a model-specific "knowledge cutoff" date gates eligibility
   entirely). User feedback (thumbs up/down on responses) can correct
   brand inaccuracies even between training updates.
2. **Search-augmented LLMs** (Perplexity, Copilot, GPT-4) — a fixed
   training set augmented by live search-engine data; links/citations
   appear and update via web crawling. Optimization here resembles
   optimizing for the *underlying* search engine (e.g. Copilot
   visibility follows Bing rankings, not Google's) — check core queries
   regularly, since visibility fluctuates like search rank. Per
   [[semrush-chatgpt-search]] — **ChatGPT Search itself retrieves from
   three sources**: OpenAI's own crawled index (via `OAI-SearchBot`),
   **Bing's search index via a Microsoft partnership** (pages crawled
   by Bingbot), and direct data partnerships with news/data providers.
   The Bing dependency means ChatGPT visibility may partially follow
   Bing ranking signals too, not just OpenAI's own crawl/index — the
   same mechanism already noted for Copilot above, now extended to
   ChatGPT Search specifically. Per [[vercel-adapting-seo-for-llms]],
   **Meta AI is reportedly also Bing-dependent** — a third product on
   the same underlying index, while Google and Perplexity are described
   as using a proprietary index and mixed sources respectively.
3. **Reasoning models with search** (DeepSeek R1-R2, Gemini 2.5, OpenAI
   o1-o4) — "mixture of experts" niche-task networks that also crawl
   and cite live web content.

## Retrievability: a fourth pipeline stage beyond crawl/index/rank

Per [[sel-integrate-geo-with-seo]] (quoting Crystal Carter, Wix) — a
named extension of the classic SEO pipeline: traditional SEO stops at
**crawlability → indexability → rankability**; AI-driven search adds a
fourth stage, **retrievability** — "how effectively AI can access,
interpret, and prioritize information about your brand when forming
responses." Rankings alone don't guarantee AI visibility, since LLMs
build responses from contextual entity patterns rather than looking up a
ranked index.

This is a different framing of the same underlying pipeline as
[[how-google-search-works]] (crawl → index → serve), not a competing
technical claim — retrievability sits conceptually where this wiki's
existing "retrieval rank as the primary citation gatekeeper" finding
([[ai-citation-landscape]], from [[airops-fan-out-effect-2026]]) already
lives, now with a named fourth-stage label to slot alongside the classic
three.

The source also proposes a **Presence / Recognition / Accessibility**
three-pillar breakdown of retrievability (consistent brand mentions in
AI training/retrieval sources; credibility via trusted-entity
associations; on-site/web structuring for AI retrieval).
**Naming-collision note**: "Presence" here is a different concept than
[[sej-the-consensus-gap]]'s Presence/Portability/Concentration
measurement framework (that Presence = % of prompts where a brand
appears in *any* engine) — both terms are legitimate and both stay in
the wiki, but don't conflate them when cross-referencing.

**Technical grounding — what "retrievability" actually is at the
architecture level**: per [[xiong-et-al-search-engines-meet-llms-2024]]
(academic survey), the mechanism behind AI Overviews/AI Mode/LLM-chat
citation is **Retrieval-Augmented Generation (RAG)** — search results
are injected into the model's context window at inference time,
addressing hallucination by grounding the response in current,
retrieved content rather than relying only on frozen training data.
"Retrievability" is, mechanically, whether your content makes it into
that retrieved context set — which is exactly why traditional ranking
signals matter but aren't sufficient alone (per the existing
retrieval-rank-as-citation-gatekeeper finding in
[[ai-citation-landscape]]): a page has to be both rankable *and*
selected into the RAG context to be cited.

## Three-layer AI search model (retrieval-speed taxonomy)

Per [[superlines-geo-guide]] (vendor content, undisclosed methodology —
treat directionally) — a different lens than the LLM-*product*
taxonomy above: this one classifies **retrieval speed tiers**, which the
same LLM product can move across depending on mode:

1. **Training data (slowest)** — relies on pre-training/periodic
   fine-tuning; takes months to reach base-model inclusion. Optimize by
   building durable authority and keeping facts consistent across owned
   and third-party sources — there's no way to accelerate this tier
   directly.
2. **High-volume AI search (speed depends on SEO)** — uses existing
   search indexes (Google, Bing); powers free ChatGPT, AI Overviews.
   Visibility speed here tracks classic SEO strength directly — the
   same "ranking well is close to a prerequisite for AI citation"
   pattern already established elsewhere in this wiki
   (see [[ai-citation-landscape]]).
3. **Agentic AI (fastest, near-real-time)** — Perplexity Pro, ChatGPT's
   research/agent modes, Claude Desktop with MCP connections; scrapes
   pages close to real time. Optimize with agent-friendly pages (clean
   HTML/schema) and monitor bot traffic directly, since indexing lag
   isn't the bottleneck here the way it is in tier 1-2.
## Two distinct influence mechanisms: training-data co-occurrence vs. retrieval-stage citation

Per [[malte-landwehr-llmo-geo-aio-guide]] — an early (Jan 2024) framing
worth distinguishing from the citation-visibility mechanics above:

- **Co-occurrence / training-data influence**: strategically pairing a
  brand with target keywords/topics on authoritative sites so that a
  model's *training data* links them together, shaping brand
  associations in static pre-trained models even with no retrieval
  step involved. Illustrated by the "Tesla whistle" example — enough
  media co-occurrence of "Tesla" and "whistle" from a PR stunt caused
  ChatGPT's autocomplete to associate the two terms. This targets the
  same **static pre-trained-data LLM** category described above
  (optimize for brand mentions, not links; changes only when the
  training set updates).
- **Citation-stage visibility** (the GEO paper's mechanism, and most of
  this page): given a source is already retrieved by a RAG system, how
  much does the generated answer actually cite/use it. Applies to the
  **search-augmented** and **reasoning-with-search** categories above.

Target authoritative sites for co-occurrence building: heavily-
moderated community sites (Wikipedia, Reddit, Quora), database
platforms (Crunchbase, Yelp, IMDB), major editorial outlets (NYT,
Bloomberg, Reuters, Forbes), and Google's Knowledge Graph source list
(~63k sites) — overlaps heavily with [[brand-entity-seo-strategy]]'s
own Knowledge-Graph-data-source list, reinforcing that brand-entity
work and GEO co-occurrence work are largely the same underlying effort
viewed from two angles.

## Why traditional SEO doesn't transfer

Traditional search engines rank by keyword matching plus authority
signals (backlinks, domain age). Generative engines instead have an LLM
read the actual retrieved content and decide what to cite and how much
to quote — so tactics built for keyword-matching rank algorithms largely
don't work:

- **Keyword Stuffing** and **Unique Words** (classic on-page SEO moves)
  showed ~0% or even negative improvement in citation visibility, and
  Keyword Stuffing measured **10% worse than baseline** when validated
  live on Perplexity.ai.
- What *does* work is qualitatively different: making content more
  citable, quotable, and evidence-backed — see
  [[geo-content-optimization-tactics]] for the ranked tactics.

**Major caveat added 2026-07-22, see Conflicting Evidence below**: per
[[c-seo-bench-2025]], a large-scale, multi-domain, multi-model re-test
of these exact tactics using a *citation-rank* outcome metric (rather
than word count) found most of them have no significant effect, and
some are actively harmful — while a document's *position in the
retrieval/context pipeline* (i.e., traditional SEO) produces far
larger gains than any content tactic tested. This section's title claim
("traditional SEO doesn't transfer") is directly challenged by that
finding, at least for the citation-rank outcome specifically.

## Visibility is measured differently than SEO ranking

Because a generated answer embeds multiple citations at different
lengths and positions in one block (rather than a linear list),
"visibility" needs its own metrics:

- **Word count** of the sentences attributed to a source.
- **Position-adjusted word count** — same, but weighted down for
  citations that appear later in the answer (earlier = more likely to be
  read).
- **Subjective Impression** — a 7-facet LLM-judged score: relevance,
  influence (how much the answer actually relies on this citation),
  uniqueness of the material, perceived prominence of position, perceived
  amount of content used, likelihood the user clicks through, and
  diversity of material presented.

  **Caveat on LLM-judged metrics generally**: per
  [[vardasbi-et-al-as-it-was-llm-search-evaluation-2026]] (a Spotify
  music-search paper, adjacent domain not web-AEO directly), "plain"
  LLM judges using semantic reasoning alone measurably diverge from
  real user preference, especially on ambiguous/long-tail queries —
  grounding the judge in actual behavioral interaction data closed
  part of that gap but didn't eliminate it. Treat Subjective Impression
  (or any purely-LLM-judged visibility score) as directional, not
  ground truth, absent a similar behavioral-grounding step.

## GEO disproportionately helps lower-ranked content

A striking finding: content that ranks poorly in traditional search can
gain the most from GEO. In one experiment, a site ranked **#5** in Google
search results gained **+115%** visibility in the generated answer after
adding citations, while the **#1**-ranked site's visibility for the same
treatment *dropped 30%*. Because the generative engine reads content
directly rather than relying on backlink/domain-authority signals, small
or under-ranked creators have a more level playing field inside AI
answers than they do in classic SERPs. Anecdotal, practitioner-level
corroboration: per [[semrush-chatgpt-search]], a marketing consultant
observed that "ChatGPT Search may rank smaller websites more fairly
than Google" — consistent in direction with the measured finding above,
though this specific observation isn't itself a study.

## Effectiveness is domain-specific

No single tactic wins everywhere — see
[[geo-content-optimization-tactics]] for which tactics work best in which
domains, and why combining tactics outperforms using any one alone.

## Appearing & measuring performance in Google's AI features

Per [[google-ai-features-appearance-guide]], Google states there are "no
additional requirements to appear in AI Overviews or AI Mode" beyond
standard indexing/snippet eligibility — reinforcing
[[google-ai-optimization-guide]]. Both AI Overviews and AI Mode may use
"query fan-out" (issuing multiple related sub-queries) to build a
response. AI-feature traffic is measurable: it shows up in Search
Console's Performance report under the "Web" search type, and Google
states AI-Overview clicks show higher-quality engagement — a claim
Google has made consistently since at least May 2025, per
[[google-succeeding-in-ai-search-2025-05]], not a new or revised
position. Site owners who want to *limit* rather than maximize
inclusion have explicit controls — see [[controlling-ai-feature-inclusion]].

**Update per [[google-generative-ai-performance-report]]**: Google
Search Console now also offers a **dedicated "Generative AI Performance
Report"** (separate from filtering the general Performance report by
"Web" search type) purpose-built for AI Overviews/AI Mode impressions,
sliceable by page, country, date, and device. Rollout is gradual and
gated on sites having sufficient AI-feature impressions.

## Conflicting Evidence

- **Claim**: Traditional SEO is largely obsolete for generative engines,
  and content should be optimized specifically for AI citation/visibility
  using distinct tactics (quotes, stats, citations).
  - Supported by: [[geo-generative-engine-optimization-aggarwal-2023]]
    (2023-11), which found classic SEO tactics like keyword stuffing
    don't transfer and citation-style content tactics do.
  - Contradicted by: [[google-ai-optimization-guide]] (2026-06), Google's
    official guidance, which states SEO fundamentals remain "the
    foundation" for AI Overviews/AI Mode and explicitly advises against
    building special AI-only infrastructure (`llms.txt`, chunking,
    AI-specific rewriting). **Corroborating practitioner voice
    (2026-08-20)**: [[zyppy-seo-strategies-for-ai-search-2026]] argues
    "good SEO is good GEO" and that most businesses can reach 90%+ of
    AI-visibility goals via adapted SEO fundamentals plus targeted
    AI-specific tweaks (fan-out targeting, third-party consensus) rather
    than a separate GEO strategy — an unmeasured, asserted figure, not
    an independent study, but a second voice on the "foundation" side.
- **Current best guess**: these findings describe **different stages of
  the same funnel**, not a true contradiction:
  - **Retrieval eligibility** (will your content even be considered as a
    candidate source?) — governed by classic SEO fundamentals:
    [[how-google-search-works]] (technical crawling/indexing/serving),
    avoiding thin/manipulative content, and [[e-e-a-t-and-page-quality]]
    (Experience, Expertise, Authoritativeness, Trust). This is what
    Google's guidance addresses, and it doesn't test or claim anything
    about citation-style content within an already-retrieved set.
  - **Citation-stage visibility** (given you're one of the sources fed to
    the model, how much does the generated answer actually use/cite
    you?) — this is what the GEO paper measures, and it's silent on
    retrieval eligibility.
  - Google's specific claims (no need for `llms.txt`, no need to chunk
    content, don't rewrite "for AI") are about **infrastructure/format**,
    not about whether citation-friendly content style (quotes, stats,
    sourcing) matters — and those tactics arguably overlap with Google's
    own "helpful, reliable, people-first" framing rather than opposing it.
  - Flagged as unresolved: whether Google's own AI Overviews specifically
    respond to the GEO paper's citation-style tactics the same way the
    third-party generative engines tested in that paper (GPT-3.5-based,
    Perplexity.ai) did is untested as of this wiki's current sources.

## Conflicting Evidence — do the Tier 1-3 content tactics actually move citation outcomes?

- **Claim**: Content-level tactics (Quotation Addition, Statistics
  Addition, Cite Sources, Fluency Optimization, etc.) meaningfully
  improve a document's visibility/citation in generative-engine
  answers, and traditional SEO tactics largely don't transfer to this
  new surface (per the "Why traditional SEO doesn't transfer" section
  above).
  - Supported by: [[geo-generative-engine-optimization-aggarwal-2023]]
    (2023-11), the wiki's founding GEO source, measuring a **word
    count** outcome (how many words the generative engine spends
    discussing a document) across 1k queries, 1 domain, single-actor
    adoption.
  - Contradicted by: [[c-seo-bench-2025]] (NeurIPS 2025), which
    re-tests the *same* eight tactics plus two new ones across 6
    domains, 4 LLMs (GPT-4o-mini, Claude 3.5 Haiku, o3, o4-mini), and
    multi-actor competitive adoption, using **citation rank** (does the
    document get cited earlier?) as the outcome. Result: only 3 of 54
    method×domain significance tests were positive and significant: LLM
    Guidance and Content Improvement, each only in 1-2 domains (Retail;
    Retail+Video Games) on GPT-4o-mini specifically. Many tactics
    (especially Statistics) were *significantly negative* in a majority
    of tested settings, and **no tactic was significant at all for Claude
    3.5 Haiku or for the question-answering task**. Meanwhile, moving a
    document to position 1 in the LLM's context window (i.e.,
    traditional retrieval-ranking/SEO) produced gains several times
    larger than the best content tactic in every domain tested.
- **Current best guess**: not a clean contradiction, but a genuine
  **downweighting of confidence** in the original Tier 1-3 rankings,
  for a specific reason the newer paper makes explicit: word count and
  citation rank are different outcomes, and a document can be discussed
  at length without being cited earlier — the more decision-relevant
  outcome for actual GEO/AEO purposes (per this wiki's own framing of
  the goal as "getting cited/mentioned") is citation rank, not word
  count. The newer paper also notes that Aggarwal et al.'s own
  *secondary* metric (position-adjusted word count) already showed a
  general decrease under these tactics — so a careful re-read of the
  original paper's own data doesn't actually establish a strong,
  clean-cut win for these tactics either. **Not fully resolved**: the
  two papers used different generative-engine setups (GPT-3.5/
  Perplexity.ai vs. GPT-4o-mini/Claude 3.5 Haiku/o3/o4-mini) and
  different domains, so some of the gap could still be model/domain
  drift rather than purely a metric-choice artifact. Until further
  replication, **treat the Tier 1-3 rankings in
  [[geo-content-optimization-tactics]] as directional/exploratory
  rather than validated for the citation-rank outcome**, and treat
  retrieval-rank/traditional-SEO improvements as the better-evidenced
  lever for that outcome specifically — independently consistent with
  [[airops-fan-out-effect-2026]]'s retrieval-rank-as-gatekeeper finding
  elsewhere in this wiki.
- **Mechanistic support added 2026-08-17**: [[peec-ai-rerankers-geo-aeo-2026]]
  (published 2026-08-06) supplies a plausible *why* for C-SEO Bench's
  otherwise puzzling null/negative results, without itself being a
  competing empirical test. Per [[ai-search-reranking-pipeline]], the
  stage that decides what gets cited is a **neural reranker** scoring
  query-passage pairs for **answer-shape alignment** — does this passage
  look like a direct answer to this question, at this granularity? On
  that account, injecting quotes/statistics/citations into a page doesn't
  change its answer shape, which is exactly the class of tactic C-SEO
  Bench found ineffective; whereas retrieval/context position (the lever
  that *did* dominate in C-SEO Bench, and in
  [[airops-fan-out-effect-2026]]) determines whether a passage reaches
  the reranker at all. This also predicts which content work *should*
  still pay off — restructuring so the answer is self-contained at the
  passage level and shaped to the query's intent, rather than decorating
  the page — which is how [[geo-content-optimization-tactics]] now frames
  its Fraggle/answer-shape guidance. **Caveat**: this is a
  mechanism-level vendor explainer, not an experiment, and the production
  rerankers in ChatGPT/Perplexity/AI Mode are undisclosed — so it
  raises confidence in the "current best guess" above without resolving
  the conflict empirically.
- **New finding, not previously in this wiki**: [[c-seo-bench-2025]]
  also shows the best-performing C-SEO tactics behave as a **congested,
  zero-sum game** — gains shrink steadily as more competing documents
  adopt the same tactic, converging toward zero near full adoption.
  Prior white-hat GEO research (including Aggarwal et al. 2024) only
  tested single-actor/unilateral adoption, so this competitive dynamic
  was previously unquantified for white-hat tactics in this wiki.

## See also

- [[ai-citation-landscape]] — empirical data on what ChatGPT, Claude, and
  Gemini actually cite in practice (media mix, provider differences,
  Wikipedia/Reddit/Axios patterns). Complements the tactics above with
  real-world citation composition data, and partially answers the "does
  this hold for newer/other generative engines" open question below —
  though it studies citation *composition*, not the effect of applying
  GEO *tactics* on ChatGPT/Claude/Gemini specifically.
- [[aio-ctr-impact]] — the economic payoff of citation: being cited in a
  Google AI Overview delivers +120% more clicks than not being cited
  (though still below a no-AIO baseline). This is the real-world traffic
  rationale for why the citation-focused tactics above are worth doing.
- [[e-e-a-t-and-page-quality]] — the retrieval-eligibility foundation
  referenced in Conflicting Evidence above: the actual official framework
  behind "classic SEO fundamentals"/"helpful, people-first content."
- [[ai-search-reranking-pipeline]] — the mechanism layer under the Tier
  1-3 conflict above: the fanout → hybrid retrieval → **reranking** →
  generation pipeline, and why answer-shape alignment (not page-level
  decoration) is what the citation-deciding stage actually scores.
- [[how-google-search-works]] — the technical crawl/index/serve pipeline
  underneath "technical crawlability": if a page isn't crawled, indexed,
  or served in the first place, it can never become a candidate source
  for any generative engine either.
- [[search-intent-and-needs-met]] — Google's query-intent taxonomy;
  "Know Simple" queries are directly relevant to structuring
  answer-friendly content.
- [[ai-coding-agent-tool-selection]] — a sibling GEO/AEO domain: the
  same "visibility inside an AI-generated answer" mechanic, but for
  coding agents choosing which *tool/library* to recommend rather than
  chat/search engines choosing which *content* to cite.
- [[agentic-web-optimization]] — a third sibling domain: optimizing a
  site so general-purpose AI agents can *act* on it (browse, fill
  forms, complete purchases), a higher bar than being cited.
- [[wix-generative-engine-optimization]] — the source for the GEO-vs-
  AI-Overview distinction and LLM taxonomy above; also has practical
  tactics in [[geo-content-optimization-tactics]]'s LLM-chat-specific
  section.
- [[malte-landwehr-llmo-geo-aio-guide]] — the co-occurrence/training-
  data-influence mechanism above, and the authoritative-source target
  list for building it.
- [[ai-traffic-scale-vs-hype]] — a scale check on this whole domain: as
  of early-2026 clickstream data, standalone AI tools remain a tiny
  fraction of overall search/social traffic, so the tactics in this
  page matter most where they overlap with Google's own AI features
  (which inherit Google's dominant search share) rather than in
  isolation.
- [[sel-what-is-generative-engine-optimization-geo-2026]] — a general
  GEO explainer that corroborates the definitions and tactics above;
  its few new data points (citation-source volatility, absolute AI-tool
  user counts) are filed on [[ai-citation-landscape]] and
  [[ai-traffic-scale-vs-hype]] instead of here.
- [[sel-integrate-geo-with-seo]] — the source for the retrievability
  fourth-pipeline-stage framing and Presence/Recognition/Accessibility
  breakdown above; also has GA4-regex and citation-monitoring-automation
  tactics filed on [[geo-content-optimization-tactics]].
- [[superlines-geo-guide]] — the source for the three-layer retrieval-
  speed taxonomy above; also has a GEO KPI matrix filed on
  [[geo-content-optimization-tactics]] and a citation-concentration
  claim filed on [[ai-citation-landscape]].
- [[c-seo-bench-2025]] — the NeurIPS 2025 re-test that significantly
  downweights confidence in the Tier 1-3 tactics above and shows
  retrieval-rank/traditional-SEO dominates content tactics for the
  citation-rank outcome; see the Conflicting Evidence section above.

## Open questions

- **Partially answered (2026-07-22)**: the GEO paper's tactics were
  originally tested on GPT-3.5-based generative engines and
  Perplexity.ai only; whether they hold up on other models was
  previously an open question. [[c-seo-bench-2025]] now tests the same
  tactics on GPT-4o-mini, Claude 3.5 Haiku, o3, and o4-mini across 6
  domains — and finds most don't hold up when measured by citation rank
  rather than word count (see Conflicting Evidence above). This
  substantially answers the "does this generalize across models"
  question, though with a metric change alongside the model change, so
  it isn't a perfectly isolated test of model-generalization alone.
- Whether Google's "don't rewrite specifically for AI" advice is in
  tension with citation-style optimization tactics, or whether those
  tactics are simply a subset of "helpful, people-first" writing, is
  unresolved — see Conflicting Evidence above.
