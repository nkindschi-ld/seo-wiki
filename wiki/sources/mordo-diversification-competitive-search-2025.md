---
type: source
tags: [seo]
date_published: 2025-01-24
date_ingested: 2026-07-22
origin: raw/studies/arxiv-2501.14922.pdf
---

# Search Results Diversification in Competitive Search (Mordo et al., 2025)

**Citation:** Mordo, Tommy; Reinman, Itamar; Tennenholtz, Moshe;
Kurland, Oren. "Search Results Diversification in Competitive Search."
arXiv:2501.14922v1 [cs.IR], 2025-01-24. Technion.
https://arxiv.org/abs/2501.14922

## What this source is

An academic **competitive search** paper (same research tradition and
overlapping authorship as [[bardas-white-hat-seo-llm-2025]] — Mordo,
Kurland, Tennenholtz appear on both). It studies document authors
(publishers) game-theoretically competing to rank highest for a query
under a classic ad hoc retrieval ranker, with no LLM involved on
either the ranking or editing side (ranking is E5 dense-embedding
cosine similarity; editing is done by human students). The novelty is
adding **search-results diversification** (MMR) to the ranking
function and analyzing how that changes publisher strategy.

## Background this paper builds on

Prior work in this lineage (cited but not yet separately ingested into
this wiki) established two findings this paper directly responds to:

- **Raifer et al. 2017** (SIGIR): in repeated ranking competitions with
  an undisclosed, relevance-only ranking function, publishers converge
  on a **"mimicking the winner"** strategy — copying content from
  whichever document ranked highest in the previous round, since it's
  the only signal available about what the hidden ranker rewards.
- **Goren et al. 2021** (CIKM): "mimicking the winner" produces a
  **herding effect** — publisher content converges/homogenizes around
  whatever got ranked first, even when that document was non-relevant
  or only covered one aspect of the query, planted there deliberately.
  Beyond corpus-diversity loss, herding is a lever an adversarial actor
  could exploit to steer publisher content en masse.

## Method

Game-theoretic analysis plus an empirical ranking competition:

- **Theory**: models the repeated ranking game under a ranking
  function that applies MMR-style diversification (a document's score
  is penalized for similarity to already-higher-ranked documents,
  Definition 2 in the paper) rather than relevance alone. Proves the
  game still has a **min-max regret equilibrium** (a stability
  concept suited to undisclosed-ranker settings, per Raifer et al.).
- **Empirical**: 40 students in an IR course served as publishers
  across 15 TREC commercial-intent queries, each run as two parallel
  7-round competitions per query — one ranked by relevance only
  (**R**, E5 cosine), one by relevance + MMR diversification (**D**,
  λ=0.5). Students weren't told which type they were in. Documents
  were relevance/quality-judged by 5 crowd workers each (840 documents
  total, dataset public).

## Key findings

- **Diversity-based ranking still has a stable equilibrium** — adding
  diversification doesn't destabilize the competitive dynamic, it just
  changes the winning strategy.
- **The equilibrium strategy shifts from "win 1st" to "secure 2nd."**
  Formally: once a publisher can't own the ranking-function's peak,
  their best move under MMR is to differentiate from the current
  winner (since similarity to the winner is now penalized) rather than
  mimic it — the opposite incentive from the relevance-only case.
- **"Mimicking the winner" is empirically reduced under diversification:**
  - Consecutive winning documents were significantly *less* similar to
    each other under D than R, across four independent similarity
    measures (E5, SBERT, TF-IDF, Jaccard) — e.g., average E5 similarity
    between consecutive winners: 0.97 (R) vs. 0.95 (D); TF-IDF: 0.89
    (R) vs. 0.76 (D).
  - Mean and minimum inter-document similarity *within* a ranked list
    was significantly lower under D than R for all four measures.
  - Similarity between the top-2 ranked documents grew monotonically
    over rounds under R but stayed comparatively flat under D.
  - When a document dropped from 1st place, it was more likely to fall
    to 3rd under D (23%) vs. 2nd under R (26%) — consistent with the
    theory: replacing the winner with a near-copy gets that near-copy
    *penalized* under MMR, dropping it further than under relevance-only
    ranking.
- Retrieval quality (NDCG@4, 0.92-0.96) was statistically indistinguishable
  between R and D — diversification didn't cost relevance in this setup.
- Students were never told which competitions used diversification,
  yet still adapted their strategy — consistent with prior findings
  that publishers can infer undisclosed ranker properties from observed
  outcomes alone.

## Relationship to existing wiki claims

- **New research thread for this wiki.** No existing concept page
  covered publisher herding, "mimicking the winner," or diversification
  as a ranking-side countermeasure — filed as a new concept,
  [[competitive-search-herding-and-diversification]].
- **Same lab/tradition as [[bardas-white-hat-seo-llm-2025]]**, but a
  different axis: Bardas studies the *editing* side (can an LLM be a
  better competitive editor than a human?); this paper studies the
  *ranking-function* side (can the ranker itself suppress the
  homogenization that competitive editing produces?). Complementary,
  not conflicting.
- No LLM is involved in this paper at all — it's the purest classic-IR
  entry in this wiki's competitive-search cluster, useful as the
  mechanism-level baseline for "mimicking the winner"/herding that the
  LLM-era papers (Bardas, and eventually Raifer/Goren if ingested)
  build on.
- **Practical translation, flagged as inference, not stated by the
  paper**: to the extent AI/answer engines apply results
  diversification (many do, to avoid redundant citations in a single
  answer), competitive content-mimicking pressure toward the top-cited
  source should be somewhat self-limiting — publishers chasing a
  "top spot" copy strategy may instead be pushed toward differentiated
  content to secure a secondary citation slot. This is an extrapolation
  from a classic ad-hoc-retrieval lab study, not a finding about LLM
  answer engines specifically.

## See also

- [[competitive-search-herding-and-diversification]] — new concept page
  synthesizing this paper's findings.
- [[bardas-white-hat-seo-llm-2025]] — same research lab, editing-side
  companion paper.
- [[c-seo-bench-2025]] — the wiki's other large-scale competitive-search
  re-test source; same broader academic tradition.
