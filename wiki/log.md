# Log

Append-only chronological record of wiki activity. Each entry starts with
a consistent prefix so the file stays greppable, e.g.
`grep "^## \[" wiki/log.md | tail -5`.

Format:
```
## [YYYY-MM-DD] ingest | <source title>
## [YYYY-MM-DD] query | "<question>"
## [YYYY-MM-DD] lint | <summary of findings>
## [YYYY-MM-DD] conflict | <topic> — <one-line description>
```

---

## [2026-07-07] ingest | GEO: Generative Engine Optimization (Aggarwal et al., 2023/2024)

First source ingested. Created [[generative-engine-optimization]] (concept)
and [[geo-content-optimization-tactics]] (playbook). No prior wiki content
existed, so no conflicts to reconcile.

## [2026-07-07] ingest | Google's Guide to Optimizing for Generative AI Features on Google Search

Updated [[generative-engine-optimization]] and
[[geo-content-optimization-tactics]] with Google's official AI-optimization
guidance.

## [2026-07-07] conflict | GEO/AEO tactics vs. Google's official guidance — retrieval-stage vs. citation-stage framing

[[generative-engine-optimization]]: reconciled as addressing different
funnel stages (see Conflicting Evidence section on that page); flagged as
not fully resolved whether Google's AI Overviews respond to GEO's
citation-style tactics the same way third-party generative engines do.

## [2026-07-07] ingest | AI Features and Your Website (Google Search Central)

Extended [[generative-engine-optimization]] with a measurement section
(Search Console "Web" reporting) and created new playbook
[[controlling-ai-feature-inclusion]] for opt-out/control mechanisms.
Agrees with and extends [[google-ai-optimization-guide]]; no conflicts.

## [2026-07-07] ingest | Generative Pulse: What Is AI Reading? (Muck Rack, May 2026)

Created new concept [[ai-citation-landscape]] for empirical citation
patterns across ChatGPT/Claude/Gemini. Added a provider-specific tactics
section to [[geo-content-optimization-tactics]] and cross-linked from
[[generative-engine-optimization]]. Landscape/empirical data, complements
rather than conflicts with existing sources.

## [2026-07-07] ingest | Top Brand Visibility Factors in ChatGPT, AI Mode, and AI Overviews (Ahrefs)

Created new concept [[ai-visibility-correlation-factors]] for the
75k-brand correlation study. Added brand-level correlational guidance to
[[geo-content-optimization-tactics]] (YouTube presence, earned mentions,
ChatGPT-targeting for smaller brands).

## [2026-07-07] conflict | Cross-provider domain-level divergence vs. brand-level mention overlap

[[ai-citation-landscape]] and [[ai-visibility-correlation-factors]]:
reconciled as different units of analysis (which source domains get
cited, vs. whether a brand gets mentioned at all) — see Conflicting
Evidence sections on both pages; flagged as unresolved since no source
has directly tested both at once.

## [2026-07-07] ingest | AIO Impact on Google CTR: 2026 Update (Seer Interactive)

Created new concept [[aio-ctr-impact]] for the citation-premium and CTR
economics data. Added query-format AIO-risk table and an
impressions-vs-clicks measurement checklist to
[[geo-content-optimization-tactics]]; cross-linked from
[[generative-engine-optimization]] as the economic rationale for
citation tactics. No conflicts.

## [2026-07-07] ingest | Google Search Quality Rater Guidelines (Sept 2025 edition)

Created two new concepts: [[e-e-a-t-and-page-quality]] (YMYL, E-E-A-T,
Page Quality tiers, and the three AI-era abuse patterns) and
[[search-intent-and-needs-met]] (query intent taxonomy, Needs Met
scale). Added E-E-A-T signal-building and Know-Simple answer-structuring
guidance to [[geo-content-optimization-tactics]], including an explicit
warning against Scaled Content Abuse. Cross-linked from
[[generative-engine-optimization]] (retrieval-eligibility foundation)
and [[ai-visibility-correlation-factors]] (official policy explanation
for the content-volume finding). No conflicts — this source provides
the official policy foundation several prior sources' findings were
implicitly describing.

## [2026-07-07] ingest | Google Search Status Dashboard — History

Backfilled ~34 dated ranking updates/incidents (July 2021–June 2026)
into `wiki/timeline.md`, extending its earliest entry back from
2023-11-16 to 2021-07-26. Created new concept
[[google-algorithm-update-history]] describing the update-type taxonomy
and the pattern of helpful-content/reviews updates merging into core
updates after 2023. This is a live page — re-ingest periodically for new
entries. No conflicts.

## [2026-07-07] ingest | How Google Search Works

Created new concept [[how-google-search-works]] (crawl/index/serve
pipeline) — the technical foundation underneath "retrieval eligibility"
and "technical crawlability," previously referenced but never defined.
Added a technical crawlability checklist to
[[geo-content-optimization-tactics]]. Cross-linked from
[[generative-engine-optimization]] and [[e-e-a-t-and-page-quality]]. No
conflicts.

## [2026-07-07] ingest | Ranking Factors Study 2024 (Semrush)

Created new concept [[traditional-seo-ranking-factors]] (classic
organic-SERP correlation data) and new playbook
[[classic-seo-ranking-factors]] (kept separate from
[[geo-content-optimization-tactics]] given the latter's growing size and
AEO-specific focus). Cross-linked from [[ai-visibility-correlation-factors]]
(direct classic-vs-AI comparison table) and [[e-e-a-t-and-page-quality]]
(independent empirical confirmation via reviews/star-rating correlation).
No conflicts — reinforces existing findings from an independent,
larger-scale, classic-SERP-focused dataset.

## [2026-07-07] ingest | Make links crawlable (Google Search Central)

Created new source [[google-links-crawlable]] and new playbook
[[link-and-anchor-text-best-practices]] (crawlable `<a href>` markup
requirements, anchor text writing rules, internal/external linking
guidance, `rel` attribute usage). Cross-linked from
[[how-google-search-works]] (links feed the crawling stage's URL
discovery) and [[classic-seo-ranking-factors]] (backlink-building
tactic now points to the link-mechanics playbook). No conflicts —
net-new technical guidance with no prior wiki coverage of link markup
or anchor text.

## [2026-07-07] ingest | Internal Links for SEO: An Actionable Guide (Ahrefs)

Created new source [[ahrefs-internal-links-for-seo]]. Substantially
expanded [[link-and-anchor-text-best-practices]]'s internal-linking
section: pyramid site structure/3-click rule, siloing + topic clusters,
reasonable-surfer link placement, power-page/content-refresh linking,
pagination markup, dofollow/crawler accessibility, and a broken-link/
orphan-page audit workflow.

## [2026-07-07] conflict | ideal number of internal links per page

