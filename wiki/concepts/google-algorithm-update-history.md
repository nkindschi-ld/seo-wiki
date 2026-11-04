---
type: concept
tags: [seo]
updated: 2026-10-26
---

# Google Algorithm Update History

A taxonomy and timeline of Google's named search ranking updates and
incidents, based on
[[google-search-status-dashboard-history]] (a live Google status page,
snapshotted 2026-07-07 covering July 2021–June 2026, re-checked
2026-10-26 for the 2026 list below). Full chronological list through
June 2026 lives in `wiki/timeline.md`; this page synthesizes the patterns.

## 2026 updates

Every ranking update on Google's Search Status Dashboard in 2026, as
checked on 2026-10-26. Times are US/Pacific. No core update has run since
the May 2026 core update. The dashboard lists nothing after the September
2026 spam update finished on Oct 8.

| Update | Rollout | Length | What it targeted | Source |
|---|---|---|---|---|
| February 2026 Discover update | Feb 5–26 | 21 days, 17 hours | Discover feed, not web search rankings | [Dashboard](https://status.search.google.com/incidents/mYbNTqV1ytDc2fA8hUz4) |
| March 2026 spam update | Mar 24–25 | 19 hours, 30 minutes | Spam policy violations | [Dashboard](https://status.search.google.com/incidents/VbnSXAH4SmEcxPtx4YSD) |
| March 2026 core update | Mar 27–Apr 8 | 12 days, 4 hours | Broad core ranking systems | [Dashboard](https://status.search.google.com/incidents/7eTbAa2jWdToLkraZj5y) |
| May 2026 core update | May 21–Jun 2 | 11 days, 21 hours | Broad core ranking systems | [Dashboard](https://status.search.google.com/incidents/wdAXJk6LRRihEjpzEeWE) |
| June 2026 spam update | Jun 24–26 | 2 days, 1 hour | Spam policy violations | [Dashboard](https://status.search.google.com/incidents/YUX1peHev5a4fkxLDiUQ) |
| August 2026 spam update | Aug 18 (09:27)–Aug 21 (01:49) | 2 days, 16 hours | Spam policy violations, all languages and locations. Google called it "a normal spam update" and named no narrower target. | [Dashboard](https://status.search.google.com/incidents/LEubPCm2octf2uMqCFKE), [Google on LinkedIn](https://www.linkedin.com/posts/today-we-released-the-august-2026-spam-update-share-7495517568963891201-qUDS/) |
| September 2026 spam update | Sep 24 (09:15)–Oct 8 (01:00) | 13 days, 16 hours | Spam policy violations, all languages and locations. Google called it "a normal spam update" and named no narrower target. Google estimated up to two weeks. At almost 14 days, it was the longest 2026 spam update. | [Dashboard](https://status.search.google.com/incidents/XhUDXP7A67iHCD2kmbVu), [Google on X](https://x.com/googlesearchc/status/2103159043347128638) |

Google didn't say either spam update targeted link spam or site
reputation abuse. Some third-party coverage says "not link spam," but
that's the writers' reading, not Google's statement. Google's guidance
for both points to its
[spam updates documentation](https://developers.google.com/search/docs/appearance/spam-updates).

## Update types

- **Core update**: broad changes to Google's overall ranking systems,
  not targeted at a specific issue. The most frequent update type,
  recurring roughly every 2-4 months throughout the whole period covered.
- **Spam update / link spam update**: targets spam and manipulation
  tactics specifically (e.g., link schemes), separate from general core
  ranking changes.
- **Helpful content update**: a distinct named update type that appeared
  three times — August 2022, December 2022, September 2023 — and never
  again afterward in this dashboard's history.
- **Product reviews update / reviews update**: a distinct named update
  type appearing seven times from December 2021 through November 2023,
  renamed partway through from "product reviews update" to just "reviews
  update," and never appearing again afterward.
- **Page experience update**: appeared once (desktop, February 2022) in
  this dashboard's coverage window.
- **Discover update**: appeared once (February 2026) in this dashboard's
  coverage window.
- **Ranking ongoing issue**: an incident/bug report rather than an
  intentional named update — appeared twice (October 2023, August 2024).

## Helpful Content and Reviews systems appear to have merged into Core

Two update types that were shipped as their own separate, named
releases early in the dashboard's history — Helpful Content Updates and
Product Reviews/Reviews Updates — stop appearing as distinct entries
after September 2023 and November 2023 respectively, even though core
updates continue on their regular cadence afterward. This pattern is
consistent with Google folding both systems into its core ranking
systems rather than continuing to ship them as separately-named,
separately-announced updates. This wiki has not yet ingested a source
that explicitly confirms this as Google's stated reasoning — flagged as
an inference from the update-naming pattern, not a directly-sourced
claim.

## Practical relevance

- **Timing content/SEO work around update cadence**: core updates land
  roughly every 2-4 months; expect ranking volatility in the weeks
  following each one (durations in the source range from under a day to
  over 40 days).
- **"Helpful content" and "product reviews" as evaluation criteria
  still matter**, even though they're no longer shipped as separately
  named updates — they're presumably now embedded in the standing core
  ranking systems, consistent with [[e-e-a-t-and-page-quality]]'s
  framing of "helpful, people-first content" as an ongoing quality
  standard rather than a one-time update to react to.
- **Not all tracked volatility is an update.** Since 2026-09-13, Google
  has been serving some rank-tracker requests poisoned SERPs (swapped
  results on a normal-looking page), peaking at 25–27% of SERPs on
  Sep 27–29 per [[nozzle-poisoned-google-serps-2026]]. That's a data
  collection problem, not a ranking change, and it isn't on the Search
  Status Dashboard. Third-party volatility indexes built on scraped SERPs
  from that period will overstate volatility. See [[serp-poisoning]].
- Check `wiki/timeline.md` directly for the full dated list, and
  re-ingest this source periodically since it's a live page that grows
  over time.

## See also

- [[e-e-a-t-and-page-quality]] — the quality framework these updates
  are presumably built on.
- `wiki/timeline.md` — the full chronological event list this concept
  synthesizes.
- [[serp-poisoning]] — fake volatility from scraped-SERP poisoning, to
  tell apart from real updates.
- [[classic-seo-ranking-factors]] — the tactic-level playbook these
  updates repeatedly rewarded or penalized; useful for reading any
  given update against what it actually changed in practice.
- [[content-pruning-playbook]] — the standard remediation after a core
  update hits a site with a large low-quality content footprint.
