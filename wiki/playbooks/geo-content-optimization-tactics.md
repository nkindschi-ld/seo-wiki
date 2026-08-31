---
type: playbook
tags: [seo, aeo]
updated: 2026-08-03
---


# GEO Content Optimization Tactics

**Why/when to use this:** Apply these when writing or revising content
you want cited/quoted by generative engines (AI Overviews, Perplexity,
ChatGPT search, etc.), as opposed to classic keyword-ranking SEO. See
[[generative-engine-optimization]] for the underlying concept. For
classic organic-SERP ranking tactics specifically, see
[[classic-seo-ranking-factors]] instead — the two overlap in places but
are grounded in different correlation studies.

Ranked by measured visibility improvement
([[geo-generative-engine-optimization-aggarwal-2023|source]]), from best
to worst, tested against a no-optimization baseline:

**Major caveat added 2026-07-22 — read before applying this tier
list.** Per [[c-seo-bench-2025]] (NeurIPS 2025), a larger, multi-domain,
multi-model re-test of these exact tactics using a *citation-rank*
outcome (does the document get cited earlier?) instead of the original
*word-count* outcome found most of these tactics have **no significant
effect on citation rank, and some are actively harmful** — while
improving a document's *retrieval/context position* (traditional SEO)
produces far larger gains than any tactic below. See "C-SEO Bench: a
large-scale re-test" further down this page for the full findings, and
[[generative-engine-optimization]]'s Conflicting Evidence section for
the reconciliation. **Practical implication: treat the tier rankings
below as directional/exploratory rather than validated for actually
winning an earlier citation, and prioritize retrieval-rank/technical-
crawlability work (see this page's Technical crawlability checklist)
over these content tactics when the two compete for effort.**

## Tier 1 — High performing (do these)

1. **Quotation Addition** — add credible, quotable quotes from relevant
   sources. Best overall performer: up to +40% on the benchmark, +22%
   validated live on Perplexity.ai.
2. **Statistics Addition** — include quantitative statistics instead of
   qualitative/vague claims wherever possible. +37% validated live on
   Perplexity.ai (Subjective Impression metric).
3. **Cite Sources** — add citations to credible sources for factual
   claims. Especially effective for lower-ranked content (see
   [[generative-engine-optimization]]'s equity finding — up to +115% for
   a rank-5 site).
4. **Fluency Optimization** — improve the fluency/flow of the writing
   itself, no new content required. +15–30%.
5. **Easy-to-Understand** — simplify language/reduce jargon. +15–30%.

**Best combination tested:** Fluency Optimization + Statistics Addition
together outperformed any single tactic by 5.5%+. If you can only pick
one pairing, use this one.

## Pick winnable topics, then defend the 5-point moat

Per [[semrush-chatgpt-topic-authority-study]] (1,094 ChatGPT categories,
Jan–Jun 2026) — a portfolio-level prioritization layer above the
page-level tactics here, and the strategic complement to "Focus over
comprehensiveness" above:

- **Most topics are unowned — treat it as a land grab.** Only 15.2% of
  categories had a clear owner; 53.7% were unsettled. There is room to
  own a topic outright in most categories.
- **Prefer winnable lower-demand subtopics over contested head terms.**
  The study found an inverse-demand paradox: only 11.3% of high-demand
  topics had a clear owner vs. 19% of lower-demand ones. High-volume
  topics fragment mention share across many brands; niches are easier to
  own. (Same direction as the fan-out "focus beats comprehensiveness"
  finding above.)
- **Concentrate on 2–3 categories where you already have signal**, not a
  broad spread — pushing one topic past the ownership threshold beats
  thin presence across many.
- **Aim for a ≥5-percentage-point mention-share margin.** Once a brand
  becomes a clear owner it holds #1 in 90.4% of month-over-month checks;
  held leads had a median 2.9-point margin, flipped leads only 1.3
  points. Reaching the moat first is a compounding, defensible asset.
- **Optimize for mention share, not just citation share.** They are
  near-decoupled (only 21% of most-cited domains are also the
  most-mentioned brand; correlation -0.229), and mention share is what
  tracks to selection (74% of users pick the top-mentioned brand). See
  [[topical-authority-in-ai-search]] and [[ai-shortlist-effect]].

## Claim frontier concepts before competitors do

Per [[vercel-adapting-seo-for-llms]] (no disclosed evidence for the
underlying mechanism, but a reasonable extension of this wiki's existing
topical-authority guidance): "LLMs favor the first or clearest
explanation of a concept. If you're early, your version may become the
default." Practical application:

- **Monitor emerging-question sources** (Twitter/X, Reddit, GitHub,
  Discord, category-specific forums) for questions being asked before
  any competitor has written a clear answer.
- **Identify shallow or absent competitor coverage** on a topic
  adjacent to your product/expertise, rather than competing head-on for
  an already-well-covered concept.
- **Publish the clearest, most original explanation first** — this is
  the acquisition-stage counterpart to this page's existing
  "concentrate in fewer, higher-authority placements" third-party-
  authority guidance, applied to owned content and topic *timing*
  rather than placement.
- **Use a concrete depth test before publishing**: "Could a competitor
  easily replicate this tomorrow?" If yes, add more original data,
  metrics, or proprietary insight until the answer is no.

## Publish citation-ready primary research/benchmarks

Per [[growth-memo-why-most-original-data-never-gets-cited]] — this
sharpens Tier 1's "Statistics Addition"/"Cite Sources" tactics: having
original data isn't enough, and most organizations' proprietary data
still fails to get cited because of *how* it's packaged, not because
the numbers themselves are weak. In one 301-page citation dataset,
primary research was rare (2.7% of pages) but earned 3.3x the citation
density of other content — and 75 of 90 primary-research citations came
specifically from **benchmarks** (named items compared head-to-head on
a measurable axis), not data dumps or narrative-buried stats.

- **Frame it as a comparison, not a data drop.** Structure the page
  around "which option is best on X" with a table of named
  competitors/options — this only works in topics that have a natural
  comparison axis (speed, cost, latency, performance); topics without
  one (e.g. category education content) don't see this effect.
- **Lead with the result.** Put the comparison finding in the first 30%
  of the content, not buried after setup/narrative. Per
  [[growth-memo-why-proprietary-data-is-your-most-defensible-asset]],
  this isn't just directional advice — **44.2% of all citations come
  from the first 30% of a page** in that source's dataset, one of the
  more concentrated placement effects measured in this wiki.
  Independently corroborated: [[similarweb-how-to-be-the-brand-ai-recommends-2026]]
  states the same figure ("44% of AI citations come from the first 30%
  of a page") from a separate analysis — two independent sources
  converging on the same number.
- **Owning the data doesn't guarantee the citation.** Per
  [[growth-memo-why-proprietary-data-is-your-most-defensible-asset]], an
  aggregator can repackage someone else's original research into a
  cleaner, more extractable format and capture the citation instead of
  the data's originator — publishing proprietary data is necessary but
  not sufficient; the structural packaging tactics on this list are what
  actually wins the citation.
- **More unique figures correlates with higher originality/information
  gain.** Per the same source (On-Page.ai data), pages with 15+ unique
  figures averaged an information-gain score of 62.1 vs. 40.2 for pages
  with minimal original data — "most pages are middling on originality,"
  so genuine data differentiation (not just more content) is what
  separates the two tiers.
- **Box the methodology visibly**: sample, timeframe, measurement
  approach, and confidence level, as a distinct callout — not folded
  into prose.
- **Use real, labeled first-party data**, not synthetic estimates —
  and say so explicitly.
- **Link raw data/sources** so claims are independently verifiable.
- **Show credibility signals**: dated corrections and acknowledged
  limitations outperform a page that claims no caveats.
- **Structure headings so a question maps directly to an answer** —
  AI-retrievable structure, not just human-readable prose.
- **Keep the URL stable.** In the source dataset, 64 of 365 cited URLs
  were dead or redirected, taking 203 citations offline — don't
  reorganize or relaunch a benchmark page's URL once it's earning
  citations.
- **Don't gate it.** Proprietary data behind a lead-gen form can't be
  crawled/cited — if citation is the goal, publish the benchmark
  itself openly, even if a deeper report stays gated.

## Focus over comprehensiveness (fan-out breadth finding)

Per [[airops-fan-out-effect-2026]] — nuances the Tier 1 tactics above:
being retrieved and relevant is necessary but writing an exhaustively
comprehensive page can actively *hurt* citation odds relative to a
focused one:

- **Don't try to cover every fan-out subtopic.** Controlling for query
  relevance, pages covering 26-50% of a query's fan-out subtopics were
  cited more often (38.2%) than pages covering 100% (34.0%). Matching
  3-4 distinct subheadings reduced citation 6pp versus matching only
  0-1 — write a focused, high-relevance answer rather than a
  comprehensive guide.
- **Heading-query match matters more than depth.** Pages with headings
  closely matching the query's language cited 41.0% of the time (0.90+
  similarity) vs. 29-30.2% for weak matches — write headings that
  mirror likely query phrasing, not generic section titles.
- **Retrieval rank is the real gatekeeper — content quality can't
  compensate for it.** Position 1 in ChatGPT's retrieval results = 58.4%
  citation rate vs. 14.2% at position 10, a gap that overwhelms every
  content-level signal measured. This means classic retrieval-
  eligibility work (technical crawlability, ranking well enough to be a
  retrieval candidate at all — see the Technical crawlability checklist
  below) is a harder prerequisite for AI citation than previously
  documented in this wiki, not just for classic SERP ranking.

## LLM-chat-specific tactics (distinct from AI Overview optimization)

Per [[wix-generative-engine-optimization]] — see
[[generative-engine-optimization]]'s new GEO-vs-AI-Overview distinction
section for why this is a separate target from the rest of this
playbook, which mostly concerns Google's AI-Overview/citation behavior.

- **On static pre-trained LLMs (Claude, older GPT, Gemini 1.5,
  NotebookLM), optimize for brand mentions, not links** — these models
  rarely surface links at all, so track bulk brand/entity queries as
  your visibility metric instead of referral traffic.
- **Use the feedback loop.** Thumbs-up/down responses on incorrect
  brand information can correct a static model's answers even between
  training updates — worth doing as an ongoing maintenance task, not
  just a one-time fix.
- **On search-augmented LLMs (Perplexity, Copilot, GPT-4), optimize for
  the underlying search engine**, not the LLM directly — Copilot
  visibility tracks Bing rankings, for example, not Google's. Check
  core queries at regular intervals since visibility fluctuates like
  search rank.
- **Build internal links from already-cited pages to pages you want
  newly cited.** When a search-augmented LLM already references a page
  (check by querying it), that page is the highest-leverage internal-
  link source for pulling other pages into the LLM's citation set — an
  LLM-citation-specific variant of [[link-and-anchor-text-best-practices]]'s
  cornerstone-content linking guidance.
- **Or edit an already-cited page directly**, rather than only linking
  to it. Per [[gofishdigital-chatgpt-search-case-study]] (n=1 case
  study): find an existing page/article a search-augmented LLM already
  cites for a target query, add the specific information you want the
  LLM to surface (structured as a clear bullet-list of key-value
  pairs — a format chosen to match how AI extraction systems parse
  content), and check back roughly a week later. In the cited example,
  adding a "Notable Clients" section to an already-cited listicle caused
  ChatGPT Search to start surfacing notable clients in that brand's
  result listing within about a week — a single data point on GEO
  edit-to-visibility latency, not a measured average.
- **Manage the LLM crawl deliberately.** LLM crawlers exist to help the
  model understand content, not to rank it — they don't need access to
  navigation/pagination pages the way a ranking crawler might benefit
  from; prioritize crawler access to brand/product/service content
  instead. Known user agents: `OAI-SearchBot`/`ChatGPT-User`/`GPTBot`
  (ChatGPT), `BingBot` (Copilot), `Google-Extended` (Gemini, inferred),
  `ClaudeBot` (Claude), `PerplexityBot` (Perplexity) — see
  [[robots-txt-strategy]] for directive syntax.
- **Go beyond content optimization — engage the platforms directly**:
  publisher content-partnership programs (OpenAI, Perplexity Publisher
  Program), custom GPTs (which also rank on Google and can embed
  outbound links), and Perplexity Pages (curated in-app brand
  experiences) are direct-visibility channels with no content-SEO
  equivalent elsewhere in this playbook.

## Chunk-level ("Fraggle") optimization and relevance-scoring tools

Per [[ipullrank-optimize-for-sge]] (2024, the oldest tactical source in
this playbook — treat the mental model as durable, the specific
case-study numbers as dated/anecdotal) — the underlying mechanism
behind the "focus over comprehensiveness" finding above: Google AI
Overviews' RAG pipeline retrieves and cites specific text chunks
("Fraggles"), not whole pages.

- **Optimize at the chunk/section level, not just the page level.**
  Identify which specific paragraph or section is likely to be
  retrieved for a target query, and make *that* chunk clear, complete,
  and self-contained — a great page with one weak target section can
  still fail to get cited.
- **Score chunk relevance before publishing**, using tools like
  MarketBrew's AI Overviews Visualizer, Orbitwise, SurferSEO, or
  MarketMuse. Target 80%+ similarity to currently-surfaced
  top-performing chunks as a practical pre-publish benchmark.
- **Supplement keyword research with People Also Ask and platform
  follow-up/related searches**, not just seed keywords — folds directly
  into [[keyword-mapping-and-cannibalization]]'s "expand keyword
  variations" step when the target is AI Overviews specifically.
- **Mine real query logs and community language, not just
  keyword-volume tools, for AI-search keyword research.** Per
  [[otterly-ai-keyword-research-2026]] (OtterlyAI's own prompt
  research, 2025), real user prompts run substantially longer and more
  specific than what keyword-estimation tools typically surface:
  average 15.1 words vs. 8.8 for tool-estimated prompts, personal
  pronouns in 52% of real prompts, and 78.9% showing clear tool-finding
  intent vs. 62.5% for estimated prompts. Practical implication: pull
  actual question-phrased queries from Search Console, support
  tickets, and community language (Reddit, forums) rather than relying
  on estimated-search-volume keyword tools alone when building a
  keyword list for AI-search targeting specifically.
- **AI Overview content has three format types** — informational
  (paragraphs/lists/images/citations), local (+ maps/Business
  listings), and shopping (+ product cards) — match your optimization
  tactics to the format your query actually triggers (e.g. Shopping
  Graph/product-feed optimization only matters for shopping-format
  queries).

### Answer shape by query intent, and the reranker's passage view

Per [[peec-ai-rerankers-geo-aeo-2026]] (see concept
[[ai-search-reranking-pipeline]] for the full mechanism) — the reranker
between retrieval and generation scores **passages**, not pages, so the
Fraggle guidance above sharpens into concrete shapes:

- **Lead each query-targeting section with one direct-answer sentence in
  the first two lines**, then evidence/context. This is the single
  highest-leverage passage edit.
- **Match the answer *shape* to the query intent** — this beats generic
  "add a list":
  - **Definition** → concise entity description with distinguishing facts.
  - **Selection ("best X")** → named options with inclusion criteria and
    trade-offs. (This — not formatting for its own sake — is *why*
    listicles win at the reranker; see [[listicles-in-ai-search]].)
  - **Comparison** → the same like-for-like criteria applied to every
    option.
  - **Procedure** → ordered steps with prerequisites and exceptions.
- **Make passages locally self-contained** — comprehensible inside any
  plausible retrieval window: use explicit names instead of pronouns, and
  keep each answer adjacent to its supporting claim. A passage that needs
  earlier context to parse loses the rerank.
- **Don't trust a single tool's "relevance score."** Reranker families
  disagree sharply on the same passage (one measured example: a shortlist
  passage scored >99.9% on strict MS MARCO models but a descriptive
  passage scored ~0.1% there and 99.9% on a ModernBERT-family model).
  Validate across models; treat any one score as directional.
- **Diagnose failures by pipeline stage** — *not retrieved* → indexing/
  coverage/authority/freshness (see technical-crawlability below);
  *retrieved but losing* → answer-shape/passage-relevance (this section);
  *strong passage, no citation* → source quality/diversity or
  generation-stage behavior.

## Patent-based selection mechanics (Google AI Overviews specifically)

Per [[richsanger-ai-overview-patent-insights]] (analysis of Google
patent US11769017B1) — a more mechanistic account of *why* the
chunk-level and query-fanout tactics above work, specific to Google AI
Overviews:

- **Two-stage selection**: Google drafts an AI Overview summary from
  direct-match query results, then separately verifies each candidate
  citation via **embedding distance** — semantic similarity between the
  generated summary statement and the actual source text — before
  including a link. Write content whose phrasing is semantically close
  to how the *answer* would plausibly be summarized, not just close to
  the query's literal wording.
- **You must already be a ranking candidate.** AI Overviews reuse
  pre-ranked index results rather than re-scoring content in real
  time — this is the same retrieval-eligibility gate as the Technical
  crawlability checklist below, restated with patent-level detail:
  no rank, no AI Overview inclusion, regardless of content quality.
- **Position 1-2 for the primary query drives direct-match inclusion**:
  53% link-inclusion rate at position 1, ~50% at position 2, dropping
  meaningfully further down — ranking top-2, not just top-10, is the
  target if the primary keyword is your inclusion pathway.
  **Corroborating same-query overlap data (2026-08-03)**: per
  [[derivatex-two-googles-one-query-aio-vs-serp-2026]] (100 B2B-software
  queries), when a source appears in *both* the AIO and the SERP, 72% of
  the time it ranks in Google's **top-5** (median #4) — page-2 rankings
  almost never cross over. But ranking is necessary-not-sufficient: 65%
  of AIO citations don't rank in Google's own top-10 at all, so top-5
  rank buys into the shared corpus, not the AIO-exclusive majority.
  **Track AIO citations and Google rankings as separate KPIs** — one is
  not a proxy for the other.
- **The related/reformulated-query pathway is the bigger lever**:
  targeting adjacent, less-competitive related queries raised link
  inclusion from 46% to over 67% in the cited research — often a more
  tractable win than fighting for position 1-2 on a highly competitive
  primary keyword.
- **YouTube is a third, separate pathway** into AI Overviews alongside
  ranking well in text results — consistent with the brand-level
  YouTube-correlation finding below.
- **Sector pattern**: Health, Finance, and Education trigger AI
  Overviews disproportionately often (informational-query-heavy),
  with YouTube/Wikipedia/Investopedia dominating as linked sources for
  informational queries in those sectors.

### YouTube-specific tactics (2026-07-23)

Per [[otterly-youtube-ai-citation-study-2026]] (100M+ citation
instances, 6 engines) — video-level tactics distinct from the
brand-level "build a YouTube presence" correlation below:

- **Make long-form the default, not Shorts.** 94% of AI citations go to
  long-form video vs. 5.7% to Shorts. If YouTube is a citation channel
  you're pursuing, don't put your GEO budget into short-form.
- **Target Perplexity and Google surfaces specifically for YouTube
  citations.** Perplexity (38.7% of its citations are YouTube) and
  Google AI Overviews (36.6%) rely on YouTube far more than ChatGPT
  (4.4%), Gemini (0.2%), or Copilot (0.5%) — a YouTube strategy is a
  Perplexity/Google-AI-surfaces play, not a general one.
- **Add chapters/timestamps if targeting Google AI Overviews or AI
  Mode.** Timestamped citations are a Google-exclusive mechanism (73%
  AI Overviews, 27% AI Mode, zero on the other four engines), and 78%
  of timestamped videos get cited across 2-5 different chapters —
  effectively multiplying one video's citation surface area. Skip this
  effort if ChatGPT/Perplexity/Gemini are the actual target.
- **Don't chase views, likes, or subscriber count.** All are
  effectively uncorrelated with citation (r = -0.02 to -0.03) — 40.83%
  of cited videos have under 1,000 views and 35% come from channels
  under 10k subscribers. Small channels get cited as often as large
  ones.
- **Write descriptions as machine-readable metadata, not marketing
  copy.** Description length (r = 0.31) and hashtags (r = 0.20) are the
  strongest (still weak) correlates found — include a clear summary,
  named entities, and properly formatted chapter markers.
- **Favor the 10-20 minute range.** The largest citation cluster (32.1%)
  falls in 10-20 minute videos; median cited-video duration is under 8
  minutes — depth over both extremes (very short or 20+ minutes) skews
  citation odds slightly, though duration itself is barely correlated
  (r = 0.02).

### Reddit community engagement tactics (2026-07-23)

Per [[otterly-reddit-geo-ai-search-citations-2026]] (8,167 citations,
60-day controlled experiment, 9x citation multiplier) — tactics for
boosting Reddit's citation visibility as an active community strategy:

- **Community engagement drives a 9x citation multiplier.** This is the
  strongest platform-specific lever measured across all Otterly studies.
  Active community management (replies, discussion) beats publishing
  strategy alone.
- **Prioritize comments/replies over upvotes or post length.** Replies
  matter more than vote counts or word length for citation visibility —
  encourage discussion and community responses rather than chasing
  upvotes or writing lengthy posts.
- **Focus on topic-specific, narrowly-focused communities** over broad
  subreddits. Niche communities show higher citation rates when actively
  managed.
- **Subreddit size (subscribers) doesn't predict citations.** Small,
  active communities get cited as frequently as large ones — don't skip
  niche subreddits based on subscriber count.
- **Maintain active community engagement.** ~30 minutes daily investment
  yields the 9x multiplier; ~15 hours monthly to sustain the effect —
  tractable for content teams as an ongoing community-building strategy.
- **Engagement on Reddit also lifts traditional search rankings.** The
  same engagement activity showed x18 SEO impact — Reddit participation
  boosts both AI citations *and* organic Google rankings from the same
  content.
- **Spread discussion across multiple threads/posts.** Active communities
  distribute citations more evenly across multiple posts rather than
  concentrating on one winner — forum participation breadth signals
  topic relevance to AI systems.

## Structural findings (word count, headings, schema, readability)

Per [[airops-fan-out-effect-2026]]:

- **Word count sweet spot: 500-2,000 words.** Pages over 5,000 words
  underperformed shorter content (28.6% vs. 30.5% citation) — don't
  assume longer/more thorough always wins.
- **4-10 H2-H4 headings optimal for articles** (33.2% citation); product
  pages performed best with **zero** headings (43.2%) — structure
  guidance is page-type-specific, not universal.
- **Add JSON-LD schema markup**: +6.5pp citation advantage overall.
  Strongest types: MedicalWebPage (47%), BreadcrumbList (46.2%),
  FAQPage (45.6%).
- **Write at a college reading level** (Flesch-Kincaid 16-17): 35.9%
  citation, outperforming both simpler and more academic writing.

## Freshness by vertical

Per [[airops-fan-out-effect-2026]] — extends the existing "keep content
fresh" guidance with a specific age curve and vertical-level variance:

- **Optimal content age is 30-89 days** (32.8% citation); content over 2
  years old declines (-5pp); content under 30 days old also underperforms
  slightly (25.3%), likely an indexing-delay effect rather than a
  genuine freshness penalty.
- Freshness only meaningfully helps when relevance is already strong
  (+4.2pp advantage) — among weak query-match pages, age effects are
  negligible, so don't expect a refresh alone to fix a fundamentally
  off-topic page.
- **Vertical-specific gaps**: Finance shows a 15pp gap between fresh and
  5+-year-old content, Travel shows the largest gap in the dataset
  (19pp); e-commerce content freshness barely matters — prioritize
  refresh cycles by vertical, not a blanket schedule.

**Unresolved tension**: [[ahrefs-why-chatgpt-cites-pages-2026]] found
the opposite pattern within search-result citations specifically —
older/established pages (median ~500 days) cited more than fresh ones
— though its own news-vertical data does show a freshness preference,
partially consistent with the above. See
[[ai-citation-landscape]]'s Conflicting Evidence section. Until
resolved, don't apply a single universal freshness curve — check
whether your content type more closely resembles a search-result page
or a news article.

## Authority-building caveat (unresolved conflict)

Per [[airops-fan-out-effect-2026]], domain authority/backlinks showed no
positive (slightly inverse) correlation with which *specific page* gets
cited, once retrieval rank and relevance are accounted for — this is in
tension with the brand-level authority correlations in
[[ai-visibility-correlation-factors]] and
[[growth-memo-topics-matter-for-third-party-authority]] (see that page's
Conflicting Evidence section, unresolved). Practical takeaway until
resolved: don't rely on authority-building alone to win a specific page's
citation — prioritize retrieval rank and query-relevance work first;
treat brand-level authority-building as a separate, longer-horizon
strategy rather than a lever for any one page's citation odds.

## Tier 2 — Modest performers

6. **Authoritative tone** — rewrite to sound more persuasive/authoritative.
   Small or no significant improvement on average — generative engines
   are largely robust to tone alone. Works better in specific domains
   (see table below) than as a general-purpose tactic.
7. **Technical Terms** — add domain-specific technical vocabulary.
   Modest, inconsistent gains.

## Tier 3 — Don't bother (traditional SEO tactics that don't transfer)

8. **Unique Words** — adding rare/unique vocabulary. ~0% improvement.
9. **Keyword Stuffing** — the classic SEO tactic. **~0% or negative** on
   the benchmark, and measured **10% worse than baseline** when validated
   live on Perplexity.ai. Do not use this for AEO/GEO purposes.

**Mechanistic why (retrieval layer).** The lexical-ranking math in
[[lexical-ranking-tf-idf-bm25]] explains *why* stuffing is futile: BM25's
term-saturation curve (`k₁`≈1.2) caps the payoff from repeated terms
(1→baseline, 5→~1.8×, 100→~2.2×), so density percentages don't move the
score — and spam detection sits on top. The same mechanics reframe two
apparently-weak tactics above: "Technical Terms" and "Unique Words" look
weak *for winning an earlier citation*, but distinctive high-IDF
vocabulary (product model numbers, versions, specs, proper nouns) is
exactly what carries the **retrieval/hybrid-retrieval** layer that
[[c-seo-bench-2025]] says dominates — embeddings blur "iPhone 15 Pro Max
256GB" into generic content, and lexical BM25 is what locates the exact
spec. Practical read: use canonical terminology *consistently* (so TF
accumulates on the term you want, not scattered synonyms) and include
specific identifiers to be *retrievable*, but don't repeat for its own
sake.

## Also don't bother (per Google's official guidance)

Per [[google-ai-optimization-guide]], Google explicitly says these do
**not** help visibility in AI Overviews/AI Mode — don't spend effort on:

- Creating `llms.txt` files or other special AI-only markup/text files —
  Google Search doesn't use them. **Scope note**: this claim is specific
  to Google's own AI Overviews/AI Mode. [[sel-ai-optimization-content-for-search-and-agents]]
  recommends creating an `llms.txt` file for documentation/reference
  content targeting the broader AI crawler/agent ecosystem (Andi,
  Perplexity, documentation tools) — but cites no evidence that it
  actually helps there either. Not logged as a resolved or unresolved
  Conflicting Evidence entry (neither source tests the other's scope
  directly), but until better evidence exists, treat Google's
  explicit "doesn't help" as the stronger claim for anything
  Google-AI-surface-related, and `llms.txt` elsewhere as a low-cost,
  unverified bet rather than a proven tactic.
  **Direct negative test (2026-07-22)**: per
  [[otterly-ai-keyword-research-2026]], a 2025 OtterlyAI experiment
  found `llms.txt` produced **no measurable citation lift** — the first
  source in this wiki to report an actual negative test result for
  `llms.txt` rather than just an absence of evidence for it. The same
  experiment found **author schema** also produced no measurable lift
  (new claim, nothing to compare it against yet), while Wikipedia
  presence, LinkedIn Pulse posts, FAQ-on-homepage content, and digital
  PR did show a lift. Treat `llms.txt` and author schema as
  increasingly unlikely to be worth prioritizing, pending independent
  replication.
  **Direct traffic-side null result (2026-07-29)**: per
  [[evilmartians-which-ai-reads-your-site-2026]], a first-party
  server-log study found `llms.txt` is barely *fetched* at all — ~660
  direct fetches over two months, only ~37 from named AI assistants
  (the rest search crawlers and scanners), and its "referral" traffic
  traced to a stale `Chrome/111.0` bot rather than a real AI client.
  This is a step beyond the Otterly result: not just "no citation lift"
  but evidence that AI clients don't request the file in the first
  place. The same study tested a **hidden AI hint** (a `<link>` tag
  pointing at a Markdown variant, tracked via a `?ref=hint` URL param)
  and got **zero attributable fetches** across all 268K agent requests —
  don't bother with decorative "point the AI here" markup either. The
  mechanism that *did* deliver Markdown was HTTP content negotiation (see
  [[technical-seo-audit-checklist]] §5), not any special file or hint.
- "Chunking" content into unnaturally small pieces for AI to parse.
- Obsessing over structured data specifically for AI purposes (still fine
  to use for general SEO, just not an AI-visibility requirement).
- Pursuing inauthentic mentions or backlinks.
- Rewriting content in a way that's specifically "for AI" rather than for
  people — write for people first (see
  [[generative-engine-optimization]]'s Conflicting Evidence section on
  how this squares with the tactics above). Corroborated by
  [[nngroup-ux-writing-faqs-2026]] (NN/g, qualitative practitioner
  guidance, not a study): "Write for people first. Structure it for
  machines second," with SEO/AEO/GEO principles held unchanged —
  "clear structure, plain language, descriptive headings, direct answers
  near the top" (the answer-first pattern). Its scannability data (NN/g
  eyetracking: users read only 20–28% of page text; readers scan and
  enter pages mid-way) is a human-readability rationale for the atomic-
  structure/descriptive-heading tactics above. *Caveat:* NN/g's
  6th–8th-grade reading-level advice targets human comprehension, a
  different outcome from [[airops-fan-out-effect-2026]]'s college-
  reading-level *AI-citation* correlation — don't conflate the two.

