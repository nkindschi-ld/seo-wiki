---
type: concept
tags: [seo, aeo]
updated: 2026-10-14
---

# SERP Poisoning

**SERP poisoning** is Google serving automated collectors a complete,
normal-looking results page whose results have been swapped out, instead of
blocking the request. The term and all data here come from
[[nozzle-poisoned-google-serps-2026]] (27.5M SERPs, 49 countries, data
2026-08-20 to 10-09). It is single-source and vendor-reported so far.

It matters for two reasons:

1. **Rank tracking and SERP-feature data** collected by scraping can now
   contain silent fake data. A poisoned page has no error, no captcha and
   nothing in the HTML to mark it. It gets stored as a real ranking.
2. **AI answers grounded in scraped Google results** may be exposed to the
   same thing. Nozzle frames poisoning as Google's response to bulk AI
   scraping and grounding, with rank trackers as collateral.

## Timeline

| Date (2026) | Event |
|---|---|
| Aug 20 – Sep 9 | Baseline: 0.17% of SERPs meet the poisoned definition |
| Sep 13 | Requests to Google start failing in bulk; collection volume falls for two weeks |
| Sep 20 | Poisoned SERPs first appear among requests that get through |
| Sep 27–29 | Peak: 25–27% of SERPs poisoned (legal SERPs 51.3% on Sep 27) |
| Oct 1 onward | Steady state of about 5–11% a day |

Block first, then poison is the reason Nozzle calls it poisoning. A refusal
makes a scraper retry; a plausible wrong answer gets kept.

## What a poisoned SERP looks like

- **Organic results mostly replaced.** 20.7% of the previous SERP's sites
  kept, against 88.5% normally. A tracked site that is one of the keyword's
  usual sites misses the top 10 on 58.6% of poisoned SERPs (vs 2.7%).
- **Replacements skew social and forum.** Reddit (+8.0 pts top-10
  presence), Facebook (+5.5), LinkedIn (+3.1), Instagram, Quora, TikTok up.
  YouTube, Yelp and MapQuest down. More foreign ccTLD sites on US keywords
  (14.2% vs 6.1%). Results can follow an over-literal reading of the query.
- **Paid features untouched.** Shopping keeps 92.2% of its items (vs
  92.8%) and ads keep more than usual (83.7% vs 70.6%).
- **Thinner page.** AI Overviews appear less (34.9% vs 54.2%) and cite
  different sources (42.3% kept vs 68.8%). People also search for appears
  less (52.7% vs 87.2%), image packs and forum blocks appear more, and
  desktop pagination often stops by page 4.
- **Short-lived.** 80% of spells are a single SERP; 77.9% of keywords have
  their usual sites back within three days.

## Who's exposed most

"Near me" queries (11.4%), long-tail phrases (9.4%), legal and home
services, and certain countries (Austria 18.8%, Australia 11.5%, India
10.9%, Canada 10.5%, US 8.5%). Brand/navigational queries (5.3%), Western
Europe (UK 3.0%) and device type matter little or are least affected. The
biggest single variable may be the **collection route**: on the same days
one route saw 1–7% and another 9–30%.

## Implications

### For SEO reporting

A one-to-three-day ranking drop since late September 2026 is more likely
poisoning than a real change, especially on local, long-tail, or legal and
home-services keywords. Before reporting a drop or reacting to it, run the
check in [[seo-reporting]]:

1. Compare against the keyword's usual page-1 sites over the previous
   weeks, not just the prior day.
2. Wait about three days. Real changes persist.
3. Confirm in Search Console. Steady impressions and clicks mean the site
   didn't move.

Poisoning is separate from algorithm volatility. See
[[google-algorithm-update-history]].

### For reading third-party studies (ingest rule)

Treat any study built on **scraped Google SERP data collected after
2026-09-13** as potentially contaminated unless it describes how it
filtered poisoned pages. That includes rank-volatility indexes, Reddit or
social share of Google results, AI Overview prevalence rates and AI
Overview citation-source studies (see
[[ai-visibility-measurement-methodology]]). The contamination is
directional: it **inflates** Reddit/Facebook/LinkedIn share and
volatility, and **deflates** AI Overview prevalence and YouTube/Yelp share.
Flag it on ingest; don't discard the study.

As of 2026-10-14, no source in this wiki uses such data.

### For AI search (hypothesis, unverified)

Per [[chatgpt-vertical-retrieval-engines]], ChatGPT reaches Google results
through `serpapi_auto_*`, a commercial Google-SERP scraper. If Google
poisons scraped requests broadly, Google-sourced grounding in ChatGPT (and
any other engine grounding on scraped Google results) could receive the
same swapped results, which would also push more Reddit and social content
into the candidate pool. Neither Nozzle nor any other source tests this.
It's an open question, not a finding.

## Open questions

- Has Google confirmed it, or said whether it targets AI grounding
  specifically?
- Do other rank trackers (Semrush, Ahrefs, STAT, SerpApi itself) see the
  same rates, and do they filter poisoned pages?
- What separates the low-poisoning and high-poisoning collection routes?
- Does Google-sourced grounding in AI engines show the same shift?

## See also

- [[nozzle-poisoned-google-serps-2026]] — the source study.
- [[seo-reporting]] — where the rank-drop check lives.
- [[ai-visibility-measurement-methodology]] — measurement caveats for
  scraped AI Overview data.
- [[chatgpt-vertical-retrieval-engines]] — the SerpAPI path into ChatGPT.
- [[google-algorithm-update-history]] — real ranking volatility, to tell
  apart from this.
- [[how-google-search-works]] — the baseline pipeline being bypassed.