[[ahrefs-internal-links-for-seo]] recommends 3-5 contextual links per
article as an "optimal" density (PageRank-dilution argument); Google's
own [[google-links-crawlable]] explicitly declines to give a number
("no magical ideal number of links... if you think it's too much, then
it probably is"). Logged as unresolved Conflicting Evidence on
[[link-and-anchor-text-best-practices]] — current best guess: treat
3-5 as a starting heuristic for typical posts, not a hard rule, since
Google is the primary ranking-authoritative source and deliberately
avoids a numeric target.

## [2026-07-07] conflict | ideal number of internal links per page — resolved

User directive: trust Google over Ahrefs on this — no numeric cap on
internal links per page. Updated [[link-and-anchor-text-best-practices]]'s
Conflicting Evidence entry and §4 "Link count" bullet to drop the "3-5"
heuristic and defer entirely to Google's "if you think it's too much,
then it probably is" guidance. Ahrefs' claim remains recorded in the
Conflicting Evidence section for reference, marked superseded rather
than deleted.

## [2026-07-07] ingest | Internal linking for SEO: why and how (Yoast)

Created new source [[yoast-internal-linking-for-seo]]. Added
cornerstone-content two-way linking, taxonomy/tag-page linking hubs, and
related/popular-posts modules to [[link-and-anchor-text-best-practices]]
§4. Cross-linked to [[generative-engine-optimization]] for the source's
GEO/AI-context framing. Noted (not applied) a minor tension: this
source recommends exact-match anchor text "when possible," which leans
more keyword-forward than Google's "avoid keyword stuffing" guidance
already in the playbook — per the user's standing preference to trust
Google over third-party SEO blogs on divergence, kept the playbook's
existing natural/varied anchor-text guidance unchanged. No numeric
link-count claim from this source — consistent with the wiki's current
Google-aligned no-cap position.

## [2026-07-07] ingest | What Claude Code Actually Chooses (Amplifying, Feb 2026)

New topic area: optimizing for coding-agent tool recommendations, not
just chat/search content citation. Created new concept
[[ai-coding-agent-tool-selection]] and new playbook
[[optimizing-for-coding-agent-recommendations]] from
[[amplifying-claude-code-picks-2026]] (2,430-prompt study of Claude
Code's tool picks across 20 categories/4 repos/3 models). Cross-linked
as a sibling domain from [[generative-engine-optimization]] — same
"visibility inside an AI-generated answer" mechanic, different engine
type (coding agent vs. chat/search) and audience (tool vendors vs.
content publishers). No conflicts — first source on this topic.

## [2026-07-07] ingest | Codex vs Claude Code: AI Agent Tool Selection Study (Amplifying, Mar 2026)

Created new source [[amplifying-codex-vs-claude-code-picks-2026]].
Extended [[ai-coding-agent-tool-selection]] with cross-agent findings:
7/12 category agreement (mostly Custom/DIY), parent-company acquisition
bias (Codex/Statsig, Claude/Bun), Cloudflare-vs-Vercel platform
lock-in, and "conversion differs more than awareness." Extended
[[optimizing-for-coding-agent-recommendations]] with a new tactic
(§7): measure and optimize per-agent, since top picks diverge sharply
between Codex and Claude Code outside standardized categories. No
conflicts — complementary follow-up to
[[amplifying-claude-code-picks-2026]], reinforcing its build-over-buy
finding on a second agent and adding acquisition/platform-affinity
data.

## [2026-07-07] ingest | The Consensus Gap (Search Engine Journal, Kevin Indig)

Created new source [[sej-the-consensus-gap]] (3.7M-URL-citation study,
ChatGPT/Perplexity/Google AI Overviews). Added the presence/
portability/concentration measurement framework, the ~2.35-2.45%
universal-overlap finding, and content-type portability ranking to
[[ai-citation-landscape]]. Added a cross-reference note to
[[ai-visibility-correlation-factors]]'s Conflicting Evidence section —
this source independently corroborates the citation-fragmentation
side of that unresolved reconciliation (different engine set,
different methodology, same conclusion) but doesn't resolve the
brand-vs-URL tension since it also measures URL-level, not
brand-level, overlap. Added measurement/prioritization tactics to
[[geo-content-optimization-tactics]]. No new conflicts — strengthens
an existing wiki finding.

## [2026-07-07] ingest | Why AI Engines Cite Different Sources but Recommend the Same Brands (BrightEdge)

Created new source
[[brightedge-ai-search-same-brands-different-sources]] (5-engine
citation study: ChatGPT, Perplexity, Gemini, Google AI Mode, Google AI
Overviews). Added engine sourcing-personality profiles, the
Google-surfaces-aren't-monolithic finding, sentiment data, and the
three-layer source framework to [[ai-citation-landscape]]. Added the
three-layer strategy, category-relative-authority guidance, and
buyer-reliance engine-weighting to [[geo-content-optimization-tactics]].

## [2026-07-07] conflict | citation-source fragmentation vs. brand-mention convergence — resolved

This source directly tests both sides of the previously-unresolved
conflict (flagged 2026-07-07, earlier today) on the same 5-engine
dataset: pairwise source overlap (16-59%) is measurably wider/more
inconsistent than pairwise brand overlap (36-55%) across every engine
pair studied. Updated the Conflicting Evidence sections on
[[ai-citation-landscape]] and [[ai-visibility-correlation-factors]]
from "unresolved, plausible inference" to "resolved, directly tested" —
old claims kept and marked superseded-with-reasoning, not deleted, per
the wiki's conflict-handling convention. One residual methodology
caveat noted (not a contradiction): BrightEdge's aggregate top-100-list
overlap numbers read higher than [[sej-the-consensus-gap]]'s per-prompt
exact-URL overlap, which is a granularity difference between the two
measurement approaches.

## [2026-07-07] ingest | Why Most Original Data Never Gets Cited (Growth Memo)

Created new source
[[growth-memo-why-most-original-data-never-gets-cited]] (analysis of
Gauge's 301-page/1,075-citation dataset). Added a new "Publish
citation-ready primary research/benchmarks" section to
[[geo-content-optimization-tactics]], extending Tier 1's existing
Statistics-Addition/Cite-Sources tactics with the structural finding
that primary research only earns outsized citation density (3.3x) when
packaged as a named-item benchmark comparison, not raw data — plus a
7-characteristic checklist and URL-stability warning (64/365 cited
URLs in the dataset were dead/redirected). No conflicts — first source
on benchmark/primary-research content structure specifically.

## [2026-07-07] ingest | Technical SEO Checklist for Search Engines and AI Search (Semrush)

Created new source [[semrush-technical-seo-checklist]] and new playbook
[[technical-seo-audit-checklist]] (crawling/indexing, UX/Core Web
Vitals, navigation, code/config, and AI grounding/agent readiness
including new ecommerce/agentic-commerce checkout guidance). Navigation
section cross-links to [[link-and-anchor-text-best-practices]] rather
than duplicating it (site-structure/breadcrumbs/orphan-page content
already covered there). Cross-linked from [[how-google-search-works]]
and [[controlling-ai-feature-inclusion]] (opposite goal: ensuring AI
crawlers aren't accidentally blocked, vs. deliberately excluding them).
No conflicts.

## [2026-07-07] ingest | How to Optimize for the Agentic Web (Semrush)

Created new source [[semrush-optimize-for-agentic-web]], new concept
[[agentic-web-optimization]] (the agentic-web definition, five-layer
optimization stack, four emerging protocol standards — MCP/WebMCP/ACP/
UCP), and new playbook [[optimizing-for-the-agentic-web]] (actionable
layers 2-5, cross-linked to [[technical-seo-audit-checklist]] for
layer 1, plus a visibility+action measurement framework). This is a
third sibling domain alongside [[generative-engine-optimization]]
(citation-focused) and [[ai-coding-agent-tool-selection]]
(coding-agent tool picks) — cross-linked from both. Added the "AI
visitor worth 4.4x more in conversion value" stat to [[aio-ctr-impact]]
as a related-but-distinct data point (session conversion value, not
citation-premium CTR). No conflicts — all layers either net-new or
consistent with/complementary to existing wiki content.

## [2026-07-07] ingest | Topics Matter for Third-Party Authority Signals (Growth Memo)
Ingested Kevin Indig/Amanda Johnson's Growth Memo piece on topic-specific
AI source trust. Extended [[ai-citation-landscape]] (topic-level source
trust variance: 33.5% vs. 7% competitor-domain citation share by topic),
[[ai-visibility-correlation-factors]] (Authority Score's 0.65 Pearson
correlation, flagged with a metric-comparability caveat vs. this page's
existing Domain Rating figures), and [[geo-content-optimization-tactics]]
(new "Third-party authority building" section: tiered authority
accumulation, named-author-over-brand-account bylines, and a 6-item
action checklist). No conflicts — all additions extend existing claims.

## [2026-07-07] ingest | Why proprietary data is your most defensible AI citation asset (Growth Memo)
Ingested Kevin Indig/Amanda Johnson's companion piece (2026-06-29, published
~1 week before [[growth-memo-why-most-original-data-never-gets-cited]], on
a different dataset — On-Page.ai information-gain research). Extended
[[geo-content-optimization-tactics]]'s "Publish citation-ready primary
research/benchmarks" section with a quantified placement stat (44.2% of
citations from a page's first 30%), an "ownership doesn't guarantee
citation" note, and information-gain-by-figure-count correlation data
(62.1 vs. 40.2). Cross-linked as a companion source with
[[growth-memo-why-most-original-data-never-gets-cited]] — independent
datasets converging on the same core claim, no conflicts.

## [2026-07-07] ingest | Semrush AI Overviews Study (2025 full-year data)
Ingested Semrush's 10M+-keyword AI Overview study. Extended
[[aio-ctr-impact]] with a full-2025 AIO prevalence trajectory
(6.49%→24.61% peak→15.69%), intent-based expansion, a zero-click-rate
decrease (33.75%→31.53%), industry saturation data, AIO-keyword
characteristics, and SERP feature co-occurrence shifts. Flagged two soft
tensions (not contradictions) against the existing Seer-based intent
prevalence figures and CTR data — different studies/snapshots/metrics,
noted inline rather than resolved as a formal conflict.

## [2026-07-07] ingest | Influence Happens Everywhere (SparkToro, Rand Fishkin)
Ingested SparkToro's clickstream study of the top 5,000 most-visited
sites. Created new concept page [[ai-traffic-scale-vs-hype]]: search+social
≈ half of all visits, Google ~73% of search and bigger than the next 13
sites combined, AI tools ~1/1,000th their press coverage in actual
traffic, influence-precedes-search, attribution bias toward search, and
the case that Google-embedded AI (not standalone AI tools) is the bigger
competitive stake. Cross-linked from [[generative-engine-optimization]]
and [[aio-ctr-impact]] as a scale caveat. No conflicts — this measures a
dimension (overall channel scale) not previously covered in the wiki.

## [2026-07-07] ingest | The Fan-Out Effect: What Happens Between a Query and a Citation (AirOps)
Ingested AirOps/Kevin Indig's large-scale ChatGPT retrieval study
(16,851 queries, 353,799 pages). Added a new "Retrieval rank as the
primary citation gatekeeper" section to [[ai-citation-landscape]]
(58.4% citation at retrieval rank 1 vs. 14.2% at rank 10; bimodal
citation distribution; memory citations). Extended
[[geo-content-optimization-tactics]] with focus-over-comprehensiveness
guidance, structural findings (word count/headings/schema/readability),
and freshness-by-vertical data.

## [2026-07-07] conflict | AI-mention authority correlation — brand-level vs. page-level
AirOps' page-level ChatGPT study found no positive (slightly inverse)
correlation between domain authority/backlinks and citation, contradicting
the brand-level authority correlations in
[[ai-visibility-correlation-factors]] (Ahrefs Domain Rating, 0.266-0.326)
and [[growth-memo-topics-matter-for-third-party-authority]] (Authority
Score, 0.65 Pearson). Added an unresolved Conflicting Evidence section
to [[ai-visibility-correlation-factors]] — current best guess is a
brand-level-vs-page-level unit-of-analysis difference (parallel to the
existing source-vs-brand-overlap resolution on that page), plus a
possible engine-mix artifact (AirOps studies ChatGPT only), but flagged
as genuinely unresolved since no single source tests both at once.

## [2026-07-07] ingest | How to Win the Race for Gen AI Search (Similarweb)
Ingested Similarweb's 38-page tactical GEO playbook (PDF). Extended
[[geo-content-optimization-tactics]] with a five-component intent
framework (task/format/entity/depth/constraint), an AI-reuse formatting
checklist (TL;DR, atomic paragraphs, templates, schema, explicit
entities), an off-page-authority prioritization score (influence ×
prompt frequency), and a net-new "Sentiment monitoring and correction"
section (per-topic sentiment tracking, on-page/off-page correction
levers). Added new playbook [[genai-search-90-day-sprint]] (12-week,
4-phase execution plan). No conflicts — reinforces
[[airops-fan-out-effect-2026]]'s retrieval-rank finding qualitatively
and extends existing tactics with more granular guidance.

## [2026-07-07] ingest | How to Be the Brand AI Recommends (Similarweb)
Ingested Similarweb's companion playbook (Darrell Mordecai, PDF, 18
pages) to [[similarweb-how-to-win-the-race-for-gen-ai-search-2026]].
Added a new "Citations vs. brand mentions" section to
[[ai-citation-landscape]] (mention vs. citation distinction,
training-data-vs-live-retrieval framing, recommendation-vs-citation
signal lists) — reframes [[airops-fan-out-effect-2026]]'s "memory
citations" finding as a training-data-sourced mention. Added Aleyda
Solis's 70-80%-of-prompts sustained-topical-authority measurement target
to [[geo-content-optimization-tactics]]. Noted independent corroboration
of the existing 44.2%-of-citations-from-first-30%-of-page stat (two
sources now agree). Added an AI-visit-vs-referral-growth cross-reference
to [[aio-ctr-impact]]. No conflicts.

## [2026-07-07] ingest | The Downstream Impact of AI Visibility (Similarweb)
Ingested Similarweb's US-desktop-panel study tracing ChatGPT
recommendations to downstream site visits (Finance/Travel/Beauty
verticals, named brand pairs, July-Dec 2025). Added a new "AI
recommendation → downstream visit impact" section to [[aio-ctr-impact]]:
2.5x visit-rate multiplier for AI-recommended brands, ~2x engagement
(pages/time), and a significant attribution caveat — 55.9% of
AI-influenced traffic arrives via search and gets invisibly absorbed
into branded-search analytics rather than counted as AI referral,
suggesting AI's true traffic influence is undercounted by referral-based
measurements like [[ai-traffic-scale-vs-hype]]'s SparkToro data (not a
conflict — an attribution caveat on how to read that data). Cross-linked
from [[ai-citation-landscape]]'s citations-vs-mentions section as direct
measured backing for the "mentions build presence" claim. No conflicts.

## [2026-07-07] ingest | AI Overviews are expanding across commercial intent search (Semrush)
Ingested Semrush's 600K+-keyword follow-up study (same research team as
[[semrush-ai-overviews-study-2025]], later window Nov 2025-Apr 2026).
Added a "Commercial vs. transactional AIO divergence and CPC clustering"
section to [[aio-ctr-impact]]: commercial-intent AIOs grew 71% while
transactional-intent AIOs declined 5% (flagged as a genuine trend shift
continuing the earlier study's peak-then-settle pattern, not a
contradiction), AIOs clustering on highest-CPC keywords, and Google
Ads+AIO coexistence roughly doubling year-over-year. No conflicts.