## C-SEO Bench: a large-scale re-test of the Tier 1-3 tactics above

Per [[c-seo-bench-2025]] (NeurIPS 2025, Puerto et al.) — a 6-domain
(Retail, Video Games, Books, Web, News, Debate), 4-model (GPT-4o-mini,
Claude 3.5 Haiku, o3, o4-mini), 16.3k-document re-test of the exact
Tier 1-3 tactics above plus two new methods, using **citation rank**
(does the LLM cite this document earlier?) instead of the original
word-count metric:

- **Out of 54 method×domain significance tests on GPT-4o-mini, only 3
  showed a significant positive effect**: Content Improvement (Retail
  only) and LLM Guidance (Retail and Video Games only). No tactic was
  significant for either question-answering domain, and **no tactic
  was significant at all on Claude 3.5 Haiku**.
- **Negative effects are common, not marginal**: the Statistics
  tactic significantly *decreased* citation rank in 19 of 24 tested
  settings. On Haiku 3.5, 26 of 30 product-recommendation settings
  showed significant negative effects.
- **Retrieval/context position dominates every content tactic tested.**
  Moving a document to position 1 in the LLM's context window (i.e.,
  improving traditional retrieval ranking) produced gains of +0.87 to
  +2.77 rank positions depending on domain — several times larger than
  the best content tactic's effect in every domain (e.g. Retail: +2.77
  for position-1 vs. +0.36 for the best content tactic tested).
  **Practical implication: if forced to choose, prioritize retrieval-
  eligibility and ranking work (see this page's Technical crawlability
  checklist and [[traditional-seo-ranking-factors]]) over the content
  tactics above** — this is the same conclusion as
  [[airops-fan-out-effect-2026]]'s retrieval-rank-as-gatekeeper finding,
  now independently corroborated via a controlled experiment (randomly
  assigned context position) rather than only observational data.
