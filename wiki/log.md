# Log

Append-only chronological record of wiki activity. Each entry starts with
a consistent prefix so the file stays greppable, e.g.
`grep "^## \[" wiki/log.md | tail -5`.

## [2026-08-20] ingest | "What we can learn from evolving ChatGPT fan-out queries" (Lily Ray)
[[lilyray-chatgpt-fanout-queries-2026]] — secondary aggregation (undisclosed methodology
throughout, treat as directional) of ~7 researchers' findings on ChatGPT's evolving fan-out
behavior. Updated [[ai-citation-landscape]] with a "ChatGPT fan-out escalation and `site:`
operator targeting" addendum (fan-out volume jump tied to an apparent model update, `site:`
usage 0.3%→23%, a retrieval-vs-citation divergence, a quantified decides-before-it-searches
citation rate 68.9% vs 2.1%, and a domain-confusion/phishing-adjacent risk). Updated
[[geo-content-optimization-tactics]] with a new `site:`-operator/official-domain-signaling
tactic section (GSC/Bing `site:`-impression monitoring, title-tag/meta clarification,
crawlable-HTML pricing/specs). No conflicts with existing wiki claims — read as a
time-series continuation of [[peec-ai-chatgpt-query-fanouts-2026]] and a sharper number on
[[ahrefs-why-chatgpt-cites-pages-2026]]'s existing Reddit retrieve-not-cite finding.

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

## [2026-07-22] ingest | "What Is Generative Engine Optimization (GEO)" (Search Engine Land, Leigh McKenzie)

Created new source
[[sel-what-is-generative-engine-optimization-geo-2026]]. A general GEO
explainer that mostly corroborates existing wiki claims
([[generative-engine-optimization]],
[[geo-content-optimization-tactics]],
[[wix-generative-engine-optimization]]) rather than extending them —
filed as a supporting citation there. Contributed three genuinely new
data points: a 40-60% month-to-month citation-source volatility figure
added to [[ai-citation-landscape]]; absolute ChatGPT (800M+ weekly)/
Gemini (750M+ monthly) user-base counts and a Tally-ChatGPT-#1-referral
anecdote added to [[ai-traffic-scale-vs-hype]] as a companion to that
page's existing relative-scale ("1/1,000th") framing. No conflicts.

## [2026-07-22] ingest | "Google AI Overviews: The Ultimate Guide to Ranking in 2025" (Single Grain, Eric Siu)

Created new source
[[singlegrain-google-ai-overviews-ultimate-guide-2025]]. A marketing-
agency round-up with no disclosed methodology for any of its stats;
most of its 15 tactics restate existing [[geo-content-optimization-tactics]]
guidance. Added two unverified/lower-confidence additions to
[[geo-content-optimization-tactics]] (query-length AIO-trigger
correlation, 50-70 word direct-answer heuristic). Also flagged as
unverified a position-based CTR-decline stat added to
[[aio-ctr-impact]].

## [2026-07-22] conflict | AIO prevalence & local-query trigger rate — SingleGrain vs. Seer/Semrush

[[aio-ctr-impact]]: SingleGrain claims 50%+ of all search results show
an AI Overview and only ~7% of local queries trigger one. Both conflict
with existing higher-rigor sources: [[semrush-ai-overviews-study-2025]]
(10M+ keywords) shows prevalence settling at 15.69% (Nov 2025), and
[[sel-what-is-generative-engine-optimization-geo-2026]] independently
corroborates ~16%; separately, this wiki's existing Seer-sourced data
(25M impressions) shows "near me" queries triggering AIOs 76.9% of the
time, over 10x SingleGrain's local-query figure. Logged as unresolved
Conflicting Evidence on [[aio-ctr-impact]] — current best guess favors
the higher-rigor, disclosed-methodology sources on prevalence; the
local-query gap is flagged as a likely definitional mismatch (local-
vertical categories vs. "near me" query format) rather than resolved.

## [2026-07-22] ingest | "Top ways to ensure your content performs well in Google's AI experiences on Search" (Google Search Central Blog, John Mueller, May 2025)

Created new source [[google-succeeding-in-ai-search-2025-05]]. The
earliest official Google guidance in this wiki on AI-search
optimization — confirms existing claims already sourced to
[[google-ai-features-appearance-guide]] and [[google-ai-optimization-guide]]
(nosnippet/data-nosnippet/max-snippet/noindex controls, higher-quality
AI Overview clicks, helpful/people-first content) were Google's
position as early as May 2025, not new. Added two minor tips to
[[technical-seo-audit-checklist]]: structured data must visibly match
the page, and page-experience issues (clutter, latency, cross-device
display) apply to AI-referred visitors specifically. No conflicts.

## [2026-07-22] ingest | "SearchGPT Optimization: 2026 Guide" (First Page Sage, Evan Bailyn)

Created new source
[[firstpagesage-searchgpt-optimization-2025-guide]]. A marketing-
agency guide with no disclosed methodology behind its five-factor
"algorithm" model; most tactics restate existing
[[geo-content-optimization-tactics]] guidance. Added a new lower-
confidence "Awards, credentials, and directory placements" section,
expanded the review-platform list (Clutch, CNET, TrustPilot, BBB), and
added Hoovers/Bloomberg to the directory-placement tactic. Also added
this source as a supporting citation on
[[ai-visibility-correlation-factors]]'s existing unresolved domain-
authority-vs-AI-citation Conflicting Evidence (doesn't resolve it —
just adds another voice to the "authority matters" side).

## [2026-07-22] ingest | "What Is ChatGPT Search & How Does It Work?" (Semrush, Rachel Handley)

Created new source [[semrush-chatgpt-search]]. Higher rigor than the
recent marketing-agency guides (named research-team byline); most
tactics restate existing [[geo-content-optimization-tactics]] guidance.
Added the ChatGPT-Search-retrieves-from-Bing-too detail (extends the
existing Copilot-follows-Bing observation) and a smaller-sites-ranked-
fairly anecdote to [[generative-engine-optimization]]; added an earlier
(Nov 2024) 28x Google-vs-ChatGPT traffic baseline and a Gartner 2028
organic-traffic-halving forecast to [[ai-traffic-scale-vs-hype]]; added
SearchGPT prototype (2024-07-25) and ChatGPT Search integration
(2024-10-31) launch dates to the timeline. No conflicts — the 28x
figure is an earlier/narrower-scope data point, not a contradiction of
the existing 345x/1,000x figures.

## [2026-07-22] ingest | "LLMO: 10 Ways to Work Your Brand Into AI Answers" (Ahrefs, Louise Linehan)

Created new source [[ahrefs-llm-optimization]]. Added a "Brand-building
LLMO tactics" section to [[geo-content-optimization-tactics]] (semantic-
proximity PR/entity-embedding mechanism, entity-research tools, the
Wikipedia four-requirement checklist, Reddit UGC investment, brand-
question research, and a schema-markup-isn't-an-LLM-signal correction)
and a new "Known adversarial risk: LLM recommendation manipulation"
awareness note (Harvard-study-sourced prompt-injection attack data —
documented for defensive monitoring, not recommended as a tactic). Added
a corroborating data point (organic rank ~0.65 correlated with LLM brand
mentions; backlinks neutral, per a cited Seer Interactive study) to
[[ai-visibility-correlation-factors]]'s existing unresolved authority-
correlation Conflicting Evidence section. No conflicts — this source
largely operationalizes and corroborates existing findings; the
quotes/statistics/citations uplift table it cites reports the same
tactic set as [[geo-generative-engine-optimization-aggarwal-2023]] with
different exact figures (not confirmed whether same study cited
differently or a separate replication — noted on the source page, not
logged as a formal conflict since directionally identical).

## [2026-07-22] ingest | "How To Integrate GEO With SEO" (Search Engine Land, Christina Adame)

Created new source [[sel-integrate-geo-with-seo]] (no disclosed
methodology — practitioner framework piece quoting Crystal Carter/Wix).
Added a named "retrievability" fourth-pipeline-stage framing
(crawlability→indexability→rankability→retrievability) and a
Presence/Recognition/Accessibility breakdown to
[[generative-engine-optimization]], with an explicit naming-collision
note against [[sej-the-consensus-gap]]'s existing
Presence/Portability/Concentration framework (same word "Presence,"
different meaning — not a factual conflict). Added a GA4-regex
AI-referral-traffic filter and a citation-monitoring-automation tactic to
[[geo-content-optimization-tactics]]'s measurement section. Added a
"ChatGPT reaches 400M weekly active users (Feb 2025)" milestone to
`wiki/timeline.md`, chronologically placed between the existing
2025-01-08 and 2025-03-13 entries — an earlier data point than
[[ai-traffic-scale-vs-hype]]'s current 800M+ figure, not a contradiction.
Most of the source's on-page/off-page/technical checklists restate
existing [[geo-content-optimization-tactics]],
[[entity-based-seo-implementation]], and [[brand-entity-seo-strategy]]
content, so were not duplicated. No conflicts.

## [2026-07-22] ingest | "AI Optimization: How to Optimize Your Content for AI Search and Agents" (Search Engine Land, Jed White)

