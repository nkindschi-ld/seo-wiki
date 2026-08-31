---
type: source
tags: [seo, aeo]
date_published: 2026-06-25
date_ingested: 2026-08-20
origin: raw/articles/zyppy-fan-out-framework-2026.md
---

# Fan-out Framework: 5 Steps to Optimize for Fan-out Queries (Cyrus Shepard / Zyppy)

**Citation:** Shepard, Cyrus. "Fan-out Framework: 5 Steps to Optimize
for Fan-out Queries." Zyppy Signal (Substack). Published 2026-06-25.
https://signal.zyppy.com/p/fan-out-framework

**Methodology note:** primarily an original practitioner framework
(disclosed, actionable) plus a secondhand round-up of Ahrefs/AirOps/
Semrush stats with no links or methodology given — the stats round-up
should be treated as unverified secondary citation, distinct from the
framework itself, which is the source's real contribution.

## Key takeaways

- **A concrete 5-step fan-out optimization workflow** — new to the
  wiki as a named, sequenced process rather than a scattered set of
  tactics: (1) identify a ranking keyword from existing top 10-20
  Google positions, (2) discover the AI engine's fan-out sub-queries
  for it using a dedicated tool, (3) consolidate the resulting topics
  into a prioritized list, (4) optimize existing pages or create new
  ones targeting those consolidated topics, (5) measure via webmaster
  tools and AI-visibility trackers. This operationalizes the
  fan-out-targeting tactics already in [[geo-content-optimization-tactics]]
  into a repeatable process with a defined discovery step.
- **Named fan-out discovery tools, new to the wiki**: QueryFan (API
  key required), Qforia (Google-specific, needs a Gemini API key),
  queryfanout.ai and "Query Fan Out Analysis" (no API required), plus
  Bing Webmaster Tools' AI Performance Report (already known to this
  wiki via [[bing-ai-performance-report]], here used for fan-out
  discovery specifically rather than just citation tracking).
- **Named premium AI-visibility trackers, two new to the wiki**: Peek
  and Gumshoe, alongside Otterly and Profound (both already covered
  extensively elsewhere in this wiki) — adds to the tool landscape in
  [[ai-visibility-measurement-methodology]].
- **Explicit content-quality warning**: don't create a low-quality page
  for every fan-out subtopic discovered — Google increasingly demotes
  scaled content. This is a direct, practitioner-stated caution against
  over-applying the fan-out-targeting tactic itself, complementing
  [[e-e-a-t-and-page-quality]]'s Scaled Content Abuse pattern.
- **Fan-out queries are explicitly framed as unstable**: "probabilistic
  and personalized, and they vary greatly across AI models and even
  within user sessions" — reinforces (rather than newly establishes)
  this wiki's existing cited-source-volatility finding
  ([[sel-what-is-generative-engine-optimization-geo-2026]]'s 40-60%
  month-to-month churn), extended here to within-session variability,
  which the wiki hadn't previously covered.
- **A specific, unverified claim about AI answer update speed**: AI
  answers reportedly use "70 days of user data rather than the 13
  months used for traditional search results," making them faster to
  respond to content changes. No source or methodology is given for
  this figure — flagged as an unverified, specific-sounding claim
  rather than adopted as fact.
- **Secondhand stats round-up with two attribution discrepancies
  against sources already in this wiki**:
  - "Ahrefs: 38% of AIO citations come from Google's top-10" — the
    wiki already has an Ahrefs figure for the same metric at **76%**
    (via [[ahrefs-b2b-seo-statistics-2025]]). The two can't both be
    Ahrefs' current headline number for the same metric; 38% happens
    to sit at the upper edge of [[rankability-where-seo-is-going-2026]]'s
    already-logged 17-38% range for a *declining-over-time* version of
    this same overlap metric — plausibly Shepard is citing a different
    Ahrefs data cut (or the Rankability figure mislabeled as Ahrefs)
    rather than a genuinely new contradiction. Treat 38% as an
    additional unverified data point in the wiki's already-open
    AIO↔SERP-overlap spread (see [[ai-citation-landscape]]), not as a
    fresh Ahrefs figure superseding 76%.
  - "AirOps: ChatGPT cited the #1-ranked page 43.2% of the time" — the
    wiki's own AirOps source page ([[airops-fan-out-effect-2026]])
    reports **58.4%** citation at ChatGPT's internal retrieval rank 1,
    not 43.2%, and doesn't contain a 43.2% figure anywhere. Possible
    reconciliation (untested): Shepard's figure may describe *Google
    organic rank 1* → ChatGPT-citation likelihood, a different metric
    than AirOps's internal-retrieval-rank framing — but this isn't
    confirmed, since the wiki's ingest of the AirOps report has no such
    breakdown. Flagged as an unreconciled discrepancy rather than
    adopted.
  - "Semrush: Perplexity showed 82% overlap with Google's top 10" — no
    existing wiki source has this specific figure; added as a new,
    unverified data point (different engine — Perplexity, not Google
    AI Overviews — so not directly comparable to the AIO↔SERP spread
    above).

## Relationship to existing wiki content

The 5-step framework and tool list are the genuine new contribution —
they sit downstream of, and operationalize, the fan-out mechanics
already established by [[peec-ai-chatgpt-query-fanouts-2026]],
[[airops-fan-out-effect-2026]], and [[lilyray-chatgpt-fanout-queries-2026]].
The stats round-up is lower-confidence secondhand citation and, in two
cases, appears to conflict with or duplicate figures this wiki already
has attributed to the same named sources — logged above rather than
silently reconciled.

## What this updated

- [[geo-content-optimization-tactics]] — added a "Fan-out discovery
  and optimization workflow" section (the 5-step process and discovery
  tools).
- [[ai-visibility-measurement-methodology]] — added Peek and Gumshoe to
  the tool landscape list.
- [[ai-citation-landscape]] — added the 38%/82% figures as additional
  (unverified) data points in the existing AIO↔SERP-overlap discussion,
  and flagged the 43.2%-vs-58.4% AirOps discrepancy.

Logged as a `conflict` entry in `wiki/log.md` for the two attribution
discrepancies (Ahrefs 38% vs. 76%; AirOps 43.2% vs. 58.4%).