- **Two new tactics tested, both among the only ones with any
  significant effect**:
  - **LLM Guidance**: generate an `llms.txt`-style markdown summary
    (title, intro, sections) and prepend it to the document. The
    best-performing tactic overall by AUC (average gain across
    adoption rates 0-100%), though still small in absolute terms and
    only significant in 2 of 6 domains.
  - **Content Improvement**: a holistic combination of all eight
    original tactics (fluency, authority, structure, bolding key
    features) into one rewrite pass — the second-best by AUC.
  - **Caution on `llms.txt`**: this finding is specific to third-party
    conversational search engines built on GPT-4o-mini/Claude/o3/
    o4-mini context windows, not Google's own AI Overviews — per
    [[google-ai-optimization-guide]] elsewhere on this page, Google
    explicitly states `llms.txt` files don't help its own AI features.
    Treat LLM Guidance as a low-cost, modestly-evidenced bet for
    third-party LLM chat surfaces specifically, not a general AI-
    visibility fix.
- **C-SEO is a congested, zero-sum game as adoption rises**: the
  average gain per adopter shrinks steadily as more competing
  documents adopt the same tactic (LLM Guidance or Content
  Improvement), converging toward zero as adoption approaches 100% —
  modeled as a non-cooperative multi-actor game. This is a genuinely
  new dynamic for this wiki: prior white-hat GEO research (including
  the Tier 1-3 source above) only tested single-actor/unilateral
  adoption. Practical implication: an early-mover advantage from
  adopting an effective content tactic is likely to erode as
  competitors copy it — don't assume a one-time content investment
  keeps paying off indefinitely if the tactic becomes common in your
  category.
