---
type: source
tags: [seo, aeo]
date_published: 2026-07-21
date_ingested: 2026-07-29
origin: raw/articles/evilmartians-which-ai-reads-your-site-2026.md
---

# Which AI Actually Reads Your Site? Two Months of LLM Traffic, Measured (Evil Martians, 2026-07-21)

**Citation:** Klubochkina, Rita; Turner, Travis. "Which AI actually reads
your site? Two months of LLM traffic, measured." Evil Martians Chronicles,
2026-07-21.
https://evilmartians.com/chronicles/which-ai-actually-reads-your-site-two-months-of-llm-traffic-measured

First-party server-log study: Evil Martians instrumented their own site with
a Netlify edge function that reads raw `User-Agent`/`Accept` headers before
rendering, classifies each client (`ai`/`browser`/`crawler`/`scanner`/
`library`), performs HTTP content negotiation (serves Markdown on
`Accept: text/markdown`), and forwards server-side events to GA4 via the
Measurement Protocol. ~268,000 agent requests vs. ~107,000 human pageviews
captured over ~2 months (early May–early July 2026). A direct companion to
[[vercel-rise-of-the-ai-crawler]] — both are real traffic-log studies, not
vendor surveys — but scoped to a single site (one developer-audience site),
so treat magnitudes as illustrative, not representative.

## Key takeaways

- **"AI traffic" is not a monolith — segment before analyzing.** The single
  most important finding: different named clients have *opposite* format
  preferences, so a coarse "AI traffic" bucket hides the behavior that
  matters. Per-agent breakdown:

  | Agent | Requests | Markdown % | Behavior |
  |---|---|---|---|
  | ChatGPT-User | 196,973 (~73%) | 0.1% | HTML almost exclusively |
  | Claude Code | 23,300 (~9%) | 76% | Requests Markdown via `Accept` header |
  | OAI-SearchBot | 7,255 | 26% | Mixed |
  | GPTBot | 3,579 | 31% | Mixed |
  | Perplexity | 7,728 | ~0% | HTML-only |

- **Content negotiation is the technique that actually works.** Serving
  Markdown in response to `Accept: text/markdown` delivered Markdown to
  Claude Code on 76% of its fetches, using standard HTTP and requiring no
  site-specific knowledge from the agent. Overall format split: HTML ~85%
  (~227K), Markdown ~15% (~40K).
- **`.md` routes: modest but real adoption** (~15% of agent traffic), mostly
  coding agents and on-demand fetchers; training crawlers largely ignore
  them.
- **`llms.txt` is barely fetched — the most direct null result yet.** ~660
  direct fetches over two months; only **~37 from named AI assistants**, the
  other ~95% from search crawlers and generic scanners. "Referral" traffic
  from it (106 of 117 hits) traced to a stale `Chrome/111.0` bot, not
  authentic AI following links. This is stronger evidence than
  [[otterly-ai-keyword-research-2026]]'s "no citation lift": that test showed
  `llms.txt` doesn't *help*; this shows AI clients don't even *request* the
  file.
- **The "hidden AI hint" `<link>` tag did nothing.** A tagged URL param
  (`?ref=hint`) produced **zero attributable fetches** across all 268K
  requests.
- **URL guessing / domain hallucination** (corroborates
  [[vercel-rise-of-the-ai-crawler]] and the checklist's hallucinated-URL
  item): agents request non-existent pages — versioned slug variants
  (`-2025`/`-2026`), invented `.md` slugs — and hallucinate wrong TLDs
  (`.dev`/`.app`/`.io`) and bare IPs. Owning the variants and redirecting
  recovers the traffic; treat recurring guessed slugs as redirect-target
  signals.
- **Server-side instrumentation sees what client-side analytics can't** —
  non-rendering agents never fire JS tags, so a GA4/edge Measurement-Protocol
  setup is required to count them. Corroborates
  [[peec-ai-server-logs-ai-search-2026]]'s server-log-first approach.

## Note on scope: format preference ≠ JS execution

"ChatGPT-User reads HTML almost exclusively" is a statement about **format
negotiation** (HTML vs. Markdown), not about whether the client executes
JavaScript. Don't conflate this with
[[vercel-rise-of-the-ai-crawler]]'s JS-execution finding — they measure
different things. This study didn't test JS rendering; it tested which
representation each agent asks for.

## What this updates in the wiki

Agrees with and extends existing claims — no conflicts.

- **[[geo-content-optimization-tactics]]** — strengthened the `llms.txt`
  "don't bother" entry with this direct traffic-side null result, and added
  the hidden-`<link>`-hint zero-fetch finding.
- **[[technical-seo-audit-checklist]]** §5 — added a **content-negotiation**
  audit item (serve Markdown on `Accept: text/markdown` for coding agents;
  keep rendered HTML excellent for the dominant HTML-only clients), added the
  "segment user agents before analyzing" caution to the server-log item, and
  enriched the hallucinated-URL item with the versioned-slug / TLD-variant
  guessing patterns.
