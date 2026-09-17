---
type: source
tags: [aeo]
date_published: 2026-07-15
date_ingested: 2026-09-10
origin: raw/studies/chinese-generative-search-citation-study-2026.pdf
---

# What Do Chinese-Language Generative Search Engines Cite and Surface? A Large-Scale Empirical Study

Tao Zhen, Yue Liu, Gege Zhang, Yixuan Niu (Aidso Wendao Research
Institute / Beijing Aichacha Technology Co., Ltd.). arXiv:2607.15771,
published 2026-07 (49-page working paper).

## Citation

Tao Zhen, Yue Liu, Gege Zhang, Yixuan Niu, "What Do Chinese-Language
Generative Search Engines Cite and Surface? A Large-Scale Empirical
Study," arXiv:2607.15771, 2026.

## Key takeaways

First large-scale, citation-level empirical study of the **Chinese-
language generative-search ecosystem** — DeepSeek, Doubao, Tencent
Yuanbao, and Qwen (Tongyi Qianwen), each across both App and Web
interfaces (8 platform interfaces total). 614 controlled queries, 3
replications, 214,119 raw records cleaned to a 160,860-citation master
dataset.

**Source ecosystem:**
- Third-party content dominates citations: News Media (28.8% of
  citations), Vertical Industry Portals (24.1%), and Social Media/
  Independent Creators (16.4%) together account for ~69% of all
  citations. Brand/Corporate official sites are only 12.9% of
  citations, spread across 6,589 unique domains (HHI ≈ 0.0008 —
  highly dispersed, not concentrated in a few big brands). Direct
  citation of official/corporate sites is comparatively rare.

**Citation absorption (depth):**
- Introduces a nominal/general/deep citation-depth scale. Mean citation
  depth and deep-citation rate varied sharply by platform: Doubao
  averaged depth 1.87 (22.3% deep citations) vs. Tencent Yuanbao's 1.42
  (7.8% deep) — a large cross-platform gap in how deeply any given
  platform actually uses what it cites.
- Semantic role drives depth: definition/explanation and procedural-
  steps citations reach the highest mean depth (~2.4, ~41% deep-
  citation rate); background-context and nominal (no substantive use)
  citations sit near depth 1 (essentially not used).
- A composite "5118-Baidu" SEO quality score (built from two
  established Chinese SEO/webmaster tools) was **not the leading
  predictor** of citation absorption, semantic role, within-answer
  position, or article recency in any of the models tested — it was
  only a moderately positive predictor in the brand-selection model.
  Classic on-page/site-quality SEO metrics and "how deeply an AI
  answer engine uses your content" are measurably different things.

**Silent citations and position:**
- **Silent citations are common: 39.3%** of listed citations across
  labeled platforms never appear as an inline citation in the answer
  body at all — listed in a source table but not actually referenced
  in the visible text. Each answer listed ~10.5 sources on average, of
  which only ~6.9 became inline citations.
- Position matters: citations appearing earlier in an answer cover more
  paragraphs and are referenced more times (both correlations ≈ -0.30
  to -0.32 with order of appearance) — an early-position advantage
  distinct from, and additive to, semantic relevance.

**Recency:**
- Article recency showed a clear time-sensitivity effect: high-
  timeliness queries cited pages with a median publication-age gap of
  18 days vs. 101 days for low-timeliness queries. The fitted citation
  half-life (how fast citation likelihood decays with publication age)
  was ~39 days for high-timeliness queries vs. ~68 days for low-
  timeliness queries — corroborating (with different absolute numbers,
  different market) the freshness-by-vertical finding already in
  [[airops-fan-out-effect-2026]].

**Brand and entity exposure:**
- Of brands present in a citation pool, only **8.3%** made it into the
  visible answer text — a large, quantified "citation ≠ exposure"
  drop-off. Cross-source occurrence count (how many different cited
  sources mention the same brand) was the strongest predictor of
  whether a brand got surfaced.
- ~13% of brand exposures in answers **could not be matched** to any
  source in the contemporaneous citation pool, and ~71% of
  contact-information exposures couldn't be matched to the crawled
  citation body text — meaning a meaningful share of what a generative
  answer surfaces about an entity doesn't trace back to any visible,
  auditable citation.

**Cross-interface consistency:**
- App and Web interfaces of the *same platform* return meaningfully
  different source sets. Mean domain-level Jaccard overlap ranged from
  only 0.19 (Qwen, "almost no overlap") to 0.51 (DeepSeek, "relatively
  most consistent") — no platform had identical App/Web source sets.
- Between-platform differences (range 0.32) substantially exceeded
  between-industry differences (range 0.06) — which interface/platform
  you're measuring matters far more than which industry vertical
  you're in.

**Limitations acknowledged by authors:** observational, not
randomized — associations, not proven causal effects; sample restricted
to pages that already made it into a citation list (doesn't observe the
full candidate/rejected pool); collection window June-July 2026;
LLM-based extraction of citation-absorption type/semantic role/semantic
similarity are themselves fixed-rule model outputs, not ground truth;
publication-date metadata was missing on some platforms.

## What this updated

- New subsection in [[ai-citation-landscape]]: "Chinese-language
  generative search engines," extending the wiki's citation-landscape
  coverage beyond the ChatGPT/Perplexity/Gemini/Claude/Google set for
  the first time.
- Cross-linked to [[citation-selection-vs-absorption-geo-framework-2026]]
  (parallel selection-vs-absorption framing, independently derived in
  a different market) and [[airops-fan-out-effect-2026]] (recency/
  freshness corroboration).
- No conflicts with existing wiki claims — this is a new geographic/
  linguistic market, and where it overlaps conceptually (absorption,
  freshness decay, silent/unused citations) it corroborates rather than
  contradicts existing findings.
