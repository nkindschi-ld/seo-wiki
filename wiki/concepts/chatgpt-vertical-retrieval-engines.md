---
type: concept
tags: [aeo]
updated: 2026-09-17
---

# ChatGPT's Vertical Retrieval Engines

ChatGPT does not run "a web search." It dispatches fan-out sub-queries across a
**registry of ~69 named, specialized retrieval engines**, each scoped to a
content type, topic vertical, recency window, or third-party data provider, and
each paired with a named **query rewriter** that reformulates the sub-query into
that engine's expected syntax.

This is the **engine-selection layer** that sits between query fan-out and
hybrid retrieval in [[ai-search-reranking-pipeline]] — stage 1.5, effectively.
The pipeline page describes retrieval as "hybrid BM25 + vector"; this page
describes *which index* that hybrid retrieval runs against, which turns out to
be a routing decision made before any relevance scoring happens.

Source: [[konitzny-chatgpt-retrieval-leak-engine-list-2026]] — an engine
registry extracted from a ChatGPT server-sent-events (SSE) leak. **Read the
rigor caveats at the bottom of this page before acting on any of it.**

## The two-tier split: internal vs. external

| Tier | Sources | What it means |
|---|---|---|
| **Internal** | `labrador`, `labrador-web` | OpenAI's own indexes — the dominant family, ~47 of the 69 engines |
| **External** | `bing`, `serpapi_auto_*`, `mai_grounding`, `mai_grounding_news`, `getty`, `yelp`, `foursquare`, `fortis`, `fortis_barebone` | Third-party retrieval APIs and data providers |

`labrador` is the internal engine family name. `labrador-web` is a separate
source for general web results, and notably `labrador-web-fallback` is tagged
**external** while `labrador-web` is tagged internal — the same index reached by
two different paths with two different trust/fallback semantics.

## ChatGPT's web backend is plural, not just Bing

The practitioner shorthand "ChatGPT search is Bing-powered" is incomplete. Four
distinct external web/news backends appear side by side:

- **`bing`** — webpages, news, and images (`bing-image`).
- **`serpapi_auto_web` / `serpapi_auto_news` / `serpapi_auto_image`** — SerpAPI
  is a commercial SERP-scraping API, predominantly of **Google**. Its presence
  as a first-class source for web, news, *and* image results implies Google SERP
  data reaches ChatGPT through an intermediary.
- **`mai_grounding` / `mai_grounding_news`** — Microsoft's MAI grounding
  service; the news variant carries a `mai-news-beta` tag, i.e. it was
  in-rollout at capture.
- **`fortis` / `fortis_barebone`** — unidentified. Returns `webpages`, `news`,
  and `business` result types.

Practical read: optimizing only for Bing's index understates the surface. A page
visible in Google but not Bing still has a retrieval path into ChatGPT, and vice
versa. Both feed the same reranker.

## Vertical engines: content-type and topic priors are baked into retrieval

The `labrador` family has dedicated engines per vertical, meaning **content type
is a routing decision, not merely a ranking signal**:

| Vertical | Engines | Rewriter |
|---|---|---|
| Wikipedia | `labrador-wiki`, `labrador-wiki-web`, `system1-wiki`, `system2-wiki` | `bing_query` / system-tier |
| arXiv / literature | `labrador-arxiv`, `labrador-arxiv-web`, `labrador-aixiv`, `system1-arxiv`, `system2-arxiv` | `bing_query`, `literature_search_query` |
| STEM | `labrador-stem`, `system1-stem`, `system2-stem` | tier rewriter |
| Reddit | `labrador-reddit-web`, `system2-reddit` | `bing_query` / `system2_search_query` |
| News | `labrador-news-1d`, `-7d`, `-all`, `-google-redirect-fallback` (+ system1/system2 variants) | `bing_query` / tier rewriter |
| Legal | `labrador-legal`, `labrador-knowledge-legal-text`, `labrador-knowledge-legal-pdf` | `legal_search_query`, `bing_query` |
| Medical | `labrador-knowledge-medical-text`, `labrador-knowledge-medical-pdf` | `bing_query` |
| Finance | `labrador-finance` | `finance_search_query` |
| Local / places | `labrador-local` (result type `places`) | none |
| PDFs | `labrador-web-pdf`, `system2-web-pdf` | `bing_query` / `system2_search_query` |
| YouTube | `labrador-web-youtube`, `system2-web-youtube` | `bing_query` / `system2_search_query` |
| Images | `labrador-images`, `labrador-images-nocache`, `system2-image` | `image_query`, `system2_image_query` |
| Synthetic | `labrador-synthetic`, `labrador-synthetic-index` | `bing_query` |

