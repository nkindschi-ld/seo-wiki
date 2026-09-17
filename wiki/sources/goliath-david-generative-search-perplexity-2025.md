---
type: source
tags: [aeo]
date_published: 2025-09-17
date_ingested: 2026-09-10
origin: raw/studies/goliath-david-generative-search-perplexity-2025.html
---

# When Content is Goliath and Algorithm is David: The Style and Semantic Effects of Generative Search Engine

Lijia Ma, Juan Qin, Xingchen (Cedric) Xu, Yong Tan. arXiv:2509.14436,
published 2025-09-17.

## Citation

Lijia Ma, Juan Qin, Xingchen (Cedric) Xu, Yong Tan, "When Content is
Goliath and Algorithm is David: The Style and Semantic Effects of
Generative Search Engine," arXiv:2509.14436, 2025.

## Key takeaways

- Large-scale observational study: 4,060 queries, 98,477 unique
  websites, comparing what Google's AI Overview (generative search)
  cites vs. what conventional organic search ranks — roughly 10,000
  sites analyzed in depth across both surfaces.
- **RQ1 — Citation preference:** AI Overview disproportionately cites
  content with **lower perplexity** (i.e., more linguistically
  predictable/"easy for a language model" text) than what conventional
  search ranking prioritizes. A one-standard-deviation decrease in
  perplexity raises citation probability from ~47% to ~56%. Cited
  sources also show substantially higher **semantic homogeneity**
  among each other than conventionally-ranked results do — the AI
  Overview's source set clusters more tightly in meaning than a
  regular SERP's top results.
- **RQ2 — Origin of the preference:** This isn't a Google-specific
  engineering choice — it traces to the underlying LLM architecture
  itself. The authors reproduced the same low-perplexity/semantic-
  homogeneity citation pattern using a RAG pipeline built directly on
  Gemini's API, independent of Google Search's production system. They
  also identified a **positional bias**: content placed near the
  beginning of a document gets preferential consideration by the
  retrieval/generation process.
- **RQ3 — Content-polishing paradox:** LLM-based content refinement
  (rewriting a page to be more fluent/lower-perplexity) was expected by
  the authors to risk homogenizing what AI summaries cite, but instead
  it **increased** information diversity within AI summaries — because
  lowering perplexity expanded the pool of eligible/citable sources
  rather than narrowing it. Polished content saw AI Overview citation
  counts increase by roughly 1-2 additional sources. Two polishing
  approaches were tested: general fluency refinement and citation-
  optimized refinement.
- **RQ4 — User-side effects:** A randomized controlled trial (147
  Prolific participants, policy-recommendation task) found users given
  AI-Overview-style assistance produced submissions with significantly
  higher information diversity. The benefit split by education level:
  graduate-educated users mainly gained *efficiency* (time saved),
  while undergraduate-or-below users gained *quality* improvements —
  the diversity/density benefit was larger for less-educated users.
- Framing: generative search engines optimize for something orthogonal
  to classic SEO's semantic-relevance/authority signals — linguistic
  predictability (perplexity) to the underlying LLM, plus a preference
  for a semantically coherent source set as a whole, not just
  individually relevant documents.
- Practical implication raised by the authors: because the preference
  is intrinsic to the LLM family (not a proprietary ranking layer),
  site owners can offline-test content citability using a RAG pipeline
  built on the same open/accessible model family the target platform
  uses, before publishing.

## What this updated

- New subsection in [[ai-citation-landscape]]: "Perplexity and semantic
  homogeneity as a citation mechanism," adding this alongside the
  existing semantic-relevance (cosine similarity) and retrieval-rank
  findings as another axis of *why* generative engines cite what they
  cite.
- New tactic in [[geo-content-optimization-tactics]]: LLM-based content
  polishing/perplexity reduction, plus reinforcement of front-loading
  core claims (positional bias), cross-linked to the existing
  inverted-pyramid guidance in [[seo-copywriting]].
- No conflicts with existing wiki claims — perplexity/homogeneity is a
  distinct mechanism from the semantic-relevance (cosine similarity)
  and retrieval-rank findings already in [[ai-citation-landscape]] and
  [[airops-fan-out-effect-2026]]; they aren't shown to compete or
  contradict, just to be additional/complementary factors.
