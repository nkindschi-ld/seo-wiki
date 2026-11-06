---
type: source
tags: [aeo]
date_published: 2026-03-10
date_ingested: 2026-11-06
origin: raw/studies/gekhman-thinking-to-recall-2026.pdf
---

# Thinking to Recall: How Reasoning Unlocks Parametric Knowledge in LLMs

Gekhman, Z., Aharoni, R., Ofek, E., Geva, M., Reichart, R., Herzig, J.
(2026-03-10). arXiv:2603.09906v1. Google Research, Technion, Tel Aviv
University. (Copy hosted at dejan.ai/media/papers/.)

**Nature of source**: peer-style research paper from Google Research.
Closed-book QA only — **search/grounding disabled** — so it speaks to
parametric recall, not live AI search.

## Setup

Hybrid models with reasoning toggled ON/OFF: Gemini-2.5-Flash,
Gemini-2.5-Pro, Qwen3-32B. Datasets: SimpleQA-Verified (1,000) and
EntityQuestions (1,000, four relations). Metric: pass@k up to k=100.

## Key takeaways

1. **Reasoning expands the parametric recall boundary** — pass@k is
   higher with reasoning ON across all models/datasets, often more so
   at high k (nearly doubling for Qwen3-32B on SimpleQA). Reasoning
   reaches answers that are effectively unreachable without it.
2. **Not about question complexity**: "multi-hop" questions didn't
   benefit more than single-hop ones; gains come from better recall.
   Less capable models benefit more.
3. **Two mechanisms**: (a) a content-independent **computational
   buffer** (even filler traces help, but plateau below full
   reasoning); (b) **factual priming / generative self-retrieval** —
   recalling related facts bridges to the answer. Extracting those facts
   and feeding them back with reasoning OFF recovers most of the gain.
4. **Hallucination risk**: traces with a hallucinated intermediate fact
   are much more likely to end wrong — SimpleQA-Verified 41.4% correct
   (clean) vs. 26.4% (hallucinated); EntityQuestions 71.1% vs. 32.2%.
   Holds within-question (slopes 0.84 / 0.86).
5. **Test-time selection**: keeping traces that recall facts gives
   +8.2% / +2.6% relative accuracy; keeping only traces whose facts
   verify (via search-enabled Gemini-2.5-Flash) gives +12.2% / +5.1%.
   Done by the researchers, not the model.

## Wiki pages updated

- [[parametric-memory-vs-grounding]] — generative self-retrieval
  section. Interpreted for SEO in [[dejan-generative-self-retrieval-2026]].
