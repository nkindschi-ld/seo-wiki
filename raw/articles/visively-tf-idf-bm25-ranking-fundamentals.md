# How Search Engines Rank Content: Understanding TF-IDF and BM25

**Source:** https://visively.com/kb/algorithms/search-ranking-fundamentals
**Author:** Pedro Dias
**Published:** 2026-08-06
**Length:** ~9,606 words (~13 min read)
**Retrieved:** 2026-08-11

> NOTE: This is a saved summary/extraction of the source article (fetched via
> WebFetch, which returns markdown-converted content). Full verbatim body was
> not preserved; key definitions, data points, and claims are recorded below.

---

## Key Definitions

**Lexical Ranking:** Scores documents by analyzing word presence and
distribution — answering "which documents contain these specific terms most
meaningfully?"

**Term Frequency (TF):** Counts how often query terms appear in a document. A
page mentioning "JavaScript" twenty times suggests stronger topical focus than
one mentioning it once.

**Inverse Document Frequency (IDF):** Weights terms by rarity across the corpus
using logarithmic scaling. Rare terms receive higher weights because they
better distinguish documents.

**TF-IDF:** Multiplies term frequency by inverse document frequency to reward
documents containing query terms frequently while prioritizing rare,
discriminative terms.

**BM25:** The practical evolution of TF-IDF, adopted as default by
Elasticsearch, Solr, and Lucene (2016). Incorporates two key refinements over
raw TF-IDF (term saturation and document-length normalization).

---

## Core Technical Claims

**Term Saturation in BM25:** Contributions from additional term occurrences
diminish as counts increase. With typical k₁ value of 1.2:

- 1 occurrence = baseline
- 5 occurrences ≈ 1.8× contribution
- 20 occurrences ≈ 2.1× contribution
- 100 occurrences ≈ 2.2× contribution (approaching maximum)

This saturation function explains why keyword stuffing provides minimal ranking
gains.

**Document Length Normalization:** BM25's b parameter (typically ~0.75) adjusts
scores based on document length relative to corpus average. Shorter, focused
documents can compete effectively with longer, comprehensive ones.

**Inverted Index Structure:** Rather than mapping "documents→terms," inverted
indexes map "terms→documents," enabling fast query processing by storing
pre-computed document lists for each term.

---

## IDF Example (10 Million Web Pages)

- "the" (9.9M documents) = very low IDF
- "website" (2M documents) = low IDF
- "JavaScript" (500K documents) = moderate IDF
- "WebAssembly" (50K documents) = high IDF
- "Binaryen" (5K documents) = very high IDF

---

## What TF-IDF Rewards vs. Misses

**Rewards:**
- Consistent use of target terminology
- Domain-specific vocabulary
- Terms that differentiate content

**Misses:**
- Synonyms and related concepts
- Query intent
- Semantic relationships (context-dependent meanings)

---

## Why Lexical Signals Still Matter

Semantic search handles vocabulary mismatches but struggles with product
identifiers, technical specifications, brand names, and domain-specific
terminology. Modern systems employ "hybrid retrieval" — running lexical (BM25)
and semantic search in parallel, merging results through rank fusion.

Semantic embeddings may treat "iPhone 15 Pro Max 256GB" as generic smartphone
content. Lexical matching locates exact specifications.

---

## Content Recommendations

1. **Terminology Consistency:** Use canonical terms throughout rather than
   varying synonyms. "Crawl budget" accumulates higher frequency than switching
   between "crawl allocation" and "crawler resources."
2. **Include Specific Identifiers:** Incorporate product model numbers, software
   versions, technical specifications, and proper nouns rather than generic
   descriptions.
3. **Balance Comprehensiveness with Focus:** Structure separate pages for
   distinct subtopics rather than cramming everything into one lengthy document.
   BM25 rewards term concentration.
4. **Multi-Signal Optimization:** BM25 mechanics determine term weighting, not
   overall ranking. Content quality, authority, freshness, and semantic
   relevance matter equally.
5. **Avoid Keyword Stuffing:** Modern search maintains explicit spam detection
   alongside saturation functions making unnatural repetition ineffective.

---

## FAQ Highlights

**Keyword Density:** Largely irrelevant due to BM25 saturation. Focus on
natural, thorough coverage rather than targeting density percentages.

**Phrase Matching:** Standard BM25 treats queries as word bags. Many systems add
phrase matching as separate boosts rewarding adjacent or nearby query terms.

**AI Search vs. Traditional Search:** Same principles apply. RAG systems use
BM25 within hybrid retrieval architectures.
