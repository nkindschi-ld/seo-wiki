---
type: source
tags: [seo, aeo]
date_published: 2026-05-13
date_ingested: 2026-08-06
origin: raw/studies/xu-measuring-google-ai-overviews-2026.pdf
---

# Xu, Iqbal & Montgomery — Measuring Google AI Overviews (arXiv 2026)

**Citation:** Haofei Xu, Umar Iqbal, Jacob M. Montgomery (Washington
University in St. Louis), "Measuring Google AI Overviews: Activation, Source
Quality, Claim Fidelity, and Publisher Impact." arXiv:2605.14021v1, published
2026-05-13. Study window Mar 13–Apr 21 2026.
https://arxiv.org/html/2605.14021v1

**Consolidation note (2026-09-17):** this page merges two source pages that
covered the same paper under different slugs — the original PDF ingest
(2026-08-06) and a later, longer markdown-extraction ingest (2026-09-10) filed
as `arxiv-measuring-google-ai-overviews-2026`. That slug has been retired and
all inbound links repointed here; this page is now the single entry for the
paper. Both raw captures are retained:
`raw/studies/xu-measuring-google-ai-overviews-2026.pdf` (primary, plus a `.md`
extraction alongside it) and
`raw/studies/arxiv-measuring-google-ai-overviews-2026.md` (the fuller HTML
extraction behind most of the detail below).

**High rigor — one of the most rigorous AIO-composition sources in the wiki.**
Independent academic (not vendor), large-scale longitudinal audit: 55,393
trending queries × 19 categories × 40 days, 7,583 AIOs, 61,212 reference URLs,
98,020 atomic claims verified against the full text of every source the AIO
itself cites. Disclosed methodology, human-validated LLM pipelines (claim
extraction F1 **90.1%**; verifier **95.6%** weighted accuracy against
two-annotator human labels), explicit limitations. Nearly every other AIO source
in this wiki is vendor research; this one is peer-review-track and — uniquely —
**compares AIO citations against the co-displayed first-page SERP as a control
pool**.

## Why it matters

Four findings: three corroborate/sharpen existing wiki claims with independent
academic data, and one (**claim fidelity**) opened a topic the wiki hadn't
covered at all — the *factual accuracy* of what AIOs say about the sources they
cite. The first-page control pool is the methodological contribution no vendor
source here provides.

## Key takeaways

### 1. Activation is 13.7% overall, and format-driven

- **13.7% overall activation** on trending queries — but see the corpus caveat;
  this is a very different query population from the brand-tracking corpora
  behind [[aio-ctr-impact]]'s prevalence numbers.
- **Question-form queries activate at 64.7% vs. 9.5% for non-questions — 6.8×.**
  `how` (84.3%) and `why` (73.4%) top the list; even the weakest interrogative
  (`did`, 39.8%) still runs 4–5× non-question queries.
- **Query length independently amplifies activation**: among non-question
  queries *alone*, 9.9% at one word rising to 38.7% at six or more words. Length
  is not merely a proxy for question phrasing.
- **13× spread by category**: Hobbies & Leisure 46.1% and Science 39.9% highest;
  **Politics 7.5%**, Law & Government 9.6%, and Beauty & Fashion 3.5% lowest.
  The authors flag the political suppression as an undisclosed editorial choice
  — but it is **selective, not blanket: Health is not suppressed (26.6%)**.
- **Activation and claim fidelity are statistically independent (p = 0.192)** —
  a low-AIO category is *not* a safer-answer category.

### 2. AIO sources are more credible than the SERP, and ~30% are off-page

- Median **8 references per AIO**. Top-cited hosts: youtube.com 5.49%,
  en.wikipedia.org 4.39%, facebook.com 3.68%, instagram.com 3.65%, usatoday.com
  2.80%.
- **AIO citation is broad where the SERP is concentrated.** Top-10 hosts take
  **29.7% of AIO citations vs. 49.6% of first-page citations**, and **56.3% of
  AIO-cited hosts were cited exactly once** in 40 days. The citation pool is a
  long tail, not a short list of winners.
- **AIO-cited domains score higher on the PC1 credibility index** — 0.732 vs.
  0.645 for co-displayed first-page results (p≪0.001), significant in **14 of 19
  categories with no significant reversal in any**. The authors state this
  "directly contradicts prior work suggesting that AIOs draw on lower-quality
  sources."
- **UGC: 14.2% of AIO refs vs. 41.4% of first-page URLs** — AIOs cite UGC *less*
  than the first page in all 19 categories. Four platforms (YouTube, Facebook,
  Instagram, Reddit) account for **96.5%** of it.
- **29.8% of AIO-cited domains appear nowhere on the corresponding first page**
  (28.5% at URL level). Domain overlap: **25.0% at top-5, 41.4% at top-10, 70.2%
  across the full first page** — direct evidence that AIO source selection is a
  mechanism *distinct from* Google's ranking algorithm. Crucially, those
  off-page citations are **higher quality, not lower** (PC1 0.758 vs. 0.724; UGC
  3.4% vs. 18.5%).

### 3. 11.0% of AIO claims are unsupported by their cited sources

- Of 98,020 atomic claims, **88.97% Consistent** and **11.03% Inconsistent** —
  **Omitted 6.98%** (no cited source mentions it), **Incorrect 2.66%** (a cited
  source contradicts it), **Ambiguous 1.39%**.
- **Omission outruns active misrepresentation ~2.6:1.** The dominant AIO failure
  is asserting something none of its citations support, not misreading a
  citation.
- **Median AIO is 93.33% grounded; 41.9% are perfectly grounded.** The tail is
  small but real: 2.74% of AIOs have under half their claims grounded, 0.85%
  none.
- **Fidelity is independent of source quality (r ≈ 0.045)** — curating better
  sources doesn't fix it.
