---
type: source
tags: [aeo]
date_published: 2026-07-01
date_ingested: 2026-09-10
origin: raw/studies/spotify-llm-search-eval-behavioral-grounding-2026.html
---

# As It Was: Aligning LLM Search Evaluation with Historical User Preferences

Vardasbi, Penha, Palumbo, Hauff, Bouchard, Lalmas (Spotify Research).
SIGIR '26 (49th ACM SIGIR Conference), published 2026-07-01.
arXiv:2607.01040.

## Citation

Ali Vardasbi et al., "As It Was: Aligning LLM Search Evaluation with
Historical User Preferences," SIGIR '26.

## Key takeaways

- Semantic-only LLM judges (evaluating search-result relevance by
  reasoning alone) diverge from actual user behavior most on ambiguous
  queries — underspecified lyric fragments, regional terms, queries
  with multiple valid interpretations.
- Proposes "QRI cards" (Query–Relevance–Impressions): compact summaries
  of how users historically engaged with similar past queries and
  results, built from the prior month's search logs, debiased with
  inverse propensity weighting to correct position bias. Capped to the
  top-10 most similar historical queries per item (by cosine
  similarity) to bound prompt length, and near-duplicate queries
  (>0.9 similarity) are excluded to prevent evaluation leakage.
- Feeding QRI cards into the LLM judge's prompt (same rubric, same
  base prompt — only the added behavioral evidence differs) improved
  Spearman correlation with true relevance by ~5% overall on 5,965
  music-search SERPs, jumping to +91% relative improvement specifically
  on cases where the plain and grounded judges disagreed ("flipped
  instances"). A held-out human-judged multilingual set (265 SERPs,
  5 languages) showed +15%.
- In production A/B tests, the behavior-grounded judge picked the
  correct live-test winner (sign alignment) 36.8% of the time vs.
  30.6% for the plain semantic judge, and converged faster/more
  reliably as behavioral evidence accumulated.
- Three mechanisms identified for how grounding helps: (1) resolving
  ambiguity by showing which entities users actually engaged with for
  similar past queries, (2) calibrating penalty severity — stricter
  when users strongly preferred a now-missing result, more lenient
  when related content was historically accepted as a substitute, and
  (3) increasing ranking sensitivity by comparing QRI evidence strength
  across multiple plausible results.
- Limitations acknowledged by the authors: absolute alignment remains
  moderate (a real gap to human agreement persists), the approach is
  weaker in cold-start/long-tail queries with sparse behavioral
  history, and there's an open risk of the LLM judge amplifying
  residual biases already present in the interaction logs it's
  grounded on.

## What this updated

- New concept page: [[llm-as-judge-behavioral-grounding]].
- Cross-linked from [[ai-citation-landscape]] and
  [[geo-content-optimization-tactics]] as background on how AI/search
  systems can evaluate relevance using behavioral signals, not as a
  citation-visibility tactic itself.
- No conflicts with existing wiki claims — this is a new methodological
  axis (how relevance gets *judged*), not a claim about how to *win*
  citations.
