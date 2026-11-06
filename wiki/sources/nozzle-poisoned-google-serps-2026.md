---
type: source
tags: [seo, aeo]
date_published: 2026-10-10
date_ingested: 2026-10-14
origin: raw/studies/nozzle-poisoned-google-serps-2026.md
---

# Poisoned Google SERPs (Nozzle Research)

**Citation:** Nozzle Research. "Poisoned Google SERPs." Nozzle, 2026-10-10
(data through 2026-10-09). No individual byline.
https://nozzle.io/research/poisoned-google-serps/
(27.5M SERPs from a representative sample of the datasets Nozzle collects
for customers, 660K+ keywords with poisoned SERPs, 49 countries, desktop /
iPhone / Android, country- to postal-code-level targeting. Baseline
2026-08-20 to 09-09; study window 2026-09-13 to 10-09. Per-day, per-site,
per-country, per-industry and per-SERP-feature CSVs are published.)

## Key takeaways

- **Google is answering scrapers with wrong results instead of
  refusing them.** A "poisoned" SERP is a complete, normal-looking page
  (same template, same frontend build, no error, no captcha) with most
  of the keyword's usual sites swapped out. Nothing in the HTML marks
  it. Only the keyword's own history does.
- **Size and timing.** 8.0% of SERPs were poisoned since 2026-09-13,
  against 0.17% in the baseline. Four in five customer datasets had at
  least one. Sequence: requests to Google started failing in bulk on
  **Sep 13** (collection volume fell for two weeks); poisoned SERPs first
  appeared among the requests that got through on **Sep 20**; the share
  peaked at 25–27% on **Sep 27–29**; it has run at about 5–11% a day
  since **Oct 1**.
- **Why "poisoning," not blocking.** A refused request tells a scraper
  to retry; a poisoned one gets stored as real data. Nozzle attributes
  it to Google's response to bulk AI scraping and grounding (collecting
  Google results to feed AI answers), with rank trackers caught because
  they collect SERPs the same way. This attribution is Nozzle's
  inference, not a Google statement.
- **The organic results are mostly replaced.** Organic results keep
  20.7% of the previous SERP's sites, against 88.5% in the baseline
  (1.79 previous top-10 sites gone per SERP vs 0.23). Example: "white
  label local seo" went from nine white-label SEO vendors to a WordPress
  tool, a steakhouse, and several .gov sites. Google read "local"
  literally.
- **What replaces them: social platforms and forums.** On the same
  keywords, top-10 presence on poisoned vs other SERPs: Reddit 28.8% vs
  20.8% (+8.0 pts), Facebook +5.5, LinkedIn +3.1, Instagram +2.5,
  Quora +1.4, Etsy, JustAnswer and TikTok up about 1 pt. YouTube
  (−2.4), Yelp (−1.8) and MapQuest (−0.7) lose ground. 7.2% of poisoned
  SERPs have three or more social sites in the top 10 (vs 2.7%). On US
  keywords, 14.2% show a foreign country-code site such as .ca or .co.uk
  (vs 6.1%).
- **Paid parts of the page hold steady; the rest don't.** Share of the
  previous SERP's items kept, baseline → poisoned: organic 88.5% →
  20.7%, People also search for 87.9% → 30.7%, People also ask 87.4% →
  46.9%, AI Overview sources 68.8% → 42.3%, local pack 85.8% → 60.5%.
  Shopping barely moves (92.8% → 92.2%) and ads keep *more* (70.6% →
  83.7%). Which features appear changes too: AI Overviews on 34.9% of
  poisoned SERPs vs 54.2%; People also search for on 52.7% vs 87.2%;
  image packs nearly double (44.2% vs 23.0%); forum blocks 27.0% vs
  20.5%. On desktop keywords that normally paginate to page 8+, 50.9%
  of poisoned SERPs stop by page 4 (vs 0.2%).
- **Tracked sites "crash."** Where a project's own site is one of the
  keyword's usual sites, it was out of the top 10 on 58.6% of poisoned
  SERPs, against 2.7% in the baseline.
- **It's brief.** 80% of poisoning spells last one SERP, 15% two, 5%
  three or more. The next SERP has the usual sites back 55.9% of the
  time; 77.9% within three days (median two days).
