---
type: concept
tags: [aeo, seo]
updated: 2026-11-06
---

# AI Search Retrieval Pipeline & Rerankers

How an AI-search engine gets from a user question to a cited answer — the
**multi-stage pipeline** (discovery → passage selection → source selection →
generation) and the **reranker** that sits between retrieval and generation and
decides which passages are relevant enough to feed the model. This is the
mechanism layer that connects several things the wiki already documents
separately: query fanout ([[peec-ai-chatgpt-query-fanouts-2026]]), hybrid
BM25+vector retrieval ([[lexical-ranking-tf-idf-bm25]]), retrieval-rank
dominance ([[airops-fan-out-effect-2026]]), and chunk-level "Fraggle" citation
([[ipullrank-optimize-for-sge]]). Based on [[peec-ai-rerankers-geo-aeo-2026]]
(Metehan Yesilyurt, Peec AI).

## The pipeline is not one ranking decision

AI search runs as **distinct stages**, each a separate failure point:

1. **Query planning / fanout** — the engine splits the user question into
   multiple sub-searches (see [[peec-ai-chatgpt-query-fanouts-2026]] for the
   fanout data and injected terms).
2. **Engine selection** — before any relevance scoring, the engine picks
   *which index* to query. ChatGPT dispatches across a registry of ~69 named
   vertical engines (Wikipedia, arXiv, Reddit, news-by-recency-window, legal,
   medical, finance, local, PDF, YouTube, images) plus multiple external
   backends (Bing, SerpAPI, Microsoft MAI grounding) — see
   [[chatgpt-vertical-retrieval-engines]]. Content format and topic are a
   **routing** decision here, not just a ranking signal later.
3. **Retrieval** — **hybrid**: keyword matching (**BM25**,
   [[lexical-ranking-tf-idf-bm25]]) + vector/embedding search, run in parallel
   and merged via **Reciprocal Rank Fusion (RRF)**.
4. **Reranking** — a neural model **re-scores** the retrieved candidate passages
   against the query, producing the ordering that actually matters.
5. **Generation** — the model writes the answer and picks citations from the
   top-reranked passages.

The practical upshot: "getting retrieved" and "getting cited" are different
events separated by the reranker. This is the mechanism *underneath*
[[airops-fan-out-effect-2026]]'s finding that retrieval rank dominates citation
— the reranker is what assigns that rank.

## What a reranker is

A **reranker** takes the candidate passages from retrieval and assigns each a
relevance score against the query. Two architectures:

- **Bi-encoder** — encodes query and document *separately* into vectors. Fast
  (document vectors can be pre-computed) but loses precision through early
  compression. This is typically the *retrieval* stage.
- **Cross-encoder** — reads query and passage *together*, allowing fine-grained
  token interaction; more precise but must be computed per query–passage pair.
  This is typically the *reranking* stage.

### Model families (open-source baselines)

The engines' *own* rerankers are undisclosed (see Caveats), but the open
landscape shows the range:

| Model | Notable trait |
|---|---|
| MS MARCO MiniLM-L6 (23M) / L12 (33M) | Production workhorses; strict; ~24% attention on punctuation/structural tokens |
| BGE-reranker-v2-m3 | 100+ languages (XLM-RoBERTa backbone) |
| ModernBERT / Ettin | 8,192-token context (vs. 512 for original BERT) — long documents |
| Qwen3-Reranker (0.6B/4B/8B) | LLM-based; accepts instructions; 32,000-token inputs |
| SPLADE | Interpretable — decomposes score into exact term-level contributions |
| ColBERT | Token-to-token MaxSim — shows which query words find strong partners |

## Models disagree — the cross-family validation finding

The single most important empirical point: **different reranker families score
the same passage very differently.** For the query "what are the best aeo
tools":

- A **direct shortlist** listing tools scored **>99.9%** across strict MS MARCO
  models (MiniLM-L6, BGE-large).
- A **descriptive product passage** scored **near-zero** on those same models
  (0.12%, 0.20%)…
- …but **99.9%** on the Ettin (ModernBERT-lineage) model.

So a passage that looks irrelevant to one reranker family looks perfect to
another. **Any single-model "relevance score" is unreliable** — validate across
model families, and don't optimize to one tool's number. It also means real
engines (which use undisclosed rerankers) can diverge from each other for
architectural reasons alone, independent of authority or content quality.

## Why listicles win, mechanistically

