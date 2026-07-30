# AI Performance in Bing Webmaster Tools

Source: https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c
Retrieved: 2026-07-23

## Overview

The AI Performance Report in Bing Webmaster Tools shows how a site's
content is used in AI-generated answers across Microsoft Copilot and
partner experiences by highlighting which pages are cited, how
visibility trends change over time, and the grounding queries
associated with the content.

## Which AI experiences are included?

AI Performance reflects grounding and citation activity across:
- Microsoft Copilot
- AI-generated summaries in Bing
- Select partner AI integrations

## What does AI Performance measure?

Summarizes and aggregates citation activity across three core areas:

- **Pages Cited in AI Answers** — how often a specific URL is visibly
  cited in an AI-generated answer.
- **Average Cited Pages** — the average number of unique pages cited
  per day across supported AI experiences during the selected range.
- **Grounding Queries Your Content Appears In** — the key phrases the
  AI used when retrieving cited content.
- **Page-Level Citation Activity** — citation counts by URL, showing
  which pages are cited most frequently. Reflects citation frequency
  only, not importance, ranking, or role within a response.

## How does AI visibility change over time?

A timeline view shows citation-volume trends across supported AI
experiences. Changes may reflect: shifts in the volume/type of user
questions, content updates, or system/model updates. Trends are
observational only and cannot be attributed to a specific cause.

Available time ranges: 7 days, 30 days, 3 months, custom range (within
available historical data).

## How are AI Performance metrics calculated?

- **Total Citations** — total times content was visibly referenced/
  shown as a source during the selected range.
- **Cited pages** — number of unique pages cited on a given day.
- **Average cited pages** — average unique pages cited per day over
  the range.

Note: AI Performance does not measure rankings, authority, performance,
or importance — it shows only what was cited.

## Grounding queries

The grounding queries tab shows grouped/generalized phrases (not full
user questions/prompts) associated with citation activity.

- The number shown reflects how often content was referenced in AI
  answers for that phrase during the selected range.
- A single grounding query can map to multiple pages, and a single page
  can appear under multiple grounding queries.
- Use grounding queries to understand which phrases drive citations,
  spot patterns, and identify strong vs. limited AI visibility areas.

Example: content cited in solar-energy-related AI answers may appear
under grounding queries like "solar energy" or "solar panels."

Grounding queries may be determined differently across AI experiences/
partners, and phrasing may vary. Data is summary-level — no individual
AI answers, exact prompts, or "why cited" reasoning is shown.

## Page-level citation activity / Grounding Query–Page Mapping

The Pages view shows which pages are cited most, lets you compare
citation activity across pages, and see distribution at the page level.
Grounding Query–Page Mapping connects the Grounding Queries and Pages
views: select a grounding query to see its cited pages, or a page to
see its associated grounding queries (one at a time, not both
simultaneously — export data to cross-reference).

## Data availability and refresh cadence

Data refreshes daily with a short processing delay; historical data is
available only for the time ranges shown in the dashboard.

## About the data

AI Performance data is aggregated/summarized/sampled, not a complete
log of every citation instance:
- Not all citation activity may appear.
- Very low/infrequent citation activity may not surface.
- Totals may differ across views (pages vs. grounding queries vs.
  time-series).
- Data represents a sample; results may be refined as more data is
  processed.
- Designed for trend analysis and comparative insight, not precise
  accounting of individual answers/prompts.
- Reflects only content eligible for indexing; Bing respects
  robots.txt and other content-owner control mechanisms.

## Downloading data

Exportable in CSV/Excel: grounding query data with citation counts,
page-level citation data, time-series metrics across custom date ranges.

## Using AI Performance to improve visibility (content best practices)

- **Align content with user intent** — review grounding queries/pages
  to understand what your content supports in AI answers.
- **Strengthen depth and expertise** — pages cited across related
  grounding queries reflect clear subject focus; expand related-area
  coverage.
- **Improve clarity and structure** — descriptive headings, concise
  sections, tables, FAQ-style content.