- **Why this doesn't flatly contradict the Tier 1-3 source above**: the
  original paper measured word count (how much the LLM discusses a
  document), not citation rank (whether it's cited earlier) — a
  document can be discussed at length without being cited first. See
  [[generative-engine-optimization]]'s Conflicting Evidence section for
  the full reconciliation. Net effect: **treat the Tier 1-3 rankings
  above as exploratory rather than validated for winning an earlier
  citation specifically**, until further replication narrows the gap.

## Provider-specific tactics

Per [[ai-citation-landscape]], ChatGPT/Claude/Gemini cite from largely
non-overlapping sources — treat them as separate targets, not one
generic "generative engine":

- **Targeting ChatGPT or Claude?** Invest in a solid **Wikipedia**
  presence — it's a top-3 cited domain in 12/17 industries for ChatGPT
  and 8/17 for Claude. Skip this if Gemini is your main target (top-3 in
  only 3/17 industries for Gemini).
- **Targeting Gemini?** Reddit presence matters — it's Gemini's single
  most-cited domain (2.4% of citations) and essentially absent for the
  other two providers. Quora shows up prominently for Gemini too.
- **Targeting Claude specifically?** It cites far less often (55% of
  responses) but much more deeply (13 citations) when it does, and
  favors academic/reference sources like PubMed Central. It never cites
  YouTube — don't rely on video content to reach Claude. **Additional
  guidance (2026-07-23)** per [[otterly-claude-ai-citation-study-2026]]:
  Claude cites almost exclusively first-party brand/company-owned content
  (64% of citations), with long-tail distribution (top 10 domains = 9.5%).
  Social media is immaterial (0.9%, almost entirely LinkedIn; Reddit 0%).
  For Claude visibility, invest in official brand documentation, well-
  structured reference content (not reviews/forums), and institutional
  sources — the opposite strategy from ChatGPT/Gemini/Perplexity.
- **Local/"best of" queries (hotels, restaurants, services)**: ChatGPT
  leans heavily on **Google Maps** results, not articles or reviews
  (188 citations per 1,000 such queries) — a current, accurate Google
  Business Profile matters more than written content here. Claude
  essentially doesn't do this.
- **Keep content fresh**: 57% of journalism citations are from the past
  12 months — publishing once and never updating loses ground to
  freshly-dated coverage over time.
- **Consider short-form, cross-topic coverage**: Axios is the one
  outlet that breaks through across most industries in ChatGPT's
  citations, plausibly due to its concise, high-frequency format —
  worth testing as a content-format hypothesis, not just a content-style
  one.
- **Targeting Microsoft Copilot/Bing AI?** Per
  [[bing-ai-performance-report]], Microsoft's own guidance corroborates
  (rather than adds new tactics beyond) what's already catalogued above:
  align content with user intent, deepen subject-area coverage,
  structure content with descriptive headings/tables/FAQs, back claims
  with evidence, keep content fresh, and keep text/image/other-media
  descriptions of the same entity consistent. The one genuinely new
  angle is diagnostic rather than tactical: Bing Webmaster Tools'
  **Intents** and **Topics** preview features let you check whether your
  citations cluster in the query-intent category you're targeting (e.g.
  Commercial/Comparison for e-commerce) and whether a topic generating
  citation activity is under-covered on your site — see
  [[ai-visibility-measurement-methodology]] for the full tool
  breakdown.

## Measure presence, portability, and concentration separately

Per [[sej-the-consensus-gap]] — don't rely on a single blended "AI
visibility" score, since engines pull from largely disjoint source
pools (only 2.35-2.45% of cited URLs appear across ChatGPT, Perplexity,
and Google AI Overviews for the same prompt; 91% appear in only one):

- Track **presence** (do you appear in any engine at all),
  **portability** (do the same cited URLs survive across engines), and
  **concentration** (what share of your citations comes from one
  engine) as three separate numbers, not one composite score.
- Don't assume ranking well in one engine predicts ranking in another —
  treat each engine as a genuinely separate optimization target (this
  reinforces the [[ai-citation-landscape]] provider-specific guidance
  above, now with direct URL-level overlap data rather than just
  domain-mix differences).
- **Prioritize explanatory content** (guides/tutorials) over
  brand-centric or transactional pages if cross-engine portability is
  your goal — guides/tutorials showed the highest (still low, 2.3%)
  portability, vs. 1.1% for homepages. Ask "does this page directly
  answer the query well" (utility) rather than "does this page
  represent our brand well" (brand centrality) — the source's framing
  is that engines favor the former.
- Pick a priority engine deliberately rather than chasing generic
  cross-engine visibility — given how low universal portability is
  (even Wikipedia is only 1.3% universal), spreading effort thin across
  all engines may be less effective than committing to the 1-2 engines
  that matter most for your actual audience/business.

## The three-layer source strategy (works across all engines at once)

Per [[brightedge-ai-search-same-brands-different-sources]] — despite the
low source-level portability above, *brand*-level recommendations
converge much more across engines (36-55% brand overlap vs. 16-59%
source overlap). This means one unified strategy, weighted per engine,
can beat five separate playbooks:

- Build presence across all three layers every engine draws from, just
  weighted differently per engine:
  1. **Authority** — trade associations, analyst firms, standards
     bodies, vertical-specific experts. Treat "authority" as
     **category-relative**, not a fixed .gov/.edu checklist — identify
     which authoritative sources actually dominate citations in *your*
     specific category.
  2. **Commercial & Editorial** — PR, trade press, review-site
     visibility, comparison content. This is the single widest lever:
     37-51% of citations across *every* engine studied, the largest
     layer everywhere.
  3. **UGC** — video, forums, community/creator coverage. Low overall
     share for most engines, but **non-negotiable specifically for
     Google AI Overviews** (~18% of its citations, with a single video
     platform alone at 10.6%) — understand which specific videos/forum
     threads it cites and earn authority within those conversations,
     rather than producing generic short-form video.
- Weight engine investment by where your actual buyers are: B2B/SaaS
  audiences skewing ChatGPT/Perplexity → emphasize authority +
  commercial/editorial, UGC supplemental. Consumer audiences skewing
  Google AI Overviews → emphasize UGC + commercial/editorial, authority
  reinforcing.
- Track Google's own surfaces separately rather than as one "Google AI"
  bucket — AI Mode and AI Overviews share 59% source overlap with each
  other (a win on one plausibly transfers), but Gemini overlaps *more*
  with ChatGPT (39%) than with either Google surface (27-34%) — Gemini
  needs its own strategy, not a "just optimize for Google" shortcut.

## Five-component intent framework and AI-reuse formatting

Per [[similarweb-how-to-win-the-race-for-gen-ai-search-2026]] — a more
granular way to align content with what an AI retriever selects than
matching a query's keywords alone. Break each target prompt into five
intent components and make sure content satisfies all five:

1. **Task intent** — what the user wants to accomplish (compare,
   choose, define, troubleshoot, plan, evaluate, configure, summarize).
2. **Format intent** — how the answer should be structured (steps,
   bullet list, comparison table, definition, checklist, pros/cons).
3. **Entity intent** — which specific brands/tools/concepts must be
   named.
4. **Depth intent** — how detailed the answer should be (high-level
   overview vs. expert deep-dive vs. beginner explanation).
5. **Constraint intent** — requirements the answer must respect (budget,
   speed, region, year, difficulty level, niche audience). The more
   granular the constraint match, the better the citation odds.

**AI-reuse formatting checklist** (make selected content easy to extract
and cite):
- [ ] Concise TL;DR (40-80 words) at the top of the page
- [ ] A "Short answer" block using bullets or numbered steps
- [ ] Clear H2/H3 headings that mirror likely user phrasing
- [ ] Short, atomic paragraphs — one idea per block
- [ ] Predictable templates the model recognizes (definitions,
      comparisons, FAQs, steps)
- [ ] Schema markup where relevant (FAQPage, HowTo, Article)
- [ ] Explicit, consistent entity naming throughout

**FAQ schema citation lift (concrete number)**: per
[[otterly-how-to-optimize-content-for-ai-search-2026]] — a first-party
OtterlyAI experiment, not a secondhand citation — implementing FAQ
schema produced a 350% increase in AI citations (2,379 vs. 529) on the
pages tested. One experiment, not independently replicated in this
wiki yet, but a concrete number behind the generic "add FAQPage schema"
advice already in the checklist above.

## Measuring AI visibility as sustained topical authority

Per [[similarweb-how-to-be-the-brand-ai-recommends-2026]] (quoting
Aleyda Solis) — a concrete visibility-measurement target that sharpens
the wiki's general "track presence per topic" guidance:

- Don't chase perfection on any single prompt. Build structured prompt
  sets reflecting real buyer journeys — representative prompts across
  key topical hubs, product categories, and funnel stages (early
  research through final transaction).
- Ask "are we consistently visible across this intent category?" rather
  than "are we showing up for this one query?"
- **Target being cited/mentioned in roughly 70-80% of relevant,
  high-intent prompts within a topic cluster** as the bar for "won" — a
  concrete, quotable target where the wiki previously only had
  qualitative "track presence per topic" guidance.

## Third-party authority building (topic-specific)

> For a **competitor-displacement** framing of these same artifact +
> off-site-seeding tactics — diagnosing which specific artifact earns a rival's
> citation and building to take it — see the [[competitor-citation-displacement]]
> playbook.

Per [[growth-memo-topics-matter-for-third-party-authority]] — extends the
three-layer source strategy above with tactics specifically for earning
third-party citations/mentions:

- **Stage-match your off-site strategy (2026-07-30).** Per
  [[victorious-q2-2026-quarterly-search-report]] (175 brands, 8
  platforms), brand *naming* is concentrated down-funnel: brands were
  named in just 0.10% of *problem-awareness* answers but >12x as often in
  *category-research* answers. So (a) publish educational,
  problem-awareness content that AI will cite even though it usually
  omits your name — it builds the third-party footprint that later
  correlates with mentions (referring domains 0.49, third-party mentions
  0.45; brands with <2,000 pages mentioning them were named just 3% of
  the time); and (b) prioritize presence on the **directories and
  comparison sites** AI leans on for category research, where mentions
  actually happen. Don't chase self-citation: 99.99% of category-research
  citations went to third-party domains, not the brand's own site.
- **Tailor placements to the vertical's citation shape.** Legal-services
  citations concentrate in a few prestige directories; SaaS citations
  scatter across 10,000+ domains — a handful of authoritative placements
  can own a legal topic, while SaaS needs broader distribution.

- **Map trusted sources per topic, not per category.** Trusted-source mix
  can shift sharply even within one category depending on the specific
  query topic (competitor domains: 33.5% of citations for invoicing
  queries vs. 7% for business-startup queries) — build a source map for
  each topic you're targeting rather than assuming one map covers a
  whole category.
- **Concentrate in fewer, higher-authority placements rather than
  spreading thin.** Authority gains are tiered, not linear — three
  placements in a top-decile-authority source outperformed a dozen
  placements across low-authority sites in the source's 1,000-domain
  analysis. Prioritize getting into the top 1-2 outlets AI already cites
  for your topic over broad low-authority PR/guest-post campaigns.
- **Use named, credentialed authors instead of brand-account bylines.**
  Fresh, expert-authored, clearly time-stamped content earned faster
  visibility than faceless brand-account publishing (per LinkedIn's
  analysis, cited in the source). **Quantified by a later, primary
  source**: per [[otterly-linkedin-ai-citations-study-2026]] (384K
  LinkedIn URLs, disclosed methodology), named individual authors draw
  91.7% of citations vs. 8.3% for company/unattributed pages (8.5 vs.
  5.5 average citations per URL) — a large, precisely-measured version
  of the same claim.
- **Prioritize targets with a two-factor score.** Per
  [[similarweb-how-to-win-the-race-for-gen-ai-search-2026]], once you've
  identified the domains and specific cited URLs AI relies on for a
  topic, rank outreach targets by **Influence score** (how authoritative
  the domain is within that specific topic) × **Prompt frequency** (how
  often that URL is cited across user prompts) — the higher the combined
  score, the more citation impact a mention there is likely to have.
