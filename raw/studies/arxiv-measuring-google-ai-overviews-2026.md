# Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact

Source: https://arxiv.org/html/2605.14021v1 (arXiv:2605.14021v1)
Authors: Haofei Xu, Umar Iqbal, Jacob M. Montgomery (Washington University in St. Louis)
Published: 2026-05-13
Fetched: 2026-09-10

## Methodology

- Puppeteer-based crawler issuing **55,393 trending queries** (Google
  Trends, 19 topical categories) over **40 days: March 13 – April 21,
  2026**.
- **7,583 AI Overviews (AIOs)** captured, embedding **61,212 reference
  URLs** across **7,479 unique hostnames**. First-page comparison pool:
  308,407 URLs across 15,394 hostnames.
- AIOs decomposed into **98,098 atomic claims** (98,020 verified);
  each claim verified against full text of every cited reference.
- Claim verifier: Grok 4.1 Fast Reasoning, temperature 0, few-shot
  prompts. Five labels: Clear / Vague / Ambiguous / Incorrect / Omitted.
- Verifier validation: stratified 100-verdict sample, two independent
  annotators, near-perfect inter-annotator agreement; verifier matched
  human label on 98/100. Frequency-weighted verifier accuracy **95.6%**.
  Both errors were over-generous (never wrongly flagged a grounded claim).
- Domain credibility measured with **PC1** (Lin et al. 2023): first
  principal component of multiple expert + crowd ratings of news-domain
  credibility, continuous 0–1 scale. PC1 coverage: 60.5% of AIO refs,
  51.8% of first-page URLs.
- Query corpus is trending-query-based and heavily skewed: Sports is
  51.4% of the corpus, Entertainment 14.9%.

## RQ1 — Activation

- Overall AIO activation: **13.7%** (7,583 of 55,393).
- Day-to-day rate broadly stable, no monotonic trend, but sharp
  short-lived spikes around major public events (Oscars/NCAA selection
  Mar 16, Artemis II launch Apr 2, NCAA Round of 64 Mar 20 — query
  volume 1.3–2.2x daily mean). AIO exposure concentrates where
  information demand peaks.

### By category (Table 3, sorted by query volume)

| Category | Queries | w/ AIO | Rate | % of corpus |
|---|---|---|---|---|
| Sports | 28,446 | 2,782 | 9.8% | 51.4% |
| Entertainment | 8,251 | 1,348 | 16.3% | 14.9% |
| Business & Finance | 3,360 | 880 | 26.2% | 6.1% |
| Other | 2,957 | 405 | 13.7% | 5.3% |
| Law & Gov. | 2,924 | 280 | 9.6% | 5.3% |
| Politics | 2,166 | 162 | 7.5% | 3.9% |
| Climate | 1,735 | 128 | 7.4% | 3.1% |
| Science | 1,560 | 622 | 39.9% | 2.8% |
| Hobbies & Leisure | 1,185 | 546 | 46.1% | 2.1% |
| Games | 778 | 80 | 10.3% | 1.4% |
| Technology | 464 | 86 | 18.5% | 0.8% |
| Shopping | 158 | 23 | 14.6% | 0.3% |
| Beauty & Fashion | 142 | 5 | 3.5% | 0.3% |
| Autos & Vehicles | 138 | 19 | 13.8% | 0.2% |
| Pets & Animals | 45 | 6 | 13.3% | 0.1% |
| **Total** | **55,393** | **7,583** | **13.7%** | 100% |

(Health reported at 26.6% in the text; Travel & Transport 8.7%,
Food & Drink 17.1%, Jobs & Education also reported.)

- 13x spread across categories (3.5% Beauty & Fashion → 46.1% Hobbies
  & Leisure).
- Politics (7.5%) and Law & Government (9.6%) below average, consistent
  with Google's stated caution on sensitive topics — but Health (26.6%)
  shows the suppression is **not applied uniformly** to all sensitive
  areas.
- **Activation rate and claim fidelity are largely independent**
  (p = 0.192): low-activation categories are not inherently safer.

### By query phrasing and length

- **Question-form queries: 64.7% activation vs. 9.5% for non-question
  queries — a 6.8x difference.** (Question-form = leading whole word is
  one of 15 interrogatives: who, what, where, when, why, how, which, is,
  are, was, can, do, does, did, has.)
- Open-ended explanatory interrogatives activate most: **how 84.3%**,
  **why 73.4%**. Closed-form lookups less: **who 47.9%**, **did 39.8%** —
  but even the lowest interrogatives trigger 4–5x more than
  non-question queries.