## [2026-07-08] ingest | Why Server Logs Are Crucial for AI Search Strategy (Peec AI)

Created new source [[peec-ai-server-logs-ai-search-2026]]. Added an
"AI bot types (training vs. indexing vs. retrieval)" subsection to
[[how-google-search-works]]'s Crawling stage, and a server-log
crawl-vs-citation gap-analysis method (§5) to
[[technical-seo-audit-checklist]]. No conflicts — net-new taxonomy and
diagnostic method filling a gap in the existing AI-crawler-access
guidance, which previously only covered the binary
allowed/blocked-in-robots.txt check.

## [2026-07-08] ingest | The Listicle Rank Effect (Peec AI)

Created new source [[peec-ai-listicle-rank-effect-2026]] (~200,000 AI
responses, 5.7M+ data points, 8 engines, Sept 2025-Mar 2026). Added a
"Listicle rank effect" section to [[ai-citation-landscape]], sharpening
[[airops-fan-out-effect-2026]]'s retrieval-rank-as-gatekeeper finding
with a third-party-listicle-specific rank mechanism and market-maturity
breakdown. Added a "Target listicle rank, not just listicle inclusion"
tactic to [[geo-content-optimization-tactics]], extending the existing
third-party authority-building guidance. No conflicts — reinforces and
sharpens the "concentration beats spread" and retrieval-rank findings
already in the wiki.

