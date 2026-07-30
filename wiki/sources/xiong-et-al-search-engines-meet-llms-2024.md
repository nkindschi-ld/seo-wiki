---
type: source
tags: [seo, aeo]
date_published: 2024-07
date_ingested: 2026-07-23
origin: raw/articles/xiong-et-al-search-engines-meet-llms-2024.md
---

# When Search Engine Services Meet Large Language Models: Visions and Challenges (Xiong et al., 2024)

**Citation:** Xiong, Haoyi; Bian, Jiang; Li, Yuchen; Li, Xuhong; Du,
Mengnan; Wang, Shuaiqiang; Yin, Dawei; Helal, Sumi. "When Search Engine
Services Meet Large Language Models: Visions and Challenges." arXiv,
2024-07. https://arxiv.org/html/2407.00128v1

An academic survey/vision paper (not an empirical study) — several
authors (Bian, Wang, Yin) are Baidu-affiliated, so treat the framing as
industry-adjacent academic perspective rather than fully independent
research.

## Key takeaways

- Frames the LLM-search relationship as **bidirectional**:
  **Search4LLM** (search infrastructure improves LLMs — pretraining
  corpus, query-click fine-tuning data, learning-to-rank as alignment
  signal, RAG for hallucination mitigation) and **LLM4Search** (LLMs
  improve search — query processing, information extraction, ranking/
  retrieval, evaluation/A-B-testing automation).
- Explicitly names **RAG (Retrieval-Augmented Generation)** as the
  mechanism addressing hallucination: injecting current search results
  into the model's context window at inference time for real-time
  information. This is the underlying technical mechanism behind
  concepts the wiki already discusses at a practitioner level (query
  fan-out, retrieval-rank-as-citation-gatekeeper, "retrievability").
- Names four open challenges relevant to why AI-search behavior is hard
  to audit/predict from the outside: **memory management** (real-time
  index consistency), an **explainability gap** ("black box" behavior
  at web scale — tracing why a specific page was/wasn't used is
  "practically impossible"), **agent coordination** (LLMs as autonomous
  planning/acting agents), and **continuous update synchronization**
  (web content changes faster than model training cycles).
- Cites a stat (1.079 billion websites as of Jan 2024, up from 185
  million ~15 years prior) as scale context, not a directly actionable
  SEO/AEO number.

## What this updates in the wiki

Agrees with and provides academic/technical grounding for existing
practitioner-level claims — no conflicts.

- Updated [[generative-engine-optimization]] — added a subsection under
  "Retrievability" explaining the RAG mechanism this survey describes,
  as the technical grounding for why "retrievability" (per
  [[sel-integrate-geo-with-seo]]) is a distinct pipeline stage from
  crawl/index/rank.
- Updated [[ai-visibility-measurement-methodology]] — added the
  "explainability gap" framing as an academic explanation for *why*
  the measurement gap exists in the first place (billions-of-parameters
  black-box behavior, not just a tooling gap AI vendors haven't gotten
  around to closing).
