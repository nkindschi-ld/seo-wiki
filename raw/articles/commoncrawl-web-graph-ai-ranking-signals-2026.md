# How SEOs Are Using Common Crawl's Web Graph Data for AI Ranking Signals

Author: Stephen Burns, Web Intelligence Lead at Common Crawl Foundation
Publish Date: 2026-01-19
Source: https://commoncrawl.org/blog/how-seos-are-using-common-crawls-web-graph-data-for-ai-ranking-signals

## The Central Thesis

The SEO industry is shifting focus from traditional search optimization to "AI visibility." Practitioners are discovering that Common Crawl's Web Graph data — used to train 64% of analyzed large language models — reveals which domains get prioritized for crawling and subsequently overrepresented in AI training datasets.

## Web Graph Metrics

Common Crawl publishes two authority measurements:
- Harmonic Centrality (HC): Indicates how "close" a domain is to other domains through link hops, identifying central hubs
- PageRank: Measures authority based on linking patterns from high-authority sites

## The Research Question

Metehan Yesilyurt, an international SEO consultant, investigated whether certain domains receive higher AI citation frequency due to their prominence in Common Crawl's training data representation.

## Critical Data Points (from Brie Moreau's analysis)

- Google position 1 ranking correlates with 46-48% AI citation probability
- Position 2 drops to approximately 37%
- Position 10 falls to roughly 19-20%
- Comparative listicles represent 32.5% of AI citations
- Analysis examined 2 million citations and 177 million sources

## Training Data Composition

Mozilla Foundation's 2024 report indicated over 80% of GPT-3 training tokens derived from filtered Common Crawl data.

## Tools & Resources Mentioned

1. CC Rank Checker Tool (webgraph.metehan.ai) — indexes 18 million domains across five time periods (2023-2025)
2. Common Crawl Index Server (index.commoncrawl.org) — searches URL patterns against crawl archives
3. Web Graph Statistics (commoncrawl.github.io/cc-webgraph-statistics/)

## Practical Applications for SEOs

- Benchmarking domain authority against competitors
- Tracking HC/PageRank changes over time
- Evaluating link sources based on position within web topology
- Understanding co-citation patterns via Reciprocal Rank Fusion

## Future Outlook

The author predicts Harmonic Centrality will become standard in SEO platforms, with tools like Semrush and Ahrefs likely integrating this metric as AI optimization becomes routine.
