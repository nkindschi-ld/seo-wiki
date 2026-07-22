---
type: source
tags: [seo]
date_published: 2025-02-23
date_ingested: 2026-07-22
origin: raw/studies/bardas-white-hat-seo-llm-2025.pdf
---

# White Hat Search Engine Optimization using Large Language Models (Bardas et al., 2025)

**Citation:** Bardas, Niv; Mordo, Tommy; Kurland, Oren; Tennenholtz,
Moshe; Zur, Gal. "White Hat Search Engine Optimization using Large
Language Models." arXiv:2502.07315v2 [cs.IR], 2025-02-23. Technion.
https://arxiv.org/abs/2502.07315

## What this source is

An academic **competitive search** paper (a different research
tradition than the GEO/AEO citation-visibility literature elsewhere in
this wiki) — it studies document authors competitively modifying their
documents to rank higher under a classic ad hoc **retrieval** ranker
(LambdaMART, or E5-embedding cosine similarity), not an LLM-generated
citation/answer. The novelty is using an LLM (GPT-4o) as the document
*editor*, prompted with examples of past rankings, rather than a
supervised feature-based method.

## Method

Four prompt-context strategies feed an LLM examples of past rankings
for a query, then ask it to edit the candidate document toward a
higher future rank while staying faithful to the original content and
under ~150 words:

- **Pointwise**: shows the query plus the document that ranked highest
  for it in the past (mimic the winner).
- **Pairwise**: shows queries with pairs of documents and which ranked
  higher.
- **Listwise**: shows a full ranked list of documents for past rounds.
- **Temporal**: shows the *same* document's own past versions and how
  its rank changed over time (learn from your own edit history).

192 prompt-configuration variants were tested; **Pairwise** (random
document-pair selection) and **Listwise** were consistently the two
best performers across both datasets and both ranking functions
tested.

## Key findings

- **The LLM-edited documents (bots) outperformed both human students
  and a prior state-of-the-art supervised baseline (SentReplace) on
  rank promotion**, across two independent ranking functions
  (LambdaMART and E5 cosine similarity) and in a live online
  competition where the bots competed against students who didn't know
  they were competing against AI.
- **Faithfulness tradeoff**: the LLM bots' edited documents were less
  faithful to the *original* document (OrigFaith) than human edits or
  SentReplace (which only swaps a single sentence), but still scored
  relatively high (0.57-0.88 depending on setup) — and were often
  *more* faithful to the overall *corpus* (CorpFaith) than SentReplace,
  meaning the LLM's edits stayed within the topical/semantic norms of
  the broader document set even while rewriting more aggressively.
- **In the live online competition** (bots undetected, competing
  against real students, crowdsourced quality/relevance judging):
  Listwise-bot documents were rated *higher quality* than student
  documents on average; Pairwise-bot documents were rated lower quality
  than student documents on average but still valid in 82.2% of cases,
  and both bots produced relevant documents more often than students
  did.
- **Temporal and Pointwise prompting underperformed** Pairwise/Listwise
  — showing a document its own edit history, or just the single best
  past competitor, was less effective than showing it a ranked/paired
  comparison set.

## Real-world applicability caveat — flagged by a later source, not just this one

This method requires **observable past rankings** for the query
(pointwise/pairwise/listwise/temporal context) — a competitive-search
research-lab setup (ranking competitions with disclosed round-by-round
results), not the situation most real-world SEO/AEO practitioners face,
where competitor rankings and the ranking function itself are opaque
and not iteratively disclosed. [[c-seo-bench-2025]] (NeurIPS 2025) cites
this exact paper and notes the same limitation independently: "their
method assumes knowing the user query beforehand, which limits its
applicability to real scenarios, where user queries are unknown."
Treat this as a research-stage technique demonstrating that LLM-guided,
ranking-history-informed editing *can* outperform both humans and
supervised baselines under lab conditions — not yet a deployable
real-world SEO tactic.

## Relationship to existing wiki claims

- **Different research tradition than GEO/AEO citation studies**: this
  paper optimizes for classic ad hoc *retrieval* ranking (LambdaMART,
  E5 cosine), not LLM-generated citation/answer inclusion — closer to
  [[traditional-seo-ranking-factors]]'s subject matter than
  [[ai-citation-landscape]]'s, but using an LLM as the *tool*, which is
  the novel part.
- **Directly discussed and dismissed for real-world use** by
  [[c-seo-bench-2025]] in its related-work section — see that source's
  page for the fuller C-SEO benchmark context this paper sits alongside
  (Nestaas et al. 2025, Kumar & Lakkaraju 2024, Pfrommer et al. 2024 —
  all cited by both papers as adjacent competitive-search/C-SEO
  literature).
- No conflict with existing wiki claims — this is a genuinely new
  method/finding (LLM-as-document-editor using past-ranking context)
  not previously covered.

## See also

- [[c-seo-bench-2025]] — cites and critiques this paper's real-world
  applicability; also the wiki's main C-SEO re-test source.
- [[traditional-seo-ranking-factors]] — the classic-ranking-factor
  literature this paper's target ranking functions (LambdaMART, E5) sit
  within.
- [[geo-content-optimization-tactics]] — brief cross-reference to this
  method as a research-stage note.
- [[mordo-diversification-competitive-search-2025]] — same Technion
  research lab, companion paper studying the ranking-function side
  (diversification as a herding countermeasure) rather than the editing
  side studied here.
