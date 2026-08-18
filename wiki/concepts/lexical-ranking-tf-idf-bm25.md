---
type: concept
tags: [seo, aeo]
updated: 2026-08-11
---

# Lexical Ranking: TF-IDF and BM25

The scoring mechanics beneath "text relevance" — how search engines and
retrieval systems score a document by the *words it contains and their
distribution*, before (or alongside) any semantic/embedding understanding.
This is the mechanistic layer under [[traditional-seo-ranking-factors]]'
finding that text relevance is the single strongest classic-SERP correlate,
and it underpins the retrieval stage of [[how-google-search-works]] and the
hybrid retrieval used by AI/RAG systems ([[generative-engine-optimization]]).
Based on [[visively-tf-idf-bm25-search-ranking-fundamentals]] (Pedro Dias,
ex-Google Search).

## Lexical vs. semantic ranking

**Lexical ranking** scores documents by analyzing word presence and
distribution — answering *"which documents contain these specific terms most
meaningfully?"* It is distinct from **semantic search**
([[entity-oriented-search-fundamentals]]), which interprets meaning, intent,
and concept relationships via embeddings. Modern systems run both in parallel
(see Hybrid retrieval below).

## The building blocks

### Term Frequency (TF)
How often query terms appear in a document. A page mentioning "JavaScript"
twenty times signals stronger topical focus than one mentioning it once — but
this relationship is *not* linear (see term saturation).

### Inverse Document Frequency (IDF)
Weights terms by **rarity across the corpus**, using logarithmic scaling. Rare
terms carry higher weight because they better distinguish documents. Illustrative
scale over ~10M web pages:

| Term | Documents containing it | IDF weight |
|---|---|---|
| "the" | 9.9M | very low |
| "website" | 2M | low |
| "JavaScript" | 500K | moderate |
| "WebAssembly" | 50K | high |
| "Binaryen" | 5K | very high |

### TF-IDF
Multiplies TF by IDF: reward documents that use query terms frequently, while
prioritizing rare, discriminative terms over common ones. Common function words
("the", "a") contribute almost nothing; distinctive domain vocabulary
contributes the most.

### BM25
The practical evolution of TF-IDF and the **default ranking function in
Elasticsearch, Solr, and Lucene since 2016**. It adds two refinements that raw
TF-IDF lacks:

1. **Term saturation** — diminishing returns on repeated terms.
2. **Document-length normalization** — adjusting for how long the document is.

## Term saturation — why keyword stuffing fails

BM25's `k₁` parameter (typically **~1.2**) makes each additional occurrence of a
term contribute less than the last. Contribution as occurrences rise:

| Occurrences | Relative contribution |
|---|---|
| 1 | baseline (1×) |
| 5 | ≈ 1.8× |
| 20 | ≈ 2.1× |
| 100 | ≈ 2.2× (approaching the ceiling) |

The curve flattens hard: going from 1 → 5 mentions buys most of the available
gain; 20 → 100 buys almost nothing. **This is the mechanistic explanation for
why keyword stuffing doesn't work** — the math itself caps the payoff, and
modern engines layer explicit spam detection on top. It also means **keyword
density percentages are largely irrelevant** as an optimization target.

## Document-length normalization

BM25's `b` parameter (typically **~0.75**) scales scores by document length
relative to the corpus average, so long documents don't win on raw term counts
alone. Consequence: **shorter, focused documents can outrank longer,
comprehensive ones.** This is the retrieval-mechanics counterpart to
[[airops-fan-out-effect-2026]]'s empirical "focus beats comprehensive coverage"
citation finding, and it supports the wiki's page-per-subtopic structuring
guidance.

## Inverted index

Retrieval systems store the corpus as an **inverted index** — mapping
*terms → documents* (a pre-computed list of documents for each term) rather than
*documents → terms*. This is what makes term-based lookup fast at web scale, and
it's why term presence is the entry ticket to being *retrievable* at all.

## What lexical ranking rewards vs. misses

**Rewards:**
- Consistent use of target terminology
- Domain-specific vocabulary
- Terms that differentiate the content from the corpus

**Misses:**
- Synonyms and related concepts
- Query intent
- Semantic relationships / context-dependent meanings (e.g. "bank")

The "misses" column is exactly what semantic/entity-oriented search
([[entity-oriented-search-fundamentals]]) exists to cover.

## Hybrid retrieval — why lexical still matters in the AI era

Semantic embeddings handle vocabulary mismatch and intent, but degrade on
**product identifiers, technical specifications, brand names, and
domain-specific terminology** — an embedding may treat "iPhone 15 Pro Max
256GB" as generic smartphone content, whereas lexical matching locates the exact
spec. So modern systems (including **RAG pipelines behind AI search**) use
**hybrid retrieval**: run BM25 and semantic search in parallel and merge results
via **rank fusion**. Per the source, the same principles apply to AI search as
to traditional search — BM25 lives *inside* the retrieval stage that feeds LLM
answers, which is why lexical precision is still a GEO/AEO concern, not just a
classic-SEO one.

Some systems also add **phrase matching** as a separate boost on top of the
default word-bag model, rewarding query terms that appear adjacent or near each
other.

## Practical implications

See [[geo-content-optimization-tactics]] and
[[classic-seo-ranking-factors]] for the actionable tactics. In brief, the
mechanics above justify:

- **Terminology consistency** — pick one canonical term and repeat it rather
  than rotating synonyms ("crawl budget" throughout, not alternating with "crawl
  allocation" / "crawler resources"), so TF accumulates on the term you want to
  rank for.
- **Include specific identifiers** — model numbers, software versions, specs,
  proper nouns; these are high-IDF, hard for embeddings to match, and the exact
  case where lexical retrieval carries the load.
- **Focus over comprehensiveness** — separate pages per distinct subtopic beat
  one sprawling document, because length normalization + term saturation reward
  concentration.
- **Don't chase keyword density / don't stuff** — saturation caps the gain and
  spam detection penalizes the attempt.
- **Treat BM25 as one signal** — it determines *term weighting*, not overall
  ranking; quality, authority, freshness, and semantic relevance matter
  alongside it.

## See also

- [[how-google-search-works]] — BM25 operates in the serving/retrieval stage of
  the crawl→index→serve pipeline.
- [[traditional-seo-ranking-factors]] — the empirical correlation study whose
  "text relevance is strongest" finding this page mechanistically explains.
- [[entity-oriented-search-fundamentals]] — the semantic/entity layer that
  covers what lexical ranking misses; the other half of hybrid retrieval.
- [[generative-engine-optimization]] — AI/RAG answers are fed by hybrid
  retrieval that includes BM25.
- [[ai-search-reranking-pipeline]] — what happens *after* the BM25+vector merge:
  the reranker that re-scores passages before generation.
- [[geo-content-optimization-tactics]] / [[classic-seo-ranking-factors]] — the
  actionable tactics grounded in these mechanics.