What this implies for optimization: **format is a retrieval surface.** A PDF, a
YouTube video, a Wikipedia entry, and an arXiv preprint each have their own
dedicated path into ChatGPT's answer — they are not competing in one undifferentiated
web pool. See [[pdf-seo-optimization]] for the PDF case and
[[geo-content-optimization-tactics]] for vertical-path tactics.

Both legal and medical appear as **paired text + PDF engines** — the only two
verticals with that split. In the highest-stakes YMYL domains, authoritative
material is disproportionately PDF-shaped (statutes, filings, clinical
guidelines), and the retrieval layer reflects that.

## News freshness is a path selection, not a ranking tweak

Three explicit recency windows exist as **separate engines**: `news-1d`,
`news-7d`, `news-all`. Freshness is therefore not a score applied within one
news index — the engine chooses a *time-bounded index* up front. A query judged
to need 24-hour news never sees week-old content at all, regardless of its
quality or authority. This sharpens the "freshness by vertical" guidance in
[[geo-content-optimization-tactics]].

There is also a `-news-google-redirect-fallback` path at every tier (plain,
system1, system2), suggesting news retrieval falls back to Google-redirect URLs
when primary news retrieval comes up short.

## System1 / System2: retrieval breadth scales with reasoning tier

Engines carry `system1` or `system2` tags with matching rewriters
(`system1_search_query`, `system2_search_query`, `system1_image_query`,
`system2_image_query`). The two tiers do **not** have equivalent coverage:

- **system1** paths: wiki, arxiv, stem, news (all windows), web fallback,
  mai-grounding web + news, serpapi web/news/image.
- **system2** paths: all of the above *plus* **Reddit, web-PDF, web-YouTube**,
  and a dedicated `system2-image`.

So the deeper-reasoning tier reaches content types the fast tier never touches.
This is a plausible mechanism under the observed "ChatGPT 5.6 retrieves more,
fans out more" shift documented in [[lilyray-chatgpt-fanout-queries-2026]]: more
reasoning may not just mean more queries, but **access to more engine types**.
Consequence: your visibility in ChatGPT can depend on which reasoning mode the
user is in — a PDF or YouTube asset may be invisible to a fast-mode answer and
retrievable in a thinking-mode answer.

## Local retrieval runs on Yelp and Foursquare

The only business/local external sources are **`yelp`** and **`foursquare`**
(both tagged `external, business`, both with `result_types: null` and no
rewriter — suggesting structured lookups rather than query-rewritten search),
plus the internal `labrador-local` returning `places`. `fortis` also returns a
`business` result type.

