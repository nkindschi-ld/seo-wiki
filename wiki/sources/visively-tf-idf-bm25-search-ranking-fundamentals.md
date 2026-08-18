---
type: source
tags: [seo, aeo]
date_published: 2026-08-06
date_ingested: 2026-08-11
origin: raw/articles/visively-tf-idf-bm25-ranking-fundamentals.md
---

# How Search Engines Rank Content: Understanding TF-IDF and BM25

**Citation:** Pedro Dias, "How Search Engines Rank Content: Understanding
TF-IDF and BM25," Visively Knowledge Base, 2026-08-06.
https://visively.com/kb/algorithms/search-ranking-fundamentals

A foundational, high-rigor technical explainer of **lexical ranking** — the
TF-IDF and BM25 scoring math that sits under "text relevance." Authored by
Pedro Dias, an ex-Google Search / Search Relations figure, which makes it a
credible mechanics reference rather than vendor marketing. Notable because the
wiki previously had the *empirical* text-relevance finding
([[semrush-ranking-factors-study-2024]]) but no page on the *scoring
mechanism* behind it.

## Key takeaways

- **Lexical ranking** scores documents by word presence/distribution;
  **TF-IDF** = term frequency × inverse (log-scaled) document frequency, so rare
  discriminative terms outweigh common ones.
- **BM25** is TF-IDF's practical successor — default in Elasticsearch, Solr,
  Lucene since **2016** — adding **term saturation** (`k₁`≈1.2: 1→baseline,
  5→~1.8×, 20→~2.1×, 100→~2.2× ceiling) and **length normalization** (`b`≈0.75,
  letting short focused docs beat long ones).
- **Keyword stuffing / keyword density** is mechanistically futile: saturation
  caps repeated-term payoff, and explicit spam detection sits on top.
- **Inverted index** (terms→documents) is the retrieval data structure.
- Lexical ranking **rewards** terminology consistency, domain vocabulary, and
  discriminative terms; it **misses** synonyms, intent, and context-dependent
  meaning — the gap semantic/entity search fills.
- **Hybrid retrieval**: BM25 + semantic embeddings run in parallel and merge via
  **rank fusion**; lexical carries product IDs / versions / specs / brand names
  that embeddings blur ("iPhone 15 Pro Max 256GB").
- **Applies to AI search too** — RAG systems use BM25 inside hybrid retrieval,
  so lexical precision is a GEO/AEO concern, not just classic SEO.
- Content recommendations: canonical terminology, include specific identifiers,
  focus over comprehensiveness (page-per-subtopic), treat BM25 as one signal
  among quality/authority/freshness/semantics, and don't stuff.

## Which wiki pages this updated

- Created concept [[lexical-ranking-tf-idf-bm25]] (new; the mechanics page).
- Added supporting citation to [[traditional-seo-ranking-factors]] (mechanistic
  "why" under the strongest-correlate text-relevance finding).
- Added supporting citation to [[geo-content-optimization-tactics]]
  (terminology-consistency / specific-identifiers tactics now have a lexical
  "why"; corroborates focus-beats-comprehensive).

## Assessment

High rigor for an explainer: correct, standard IR mechanics with realistic
parameter values, authored by a credible ex-Google source, and explicit about
scope (BM25 is one signal, not the whole ranking system). No conflicts with
existing wiki claims — corroborates and mechanistically grounds them.
