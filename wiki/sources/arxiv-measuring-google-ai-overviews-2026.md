---
type: source
tags: [seo, aeo]
date_published: 2026-05-13
date_ingested: 2026-09-10
origin: raw/studies/arxiv-measuring-google-ai-overviews-2026.md
---

# Measuring Google AI Overviews (Xu, Iqbal & Montgomery, arXiv 2026)

**Citation:** Xu, Haofei; Iqbal, Umar; Montgomery, Jacob M.
(Washington University in St. Louis). "Measuring Google AI Overviews:
Activation, Source Quality, Claim Fidelity, and Publisher Impact."
arXiv:2605.14021v1, published 2026-05-13.
https://arxiv.org/html/2605.14021v1

The first large-scale independent academic audit of Google AI Overviews
in this wiki: 55,393 trending queries over 40 days (Mar 13–Apr 21,
2026), 7,583 AIOs, 61,212 cited reference URLs, and 98,020 atomic
claims verified against the full text of every source the AIO itself
cites. Nearly every other AIO source in this wiki is vendor research;
this one is peer-review-track, publishes its validation numbers
(verifier accuracy 95.6% against two-annotator human labels), and
compares AIO citations directly against the co-displayed first-page
SERP as a control pool.

## Key takeaways

### Activation

- **13.7% overall activation** on trending queries — but see the
  corpus caveat below; this is a very different query population from
  the brand-tracking corpora behind [[aio-ctr-impact]]'s prevalence
  numbers.
- **Question-form queries activate at 64.7% vs. 9.5% for non-question
  queries — 6.8x.** `how` (84.3%) and `why` (73.4%) top the list;
  even the weakest interrogative (`did`, 39.8%) still runs 4–5x
  non-question queries.
- **Query length independently amplifies activation**: among
  non-question queries alone, 9.9% at one word rising to 38.7% at six
  or more words. Length is not just a proxy for question phrasing.
- 13x spread by category (Beauty & Fashion 3.5% → Hobbies & Leisure
  46.1%). Politics (7.5%) and Law & Government (9.6%) are suppressed,
  but **Health is not (26.6%)** — the sensitive-topic caution is
  selective, not blanket.
- Activation rate and claim fidelity are **statistically independent**
  (p = 0.192): a low-AIO category is not a safer-answer category.

### Source selection

- Median **8 references per AIO**; top 5 cited hosts are youtube.com
  (5.49%), en.wikipedia.org (4.39%), facebook.com (3.68%),
  instagram.com (3.65%), usatoday.com (2.80%).
- **AIO citation is broad where the SERP is concentrated.** Top-10
  hosts take 29.7% of AIO citations vs. 49.6% of first-page citations;
  56.3% of AIO-cited hosts were cited exactly once in 40 days. The
  citation pool is a long tail, not a short list of winners.
- **AIO-cited domains are measurably more credible than the
  co-displayed organic results**: mean PC1 0.732 vs. 0.645, significant
  in 14 of 19 categories with **no significant reversal in any
  category**. The authors state this "directly contradicts prior work
  suggesting that AIOs draw on lower-quality sources."
- **UGC share: 14.2% of AIO refs vs. 41.4% of first-page URLs** — AIOs
  cite UGC *less* than the first page in all 19 categories. Four
  platforms (YouTube, Facebook, Instagram, Reddit) are 96.5% of it.
- **29.8% of AIO-cited domains appear nowhere on the corresponding
  first page** (28.5% at URL level). Domain overlap is 25.0% with
  top-5, 41.4% with top-10, 70.2% with the full first page. Crucially,
  **those off-page citations are higher quality, not lower** (PC1 0.758
  vs. 0.724; UGC 3.4% vs. 18.5%).

### Claim fidelity

- **88.97% of claims are consistent** with the sources the AIO cites;
  11.03% are not — **Omitted 6.98%** (no cited source mentions it),
  **Incorrect 2.66%** (a cited source contradicts it), **Ambiguous
  1.39%**.
- Omission outruns active misrepresentation ~2.6:1. The dominant AIO
  failure is asserting something none of its citations support, not
  misreading a citation.