**No Google Business Profile path appears anywhere in the registry.** If that
holds, local and business-entity visibility inside ChatGPT is mediated by Yelp
and Foursquare listing accuracy — a different dependency than the Google Maps
reliance documented for AI Overviews in [[ai-citation-landscape]] ("Local
queries lean on Google Maps, not articles"). Flagged as a **gap**: the wiki has
no local-AI-visibility playbook, and this single source isn't a sufficient
basis to build one.

## The rewriter layer explains the `site:` operator surge

`bing_query` is the dominant rewriter — applied not only to Bing but to most
**internal** `labrador` engines too. Sub-queries are therefore reformulated into
**Bing-style search syntax** before hitting even OpenAI's own indexes.

This is the mechanical explanation for an empirical finding already in the wiki:
[[lilyray-chatgpt-fanout-queries-2026]] measured `site:` operator usage in
ChatGPT fan-outs jumping from 0.3% to 23%. If fan-out queries pass through a
Bing-syntax rewriter, operator-laden queries are the expected output, not an
anomaly. It also raises the stakes on the domain-confusion risk documented
there — a rewriter that emits `site:wrongdomain.com` removes you from that
entire path.

Vertical-specific rewriters (`literature_search_query`, `finance_search_query`,
`legal_search_query`, `image_query`) indicate query reformulation is itself
domain-aware, not one generic transformation.

## Caution: a dedicated retrieval path is not evidence of citation value

The most-liked comment on the source argues that a separate Reddit engine proves
how much weight Reddit threads carry — "nobody builds a dedicated retrieval path
for a site unless the answers depend on it."

**This inference does not survive contact with the wiki's citation data.** Both
things are true at once:

- Reddit has *two* dedicated retrieval engines (`labrador-reddit-web`,
  `system2-reddit`).
- Reddit is cited at **1.93%** in ChatGPT and accounts for **67.8%** of
  *non-cited* retrieved URLs ([[ahrefs-why-chatgpt-cites-pages-2026]]); Dan
  Petrovic reports ChatGPT discards Reddit retrievals **~99%** of the time
  ([[lilyray-chatgpt-fanout-queries-2026]]).

A dedicated engine is evidence of **retrieval volume and routing intent**, not
of citation outcome. Reddit is the clearest case in the wiki of a source that is
heavily retrieved and rarely cited — exactly the retrieved-but-loses-the-rerank
failure mode in [[ai-search-reranking-pipeline]]. Generalize the rule: reading
an engine registry tells you what *gets fetched*, and citation is decided two
stages later. Don't infer value from the existence of a path.

## Open questions

- **`labrador-synthetic` / `labrador-synthetic-index`** — result types
  `synthetic` and `synthetic-index`. Unexplained. The names suggest an
  OpenAI-generated derived or summarized index layer, which would mean some
  retrieval runs against OpenAI's *representation* of content rather than the
  live page. If so it would be highly consequential for AEO, since it decouples
  what the model retrieves from what you publish. **Speculative — no evidence
  beyond the name.**
- **`fortis` / `fortis_barebone`** — unidentified external engine; webpages,
  news, business.
- **`labrador-aixiv`** — distinct from `labrador-arxiv`, with result type
  `aixiv` and the `literature_search_query` rewriter. Possibly an AI-paper index
  or a typo preserved in config.
- **`labrador-images-nocache`** — a cache-bypassing image path; trigger unknown.
- **Call frequency by engine is unknown.** A commenter asked this directly and
  it is unanswered. The registry is a *capability list*, not a distribution.

## Rigor caveats

- **Single practitioner, unverified leak, no published methodology.** No sample
  size, no collection procedure, no replication. Konitzny is a credible
  practitioner (Peec AI, already cited in this wiki) relaying an extraction by
  Metehan Yesilyurt.
- **An enumerated config is not an active-traffic profile.** Registries routinely
  contain legacy, deprecated, dark-launched, or geo/experiment-gated entries that
  never fire for real users. Without frequency data, every engine here is
  "exists," not "matters."
- **Engine semantics are inferred from names.** `fortis`, `synthetic`, and
  `aixiv` are labelled, not documented. Treat the naming-based readings above as
  hypotheses.
- **Snapshot, not steady state.** The `mai-news-beta` tag proves the registry was
  mid-rollout at capture. This will drift.

**Confidence summary:** high value as a *structural map* of how ChatGPT routes
retrieval; low value as evidence of *how much* any single path matters.

## See also

- [[ai-search-reranking-pipeline]] — the stage model this page slots into;
  engine selection precedes hybrid retrieval and reranking.
- [[lilyray-chatgpt-fanout-queries-2026]] — the empirical fan-out and `site:`
  operator data this registry mechanically explains.
- [[ai-citation-landscape]] — citation outcomes by source type, including the
  Reddit retrieve-heavy/cite-rarely pattern.
- [[geo-content-optimization-tactics]] — vertical-path and freshness tactics.
- [[pdf-seo-optimization]] — the dedicated `web-pdf` retrieval path.
- [[generative-engine-optimization]] — umbrella concept.
