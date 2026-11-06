Source: https://claude.ai/artifact/P4CZc9VEMW31gekzeFzau6 (interactive explainer linked from dejan.ai/blog/fanout-vectors/ as "Visual Explainer")
Retrieved: 2026-11-06
Note: the page is JS-rendered; full HTML is saved alongside as dejan-textless-query-fanout-explainer-2026.html. Below is a content summary captured at retrieval time.

# Textless Query Fan-Out

Explainer of Jiang et al., "Efficient, Property-Aligned Fan-Out Retrieval via RL-Compiled Diffusion" (arXiv 2603.06397, March 2026; Google Research + UIUC). The "After" pipeline is labelled hypothetical on the page.

- Before (LLM): a 4B autoregressive LLM (Gemma3-4B / Qwen3-4B) writes 10 text sub-queries, each then embedded for nearest-neighbour search. Batch of 8 queries: 1.46 s. 1,024 queries: ~50 s.
- After (R4T-Diffusion): query encoded once; a 53.9M-parameter diffusion transformer generates 10 sub-query vectors (128 dims) over 256 denoising steps. Batch of 8: 0.07 s. 1,024 queries: 4.21 s.
- No readable sub-query text is produced; paper lists groundedness as N/A.
- Training: RL rewards whole sub-query sets on diversity, relevance, and closeness to real items; the LLM then generates 128 fan-outs per training query (temp 0.9) and the diffusion model is distilled to reproduce those vectors. Only the small model runs at serve time.
- Diversity trade-off: distilled 74.3 vs teacher 76.8 (LLM-judged, Polyvore, Gemma3-4B teacher).
- Tested on Polyvore fashion outfits and a proprietary expert music-playlist set. Not tested on web search; paper does not claim Google uses it in Search / AI Overviews / AI Mode.
- Page's implications: textless fan-out would make sub-queries unobservable; phrasing-level optimization may matter less than topical/entity coverage; content/index quality still decides which items sit near generated vectors. Relevance to Google Search is speculative.