Listicles perform well because of **answer-shape alignment, not a universal
formatting preference**: a listicle contains extractable answers, named
entities, and coverage of multiple query variants — exactly the shape a
reranker scores highly for a "best/selection" query. This complements (doesn't
replace) the **fanout-injection** mechanism in [[listicles-in-ai-search]]: fanout
explains why the engine *searches* for listicle-shaped sub-queries; the
reranker explains why listicle-shaped *passages* then win the relevance score.
Two stages, two mechanisms, same outcome.

## Candidate page selection: a page-level gate before passage scoring

*(Added 2026-10-05 from Lumar's GEO series: [[lumar-candidate-page-selection]],
[[lumar-semantic-relevance-three-jobs]]. These are framework pieces with no
data.)*

Inside the retrieval stage (3), a **page-level** decision comes before the
passage-level work. Is this page a plausible source for this query at all?
Scoring every passage of every indexed page isn't practical, so the system
first narrows the pool with page-level signals:

- **Lexical:** exact or near-exact query terms in the title, H1, headings and
  anchor text (the BM25 side, [[lexical-ranking-tf-idf-bm25]]).
- **Semantic "aboutness":** is the page genuinely about the topic, or does it
  only mention it?
- **Authority:** applied as a query-dependent filter, a hard gate for YMYL
  (see [[authority-in-generative-search]]).
- **Freshness:** query-dependent. ChatGPT runs it as separate news-recency
  *engines* ([[chatgpt-vertical-retrieval-engines]]), which is an even
  earlier version of the same idea.

Candidacy is **query-dependent**. A general car blog can be a candidate for
"how oil changes work" and never for "Honda Civic oil drain torque." Classic
rank-tracking tools can't see this stage: a page can rank and still never
enter the pool.

### Semantic relevance has three jobs

Lumar's split of "relevance" across stages, which sharpens the "don't trust
one relevance score" advice below:

| Stage | Question | What it optimizes |
|---|---|---|
| Candidate selection | Is this page about the query? | Topical clarity |
| Chunk retrieval (stages 3–4) | Which passage best answers it? | Answer match: entities, units, exact phrasing, steps |
| Citation (stage 5) | Is this chunk safe and precise enough to cite? | Self-contained facts ([[chunkability]]) |

A page can pass one stage and fail the next. It can be clearly on-topic with
no precise passage, or have a precise passage that doesn't stand alone. A
single page-level similarity score hides which stage failed.

## Passage-level, not page-level

The reranker scores **passages**, so:

- **Strong pages can contain weak passages**, and **weaker-authority pages can
  contain the single clearest extractable answer** and win the citation.
- **Page-level metrics alone cannot explain citation outcomes.**
- **Measured at the sentence level**: [[dejan-grounding-snippets-2026]]
  finds query-focused sentence scoring (replicated with a `deberta-v3-large`
  cross-encoder), with the #1 source taking the largest share of a fixed
  snippet budget — see [[grounding-snippets]].

This is the retrieval-mechanics grounding for the wiki's chunk-level "Fraggle"
guidance ([[ipullrank-optimize-for-sge]], and the "focus over comprehensiveness"
finding in [[airops-fan-out-effect-2026]] / the length-normalization mechanic in
[[lexical-ranking-tf-idf-bm25]]).

## Diagnostic framework: classify the failure by stage

Because the pipeline is staged, a visibility problem has a *locatable* cause:

- **Not retrieved at all** → indexing, coverage, authority, or freshness
  problem (fix crawlability/retrieval eligibility — see
  [[how-google-search-works]]).
  Includes failing **candidate page selection** (page topic unclear, title
  and H1 not aligned with the query, or filtered out on authority for a
  YMYL query). See the section above.
- **Never routed to your content's engine** → an *engine-selection* failure that
  precedes retrieval entirely. A PDF or video asset unreachable at the user's
  reasoning tier, or a business absent from Yelp/Foursquare, loses before BM25
  runs. See [[chatgpt-vertical-retrieval-engines]].
- **Retrieved but losing the rerank** → answer-shape or passage-relevance
  problem (fix the passage: answer-first, self-contained).
- **Strong passage but not cited** → source-quality, source-diversity, or
  generation-stage behavior (a source-selection issue, not a passage issue).

## Practical implications

Actionable tactics live in [[geo-content-optimization-tactics]]; in brief, the
reranker mechanics justify:

- **Answer-first passages** — one direct-answer sentence in the first two lines
  of each query-targeted section, then evidence/context.
- **Answer shape matched to query intent** — definition → concise entity
  description; selection → named options + inclusion criteria + trade-offs;
  comparison → like-for-like criteria across all options; procedure → ordered
  steps with prerequisites/exceptions.
- **Local self-containment** — each passage must make sense inside any plausible
  retrieval window: explicit names not pronouns, answers adjacent to their
  supporting claims.
- **Don't trust one relevance score** — validate content across reranker
  families; treat any single tool's % as directional.

## Caveats

- The **specific rerankers used by ChatGPT, Google AI Overviews, and Perplexity
  are undisclosed.** OpenAI's File Search docs confirm the *architecture*
  (hybrid retrieval + reranking); BGE/MiniLM are open baselines, not confirmed
  production models. Treat named models as *illustrative of the mechanism*, not
  as the engines' actual stack.
- **Attention heatmaps are weak evidence** — MS MARCO models spend ~24% of
  attention on punctuation/structural tokens, so attention-visualization
  "insights" are partly artifact. Exact term contributions (SPLADE) and token
  alignments (ColBERT) are stronger diagnostics.

## Conflicting Evidence

- **Claim:** pages that cover several unrelated subjects are weaker
  candidates for AI retrieval, so a page should keep one clear topic.
  - Supported by: [[lumar-candidate-page-selection]] (2026-08-12) and
    [[lumar-semantic-relevance-three-jobs]] (2026-08-21), both vendor
    frameworks with no data. Partial empirical support from
    [[airops-fan-out-effect-2026]]: pages covering 26–50% of fan-out
    subtopics out-cite 100%-coverage pages when relevance is held constant.
    That measures breadth *within* one topic, not unrelated subjects.
  - Contradicted by: [[google-ai-optimization-guide]] (2026-06, official).
    "Google systems are able to understand the nuance of multiple topics on
    a page and show the relevant piece to users."
- **Current best guess:** unresolved. Google's statement is official, but it
  covers Google's own systems, and the claim is that it can *extract* the
  relevant passage from a multi-topic page. It doesn't say multi-topic pages
  are equally likely to be *selected as candidates*. Lumar's claim is
  engine-agnostic and unmeasured. The AirOps data favors focus, but on a
  different variable. Practical leaning: keep one clear primary topic per
  page anyway (it costs little and helps lexical matching on title and H1),
  but don't split working multi-topic pages purely for AI on Google
  surfaces. Needs a direct test, e.g. citation rates for single-topic vs.
  multi-topic pages with matched passages.

## See also

- [[geo-diagnostic-checklist]] — the page-level triage playbook that
  operationalizes this failure-stage diagnostic into per-page checks.
- [[chatgpt-vertical-retrieval-engines]] — the engine-selection substage added
  above: which index the hybrid retrieval actually runs against, and why a
  dedicated retrieval path is not evidence of citation value.
- [[peec-ai-chatgpt-query-fanouts-2026]] — the query-planning/fanout stage that
  feeds retrieval, and the RRF mechanism named here.
- [[lexical-ranking-tf-idf-bm25]] — the BM25 half of hybrid retrieval that
  precedes reranking.
- [[airops-fan-out-effect-2026]] — the empirical retrieval-rank-dominates-
  citation finding this pipeline mechanistically explains.
- [[listicles-in-ai-search]] — the fanout-injection mechanism this page's
  answer-shape mechanism complements.
- [[generative-engine-optimization]] — the umbrella concept; "retrieval
  eligibility" is stage 1–2 of this pipeline.
- [[geo-content-optimization-tactics]] — the actionable answer-shape /
  self-containment / diagnostic tactics.
- [[chunkability]] — the passage-level "can this chunk stand alone?" property
  that the citation-stage relevance job depends on.
- [[authority-in-generative-search]] — authority as a query-dependent filter at
  candidate selection, a hard gate for YMYL.
- [[lumar-candidate-page-selection]] and
  [[lumar-semantic-relevance-three-jobs]] — sources for the candidate-selection
  section and the three-jobs table.
- [[query-fanout]] — overview of stage 1 (query planning/fanout): Google's confirmation, injected terms, and the textless-fanout research.
- [[grounding-snippets]] — what survives after reranking: sentence-level extracts from a ~2,000-word per-query budget, split by rank.