- **Action checklist**:
  - [ ] Identify 2-3 credible subject-matter experts to author/be quoted
        in third-party content.
  - [ ] Map which sources AI already cites for your specific topics
        (not just your category).
  - [ ] Concentrate outreach/PR effort on the highest-authority
        publications in that map.
  - [ ] Pursue nofollow placements too — citation value doesn't require
        a dofollow link.
  - [ ] Create embeddable data assets (charts/widgets other sites can
        embed, carrying a link back).
  - [ ] Publish on LinkedIn for faster indexing/visibility alongside
        primary publication.

## Organic citation seeding: channel list and the paid-vs-organic nuance

Per [[vercel-adapting-seo-for-llms]] — extends the third-party
authority-building guidance above with a specific, high-signal channel
list and one new nuance: **paid links reportedly carry reduced weight in
training data compared to organic references** — community mentions
that read as organic (not sponsored) are more likely to shape how a
model associates a brand with a concept.

- **Seed presence across**: Reddit, GitHub, Hacker News, Twitter/X,
  LinkedIn, Stack Overflow, changelogs, AMAs, product demos, and
  open-source/referenceable examples — indexable, high-signal channels
  where "community mentions associate brands with concepts" and models
  tend to follow human citing patterns.
- **Don't substitute paid placement for organic mentions** if AI
  training-data influence (as opposed to live retrieval citation) is the
  goal — this is a different mechanism than [[peec-ai-self-promotional-listicles-2026]]'s
  live-retrieval citation-rate findings above, so treat this as an
  additional, training-data-specific consideration rather than a
  replacement for the existing self-promotional-content cautions.

## LinkedIn-specific tactics: format and authorship over engagement

Per [[otterly-linkedin-ai-citations-study-2026]] (2.06M citation
records, 6 engines) — sharpens the general LinkedIn-seeding guidance
above into concrete, disclosed-methodology tactics:

- **Publish long-form Pulse articles, not just short posts.** Pulse
  articles draw 72.2% of LinkedIn AI citations from just 63.0% of URLs
  (8.5 avg citations/URL), vs. posts (26.1% of citations, 5.9 avg) and
  profiles (1.7% of citations, 3.0 avg). Pulse articles also run far
  longer (median 1,021 words vs. 185 for posts) — length itself isn't
  the driver (see below), but the format correlates strongly.
- **Don't optimize for engagement — it doesn't predict citation.**
  Likes, comments, emojis, and hashtags all show near-zero correlation
  with citation (r = -0.02 to -0.06); posts with video or images
  averaged *fewer* citations than posts without. Spend effort on
  extractable, substantive content instead of engagement-bait
  formatting.
- **Target Perplexity and Google AI Overviews specifically for
  LinkedIn content** — together they account for 65.5% of all LinkedIn
  AI citations (43.3% and 22.2% respectively). If optimizing
  specifically for Microsoft Copilot, prioritize Pulse articles almost
  exclusively — 90.2% of Copilot's LinkedIn citations are articles, a
  higher concentration than any other engine studied.

**Second-source corroboration + additional tactics** (per
[[semrush-linkedin-ai-visibility-study-2026]], 89K LinkedIn URLs, 325K
prompts, 3 engines — independently replicates the long-form-wins and
engagement-doesn't-matter findings above on a different sample):

- **Post consistently — cadence is itself a citation signal.** 75% of
  cited authors posted 5+ times in four weeks. Build employee-advocacy /
  SME-enablement programs so experts publish on a regular schedule, not
  in one-off bursts.
- **Publish original, educational content.** 95% of LinkedIn AI citations
  are original (reshares only ~5%); 54–64% of cited posts share
  knowledge/practical advice. Don't reshare — write.
- **Hit the cited-length bands.** Articles **500–2,000 words**, posts
  **50–299 words** are cited most.
- **Structure answer-first and define your terms.** Lead with the direct
  answer under a clear headline, then logical flow; explicitly define key
  concepts and brand terms (LinkedIn content scored 0.57–0.60 semantic
  similarity to AI answers, higher than Reddit/Quora — extractable,
  well-defined content mirrors answers better).
- **Ignore follower count.** Authors with <500 followers are cited
  equally or more than those with 500+ — expertise/relevance beats reach,
  consistent with the engagement null above.
- *Caveat — Company Page vs. individual:* both studies agree individuals
  dominate on ChatGPT and Google AI Mode, but Semrush found Perplexity
  leaning to Company Pages (59%) against Otterly's individual-dominant
  aggregate — an unresolved split logged under
  [[ai-citation-landscape]]'s Conflicting Evidence. Default to
  named-individual authorship; balance in a Company-Page presence rather
  than betting everything on either.

## Content refresh cadence: a concrete schedule

Per [[vercel-adapting-seo-for-llms]] — a specific cadence extending this
page's existing general "keep content fresh" guidance: review content on
**30, 90, and 180-day intervals** — refresh stale material, expand
high-performing pages, archive obsolete pages with 301 redirects, and
close competitive gaps proactively. Also maintain basic freshness
hygiene alongside the review cadence: fix 404s, keep sitemap `lastmod`
timestamps accurate, and keep sitemaps clean — "models re-crawl the web
regularly," so stale content compounds in disadvantage over time rather
than just sitting flat.

## Target common query-fanout injection angles

Per [[peec-ai-chatgpt-query-fanouts-2026]] (5M query fanouts,
ChatGPT/Perplexity/Grok, April 2026) — write toward the hidden
sub-queries an engine actually issues, not just a page's literal
target query:

- **Cover comparison/best-of/review angles explicitly**, even if the
  target query doesn't use that language — ChatGPT injects "best" into
  24.3% of advice-style questions and "reviews" is its third
  most-injected word overall. A page that already addresses "best X,"
  "X vs Y," and "X reviews" framing is more likely to match what the
  engine is actually retrieving against.
- **Maintain a review-platform presence** (G2, Glassdoor, Sitejabber,
  or category-equivalent) since ChatGPT actively searches review
  content even when the user didn't ask for it — this shapes brand
  description regardless of whether your own site ranks for the
  literal query. **Caveat (unresolved conflict)**: [[derivatex-4cs-explainable-to-ai-2026]]'s
  small (n=233) ChatGPT-only "Authority Inversion" study found G2 and
  Capterra cited *zero* times, with 84% of recommendation citations from
  vendor self-descriptions/niche sites — see [[ai-citation-landscape]]'s
  Conflicting Evidence section. Don't drop review-platform work on that
  single study, but pair it with making your own primary pages maximally
  legible (see [[explainable-to-ai-4cs]]). Per
  [[firstpagesage-searchgpt-optimization-2025-guide]] (no disclosed
  methodology, treat as directional rather than measured) — Clutch,
  CNET, Capterra, TrustPilot, and the Better Business Bureau round out
  this list for B2B/service categories where G2/Glassdoor coverage is
  thin.
- **Keep a current-year reference current** on pages likely to be
  fanned out with a year token (5.44% of ChatGPT prompts get one
  injected) — stale "2024" mentions on an otherwise-good page can
  mismatch a freshness-weighted fanout subquery.
- **If targeting Grok specifically**, note it fans out far more
  aggressively (6.8 subqueries/query vs. ChatGPT's 2.1) and explicitly
  site-targets a small set of trusted domains (Reddit, Wirecutter,
  Consumer Reports) at very high rates — presence within those
  specific trusted sources may matter more for Grok visibility than
  general on-site optimization.
- **Don't rely on ranking for a query's literal phrasing alone** —
  since fanout results are combined via Reciprocal Rank Fusion,
  content that surfaces across multiple fanout angles (e.g. both a
  "best X" list and an "X reviews" page) has a structural ranking
  advantage over content matching only one angle.

## Fan-out discovery and optimization workflow (2026-08-20)

Per [[zyppy-fan-out-framework-2026]] (Cyrus Shepard) — a named,
repeatable 5-step process for operationalizing the fan-out-targeting
tactics above (originally sourced from
[[peec-ai-chatgpt-query-fanouts-2026]] and
[[lilyray-chatgpt-fanout-queries-2026]]) into a concrete workflow with a
defined discovery step:

1. **Identify a ranking keyword** — pick a query where the page already
   holds a top 10-20 Google position, since fan-out subquery discovery
   works from an existing foothold, not a cold-start topic.
2. **Discover fan-out queries** for that keyword using a dedicated tool:
   QueryFan (API key required), Qforia (Google-specific, needs a Gemini
   API key), queryfanout.ai or the "Query Fan Out Analysis" tool (no API
   required), Bing Webmaster Tools' AI Performance Report (see
   [[bing-ai-performance-report]]), or, per
   [[zyppy-seo-strategies-for-ai-search-2026]], **AlsoAsked.com** as a
   free proxy — "People Also Ask" question data correlates with the
   kind of sub-questions AI engines fan out to, giving a no-API
   discovery option.
3. **Consolidate** the resulting sub-queries into a prioritized topic
   list — use a clustering tool (Keyword Insights) or a keyword-research
   tool (Ahrefs Keyword Explorer) to group overlapping fan-out subtopics
   rather than treating each one as a separate target.
4. **Optimize existing pages or create new ones** targeting the
   consolidated topics — but **do not create a low-quality page per
   fan-out subtopic discovered**; the source explicitly warns this
   triggers Google's Scaled Content Abuse demotion (see
   [[e-e-a-t-and-page-quality]]) rather than improving fan-out coverage.
5. **Measure results** via webmaster tools (Bing AI Performance Report,
   Google Search Console's Generative AI Features report) and/or a
   premium AI-visibility tracker (Peek, Otterly, Profound, Gumshoe — see
   [[ai-visibility-measurement-methodology]] for the fuller tool
   landscape).

**Caveat baked into the framework itself**: fan-out queries are
"probabilistic and personalized, and vary greatly across AI models and
even within user sessions" — treat any single discovery-tool snapshot as
a sample of a moving target, not a fixed subtopic list, consistent with
this wiki's existing cited-source-volatility findings (40-60%
month-to-month churn per [[sel-what-is-generative-engine-optimization-geo-2026]]).

## Email and personal-context signals (2026-08-20)

Per [[ipullrank-google-personal-intelligence-experiment-2026]] (see
[[personal-context-signals-in-ai-search]] for the full mechanism
writeup) — a controlled experiment found Google AI Mode's opted-in
"Personal Intelligence" feature lets Gmail/Photos content shift which
brands get recommended to that specific user, independent of public
web authority (seeded-brand appearance rose from 23.9% to 66.8%; email
seeding alone reached 53.6%). Caveats first: small-sample, 16-day,
opted-in-only experiment, not yet independently corroborated — treat
the tactic below as a low-cost hedge, not a proven lever:

- **Treat customer-communication email as a discovery channel, not
  just a retention one**: order confirmations, receipts, product-
  education emails, and recommendation emails are plausible candidates
  for the kind of content that seeded brand recognition in this
  experiment. No changes to email content are validated as effective
  yet — this is a "worth monitoring/testing," not a "do this" tactic.
- **Don't expect this to substitute for public web presence**: AI Mode
  continued citing external sources even while personalizing, and the
  effect was weakest in trust-heavy/considered categories (banking, B2B
  services) — personal-context signals appear to shift *consideration*,
  not replace the citation/authority requirements covered elsewhere in
  this playbook.
- **Category-dependent**: expect little effect in trust-heavy/YMYL-
  adjacent categories and more in consumer-preference categories —
  don't apply a blanket email-content strategy uniformly across
  verticals.
