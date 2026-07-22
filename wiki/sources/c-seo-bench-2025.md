---
type: source
tags: [seo, aeo]
date_published: 2025-12-02
date_ingested: 2026-07-22
origin: raw/studies/c-seo-bench-does-conversational-seo-work-2025.pdf
---

# C-SEO Bench: Does Conversational SEO Work? (Puerto et al., NeurIPS 2025)

**Citation:** Puerto, Haritz; Gubri, Martin; Green, Tommaso; Oh, Seong
Joon; Yun, Sangdoo. "C-SEO Bench: Does Conversational SEO Work?" 39th
Conference on Neural Information Processing Systems (NeurIPS 2025),
Track on Datasets and Benchmarks. Parameter Lab / NAVER AI Lab.
https://github.com/parameterlab/c-seo-bench ·
https://huggingface.co/datasets/parameterlab/c-seo-bench (Publish date
approximate — NeurIPS 2025 conference dates; no more specific date
disclosed in the PDF.)

## Why this source matters

This is a **direct, larger-scale re-test of the exact tactics behind
this wiki's Tier 1-3 "GEO Content Optimization Tactics"**
([[geo-generative-engine-optimization-aggarwal-2023]], the wiki's
founding GEO source) — same eight content transformations (Authoritative,
Statistics, Citations, Fluency, Unique Words, Technical Terms, Simple
Language, Quotes), plus two new methods (Content Improvement, LLM
Guidance/`llms.txt`-style), tested across 6 domains (Retail, Video
Games, Books, Web, News, Debate), 4 LLMs (GPT-4o-mini, Claude 3.5
Haiku, o3, o4-mini), and — critically — a different, more
decision-relevant outcome metric: **citation rank** (does the LLM cite
this document earlier in its response?) rather than Aggarwal et al.'s
original **word count** metric (how many words the LLM spends
discussing the document).

## Key findings

- **Most C-SEO content tactics show no significant effect on citation
  rank, and several are actively harmful.** Out of 54
  method×domain×significance tests on GPT-4o-mini, only 3 showed a
  statistically significant *positive* effect (Content Improvement on
  Retail; LLM Guidance on Retail and Video Games). No method was
  significant for the question-answering task at all, and *no method*
  was significant on Claude 3.5 Haiku.
- **Negative effects are not marginal.** The Statistics method
  significantly *decreased* ranking in 19 of 24 tested settings; on
  Haiku 3.5, 26 of 30 product-recommendation settings showed
  significant negative effects; on o4-mini, 19 of 30 question-answering
  settings did too.
- **Document position in the LLM's context window (i.e., retrieval
  rank / traditional SEO) dominates every content tactic by a wide
  margin.** Moving a document to position 1 in context produced gains
  of +0.87 to +2.77 rank positions depending on domain — several times
  larger than the best C-SEO method's effect (e.g. Retail: +2.77 for
  position-1 vs. +0.36 for the best C-SEO method, LLM Guidance).
- **The best C-SEO methods (LLM Guidance, Content Improvement) behave
  as a congested, zero-sum game as adoption rises.** AUC-measured gains
  shrink steadily as more competing documents adopt the same method,
  converging toward zero as adoption approaches 100% — modeled as a
  non-cooperative multi-actor game, a dynamic not previously
  quantified for white-hat C-SEO in this wiki (prior white-hat work,
  including Aggarwal et al. 2024, tested single-actor/unilateral
  adoption only).
