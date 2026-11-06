---
type: source
tags: [aeo, seo]
date_published: 2026-09-24
date_ingested: 2026-11-06
origin: raw/articles/dejan-fanout-vectors-2026.md
---

# Fanout Vectors (DEJAN)

Petrovic, D. / DEJAN AI (2026-09-24). dejan.ai/blog/fanout-vectors/.

**Nature of source**: short practitioner note on a reproduction of
Google research (Jiang et al., arXiv 2603.06397) — explained in detail
by the linked visual explainer, [[dejan-textless-query-fanout-explainer-2026]].
Speculative about production use.

## Key takeaways

1. The Google paper generates fan-out **as vectors, not text**: a small
   diffusion model takes a query embedding and outputs sub-query
   embeddings used directly for retrieval. Petrovic's prediction: if
   this reaches production, "text fanouts are gone."
2. Explicit caveat: research only, no guarantee Google ships it, or
   where/when/how.
3. DEJAN reproduced it, **skipping the RL step** and instead using a
   strong teacher (Gemma-4-26B-A4B) to generate synthetic orthogonal
   fanouts, trained on Google's e-commerce taxonomy. Model and demo:
   huggingface.co/dejanseo/fanout-diffusion. Reports very fast inference
   with a 1-bit architecture and custom CUDA kernels.

## Wiki pages updated

- Created [[query-fanout]] — "textless fan-out" section.
