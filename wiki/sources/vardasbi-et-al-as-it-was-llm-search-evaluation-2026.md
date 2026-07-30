---
type: source
tags: [aeo]
date_published: 2026-07-01
date_ingested: 2026-07-23
origin: raw/articles/vardasbi-et-al-as-it-was-llm-search-evaluation-2026.md
---

# As It Was: Aligning LLM Search Evaluation with Historical User Preferences (Vardasbi et al., Spotify, SIGIR '26)

**Citation:** Vardasbi, Ali; Penha, Gustavo; Palumbo, Enrico; Hauff,
Claudia; Bouchard, Hugues; Lalmas, Mounia (Spotify). "As It Was:
Aligning LLM Search Evaluation with Historical User Preferences."
SIGIR '26, 2026-07-01. DOI 10.1145/3805712.3808488.
https://arxiv.org/html/2607.01040v1

**Scope note**: this is a Spotify-authored paper about evaluating
LLM-as-judge systems for **music search relevance** — an internal
search-quality methodology paper, not a study of web-content AI
citation/visibility. Included here for a narrow, indirect reason (see
below), not as a mainline GEO/AEO source.

## Key takeaways

- Introduces "Query–Relevance–Impressions (QRI) cards" — grounding
  LLM relevance judgments in historical user-interaction data
  (debiased via inverse propensity scoring for position bias), instead
  of semantic reasoning alone.
- **"Plain" LLM judges (semantic-only) measurably diverge from real
  user preference**, especially on ambiguous/long-tail queries — the
  behavior-grounded judge improved Spearman correlation ~5% overall,
  +91% on judge-disagreement cases, and closed roughly a fifth of the
  gap to online A/B alignment (30.6% → 36.8%).
- Even with grounding, absolute alignment with true online preference
  "remains moderate" — the authors explicitly caution more/richer
  behavioral signal is likely needed, and flag a risk of amplifying
  residual bias already present in interaction logs.

## What this updates in the wiki

Adds a methodological caveat, not a conflict with any specific existing
claim.

- Updated [[generative-engine-optimization]] — added a caveat to the
  "Visibility is measured differently than SEO ranking" section, next
  to its existing "Subjective Impression" (7-facet LLM-judged score)
  metric: LLM-as-judge scoring of relevance/visibility should be read
  with the caveat that "plain" semantic LLM judgment has been shown
  (in an adjacent domain, music search) to diverge from real user
  preference unless grounded in actual behavioral data — a reason to
  treat any purely-LLM-judged AI-visibility metric as directional
  rather than ground truth.
- No changes to [[ai-visibility-measurement-methodology]] — that page's
  metrics (traffic/CTR-based, native impression/citation counts) aren't
  LLM-judge-based, so this caveat doesn't apply there.
