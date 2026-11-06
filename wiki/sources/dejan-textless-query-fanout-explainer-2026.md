---
type: source
tags: [aeo]
date_published: 2026-09-24
date_ingested: 2026-11-06
origin: raw/articles/dejan-textless-query-fanout-explainer-2026.md
---

# Textless Query Fan-Out (interactive explainer)

Interactive explainer page (claude.ai/artifact/P4CZc9VEMW31gekzeFzau6)
linked as the "Visual Explainer" from [[dejan-fanout-vectors-2026]];
explains Jiang et al., "Efficient, Property-Aligned Fan-Out Retrieval
via RL-Compiled Diffusion" (arXiv 2603.06397, March 2026; Google
Research + UIUC). Publish date assumed to match the linking post. The
"After" pipeline is labelled hypothetical. Raw copy is the page HTML
plus a captured summary (JS-rendered page).

## Key takeaways

1. **Before**: a 4B LLM (Gemma3-4B/Qwen3-4B) writes 10 text sub-queries,
   each embedded for nearest-neighbour search — 1.46 s per batch of 8,
   ~50 s for 1,024 queries.
2. **After (R4T-Diffusion)**: query encoded once; a 53.9M-parameter
   diffusion transformer generates 10 × 128-dim sub-query vectors over
   256 denoising steps — 0.07 s per batch of 8, 4.21 s for 1,024.
3. **No readable sub-queries**; the paper lists groundedness as N/A.
4. **Training**: RL rewards whole sub-query sets for diversity,
   relevance, and closeness to real items; the RL'd LLM generates 128
   fanouts per training query, distilled into the diffusion model. Small
   diversity cost (74.3 vs. teacher 76.8).
5. **Scope**: tested on Polyvore fashion outfits and proprietary music
   playlists — **not web search**; no claim Google uses it in Search,
   AI Overviews, or AI Mode.
6. Implications (inferred): fanout would become unobservable;
   phrasing-level targeting would matter less than topical/entity
   coverage; index/content quality still decides what sits near the
   generated vectors.

## Wiki pages updated

- Created [[query-fanout]] — "textless fan-out" section.