- Median AIO is 93.33% grounded; 41.9% are perfectly grounded. The tail
  is small but real: 2.74% of AIOs have under half their claims
  grounded, 0.85% have none.
- Even under the most generous correction for uncrawlable UGC sources,
  the inconsistency floor is **~5.3%**.
- Highest-fidelity categories are the consequential ones — Health
  94.77%, Politics 93.65%, Science 91.82% — consistent with stricter
  YMYL grounding.
- Climate's 48.23% is a **measurement artifact** (live weather values
  vs. pages re-crawled hours later), not an AIO failure; the authors
  normalize it out and land on 18 of 19 categories inside an
  85.9%–94.8% band.

### Publisher economics

- **50.63% of AIO-cited pages display visible ads** — a conservative
  floor, since the 14.2% UGC share is treated as ad-free. Highest in
  Hobbies & Leisure (63.14%), Sports (60.19%), Entertainment (55.50%);
  lowest in Health (27.77%) and Law & Government (29.47%).
- **Only 2.16% of AIO-bearing SERPs carry Google sponsored ads, and
  0.51% place them above the AIO.** The authors' framing: AIOs
  restructure the page in a way that preserves Google's ad capture
  while reducing publisher click-throughs.

## Relationship to existing wiki claims

- **Conflicts** with [[ai-citation-landscape]]'s "76% of AI Overview
  citations pull from Google's own top-10 organic results" (via
  [[ahrefs-b2b-seo-statistics-2025]]). This study measures 41.4%
  domain overlap at top-10 and 70.2% across the whole first page.
  Logged as Conflicting Evidence on [[ai-citation-landscape]].
- **Extends** [[ai-citation-landscape]]'s AIO sourcing profile with a
  first-page control pool that no vendor source in the wiki provides —
  the relevant comparison is not "AIOs cite a lot of UGC" but "AIOs
  cite *less* UGC and *more* credible domains than the organic results
  sitting directly beneath them."
- **Nuances** [[brightedge-ai-search-same-brands-different-sources]]'s
  "AI Overviews is a UGC-first engine" characterization: same
  direction relative to other engines, but the absolute numbers run
  lower here (14.2% vs. ~17.5–18% UGC; YouTube 5.49% vs. 10.6%), and
  the first-page control reframes what "UGC-first" means.
- **Extends** [[aio-ctr-impact]] on the economics side with the
  supply-side measurement it lacked: what share of the pages feeding
  AIOs actually depend on ad revenue (50.63%+), and how rarely Google's
  own ads are displaced (2.16% of AIO SERPs).
- **Adds a dimension the wiki did not cover at all**: claim fidelity —
  whether an AIO's assertions are actually supported by the sources it
  credits. Filed to the new [[ai-overview-grounding-and-fidelity]].
- **Corroborates, at different magnitudes**, [[aio-ctr-impact]]'s
  "question-format queries trigger AIOs" finding
  ([[seerinteractive-aio-ctr-impact-2026-update]] reports 85.9%; this
  reports 64.7%). Corpus difference, not contradiction — see caveat.

## Caveats

- **The query corpus is trending queries, not commercial queries.**
  Sports alone is 51.4% of the corpus and Entertainment 14.9%, so the
  13.7% headline activation rate is not comparable to the
  brand-keyword and commercial-keyword prevalence numbers in
  [[aio-ctr-impact]]. Per-category rates and within-corpus contrasts
  (question vs. non-question, AIO vs. first page) travel; the headline
  aggregate does not.
- **US desktop, English, 40 days, one snapshot period.**
- Claim verification depends on an LLM verifier (Grok 4.1 Fast
  Reasoning). It is validated at 95.6% weighted accuracy against
  two-annotator human labels, and its errors ran generous rather than
  harsh — but it is still an LLM judging LLM output.
- Social and video platform bodies were not crawled, which inflates
  measured inconsistency (the authors bound this and still find a
  ~5.3% floor) and deflates measured ad prevalence.
- Ad detection is visible-ad detection on crawled pages; affiliate,
  subscription, and lead-gen monetization are invisible to it, so
  "50.63% ad-supported" understates commercial dependence on AIO-cited
  traffic.
