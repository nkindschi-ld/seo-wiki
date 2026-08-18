# Rerankers for GEO/AEO: How AI Search Chooses Passages and Sources

**Source:** https://peec.ai/blog/rerankers-for-geo-aeo-how-ai-search-chooses-passages-and-sources
**Author:** Metehan Yesilyurt (Peec AI)
**Published:** 2026-08-06
**Retrieved:** 2026-08-12

> NOTE: Saved summary/extraction (fetched via WebFetch, markdown-converted).
> Full verbatim body not preserved; mechanisms, models, findings below.

---

## Core argument

AI search operates through distinct stages — discovery, passage selection,
source selection, answer generation — not a single ranking decision. A
**reranker** is the filtering mechanism between retrieval and generation: it
scores candidate passages against the query and assigns relevance scores.

## The AI search pipeline

1. **Query planning** — splits the user question into multiple searches
   (fanout).
2. **Retrieval** — keyword matching (BM25) + vector search (embeddings), merged
   via **Reciprocal Rank Fusion (RRF)**.
3. **Reranking** — re-scores candidates using neural models.
4. **Generation** — produces answers and citations.

## Bi-encoder vs. cross-encoder

- **Bi-encoders**: encode query and document separately into vectors; fast
  (pre-computable) but lose precision through early compression.
- **Cross-encoders**: read query and passage together; fine-grained interaction
  but require full computation per pair.

## Model families

- **BERT-based (MS MARCO-trained)**: MiniLM-L6 (23M params), MiniLM-L12 (33M) —
  production workhorses; ~24% attention allocated to punctuation/structural
  tokens (attention-visualization artifact risk).
- **BGE-reranker-v2-m3**: 100+ languages via XLM-RoBERTa backbone.
- **ModernBERT**: 8,192-token context (vs. 512 for original BERT).
- **Qwen3-Reranker (0.6B/4B/8B)**: LLM-based rerankers, accept instructions,
  32,000-token inputs.
- **SPLADE**: decomposes scores into exact term-level contributions
  (interpretable vocabulary expansion).
- **ColBERT**: token-to-token matching via MaxSim (shows which query words find
  strong document partners).

## Critical measurement finding

Query "what are the best aeo tools": a descriptive product passage scored
near-zero from strict MS MARCO models (MiniLM-L6: 0.12%, BGE-large: 0.20%),
while a direct shortlist listing tools scored **>99.9%** across the same models.
The **Ettin model (ModernBERT lineage) reversed this** — rating the descriptive
passage 99.9% relevant. Takeaway: single-model scores mislead without
cross-family validation.

## Operational insights

- **Why listicles perform well**: answer-shape alignment, not universal
  formatting preference. Listicles contain extractable answers, named entities,
  and coverage of multiple query variants.
- **Passage-level retrieval reality**: strong pages can contain weak passages;
  weaker-authority pages may contain clearer extractable answers. Page-level
  metrics alone can't explain citation outcomes.
- **Attention as unreliable evidence**: attention heatmaps partly reflect
  artifacts; exact term contributions and token alignments are stronger
  diagnostics.

## Content strategy recommendations

- **Answer-first structure**: each section targeting a query needs one
  direct-answer sentence in the first two lines, then supporting evidence and
  context.
- **Answer shape by intent**:
  - Definitions → concise entity description with distinguishing facts.
  - Selection queries → named options with inclusion criteria and trade-offs.
  - Comparisons → like-for-like criteria applied to all options.
  - Procedures → ordered steps with prerequisites and exceptions.
- **Local self-containment**: content should be comprehensible within any
  plausible retrieval window — explicit naming rather than pronouns, answers
  kept adjacent to supporting claims.

## Diagnostic framework (failure-stage classification)

- **No retrieval** → indexing, coverage, authority, or freshness problems.
- **Retrieved but losing** → answer-shape or passage-relevance issues.
- **Strong passage, no citation** → source quality, diversity, or
  generation-stage behavior.

## Model selection guide

| Use case | Recommended model |
|---|---|
| Explainability | SPLADE (term-level decomposition) |
| Query-word coverage analysis | ColBERT (token alignment visibility) |
| Best accuracy (compute available) | Qwen3-Reranker 4B/8B |
| High-volume, CPU scoring | ms-marco-MiniLM-L-6-v2 |
| Multilingual content | BGE-reranker-v2-m3 |
| Long documents | Ettin/ModernBERT family |

## Reporting framework

Separate metrics by retrieval exposure, candidate strength, and final citation
rate rather than collapsing into one visibility score. Segment by query intent
(brand, definition, comparison, selection, procedural). Specify model version,
query set, locale, date, and passage-window size for reproducibility.

## What remains unconfirmed

OpenAI's File Search documentation confirms a hybrid-retrieval-plus-reranking
architecture, but the specific open-source models used internally by ChatGPT,
Google AI Overviews, or Perplexity are **undisclosed**. BGE and MiniLM are
useful open baselines without evidence of proprietary adoption.