- **This is genuinely early evidence**: a single small experiment, no
  replication yet, testing only *opted-in* Personal Intelligence rather
  than default AI Mode. Worth watching, not worth over-investing in
  until corroborated.

## Benchmark domain standing via Common Crawl's Web Graph (2026-08-20)

Per [[commoncrawl-web-graph-ai-ranking-signals-2026]] — Common Crawl's
dataset trains a large share of LLMs (64% of analyzed models; over 80%
of GPT-3's training tokens per Mozilla Foundation's 2024 report per
[[how-google-search-works]]), so a domain's standing in Common Crawl's
own **Web Graph** is a plausible, checkable proxy for how
"overrepresented" it is in LLM training data specifically — distinct
from, and a useful complement to, commercial Domain Rating/Authority
Score metrics that reflect Google's index rather than LLM training
corpora:

- **Check Harmonic Centrality and PageRank** for your domain and
  competitors via the free **CC Rank Checker** (webgraph.metehan.ai,
  18M domains across five time periods 2023-2025) or Common Crawl's own
  **Web Graph Statistics** (commoncrawl.github.io/cc-webgraph-statistics).
- **Track changes over time** rather than a single snapshot — five
  historical periods are available, letting you see whether a domain's
  training-data-relevant standing is rising or falling independent of
  its Google ranking.
- **Weight link-building targets by web-graph position, not just
  referring-domain count**: a link from a domain with high Harmonic
  Centrality (a well-connected hub) plausibly carries more training-data
  representation value than a link from an equally-authoritative but
  more peripheral domain — untested as a direct causal claim, but a
  reasonable prioritization heuristic given the mechanism.
- **Treat this as directional, not a validated ranking factor**: the
  underlying claim (web-graph centrality → AI citation likelihood) is
  a plausible inference from Common Crawl's training-data role, not a
  measured correlation tested in this source. Pair with, don't replace,
  the citation-probability-by-organic-rank guidance above.

## `site:` operator targeting and official-domain signaling (2026-08-20)

