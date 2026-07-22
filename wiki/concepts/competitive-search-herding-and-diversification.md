---
type: concept
tags: [seo, aeo]
updated: 2026-07-22
---

# Competitive Search: Herding and Diversification

A game-theoretic framing of what happens when many publishers compete
to rank highest for the same query, under a ranking function they
cannot see. This is a different research tradition than most of this
wiki's GEO/AEO citation-visibility literature — it comes from academic
**competitive search** (Kurland, Tennenholtz, and collaborators at
Technion), studying document authors as strategic players in a
repeated game rather than measuring citation correlations after the
fact. It's the mechanism-level explanation for *why* competitive
content tends to converge, and one lever (ranking-side diversification)
that counteracts it.

## The core dynamic: "mimicking the winner"

When a ranking function is undisclosed (the normal real-world case),
the only signal publishers have about what it rewards is which
documents rank highest. In repeated ranking competitions, this reliably
produces a **"mimicking the winner"** strategy: publishers who didn't
win a round edit their next submission to resemble whatever document
ranked #1 in the previous round, since it's the best available evidence
of what the ranker wants (Raifer et al. 2017, cited by
[[mordo-diversification-competitive-search-2025]]).

## The herding effect

Goren et al. (2021) showed this strategy produces **herding**:
publisher content homogenizes around the top-ranked document, even
when it was deliberately planted and non-relevant or only covering one
aspect of a multi-aspect query. Beyond the obvious harm (reduced
corpus/topical diversity), herding is a lever an adversarial actor
could exploit — plant a document with a desired property at the top,
and publisher herds will reproduce that property at scale.

This is the theoretical backbone behind a practical concern already
present elsewhere in this wiki: if AI answer engines converge on citing
a narrow set of sources, and publishers respond by mimicking whatever
gets cited/ranked, the result is a feedback loop toward homogenized
content — the opposite of what search/answer quality wants, and the
opposite of what [[c-seo-bench-2025]] frames as a "congested zero-sum
game" when many publishers adopt the same tactics simultaneously.

## Diversification as a countermeasure

[[mordo-diversification-competitive-search-2025]] asks whether adding
**search-results diversification** to the ranking function (e.g.,
Maximal Marginal Relevance — penalizing a document's score for
similarity to documents already ranked above it) changes this dynamic.
Both a game-theoretic proof and a 40-student empirical ranking
competition (relevance-only vs. relevance+MMR, matched queries) found:

- The competitive game is **still stable** under diversification (a
  min-max regret equilibrium exists) — diversification doesn't break
  the system, it changes the winning strategy.
- Publishers who can't own the top rank switch from *mimicking* the
  winner to *differentiating* from the winner, because under MMR,
  similarity to the current #1 is now penalized rather than rewarded.
  Some publishers effectively stop competing for 1st place and instead
  compete for 2nd, which requires their content to diverge from the
  winner.
- Empirically: consecutive winning documents were measurably less
  similar to each other, and inter-document similarity within a ranked
  list was measurably lower, under diversification than under
  relevance-only ranking — with no loss of measured retrieval quality
  (NDCG@4 was statistically indistinguishable between conditions).

## Practical read for GEO/AEO — inference, not directly tested

The paper studies classic ad-hoc retrieval (E5 embeddings, human
editors), not an LLM answer engine. But the mechanism generalizes as a
hypothesis worth tracking: to the extent an AI answer engine
diversifies which sources it cites within a single answer (many
already do, to avoid citing near-duplicate sources), the
"copy-whatever's-cited" pressure that drives content homogenization in
[[ai-citation-landscape]] and [[listicles-in-ai-search]] should be
partially self-limiting — publishers chasing a top-citation-slot copy
strategy may be structurally pushed toward differentiated content
instead. No source in this wiki has yet tested this directly for LLM
citation behavior; flagging it as a hypothesis for a future source to
confirm or refute, not a settled claim.

## Related academic lineage not yet separately ingested

Several papers in this tradition are cited by the two sources above but
don't yet have their own wiki source page: Raifer et al. 2017 (SIGIR,
established "mimicking the winner"), Goren et al. 2020/2021 (SIGIR/CIKM,
herding), Ben-Basat et al. 2017 (JAIR, Nash-equilibrium analysis under a
disclosed ranker), and Nachimovsky et al. 2024 (ICTIR, multi-query
competitive search). Worth ingesting directly if this thread gets
pulled on further.

## See also

- [[mordo-diversification-competitive-search-2025]] — the source for
  this page's diversification findings.
- [[bardas-white-hat-seo-llm-2025]] — same research lab; studies the
  editing side (LLM-as-competitive-editor) rather than the ranking-function side.
- [[c-seo-bench-2025]] — independent large-scale empirical evidence of
  C-SEO as a "congested zero-sum game" under competitive adoption,
  consistent with this page's herding framing.
- [[ai-citation-landscape]], [[listicles-in-ai-search]] — the GEO/AEO
  citation-concentration observations this page's countermeasure
  hypothesis speaks to.
