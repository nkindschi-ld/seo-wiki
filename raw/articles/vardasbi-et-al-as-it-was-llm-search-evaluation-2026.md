# As It Was: Aligning LLM Search Evaluation with Historical User Preferences

Authors: Ali Vardasbi, Gustavo Penha, Enrico Palumbo, Claudia Hauff,
Hugues Bouchard, Mounia Lalmas (all Spotify)
Publish date: 2026-07-01
Venue: SIGIR '26 (49th International ACM SIGIR Conference)
DOI: 10.1145/3805712.3808488
Source: https://arxiv.org/html/2607.01040v1
Retrieved: 2026-07-23

## Abstract summary

Introduces a behavior-grounded LLM evaluation framework for music
search that augments semantic judgment with historical user
interaction data. Uses "Query–Relevance–Impressions (QRI) cards" to
ground LLM-based relevance assessments in empirical user engagement
patterns, improving alignment with actual user preferences beyond what
semantic reasoning alone achieves.

## Methodology

- Compares two LLM judge variants using identical prompts/rubrics: a
  "Plain" judge (semantic similarity only) vs. a "Behavior-Grounded"
  judge (given QRI cards summarizing historical query-entity
  interactions with debiased relevance estimates via inverse propensity
  scoring, correcting for position bias in interaction logs).
- Data: ~5,000 log-derived queries (20-400 users, 10-day period);
  a 265-instance, 5-language human-judged multilingual (HJM) dataset;
  a 904-query online A/B production experiment.

## Key findings

- Spearman rank correlation improved ~5% overall on 5,965 recomposed
  SERPs; +91% relative improvement on cases where the plain and
  behavior-grounded judges disagreed.
- +15% correlation increase on the multilingual human-judged dataset.
- Online A/B test alignment: 30.6% (plain judge) vs. 36.8%
  (behavior-grounded judge).
- Behavioral grounding is most effective at resolving ambiguous
  queries, recalibrating error severity in near-miss cases, and
  improving sensitivity to ranking-quality distinctions among plausible
  results.

## Limitations acknowledged

Absolute alignment with online preferences remains moderate — richer
behavioral signals may be needed for further gains. The authors flag a
need for safeguards against amplifying residual biases already present
in interaction logs (the debiasing correction reduces but doesn't
eliminate this risk).

## Relevance note

This is a Spotify-authored paper about evaluating LLM-as-judge systems
for **music search relevance**, not about web content citation/AEO
directly. Its relevance to this wiki is methodological: it's evidence
that "plain" LLM-judge relevance scoring (semantic reasoning alone,
without grounding in real user behavior) measurably diverges from
actual user preference, especially on ambiguous/long-tail queries —
relevant caveat for any LLM-judge-based AI-visibility metric.
