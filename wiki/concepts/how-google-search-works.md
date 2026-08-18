---
type: concept
tags: [seo, aeo]
updated: 2026-07-08
---

# How Google Search Works

The technical pipeline underlying "retrieval eligibility" — referenced
but never defined in [[generative-engine-optimization]] and
[[e-e-a-t-and-page-quality]]. Based on
[[google-how-search-works]]. Three stages, each with its own distinct
failure modes:

## 1. Crawling

Googlebot discovers URLs (via previously-crawled pages, links, and
submitted sitemaps — there's no central page registry) and fetches
content. Crawl frequency/depth per site is decided algorithmically and
throttled to avoid overloading the site. Links only feed discovery if
they're crawlable in the first place — see
[[link-and-anchor-text-best-practices]] for the required `<a href>`
markup.

**Google renders JavaScript** during crawling using a recent Chrome
version — content that only appears after JS execution is visible to
Google, but this is also a common failure point: if rendering fails or
times out, JS-dependent content may never be seen at all.

Common crawling failures: server/network problems, or `robots.txt`
rules blocking access (deliberately, via
[[controlling-ai-feature-inclusion]]-style directives, or by accident).

### AI bot types (training vs. indexing vs. retrieval)

Per [[peec-ai-server-logs-ai-search-2026]], AI-search crawlers split
into three functionally distinct categories, each worth distinguishing
in server-log analysis:

- **Training bots** (e.g. GPTBot, Common Crawl) — gather data to build
  a model's baseline knowledge. Training data only refreshes at
  retraining time, so crawl access *now* shapes what a future model
  generation knows, not what the current one already knows.
- **Search/indexing bots** (e.g. OAI-SearchBot) — build the retrieval
  pool for AI search/citation. A page unreachable to these bots is not
  eligible to be surfaced at all — the AI-search analogue of Google's
  indexing stage.
- **User query/retrieval bots** (e.g. ChatGPT-User) — fetch specific
  pages live, per individual user query. Unlike the other two, these
  visits are request-driven, not crawl-driven.

A healthy crawl pattern shows all three bot types visiting a site; see
[[technical-seo-audit-checklist]] for the log-vs-citation diagnostic
method built on this taxonomy.

## 2. Indexing

Google analyzes crawled content (text, title elements, alt attributes,
images, video) and decides what the page is about. Includes
**canonicalization**: clustering duplicate/near-duplicate pages and
picking a representative canonical version, plus collecting signals
(language, geographic relevance, usability) for later ranking use.

**Indexing is not guaranteed** even for crawled pages: "not every page
that Google processes will be indexed." Common causes: low-quality
content (see [[e-e-a-t-and-page-quality]]'s Page Quality tiers),
`robots` meta rules disallowing indexing, or crawl-unfriendly site
architecture.

## 3. Serving

Ranking happens programmatically against "hundreds of factors,"
including location, language, and device — the same query can
legitimately produce very different results (and different SERP
features, like local packs or image results) depending on context and
intent (see [[search-intent-and-needs-met]]).

**A page can be indexed but never served** for a given query — this is
a distinct failure mode from crawling or indexing failure, caused by
irrelevance, low quality, or `robots` meta rules blocking serving
specifically.

## No pay-to-play at any stage

Google explicitly states it doesn't accept payment for more frequent
crawling, indexing, or higher ranking — all three stages are automated
and programmatic.

## Practical relevance

This pipeline is the technical foundation underneath
[[generative-engine-optimization]]'s "retrieval eligibility" concept and
[[google-ai-optimization-guide]]'s framing that generative AI features
are "rooted in our core Search ranking and quality systems" — if content
isn't crawled, isn't indexed, or isn't served for a relevant query, it
can never become a candidate source for an AI-generated answer either.

## See also

- [[e-e-a-t-and-page-quality]] — the quality assessment that determines
  indexing/ranking eligibility once a page is technically crawlable.
- [[search-intent-and-needs-met]] — how serving-stage relevancy
  judgments work once a page is indexed.
- [[geo-content-optimization-tactics]] — technical crawlability
  checklist drawn from this source.
- [[link-and-anchor-text-best-practices]] — the link-markup and anchor
  text rules that determine whether links actually feed URL discovery.
- [[technical-seo-audit-checklist]] — a consolidated, practitioner-
  checklist audit against this crawl/index/serve pipeline: robots.txt,
  redirects, Core Web Vitals, Schema, and AI/agent crawler access.
- [[peec-ai-server-logs-ai-search-2026]] — source for the AI bot-type
  taxonomy (training/indexing/retrieval) above.
- [[lexical-ranking-tf-idf-bm25]] — the TF-IDF/BM25 scoring mechanics
  that run inside the serving/retrieval stage of this pipeline.