Created new source [[sel-ai-optimization-content-for-search-and-agents]]
(author runs a competing AI search product, Andi; performance stats have
no disclosed sample/methodology — treated as directional). Extended
[[robots-txt-strategy]]'s per-LLM crawler table with new bot names
(`GoogleOther`, `AndiBot`, `ExaBot`, `PhindBot`, `YouBot`,
`FirecrawlAgent`, `CCBot`) and a concrete three-category allow/disallow
robots.txt template (allow AI search/agent bots, disallow AI
training-data bots, allow traditional search). Extended
[[technical-seo-audit-checklist]]'s AI-specific technical risks section
with a which-crawlers-render-JS breakdown (only Gemini/AppleBot),
an AWS-WAF mitigation (allow major U.S. datacenter IP ranges), tight
1-5-second retrieval-timeout constraints, and AI-crawler efficiency/
error-rate benchmarks (34% error rate, 47x inefficiency vs. Googlebot,
~28% of Googlebot's volume). Extended
[[optimizing-for-the-agentic-web]]'s Layer 4 with "agent-responsive
design"/ARIA-labeling guidance for computer-use agents and a
lighter-weight programmatic-access (API/RSS) option. Added an inline
scope-difference note (not a formal Conflicting Evidence entry) to
[[geo-content-optimization-tactics]]'s existing "don't bother with
llms.txt" guidance — this source recommends creating one for the
broader AI-crawler ecosystem, while Google's existing guidance is scoped
specifically to its own AI Overviews/AI Mode; neither source tests the
other's scope directly. No formal conflicts logged.

## [2026-07-22] ingest | "SEO Case Study: How We Influenced the ChatGPT Search Results" (Go Fish Digital, Chris Long)

Created new source [[gofishdigital-chatgpt-search-case-study]] (n=1
anecdote, single company/query, no disclosed measurement methodology).
Added an "edit an already-cited page directly" tactic to
[[geo-content-optimization-tactics]]'s LLM-chat-specific tactics section,
alongside the existing cited-page-internal-linking tactic — extends it
with a concrete example (adding a key-value-pair "Notable Clients"
section to an already-ChatGPT-cited listicle surfaced results within
~1 week) and a first (single-data-point) figure for GEO edit-to-
visibility latency. Reinforces rather than conflicts with the existing
ChatGPT-Search-retrieves-via-Bing finding from [[semrush-chatgpt-search]].
No conflicts.

## [2026-07-22] ingest | "The Complete 10-Step Guide to Generative Engine Optimization (GEO) in 2026" (Superlines, Jere Meriluoto)

Created new source [[superlines-geo-guide]] — vendor content marketing
(author's company sells GEO visibility-tracking software), undisclosed
methodology throughout, several statistics attributed secondhand to
third parties (Forrester, Adobe, a Kevin Indig LinkedIn analysis)
without verifiable direct citation. Added a three-layer AI search model
(Training Data/High-Volume AI Search/Agentic AI, a retrieval-speed
taxonomy distinguished from the existing LLM-product taxonomy) to
[[generative-engine-optimization]]. Added a named GEO KPI matrix
(Citation Frequency, AI Brand Visibility, Share of Voice, Context
Accuracy, Prompt Coverage, Assisted Conversions) to
[[geo-content-optimization-tactics]]'s measurement section, with
benchmarks explicitly flagged as vendor-sourced/unverified. Added an
unsourced "2-7 domains cited per response" citation-concentration claim
to [[ai-citation-landscape]], flagged as directional/unconfirmed.
Deliberately did not propagate the source's budget/team-structure
guidance or secondhand market-adoption statistics (2.5B daily prompts,
71%/89%/87% figures, 2030 traffic-crossover prediction) — no disclosed
basis and this wiki already has more directly-sourced data via
[[ai-traffic-scale-vs-hype]]. No conflicts — the llms.txt recommendation
adds a second voice to the already-flagged unresolved scope question on
[[geo-content-optimization-tactics]] rather than a new conflict; most of
the 10-step framework restates existing tactics under new naming.

## [2026-07-22] ingest | "How we're adapting SEO for LLMs and AI Search" (Vercel, Kevin Corbett & Malte Ubl)

Created new source [[vercel-adapting-seo-for-llms]] — engineering-team
blog post with first-party company data, higher credibility than most
GEO blog content ingested so far (though the specific 34.5%
click-reduction and Tally ARR figures have no disclosed independent
methodology beyond the companies' own reporting). Added a first-party
ChatGPT-referral-signup growth case study (Vercel: 1%→4.8%→10% of new
signups) and quantified Tally ARR figures ($2M→$3M in 4 months) to
[[ai-traffic-scale-vs-hype]], extending the existing Tally "#1 referral
source" anecdote. Added the 34.5% AI-Overview click-reduction figure to
[[aio-ctr-impact]] as a lower-confidence corroborating data point
(directionally consistent with, not independent confirmation of, the
page's existing ~38%-below-baseline finding). Added "frontier concept
identification" (first-mover topic ownership), a "could a competitor
replicate this tomorrow" authorship depth test, an expanded organic-
citation-seeding channel list with a paid-vs-organic training-data
weighting nuance, and a 30/90/180-day content refresh cadence to
[[geo-content-optimization-tactics]]. Added an SSR/SSG/ISR remediation
for the JS-rendering-invisible-to-AI-crawlers risk to
[[technical-seo-audit-checklist]]. Added Meta AI as a third
Bing-dependent product to [[generative-engine-optimization]]'s
search-augmented-LLM section. No conflicts — corroborates and extends
existing findings throughout.

## [2026-07-22] ingest | "The AI Mention Effect" (Profound, Nikolas Laskaris)

Created new source [[tryprofound-ai-mention-effect]] — a 2M+-conversation,
Jan-Jun 2026 backward-placebo study of AI-mention-to-downstream-visit
lift across ChatGPT/Gemini/Google AI Overviews. Added a per-platform
visit-lift breakdown (Gemini +145%, Google AI Overviews +61%, ChatGPT
+48%), industry variation, and a timing distribution (20.5% of visits
within 1 hour, 42% within 24 hours) to [[aio-ctr-impact]], extending
(not conflicting with) [[similarweb-downstream-impact-of-ai-visibility-2026]]'s
existing 2.5x visit-rate multiplier. Added a precisely-quantified
attribution gap (~2.5% of downstream visits carry any trackable
AI-referral parameter, even after ChatGPT's May 2026 more-clickable-links
update) to [[aio-ctr-impact]] and [[ai-citation-landscape]], sharpening
the existing 55.9%-arrives-via-search finding. No conflicts.

## [2026-07-22] ingest | "The Shortlist is the New Shelf" (Profound, Kevin Indig/Eric Van Buskirk/Jasman Singh)

Created new source [[tryprofound-shortlist-is-the-new-shelf]] and new
concept page [[ai-shortlist-effect]] — a 56-participant, 221-task
session study (video/think-aloud) plus a 6,882-citation share-of-voice
analysis, the first source in this wiki connecting AI *visibility*
directly to an actual *purchase decision outcome*. Core finding: chosen
brands had ~2x the share of voice of rejected brands in ChatGPT answers
(24% vs. 11%), correlation 0.57, ranging from 0.97 (grocery) to -0.98
(coaching, reversed) by category. Added a purchase-decision-stage
tactic set ("Structure content for ChatGPT-generated comparison grids")
to [[geo-content-optimization-tactics]]: grid inclusion, "best for X"
labels, pricing accuracy, and disclosed downsides as four framing
levers independent of raw visibility. Cross-linked from
[[ai-visibility-correlation-factors]] (appearing vs. being chosen) and
[[listicles-in-ai-search]] (third-party listicle citation vs. this
source's live in-chat comparison grid, a related but distinct
mechanism). No conflicts — extends existing zero-click and visibility-
correlation findings with a new outcome variable.

## [2026-07-22] ingest | "C-SEO Bench: Does Conversational SEO Work?" (Puerto et al., NeurIPS 2025)

Created new source [[c-seo-bench-2025]] — a NeurIPS 2025 benchmark
(6 domains, 4 LLMs, 16.3k documents, multi-actor competitive adoption)
directly re-testing the exact tactics behind
[[geo-generative-engine-optimization-aggarwal-2023]]'s Tier 1-3 GEO
tactics, using a citation-rank metric instead of the original
word-count metric. Result: only 3 of 54 method×domain tests showed a
significant positive effect (LLM Guidance, Content Improvement, each in
1-2 domains only), no tactic was significant for Claude 3.5 Haiku or
for question-answering, several tactics (especially Statistics) were
significantly negative in most tested settings, and moving a document
to position 1 in the LLM's context (traditional SEO/retrieval rank)
produced gains several times larger than any content tactic. Also
introduces a new finding for this wiki: C-SEO behaves as a congested,
zero-sum game under competitive multi-actor adoption.

## [2026-07-22] conflict | GEO Tier 1-3 content tactics vs. citation-rank re-test

[[c-seo-bench-2025]] directly challenges
[[geo-generative-engine-optimization-aggarwal-2023]]'s Tier 1-3 tactic
rankings in [[geo-content-optimization-tactics]] and the "traditional
SEO doesn't transfer" framing in [[generative-engine-optimization]].
Added Conflicting Evidence sections to both pages rather than
overwriting the original tactic list: current best guess is that this
reflects a genuine metric-choice difference (word count vs. citation
rank) rather than a clean reversal, but citation rank is the more
decision-relevant outcome for GEO/AEO purposes, so confidence in the
Tier 1-3 rankings is significantly downweighted pending further
replication. Independently corroborates (via a controlled experiment)
[[airops-fan-out-effect-2026]]'s retrieval-rank-as-gatekeeper finding
in [[ai-citation-landscape]] — cross-linked there too.

## [2026-07-22] ingest | "White Hat Search Engine Optimization using Large Language Models" (Bardas et al., Technion, arXiv 2025)

Created new source [[bardas-white-hat-seo-llm-2025]] — an academic
competitive-search paper (a different tradition from the GEO/AEO
citation studies elsewhere in this wiki) showing that prompting an LLM
(GPT-4o) to edit a document using past-ranking context (Pairwise and
Listwise context outperformed Pointwise and Temporal) beats both human
editors and a supervised feature-based baseline on classic ad hoc
retrieval rankers (LambdaMART, E5 cosine similarity), including in a
live online competition against unaware human students. Added a
research note to [[geo-content-optimization-tactics]] flagging this as
not yet real-world-applicable, since the method requires observing past
rankings — a limitation [[c-seo-bench-2025]] independently flags about
this exact paper in its own related-work section, so both sources are
now cross-linked. No conflicts — a genuinely new method not previously
covered, filed with an explicit applicability caveat rather than as an
actionable tactic.

## [2026-07-22] ingest | "Manipulating Large Language Models to Increase Product Visibility" (Kumar & Lakkaraju, Harvard, arXiv 2024)

Created new source [[kumar-lakkaraju-manipulating-llms-2024]] — the
primary source behind a black-hat adversarial-risk note already in this
wiki (previously cited only secondhand via [[ahrefs-llm-optimization]]).
Verified findings: a GCG-optimized "Strategic Text Sequence" on Llama-2
took a near-invisible fictitious product to the top recommendation
within ~100 iterations; rank-advantage rate under randomized product
order rose from ~40% (fixed-order-optimized attack) to ~95%
(order-robust-optimized attack) for a low-visibility product, and from
a net-neutral ~15%/~15% to ~48% for an already-competitive product —
order-robust optimization is the key lever, not the base attack.

## [2026-07-22] conflict | secondhand citation inaccuracy — "34% to 59.4%" figure not in the primary source

Verified [[ahrefs-llm-optimization]]'s claim that the Kumar & Lakkaraju
paper found a preference-manipulation attack "raised a fake product's
recommendation rate from 34% to 59.4%" against the primary paper
([[kumar-lakkaraju-manipulating-llms-2024]]) — that specific figure does
not appear anywhere in it. Corrected [[geo-content-optimization-tactics]]'s
"Known adversarial risk" section to the verified primary-source figures
rather than deleting the original claim silently; added a correction
note to [[ahrefs-llm-optimization]] pointing to the fix rather than
editing what that source page records Ahrefs as having said. The
underlying vulnerability's *existence* is confirmed by the primary
source — only the specific numbers were inaccurate.

## [2026-07-22] ingest | Search Results Diversification in Competitive Search (Mordo et al., 2025)

Filed [[mordo-diversification-competitive-search-2025]]. Same
competitive-search research tradition and overlapping authorship with
[[bardas-white-hat-seo-llm-2025]], but studies the ranking-function
side rather than the editing side: proves game-theoretically and shows
empirically (40-student ranking competition) that adding search-results
diversification (MMR) to a ranking function still yields a stable
equilibrium while shifting publishers from "mimicking the winner" to
differentiating for 2nd place, ameliorating the herding effect
documented in prior work (Raifer et al. 2017, Goren et al. 2021). New
research thread for this wiki — no conflict with existing claims. Filed
a new concept page, [[competitive-search-herding-and-diversification]],
to hold the herding/diversification mechanism and a flagged (untested)
hypothesis about its relevance to AI-answer-engine citation
diversification.

## [2026-07-22] ingest | Where SEO Is Going: The 2026 State of AI Search (Rankability)

Filed [[rankability-where-seo-is-going-2026]]. Two-tier source: primary
Google Keyword Planner demand data (3,751 keywords, 48 months) is
genuinely new to this wiki and filed as a new concept page,
[[seo-aeo-geo-search-demand-trends]] — SEO interest's first sustained
decline (-30% off its mid-2025 peak) while AI search demand keeps
accelerating (3.6x since 2022), AEO/GEO's 0-to-named-to-plateau arc with
a volume-vs-usage naming tension (GEO 2x AEO's volume, but AEO winning
as the professional label), and AI agents' hype-to-deployment
volatility. Two secondary, undisclosed-inline-sourcing claims intersect
with existing conflicts and were added as unverified data points rather
than resolutions: a ~48% AIO-prevalence figure (added to
[[aio-ctr-impact]]'s existing 50%+-vs-15-16% Conflicting Evidence), and
a 75%→17-38% ranking/citation-overlap-decline claim (added to
[[ai-citation-landscape]]'s existing 76%-top-10-vs-93.8%-not-top-10
tension). No conflict logged as resolved by this source.

## [2026-07-22] ingest | The URL AI Citation Study 2026 (Otterly.ai)

Filed [[otterly-url-ai-citations-study-2026]] (1.03M URLs, 1.93M
citation instances, 6 engines, disclosed Pearson-correlation
methodology). Two findings independently corroborate existing wiki
claims using different metrics: page-type citation frequency (guide
+42%, pricing -21%) matches the existing content-type-portability
ranking in [[ai-citation-landscape]]; and its power-law citation
concentration (15.8% of URLs generate 50% of citations) gives disclosed-
methodology support to a previously-unsourced Superlines concentration
claim. One genuine nuance flagged (not a formal conflict): this study's
near-zero correlation for URL structural mechanics (length, hyphens,
digits, question-pattern wording) sits in tension with Ahrefs'
ChatGPT-specific natural-language-URL-slug finding (89.78% vs. 81.11%)
already in the wiki — noted inline rather than logged as a resolved or
unresolved Conflicting Evidence entry, since the two studies measure
overlapping but not identical things. Added a new actionable tactic
(clean canonical URLs, +24% citations) to
[[geo-content-optimization-tactics]].

## [2026-07-22] ingest | 1 in 8 Social Media AI Citations Point to LinkedIn (Otterly.ai)

Filed [[otterly-linkedin-ai-citations-study-2026]] (2.06M citation
records, 384K LinkedIn URLs, 6 engines, disclosed methodology, Jan-Jun
2026) — same author/methodology family as
[[otterly-url-ai-citations-study-2026]], narrowed to LinkedIn. Strongly
corroborates and precisely quantifies an existing but vaguely-sourced
claim in [[geo-content-optimization-tactics]] (named authors outperform
brand pages: 91.7% vs. 8.3% citation share). Adds three genuinely new
findings to [[ai-citation-landscape]]: engagement metrics (likes,
comments, video/image presence) show near-zero correlation with AI
citation — the first source in this wiki to test this directly; an even
steeper LinkedIn-specific citation power law than the general-web study;
and a correlational, cause-unexamined gender disparity in citation share
(76.4% men / 23.5% women among identifiable individual authors),
reported factually with an explicit caveat that the study doesn't
establish whether this reflects underlying authorship demographics or
engine-side bias. Added LinkedIn-specific tactics (Pulse articles over
posts, engagement-metric warning, per-engine targeting) to
[[geo-content-optimization-tactics]]. No conflicts logged.

## [2026-07-22] ingest | An Analysis of AI Overview Brand Visibility Factors (Ahrefs, 2025-05-26)

Identified this article as the earlier, single-platform (AI Overviews
only) predecessor of the already-ingested Dec 2025 study,
[[ahrefs-ai-brand-visibility-correlations]] — same authors and
methodology, correlation figures consistent with the narrow end of the
existing ranges. Rather than file a duplicate source page, added a
"Predecessor article" note to the existing source page and folded its
few new data points (a 10x visibility-cliff stat between the top and
50-75th web-mention percentiles, a 26%-zero-AI-mentions figure, and
three additional weak-correlate factors: referring domains, URL Rating,
site pages) into [[ai-visibility-correlation-factors]]. No conflict
with existing claims. Passed on a second candidate ingest this session
(SEOmator's secondhand summary of a Profound/Brighton SEO 2025 talk) at
the user's direction.

## [2026-07-22] ingest | How to Optimize Content for AI Search: The Complete Guide (Otterly.ai, 2026)

Filed [[otterly-how-to-optimize-content-for-ai-search-2026]]. Mostly a
tactics guide restating content already covered in
[[geo-content-optimization-tactics]] and [[robots-txt-strategy]] — not
individually re-filed. Four genuinely new/notable additions: (1) a
BrightEdge-sourced (no link given) counter-claim that top-10-organic/
AI-citation overlap *grew* from 32.3% to 54.5%, added to
[[ai-citation-landscape]] directly against
[[rankability-where-seo-is-going-2026]]'s already-unverified claim that
this same overlap *collapsed* — now two contradicting unverified voices
rather than one, question left genuinely open; (2) a first-party
OtterlyAI FAQ-schema experiment (+350% citations) added to
[[geo-content-optimization-tactics]]; (3) a secondhand Monash freshness
figure (26% fresher) added to the existing freshness Conflicting
Evidence in [[ai-citation-landscape]]; (4) an undisclosed-source
daily-query-volume-by-engine table added to [[ai-traffic-scale-vs-hype]].
The article's headline "+40% visibility" GEO-paper stat was already in
the wiki with fuller (skeptical) context from [[c-seo-bench-2025]] —
no action needed there.

## [2026-07-22] ingest | AI Keyword Research in 2026 (Otterly.ai)

Filed [[otterly-ai-keyword-research-2026]] — same author, heavy overlap
with the prior same-day Otterly ingest (identical query-volume, FAQ-lift,
citation-breakdown, and referral-traffic figures; not re-filed). Two
genuinely new additions: (1) OtterlyAI's own real-vs-estimated-prompt
research (real prompts average 15.1 words vs. 8.8 estimated, 52%
personal pronouns, 78.9% tool-finding intent vs. 62.5%) added as a new
keyword-research tactic in [[geo-content-optimization-tactics]]; (2) a
2025 OtterlyAI experiment finding llms.txt, author schema, and YouTube
content all show no measurable citation lift, while Wikipedia,
LinkedIn Pulse, FAQ-on-homepage, and digital PR do — added to
[[geo-content-optimization-tactics]] (llms.txt/author-schema) and
[[ai-visibility-correlation-factors]] (YouTube, flagged as a nuance
against the existing YouTube-mentions-correlate-strongest finding
rather than a contradiction, since mention-correlation and
content-citation-lift are different mechanisms). Skipped two
low-rigor, undisclosed-methodology stats (15%-of-traffic-from-AI-bots,
granular Gemini/Perplexity referral-share figures) per the plan agreed
with the user.

## [2026-07-23] ingest | The YouTube Citation Study 2026 (Otterly.ai)

Filed [[otterly-youtube-ai-citation-study-2026]] — same author/
methodology family as the prior Otterly URL and LinkedIn studies,
100M+ citation instances, 6 engines, 30-day window, narrowed to
YouTube. Updated [[ai-citation-landscape]]'s YouTube-by-provider section
with a sharper per-engine breakdown (Perplexity 38.7%, Google AI
Overviews 36.6% vs. ChatGPT 4.4%, Gemini 0.2%, Copilot 0.5%) and new
video-structure findings (94% long-form vs. 5.7% Shorts; timestamped/
chapter citations exclusive to Google AI Overviews/AI Mode; popularity
signals uncorrelated with citation). Added YouTube-specific tactics to
[[geo-content-optimization-tactics]] (long-form over Shorts, chapters
for Google surfaces, description-as-metadata, ignore view/subscriber
counts).

## [2026-07-23] conflict | YouTube-per-provider-citation-share — Gemini figure

The new study's Gemini figure (0.2% of Gemini's citations are YouTube)
diverges sharply from an existing, vaguer estimate
([[muckrack-generative-pulse-ai-reading-may-2026]] via
[[ai-citation-landscape]]) that put YouTube at "~2% of citations for
both ChatGPT and Gemini" — an order-of-magnitude gap on the Gemini side
specifically, while the ChatGPT side (4.4% vs. ~2%) is directionally
consistent. Flagged inline in [[ai-citation-landscape]] as an unresolved
discrepancy rather than a resolved contradiction, since no source
directly reconciles the two measurements.

## [2026-07-23] query | "SEO/AEO visibility suggestions for launchdarkly.com/blog/observability-is-not-enough"

Audited the LaunchDarkly blog post "Observability is not enough" against
[[geo-content-optimization-tactics]], [[technical-seo-audit-checklist]],
[[link-and-anchor-text-best-practices]], [[entity-based-seo-implementation]],
[[saas-seo-strategy]], [[e-e-a-t-and-page-quality]], and
[[search-intent-and-needs-met]]. Key gaps flagged: no FAQ schema (Otterly's
+350% citation-lift tactic), no TL;DR/short-answer block in the first 30% of
the page, only 4 H2s with no sub-structure, no comparison table for the
"observability vs. runtime control" framing despite it being the article's
core thesis, and an author byline (Content Marketing Manager) that doesn't
establish technical E-E-A-T on a reliability/YMYL-adjacent topic. Answer
delivered in chat, not filed as a new wiki page (one-off page audit, not a
durable claim/tactic).

## [2026-07-23] ingest | Active Reddit Communities Get Cited x9 Times More (Otterly.ai)

Filed [[otterly-reddit-geo-ai-search-citations-2026]] — controlled
experiment (60 days, 8,167 citations, 126 subreddits, 5 engines) with
causal (treatment vs. control) design, distinct from earlier Otterly
correlational studies. Added Reddit-community-engagement subsection to
[[ai-citation-landscape]] and Reddit engagement tactics to
[[geo-content-optimization-tactics]]. Key finding: active community
engagement (replies/discussion) drives a 9x citation multiplier on Reddit
— the strongest platform-specific lever measured across all Otterly
studies to date. Comments matter more than upvotes; community size
doesn't predict citations. Bonus: Reddit engagement also boosts
traditional search rankings (x18 SEO impact) from the same content.

## [2026-07-23] ingest | Claude AI Citations Study: How to Get Cited in 2026 (Otterly.ai)

Filed [[otterly-claude-ai-citation-study-2026]] — Claude-specific citation
analysis (379K citations, June 2026), same author as earlier Otterly URL/
YouTube/Reddit studies. Updated [[ai-citation-landscape]]'s "Providers are
separate environments" and "Wikipedia, Reddit, YouTube" sections with
Claude's extreme brand-content dominance (64% first-party, vs. ChatGPT/
Gemini/Perplexity's mixed sources) and social-media immateriality (0.9%,
Reddit literally 0 citations). Updated [[geo-content-optimization-tactics]]
with Claude-specific tactics (invest in official docs and institutional
sources, not forums/reviews/social; opposite of other-engine strategy).
Top 10 domains = only 9.5% of citations (long-tail distribution, not
power-law concentration).

## [2026-07-23] ingest | Measuring Your AI Brand Footprint (Whole Whale, 2025)

Filed [[wholewhale-ai-brand-footprint-measurement]]. Created new concept
[[ai-visibility-measurement-methodology]] addressing the measurement gap
in standard analytics tools (GSC/Bing don't expose AI impression counts).
Key contribution: the reverse-engineered-impressions formula (AI-Sourced
Traffic ÷ Estimated CTR, with a 2% baseline from Search Engine Land 2025)
and a framework for identifying AI-sourced traffic manually. Added the
proprietary AI Brand Footprint™ metric, tool landscape (Trakkr, Evertune),
and Gen-Z consumer-behavior context (70%+ prefer AI assistants for
research) to the new concept. Noted unresolved tensions: universal CTR
baseline is likely context-dependent (by platform/format/intent), and
reverse-engineered impressions are a proxy, not direct measurement. No
conflicts with existing claims — fills a measurement-methodology gap not
previously covered in the wiki's AEO guidance (which focused on tactics/
correlation-factors but not how to measure baseline AI visibility).

## [2026-07-23] ingest | Generative AI Performance Report (Google Search Console Help)

Filed [[google-generative-ai-performance-report]]. Google Search
Console now ships a dedicated report tracking impressions from AI
Overviews and AI Mode specifically (by page, country, date, device),
distinct from filtering the general Performance report by "Web" search
type as previously documented ([[google-ai-features-appearance-guide]],
2025-12-10). Treated as an update/refinement, not a conflict — updated
[[generative-engine-optimization]] and [[controlling-ai-feature-inclusion]]
to point to the new dedicated report as the more precise measurement
tool, and updated [[ai-visibility-measurement-methodology]] to note the
measurement gap is now partially closed for Google's own AI surfaces
(third-party engines — ChatGPT, Claude, Gemini standalone, Perplexity —
still have no native impression exposure, so the reverse-engineering
approach there stands unchanged). No confirmed publish/rollout date
recoverable from the source, so no timeline entry added.

## [2026-07-23] ingest | AI Performance in Bing Webmaster Tools (Bing Help Documentation)

Filed [[bing-ai-performance-report]] (content pasted directly by the
user as HTML — an initial automated fetch of the URL returned no
substantive body content, so treat provenance as user-supplied rather
than independently re-verified). Bing Webmaster Tools ships a dedicated
"AI Performance Report" for Copilot/Bing AI summaries/partner
integrations, tracking **citations** (not impressions) by page and
"grounding query," plus four preview features: Intents (query-intent
classification), Topics (thematic query grouping), Citation Share
(relative citation presence per query, competitor-blind), and Compare
(period-over-period overlay).

## [2026-07-23] conflict | ai-visibility-measurement-methodology — Bing native-tracking claim corrected

The concept page's intro previously stated flatly that "Bing Webmaster
Tools provide[s] no native AI-impression tracking." [[bing-ai-performance-report]]
shows this is no longer true — Bing now has a dedicated citation-tracking
report, paralleling [[google-generative-ai-performance-report]] for
Google. Corrected the claim in place (not treated as a real evidentiary
conflict between two sources — the old claim was simply time-bound and
Bing shipped the feature since). Also flagged a genuine measurement-unit
distinction going forward: Google's tool reports *impressions*, Bing's
reports *citations* — not directly comparable numbers. Added a
corroborating (not new) Bing/Copilot tactics note to
[[geo-content-optimization-tactics]].

## [2026-07-23] ingest | How to Track AI Search Traffic to Your Site in GA4 (seoClarity, Mark Traphagen, 2025-03-25)

Filed [[seoclarity-track-ai-search-traffic]]. Agrees with and extends
existing guidance — no conflicts. Added the article's GA4 UI walkthrough
(Traffic Acquisition detail report + Session Source/Medium column +
"Matches Partial Regex" filter) to
[[geo-content-optimization-tactics]]'s existing AI-referral-traffic
regex-filter tactic as a step-by-step complement, plus its anecdotal
"700% spike in some industries" figure (no industry/timeframe given).
Added seoClarity's vendor-described "AI Search Visibility" tool (part of
"Clarity ArcAI") to [[ai-visibility-measurement-methodology]]'s Tool
Landscape, alongside Trakkr/Evertune — flagged as vendor marketing
content, not independently verified.

## [2026-07-23] ingest | The Rise of the AI Crawler (Vercel, 2024-12-17)

Filed [[vercel-rise-of-the-ai-crawler]]. First-party one-month
traffic-log study across Vercel's hosting network — real data, not a
vendor survey. Agrees with and strengthens existing claims — no
conflicts. Key contribution: independently confirms the previously
"undisclosed methodology, treat directionally" claim
([[sel-ai-optimization-content-for-search-and-agents]]) that only
Gemini/AppleBot render JavaScript among major AI crawlers, now
corroborated by real traffic data. Added new findings to
[[technical-seo-audit-checklist]] §5: AI-crawler request-volume
comparison (28% of Googlebot's volume combined), a crawl-inefficiency
finding (ChatGPT/Claude ~35% 404 rate + ChatGPT 14.36% redirect waste,
vs. Googlebot's 8.22%/1.49%) as a new audit checklist item, and
U.S.-only AI-crawler data-center geography as an IP-allowlisting note.
Added a timeline entry (2024-12-17, real publish date).

## [2026-07-23] ingest | AI Crawlers & Bots Directory (StackFox)

Filed [[stackfox-ai-crawlers-directory]]. A living third-party
directory, not a dated article — individual bot names/purposes sit
behind an interactive accordion UI that automated fetching couldn't
extract, so only organization-level bot counts were captured (~94+
bots across ~28+ organizations). Treated as a reference pointer, not a
citable finding: flagged a real coverage gap in [[robots-txt-strategy]]
(the wiki's per-LLM user-agent table covers ChatGPT/Copilot/Gemini/
Claude/Perplexity/Andi/Exa/Phind/You.com/Firecrawl/Common Crawl but not
Meta, Amazon, xAI, ByteDance, Cohere, Mistral AI, DeepSeek, Allen
Institute for AI, Zhipu AI, or Apple) and added a pointer to this
directory rather than fabricating unverified user-agent strings. No
conflicts. No timeline entry (no publish date — living tool).

## [2026-07-23] ingest | When Search Engine Services Meet Large Language Models: Visions and Challenges (Xiong et al., arXiv, 2024-07)

Filed [[xiong-et-al-search-engines-meet-llms-2024]]. Academic
survey (Baidu-adjacent authorship — treat framing as industry-adjacent,
not fully independent). Agrees with and provides technical/academic
grounding for existing practitioner-level claims — no conflicts. Added
a "Technical grounding" subsection to [[generative-engine-optimization]]
under "Retrievability," naming RAG (Retrieval-Augmented Generation) as
the actual mechanism behind AI-citation behavior — context injection at
inference time, explaining why rankability alone doesn't guarantee
citation. Added the survey's "explainability gap" framing to
[[ai-visibility-measurement-methodology]] as a structural (not just
tooling-lag) explanation for why native measurement tools report only
sampled/aggregated activity rather than a full per-citation audit
trail. Added a timeline entry (2024-07, approximate — arXiv gave month
only).

## [2026-07-23] ingest | As It Was: Aligning LLM Search Evaluation with Historical User Preferences (Vardasbi et al., Spotify, SIGIR '26, 2026-07-01)

Filed [[vardasbi-et-al-as-it-was-llm-search-evaluation-2026]]. A
Spotify music-search LLM-as-judge evaluation paper — adjacent domain,
not web-AEO directly, included for a narrow methodological reason.
Finding: "plain" semantic-only LLM judges measurably diverge from real
user preference (especially ambiguous/long-tail queries); grounding
the judge in historical behavioral interaction data (QRI cards, IPS-
debiased) improves alignment (~5% Spearman correlation overall, +91% on
disagreement cases) but leaves absolute online-preference alignment
"moderate." Added as a caveat to [[generative-engine-optimization]]'s
existing "Subjective Impression" (7-facet LLM-judged) visibility metric
— not a conflict with any existing wiki claim, but a reason to treat
purely-LLM-judged AI-visibility scores as directional rather than
ground truth. Added a timeline entry (2026-07-01, real publish date).

## [2026-07-23] ingest | AI Platform Citation Patterns (Profound, Nick Lafferty, 2025-06-05, updated 2025-08)

Filed [[tryprofound-ai-platform-citation-patterns]]. 680M-citation,
10-month (Aug 2024–Jun 2025) study of ChatGPT/Google AI Overviews/
Perplexity citation sourcing. Mostly agrees with and adds a new
data point to [[ai-citation-landscape]]'s existing per-provider
sourcing findings (added as a new addendum subsection under
"Wikipedia, Reddit, and YouTube diverge sharply by provider"), plus a
new aggregate domain-TLD data point (.com 80.41%, .org 11.29%). Added
a timeline entry (2025-06-05, real publish date).

## [2026-07-23] conflict | ai-citation-landscape — two unresolved magnitude tensions vs. brightedge

[[tryprofound-ai-platform-citation-patterns]] surfaces two magnitude
discrepancies against [[brightedge-ai-search-same-brands-different-sources]]
that don't resolve cleanly: (1) Perplexity's Reddit share here (6.6% of
total, 46.7% of top 10 — a "community-driven" profile) is in tension
with brightedge's "research librarian," low-UGC (1.5%) characterization
of Perplexity; (2) Google AI Overviews' YouTube share here (1.9%) is an
order of magnitude below brightedge's "single video platform = 10.6%
of AI Overviews citations." Both are plausibly explained by different
sampling windows or citation-counting methodology rather than a real
behavior shift, but neither source reconciles the other — flagged in
[[ai-citation-landscape]] as open discrepancies, not resolved in either
direction. Current best guess: treat both studies' per-engine
percentages as directional rather than precise, pending a source that
explains the gap.

## [2026-07-23] ingest | Ranking Manipulation for Conversational Search Engines (Pfrommer et al., UC Berkeley, EMNLP 2024)

Filed [[pfrommer-et-al-ranking-manipulation-conversational-search-2024]].
Peer-reviewed EMNLP 2024 paper. Agrees with and extends existing
guidance — closes an explicitly flagged gap rather than conflicting:
[[geo-content-optimization-tactics]]'s "Known adversarial risk" section
(sourced from [[kumar-lakkaraju-manipulating-llms-2024]]) had noted that
paper's gradient-based attack was "not independently retested... on
production black-box systems." This paper supplies exactly that test
for a different attack family (tree-of-attacks jailbreaking) on a
different production system (Perplexity, via Sonar Large Online as a
surrogate) and finds the vulnerability holds without white-box access.
Updated [[geo-content-optimization-tactics]] accordingly. Added a
timeline entry (2024-11-12, EMNLP conference date).

## [2026-07-24] query | "Review the AgentControl 'Agent optimization' Confluence draft for traditional-search and LLM/AEO optimization — title, headings, formatting, keyword targeting"

Reviewed a Confluence content draft (LaunchDarkly's AgentControl Agent
Optimization feature explainer) against [[geo-content-optimization-tactics]],
[[technical-seo-audit-checklist]], and [[keyword-mapping-and-cannibalization]],
plus live Semrush keyword-volume data (`type=phrase_this`/`phrase_related`
API calls, not an ingested source — no wiki/sources page created for this
one-off pull). Findings delivered in chat, not filed as a new wiki page since
the draft itself is an internal LD asset, not an external source: (1) title/H1
should target category terms, not the near-zero-volume product-name term;
(2) headings should shift from marketing phrasing to query-shaped H2s per the
existing heading-query-match tactic; (3) draft has zero tables/lists/TL;DR
despite content that maps well onto this wiki's benchmark-comparison and
AI-reuse-formatting tactics; (4) flagged a page-hygiene issue outside SEO
scope — the draft contains two near-duplicate stacked copies of the same
content. Added one durable, generalizable lesson to
[[keyword-mapping-and-cannibalization]] (see below) since it's a pattern
likely to recur for other LD feature-launch content, not just this draft.

## [2026-07-27] ingest | How to Audit Your AI Entity Footprint (Rich Sanger, Search Engine Land)

Ingested Rich Sanger's "AI entity footprint audit" framework
([[sel-ai-entity-footprint-audit]]) — same author as
[[richsanger-ai-overview-patent-insights]]. Created a new playbook
[[ai-entity-footprint-audit]] capturing the six audit dimensions (identity,
differentiation, evidence, consistency, relationships, specialization), the
four signal categories (owned/customer/third-party/ecosystem), the 0–5
per-dimension scoring rubric, the 6-step audit process (starting with a "tell
me everything you know about [Business]" multi-platform probe), and the
industry-variation notes. No conflicts — the piece operationalizes and sits
upstream of existing pages. Cross-linked it as a diagnostic layer from
[[brand-entity-seo-strategy]] (which *builds* the entity signals this audit
inspects; bumped its `updated` date) and distinguished it in
[[ai-visibility-measurement-methodology]] (measures citation/traffic *outcomes*;
this measures whether AI *understands* the brand — an upstream prerequisite).
Grounded conceptually in [[entity-oriented-search-fundamentals]].

## [2026-07-29] ingest | Which AI Actually Reads Your Site? Two Months of LLM Traffic, Measured (Evil Martians)

First-party, two-month server-log study (268K agent vs. 107K human requests)
— a direct companion to [[vercel-rise-of-the-ai-crawler]]. Created source page
[[evilmartians-which-ai-reads-your-site-2026]]. Mostly corroborating/extending,
no conflicts. Three genuinely new contributions filed: (1) **content
negotiation** (`Accept: text/markdown`) is the mechanism that actually
delivers Markdown to coding agents (Claude Code 76%), added as a new §5 item in
[[technical-seo-audit-checklist]] with the caveat that ChatGPT-User (~73% of
traffic, HTML-almost-exclusively) keeps rendered-HTML quality primary; (2) the
most direct `llms.txt` null result yet — barely *fetched* (~37 named-assistant
fetches / two months), plus a hidden `<link>` "AI hint" with zero attributable
fetches — added to [[geo-content-optimization-tactics]]'s "don't bother"
section, one step beyond [[otterly-ai-keyword-research-2026]]'s no-citation-lift
result; (3) "segment user agents before analyzing" caution + versioned-slug /
wrong-TLD URL-hallucination patterns, folded into the §5 server-log and
hallucinated-URL items. Noted a scope caution: the study's "reads HTML" is a
format-negotiation finding, not a JS-execution finding (distinct from Vercel's).

## [2026-07-29] query | "outline for DevRel talk: why LD must show up in LLM/coding-agent responses + how"
Guided the user (SEO/AEO Manager) through building a ~15-min educate/awareness
talk outline for the DevRel team, grounded in the wiki
([[ai-coding-agent-tool-selection]], [[optimizing-for-coding-agent-recommendations]],
[[geo-content-optimization-tactics]], [[ai-shortlist-effect]],
[[brand-entity-seo-strategy]]) and internal Glean docs (coding-agent optimization
research report, GitHub/docs AEO audit, DevRel strategy). Anchored on the
0%-primary-picks/38%-mention "known but rejected" LD finding and the PostHog
bundling win. Filed the result as a working-draft playbook
[[launchdarkly-ai-visibility-devrel-brief]] (owner will update); updated index.

## [2026-07-29] update | [[launchdarkly-ai-visibility-devrel-brief]] v2 — reframed around current positioning
Per owner request, simplified the [[ai-shortlist-effect]] line ("showing up in the
AI's answer is most of what gets you picked") and rebuilt the brief around LD's
May-2026 repositioning as "the runtime control layer for the AI era" (CodeControl +
AgentControl; feature flags = foundation, not focus). Grounded in Glean: Platform
Messaging Framework, AI deal deck, homepage, DevRel strategy. New spine: AI's mental
model of LD is stale, so the reposition stalls in the channel where developers form
first impressions; AgentControl is a young, unclaimed category to win early. Updated
index entry.

## [2026-07-30] ingest | Semrush × Growth Memo — The State of Topic Authority in ChatGPT
Semrush/Kevin Indig study of 1,094 US ChatGPT categories (Jan–Jun 2026; 220K+
domains, 600K+ citations). Created concept [[topical-authority-in-ai-search]]
(ownership distribution: 15.2% clear owner / 31.2% emerging / 53.7% unsettled;
inverse-demand paradox; ~5-point mention-share stability moat, 90.4% MoM retention;
mentions-vs-citations decoupling -0.229). Created source page
[[semrush-chatgpt-topic-authority-study]]. Updated [[ai-visibility-correlation-factors]]
(owner-vs-runner-up win-rates: branded search 55.7%, organic traffic 48.4%, Authority
Score 52.5% — near-coin-flips; only branded search significant; folded into the
Authority Score conflict thread with the Kevin-Indig-authored-both-studies wrinkle),
[[ai-citation-landscape]] (empirical mention/citation decoupling), and
[[geo-content-optimization-tactics]] (new "pick winnable topics, defend the 5-point
moat" prioritization section). Cross-linked [[ai-shortlist-effect]]. Updated index.

## [2026-07-30] ingest | Victorious Q2 2026 Quarterly Search Report (recognition vs. mentions)
Michael Transon/Victorious cross-vertical study (175 brands, 8 platforms, 49,391
citations; SEJ-published). Created source [[victorious-q2-2026-quarterly-search-report]].
Headline recognition-vs-mention gap: 96% of brands described accurately but 89% never
appeared in category-research answers. Updated [[ai-visibility-correlation-factors]]
(referring-domains 0.49 / third-party-mentions 0.45 correlates, <2,000-pages→3% floor,
99.99% third-party citation), [[topical-authority-in-ai-search]] (recognition-mention
gap as "most brands unowned" corroboration), [[ai-citation-landscape]] (third-party
citation dominance + 0.10%-naming-on-problem-prompts, >12x down-funnel lift),
[[geo-content-optimization-tactics]] (stage-matched + vertical-specific off-site
strategy), and [[launchdarkly-ai-visibility-devrel-brief]] (external backing for the
"known but rejected" hook). Updated index.

## [2026-07-31] query | "SEO/GEO/AEO on-page optimization for /blog/safe-innovation-generative-ai-financial-services/"
Reviewed the LaunchDarkly GenAI-in-financial-services blog against
[[link-and-anchor-text-best-practices]], [[geo-content-optimization-tactics]], and the
seo-meta-tags skill specs. Grounded in the page's GSC export (90d: 775 impressions,
avg pos 6.67, **0 clicks / 0% CTR**) and Semrush demand ("generative ai in financial
services" 320 vol / KD 42; "ai in financial services" 1,300; "generative ai in banking"
880). Scoped to title, meta description, H2/H3, keyword insertion, and internal linking —
no new content/claims. Recommendations delivered in chat (not yet filed as a page).

## [2026-08-03] ingest | NN/g — UX Writing: FAQs from Practitioners (Kaley, 2026)
Anna Kaley/Nielsen Norman Group practitioner Q&A (published 2026-05-08). Primarily a
UX-writing-craft article; ingested per user's "source page + light cross-links" scope
decision for its narrow, mostly-corroborative AEO/GEO slice (no study of its own).
Created source [[nngroup-ux-writing-faqs-2026]] and raw archive. Light supporting-
citation notes added to [[geo-content-optimization-tactics]] ("write for people first,
structure for machines second"; answer-first principles unchanged; NN/g 20–28%-read
scannability rationale) and [[aio-ctr-impact]] (traffic→engagement KPI shift in the
zero-click era). Flagged a non-conflict nuance in the source page: NN/g's human-
comprehension 6th–8th-grade reading level is a different dependent variable from
[[airops-fan-out-effect-2026]]'s college-level AI-citation correlation. Updated index.

## [2026-08-03] ingest | DerivateX — "Two Googles, One Query" (Google AIO vs. SERP source overlap)
Apoorv Sharma/DerivateX Research benchmark (published 2026-07-06; disclosed methodology,
100 B2B-software buyer-intent queries, 1,259 AIO citations vs. 1,000 top-10 SERP results,
single-session June–July 2026 — directional, B2B-only). Full ingest per user scope choice.
Created source [[derivatex-two-googles-one-query-aio-vs-serp-2026]] and raw archive.
Headline: AIO↔SERP source overlap only 35% (65% AIO-exclusive), 28% product overlap,
shared sources concentrate top-5 (median #4), YouTube–Reddit inversion (AIO 7.3× more
YouTube than SERP; SERP 1.9× more Reddit than AIO), source-type mix (AIO listicles 63.4% /
video 9%), category divergence by listicle-ecosystem maturity (~20% help desk → 62%
QuickBooks hosting). Updated [[ai-citation-landscape]] (new AIO↔SERP divergence subsection;
35% placed as a disclosed-methodology mid-range point among the open Ahrefs-76%/iPullRank-
6.2%/Rankability-17-38%/Otterly-54.5% spread), [[listicles-in-ai-search]] (63.4% AIO
listicle share + maturity-divergence pattern), [[geo-content-optimization-tactics]]
(top-5 necessary-not-sufficient + separate-KPI note in patent-mechanics section), and
[[richsanger-ai-overview-patent-insights]] (nuance note: 65%-AIO-exclusive bounds but
doesn't contradict "AIO reuses pre-ranked results" — retrieval candidate ≠ top-10). Updated
index. No formal Conflicting Evidence entry logged — the overlap figure joins an
already-flagged open question rather than creating a new contradiction.

## [2026-08-03] ingest | DerivateX — "Competitor Citation Steal" framework (Sharma, 2026)
Apoorv Sharma/DerivateX original tactical framework + LLM prompt (published 2026-04-10);
tactical companion to [[derivatex-two-googles-one-query-aio-vs-serp-2026]]. Full ingest as
a new playbook per user scope choice. Created source
[[derivatex-competitor-citation-steal-prompt-2026]], raw archive, and new playbook
[[competitor-citation-displacement]] (7-step method: Citation Mapping → Gap Autopsy →
Steal Matrix → Artifact Blueprints → Entity Line Standardization → 30-day calendar →
weekly diagnostic; the copy-paste prompt is paraphrased, not reproduced verbatim —
proprietary/copyright). Method treated as original vendor guidance sound because it
operationalizes independently-validated tactics; cited evidence (AirOps, SE Land, SE
Ranking, Wix) mostly corroborates existing wiki sources; one new-but-secondhand stat
(Stacker multi-publication +325%) logged as unverified; case studies (REsimpli, Gumlet
20%-inbound-revenue) flagged as vendor claims, not evidence. Added inbound cross-links
from [[ai-entity-footprint-audit]] (competitor-facing counterpart), [[brand-entity-seo-strategy]]
(Entity Line Standardization ↔ consistent-definition step), and
[[geo-content-optimization-tactics]] (third-party-authority section). Updated index.

## [2026-08-03] ingest | DerivateX — "The 4 C's of Being Explainable to AI" (Sharma, 2026)
Apoorv Sharma/DerivateX original positioning framework (published 2026-07-11); third
DerivateX/Sharma source in the wiki. Full ingest as a new playbook per user scope choice.
Created source [[derivatex-4cs-explainable-to-ai-2026]], raw archive, and new playbook
[[explainable-to-ai-4cs]] (the 4 C's — Category/Customer/Contrast/Consistency — + a
two-minute 4-engine self-test; "legible beats liked" thesis). Attached first-party data:
50-company/1,400-prompt benchmark (half <50/100 AI presence despite high favorability —
corroborates [[victorious-q2-2026-quarterly-search-report]] recognition-vs-mention gap and
[[ai-shortlist-effect]]); and the n=233 "Authority Inversion" study. Inbound cross-links
added from [[ai-entity-footprint-audit]] (fast positioning-specific self-test variant) and
[[brand-entity-seo-strategy]] (messaging-legibility layer). Company scores (Clio 89,
ServiceTitan 68 vs. Jobber 41) treated as illustrative, not validated. Updated index.

## [2026-08-03] conflict | third-party review platforms vs. vendor self-description as the driver of AI recommendations
[[derivatex-4cs-explainable-to-ai-2026]]'s "Authority Inversion" study (n=233 ChatGPT
recommendations, 40 categories) found 84% of citations came from vendor self-descriptions/
niche sites and **G2/Capterra cited zero times** — in tension with the wiki's
third-party-authority/review-platform guidance ([[geo-content-optimization-tactics]]'s
review-platform tactic; [[victorious-q2-2026-quarterly-search-report]]'s 99.99%
third-party category-research citations + referring-domains/third-party-mention
correlates; and DerivateX's own [[derivatex-two-googles-one-query-aio-vs-serp-2026]]
5%-AIO-review-site figure). Logged as **unresolved** Conflicting Evidence in
[[ai-citation-landscape]] with a recommendations-vs-citations / engine-and-sample
reconciliation (ChatGPT-only, small n, "vendor self-description OR niche sites" combined
bucket); caveat also added to the geo review-platform tactic. Not resolved — practical
guidance: do both (mention-side third-party presence + recommendation-wording legibility).

## [2026-08-03] ingest | Search Engine Land — MOFU Keywords Guide (Edwards, 2025)
Katlyn Edwards/Search Engine Land classic-SEO guide (last updated 2025-11-27); no
AI/AEO/GEO content, heavily overlapping the wiki's existing funnel/keyword-mapping/SaaS
coverage. Source page + light cross-links per user scope choice. Created source
[[sel-mofu-keywords-2025]] and raw archive. Added a "Map keywords to funnel stage
(ToFu/MoFu/BoFu)" section to [[keyword-mapping-and-cannibalization]] capturing the three
additive bits (vertical-agnostic five-type MOFU keyword taxonomy; funnel-stage internal
linking; GA4 assisted-conversion + multi-touch attribution measurement) and generalizing
the SaaS-specific comparison/features/industries taxonomy in [[gofishdigital-seo-for-saas]]
to any vertical. Added a "Related" pointer in [[gofishdigital-seo-for-saas]]. No timeline
entry (evergreen guide, not a dated real-world event). Updated index.

## [2026-08-06] ingest | Aluri — Enhancing Developer Productivity Through Intelligent Documentation Retrieval (JISEM 2025)
Ingested a query-prompted source: client asked how dev docs served over MCP shape the
agentic experience, and what's good/bad about that format. Filed [[aluri-mcp-documentation-retrieval-2025]]
with a prominent ⚠️ rigor caveat — it's an architecture/design article with ZERO quantitative
results (no sample sizes, no measured values, low-tier JISEM special-issue venue,
AI-generated-sounding prose, secondary references), so all "productivity/quality benefit"
claims are logged as unsubstantiated. Salvageable part is the design patterns (MCP-server-as-
middleware, code-aware chunking, hard/soft metadata filters with adaptive relaxation,
per-collection similarity thresholds, context-window transformation/ranking, selective-
disclosure security). Created concept [[docs-over-mcp]] (docs as an agent-callable tool vs.
an HTML page an agent crawls; four-axis agentic-experience framework; good/bad tradeoffs;
public-vs-internal use cases) — this fills a gap flagged in the preceding query. Cross-linked
from [[agentic-web-optimization]] (see-also) and added point 11 + see-also to
[[optimizing-for-coding-agent-recommendations]]. Updated index.

## [2026-08-06] query | "how do we consider the agentic experience of content served over mcp? what's good/bad about that format?"
Client question re: developer docs showing up in MCP. Answered from [[agentic-web-optimization]]
and [[optimizing-for-coding-agent-recommendations]]; synthesized the docs-over-MCP framing
(docs as a callable tool, four-axis eval, good/bad list). Flagged the missing concept page,
then filled it via the ingest above ([[docs-over-mcp]]).

## [2026-08-06] ingest | MCP-Focus — Function-Oriented Document Enhancement for MCP Server Retrieval (SIGIR '26)
Ingested via URL (dl.acm.org/doi/10.1145/3805712.3809582). ACM PDF/landing returned HTTP 403
to WebFetch — assembled citation, abstract summary, method, and benchmark from the SIGIR
proceedings listing, web search, and the authors' public repo (github.com/JingWC/MCP-Focus);
saved a metadata raw record at raw/studies/mcp-focus-server-retrieval-2026.md noting the
paywall. High-rigor SIGIR paper: MCP *server retrieval* framed as its own IR problem; raw
self-reported server docs (README + tool name/description/input-schema) are weak retrieval
signals; MCP-Focus generates implementation-grounded docs via white-box code analysis
(Tool Parser → tool-doc refinement → server-doc synthesis) that consistently beat raw-doc
baselines across multiple dense retrievers on a 3,763-server benchmark (exact magnitudes not
accessible behind paywall; direction corroborated by multiple public sources). Filed
[[mcp-focus-server-retrieval-2026]]. Extended [[docs-over-mcp]] with an "MCP server
discoverability / retrievability" section and upgraded its "tool descriptions are an
optimization surface" claim from asserted → empirically supported. Annotated
[[aluri-mcp-documentation-retrieval-2025]] with a corroboration note (its doc-quality premise
is now rigorously supported, even though its outcome claims remain unmeasured). Updated index.

## [2026-08-06] ingest | MCP-Focus (SIGIR '26) — verified against full PDF
User supplied the full PDF (raw/studies/mcp-focus-server-retrieval-2026.pdf) after the ACM
403 during the initial URL ingest. Verified all previously-filed claims against the paper:
title/authors/venue/DOI/repo/benchmark-size (3,763 servers) all correct; direction of finding
correct. Corrections/upgrades made: pipeline stage names fixed to Tool Extractor → Tool
Document Refiner → Server Document Refiner (previously "Tool Parser / -Refinement"); removed
the "paywalled / magnitudes unconfirmed" caveats across the raw record, source page, concept
[[docs-over-mcp]], and index; added exact figures (BM25 r@10 ~0.48→~0.73; BGE best; 6
retrievers; generalizes to MCP-Bench/MCP-Universe; beats RepoAgent same-LLM; Tool Document
Refiner is the highest-impact stage in ablation). Benchmark detail added: 1,000 queries each
for 1/2/3-function settings; Table 1 audit shows ~85% of popular servers have missing/poor
tool-output docs. Now a fully-confirmed high-rigor source.

## [2026-08-06] query | "Write a concise non-SEO-audience guide to writing meta tags (page titles & descriptions)"

Answered and filed as a new playbook [[writing-meta-tags]]. Pulled
LaunchDarkly's current positioning from Glean (Platform Messaging
Framework, Mar 2026: "runtime control plane for features and agents,"
tagline "Move at AI speed. Stay in control," Release/Observe/Iterate
pillars) to ground the example titles/descriptions in current messaging
rather than legacy feature-flag framing. Guide covers what meta tags
are, why they matter, length/keyword/uniqueness rules, good-vs-bad
examples, and per-content-type guidance (informational/product/solution/
thought-leadership). Cross-links [[traditional-seo-ranking-factors]] and
[[aio-ctr-impact]]; points to the `seo-meta-tags` skill for the strict
formatting spec. Added to index under Playbooks.

## [2026-08-06] query | "Any downside/upside to keeping the deprecated meta keywords tag? Do AI crawlers read it?" — filed as new concept [[meta-keywords-tag]], cross-linked from [[writing-meta-tags]]

## [2026-08-06] ingest | geoSurge — "Model memory predicts which brands get searched"
Vendor study (geoSurge; 9 industries, 66 buyer questions, ~4,000 responses,
1,416 brand observations; memory measured on a separate model, search on
Gemini 3.5 Flash; May 29–Jun 9 2026). Core finding: a brand in the model's
top-10 training memory was live-searched 55.7% of the time vs. 17.4% for a
not-remembered brand — a 3.2× gap, graded by recall depth (top-5 67% / rest
of top-10 39% / not-remembered 17%). Adds a retrieval-stage mechanism: training
memory biases *what the model searches for*, linking the training-data and
live-retrieval pathways the wiki had treated as parallel. Filed source
[[geosurge-model-memory-predicts-search-2026]]; updated concepts
[[ai-citation-landscape]] (training/retrieval section) and
[[topical-authority-in-ai-search]] (memory as upstream funnel input).
Flagged rigor caveats: vendor source, explicitly associational (brand-prominence
confound), undisclosed proprietary memory metric, single search model, some
per-industry figures on as few as 6 prompts.

## [2026-08-06] ingest | Xu, Iqbal & Montgomery — "Measuring Google AI Overviews" (arXiv:2605.14021v1)
High-rigor WashU academic audit: 55,393 trending queries × 19 categories × 40 days
(Mar 13–Apr 21 2026), 7,583 AIOs, 61,212 references, 98,020 atomic claims; disclosed
methodology, human-validated LLM pipelines (extraction F1 90.1%, verification 95.6%).
Four findings mapped across pages: (1) 13.7% overall activation / 64.7% question-form /
7.5% politics-suppressed → added as a third low-side data point to the AIO-prevalence
Conflicting Evidence in [[aio-ctr-impact]] with a trending-query sampling-frame caveat;
(2) 29.8% of AIO-cited domains off-page (41.4% top-10 overlap) + AIO more credible /
lower-UGC than SERP → corroborates and sharpens the AIO↔SERP-divergence section in
[[ai-citation-landscape]], with a reconciliation against BrightEdge's "UGC-first engine"
framing (different baselines, no conflict); (3) 11.0% of AIO claims unsupported by cited
pages, omission-dominant, independent of source quality → NEW "claim fidelity" section in
[[ai-citation-landscape]] (being cited ≠ being represented accurately); (4) 50.63% of
AIO-cited pages carry ads while Google's ads persist → new publisher-economics section in
[[aio-ctr-impact]], including independent corroboration of the ~38% organic-click-reduction
figure (Agarwal & Sen 2026, cited within the paper). Saved raw PDF + extraction; filed
source [[xu-measuring-google-ai-overviews-2026]]. No new Conflicting Evidence entries —
findings extend/corroborate existing claims.

## [2026-08-06] ingest | Accessibility-tree cluster (SEL McAlpin + OpenAI Publishers/Developers FAQ + microsoft/playwright-mcp)
Three related sources ingested together around one thesis: AI browsing/computer-use agents
perceive and operate web pages via the **accessibility tree** (ARIA roles/names/states), not
pixels. (1) [[sel-accessibility-tree-seo-use-cases-2026]] — John McAlpin/Search Engine Land,
10-use-case accessibility-tree SEO audit; (2) [[openai-publishers-developers-faq]] — OpenAI
first-party: ChatGPT Atlas reads ARIA, plus the OAI-SearchBot/GPTBot/ChatGPT-User taxonomy and
noindex/utm nuances; (3) [[microsoft-playwright-mcp]] — Microsoft's agent-browser MCP server
that operates on accessibility snapshots ("not pixel-based input"). Created new playbook
[[accessibility-tree-audit-for-ai-agents]]; added a "how agents perceive a page" section to
concept [[agentic-web-optimization]]; extended [[optimizing-for-the-agentic-web]]'s ARIA bullet
and [[technical-seo-audit-checklist]]'s §5 agent-readiness item; upgraded [[robots-txt-strategy]]
with OpenAI's first-party crawler-function clarifications. No conflicts — the two primary/first-
party sources corroborate the practitioner article's central mechanism.

## [2026-08-11] ingest | How Search Engines Rank Content: Understanding TF-IDF and BM25 (Pedro Dias / Visively)
Ingested [[visively-tf-idf-bm25-search-ranking-fundamentals]], a high-rigor lexical-ranking explainer by
Pedro Dias (ex-Google Search). Created concept [[lexical-ranking-tf-idf-bm25]] (TF/IDF/TF-IDF/BM25 mechanics,
term saturation, length normalization, inverted index, hybrid retrieval). Added mechanistic cross-links:
[[traditional-seo-ranking-factors]] (the "why" under the strongest text-relevance correlate),
[[how-google-search-works]] (BM25 in the serving/retrieval stage), and [[geo-content-optimization-tactics]]
(mechanistic why keyword stuffing/density fails + reframing "Technical Terms"/"Unique Words" as
retrieval-layer, not citation-layer, signals). No conflicts — corroborates and grounds existing claims.

## [2026-08-11] ingest | URL Structure Fundamentals: Architecture, Trailing Slashes, and Persistence (Pedro Dias / Visively)
Ingested [[visively-url-structure-fundamentals]] (Pedro Dias, ex-Google Search). Created playbook
[[url-structure-best-practices]] (design-for-persistence, flat-architecture myth, trailing slashes,
eliminate-internal-redirects, flat-vs-hierarchical, slug guidance). Cross-linked
[[technical-seo-audit-checklist]] (authoring-side complement to its server-side canonicalization) and
[[otterly-url-ai-citations-study-2026]] (design-side complement to its AI-citation correlation study).
No conflicts — corroborates the existing URL-citation null-result-on-micro-structure finding from the
design/persistence angle.

## [2026-08-12] ingest | URL as UI (Jakob Nielsen / NN/g, 1999)
Ingested [[nngroup-url-as-ui-1999]], the primary source behind the "Nielsen usability heuristics"
previously cited secondhand (via [[visively-url-structure-fundamentals]]) in
[[url-structure-best-practices]]. Upgraded that playbook's heuristic citation from secondhand to
primary and added two new specifics: the all-lowercase rule and a 2007 MS Research 24%-gaze-time-on-URL
credibility data point (framed as the human-behavior antecedent to the clean-canonical-URL AI-citation
lift in [[otterly-url-ai-citations-study-2026]]). No conflicts — foundational and corroborative.

## [2026-08-12] ingest | We Analyzed 89K LinkedIn URLs Cited in AI Search (Semrush / Margarita Loktionova)
Ingested [[semrush-linkedin-ai-visibility-study-2026]] (89K LinkedIn URLs, 325K prompts, 3 engines,
Jan–Feb 2026) — the independent second LinkedIn AI-citation study, cross-checking
[[otterly-linkedin-ai-citations-study-2026]]. Strongly corroborates on four axes (LinkedIn ~11% share,
long-form/original content dominates, engagement doesn't predict citation, follower count irrelevant).
Added new tactics to [[geo-content-optimization-tactics]] (posting consistency 75%/5+-per-4wks,
originality/educational intent, 500–2,000-word article band, answer-first + define-terms) and a
corroboration addendum to [[ai-citation-landscape]].

## [2026-08-12] conflict | LinkedIn Company Pages vs. individual creators on Perplexity
[[semrush-linkedin-ai-visibility-study-2026]] found Perplexity cites 59% Company Pages, against
[[otterly-linkedin-ai-citations-study-2026]]'s 91.7%-individual aggregate (ChatGPT + Google AI Mode
agree individuals dominate in both). Hard to reconcile since Otterly says Perplexity drives 43.3% of all
LinkedIn citations. Logged as unresolved Conflicting Evidence on [[ai-citation-landscape]]; likely a
definitional/engine-set/time-window difference. Named-author tactic unchanged (both agree in aggregate).

## [2026-08-12] ingest | Rerankers for GEO/AEO: How AI Search Chooses Passages and Sources (Peec AI / Metehan Yesilyurt)
Ingested [[peec-ai-rerankers-geo-aeo-2026]], a mechanism-level explainer of the AI-search retrieval
pipeline and reranker stage. Created concept [[ai-search-reranking-pipeline]] (staged pipeline, bi/cross-
encoder, reranker model families, cross-family score-disagreement, answer-shape-alignment, passage-vs-page,
failure-stage diagnostic). Extended [[geo-content-optimization-tactics]] (answer-shape-by-intent + local
self-containment + stage diagnostic, sharpening the existing Fraggle section) and added a complementary
answer-shape mechanism note to [[listicles-in-ai-search]]. Cross-linked [[lexical-ranking-tf-idf-bm25]]
(what happens after the BM25+vector merge). No conflicts — mechanistically unifies existing findings
([[airops-fan-out-effect-2026]] retrieval-rank dominance, [[peec-ai-chatgpt-query-fanouts-2026]] fanout/RRF).

## [2026-08-17] lint | Full-wiki lint pass — 4 fixes applied, 1 finding accepted as-is
Mechanical pass over 175 pages (link graph, frontmatter schema, date ordering, link convention).
Fixed: (1) broken wikilink in [[ai-visibility-measurement-methodology]] — `tryprofound-downstream-impact-
of-ai-visibility-2026` corrected to [[similarweb-downstream-impact-of-ai-visibility-2026]] (wrong vendor
prefix; verified the 2.5x/55.9% figures do belong to the Similarweb source). (2) Orphan page
[[writer-checklist-blog-posts]] — a complete playbook that was never added to `wiki/index.md` and had zero
inbound links; added an index entry, an inbound link from [[writing-meta-tags]], and a "Where these rules
come from" section wikilinking its 10 underlying sources (it previously contained no wikilinks at all,
against the link convention). (3) Stale conflict entry on [[generative-engine-optimization]] — the Tier 1-3-
tactics-vs-[[c-seo-bench-2025]] conflict didn't cite [[peec-ai-rerankers-geo-aeo-2026]] /
[[ai-search-reranking-pipeline]] (ingested 2026-08-12), which supplies a mechanistic *why* for C-SEO Bench's
null/negative results (rerankers score answer-shape alignment, not page-level decoration); added as
"Mechanistic support" raising confidence in the existing best guess without resolving it empirically, plus
a See-also cross-link. (4) Reformatted the lone [[robots-txt-strategy]] Conflicting Evidence entry to the
CLAUDE.md schema (Claim / Supported by / Contradicted by / Current best guess), citing
[[google-robots-txt-intro]] and [[ahrefs-robots-txt-guide]], and added the mutual-exclusivity point (a
disallowed URL can never have its `noindex` read).
Accepted as-is: 3 source pages lack `date_published` ([[google-images-seo]],
[[similarweb-how-to-be-the-brand-ai-recommends-2026]], [[similarweb-how-to-win-the-race-for-gen-ai-search-2026]])
— checked the raw files; these are genuinely undated (evergreen doc / undated PDF), so there is no date to
backfill. Clean: no other broken links, no orphans, no index-only pages, no relative-markdown links, no
missing/empty tags, no type mismatches, no duplicate index entries. Also verified all `origin:` paths in
wiki/sources/ resolve to real files in raw/. An audit of all 5 Conflicting Evidence sections against the
full source list found the other 7 conflict entries still current, and no new unflagged numeric/directional
contradictions across the wiki.

## [2026-08-20] ingest | "Fan-out Framework: 5 Steps to Optimize for Fan-out Queries" (Cyrus Shepard / Zyppy)
[[zyppy-fan-out-framework-2026]] — a named 5-step fan-out discovery-and-optimization workflow
(new "Fan-out discovery and optimization workflow" section in [[geo-content-optimization-tactics]])
with named discovery/clustering/measurement tools; added Peek and Gumshoe to
[[ai-visibility-measurement-methodology]]'s tool landscape.

## [2026-08-20] conflict | AIO/SERP-overlap and rank-1-citation figures — secondhand-citation discrepancies
[[zyppy-fan-out-framework-2026]] attributes to Ahrefs a 38% AIO-citations-from-top-10 figure, which
conflicts with the 76% figure this wiki already has from Ahrefs ([[ahrefs-b2b-seo-statistics-2025]])
for the same metric — logged as an additional unverified data point in the existing open
AIO↔SERP-overlap spread in [[ai-citation-landscape]] rather than resolved. Separately, it attributes
to AirOps a 43.2% ChatGPT-rank-1-citation figure, which does not match the 58.4% figure this wiki's
own AirOps ingest ([[airops-fan-out-effect-2026]]) reports for ChatGPT retrieval rank 1 — flagged as
an unreconciled discrepancy (possibly a different metric: Google organic rank 1 vs. ChatGPT internal
retrieval rank 1) in [[ai-citation-landscape]]'s "Retrieval rank as the primary citation gatekeeper"
section. Neither discrepancy changes existing wiki claims; both are flagged pending a source that
reconciles them.

## [2026-08-20] ingest | "How SEOs Are Using Common Crawl's Web Graph Data for AI Ranking Signals" (Stephen Burns / Common Crawl)
[[commoncrawl-web-graph-ai-ranking-signals-2026]] — first-party Common Crawl blog on its Web Graph
data (Harmonic Centrality, PageRank) as a training-data-representation proxy, plus training-data-share
figures (64% of analyzed LLMs, 80%+ of GPT-3 tokens per Mozilla Foundation). Added the figures and
metric definitions to [[how-google-search-works]]'s training-bot note, a new domain-benchmarking
tactic to [[geo-content-optimization-tactics]] (CC Rank Checker / Web Graph Statistics tools), and a
secondhand rank-vs-citation-probability data point (46-48%/37%/19-20% at positions 1/2/10) plus a
32.5%-listicle-citation-share figure to [[ai-citation-landscape]] and [[listicles-in-ai-search]]. No
conflicts — same direction as, milder magnitude than, existing retrieval-rank findings.

## [2026-08-20] ingest | "Your Inbox Might Be the Next AI Search Signal" (Garrett Sussman / iPullRank)
[[ipullrank-google-personal-intelligence-experiment-2026]] — a controlled experiment on Google AI Mode's
opted-in "Personal Intelligence" feature, finding Gmail/Photos content shifts brand recommendations for
that user (23.9%→66.8% seeded-brand appearance; email >> photo seeding; effect present even for
zero-web-presence fake brands; category-dependent, weaker in trust-heavy verticals). This is a genuinely
new visibility layer for this wiki — private, per-user personal-context signals, distinct from every
existing public-web citation/retrieval/authority finding. Created new concept
[[personal-context-signals-in-ai-search]]; added an early/unproven "Email and personal-context signals"
tactic to [[geo-content-optimization-tactics]] and a "personal context management" measurement-layer note
to [[ai-visibility-measurement-methodology]]. No conflicts with existing wiki claims — the source's own
"web grounding persists" finding suggests this layers on top of, rather than replaces, the public-web
citation mechanics already documented.

## [2026-08-20] ingest | "These SEO Strategies Drive 90% of Your AI Visibility" (Cyrus Shepard / Zyppy)
[[zyppy-seo-strategies-for-ai-search-2026]] — practitioner synthesis piece; mostly restates existing wiki
mechanisms (fan-out/RRF, third-party authority, technical crawlability) under a three-stage
eligibility/citation/recommendation framework. Added Shepard as a corroborating practitioner voice on the
"SEO fundamentals are the foundation" side of [[generative-engine-optimization]]'s existing Conflicting
Evidence entry (his unmeasured "90%" figure, not a new study). Added two new tools (AI Difference Engine,
AlsoAsked.com) and a one-sentence brand-positioning formula to [[geo-content-optimization-tactics]],
cross-linked with [[explainable-to-ai-4cs]]'s four C's. No conflicts.

## [2026-08-24] query | "Write meta tags for /solutions/enterprise-prompt-management-tools/"
Applied [[writing-meta-tags]] (solution-page guidance: lead with the outcome/audience problem) plus the
strict `seo-meta-tags` skill spec (Title Case, `| LaunchDarkly` suffix, 65/155-char limits, CTA). Semrush
US data used to pick the primary keyword: "prompt management" 320/mo KD 34; "prompt management tools"
170/mo; "prompt versioning" 170/mo; "enterprise prompt management" only 70/mo but trending 0.57 -> 1.00.
Chose "Enterprise Prompt Management" to capture the head term plus the enterprise modifier the URL
targets. Delivered 3 title + 3 description variations; nothing new filed to concepts/playbooks.
## [2026-09-04] ingest | 15 sources: topic clusters, broken link building, digital PR, brand awareness, LLMO/GEO/AIO, SEO reporting, content marketing, SEO copywriting, keyword research, SEO competitive analysis

User handed 18 URLs; 3 were already in the wiki
([[sel-brand-entity-seo-5-step-framework]], [[iloveseo-brand-seo-and-ai]],
[[wix-generative-engine-optimization]]) and were skipped as duplicates.
Ingested the remaining 15:

- Topic clusters (Semrush, Surfer SEO, Sitebulb) → new playbook
  [[topic-cluster-strategy]], cross-linked from
  [[link-and-anchor-text-best-practices]] (which already had a
  topic-cluster subsection tied to the Schmitt case study) and
  [[keyword-mapping-and-cannibalization]] (topic/pillar-first variant).
- Broken link building (Semrush, Ahrefs) → new playbook
  [[broken-link-building]].
- Digital PR (Semrush) → new playbook [[digital-pr-strategy]].
- SEO for brand awareness (Semrush) → extended existing
  [[brand-entity-seo-strategy]] with a lighter-weight, pre-authority
  "brand awareness via content SEO" path (long-tail keyword clustering
  + branded-search-traffic measurement) alongside the existing
  machine-legibility/Knowledge-Graph framework.
- LLMO/GEO/AIO guide (Malte Landwehr, LinkedIn, Jan 2024) → extended
  [[generative-engine-optimization]] with a co-occurrence/training-data-
  influence mechanism distinct from citation-stage RAG visibility, and
  extended [[geo-content-optimization-tactics]] with an explicit
  LLM-crawler robots.txt-blocking check.
- SEO reporting, SEO copywriting, keyword research (2026 update), SEO
  competitive analysis (all Semrush) → four new playbooks:
  [[seo-reporting]], [[seo-copywriting]], [[keyword-research]] (cross-
  linked with [[keyword-mapping-and-cannibalization]] as the
  discovery-before-mapping step), [[seo-competitive-analysis]].
- Semrush Academy course pages (Content Marketing, SEO Essentials) →
  filed as curriculum/reference source pages, no new tactical claims;
  used to justify a new thin connective concept page
  [[content-marketing-strategy]] tying the new and existing content
  playbooks together.
- Crawling Mondays YouTube video (Aleyda Solis) → source page filed as
  a placeholder. Content was not retrievable: YouTube's page returned
  only navigation chrome, oEmbed gave title/channel only, the Sitebulb
  recap of this exact episode 404'd, and Wayback Machine access was
  unavailable this session. No takeaways attributed to it.

No real-world-dated events for the timeline — all 15 are evergreen
guides/courses, consistent with the 2026-07-11 batch's precedent for
this source type. No conflicts found with existing wiki claims.

## [2026-09-04] ingest | Link building: Moz beginner's guide, Ahrefs link building guide, Pitchbox link prospecting hacks, Crawling Mondays outreach video (2020)
Ingested 4 sources on external link building/outreach — a genuinely new
topic area not previously covered (existing [[link-and-anchor-text-best-practices]]
covers link markup/anchor text/internal linking, not backlink acquisition).
Created [[link-building]] (concept: four ways links get built, five link
quality metrics, realistic outreach benchmarks) and
[[link-building-outreach-tactics]] (playbook: prospect qualification,
Skyscraper 2.0/guest-posting/resource-page prospecting, outreach keys to
success, common mistakes). No conflicts with existing pages — the four
sources are mutually consistent. Note: the YouTube video's transcript
could not be retrieved (YouTube's transcript API rejected the request in
this session's sandboxed browser; timedtext endpoint returned empty) —
that source was ingested at the chapter/description level only, flagged
in its source page and raw file for future re-fetch if deeper detail is
needed.

## [2026-09-04] ingest | Lead magnet checklists (LiveAgent, Ivyforms) and PDF SEO optimization (Digital Chakra)
Ingested 3 sources — new topic area, no prior lead-magnet or PDF-SEO
coverage in the wiki. Created [[lead-magnet-checklist]] (playbook:
strategy/content/format/delivery/landing-page/follow-up/tracking,
merging LiveAgent's process-stage checklist with Ivyforms'
benchmark-tiered checklist — no conflicts between the two, just
different depth/focus) and [[pdf-seo-optimization]] (playbook: 11-point
PDF-specific SEO checklist plus indexability/ranking-vs-HTML technical
constraints). Cross-linked into [[content-marketing-strategy]],
[[image-seo-checklist]], [[technical-seo-audit-checklist]], and
[[robots-txt-strategy]]. Noted LiveAgent's "add chat button" item as a
vendor plug rather than a general best practice. No real-world-dated
events for the timeline (evergreen guides). No conflicts with existing
wiki claims.

## [2026-09-04] lint | Full-wiki lint: structure clean; 8 playbooks missing concept backlinks, 7 dated research sources missing timeline entries
Scope: 17 concepts, 26 playbooks, 86 sources, 89 raw files.

Clean (no action needed):
- **Broken links** — every `[[wikilink]]` target resolves. The only
  unmatched targets are `[[source-slug]]`/`[[concept-slug]]` in
  timeline.md's format documentation (template placeholders, as noted
  in the 2026-07-11 lint).
- **Index coverage** — all 129 pages are listed in index.md; index.md
  lists no page that doesn't exist.
- **Frontmatter** — `type`/`tags`/`updated` present on every concept
  and playbook; `type`/`tags`/`date_ingested`/`origin` present on every
  source page.
- **Raw ↔ source integrity** — every `origin:` path resolves to a real
  file under `raw/`, and every file in `raw/` is referenced by exactly
  one source page. No orphaned raw material, no dangling origins.
- **Open conflicts re-checked** — the four unresolved Conflicting
  Evidence sections (content-age/freshness in
  [[ai-citation-landscape]], authority-vs-citation in
  [[ai-visibility-correlation-factors]], traditional-SEO-vs-GEO in
  [[generative-engine-optimization]], internal-link-count in
  [[link-and-anchor-text-best-practices]]) were tested against the 20
  sources ingested on 2026-09-04. None of those sources carries
  freshness, content-age, or authority-correlation data, so no conflict
  is newly resolvable and none needed reopening.

Findings (reported, not yet fixed):
1. **8 playbooks link sideways but never up to a concept page**, which
   CLAUDE.md's playbook schema requires ("links back to the concept(s)
   it belongs to"): [[broken-link-building]],
   [[content-pruning-playbook]], [[controlling-ai-feature-inclusion]],
   [[enterprise-seo-strategy]], [[image-seo-checklist]],
   [[keyword-mapping-and-cannibalization]], [[saas-seo-strategy]],
   [[seo-competitive-analysis]]. All are well cross-linked to sibling
   playbooks and sources — only the upward link to the concept layer is
   missing.
2. **2 concepts link to no playbook**: [[e-e-a-t-and-page-quality]] and
   [[google-algorithm-update-history]]. Both have obvious downstream
   playbooks ([[seo-copywriting]]/[[content-pruning-playbook]] and
   [[classic-seo-ranking-factors]] respectively) that they don't point
   at.
3. **7 dated research/analysis sources missing from timeline.md**,
   inconsistent with directly comparable peers that do have entries
   (e.g. [[ahrefs-why-chatgpt-cites-pages-2026]],
   [[growth-memo-why-most-original-data-never-gets-cited]],
   [[peec-ai-listicle-rank-effect-2026]]):
   [[semrush-ai-overviews-study-2025]] (2025-03-01),
   [[sparktoro-influence-happens-everywhere-2026]] (2026-03-25),
   [[growth-memo-topics-matter-for-third-party-authority]] (2026-06-15),
   [[similarweb-downstream-impact-of-ai-visibility-2026]] (2026-06-24),
   [[growth-memo-why-proprietary-data-is-your-most-defensible-asset]]
   (2026-06-29), [[semrush-ai-overviews-commercial-search-2026]]
   (2026-07-02), and [[richsanger-ai-overview-patent-insights]]
   (2024-11-19). The evergreen how-to guides correctly stay off the
   timeline per the 2026-07-11 event-vs-activity ruling; these seven are
   studies/reports/patent analysis, i.e. events by that same ruling.
4. **[[robots-txt-strategy]]'s Conflicting Evidence section doesn't use
   the schema format** — it's a prose paragraph about practitioner
   folklore vs. Google's stance, with no Claim / Supported by /
   Contradicted by / Current best guess structure and no source
   citations on either side. It's also not really a source conflict;
   arguably it should be a "Common misconception" section instead.
5. **1 orphan: [[crawlingmondays-strategical-content-optimization]]** —
   no inbound links except index.md. This is intentional and documented
   on the page itself: the video's content could not be retrieved, so it
   was filed as a placeholder with no citable claims. Flagged for
   visibility, not as a defect — leave it until a transcript is
   available.

Fixes applied (same day, user go-ahead):
- **Finding 1 & 2 — cross-reference layer repaired.** Added concept
  backlinks to all 8 playbooks (creating a `## See also` section on the
  4 that had none: [[content-pruning-playbook]],
  [[enterprise-seo-strategy]], [[image-seo-checklist]],
  [[saas-seo-strategy]]), and playbook links to
  [[e-e-a-t-and-page-quality]] and [[google-algorithm-update-history]].
  ~20 new cross-references; each names *why* the pages relate rather
  than just listing a slug. `updated:` bumped to 2026-09-04 on all 10.
  Every playbook now links to at least one concept and every concept to
  at least one playbook.
- **Finding 3 — 7 timeline entries backfilled** in chronological
  position, each marked "Backfilled during the 2026-09-04 lint" so the
  append-only convention stays auditable:
  [[richsanger-ai-overview-patent-insights]] (2024-11-19),
  [[semrush-ai-overviews-study-2025]] (2025-03-01),
  [[sparktoro-influence-happens-everywhere-2026]] (2026-03-25),
  [[growth-memo-topics-matter-for-third-party-authority]] (2026-06-15),
  [[similarweb-downstream-impact-of-ai-visibility-2026]] (2026-06-24),
  [[growth-memo-why-proprietary-data-is-your-most-defensible-asset]]
  (2026-06-29), [[semrush-ai-overviews-commercial-search-2026]]
  (2026-07-02). Timeline verified in date order end to end (77 entries).
- **Finding 4 — [[robots-txt-strategy]] restructured.** The off-schema
  "Conflicting Evidence" section is gone; its content is now a
  "The 'quick fix for duplicate content' version of this mistake"
  subsection folded into the page's existing "Critical misconception"
  section, with both sides cited ([[google-robots-txt-intro]],
  [[ahrefs-robots-txt-guide]]) and the mechanism spelled out — blocking
  in robots.txt prevents Google from ever seeing the `noindex` that
  would have worked. Added an explicit note that this page carries no
  Conflicting Evidence section *because* the disagreement is official-
  guidance-vs-folklore, not source-vs-source, so a future lint doesn't
  re-flag it as a missing section.
- **Bonus fix — internal contradiction on the same page.** The
  misconception section claimed Google "can still crawl and index"
  a robots.txt-disallowed URL, contradicting the rest of the page (and
  the mechanism it's explaining). Corrected to: Google can still index
  the URL from external links without crawling the page.

Not fixed, by decision:
- [[crawlingmondays-strategical-content-optimization]] stays orphaned.
  It's a documented placeholder for a video whose content couldn't be
  retrieved; linking it from a concept/playbook would imply it supports
  claims it can't. Revisit if a transcript becomes available.

Post-fix verification: no broken links, no orphans, index.md complete,
frontmatter complete, raw ↔ source mapping 1:1, timeline chronologically
ordered.

## [2026-09-06] ingest | Footer SEO — three sources (Growth Memo, SEOptimer, HeyDay Marketing)

Ingested as a set, since all three cover the same narrow topic (sitewide
footer optimization) at very different quality levels:

- [[growth-memo-show-me-your-footer]] (Kevin Indig, 2023-07-31) —
  substantive; the only one with a named Google statement, a first-party
  case, and third-party UX research.
- [[seoptimer-website-footer-seo]] (Jay Kang, 2019-10-01) — design/UX
  led, no citations, but the best material on footer *elements* and CTA
  discipline.
- [[heydaymarketing-footer-optimization]] (2024-05-23) — agency
  marketing post, no data; retained for two ideas the others miss
  (footer schema markup, local-SEO NAP) plus a maintenance cadence.

Created:
- [[footer-optimization]] — new playbook consolidating all three, led by
  Indig's honest "low impact, but not no impact" framing and the crawl-
  rate (not ranking-weight) mechanism.

Updated:
- [[link-and-anchor-text-best-practices]] — reasonable-surfer placement
  bullet and audit-checklist item softened to mark placement weighting
  as contested; added a footer-link cross-reference and See also entry.
- [[link-building]] — Placement quality-metric bullet now distinguishes
  acquired backlinks (hierarchy holds) from internal links (contested).
- `wiki/index.md`, `wiki/timeline.md` (3 dated entries: 2019-10-01,
  2023-07-31, 2024-05-23).

Deliberately excluded: HeyDay's advice to seed commercial keywords
("SEO company," "SEO agency") into footer copy. It is footer keyword
stuffing and contradicts the same article's own anti-stuffing warning
two sentences earlier. Recorded as an anti-pattern in
[[footer-optimization]] with the reasoning, so a future lint doesn't
re-add it as a "missing" tactic.

## [2026-09-06] conflict | Footer/boilerplate link weight — Mueller vs. the reasonable-surfer model

[[growth-memo-show-me-your-footer]] quotes John Mueller saying Google
does *not* discount footer links ("whether they're in the header or in
the footer or the sidebar or the main content, that doesn't really
change anything for us"). This contradicts the reasonable-surfer
placement hierarchy the wiki carried unqualified in
[[link-and-anchor-text-best-practices]] and [[link-building]], sourced
from [[ahrefs-internal-links-for-seo]], [[yoast-internal-linking-for-seo]]
and [[ahrefs-link-building]].

Logged as **unresolved**, leaning Mueller for internal links (standing
preference for official Google guidance over third-party SEO blogs; the
reasonable-surfer patent dates to 2004 and Google filed User-Sensitive
PageRank in 2016). Two caveats keep it open: Mueller describes how
Google *treats links it finds*, not practical equivalence of outcomes;
and the hierarchy remains sound for *acquired backlinks*, where an
editorial placement signals endorsement a sitewide footer link doesn't.
Recorded in full on [[link-and-anchor-text-best-practices]].

## [2026-09-06] conflict | Footer link density — "fat but not obese" vs. "simplicity first"

[[growth-memo-show-me-your-footer]] says there's no downside to a large
footer if PageRank/CheiRank stay balanced and disputes that big footers
are bad UX. [[seoptimer-website-footer-seo]] and
[[heydaymarketing-footer-optimization]] both argue for restraint, the
latter citing link-equity dilution.

Logged as **unresolved**, leaning Indig — consistent with the wiki's
existing no-numeric-cap resolution on internal link counts, and because
the opposing sources offer no data and reuse the simplified
PageRank-dilution argument the wiki already declined. Best guess: the
binding constraint is organization/scannability, not link count.
Recorded on [[footer-optimization]].

## [2026-09-10] ingest | Spotify — "As It Was: Aligning LLM Search Evaluation with Historical User Preferences" (SIGIR '26)
Ingested arXiv:2607.01040. New concept page
[[llm-as-judge-behavioral-grounding]] on grounding LLM-as-judge search
evaluation in historical user-behavior data (QRI cards) rather than
semantic reasoning alone — +91% relative correlation gain on
judge-disagreement cases, better live-A/B sign-alignment (36.8% vs
30.6%). No conflicts with existing wiki claims; cross-linked from
[[ai-citation-landscape]] and [[geo-content-optimization-tactics]] as
evaluation-methodology background, not a citation tactic.

## [2026-09-10] ingest | Salvi, Cuevas, Horta Ribeiro (Princeton) — "Commercial Persuasion in AI-Mediated Conversations"
Ingested arXiv:2604.04263. New concept page
[[ai-mediated-commercial-persuasion]]: LLM chat interfaces nearly
triple sponsored-product selection vs. traditional search (61.2% vs
22.4%), driven mainly by disparaging non-sponsored alternatives rather
than promoting sponsors; "Sponsored" labels + warnings only raise
detection to 35.1%. No conflicts with existing wiki claims — a new
risk axis (active suppression via language, not omission). Cross-
linked from [[ai-citation-landscape]], [[agentic-web-optimization]],
and [[brand-entity-seo-strategy]].

## [2026-09-10] ingest | Gjorgjevska, Mirceva, Mirchev — "WebKnoGraph: GNN-Powered Internal Linking"
Ingested arXiv:2606.06106. Added a pre-deployment evaluation
subsection to [[link-and-anchor-text-best-practices]] §4: GraphSAGE-
based candidate link scoring across authority yield/volatility/
down-up-ratio and semantic-coherence change, tested on a 1,841-page
production crawl. Core finding: automatic link selection maximizes
authority redistribution at a semantic-coherence cost; expert-assisted
selection preserves coherence better but every tested intervention
still showed negative coherence change. No conflicts with existing
link-count/reasonable-surfer guidance — a complementary evaluation
method, not a competing tactic. Cross-linked from
[[ahrefs-internal-links-for-seo]], [[yoast-internal-linking-for-seo]],
and [[topic-cluster-strategy]].

## [2026-09-10] ingest | Ma, Qin, Xu, Tan — "When Content is Goliath and Algorithm is David"
Ingested arXiv:2509.14436. Added a "Perplexity and semantic
homogeneity as a citation mechanism" subsection to
[[ai-citation-landscape]] and a "Reduce perplexity and front-load core
claims" tactic to [[geo-content-optimization-tactics]]. Key findings:
lower-perplexity content is cited more (47%→56% at -1 SD perplexity),
cited source sets are more semantically homogeneous than conventional
SERPs, the preference is intrinsic to the LLM (reproduced via Gemini's
RAG API, not Google-specific), positional bias favors document-opening
content, and LLM-based content polishing counterintuitively increases
citation diversity rather than homogenizing it. No conflicts with
existing wiki claims — complementary to the existing semantic-
relevance/cosine-similarity and retrieval-rank findings, not competing
with them. Cross-linked from [[seo-copywriting]]'s inverted-pyramid
guidance.

## [2026-09-10] ingest | Zhang, He, Yao — "From Citation Selection to Citation Absorption"
Ingested arXiv:2604.25707v2. Added a "Citation selection vs.
absorption" subsection to [[ai-citation-landscape]] and an "Optimize
for absorption, not just citation count" tactic to
[[geo-content-optimization-tactics]]. Key findings: citation breadth
and depth diverge sharply by platform (Perplexity broad-shallow: 16.35
sources/answer at 0.0646 influence; ChatGPT narrow-deep: 6.88 sources
at 0.2713 influence); high-influence pages are structurally denser
(11.4x words, 12.5x headings, 8.94x list density); evidence genre
(definitions +57%, comparisons +55%, code +77%) drives absorption more
than Q&A formatting alone (which showed a -5.74% effect without real
evidence density); news is cited often but absorbed weakly vs.
encyclopedic content. No conflicts — a complementary measurement axis
to [[sej-the-consensus-gap]]'s presence/portability/concentration
framework, cross-linked there.

## [2026-09-10] ingest | Lopez-Fonseca, Rodriguez, Bechtold, Del Alamo — "Do Generative AI Assistants Respect robots.txt?"
Ingested arXiv:2607.14447. Added an "Empirical AI-assistant compliance
data" subsection to [[robots-txt-strategy]]: Claude/Mistral respected
robots.txt in controlled tests; DeepSeek/Gemini/Grok/Qwen did not.
Generic user-agents block assistant-specific targeting; access and
visible-answer behavior frequently diverge (Copilot accessed
everything but answered correctly on nothing; ChatGPT sometimes
answered without accessing); Grok showed 173+ post-window accesses and
48-52x expected per-trial request volume. No conflicts — quantifies an
existing wiki limitation ("not all crawlers respect robots.txt...AI
crawlers"). Cross-linked from [[robots-txt-audit-checklist]].

## [2026-09-10] ingest | Zhen, Liu, Zhang, Niu — "What Do Chinese-Language Generative Search Engines Cite and Surface?"
Ingested arXiv:2607.15771 (PDF, 49pp). Added a "Chinese-language
generative search engines" subsection to [[ai-citation-landscape]] —
first coverage of DeepSeek/Doubao/Tencent Yuanbao/Qwen in this wiki.
Key findings: third-party-content-dominant source ecosystem parallels
English-language engines; a classic SEO composite score was not the
leading predictor of citation absorption in any model; 39.3% of listed
citations are "silent" (never used inline); only 8.3% of pool brands
reach the visible answer; freshness half-life ~39/68 days by query
timeliness (directionally corroborates
[[airops-fan-out-effect-2026]]); App/Web interfaces of the same
platform return meaningfully different source sets (domain overlap
0.19-0.51). No conflicts — new market, corroborating where it overlaps
conceptually. Cross-linked to
[[citation-selection-vs-absorption-geo-framework-2026]].

## [2026-09-10] lint | cross-reference and metadata check
Scanned for broken wikilinks, orphan pages, index.md completeness, and
stale `updated:` frontmatter. Findings and fixes:
- No broken wikilinks (all 141 unique link targets resolve to real
  pages).
- index.md is complete (all 143 pages listed, no dangling entries).
- Orphan pages (no inbound links): 2 found.
  - [[oncrawl-xml-sitemap-optimization]] — its "What this updates" note
    claimed it fed [[xml-sitemap-optimization-checklist]], but that
    playbook never linked back. Fixed: added citation + Related-pages
    link.
  - [[crawlingmondays-strategical-content-optimization]] — left as-is;
    it's a deliberate placeholder for a source whose content couldn't
    be retrieved, so no page should cite it yet.
- Stale `updated:` frontmatter: 9 concept/playbook pages were edited in
  today's 5 source ingests but their frontmatter date wasn't bumped.
  Fixed: [[agentic-web-optimization]], [[ai-citation-landscape]],
  [[robots-txt-strategy]], [[brand-entity-seo-strategy]],
  [[geo-content-optimization-tactics]],
  [[link-and-anchor-text-best-practices]],
  [[robots-txt-audit-checklist]], [[seo-copywriting]],
  [[topic-cluster-strategy]], and [[xml-sitemap-optimization-checklist]]
  (found via the orphan fix above) all now show `updated: 2026-09-10`.
- Reviewed all 5 open Conflicting Evidence sections (content-freshness
  in [[ai-citation-landscape]], authority-correlation in
  [[ai-visibility-correlation-factors]], footer-link-density in
  [[footer-optimization]], the SEO-obsolescence question in
  [[generative-engine-optimization]], and the reasonable-surfer-vs-
  Mueller footer question in
  [[link-and-anchor-text-best-practices]]) — none resolved by today's
  new sources; left open as-is.
## [2026-09-10] ingest | Measuring Google AI Overviews (Xu, Iqbal & Montgomery, arXiv:2605.14021)

First independent academic AIO audit in the wiki (55,393 trending
queries, 7,583 AIOs, 61,212 cited URLs, 98,020 verified claims,
Mar-Apr 2026). New source page
`arxiv-measuring-google-ai-overviews-2026` and new concept
[[ai-overview-grounding-and-fidelity]]. Updated
[[ai-citation-landscape]] (new AIO-vs-first-page source-selection
section: long-tail breadth, PC1 credibility gap, 14.2% vs 41.4% UGC,
29.8% off-page citations), [[aio-ctr-impact]] (activation by question
form/query length; supply-side ad-dependence economics), and
[[geo-content-optimization-tactics]] (activation levers plus a new
"verify how you're represented" audit checklist).

## [2026-09-10] conflict | AIO citation vs. top-10 ranking - 76% (Ahrefs) vs. 41.4% domain overlap (arXiv)

Logged on [[ai-citation-landscape]]. Ahrefs B2B stat says 76% of AIO
citations come from Google's own top 10; the arXiv audit measures
41.4% per-AIO domain overlap at top-10 and 70.2% across the full first
page, with 29.8% of cited domains appearing nowhere on it. Partly a
unit-of-analysis difference (citation-weighted vs. per-AIO domain
average) and partly a corpus difference (B2B vs. trending). Leaning
toward treating 76% as an upper bound that doesn't generalize across
query mixes; flagged unresolved.

## [2026-09-14] lint | Merged the GitHub `origin` history into the local wiki (12 conflicts)

Pulled `origin/main` (nealkindschi/seo-wiki), which had diverged from the
local branch: 16 commits upstream, 10 local. Resolved 12 merge conflicts
by union/reconciliation rather than taking either side — `log.md`,
`timeline.md` and `wiki/index.md` merged as unions (with the overlapping
`index.md` entries for [[ai-citation-landscape]],
[[robots-txt-strategy]], [[geo-content-optimization-tactics]],
[[link-and-anchor-text-best-practices]],
[[optimizing-for-coding-agent-recommendations]] and
[[technical-seo-audit-checklist]] rewritten to carry both sides' detail),
and section-level conflicts on [[ai-citation-landscape]],
[[aio-ctr-impact]], [[generative-engine-optimization]],
[[robots-txt-strategy]] and [[geo-content-optimization-tactics]] resolved
by keeping both sides' new sections and collapsing the duplicated
`## Conflicting Evidence` headings into one. No claims dropped.

**Open finding — duplicate source page.** The same paper (Xu, Iqbal &
Montgomery, *Measuring Google AI Overviews*, arXiv, 2026-05-13) exists
under two slugs: [[xu-measuring-google-ai-overviews-2026]] (ingested
2026-08-06 from the PDF) and
`arxiv-measuring-google-ai-overviews-2026` (ingested 2026-09-10 from a
markdown extraction, longer writeup). Concept pages now cite both slugs
interchangeably. Needs consolidation to one slug with the other's unique
detail folded in — not done here, awaiting go-ahead.

## [2026-09-14] ingest | Why Your Content Isn't Getting Cited: A GEO Diagnostic Checklist (Lumar)

New playbook [[geo-diagnostic-checklist]] — a six-check triage
framework (candidate eligibility, aboutness signals, chunk
retrievability, standalone passage context, authority constraints,
problem-solution alignment) for diagnosing why a specific page isn't
getting cited before applying [[geo-content-optimization-tactics]].
New source page [[lumar-geo-diagnostic-checklist]]; no original data
or studies, restates existing retrieval-eligibility-vs-citation-stage
framing already in [[generative-engine-optimization]] — no conflicts.
Linked from [[generative-engine-optimization]] and
[[geo-content-optimization-tactics]].

## [2026-09-17] ingest | The Complete List: Every Search Engine Hidden Inside ChatGPT's Retrieval Leak (David Konitzny, LinkedIn)

Ingested an enumeration of **69 named ChatGPT retrieval engines** extracted
from a leaked server-sent-events config (leak originally found by Metehan
Yesilyurt). Raw capture:
`raw/articles/konitzny-chatgpt-retrieval-leak-engine-list-2026.md`. Source page:
[[konitzny-chatgpt-retrieval-leak-engine-list-2026]].

**New concept page:** [[chatgpt-vertical-retrieval-engines]] — the engine map
(internal `labrador` family vs. four external backends), vertical engines per
content type, news freshness as separate 1d/7d/all engines, the `bing_query`
rewriter layer, system1-vs-system2 unequal coverage, and open questions
(`labrador-synthetic`, `fortis`, `aixiv`).

**Updated:** [[ai-search-reranking-pipeline]] (renumbered the pipeline to insert
an **engine-selection** substage before hybrid retrieval, plus a new
never-routed-to-your-engine failure mode in the diagnostic framework),
[[ai-citation-landscape]] ("ChatGPT's retrieval backend is plural, not just
Bing" addendum), [[geo-content-optimization-tactics]] ("Vertical retrieval-path
eligibility" tactics), [[pdf-seo-optimization]] (dedicated but system2-gated
`web-pdf` path), [[wiki/index.md]], [[wiki/timeline.md]].

**No conflicts logged.** The source extends rather than contradicts existing
pages; the wiki carried no claim that ChatGPT's backend was Bing-only.

**Caution written instead of a conflict entry** (per user direction): the
source's top comment infers Reddit's high value from its dedicated retrieval
engines, which sits against [[ahrefs-why-chatgpt-cites-pages-2026]]'s 1.93%
Reddit citation rate / 67.8%-of-non-cited-URLs and the ~99% discard figure in
[[lilyray-chatgpt-fanout-queries-2026]]. Recorded as a caution on
[[chatgpt-vertical-retrieval-engines]] — a reader inference, not a claim
Konitzny makes, and not a source-vs-source contradiction.

**Gap surfaced, deliberately not filled** (per user direction): Yelp/Foursquare
listing accuracy as the local/business AI-visibility lever, with no Google
Business Profile path in the registry. No local playbook exists in this wiki;
one unverified source is not a sufficient basis to build one. Noted on the
concept page and as a single actionable bullet in
[[geo-content-optimization-tactics]].

**Rigor caveat carried on every page touched:** configuration dump, not a study
— no call frequency per engine (a commenter asked; unanswered), single
practitioner, unverified leak, engine semantics inferred from names, and the
`mai-news-beta` tag shows the registry was mid-rollout. Structural map, not a
traffic profile.

## [2026-09-17] lint | Consolidated the duplicate *Measuring Google AI Overviews* source pages

Resolved the open finding logged in the 2026-09-16 merge entry: Xu, Iqbal &
Montgomery, *Measuring Google AI Overviews* (arXiv:2605.14021v1, 2026-05-13)
existed as **two source pages** — `xu-measuring-google-ai-overviews-2026`
(ingested 2026-08-06 from the PDF) and
`arxiv-measuring-google-ai-overviews-2026` (ingested 2026-09-10 from a longer
HTML/markdown extraction). Concept pages had been citing both slugs
interchangeably, sometimes within the same page.

**Kept:** [[xu-measuring-google-ai-overviews-2026]] — the author-name slug
matches this wiki's convention for academic papers
([[entity-oriented-search-balog-2018]], [[xiong-et-al-search-engines-meet-llms-2024]],
[[vardasbi-et-al-as-it-was-llm-search-evaluation-2026]],
[[geo-generative-engine-optimization-aggarwal-2023]]), and it was the earlier
ingest.

**Retired:** `arxiv-measuring-google-ai-overviews-2026` (page deleted).

**Unique detail folded in from the retired page** (the 2026-09-10 writeup was
the fuller one, so most of this is net-new to the surviving page): median 8
refs/AIO; the citation-breadth finding (top-10 hosts 29.7% of AIO citations vs.
49.6% of first-page, 56.3% of hosts cited exactly once); PC1 significant in 14
of 19 categories with no reversal, plus the authors' "directly contradicts prior
work" framing; four platforms = 96.5% of AIO UGC; off-page refs being *higher*
quality (PC1 0.758 vs 0.724, UGC 3.4% vs 18.5%) and 28.5% off-page at URL level;
per-interrogative activation (`how` 84.3%, `why` 73.4%, `did` 39.8%); health
*not* suppressed (26.6%) so the sensitive-topic caution is selective; activation
↔ fidelity statistical independence (p=0.192); grounding distribution (median
93.33%, 41.9% perfect, 2.74% under half, 0.85% none); the Climate 48.23%
artifact and the 85.9–94.8% normalized band; per-category ad rates; the
2.16%/0.51% Google-sponsored-ad figures; corpus composition (Sports 51.4%,
Entertainment 14.9%); the Grok 4.1 verifier identity; and the logged conflict
against [[ahrefs-b2b-seo-statistics-2025]]'s 76%-from-top-10 claim.

**Unique detail retained from the surviving page:** claim-extraction F1 90.1%;
fidelity independent of source quality (r≈0.045); lowest-fidelity categories
(Autos/Sports/Jobs ~77–82%); the authors' "inherent to generative AI at its
current state" framing; and the imported downstream figures (Agarwal & Sen ~38%
click reduction / ~33% more zero-click, Wikipedia −15%, Stereogum −70% ad
revenue, The Planet D −90% traffic).

**Links repointed** (13 wikilinks across 5 live pages):
[[ai-citation-landscape]] (3, including the `Contradicted by:` line in its
Conflicting Evidence section), [[aio-ctr-impact]] (2),
[[ai-overview-grounding-and-fidelity]] (2, including its `Primary source:`
line), [[geo-content-optimization-tactics]] (2), [[wiki/timeline.md]] (1), and
[[wiki/index.md]] (2 entries merged into 1).

**Append-only files handled without rewriting history:** the two historical
mentions of the retired slug in earlier `log.md` entries were converted from
wikilinks to code spans (`arxiv-measuring-google-ai-overviews-2026`), preserving
the original wording while removing links that would now dangle. The
`timeline.md` entry for this paper's publication was repointed to the surviving
slug — a pointer repair, not a change to the recorded event.

**Raw files:** both retained, per the never-edit-`raw/` rule —
`raw/studies/xu-measuring-google-ai-overviews-2026.pdf` (+ its `.md`
extraction) and `raw/studies/arxiv-measuring-google-ai-overviews-2026.md`. The
surviving page's `origin:` names the PDF and its body documents both captures,
so the retired slug's provenance is still traceable.

**Verified:** no broken wikilinks wiki-wide (excluding the known
`[[source-slug]]`/`[[concept-slug]]` template placeholders in the format blocks
of this file and `timeline.md`); one index entry for the paper; no orphan.

## [2026-09-17] lint | Merged upstream `origin/main` (Lumar GEO checklist) and cross-checked it against the engine-registry ingest

Folded in the 2 upstream commits this branch was missing (Lumar GEO diagnostic
checklist ingest, PR #8). **5 conflicts, all resolved by union or
later-date**, none by discarding a side:

- `wiki/index.md` (2) — kept the local, richer [[geo-content-optimization-tactics]]
  blurb and added upstream's new [[geo-diagnostic-checklist]] entry. **Second
  conflict was the important one:** upstream still carried an index entry for
  `arxiv-measuring-google-ai-overviews-2026`, the slug retired earlier today.
  Taking upstream's side wholesale would have **resurrected a link to a deleted
  page**; took only the [[lumar-geo-diagnostic-checklist]] line.
- `wiki/log.md` — union, with upstream's 2026-09-14 Lumar entry inserted before
  today's entries so dates stay ascending.
- `wiki/timeline.md` — union, 2026-09-14 Lumar event before the 2026-09-17
  engine-registry event.
- [[generative-engine-optimization]] and [[geo-content-optimization-tactics]] —
  `updated:` frontmatter only; both sides had edited the pages, so both took
  2026-09-17.

**Cross-check outcome: complements, no conflict.** [[geo-diagnostic-checklist]]
is a page-level triage framework whose six checks are all *content-side*
(aboutness, chunk retrievability, standalone passage context, authority). None of
them asks whether the content sits in a **format or vertical the engine routes
to at all** — the engine-selection failure mode added today from
[[konitzny-chatgpt-retrieval-leak-engine-list-2026]], which happens *upstream of
retrieval*. A page can pass all six checks and still never enter the candidate
pool.

**Gap closed:** added an attributed **check 0 (retrieval-path routing)** to
[[geo-diagnostic-checklist]], flagged as not from the Lumar source and carrying
that source's unverified-single-practitioner caveat — format/HTML-equivalent
coverage, the system2-gated PDF and YouTube paths, Yelp/Foursquare listings for
local queries, and publishing inside the news recency window. Cross-linked in
both directions with [[chatgpt-vertical-retrieval-engines]] and
[[ai-search-reranking-pipeline]], whose failure-stage diagnostic this playbook
operationalizes per page.

**Note on overlap already present upstream:** Lumar's checks 3 and 4 map onto
the "retrieved but loses the rerank" stage and its check 5 onto authority as a
retrieval-eligibility gate, both of which [[ai-search-reranking-pipeline]] and
[[generative-engine-optimization]] already covered. Upstream had linked those
correctly; no duplication introduced.