## [2026-07-08] ingest | Patterns We See in ChatGPT Query Fanouts (Peec AI)

Created new source [[peec-ai-chatgpt-query-fanouts-2026]] (5M query
fanouts, ChatGPT/Perplexity/Grok, April 2026). Added a "Query fanout
mechanics" section to [[ai-citation-landscape]], explaining the
engine-side hidden-subquery injection behavior previously only named
in passing (Google's "query fan-out" term in
[[generative-engine-optimization]]) — explicitly distinguished from
[[airops-fan-out-effect-2026]]'s different fan-out finding (content
subtopic coverage vs. this source's engine-side subquery injection).
Added a "Target common query-fanout injection angles" tactic to
[[geo-content-optimization-tactics]]. No conflicts — clarifies and
extends existing terminology rather than contradicting it.

## [2026-07-08] ingest | Self-Promotional Listicles Analysis (Peec AI)

Created new source [[peec-ai-self-promotional-listicles-2026]] (13,000
listicles, 232,000 citations, 12 weeks Dec 2025-Feb 2026, software
sector, 6 platforms). Added a "Self-promotional listicles still get
cited" section to [[ai-citation-landscape]] (~11% of citations
self-promotional, sharp platform divergence, no algorithmic correction
observed) and a caution note to the listicle-targeting tactic in
[[geo-content-optimization-tactics]]. Not logged as a formal
Conflicting Evidence entry against [[e-e-a-t-and-page-quality]]'s
undisclosed-conflict-of-interest guidance — the two make different
kinds of claims (stated best practice vs. empirical filtering-gap
evidence), noted inline in both pages instead. No factual conflicts.

## [2026-07-08] ingest | Why ChatGPT Cites One Page Over Another (Ahrefs)

Created new source [[ahrefs-why-chatgpt-cites-pages-2026]] (1.4M
ChatGPT prompts, Feb 2025, cosine-similarity semantic analysis
segmented by reference type). Added a "Citation rate by source type
and semantic relevance (ChatGPT)" section to [[ai-citation-landscape]]
(search-index dominance, Reddit's retrieved-but-uncited pattern,
semantic-relevance scores, URL-slug data) and matching tactics to
[[geo-content-optimization-tactics]].

## [2026-07-08] conflict | optimal content age for AI citation

[[ahrefs-why-chatgpt-cites-pages-2026]] finds older/established pages
(median ~500 days) cited more than fresh ones within search-result
retrieval sets, contradicting [[airops-fan-out-effect-2026]]'s 30-89
day optimal-freshness finding. Logged as unresolved Conflicting
Evidence on [[ai-citation-landscape]] and flagged inline in
[[geo-content-optimization-tactics]]'s "Freshness by vertical"
section — current best guess is a reference-type/segmentation
difference (Ahrefs's own news-vertical data does show a freshness
preference, partially consistent with AirOps), but not directly
tested by either source.

## [2026-07-08] ingest | We Studied Over 1 Million Domains to Find the Most Common Technical SEO Issues (Ahrefs)

Created new source [[ahrefs-site-audit-study-2023]] (1,002,165
domains, Ahrefs Site Audit tool, 2023). Added prevalence data and
priority calibration to [[technical-seo-audit-checklist]] §1
(redirect/HTTPS chain-vs-presence distinction) and §4 (title tags
worth fixing, meta descriptions not a ranking factor, alt text as
accessibility-first, multiple/missing H1 low-severity, Open Graph as
social-only). No conflicts — independent large-scale prevalence data
reinforcing and calibrating the existing Semrush-based checklist;
downgrades a few commonly-over-prioritized issues (multiple H1s,
incomplete Open Graph) to explicitly low-priority rather than
contradicting anything already in the wiki.

## [2026-07-08] ingest | Anchor Text: A Data-Driven Guide (Ahrefs)

Created new source [[ahrefs-anchor-text-2020]] (384,614-page + 16,000-
page correlation studies). Added a "Backlink anchor text: don't
manipulate it" section to [[link-and-anchor-text-best-practices]],
extending the existing internal-linking-focused anchor text guidance
with the external/backlink-specific angle: weak-to-negligible
correlation for every anchor type, the don't-manipulate-your-ratio
conclusion, the guest-blogging exception, and Penguin-update history.
Added a matching "don't bother" entry to [[classic-seo-ranking-factors]].
No conflicts — new scope (backlink anchor text vs. the wiki's existing
internal-linking anchor text coverage), directionally consistent with
existing "vary anchor text, avoid keyword stuffing" guidance.

## [2026-07-08] ingest | 43 B2B SEO Statistics for 2025 (Ahrefs)

Created new source [[ahrefs-b2b-seo-statistics-2025]] (a compilation
of 43 third-party B2B SEO/marketing statistics). Selectively applied
the most novel/actionable subset: added an independent 345x traffic-
ratio corroboration to [[ai-traffic-scale-vs-hype]]; added AI Overview
citation-composition data (76% from top-10 organic, 28.9% from top-50
brands) and a citation-without-organic-visibility nuance (28% of
ChatGPT's top-cited pages have zero organic visibility) to
[[ai-citation-landscape]]; added an AI-content-adoption-scale note
(87% of marketers, 42% higher output) to
[[geo-content-optimization-tactics]], cross-linked to the existing
Scaled Content Abuse warning. B2B buyer-journey and general
content-marketing-budget stats archived in the source/raw pages but
not written into playbooks — not directly SEO/AEO-actionable. No
conflicts.

## [2026-07-08] ingest | Why Calling Yourself The Best Could Be Helping Your Competitors Win In AI Search (SEJ, Lily Ray)

Created new source [[sej-why-calling-yourself-the-best-2026]] (323
tracked citation instances, 100 B2B queries). Added a
"Citation-without-recommendation in self-promotional listicles"
section to [[ai-citation-landscape]] (69% failure rate, authority-based
exemptions, reported Google countermeasures) and strengthened the
existing self-promotional-listicle caution in
[[geo-content-optimization-tactics]]. Reconciled inline (not logged as
a formal conflict) against [[peec-ai-self-promotional-listicles-2026]]'s
"no algorithmic correction" finding over the overlapping Dec 2025-Feb
2026 window — the two measure different mechanisms (raw citation rate
vs. citation-to-recommendation conversion and organic-visibility-level
countermeasures), so both can be simultaneously true.

## [2026-07-11] ingest | Google Sitemaps Overview

Created new source [[google-sitemaps-overview]] providing sitemap-specific
deep-dive complementing [[google-search-fundamentals-get-started]]. Key
contributions: metadata types (video, image, news, language) enabling
specialized search features; when sitemaps are needed (500+ pages, new
sites, media-rich content); CMS auto-generation overview; Search Console
monitoring (Sitemaps report, indexation status tracking); critical
limitation that sitemap inclusion doesn't guarantee indexing (sitemaps are
discovery aids, not indexing guarantees). Extended [[technical-seo-audit-checklist]]
§1 with expanded sitemap submission guidance and GSC Sitemaps report
monitoring checklist. No conflicts — supplementary reference providing
sitemap-focused implementation details.