- **Who's hit most.**
  - *Country:* Austria 18.8%, South Africa 18.4%, UAE 14.4%, New Zealand
    13.8%; among big markets Australia 11.5%, India 10.9%, Canada 10.5%,
    US 8.5%. Western Europe is lowest: UK 3.0%, Spain 3.4%, France and
    Italy 3.9%, Germany 4.3%.
  - *Device:* barely matters (desktop 7.7%, iPhone 8.3%, Android 7.1%).
  - *Query type:* "near me" 11.4% vs 7.8% for everything else; long tail
    (<100 searches/month) 9.4% vs 6.1–7.1%; most-navigational brand
    phrases lowest at 5.3%. Local vs national targeting makes no
    difference once mobile and "near me" are controlled for (7.5% vs
    7.4% across 21,508 matched pairs).
  - *Industry (US):* legal 15.9% overall (51.3% on Sep 27), home
    services 12.7%, weddings 11.6%; automotive 5.3% and pets 4.3% lowest.
    Every industry peaked Sep 27–29.
  - *Collection route:* on the same days (Sep 30–Oct 9) one of Nozzle's
    routes to Google returned 1–7% poisoned SERPs and another 9–30%.
- **How to tell it from a real ranking change** (turned into a check in
  [[seo-reporting]] and [[serp-poisoning]]):
  1. Compare against the keyword's usual page-1 sites over prior weeks,
     not just yesterday (yesterday may be poisoned too).
  2. Wait: a real ranking change stays; poisoning mostly reverses within
     three days.
  3. Look for the thin-page tells (no AI Overview or People also search
     for, more image packs and social sites, shallow pagination). None is
     reliable alone.
  4. Check Search Console. Steady impressions and clicks mean nothing
     happened to the site.

## Method

A keyword's "usual sites" are those in its top 10 on at least 60% of its
baseline SERPs (keywords with five or more baseline SERPs only; SERPs with
no organic results excluded). A SERP is poisoned when fewer than half of the
usual sites appear on any of its pages **and** they come back: at least 80%
back on a later SERP within 14 days, or most of the sites missing from the
previous SERP back within three days. Poisoned-vs-other comparisons compare
each keyword with itself, weighted by its poisoned SERPs. Screenshots render
Nozzle's stored page-1 HTML in Chrome with Google's external scripts blocked.

## Caveats

- **Vendor with a motive.** Nozzle sells rank tracking; "Google is
  poisoning us" is a more flattering explanation for bad data than a
  collection fault. The method mitigates this (the definition requires
  the usual sites to return, and the route split shows collection-path
  dependence), but there is no independent replication yet.
- **Attribution is inferred.** The "response to AI scraping" reading is
  from timing and pattern, not a Google statement.
- **Definition undercounts the recent days.** A SERP only counts as
  poisoned once its usual sites come back, so the last few days were
  still filling in at publication. It also can't detect poisoning on
  keywords without a stable baseline.
- **Route-dependent.** Rates vary 1–30% by collection route on the same
  days, so other trackers' exposure may differ a lot from Nozzle's
  averages.

## Relationship to existing wiki claims

- **No conflicts.** No existing source in the wiki relies on scraped
  Google SERP data collected after 2026-09-13 (checked on ingest). The
  impact is forward-looking: a data-quality caveat for future sources,
  recorded in [[serp-poisoning]].
- **Extends** [[chatgpt-vertical-retrieval-engines]]: ChatGPT reaches
  Google results via `serpapi_auto_*` (a commercial Google-SERP
  scraper). If Google poisons scraped requests, that path may return
  poisoned results too. This is a wiki hypothesis; the study doesn't test
  or claim it.
- **Adds a measurement caveat to** [[ai-visibility-measurement-methodology]]:
  scraped AI Overview prevalence and citation-source data are affected
  (AI Overviews appear less often and cite different sources on poisoned
  SERPs).
- **Adds a "volatility that isn't an update" category** to
  [[google-algorithm-update-history]].

## Updated pages

- [[serp-poisoning]] (new concept)
- [[seo-reporting]]
- [[ai-visibility-measurement-methodology]]
- [[chatgpt-vertical-retrieval-engines]]
- [[google-algorithm-update-history]]
