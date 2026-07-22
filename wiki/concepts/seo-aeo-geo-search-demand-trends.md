---
type: concept
tags: [seo, aeo]
updated: 2026-07-22
---

# SEO/AEO/GEO Search Demand Trends

How much people are *searching for these terms themselves* (SEO, AI,
AI agents, AEO, GEO) over time — distinct from every other data type in
this wiki, which measures citation/visibility mechanics *within* AI
answers. This page tracks industry attention and terminology adoption,
not AI-answer-engine behavior. Based on
[[rankability-where-seo-is-going-2026]], a Google Keyword Planner panel
of 3,751 keywords across 48 months (June 2022-May 2026).

**Caveat inherited from the source**: this measures search *interest*
(a leading indicator of attention), not revenue, adoption, or ranking
outcomes directly. Bucketed monthly volumes mean single-month spikes are
partly a rounding artifact — read the trend, not any one month.

## The four-line divergence

Rolling 12-month search volume by theme (12 months to May, each year):

| Theme | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|
| AI (general) | 91.1M | 124.6M | 176.6M | 326.9M |
| SEO | 27.0M | 25.8M | 47.7M | 33.4M |
| AI agents | 38.9K | 145.7K | 634.9K | 843.2K |
| GEO | 0 | 2.8K | 15.6K | 59.8K |
| AEO | 0.4K | 1.0K | 7.4K | 27.3K |

Three patterns stand out:

- **AI demand is the tide everything else rides on**: ~10x the size of
  SEO demand and still accelerating (+260%/3.6x since 2022).
- **SEO interest has rolled over for the first time in this panel**:
  peaked at ~47.7M (year to May 2025), fell ~30% to ~33.4M by May 2026.
  In an indexed/rebased view (baseline = June 2024), SEO is the *only*
  one of the five tracked themes trending below where it started — AI,
  agents, AEO, and GEO are all still above their baseline even after
  AEO/GEO's own plateau (below).
- **AEO and GEO are real but still three orders of magnitude smaller
  than SEO**: both went from ~0 (2023) to a named, measurable discipline
  (2025), then plateaued in early 2026 — AEO ~17% below its September
  2025 peak, GEO ~45% below its August 2025 peak.

## Reading "SEO interest is declining" correctly

The source is explicit that this is not "SEO is dying" — it's **search
being abstracted away by an AI answer layer**, with the optimization
economy reorganizing around influencing that layer rather than the
practice disappearing. This is consistent with this wiki's existing
framing in [[generative-engine-optimization]] and
[[ai-traffic-scale-vs-hype]]: the underlying skills (crawlable,
authoritative, well-structured content) persist; what's declining is
interest in the *term* "SEO" and the mental model of ranking-for-clicks
it implies, not the underlying practice.

## The AEO-vs-GEO naming tension

A specific, quotable finding: **GEO carries roughly 2x AEO's raw search
volume**, yet the source observes practitioners converging on "AEO" as
the standard professional label anyway. Its interpretation (not
independently verified by any other source in this wiki): GEO caught on
as the catchier public-facing name, while AEO wins in
professional/boardroom contexts because it maps cleanly to a
measurable, sellable outcome — getting cited in an answer. The source
predicts the two terms consolidate toward one dominant label within
~18 months (i.e., by roughly late 2027). This is a **prediction, not an
observed outcome** — worth revisiting against a future search-demand
snapshot rather than treated as settled.

This wiki has taken a pragmatic position on the same naming question
independently: [[generative-engine-optimization]] treats "GEO and AEO
as the same underlying idea," using GEO as the primary label because
the founding academic paper ([[geo-generative-engine-optimization-aggarwal-2023]])
coined it — a different (etymological) reason than this source's
volume-vs-usage argument, but the same practical conclusion that the
terms are functionally interchangeable at this stage.

## AI agents: hype-to-deployment shape

AI-agent search demand grew ~22x from 2022-23 to 2025-26, ramped
hardest through 2024 and early 2025, then went **volatile** — peaking
around early 2026 before pulling back ~40%. The source reads this
specific shape (steep ramp, then choppy plateau rather than continued
monotonic growth) as the signature of a category graduating from
speculative hype into actual deployment, not a category failing. It
frames the practical shift this implies: agents are becoming
*consumers* of search results in their own right, so the optimization
question broadens from "does my page rank?" to "does the agent choose,
trust, and transact with my brand?" — the same reframing already
covered tactically in [[optimizing-for-the-agentic-web]] and
[[agentic-web-optimization]].

## Forward-looking scenarios (source's own predictions, not observations)

The source offers a three-horizon forecast, explicitly speculative:

- **Now-2026**: AI Overviews mainstream, organic CTR still falling,
  AEO/GEO in early-adopter phase.
- **2026-2027**: "AI visibility" becomes a budgeted line item, AEO/GEO
  terminology consolidates, a second wave of adoption hits the
  mid-market.
- **2027-2028**: agents transact at scale, "agent experience" (AX)
  emerges as its own discipline, multi-engine visibility becomes table
  stakes.

Flagged as forecasts to revisit against future data, not findings to
treat as established.

## See also

- [[rankability-where-seo-is-going-2026]] — the source for all data on
  this page.
- [[generative-engine-optimization]] — this wiki's existing GEO/AEO
  terminology stance, arrived at independently of this page's
  volume-vs-usage naming argument.
- [[ai-traffic-scale-vs-hype]] — a related but distinct scale check:
  clickstream *traffic share* (how much of actual web visits AI tools
  capture) rather than this page's keyword *search-demand* trends (how
  much people search for these terms). Both point toward AI-related
  categories being smaller in absolute terms than their attention/hype
  would suggest, measured two different ways.
- [[optimizing-for-the-agentic-web]], [[agentic-web-optimization]] — the
  tactical playbooks behind this page's "agents as search-result
  consumers" reframing.