## [2026-07-11] ingest | Inlinks: Entity-Based SEO Guide

Created new source [[inlinks-entity-based-seo-guide]] and new playbook
[[entity-based-seo-implementation]]. This source provides tactical/practical
counterpart to the theoretical foundation in [[entity-oriented-search-fundamentals]].
Key contributions: Google's four-step NLP pipeline (preprocessing → feature extraction
→ model building → inference), three-step implementation framework (entity extraction,
topic cluster expansion, entity-based internal linking), schema markup guidance ("about"
field with sameAs links), measurable impact (440% impressions, 52% CTR in case study),
and critical insight that entity optimization for traditional search simultaneously
optimizes for AI search (both rely on entity recognition). Extended
[[geo-content-optimization-tactics]] with entity extraction and topic clustering as
Tier 1 tactic; extended [[technical-seo-audit-checklist]] §4 with entity schema markup.
No conflicts — directly operationalizes [[entity-oriented-search-fundamentals]] with
actionable three-step framework and measurable results.

## [2026-07-11] ingest | Entity-Oriented Search (Balog, 2018) — Selective academic ingest

Created new source [[entity-oriented-search-balog-2018]] and concept
[[entity-oriented-search-fundamentals]] covering foundational IR theory on
how modern search systems (Google Knowledge Graph, AI systems like ChatGPT)
organize information around *entities* rather than keywords/documents.
Selectively ingested Chapters 1 (Introduction), 5 (Entity Linking), 8
(Leveraging Entities in Document Retrieval); excluded Chapters 3-4, 6-7
(theoretical algorithms outside SEO scope). Key contributions: entity
definition/properties, knowledge base hierarchy (catalog→repository→KB),
entity linking pipeline (mention detection→candidate selection→disambiguation),
entity-based query expansion. Cross-linked from [[generative-engine-optimization]]
(AI systems rely on entity linking to ground responses) and [[how-google-search-works]]
(entity linking is parallel retrieval process to term-based ranking). No
conflicts — foundational theory that complements existing wiki coverage of
AI search mechanisms.

## [2026-07-08] lint | Full-wiki lint pass: 2 missing cross-refs fixed, listicle content split out, timeline re-sorted, bot names updated