- **Why this doesn't contradict Aggarwal et al. 2024's original
  results, per the authors' own reconciliation**: word count (the
  original metric) and citation rank (this paper's metric) measure
  different things — a document can be discussed at length without
  being cited *earlier*. The authors note Aggarwal et al.'s own
  position-adjusted word-count metric already showed a general
  decrease, "implicitly indicating that the C-SEO methods do not
  generally improve citation ranking" — i.e., a careful re-read of the
  original paper's own secondary metric is consistent with this
  paper's negative finding, not opposed to it.
- **Benchmark scale/design**: 2 tasks (question answering, product
  recommendation) × 6 domains, 16.3k documents, 1.9k+ queries — the
  first C-SEO benchmark to test multiple domains and a multi-actor
  (competitive, up to 10 simultaneous adopters) adoption scenario,
  versus prior work's single-domain, single-actor designs.
- **Scope limitation stated by the authors**: this evaluates
  *white-hat* C-SEO (legitimate content improvement) only, not
  black-hat/adversarial prompt-injection methods (a separate research
  line — Nestaas et al. 2025, Kumar & Lakkaraju 2024, Pfrommer et al.
  2024 — which the authors note shows different, prisoner's-dilemma-like
  dynamics under adversarial competition).

## Relationship to existing wiki claims — CONFLICT

This directly conflicts with this wiki's Tier 1-3 tactic rankings in
[[geo-content-optimization-tactics]] and the "Why traditional SEO
doesn't transfer" framing in [[generative-engine-optimization]], both
built on [[geo-generative-engine-optimization-aggarwal-2023]]'s
word-count-based results. See the Conflicting Evidence sections added
to both pages. In brief: **this paper's citation-rank metric is more
decision-relevant** (it measures whether a document gets cited
*earlier*, the actual C-SEO goal per this wiki's own framing) and its
benchmark is far larger/broader (6 domains, 4 models, multi-actor,
16.3k documents vs. Aggarwal et al.'s 1 domain/1k queries/single actor)
— but it doesn't erase the original findings, since the two papers
measure genuinely different outcomes. Treat this as a significant
downweighting of confidence in the Tier 1-3 content tactics, not a
full reversal, pending further replication.

## Strong corroboration (not conflict) with existing findings

- **[[airops-fan-out-effect-2026]]'s retrieval-rank-as-gatekeeper
  finding** (ChatGPT: position 1 in retrieval = 58.4% citation rate vs.
  14.2% at position 10) is independently and causally corroborated by
  this paper's in-context-position experiment (position 1 in the LLM's
  context window produces by far the largest citation-rank gains of
  anything tested) — two differently-designed studies, on different
  platforms, converging on the same mechanism: **where a document sits
  in the retrieval/context pipeline dominates content-level
  optimization.**
- Reinforces this wiki's existing "get retrieved first, then compete on
  content" framing in [[geo-content-optimization-tactics]]'s "Focus
  over comprehensiveness" section — now with a controlled, causal
  experiment (randomized context position) rather than only
  observational retrieval-rank correlation.

## Caveats

- Content transformations and the conversational search engine
  generation step both use commercial proprietary models
  (`gpt-4o-mini` to apply C-SEO methods; `gpt-4o-mini`,
  `claude-3-5-haiku`, `o3`, `o4-mini` to run the CSE) — results may not
  generalize to other model families/versions.
- English-language content only.
- Does not test interplay between traditional SEO and C-SEO applied
  together (left as future work by the authors).
- Multi-actor simulation capped at 10 simultaneous adopters.

## See also

- [[geo-content-optimization-tactics]] — the Tier 1-3 tactics this
  paper re-tests; see its updated Conflicting Evidence section.
- [[generative-engine-optimization]] — the "why traditional SEO doesn't
  transfer" framing this paper significantly complicates; see its
  updated Conflicting Evidence section and Open Questions.
- [[geo-generative-engine-optimization-aggarwal-2023]] — the original
  paper whose exact tactics and dataset methodology this paper
  extends and re-tests with a different metric.
- [[airops-fan-out-effect-2026]] — the independent corroborating
  retrieval-rank-as-gatekeeper finding.
- [[ai-citation-landscape]] — houses the airops-fan-out-effect-2026
  retrieval-rank section this paper corroborates.
- [[bardas-white-hat-seo-llm-2025]] — a paper this benchmark's related-
  work section cites and critiques directly (its method "assumes
  knowing the user query beforehand"); a different research tradition
  (classic retrieval-ranking competitive search) adjacent to this one.
- [[kumar-lakkaraju-manipulating-llms-2024]] — another related-work
  citation, this one on the black-hat side (adversarial STS/GCG attacks)
  that this benchmark's white-hat scope explicitly excludes.