- **Support claims with evidence** — examples, data, cited sources.
- **Keep content fresh and accurate** — regular updates help AI systems
  reference current information.
- **Maintain consistency across formats** — text/images/other media
  should describe the same products, entities, concepts.

Further guidance linked: "Optimizing your content for inclusion in AI
search answers" (Microsoft Advertising blog, Oct 2025).

## FAQs (selected)

- **Citations ≠ clicks/traffic.** A citation means content was visibly
  referenced/shown; it doesn't represent traffic, clicks, or engagement.
- **Citation counts change** based on user demand, content freshness,
  model updates, partner refresh cycles, and shifts in topics asked.
- **Pages never cited** may be less relevant to common questions, lack
  clarity/depth, be outdated, or be outperformed by other sources.
- **Grounding queries look short/vague** by design — grouped,
  generalized phrases, not individual user questions or long-tail
  queries.
- **AI Performance metrics ≠ traditional search metrics** (rankings,
  clicks, traffic) — grounding/citations show how AI systems use
  content to generate answers, a different thing.
- Sparse/infrequent citation activity may simply not surface — not a
  penalty or exclusion signal.
- Filtering by grounding query and by page independently can yield
  slightly different citation counts for the "same" pairing, because
  each is sampled over slightly different time windows — expected
  behavior, not a data error.

## Preview capabilities: Intents, Topics, Citation Share, Compare

Bing Webmaster Tools is expanding AI Performance with four preview
capabilities that move beyond raw citation counts:

### Intents

Classifies grounding queries by query intent (Informational, Media,
Navigational, Commercial, Learn and Solve, Research, Live Event, Local,
Comparison, Planning, Utility, Creation, Conversational, Other) via
AI/ML classifiers analyzing the query and context. Classifiers are
described as "continuously improving" — labels may not perfectly match
expectations for ambiguous/multi-intent queries.

Usage: identify which intent categories your citations cluster in (e.g.
Commercial/Comparison strength for e-commerce sites), spot intent gaps
(expecting Research citations but seeing mostly Informational), and
align content format to intent (comparison tables for Comparison,
step-by-step for Planning, concise explanations for Informational).
Does not guarantee citation outcomes.

### Topics

Groups related grounding queries into broader thematic clusters (e.g.
"Solar Energy" grouping "solar panels," "solar energy efficiency,"
"residential solar installation"), assigned by AI/ML classifiers.
Quality expected to improve as classifiers mature; niche/specialized
domains may see imperfect groupings currently.

Usage: identify strong subject areas, discover content gaps (a topic
generating citation activity with limited site coverage), guide
theme/audience-based content planning rather than keyword-level.

### Citation Share

The percentage of citations attributed to your site out of all
citations shown for a specific grounding query — a *relative* visibility
metric, distinct from Total Citations (a *volume* metric). A site can
have high total citations but low Citation Share if activity for that
query is spread across many sources.

Does **not** expose competitor domain names or identify who holds the
remaining share — shows only your relative presence.

Interpretation guide:
- High and stable share → consistent citation share for that query.
- High but declining share → citation activity becoming more
  distributed; consider content updates/deeper coverage.
- Low share on a core query → smaller portion of citation space;
  consider improving completeness/currency/clarity.
- Growing share → larger share over time; may reflect content changes,
  demand shifts, or ecosystem/model changes.

Explicitly **not** a ranking, traffic, or quality score — driven by many
factors (demand shifts, content changes across the web, model updates,
freshness signals, partner refresh cycles). Can help observe whether
share changes after content updates but does not establish causation.

### Compare

Overlays a previous time period on the same chart as the current view
(current = solid line, comparison = dashed line, day-aligned). Options:
previous period at various durations, or a custom two-range comparison.
Useful for before/after content-update checks and general trend
comparison. Does not explain *why* metrics changed — observational only.

Feedback on these preview capabilities can be submitted via an in-report
UI or standard Bing Webmaster Tools support channels.