- **Length independently amplifies activation.** Restricting to
  non-question queries only, AIO rate climbs from **9.9% at one word to
  38.7% at six or more words**. (Overall — questions included — six-plus
  word queries hit 58.1%.)
- Combined implication: AIO exposure concentrates among users posing
  open-ended questions requiring synthesis — precisely where fidelity
  failures are most consequential.

## RQ2 — Source selection

### Reference reliance

- Median **8 references per AIO** (mean 8.1, range 1–32).
- Reference count by category: Travel & Transportation (median 12),
  Health (11), Shopping and Autos & Vehicles (10) cite most; Sports,
  Jobs & Education, Hobbies & Leisure, Climate cluster at median 7.
- **AIO citation is long-tailed; first-page SERP is concentrated:**

| Top-N hostnames | Share of AIO citations | Share of first-page citations |
|---|---|---|
| Top 5 | 20.0% | 39.1% |
| Top 10 | 29.7% | 49.6% |
| Top 50 | 48.3% | 65.7% |
| Top 100 | 57.1% | 71.1% |

- **4,212 hosts (56.3% of AIO's unique hosts) were cited exactly once**
  over 40 days, vs. 42.1% singletons on the first-page SERP — despite
  the SERP pool having more than twice as many unique hosts (15,394 vs.
  7,479). "Source breadth, not concentration, is the dominant shape of
  AIO citation."
- Top 5 cited hostnames: **youtube.com 5.49%, en.wikipedia.org 4.39%,
  facebook.com 3.68%, instagram.com 3.65%, usatoday.com 2.80%.**

### AIO vs. first-page source quality

- Mean PC1 credibility: **AIO refs 0.732 vs. first-page 0.645 — a gap
  of +0.087** (Welch's t, p < .001; 37,020 AIO refs vs. 159,752 matched
  first-page URLs).
- Per-category Welch's t-tests with Bonferroni correction: significant
  in **14 of 19 categories, all favoring AIO references; no category
  shows a significant reversal.** The 5 non-significant categories all
  have small AIO subsamples (power, not direction reversal).
- AIO PC1 range: Science 0.769, Business & Finance 0.751, Sports 0.748
  at the top; Autos & Vehicles 0.586 and Beauty & Fashion 0.536 at the
  bottom.
- Excluding unscored URLs is conservative — unmatched entries are
  dominated by social platforms and brand-owned domains that skew
  low-credibility and appear at higher volume in the first-page pool.
- **"This finding directly contradicts prior work suggesting that AIOs
  draw on lower-quality sources than traditional results (Aral et al.,
  2026)."**
- But: source quality and claim fidelity are **largely independent** —
  better sourcing alone won't reduce the unsupported-claim rate.

### UGC prevalence

- UGC defined as platforms without strong editorial moderation:
  facebook, instagram, linkedin, pinterest, quora, reddit, threads,
  tiktok, twitter/x, youtube. Wikipedia explicitly excluded (strong
  editorial review).
- **14.2% of AIO reference URLs are UGC (8,688 of 61,212) vs. 41.4% of
  first-page result URLs (127,814 of 308,407).** AIOs cite UGC *less*
  than the first page in **all 19 categories**.
- Four platforms are 96.5% of the AIO UGC contribution: youtube.com
  5.49%, facebook.com 3.68%, instagram.com 3.65%, reddit.com 0.87%.
  All other UGC platforms together under 1%.
- 3x spread by category: Climate 9.3% and Health 10.7% lowest; Beauty &
  Fashion 28.9% and Autos & Vehicles 27.4% highest. Sports 11.2%,
  Entertainment 19.4%, Technology 20.3%, Shopping 25.9%.
- This lower UGC share partly explains AIOs' higher average credibility.

### Reference overlap with first-page results

- Averaged across the 7,583 AIOs, AIO reference domains overlap:
  **25.0% with top-5 first-page results, 41.4% at top-10, 70.2% across
  the full first page.**
- **29.8% of AIO reference domains do not appear anywhere on the
  corresponding first page.** At URL level, **28.5% (17,451 of 61,206)**
  come from hosts the first page does not surface for that query.
- **Off-page references are higher quality, not lower**: mean PC1 0.758
  and UGC share 3.4%, vs. PC1 0.724 and UGC share 18.5% for AIO refs
  that also appear on the first page.
- "Google describes AIOs as grounded in its core ranking infrastructure,
  but the AIO and first-page mechanisms clearly apply different
  selection criteria even when acting on the same index. Thus,
  publishers whose content informs an AIO are not necessarily the same
  publishers whose pages users would encounter by scrolling past it."

## RQ3 — Claim fidelity

- 98,020 verified claims across 7,491 verifiable AIOs (mean 12.9 claims
  per AIO, median 12, range 0–64).

| Label | Count | Share |
|---|---|---|
| Clear (literal support) | 82,933 | 84.61% |
| Vague (inferred support) | 4,271 | 4.36% |
| Ambiguous (cited sources conflict) | 1,367 | 1.39% |
| Incorrect (cited source contradicts) | 2,609 | 2.66% |
| Omitted (no cited source mentions it) | — | 6.98% |

- **88.97% consistent, 11.03% inconsistent.**
- AIO-level: median AIO has **93.33%** of claims grounded; **41.9%**
  (3,141) are perfectly grounded; **61.8%** (4,631) are ≥90% consistent.
  Failure tail: **2.74%** (205 AIOs) have fewer than half their claims
  grounded; **0.85%** (64) have zero consistent claims.
- **Omission dominates active misrepresentation** (~2.6x more frequent).
- Measurement caveat, self-bounded: 59.9% of Inconsistent claims appear
  in AIOs citing at least one uncrawled UGC source. Even assuming *all*
  of those are actually supported, the residual inconsistency rate would
  fall from 11.0% only to **~5.3%** — "a substantive floor."
- The Incorrect category is the sharpest failure mode: direct conflict
  between an AIO assertion and a source the AIO itself cites for it —
  something a reader of the summary alone cannot detect.

### By category

- Highest fidelity: **Health 94.77%, Politics 93.65%, Science 91.82%,
  Business & Finance 91.42%, Hobbies & Leisure 91.40%** — several of
  the most consequential categories, possibly reflecting stricter
  grounding under Google's YMYL policy.
- Excluding Climate, per-category fidelity ranges 76.85% (Jobs &
  Education) to 94.77% (Health).
- **Climate's 48.23% is a measurement artifact**, not an AIO failure:
  dominated by weather/forecast queries where the AIO reports live
  values from structured weather feeds; cited pages (weather.com,
  forecast.weather.gov) update continuously, so by crawl time the
  figures have shifted. Jobs & Education shows the same pattern on
  school-closure queries; Technology on weather; Shopping on trending
  products.
- Normalizing out those real-time sub-populations: Technology rises to
  89.41%, Shopping to 85.90%, Jobs & Education to 87.71% — after which
  **18 of 19 categories sit in an 85.9%–94.8% band**.
- The remaining gradient tracks the availability of authoritative
  editorial text on a topic.
- The 9.64% combined Omitted + Incorrect rate should be read as a
  **conservative ceiling** on substantive AIO unfaithfulness.

## RQ4 — Publisher economics

- **50.63% of AIO-cited reference URLs (30,994 of 61,212) display
  visible ads** — i.e. more than half the pages whose content makes AIO
  synthesis possible run ad-supported models dependent on the page-view
  traffic AIOs intercept.
- This is a **conservative lower bound**: a further 14.2% of references
  point to social/video platforms the pipeline does not crawl and treats
  as ad-free, though they run large ad businesses.
- Ad prevalence by category: Hobbies & Leisure 63.14%, Sports 60.19%,
  Entertainment 55.50%, Science 41.85%, Business & Finance 39.97%,
  Law & Government 29.47%, Health 27.77%.
- **Only 2.16% of AIO-bearing SERPs display Google sponsored ads, and in
  just 0.51% do those ads appear above the AIO.**
- Framing: "AIOs restructure the page in a way that preserves Google's
  ad capture while reducing click-throughs to publishers."

## Concluding position and recommendations

The paper's summary judgment: the system "is performing better than its
critics often claim and worse than Google's own public
characterizations suggest."

Tensions documented with Google's public claims:
- Google says AIOs draw from top web results; 29.8% of cited domains
  don't appear on the first page at all.
- Google emphasizes grounding architecture; ~11% of claims remain
  unsupported by the sources the AIO itself cites.
- Google's own sponsored inventory persists on AIO-bearing pages while
  publisher click-throughs are compressed.

Recommendations:
- **Transparency**: publish measurable performance targets by category;
  genuine support for independent auditing.
- **Economics**: revenue-sharing or licensing arrangements with content
  producers; design changes making citations more prominent and clicks
  easier; deployment restrictions in financially fragile content
  ecosystems.
- **Technical limits**: unsupported claims are "inherent to generative
  AI at its current state"; better sources alone won't fix it —
  structural fixes needed, prioritized where errors carry the greatest
  consequence (health, politics, science).
- **Future work**: whether users act on and propagate errors;
  distributional effects across user populations; tracking system
  evolution.