Per [[lilyray-chatgpt-fanout-queries-2026]] (secondary aggregation,
undisclosed methodology — treat as directional) — ChatGPT's `site:`
operator usage in fan-out queries reportedly rose from 0.3% to 23% of
fan-outs alongside a broader fan-out-volume jump (see
[[ai-citation-landscape]]'s "ChatGPT fan-out escalation" addendum),
increasingly restricting retrieval to specific trusted or brand-official
domains rather than open web search:

- **Monitor `site:` search impressions** in Google Search Console and
  Bing Webmaster Tools — a concrete way to detect whether ChatGPT (via
  Bing-index-backed retrieval) is issuing `site:`-restricted queries
  against your domain at all, and whether it's targeting the *correct*
  one.
- **Clarify official-domain status** through title tag and meta
  description language (e.g. explicitly stating "official site" /
  the brand's canonical domain) as a countermeasure to the
  domain-confusion risk below — a low-cost signal when the model's
  `site:` targeting is query-constructed rather than looked up.
- **Domain-confusion risk is real and can cause full-channel
  invisibility, not just mis-citation**: ChatGPT has constructed
  `site:` queries against the wrong domain entirely (e.g.
  `site:census.com` instead of the startup's actual `getcensus.com`).
  If the model has the wrong domain and retrieval for that query is
  `site:`-gated, the correct domain never enters the retrieval set at
  all. Brands with a domain name that diverges from their obvious
  brand-name guess (non-`.com` TLDs, abbreviated/rebranded domains)
  are at higher risk and should prioritize the title-tag/meta
  clarification above.
- **A related but distinct security risk**: Netcraft found ~1/3 of
  brand login links generated by LLMs pointed to domains the brand
  didn't own, and ~29% targeted unregistered/parked domains — this is
  an LLM-answer-generation failure (hallucinated URL) rather than a
  `site:`-search failure, but the same underlying fix (making the
  official domain unambiguous and consistently signaled) helps both.
- **Keep pricing/specs in crawlable HTML, not JS or images** — product
  specs/pricing queries are one of the query types most likely to
  trigger brand-official-domain `site:` targeting, so content that
  isn't crawlable there is invisible to that specific retrieval path
  even if the model targets the right domain.

## Awards, credentials, and directory placements as authority signals (lower confidence)

Per [[firstpagesage-searchgpt-optimization-2025-guide]] — no disclosed
methodology, sample size, or study behind this claim (a marketing
agency's own model of "the algorithm," not a measured study); treat
directionally rather than as verified fact, and as an addition to
this wiki's authority-signal tactics rather than a replacement:

- **Publicize awards and accreditations** — both consumer-facing
  awards (from non-industry sources) and B2B industry awards from
  professional associations are claimed to carry signal, distributed
  via social/PR channels rather than just listed on-site.
- **Pursue directory listings beyond Wikipedia** — Hoovers and
  Bloomberg are named alongside Wikipedia as directories worth
  submitting company information to, to increase crawler exposure.
- **For newer brands without list placements yet**, lean on customer/
  usage metrics (adoption rate, customer count, market share) as a
  substitute authority signal until third-party list/review coverage
  accumulates.
- **Google ranking as a SearchGPT input**: this source claims
  SearchGPT/ChatGPT references top Google results directly, so
  improving classic Google rankings feeds AI visibility too. This
  aligns with the "supported by" side of
  [[ai-visibility-correlation-factors]]'s existing Conflicting
  Evidence on domain/brand authority (Ahrefs, Growth Memo) rather than
  the "contradicted by" side (AirOps' page-level null finding) — see
  that page for the full unresolved picture; this source doesn't
  resolve it, just adds another voice to one side.

## Optimize for search-index citation and semantic relevance (ChatGPT)

Per [[ahrefs-why-chatgpt-cites-pages-2026]] (1.4M ChatGPT prompts) —
sharpens the "get retrieved, then compete on relevance" framing above
with source-type-specific data:

- **Prioritize ranking in the search index over other channels.**
  ~88% of ChatGPT citations come from the search-index reference type;
  Reddit, YouTube, and academic sources are each cited under 2% of the
  time even when retrieved — classic search visibility remains the
  dominant lever for ChatGPT citation specifically.
- **Write toward semantic alignment with likely fanout sub-queries,
  not just the surface prompt.** Cited pages score meaningfully higher
  on title-level semantic similarity to both the user's literal prompt
  (0.602 vs. 0.484 for non-cited) and ChatGPT's internal fanout
  sub-queries (0.656) — reinforces the query-fanout-angle tactic above
  with a direct relevance-score mechanism.
- **Use natural-language URL slugs.** Search results with
  natural-language slugs were cited at 89.78% vs. 81.11% for
  non-natural-language URLs — a small but measurable structural lever
  for ChatGPT specifically. **Caveat**: a much larger 6-engine study,
  [[otterly-url-ai-citations-study-2026]] (1.03M URLs), found URL
  length, hyphen count, digit presence, and question-pattern wording
  (how-to/what-is) all non-predictive of citation — don't over-invest
  in URL micro-optimization beyond this one lever, and treat it as
  possibly ChatGPT-specific rather than universal.
- **Use clean, canonical URLs — avoid unnecessary query strings.**
  Per [[otterly-url-ai-citations-study-2026]], URLs without query
  strings averaged 24% more citations than parameterized URLs (2.1 vs.
  1.6). A concrete, actionable lever: consolidate tracking-parameter
  variants to a canonical URL rather than letting AI crawlers retrieve
  and split citation credit across multiple parameterized versions of
  the same page.
- **Prioritize reference/guide content over transactional pages when
  choosing what to build.** Per the same study, guide pages average
  42% more citations than baseline, while product/service (-16%) and
  pricing pages (-21%) underperform — independently corroborating this
  page's existing content-type-portability findings above (guides
  highest, product/homepage lowest).
- **Don't expect Reddit presence to earn direct citation** — it's
  retrieved constantly (67.8% of all non-cited URLs) but rarely
  attributed. Treat Reddit presence as shaping ChatGPT's background
  understanding/consensus of a topic, not as a citation-generating
  channel in its own right.

## Target listicle rank, not just listicle inclusion

Per [[peec-ai-listicle-rank-effect-2026]] (see
[[listicles-in-ai-search]] for the full listicle picture) — extends
the third-party authority-building guidance above with a rank-specific
tactic: getting *into* a third-party listicle isn't the finish line,
since position within it measurably shifts visibility, answer
placement, and mention count.

- **Identify which listicles AI engines actually cite repeatedly** for
  your commercially important prompts, not listicles in general — a
  low-retrieval listicle contributes little regardless of your rank in
  it.
- **Concentrate on rank within those specific sources.** Five strong
  placements in frequently-cited listicles outperform fifty placements
  in rarely-retrieved ones — this reinforces the topic-specific
  authority-building guidance above ("concentrate in fewer,
  higher-authority placements").
- **Match strategy to market maturity.** In fragmented/emerging
  markets, prioritize immediate rank/placement work (steepest rank
  dropoff, biggest marginal win from #1). In established markets,
  pair listicle rank work with broader brand-building — rank
  sensitivity is flatter once a brand is already included.
- **Weight effort by target engine.** Tight-retrieval engines (ChatGPT,
  GPT-5 Search, Microsoft Copilot) reward top listicle rank more
  heavily than broad-retrieval engines (Google AI Overview, AI Mode) —
  prioritize listicle-rank work if those tighter-retrieval engines are
  your primary target.

**Caution — self-promotional listicles are not a recommended shortcut.**
Per [[peec-ai-self-promotional-listicles-2026]], publishing a
self-promotional "best of" listicle on your own domain does still get
cited on some platforms (~11% of citations in the studied sector,
higher on Google AI Mode/Perplexity than ChatGPT) — but this is
reported as an inconsistent retrieval-filtering gap, not a validated
tactic. Third-party listicle placement, authentic third-party reviews,
and educational content remain the recommended path; see
[[e-e-a-t-and-page-quality]] for the trust/disclosure risk of
undisclosed self-interest.

**It can actively backfire.** Per
[[sej-why-calling-yourself-the-best-2026]], even when a self-ranked
listicle *does* get cited by Google AI Overviews, the AI's actual
recommendation goes to a competitor named within that same listicle
roughly 69% of the time — your own content ends up promoting a rival,
unless you already have strong pre-existing authority signals (high
Domain Rating, backlink volume, established AI-mention frequency).
Google has reportedly also begun demoting domains with a pattern of
excessive self-promotional content and adding AI Overview disclaimer
language around "self-proclaimed expert" sources. If you don't already
have strong domain authority, skip self-ranked listicles entirely and
invest in earning a mention in someone else's.

## Structure content for ChatGPT-generated comparison grids (purchase-decision stage)

Per [[ai-shortlist-effect]] (56-participant session study + 6,882-
citation share-of-voice analysis) — a purchase-decision-stage tactic
set distinct from the citation-stage tactics above, since it targets
what happens *inside* the chat once a user is actively comparing
options, not what gets cited on the open web:

- **Getting lifted into ChatGPT's own comparison grid matters more than
  raw mentions.** Comparison/feature grids held user attention in
  35.9%/15% of tasks respectively, more than prose answers — the
  source calls this "the AEO equivalent of owning a featured snippet."
  Structure product/service information (named attributes, consistent
  units, direct feature parity vs. competitors) so a model can render
  it cleanly as a grid row, not just prose.
- **Add a clear "best for X" label**, not just a feature list —
  explicit positioning measurably outperformed an unlabeled comparison
  in the study.
- **Keep pricing current everywhere a model might source it.** Stale or
  wrong pricing measurably hurt selection odds; this is an ongoing
  accuracy-maintenance task (across your own site and any third-party
  pages a model might cite), not a one-time content edit.
- **Disclose downsides plainly instead of omitting or spinning them.**
  Trade-offs stated directly increased user trust in the comparison and
  correlated with being *selected*, not rejected — counterintuitive
  relative to classic marketing instinct to downplay weaknesses.
- **Don't assume unknown brands can't win a slot.** Participants
  considered and picked brands they'd never heard of when positioning
  was clear — familiarity is not a gating factor at the comparison-grid
  stage, only clear framing is.
- **Weight effort by category.** Visibility-to-selection correlation
  ranged from 0.97 (grocery) to -0.98 (coaching, reversed) — in
  commoditized categories, raising share of voice should reliably move
  selection; in highly personal/trust-driven categories, generic
  high-visibility framing may backfire relative to individually-matched
  positioning. Check which kind of category you're in before assuming
  visibility work will pay off here.

## Brand-level visibility factors (correlational, not causally tested)

Per [[ai-visibility-correlation-factors]] — unlike the Tier 1-3 tactics
above, which were causally tested via controlled experiment, these are
**correlations only** (explicitly not causation per the source):

- **Build a YouTube presence.** Of all factors studied, YouTube mentions
  correlated strongest with AI-mention visibility (~0.737) — stronger
  than branded web mentions, backlinks, or Domain Rating.
- **Earn genuine mentions rather than manufacturing content volume.**
  Content volume showed almost no correlation with AI visibility —
  publishing more, by itself, isn't associated with more visibility.
- **If you're a smaller/challenger brand without established authority,
  target ChatGPT specifically.** It shows the weakest correlation with
  pre-existing brand-authority metrics of the three platforms studied —
  AI Mode in particular behaves like a "consensus engine" favoring
  already-known brands, so it's a harder surface to break into without
  existing authority.
- Backlinks and Domain Rating still correlate, but are the *weakest*
  correlates measured (0.19–0.33) — don't expect classic link-building
  alone to move AI visibility much.

## A one-sentence brand-positioning formula (2026-08-20)

Per [[zyppy-seo-strategies-for-ai-search-2026]] — a compact positioning
template for keeping brand facts consistent across owned properties:
**"[Brand] is a [product] for [audience], especially [use case],
because [differentiator]."** This is a shorter, single-sentence
restatement of the same discipline as [[explainable-to-ai-4cs]]'s four
C's (Category≈product, Customer≈audience, Contrast≈differentiator,
plus Consistency as an explicit requirement in both frameworks) — use
whichever phrasing is easier to enforce across a team; they aren't
competing tactics, just two independently-arrived-at versions of "state
your positioning in one unambiguous sentence and repeat it verbatim
everywhere."

## Brand-building LLMO tactics

Per [[ahrefs-llm-optimization]] — brand-level tactics for shaping how
LLMs associate a brand with topics, distinct from the page-level citation
tactics above:

- **Invest in PR aimed at specific topic associations, not just general
  coverage.** LLMs map brand-topic associations via token embeddings and
  cosine similarity in semantic space — a brand that accumulates PR
  mentions tightly clustered around a target topic (the source's example:
  Herman Miller earning 273 pages of "ergonomic" press mentions in a
  year) becomes more likely to be recommended for that topic. Track share
  of voice for target topics, monitor mentions/links, and test LLMs
  directly with focus-topic questions as a measurement loop.
- **Do entity research instead of keyword research.** Identify how LLMs
  currently perceive your brand's entity relationships (via Google's
  Natural Language API, Inlinks' Entity Analyzer, or Ahrefs' AI Content
  Helper), find the gap between current and desired perception, then
  create content specifically to build the missing associations.
- **Claim a Wikipedia listing.** Every major LLM trains on Wikipedia,
  often as its largest single data source. Four requirements gate
  acceptance: **notability** (independent recognition via news/books/
  academic papers), **verifiability** (claims backed by reliable
  third-party sources), **neutral point of view**, and **avoiding
  conflict of interest** (written by brand-impartial contributors, not
  the brand itself) — build edit history and third-party credibility
  before attempting a listing. Reinforces this playbook's existing
  Wikipedia tactic for ChatGPT/Claude targeting above.
- **Research brand-specific questions**, not just topic keywords: pull
  branded "Questions" data (e.g. Ahrefs' Questions tab filtered to
  Brand) and separately type "Is [brand name]..." into ChatGPT/Perplexity
  to observe autocomplete — these prompts differ from Google's
  autocomplete/PAA suggestions and represent a distinct optimization
  target.
- **Invest in genuine Reddit UGC** (community building, AMAs, influencer
  partnerships) rather than link-spamming — Reddit's own S-1 filing
  states its content is "foundational to how leading LLMs have been
  trained," consistent with this wiki's existing Reddit-matters-for-
  Gemini finding.
- **Rate LLM responses (thumbs up/down) on brand-related answers.**
  Corroborates the existing feedback-loop tactic above for static models —
  this source adds that Gemini specifically may not train on prompts/
  responses at all unless a user explicitly opts to share feedback.
- **Don't expect schema markup to be a direct LLM-visibility lever.** The
  source explicitly corrects an earlier claim: AI crawlers read rendered
  HTML, not client-side-rendered content or structured data — schema
  remains valuable for classic rich results and entity clarity, but isn't
  itself read as an LLM-citation signal.

**Corroborating data point**: a Seer Interactive study (10,000 finance/
SaaS purchase-intent queries, GPT-4o-measured brand mentions vs. Google/
Bing SERP rank) found organic ranking correlates with LLM brand mentions
at ~0.65 strength, while **backlinks showed a surprisingly neutral
impact** — consistent with [[airops-fan-out-effect-2026]]'s and
[[ahrefs-why-chatgpt-cites-pages-2026]]'s findings that classic search
ranking is close to a prerequisite for AI citation. See
[[ai-visibility-correlation-factors]]'s Conflicting Evidence section for
how this fits the wiki's unresolved authority-correlation picture.

## Research note: LLM-guided editing using past-ranking context (not yet real-world applicable)

Per [[bardas-white-hat-seo-llm-2025]] (Technion, arXiv 2025-02) — a
different research tradition than the citation-visibility tactics
above: this paper optimizes for classic ad hoc *retrieval* ranking
(LambdaMART, E5 embedding cosine similarity), not LLM-citation
inclusion, but is included here because the method itself is novel and
adjacent. In lab "competitive search" conditions, prompting an LLM
(GPT-4o) to edit a document using examples of **past rankings** for the
same query — best via **Pairwise** (document pairs + which ranked
higher) or **Listwise** (full ranked lists) context — outperformed both
human competitors and a prior supervised feature-based baseline on rank
promotion, while staying reasonably faithful to the original content.

**Why this isn't an actionable tactic yet**: the method requires
*observing past rankings* for your query — available in the paper's
research-lab ranking competitions, not in real-world SEO/AEO, where
competitor rankings and the ranking function are opaque. Per
[[c-seo-bench-2025]], which cites this exact paper: "their method
assumes knowing the user query beforehand, which limits its
applicability to real scenarios, where user queries are unknown." Filed
here as a research-stage signal that LLM-guided, feedback-informed
editing *can* beat both human editors and supervised methods under lab
conditions — worth revisiting if a real-world proxy for "past rankings"
(e.g. your own historical rank-tracking data plus visible competitor
positions) becomes practical to feed into a similar prompting approach.

## Known adversarial risk: LLM recommendation manipulation

Per [[ahrefs-llm-optimization]] (citing a Harvard study, "Manipulating
Large Language Models to Increase Product Visibility") — awareness only,
**not a recommended tactic**: attackers can shift which brand/product an
LLM recommends via adversarial prompt injection embedded in web content
or plugin documentation.

**Correction (2026-07-22), verified against the primary source**: the
original figures cited here ("shifted ranking in ~40% of evaluations";
"raised recommendation rate from 34% to 59.4%") were sourced secondhand
via Ahrefs. Having now ingested the primary paper directly
([[kumar-lakkaraju-manipulating-llms-2024]]), the "34%→59.4%" figure
does **not appear anywhere in it** — likely a misattribution or garbled
restatement in the secondhand source. The verified findings from the
primary paper (Kumar & Lakkaraju, Harvard, arXiv 2404.07981, tested on
Llama-2 with a GCG-optimized "Strategic Text Sequence," fictitious
10-product coffee-machine catalog):

- A near-invisible product (almost never recommended due to high price)
  went from **not appearing at all to the top recommendation within
  ~100 optimization iterations**, and stayed there.
- With a **fixed prompt order**, the attack gave a rank *advantage* in
  only **~40%** of randomized-evaluation trials (~60% no change) — but
  optimizing the attack sequence itself **against randomized product
  order** raised the advantage rate to **~95%**, with disadvantage
  negligible. **Order-robust optimization, not the base attack itself,
  is what makes this reliable.**
- For a product that already ranked competitively (usually 2nd without
  intervention), a fixed-order attack sequence was *no better than
  chance* under randomized order (~15% advantage vs. ~15% disadvantage,
  "neutralizing its overall benefit") — order-robust optimization was
  necessary to get any net benefit at all (~48% advantage).
- **Requires gradient/white-box access** (or reliance on
  cross-model transferability asserted by prior jailbreak literature,
  not independently retested here on production black-box systems) —
  a meaningfully higher technical bar than plain-text prompt injection.

**That "not independently retested on production black-box systems"
gap is now closed**, per [[pfrommer-et-al-ranking-manipulation-conversational-search-2024]]
(EMNLP 2024, UC Berkeley) — a different attack family (tree-of-attacks
jailbreaking, not gradient-optimized strings) but the same underlying
threat model. Attacks crafted against GPT-4 Turbo and hosted on real
webpages transferred successfully to Perplexity's Sonar Large Online
model (a surrogate for perplexity.ai, used since full API access
wasn't available) — a mean ranking-score gain of 54.23% of the maximum
possible gap, with **no white-box/gradient access to Perplexity's
actual closed-source RAG pipeline required**. The same paper also finds
that baseline (non-adversarial) LLM ranking behavior already varies
significantly by model in how much weight it gives product name/brand
vs. document content vs. context position — a reminder that "why did
the LLM rank this product where it did" doesn't have one universal
answer even before considering manipulation.

Practical implication unchanged: monitor how LLMs describe your brand
relative to competitors on a recurring basis (see the
sentiment-monitoring workflow below) — an unexplained shift in
LLM-stated recommendations or sentiment toward a competitor may indicate
this kind of manipulation rather than a genuine organic ranking change.
See [[kumar-lakkaraju-manipulating-llms-2024]] for the full verified
findings.

## Sentiment monitoring and correction

Per [[similarweb-how-to-win-the-race-for-gen-ai-search-2026]] — a
distinct GEO workstream from citation/visibility: being cited isn't
enough if the AI's answer frames the brand negatively, inaccurately, or
as a "budget"/"lower-tier" option, since that shapes user perception
before any click happens. AI answers reflect the tone of the sources
they trust, not an invented judgment.

- **Track sentiment per topic, not just brand-wide** — a brand can read
  positively overall while one specific topic (e.g., a product line or
  use case) carries disproportionately negative framing.
- **Find the root cause before fixing anything**: are review sites
  describing the product inaccurately? Are outdated articles still
  ranking/getting cited? Are competitor comparisons framing the brand
  poorly? Is the brand's own content unclear or missing key information?
- **Fix via two levers, not one**:
  - *On-page*: clarify misunderstood features, correct outdated
    information, directly address the weaknesses users are asking
    about, add explicit positive entity descriptions, include
    structured facts the model can easily reuse.
  - *Off-page*: strengthen or correct the external sources AI relies on
    — fresh expert reviews, updated product comparisons, data-backed
    press mentions, new directory listings, improved UGC, corrected
    Wikipedia/G2/niche-directory entries.
- **Recheck after updates, on a delay.** Sentiment shifts slowly — re-run
  sentiment analysis after content updates, PR improvements, or new
  citations land, rather than expecting an immediate change.

## Query-format AIO risk (which pages to prioritize/audit)

Per [[aio-ctr-impact]], AI Overview trigger rate varies enormously by
query format — prioritize AEO/GEO work on pages targeting these formats,
since they're the most likely to have an AIO inserted above them:

| Query format | AIO trigger rate |
|---|---|
| Comparison ("X vs Y") | 95.4% |
| Review queries | 86.3% |
| Question-format | 85.9% |
| Price/cost/buy queries | 83.4% |
| "Best of" queries | 81.3% |
| "Near me" queries | 76.9% |
| Single-word queries | 27.3% (don't assume short queries are safe) |

Being cited within the AIO on these pages is worth **+120% more clicks**
than not being cited (though still below a no-AIO baseline) — see
[[aio-ctr-impact]] for the full economics.

**Lower-confidence addition**: per
[[singlegrain-google-ai-overviews-ultimate-guide-2025]] (no disclosed
methodology or sample size) — queries of 8+ words are claimed to be 7x
more likely to trigger an AI Overview than shorter queries. Directionally
consistent with [[semrush-ai-overviews-study-2025]]'s finding that
AIO-triggering keywords skew long-tail (~60% at ≤100 monthly searches),
but that's a different axis (search volume, not word count) — treat
this specific 7x figure as unverified rather than corroborated.

## Direct-answer format for AI Overview capture

Per [[singlegrain-google-ai-overviews-ultimate-guide-2025]] (no disclosed
methodology) — lead the page with a **50-70 word direct answer**
immediately after the H1, before any other content, phrased to stand
alone as a self-contained answer to the target query. Consistent with
this page's existing extractable-content/front-loading guidance
elsewhere in the wiki (see [[generative-engine-optimization]]'s
extractability principles), but the specific 50-70 word range isn't
independently verified by any other source in this wiki — treat as a
reasonable starting heuristic, not a measured optimum.

## Measurement checklist: don't panic on CTR alone

Per [[aio-ctr-impact]], a falling CTR on AIO-cited queries can be a
measurement artifact rather than a real problem:

- [ ] Before reacting to a CTR drop, check impressions and clicks
      separately — did clicks actually fall, or did impressions surge
      (meaning you're earning *more* citations, not losing existing ones)?
- [ ] Track organic and paid CTR separately — they respond to AIOs very
      differently and one can look fine while the other looks alarming.
- [ ] Treat single-brand/single-account CTR anomalies with suspicion —
      aggregate benchmarks can be skewed by one outlier account.

## AI-referral traffic and citation-monitoring automation

Per [[sel-integrate-geo-with-seo]] — concrete operational tactics for the
measurement gap noted above (traditional rankings/CTR/traffic don't
capture zero-click AI interactions):

- **Set up a GA4 regex filter to isolate AI-tool referral traffic**
  rather than relying on default channel groupings, which often miscount
  or omit it: `(.*gpt.*|.*chatgpt.*|.*openai.*|.*neeva.*|.*writesonic.*|.*nimble.*|.*outrider.*|.*perplexity.*|.*google.*bard.*|.*bard.*|.*edgeservices.*|.*gemini.*google.*|.*copilot.*)`
  — undisclosed methodology behind this exact pattern, but it's a
  reasonable starting filter to adapt as new AI referrer domains emerge.
  Per [[seoclarity-track-ai-search-traffic]], the UI path to apply a
  filter like this: Reports > Library > "Create Detail Report" off
  Traffic Acquisition, add a Session Source/Medium column, set it as
  default, then apply a "Matches Partial Regex" filter joining AI engine
  names with `|` (that source names ChatGPT, Perplexity, Claude, and
  Gemini but doesn't supply its own regex — use the pattern above).
  Same source reports "some industries" saw AI-referral traffic spikes
  over 700%, with no industry/timeframe specificity — anecdotal, not a
  benchmark.
- **Automate AI-citation/mention checks** rather than manually querying
  each engine — a Google-Sheets-plus-LLM-API workflow (querying a fixed
  prompt set on a schedule and logging whether/how the brand appears) is
  a practical low-effort way to operationalize the presence-per-topic
  tracking already recommended above.
- **Watch branded search volume and direct/returning-visitor traffic as
  a proxy for successful AI-driven discovery** — a brand initially
  discovered via an AI answer often converts to a branded search or
  direct visit rather than a trackable AI referral click, so a rise in
  branded search alongside flat AI-referral numbers can still indicate
  AI-driven awareness working.

## Named GEO metrics (vendor-proposed benchmarks, unverified)

Per [[superlines-geo-guide]] (vendor content-marketing, no disclosed
methodology behind the specific benchmark numbers — use the metric
*names/definitions* as a useful measurement vocabulary, not the
benchmarks as validated targets):

| Metric | Definition | Measurement | Starter benchmark (unverified) |
|---|---|---|---|
| Citation Frequency | How often AI cites your domain | Track across ChatGPT/Perplexity/Gemini/Mistral/Copilot | +10-20% monthly growth for priority prompts |
| AI Brand Visibility | % of answers mentioning your brand | Mentions ÷ total answers × 100 | 15-30% in owned topics after 60-90 days |
| Share of Voice (AI SOV) | Your brand's mentions vs. competitors' | Your mentions ÷ total competitor mentions | Top 3 within core clusters |
| Context Accuracy | Whether AI summaries describe you correctly | Manual review + sentiment/fact checks | >95% accurate on top pages |
| Prompt Coverage | % of tracked prompts where you appear | Appearing prompts ÷ total tracked | 50-70% in priority clusters |
| Assisted Conversions | Revenue influenced by AI exposure | Correlate citation spikes with branded search/pipeline | Show lift vs. baseline |

These overlap conceptually with this wiki's existing measurement
guidance (presence/portability/concentration, citation gap tracking,
AI-referred sessions) — use this table mainly to standardize naming
across a team/report, not as a replacement for the more rigorously
sourced benchmarks elsewhere on this page.

## Technical crawlability (retrieval-eligibility prerequisite)

Per [[how-google-search-works]], none of the tactics above matter if a
page is never crawled, indexed, or served in the first place — this is
the layer beneath E-E-A-T:

- [ ] Is the page accessible to Googlebot — not accidentally blocked by
      `robots.txt`, and not requiring a login to view?
- [ ] If content is rendered via JavaScript, does it still appear when
      rendered with a headless/recent Chrome (i.e., does Google actually
      see it after rendering, not just in the raw HTML)?
- [ ] Is the page linked from somewhere Google can discover (internal
      links, a submitted sitemap), not an orphan page?
- [ ] Is there a clear canonical version if similar/duplicate content
      exists elsewhere, so Google doesn't pick the wrong page as
      canonical or split signals across duplicates?
- [ ] If a page is indexed but never appears in results, check whether
      it's a relevance/quality issue (see E-E-A-T checklist below) or a
      `robots` meta rule blocking serving specifically — these are
      different problems with different fixes.

**AI-crawler-specific version of this check (2026-08-20)**: per
[[zyppy-seo-strategies-for-ai-search-2026]], the same JS-rendering-gap
question needs a separate pass *for AI crawlers specifically*, since
they don't all render JS the way Googlebot does (see
[[vercel-rise-of-the-ai-crawler]]'s confirmed per-bot JS-rendering
differences). The **AI Difference Engine** browser extension (Gray Dot
Co) diffs what an AI crawler sees against what a human browser sees on
the same page — a free, direct way to spot this gap rather than
inferring it from server logs alone. Also audit CDN/firewall-level bot
rules (Cloudflare and similar) separately from `robots.txt` — a
CDN-level block can silently override a permissive `robots.txt` rule,
and the two are commonly managed by different teams.

## E-E-A-T signal-building (retrieval-eligibility foundation)

Per [[e-e-a-t-and-page-quality]], these don't move citation-stage
visibility metrics directly, but they're the retrieval-eligibility
foundation everything above depends on — Trust is the most important
factor, and low-E-E-A-T content risks not being surfaced as a candidate
source at all:

- [ ] Does the page or its author have a real, verifiable "About"/bio
      with genuine credentials or experience for the topic?
- [ ] For YMYL topics (health, finance, government/civics/safety), is
      the content expert-sourced and accurate, not just well-written?
- [ ] Is there independent evidence of trustworthiness (reviews, press,
      citations from others) beyond what the site says about itself?
- [ ] Are there conflicts of interest undisclosed (e.g., a manufacturer's
      own "review" of its product)? Disclose them or avoid the format.

**Critical warning — Scaled Content Abuse**: per
[[e-e-a-t-and-page-quality]], Google explicitly rates pages **Lowest
quality** when generative AI (or any automation) is used to produce many
low-effort, low-value pages — "no matter how it's created," and even
under mere suspicion of the pattern. This isn't just "content volume
doesn't help" (per [[ai-visibility-correlation-factors]]) — scaled,
low-effort AI content is an explicit penalty target. If using AI to help
draft content, ensure each page has genuine added value, editing, and
originality; don't publish AI output at scale with little to no human
curation.

**This risk is now common, not hypothetical**: per
[[ahrefs-b2b-seo-statistics-2025]], 87% of marketers already use AI for
content creation, at roughly 4.7x lower cost and 42% higher publishing
volume than non-AI-using marketers — the exact volume/cost dynamic that
makes Scaled Content Abuse easy to fall into unintentionally. Treat AI
drafting as a starting point requiring genuine editorial work per page,
not a volume lever.

## Know-Simple answer structuring

Per [[search-intent-and-needs-met]], "Know Simple" queries (short,
factual, one-right-answer) get pulled into concise direct-answer
treatments. For any page targeting this kind of query:

- [ ] Is there one clear, complete, correctly-stated 1-2 sentence answer
      to the specific factual question, not buried in a longer narrative?
- [ ] Does that answer appear early/prominently rather than only at the
      end of a long article?

## Domain-specific guidance

Tactic effectiveness varies by content domain/query type — pick the
tactic that matches your content's domain rather than defaulting to the
Tier 1 list blindly:

| Tactic | Works best for |
|---|---|
| Authoritative | Debate-style content, History, Science |
| Fluency Optimization | Business, Science, Health |
| Cite Sources | Factual/statement content, Law & Government |
| Quotation Addition | People & Society, Explanation, History |
| Statistics Addition | Law & Government, Debate, Opinion |

## Checklist for a page you want cited by AI answer engines

- [ ] Does every non-trivial claim have a citation to a credible source?
- [ ] Are there direct quotes from authoritative sources, not just
      paraphrase?
- [ ] Are quantitative stats included instead of vague qualitative claims
      where possible?
- [ ] Is the writing fluent and easy to understand, not just
      keyword-dense?
- [ ] Have you avoided keyword stuffing and unnatural repetition?
- [ ] Does the tone/tactic match the content's domain (see table above)?
