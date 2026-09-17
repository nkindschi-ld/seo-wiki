---
type: source
tags: [aeo]
date_published: 2026-04-29
date_ingested: 2026-09-10
origin: raw/studies/citation-selection-vs-absorption-geo-framework-2026.html
---

# From Citation Selection to Citation Absorption: A Measurement Framework for Generative Engine Optimization Across AI Search Platforms

Zhang Kai, He Xinyue, Yao Jingang. arXiv:2604.25707v2, published
2026-04-29.

## Citation

Zhang Kai, He Xinyue, Yao Jingang, "From Citation Selection to
Citation Absorption: A Measurement Framework for Generative Engine
Optimization Across AI Search Platforms," arXiv:2604.25707, 2026.

## Key takeaways

- Proposes a two-stage GEO measurement framework distinguishing
  **selection** (is a source cited, and how many times) from
  **absorption** (how much that citation actually shapes the generated
  answer's content) — two properties that diverge by platform.
- Dataset: 602 stratified prompts across four layers (main topic,
  writing style, language, scenario type), 18,151 successfully fetched
  pages (76.44% fetch success rate), 21,143 citations, 23,745
  citation-level features, released as a public "geo-citation-lab"
  repository.
- **Breadth and depth diverge sharply by platform**:
  - **Perplexity** cites the broadest source set (16.35 average
    citations per answer) but each source has the **lowest** average
    influence (0.0646).
  - **ChatGPT** cites the fewest sources (6.88 average) but each cited
    source has much **higher** average influence (0.2713) — a roughly
    4x higher per-source influence than Perplexity despite citing
    less than half as many sources.
  - Being cited frequently across many answers doesn't mean any single
    citation is doing much work within an answer.
- **Absorption/"influence score"** is a weighted formula that rewards:
  repeated reference within the answer, early appearance, coverage
  across multiple answer paragraphs, TF-IDF similarity to the answer
  text, and n-gram overlap — a substantially more granular metric than
  raw citation presence/count.
- **What drives high absorption**: high-influence pages have on average
  11.4x more words, 12.5x more headings, and 8.94x denser lists than
  low-influence pages, plus a moderate correlation (r=0.43) between
  semantic alignment and LLM-judged relevance.
- **Evidence genre matters more than formatting wrapper alone**:
  definitions (+57% influence), comparisons (+55%), and code (+77%)
  measurably increase absorption. Q&A-style formatting alone, without
  real evidence density, actually shows a *negative* relative influence
  effect (-5.74%) vs. non-Q&A content — formatting isn't a substitute
  for substance.
- English-language content doesn't universally increase citation
  breadth — the effect is platform-dependent, not a blanket rule.
- **News is cited often but absorbed weakly** (0.0726 average
  influence) vs. **encyclopedic content**, which is absorbed far more
  deeply (0.2144) — frequency of citation and depth of use are
  genuinely separate properties, exemplified by this content-type
  split.
- Core theoretical framing: the "Evidence-Container Hypothesis" — pages
  become valuable to generative engines when they're decomposable into
  reusable semantic units (clear topical scope, modular sections,
  dense definitions/stats/comparisons/procedures, semantic alignment
  with likely user intent), which is a different success criterion
  from classical SEO's ranking-position focus.
- Authors are explicit about the limits of their own claims, stratifying
  findings into four confidence tiers: Level 1 descriptive counts
  (established), Level 2 comparative contrasts (supported), Level 3
  mechanistic interpretations (plausible), Level 4 causal optimization
  rules (explicitly future work, not claimed here) — they avoid causal
  claims and note this is correlational.

## What this updated

- New subsection in [[ai-citation-landscape]]: "Citation selection vs.
  absorption," adding this as a complementary measurement axis
  alongside the existing presence/portability/concentration framework
  from [[sej-the-consensus-gap]].
- New guidance in [[geo-content-optimization-tactics]]: target
  absorption (evidence-dense, modular, decomposable sections) not just
  citation count/presence; the Q&A-formatting-isn't-enough finding
  refines existing structural guidance.
- Cross-linked from [[sej-the-consensus-gap]] as a related but distinct
  measurement framework (portability/concentration measures *whether
  and where* a source appears across a citation landscape; this
  measures *how much a given citation matters within a single
  answer*).
- No conflicts with existing wiki claims — genuinely new, complementary
  axis.