Clean: no broken wikilinks, no orphan pages, all source `origin:`
paths resolve, log format consistent. Fixed with user approval:
(1) added [[ahrefs-b2b-seo-statistics-2025]]'s 25.7% AI-freshness-
preference stat and [[muckrack-generative-pulse-ai-reading-may-2026]]'s
recency finding to the unresolved content-age Conflicting Evidence on
[[ai-citation-landscape]]; (2) registered
[[sej-why-calling-yourself-the-best-2026]]'s authority-moderation
finding on [[ai-visibility-correlation-factors]]'s unresolved
authority-correlation conflict (narrows, doesn't resolve); (3) created
[[listicles-in-ai-search]] consolidating the three listicle sections
previously on [[ai-citation-landscape]] (rank effect, self-promo
citation rates, citation-vs-recommendation decoupling) — that page now
points there; (4) one-time chronological re-sort of `wiki/timeline.md`
(68 entries, content unchanged — ingestion order had drifted from
event order; future entries still appended); (5) updated stale
"Claude-Web" bot name in [[technical-seo-audit-checklist]] §5 to
current OpenAI/Anthropic crawler names mapped onto the
training/indexing/retrieval taxonomy, with a note that bot names
should be verified against vendor docs at audit time.

## [2026-07-11] ingest | Google Search Fundamentals: Get Started

Created new source [[google-search-fundamentals-get-started]] (official
Google documentation on technical SEO fundamentals). Extended
[[technical-seo-audit-checklist]] with additional guidance on robots.txt
strategy (crawl control, not indexing control), sitemaps, canonicalization,
mobile-first indexing as the default pattern, schema markup/rich results,
and updated date from 2026-07-08 to 2026-07-11. This is foundational
official guidance reinforcing and extending existing wiki coverage;
no conflicts — all additions cross-link to existing pages and raise
priority on mobile and schema markup guidance in audits.

## [2026-07-11] ingest | Ahrefs: The Beginner's Guide to Technical SEO

Created new source [[ahrefs-beginner-guide-technical-seo]] with practical
prioritization framework and AI-specific risks. Extended
[[technical-seo-audit-checklist]] with: (1) a priority-tier framework
header (high-impact vs. medium-priority projects per Ahrefs finding that
content/links outperform technical work for most sites), (2) new
"AI search-specific technical risks" subsection in §5 covering JS rendering
invisibility to LLMs, third-party blocking (Cloudflare), hallucinated URLs,
code fingerprints, and AI content detection. Extended
[[link-and-anchor-text-best-practices]] with a new "Link recovery and
discovery: High-impact quick wins" section covering the 301-redirect link
recovery tactic (single redirects restore hundreds of cross-domain links)
and the contextual-internal-link-to-existing-rankings discovery pattern.
No conflicts — reinforces and operationalizes the existing link-building
and technical-audit guidance with a prioritization lens and new AI risks.

## [2026-07-11] ingest | OnCrawl: XML Sitemap Optimization

Created new source [[oncrawl-xml-sitemap-optimization]] and new playbook
[[xml-sitemap-optimization-checklist]]. This source provides tactical
operational guidance on sitemap content optimization complementing the
strategic foundation in [[google-sitemaps-overview]]. Key contributions:
the 20% discovery-from-sitemaps stat (vs. 80% from links), money-pages-only
strategy, exclusion rules (non-200 responses, noindexed pages, canonicalized
URLs), protocol compliance, section organization for GSC monitoring, and
crawl budget efficiency principles. No conflicts — the OnCrawl tactics
operationalize Google's "sitemaps are discovery aids" principle with
concrete optimization rules; all findings consistent with [[how-google-search-works]]'s
crawl budget mechanics.

## [2026-07-11] ingest | Google: Robots.txt Introduction

Created new source [[google-robots-txt-intro]], new concept
[[robots-txt-strategy]], and new playbook [[robots-txt-audit-checklist]].
Key contributions: the critical misconception-correction that robots.txt
does NOT prevent indexing (blocked URLs can still rank if externally linked);
robots.txt manages *crawler traffic*, not *indexing control* (use `noindex`
meta tag for that); proper use cases (admin blocking, parameter cleanup,
media filtering); syntax/crawl optimization rules; GSC testing. The concept
page covers what robots.txt is/isn't; the playbook is an operational audit
checklist. No conflicts — all findings align with
[[google-search-fundamentals-get-started]] and [[how-google-search-works]]'s
crawl-stage mechanics. This source fills a critical educational gap:
most SEO practitioners misuse robots.txt for indexing control, a mistake
this source corrects via official Google guidance.

## [2026-07-11] ingest | Ahrefs: Robots.txt Implementation Guide

Created new source [[ahrefs-robots-txt-guide]]. Extended [[robots-txt-strategy]]
with file structure (500KB max, root-only), user-agent breakdown (Googlebot,
Bingbot, Slurp, etc.), and directive types (Disallow/Allow/Sitemap with examples).
Extended [[robots-txt-audit-checklist]] with critical syntax rules: trailing-slash
gotchas (`Disallow: /de` vs. `/de/`), pattern matching (`*`, `$`), subdomain strategy
(separate robots.txt per subdomain), GSC auditing via Coverage and URL Inspection
tools, and dangerous-mistake warnings ("one character = SEO damage"). Key finding:
overly broad directives like `Disallow: /de` unintentionally block `/designer-dresses/`
and `/delivery-info.html` — a real SEO hazard. No conflicts — Ahrefs' tactical
implementation details operationalize Google's strategic framework with concrete
syntax examples and error scenarios.

## [2026-07-11] ingest | Samuel Schmitt, "Topic Clusters Case Study: Key Insights"
Added [[samuelschmitt-topic-cluster-case-study]]. Case study evidence for the
existing pillar/topic-cluster guidance in [[link-and-anchor-text-best-practices]]:
splitting a 3,500-word tutorial into a 5-page pillar+subpage cluster produced
1000% weekly-pageview growth (16,000 pageviews over 5 months), diagnosed via a
Google Search Console keyword-to-section mapping that showed rankings degrading
deeper into the original article. Added a "when to split into a topic cluster"
subsection with the diagnostic method and 7-step build workflow. No conflicts —
extends existing topic-cluster/pillar-page guidance with a concrete before/after
case study and a diagnostic trigger it previously lacked.

## [2026-07-11] ingest | Lidia Infante/Rise at Seven, "The Beginner's Guide to Keyword Mapping"
Added [[riseatseven-keyword-mapping-guide]] and new playbook
[[keyword-mapping-and-cannibalization]] — no prior page covered
keyword-to-page mapping as a discrete process. Captures the 5-step build
process (GA priority pages → seed keyword → ~10 variations via
Ahrefs/Semrush clustering → maintained/tagged map → optimization
roadmap) and the three-failure-mode diagnostic tree (missing content,
non-ranking content, keyword cannibalization). Cross-linked to
[[link-and-anchor-text-best-practices]] (internal-linking diagnostics)
and [[entity-based-seo-implementation]] (the entity-level version of
cannibalization). No conflicts.

## [2026-07-11] ingest | Rachel Handley/Semrush, "Keyword Mapping for SEO"
Added [[semrush-keyword-mapping]]. Agrees with and extends
[[riseatseven-keyword-mapping-guide]]/[[keyword-mapping-and-cannibalization]]:
same core practice, but starts from topic areas + pillar/subpage clustering
(Keyword Strategy Builder) rather than existing GA traffic, and adds
on-page keyword-placement and keyword-map-aware anchor-text tactics.
Updated [[keyword-mapping-and-cannibalization]] with the topic/pillar-first
build variant and the on-page/internal-linking tactics section. No conflicts.

## [2026-07-11] ingest | Google, "Google Images and Google Search"
Added [[google-images-seo]] and new playbook [[image-seo-checklist]] —
no prior page covered image-search-specific SEO. Key points: images
must be real `<img>` elements (CSS backgrounds are never indexed), image
sitemaps for CDN-hosted/otherwise-undiscovered images, alt text as "the
most important attribute," and preferred-image declaration via
`primaryImageOfPage`/`og:image`. The alt-text guidance directly extends
[[ahrefs-site-audit-study-2023]]'s finding that missing alt attributes
are the most common technical SEO issue (80.4% of sites) — pairs the
prevalence data with positive guidance. Cross-linked to
[[xml-sitemap-optimization-checklist]] and [[technical-seo-audit-checklist]].
No conflicts.

## [2026-07-11] ingest | Joshua Hardwick/Ahrefs, "Image SEO: 12 Actionable Tips"
Added [[ahrefs-image-seo]]. Agrees with and substantially extends
[[google-images-seo]]/[[image-seo-checklist]] with tactical/performance
depth: file-type selection rules, compression-tool benchmarks
(ImageOptim/ShortPixel/TinyPNG), an alt-text authoring formula ("This is
a(n) ___ of ___"), image-sitemap XML tags, SVG minification/GZIP, lazy
loading, browser caching, CDN usage (with a CNAME warning to avoid
losing SEO value to the CDN's own domain), and a bonus link-equity
recovery tactic (reclaiming backlinks that point directly at image
files). Updated [[image-seo-checklist]] with all of the above. No
conflicts.

## [2026-07-11] ingest | Steven van Vessum/Conductor, "Content Pruning"
Added [[conductor-content-pruning]] and new playbook
[[content-pruning-playbook]] — no prior page covered content pruning.
Captures the inventory→audit→decide process, cadence (6mo/3mo by site
size), a 4-tier alternatives-to-deletion ladder (improve → consolidate
→ noindex → remove-with-staging), and the recurring practitioner
warning that redirect discipline, not the pruning decision itself, is
what causes lasting traffic loss. Cross-linked to
[[keyword-mapping-and-cannibalization]] (cannibalization is an audit
trigger here, and "merge weak pages" is the same fix that playbook
recommends) and [[technical-seo-audit-checklist]]. No conflicts.

## [2026-07-11] ingest | Sydney Go/Semrush, "Content Pruning"
Added [[semrush-content-pruning]]. Agrees with and extends
[[conductor-content-pruning]]/[[content-pruning-playbook]]: same core
model (refresh/consolidate/remove vs. Conductor's finer 4-way split
that separates out noindex), a more granular 7-step process with a
concrete traffic threshold example (1,000 monthly organic sessions) and
an explicit "check backlinks before removing" step, the 404/broken-
internal-link risk of removal spelled out, and a first-party case study
(Semrush's own blog traffic growth from refreshing). Updated
[[content-pruning-playbook]] with the threshold example, backlink-check
step, removal risk, and case study. No conflicts.

## [2026-07-11] ingest | Garrett Sussman/iPullRank, "How to Optimize for AI Overviews"
Added [[ipullrank-optimize-for-sge]] (2024, oldest tactical AEO source in
the wiki). Extends [[geo-content-optimization-tactics]] with the
underlying chunk-level ("Fraggle") retrieval mechanism behind the
existing focus-over-comprehensiveness finding, a PAA/follow-up-query
keyword-expansion tactic (folded into
[[keyword-mapping-and-cannibalization]]'s expand-variations step),
chunk-relevance-scoring tools (MarketBrew, Orbitwise, SurferSEO,
MarketMuse) with an 80%+ similarity benchmark, and a three-format
(informational/local/shopping) AI-Overview content taxonomy. Noted but
did not resolve a citation-position tension the source itself flags
(93.8% of citations outside top-10 organic vs. a separate study finding
concentration at positions 1/2/9) — different metric from, and not a
direct conflict with, the wiki's existing ChatGPT search-index-citation
data. No new conflicts requiring a Conflicting Evidence section.

## [2026-07-11] ingest | Rich Sanger, "AI Overview Optimization: Insights from Google's Patent"
Added [[richsanger-ai-overview-patent-insights]] (analysis of US patent
11769017B1). Extends [[geo-content-optimization-tactics]] with a
mechanistic, patent-based account of AI Overview selection: two-stage
direct-match-then-embedding-distance verification (a concrete mechanism
underlying the wiki's existing chunk-retrieval and semantic-similarity
findings), position-1/2 link-inclusion rates (53%/~50%), the
related-query pathway's 46%→67% inclusion lift, a YouTube pathway, and
a query-dependent/query-independent/user-dependent evaluation-signal
taxonomy. No conflicts — corroborates and mechanistically explains
existing findings rather than contradicting them.

## [2026-07-11] ingest | Crystal Carter/Wix, "Generative Engine Optimization: LLM Optimization Strategies"
Added [[wix-generative-engine-optimization]]. Introduces a distinction
the wiki hadn't made explicit: GEO/LLM-chat optimization (ChatGPT,
Gemini, Perplexity, Claude as products) is a separate discipline from
Google AI Overview optimization, with a different user journey
(opt-in/interactive vs. passive/non-opt-in). Updated
[[generative-engine-optimization]] with this distinction and a
static/search-augmented/reasoning-model LLM taxonomy. Updated
[[geo-content-optimization-tactics]] with an "LLM-chat-specific
tactics" section: brand-mentions-not-links framing for static models,
the feedback-loop (thumbs up/down) visibility tactic, citation-based
internal linking for search-augmented models, and direct-platform-
engagement tactics (publisher partnerships, custom GPTs, Perplexity
Pages). Updated [[robots-txt-strategy]] with a concrete per-LLM
crawler user-agent table (GPTBot/OAI-SearchBot/ChatGPT-User, BingBot,
Google-Extended, ClaudeBot, PerplexityBot). No conflicts — the
traffic-scale stats cited are consistent with (not contradicting)
[[ai-traffic-scale-vs-hype]]'s framing.

## [2026-07-11] ingest | Gianluca Fiorelli, "The Role of SEO in Making Branding Understood by Search Engines and AI"
Added [[iloveseo-brand-seo-and-ai]] and new playbook
[[brand-entity-seo-strategy]] — treats the brand itself as the entity
to be made machine-legible (distinct from
[[entity-based-seo-implementation]]'s focus on entities within
content). Four-trial framework: Knowledge Graph/Organization-schema
audit (40+ properties, sameAs, parentOrganization/subOrganization,
about/mention), branded query analysis (GSC + competitor + product-
level), a "winning zone" content framework (buyer persona × audience
persona × business objective intersection), and cross-channel
amplification as its own workstream. Also captured Navboost/CTR brand
bias, the 44.19%-of-searches-are-brand-related stat (SparkToro), and
"monosemanticity" as a new disambiguation concept relevant to
[[entity-oriented-search-fundamentals]]. Cross-linked from
[[entity-based-seo-implementation]]. No conflicts.

## [2026-07-11] ingest | Jes Scholz, "Brand Entity SEO: A 5-Step Framework" (Search Engine Land, 2023)
Added [[sel-brand-entity-seo-5-step-framework]]. Agrees with and
operationalizes [[brand-entity-seo-strategy]] (from the prior iloveseo
ingest) with a tighter, sequenced how-to: leadership-sponsorship
business case via branded-SERP/knowledge-panel gap analysis, a
semantic-triple entity bio validated via Google's NL API, a named
corroboration-platform list (CrunchBase/Trustpilot/Yelp/Entrepreneur/
Forbes/GBP/Wikidata) plus fact-checking old digital PR, a concrete
Organization-schema required/optional property split (required:
url+logo; optional: alternateName/legalName/description/image/contact/
award/@id/sameAs) with a reminder to manually submit the About page URL
in GSC, and related-entity markup (people/products/events/podcasts).
Also names the SameAs-consolidation mechanism for disambiguating
fragmented Knowledge Panel URLs. Updated [[brand-entity-seo-strategy]]
with the full 5-step sequence and disambiguation mechanism. No
conflicts — older (2023) source, but purely additive/operational.

## [2026-07-11] ingest | Patrick Stox/Ahrefs, "Enterprise SEO Strategies For Maximum Growth"
Added [[ahrefs-enterprise-seo]] and new playbook
[[enterprise-seo-strategy]] — a new organizational layer above the
wiki's existing tactical playbooks (stakeholder buy-in messaging,
Impact-Effort prioritization, tiered reporting by audience, org
structure/evangelism, content-dev/redirect-matching/content-gap process
frameworks). Where content/link/technical tactics overlapped existing
pages they agreed and extended rather than conflicted: cannibalized-
content consolidation reinforces
[[keyword-mapping-and-cannibalization]]/[[content-pruning-playbook]],
the ~2/3-links-decay-over-9-years stat reinforces the redirect-
discipline guidance in [[content-pruning-playbook]], and unlinked-
mention recovery is the same tactic family as
[[ahrefs-image-seo]]'s link-equity recovery. Cross-linked the new
playbook to all four. No conflicts.

## [2026-07-11] ingest | Jonas Sickler/Terakeet, "Enterprise SEO: A Marketer's Guide to Search Optimization"
Added [[terakeet-enterprise-seo]]. Agrees with and extends
[[ahrefs-enterprise-seo]]/[[enterprise-seo-strategy]] with an older
(2020) but distinct market-share/brand-reputation framing. Updated
[[enterprise-seo-strategy]] with: brand-reputation/SERP-control
strategy (shoring up owned/preferred content ahead of a crisis, tied to
[[geo-content-optimization-tactics]]'s AI-sentiment section as the
classic-SERP counterpart), a 4-tier keyword funnel framework (research/
category/product/branded) layered onto
[[keyword-mapping-and-cannibalization]], content atomization (75%
per-segment customization ratio), named BPM/dashboard tooling
(Process Street/Pipefy/Kissflow, Domo/Tableau/DashThis/Grow), and
publisher/corporate partnership link-building tactics. Flagged the
source's own case-study stats (265% market-share growth, etc.) as
vendor-reported, not independently verified. No conflicts.

## [2026-07-11] ingest | Carlos Silva et al./Semrush, "SaaS SEO: An Actionable Strategy for Growth"
Added [[semrush-saas-seo]] and new playbook [[saas-seo-strategy]] — the
wiki previously had only a single line on SaaS SEO (in
[[enterprise-seo-strategy]]). Captures the persona/problem-over-keyword
and conversion-over-traffic SaaS reframing, the ToFu/MoFu/BoFu funnel
(compatible with, not conflicting with,
[[terakeet-enterprise-seo]]'s 4-tier Research/Category/Product/Branded
framework), a 9-step build process, the SaaS-specific comparison-
keyword ("[Product] vs. [Competitor]") tactic, and in-content
conversion-mechanism tactics (internal linking across funnel stages,
embedded lead capture, trial/demo CTAs). Cross-linked from
[[enterprise-seo-strategy]]'s SaaS note and to
[[keyword-mapping-and-cannibalization]]/[[technical-seo-audit-checklist]].
No conflicts.

## [2026-07-11] ingest | Chris Long/Go Fish Digital, "SaaS SEO: The Ultimate Guide"
Added [[gofishdigital-seo-for-saas]]. Agrees with and extends
[[semrush-saas-seo]]/[[saas-seo-strategy]] with a sharper, more
contrarian core claim: single-vendor product pages rarely rank for
competitive category terms because aggregators (Capterra alone: 750+
category pages) dominate them, since users want to compare multiple
vendors at once. Updated [[saas-seo-strategy]] with a new "aggregator
competition" section (Capterra-mining, reverse-gap analysis, the
84.3-day sales-cycle stat), a features/industries/alternatives page
taxonomy, the "software" terminology tactic, and tangential-content
link building (95-backlinks/69-domains case example). No conflicts —
this source's "alternatives pages" tactic is functionally the same as
[[saas-seo-strategy]]'s existing comparison-keyword step, just named
differently; noted, not duplicated.

## [2026-07-11] ingest | Kevin Indig, "3 Advanced SaaS SEO Strategies & Best Practices" (SEJ, 2020)
Added [[sej-advanced-saas-seo-strategies]]. Extends [[saas-seo-strategy]]
with a scalable-content-format layer not previously covered: learn hubs
(topic-organized knowledge centers with embedded product mentions —
Zapier/Canva examples), marketplace formats (one page template applied
across many entities — Shopify/Zapier examples), and tools/calculators
as self-linking product gateways (Gusto/Splunk examples). Noted a
nuance versus the existing comparison-keyword/alternatives-page
tactics: this source frames "alternatives to X" as a broad resource-
content angle rather than a head-to-head comparison table — a
complementary framing, not a conflict. Updated [[saas-seo-strategy]]
with the new section and checklist item. No conflicts.

## [2026-07-11] ingest | Viola Eva, "Effective SEO Implementation for Software Businesses" (SEJ, 2019)
Added [[sej-seo-software-businesses]]. Extends [[saas-seo-strategy]]
with a site-architecture layer: a mega-menu strategy (present the same
product through multiple navigation lenses — brand/feature, function,
industry, role, task — but link every overlapping category to one
destination page, preventing cannibalization at the navigation-design
stage rather than after the fact) and a Level 1/2/3 silo depth model
with a concrete 10-30-posts-per-silo threshold, sharpening
[[link-and-anchor-text-best-practices]]'s existing general siloing
guidance. Its "most traffic comes from bottom-level posts" finding
reinforces [[gofishdigital-seo-for-saas]]'s aggregator-competition
conclusion. Updated [[saas-seo-strategy]] with the new section. No
conflicts.

## [2026-07-11] lint | Full-wiki lint pass: no orphans/broken links found, 2 missing cross-refs fixed
Checked: (1) every wiki page is linked from at least one other page —
no orphans found; (2) every `[[wikilink]]` target resolves to an
existing page — no broken links (the only unmatched targets were
`[[concept-slug]]`/`[[source-slug]]`, which are template placeholders
in timeline.md's format documentation, not real links); (3) every page
is listed in index.md — confirmed; (4) frontmatter completeness
(type/tags/updated for concepts/playbooks, type/date_ingested/origin
for sources) — all present; (5) existing Conflicting Evidence sections
reviewed — all still accurate, none newly resolvable by today's
ingests (which were mostly SaaS/enterprise/image/pruning topics
unrelated to the open conflicts); (6) real-world-dated sources checked
against timeline.md — today's 18 ingests are evergreen guides/tactics
articles, not dated events, so correctly excluded per CLAUDE.md's
event-vs-activity distinction.
Fixed 2 missing cross-references: added [[image-seo-checklist]] and
[[content-pruning-playbook]] to [[technical-seo-audit-checklist]]'s See
also section; linked [[brand-entity-seo-strategy]] from
[[enterprise-seo-strategy]]'s brand-reputation section.

## [2026-07-21] ingest | How to Write a Great agents.md (GitHub Blog, Matt Nigh)

Created new source [[github-blog-writing-great-agents-md]] (analysis of
2,500+ public `agents.md` files). Off-topic relative to this wiki's core
SEO/AEO scope by default — flagged to the user before filing; user
directed ingest anyway on the basis that instructing coding agents is
part of the AEO-adjacent scope. Created a new pairing distinct from the
existing [[ai-coding-agent-tool-selection]] domain: new concept
[[agents-md-instruction-files]] and new playbook
[[writing-effective-agents-md-files]], covering how repo-owned
instruction files shape a coding agent's *behavior* inside a repo
(specificity divide, six coverage areas, three-tier boundaries,
narrow-specialist-agent taxonomy) — a different layer than that existing
domain's *which tool the agent recommends* focus. Cross-linked both
directions between the two pairs. No conflicts — first source on this
specific sub-topic.

## [2026-07-22] ingest | Optimizing Your Codebase for AI Coding Agents (Aaron Gustafson)

Created new source [[aaron-gustafson-optimizing-codebase-for-ai-agents]]
(first-hand case study of GitHub Copilot's autonomous agent). User
clarified this sub-topic (coding-agent instruction/optimization) is a
standing in-scope part of their role, not a one-off exception — no
longer flagging it as off-topic on future ingests. Extends
[[agents-md-instruction-files]] and [[writing-effective-agents-md-files]]
with two new points beyond specificity/boundaries: consolidating to one
authoritative doc source (vs. scattered/contradictory docs) and building
narrow validation scripts rather than trusting the agent to pick an
efficient check itself, plus quantified stakes (~40% time cost from doc
sprawl, 15+ min token-burning deliberation from unaddressed edge cases;
~40%/~75%/>80% improvement after fixes). No conflicts — complements the
GitHub Blog source's framework with a single case study's numbers.

## [2026-07-22] query | "checklist of best practices for optimizing GitHub repos for coding agents, with why explanations"

Answered from [[agents-md-instruction-files]] and
[[writing-effective-agents-md-files]] — no new synthesis filed, content
already exists as that playbook's 11-item checklist.

## [2026-07-22] ingest | What Fable Actually Chooses (Amplifying, Jul 2026)

Created new source [[amplifying-claude-code-picks-fable-2026]]. Extends
[[ai-coding-agent-tool-selection]] and
[[optimizing-for-coding-agent-recommendations]]: custom/DIY code share
nearly doubled generation-over-generation (11%→21.4%), a new "deferred
buy" pattern (32.5% of custom builds name their own vendor upgrade path
in code comments), a bundling-beats-dedicated-tool finding (PostHog
27% share over LaunchDarkly's 0% in Feature Flags via analytics
bundling — noted as directly relevant to this wiki's operator's own
product category), and a provider-vs-technology distinction. No
conflicts — sharpens and extends the existing build-over-buy/recency
findings from [[amplifying-claude-code-picks-2026]] with a newer model
generation.

## [2026-07-22] ingest | Claude Code Hardcoded Vendor Analysis (Amplifying, Mar 2026)

Created new source [[amplifying-claude-code-hardcoded-vendors-2026]]
(leaked-source analysis of Claude Code's TypeScript, extracted from
public npm source maps). Added a new "Hardcoded platform integration is
a separate visibility layer from model picks" section to
[[ai-coding-agent-tool-selection]] — a genuinely distinct mechanism
(engineering-controlled allowlists: MCP output rendering for 489 tools,
6 "claude.ai-hosted" OAuth connectors, 89 WebFetch-preapproved hosts)
from every other source's training-data/prompting-based dynamic. Added
a largely-non-actionable-but-track-worthy awareness tactic to
[[optimizing-for-coding-agent-recommendations]]. No conflicts — new
mechanism, first source on engineering-level (vs. model-level) vendor
treatment.
