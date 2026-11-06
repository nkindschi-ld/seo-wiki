---
type: source
tags: [aeo]
date_published: 2026-06-21
date_ingested: 2026-11-06
origin: raw/studies/dejan-grounding-snippets-2026.md
---

# Grounding Snippets (DEJAN)

Petrovic, D. / DEJAN AI (2026-06-21). "Grounding Snippets."
dejan.ai/blog/grounding-snippets/.

**Nature of source**: synthesis page summarizing DEJAN's earlier
grounding research, with a quantitative analysis of 7,060 queries,
2,275 pages and 883,262 snippets. DEJAN states it did not control for
authority or freshness and keeps raw data private — "strong directional
signal rather than settled fact." Promotes snippets.dejan.ai and
"Selection Rate Optimization."

## Key takeaways

1. **Grounding snippets are extractive**: exact sentences, scored
   against the (fanout) query, stitched with ellipses
   ("segment … segment"). Claude shows the same format.
2. **Google's extraction traits**: query-focused (same page yields
   different extracts per fanout query); **lead bias** (opening
   paragraphs extracted almost wholesale); structural noise (TOCs,
   headers scored as sentences); per-chunk relevance score 0.1–1.0.
   DEJAN replicates it with a fine-tuned `deberta-v3-large`
   cross-encoder.
3. **Fanout**: each sub-query retrieves its own 5–20 sources, so a page
   can be grounded for one angle and absent for another.
4. **About a third survives**: ~32% of available characters cited in a
   sample (21–65% per source). Kept: core service info, process
   steps, pricing, examples. Dropped: navigation, boilerplate,
   promotions, off-topic sections, verbatim customer quotes.
5. **Fixed budget shared by rank**: ~2,000 words per query (median
   1,929, p95 2,798), avg chunk 15.5 words. #1 source ≈ 531 words
   (28%), #5 ≈ 266 (13%). Coverage ~61% under 1,000 words vs. ~13% at
   3,000+; selection plateaus ~540 words (~3,500 chars). **Density
   beats length.**
6. **Transient**: snippets are purged after one turn; follow-ups work
   from the model's own earlier summary.
7. **Platform differences**: Gemini ~1:1 received-to-cited, indexes
   results as `query.result` pairs (~10/query); GPT casts widest net
   and cites least (~20:1 "visibility trap"), sees results as small
   cards and opens fixed text windows; Claude grounds in two passes,
   most token-hungry.
8. Gemini once recited a grounding citation for a non-existent paper —
   self-reported grounding isn't always reliable.

## Wiki pages updated

- Created [[grounding-snippets]] (concept).
- [[query-fanout]] (created) — per-sub-query retrieval.
- [[geo-content-optimization-tactics]] — extraction-ready writing
  tactics, supporting existing front-loading and focus findings.
- [[parametric-memory-vs-grounding]] — cross-link.
