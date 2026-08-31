---
type: source
tags: [seo, aeo]
date_published: 2026-01-19
date_ingested: 2026-08-20
origin: raw/articles/commoncrawl-web-graph-ai-ranking-signals-2026.md
---

# How SEOs Are Using Common Crawl's Web Graph Data for AI Ranking Signals

**Citation:** Burns, Stephen (Web Intelligence Lead, Common Crawl
Foundation). "How SEOs Are Using Common Crawl's Web Graph Data for AI
Ranking Signals." Common Crawl Blog. Published 2026-01-19.
https://commoncrawl.org/blog/how-seos-are-using-common-crawls-web-graph-data-for-ai-ranking-signals

**Methodology note:** first-party from Common Crawl on its own dataset/
tooling (high rigor for the web-graph-metrics description), but the
citation-probability statistics are attributed secondhand to "Brie
Moreau's analysis" with no link or disclosed methodology given in this
article — treat those specific numbers as directional, not verified.

## Key takeaways

- **Common Crawl's Web Graph is training-data infrastructure, not just
  a crawl archive**: per the article, Common Crawl's dataset is used to
  train **64% of analyzed LLMs**, and Mozilla Foundation's 2024 report
  found **over 80% of GPT-3's training tokens** derived from filtered
  Common Crawl data. This adds hard numbers to a fact this wiki already
  knew qualitatively — [[how-google-search-works]] already lists Common
  Crawl as a "training bot" in its AI-bot-type taxonomy, but without
  any figure on *how much* of frontier-model training data it actually
  supplies.
- **Two publicly-available domain-authority metrics, new to this
  wiki**: **Harmonic Centrality** (how "close" a domain is to others via
  link hops — identifies central web hubs) and **PageRank** (authority
  from being linked by other high-authority sites), both published by
  Common Crawl itself and computed over its full crawl graph.
- **The strategic inference (Metehan Yesilyurt's research question)**:
  since crawl access today shapes training data tomorrow
  ([[how-google-search-works]]'s existing training-bot framing), a
  domain's standing in Common Crawl's Web Graph may predict — or at
  least correlate with — how "overrepresented" that domain is in LLM
  training data, and therefore in the model's baseline
  brand-familiarity/citation tendencies. This is a plausible mechanism,
  not a directly tested causal claim in this article.
- **A large secondhand correlation dataset (Brie Moreau, 2M citations,
  177M sources, undisclosed methodology)**: Google organic position 1 →
  46-48% AI citation probability, position 2 → ~37%, position 10 →
  ~19-20%; comparative listicles account for **32.5%** of AI citations.
  Directionally consistent with this wiki's existing retrieval-rank-
  dominates-citation cluster ([[airops-fan-out-effect-2026]]'s 58.4%/
  14.2% rank-1/rank-10 ChatGPT figures; [[richsanger-ai-overview-patent-insights]]'s
  53%/~50% position-1/2 inclusion rates) but a different, milder
  magnitude and gentler rank-10 falloff (19-20% vs. AirOps's 14.2%) —
  plausibly because this dataset isn't segmented by engine or reference
  type the way AirOps's ChatGPT-only, retrieval-rank-specific figures
  are. Not logged as a formal conflict — same direction, different
  sample/segmentation, no disclosed methodology to reconcile against.
- **Named practical tools**: the **CC Rank Checker** (webgraph.metehan.ai
  — indexes 18M domains across five time periods, 2023-2025), the
  **Common Crawl Index Server** (index.commoncrawl.org — URL-pattern
  lookup against crawl archives), and **Web Graph Statistics**
  (commoncrawl.github.io/cc-webgraph-statistics) — all free/public,
  giving SEOs a way to check a domain's HC/PageRank standing directly
  rather than relying on a commercial domain-authority metric as a
  proxy for training-data representation.
- **Predicted tooling trend**: the author expects Harmonic Centrality to
  become a standard metric in mainstream SEO platforms (Semrush, Ahrefs)
  as AI-visibility optimization matures — a forward-looking prediction,
  not a measured finding.

## Relationship to existing wiki content

Extends [[how-google-search-works]]'s existing training-bot mention
(Common Crawl named only in passing) with concrete provenance figures
and two named, checkable authority metrics. Adds a new, independent
(if unverified) data point to the retrieval-rank-as-citation-gatekeeper
cluster already anchored by [[airops-fan-out-effect-2026]] in
[[ai-citation-landscape]], and to the listicle-dominance findings in
[[listicles-in-ai-search]]. Connects to [[peec-ai-rerankers-geo-aeo-2026]]
and [[peec-ai-server-logs-ai-search-2026]] by author (Metehan Yesilyurt),
already a source in this wiki for AI-search mechanism analysis.

## What this updated

- [[how-google-search-works]] — added training-data-provenance figures
  (64% of LLMs, 80%+ of GPT-3 tokens) and the Harmonic Centrality/
  PageRank metric definitions to the training-bot note.
- [[ai-citation-landscape]] — added Brie Moreau's rank-vs-citation-
  probability data point to "Retrieval rank as the primary citation
  gatekeeper."
- [[listicles-in-ai-search]] — added the 32.5%-of-citations listicle
  share as a corroborating data point.
- [[geo-content-optimization-tactics]] — added a tactic on benchmarking
  domain standing via Common Crawl's free Harmonic Centrality/PageRank
  tools.

No conflicts.
