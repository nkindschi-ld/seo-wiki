---
type: playbook
tags: [seo, aeo]
updated: 2026-10-14
---

Why / when to use this: use when setting up or refreshing recurring
stakeholder/client reporting — turns scattered tool data (GSC, GA4,
rank tracking, AI Visibility, backlinks, site audit) into one
consistent, business-facing narrative. Reporting now explicitly
includes AI-search performance alongside traditional metrics, not as a
separate initiative.

## What an SEO report is now

"An overview of selected metrics that illustrate a website's
performance in regular search **and** AI search" — AI Visibility (a
1-100 score, brand mentions, citation counts) is a standard reporting
section in current practice, not optional or experimental.

## Metrics to include

- Organic clicks (traffic from search results)
- AI Visibility score, brand mentions, and citation counts
- Click-through rate (CTR)
- Conversion rate
- Keyword rankings
- Backlinks and referring domains
- Site health / technical indicators

## Data sources, mapped to metric

- **Google Search Console** (Performance > Search Results) — organic
  clicks, average CTR, page-level export.
- **AI Visibility tooling** — AI Visibility score, brand mentions,
  citation counts.
- **Google Analytics 4** (Reports > Engagement > Landing page, filtered
  to organic) — conversions.
- **Organic Traffic Insights** (or equivalent) — de-anonymizes
  "not provided" keyword data by page.
- **Rank/position tracking** — weekly automated ranking updates. Since
  2026-09-13, scraped rank data can contain silently poisoned SERPs; see
  "Before reporting a ranking drop" below and [[serp-poisoning]].
- **Backlink tooling** — referring domains, new/lost backlinks,
  Authority Score/Domain Rating trend.
- **Site audit tooling** — crawlability, performance, and UX health
  across 100+ technical factors.

## Report structure

Executive summary → traffic overview → AI Visibility data → keyword
performance → conversions and ROI → backlink analysis → content
performance → technical health status → recommended actions.

## Before reporting a ranking drop

Since late September 2026, Google has been serving some rank-tracker
requests complete-looking SERPs with most of the usual sites swapped out
([[nozzle-poisoned-google-serps-2026]]: 8.0% of SERPs since Sep 13; a
tracked site falls out of the top 10 on 58.6% of them). Check before
explaining a drop:

1. **Compare against the keyword's usual page-1 sites over prior weeks,**
   not just last week's or yesterday's SERP, which may be poisoned too. If
   most of the usual sites vanished at once, suspect the data, not the
   site.
2. **Give it about three days.** 77.9% of poisoned SERPs are back to
   normal within three days. A real ranking change persists.
3. **Confirm in Search Console.** If impressions and clicks for the
   query or page are steady, nothing happened to the site.
4. **Note the higher-risk segments:** "near me" and long-tail queries,
   legal and home-services keywords, and markets like Australia, India and
   Canada.

If a drop fails these checks, report it as a data anomaly, not a loss.

## Presentation best practices

- Use a logical structure aligned to business goals, not a raw metrics
  dump.
- Explain **why** a metric changed and what caused the movement — don't
  just report the delta.
- Keep a consistent cadence (weekly, monthly, or quarterly — monthly is
  most common).
- End on actionable positives and next steps, not just a list of
  problems.
- Use data visualizations to simplify complex or multi-metric sections.

## Automation

Drag-and-drop/widget-based reporting tools can pull from multiple data
sources into one dashboard, schedule automated report generation, and
handle recurring email delivery — worth setting up once cadence and
structure are settled, rather than rebuilding the report manually each
period.

## Checklist

- [ ] Report includes both traditional metrics and AI Visibility
      metrics.
- [ ] Structure follows: summary → traffic → AI visibility → keywords →
      conversions/ROI → backlinks → content → technical health →
      actions.
- [ ] Each significant metric change has a stated cause, not just a
      number.
- [ ] Any ranking drop was checked against the keyword's multi-week
      history and Search Console before reporting (rules out
      [[serp-poisoning]]).
- [ ] Report ends with recommended next actions, not only problems.
- [ ] Cadence is fixed and consistent across reporting periods.
- [ ] Automated/scheduled delivery set up if this is a recurring
      report.

## See also

- [[generative-engine-optimization]] and [[ai-visibility-correlation-factors]]
  — background on what AI Visibility metrics actually measure.
- [[seo-competitive-analysis]] — competitor benchmarking data that can
  feed into the same report.
- [[keyword-mapping-and-cannibalization]] — the keyword-ranking data
  source for the keyword-performance section.

- [[serp-poisoning]] — why scraped rank data since Sep 2026 can show
  fake drops.

See [[semrush-seo-report]] for the full source writeup, and
[[nozzle-poisoned-google-serps-2026]] for the rank-drop check.
