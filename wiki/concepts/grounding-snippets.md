---
type: concept
tags: [aeo]
updated: 2026-11-06
---

# Grounding Snippets

A **grounding snippet** is the short set of sentences an AI search
system extracts from a retrieved page and places in the model's context
to write its answer. It is the unit that actually reaches the model:
most of a page never does. You can rank first in classic search and
still contribute almost nothing here.

Main source: [[dejan-grounding-snippets-2026]] (7,060 queries, 2,275
pages, 883,262 snippets; vendor data, not controlled for authority or
freshness — treat as directional).

## How snippets are built

- **Extractive, sentence-level.** The system scores individual
  sentences against the (fanout) query and stitches the top ones
  together with ellipses ("segment … segment … segment"). Exact
  sentences, not paraphrase. Google and Claude both show this shape.
- **Query-focused**: the same page gives different extracts for
  different [[query-fanout]] sub-queries.
- **Lead bias**: opening paragraphs are taken almost wholesale —
  consistent with the positional bias toward document beginnings in
  [[goliath-david-generative-search-perplexity-2025]].
- **Structural noise competes**: tables of contents, headers, and stray
  markers get scored as if they were sentences.
- Each chunk carries a relevance score (Google: 0.1–1.0).

## A fixed budget, shared by rank

- Roughly **2,000 words of grounding per query** (median 1,929; p95
  2,798), average chunk ~15.5 words.
- **Rank sets share**: the #1 source gets ~531 words (28%), the #5
  source ~266 (13%) — about half. This mirrors the retrieval-rank
  gatekeeper effect in [[ai-citation-landscape]].
- **Longer pages get lower coverage**: ~61% of a sub-1,000-word page is
  covered vs. ~13% at 3,000+ words; selection plateaus around 540 words
  (~3,500 characters). Density beats length — agrees with the 500–2,000
  word sweet spot and focus-over-comprehensiveness findings in
  [[geo-content-optimization-tactics]].
- In one sample only ~32% of available characters were used (21–65% per
  source). Kept: core service info, process steps, pricing, examples.
  Dropped: navigation, boilerplate, time-limited promotions, off-topic
  sections, verbatim customer quotes.

## Transient by design

Snippets are injected for one turn and then purged. A follow-up question
works from the model's own earlier summary, not your page — so what
persists of you is whatever the first snippet captured.

## Platforms differ

- **Google/Gemini**: near 1:1 received-to-cited; results held as
  ordered `query.result` pairs (~10 per query).
- **OpenAI/GPT**: widest net, fewest citations (~20:1); sees each result
  as a small card (title, URL, 1–3 sentence snippet) and opens fixed
  text windows rather than whole pages.
- **Anthropic/Claude**: two-pass grounding, most token-hungry, exposes
  some unselected pages.

See also the single-query funnel in [[parametric-memory-vs-grounding]]
and engine personalities in [[ai-citation-landscape]].

## What snippets don't fix

Grounding enters the model as ordinary context tokens. The model still
ranks candidates using its own recall alongside them
([[dejan-generative-self-retrieval-2026]]), and grounded answers can
still misstate sources — see [[ai-overview-grounding-and-fidelity]].
Self-reported grounding isn't always reliable either: Gemini once cited
a non-existent paper while describing its own grounding.

## Content implications

- Write dense, self-contained sentences that survive extraction alone.
- Put the key information in the opening paragraph.
- Cover the fanout angles a question splits into.
- Strip menus, TOCs, and boilerplate from the main content area.
- Think in modular blocks; the winning unit is the sentence.

Tactics are filed in [[geo-content-optimization-tactics]].

## See also

- [[chunkability]] — the same passage-level principle one level coarser; self-contained sentences survive extraction.
- [[ai-search-reranking-pipeline]] — the rerank stage DEJAN's cross-encoder replication models; snippets are what survives it.
- [[query-fanout]] — the sub-queries each snippet budget is spent against.
