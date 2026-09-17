---
type: source
tags: [seo]
date_published: 2026-06-04
date_ingested: 2026-09-10
origin: raw/studies/webknograph-gnn-internal-linking-2026.html
---

# WebKnoGraph: GNN-Powered Internal Linking

Emilija Gjorgjevska (TU Munich), Georgina Mirceva, Miroslav Mirchev
(Ss. Cyril and Methodius University, Skopje). arXiv:2606.06106,
published 2026-06-04.

## Citation

Emilija Gjorgjevska, Georgina Mirceva, Miroslav Mirchev, "WebKnoGraph:
GNN-Powered Internal Linking," arXiv:2606.06106, 2026.

## Key takeaways

- Open-source framework for evaluating internal-linking *interventions*
  before deployment, instead of relying on manual judgment, generic
  heuristics, or a live A/B test to find out after the fact.
- Pipeline: site modeled as a directed graph of internal hyperlinks →
  page content embedded with `nomic-embed-text-v1` (768-dim) →
  GraphSAGE node embeddings combine content features with graph-
  neighborhood structure → candidate links ranked by combining
  topology, structure, and content similarity → strategy-specific
  filters (target high/low-PageRank pages, directory depth, folder
  membership).
- The site graph is evaluated embedded inside a larger **composite host
  graph** (both an empirical FineWeb-derived graph and a synthetic
  Barabási–Albert graph), not in isolation — modeling how internal-link
  changes interact with the site's existing external-link ecosystem
  rather than assuming a closed system.
- Two link-selection regimes compared, with ~240-link intervention
  budgets (reflecting realistic editorial capacity):
  - **Automatic** — pure GraphSAGE ranking with load-balancing
    constraints.
  - **Expert-assisted** — SEO professionals (from WordLift) choosing
    from GraphSAGE-ranked candidates, factoring in template
    compatibility, semantic relevance, and implementation feasibility.
- **Core tradeoff finding:** automatic selection produces stronger
  PageRank/authority redistribution but at a semantic cost; expert-
  assisted selection better preserves semantic coherence. Notably,
  expert-selected *low-PageRank* interventions achieved the highest
  authority gains of any regime tested, but with the least favorable
  loss-gain balance (concentrated authority gains funded by authority
  loss elsewhere).
- **Every tested intervention produced a negative semantic-coherence
  change** — adding links beyond a site's original architecture carries
  an inherent topical-coherence cost, even under expert selection.
- Four proposed evaluation metrics, explicitly framed as jointly
  necessary (no single one suffices): **Authority Yield** (marginal
  authority gain per added link), **Authority Volatility** (how stable
  the predicted authority shift is across different embeddings),
  **Authority Down/Up Ratio** (balance of pages losing vs. gaining
  authority), and **Semantic Coherence Change** (topical consistency of
  newly linked page pairs).
- Evaluated on a real 1,841-page production crawl of Kalicube.com,
  across a range of "bridging" (external connectivity) levels.
- Recommended workflow: generate candidate intervention sets at scale,
  score them jointly across authority gain/volatility/loss-gain
  balance/semantic coherence, *then* review for editorial
  deployability — pre-deployment triage rather than post-launch
  attribution guesswork.
- Limitations acknowledged by authors: no behavioral signals used
  (clicks, impressions, crawl frequency), no live A/B testing
  validation — results are "production-crawl evaluation analyses," not
  verified ranking/traffic predictions. Tested on a single domain;
  generalization to e-commerce/news/documentation sites is
  unvalidated. Authors used LLM assistance for coding/writing but state
  they retain accountability for conceptual contributions/conclusions.

## What this updated

- New subsection in [[link-and-anchor-text-best-practices]] on
  pre-deployment evaluation of internal-link interventions and the
  authority-vs-coherence tradeoff.
- Cross-linked from [[ahrefs-internal-links-for-seo]],
  [[yoast-internal-linking-for-seo]], and [[topic-cluster-strategy]].
- No conflicts with existing wiki claims — this is a methodology/
  evaluation-framework addition, not a competing tactic. It doesn't
  resolve or contradict the existing 3-5-links-per-article density
  heuristic or reasonable-surfer guidance; it's a way to test a batch
  of proposed links before publishing them.