- Highest fidelity in the consequential categories — **Health 94.77%, Politics
  93.65%, Science 91.82%** (consistent with stricter YMYL grounding); lowest in
  Autos/Sports/Jobs (~77–82%).
- **Climate's 48.23% is a measurement artifact** (live weather values vs. pages
  re-crawled hours later), not an AIO failure; normalized out, 18 of 19
  categories sit inside an **85.9%–94.8% band**.
- Even under the most generous correction for uncrawlable UGC sources, a **~5.3%
  inconsistency floor** remains. The authors frame unsupported claims as
  "inherent to generative AI at its current state."

### 4. Publishers lose the click while Google keeps the ad

- **50.63% of AIO-cited pages carry visible display ads** — a conservative
  floor, since the 14.2% UGC share is treated as ad-free and social/video refs
  weren't crawled. Highest in Hobbies & Leisure (63.14%), Sports (60.19%),
  Entertainment (55.50%); lowest in Health (27.77%) and Law & Government
  (29.47%).
- **Only 2.16% of AIO-bearing SERPs carry Google sponsored ads, and 0.51% place
  them above the AIO.** The authors' framing: AIOs restructure the page in a way
  that **preserves Google's ad capture while reducing publisher click-throughs**.
- The paper **imports (does not independently measure)** the downstream traffic
  effects: ~38% organic-click reduction and ~33% more zero-click searches
  (Agarwal & Sen 2026), Wikipedia −15% (Khosravi & Yoganarasimhan 2026), and
  case losses (Stereogum −70% ad revenue, The Planet D −90% traffic).

## Relationship to existing wiki claims

- **Conflicts** with [[ai-citation-landscape]]'s "76% of AI Overview citations
  pull from Google's own top-10 organic results" (via
  [[ahrefs-b2b-seo-statistics-2025]]). This study measures 41.4% domain overlap
  at top-10 and 70.2% across the whole first page. Logged as Conflicting
  Evidence on [[ai-citation-landscape]].
- **Extends** [[ai-citation-landscape]]'s AIO sourcing profile with a first-page
  control pool no vendor source in the wiki provides — the relevant comparison
  is not "AIOs cite a lot of UGC" but "AIOs cite *less* UGC and *more* credible
  domains than the organic results sitting directly beneath them."
- **Nuances** [[brightedge-ai-search-same-brands-different-sources]]'s "AI
  Overviews is a UGC-first engine" characterization: same direction relative to
  other engines, but the absolute numbers run lower here (14.2% vs. ~17.5–18%
  UGC; YouTube 5.49% vs. 10.6%), and the first-page control reframes what
  "UGC-first" means.
- **Extends** [[aio-ctr-impact]] on the economics side with the supply-side
  measurement it lacked: what share of the pages feeding AIOs actually depend on
  ad revenue (50.63%+), and how rarely Google's own ads are displaced (2.16% of
  AIO SERPs).
- **Adds a dimension the wiki did not cover at all**: claim fidelity — whether
  an AIO's assertions are actually supported by the sources it credits. Filed to
  [[ai-overview-grounding-and-fidelity]].
- **Corroborates, at different magnitudes**, [[aio-ctr-impact]]'s
  question-format activation finding
  ([[seerinteractive-aio-ctr-impact-2026-update]] reports 85.9%; this reports
  64.7%). Corpus difference, not contradiction — see caveats.

## Rigor caveats / limitations (stated)

- **The query corpus is trending queries, not commercial queries.** Sports alone
  is 51.4% of the corpus and Entertainment 14.9%, so the 13.7% headline
  activation rate is **not comparable** to the brand-keyword and
  commercial-keyword prevalence numbers in [[aio-ctr-impact]]. Per-category
  rates and within-corpus contrasts (question vs. non-question, AIO vs. first
  page) travel; the headline aggregate does not.
- **US desktop, English, 40 days, one snapshot period.**
- **No direct traffic measurement** — publisher-impact click figures are
  imported from other papers, not measured here.
- Claim verification depends on an **LLM verifier (Grok 4.1 Fast Reasoning)**.
  Validated at 95.6% weighted accuracy against two-annotator human labels, with
  errors running generous rather than harsh — but it is still an LLM judging LLM
  output.
- **Social and video platform bodies were not crawled** (auth barriers), which
  inflates measured inconsistency (bounded by the authors at a ~5.3% floor) and
  deflates measured ad prevalence. Paywalled pages partial.
- Ad detection is **visible-ad** detection on crawled pages; affiliate,
  subscription, and lead-gen monetization are invisible to it, so "50.63%
  ad-supported" **understates** commercial dependence on AIO-cited traffic.

## Pages created / updated

- Created [[ai-overview-grounding-and-fidelity]] — the claim-fidelity concept
  (2026-09-10 ingest).
- Updated [[aio-ctr-impact]] — activation/prevalence data point (added to the
  prevalence-debate Conflicting Evidence), publisher-ad/click-loss economics,
  the 2.16%-Google-ads supply-side measurement, and corroboration of the ~38%
  below-no-AIO click figure.
- Updated [[ai-citation-landscape]] — the 29.8%-off-page / top-5/top-10/
  first-page overlap AIO↔SERP-divergence data point (and the Conflicting
  Evidence entry against the Ahrefs 76% claim), the AIO-vs-SERP UGC-suppression
  finding with its first-page control (reconciled against BrightEdge's
  "UGC-first engine" framing), the citation-breadth/long-tail finding, and the
  claim-fidelity section (being cited ≠ being represented accurately).
- Updated [[geo-content-optimization-tactics]] — question-format AIO risk and
  the ~11% unsupported-claim implication for how you're represented.
- Referenced by [[personal-context-signals-in-ai-search]].
