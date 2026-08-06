---
type: source
tags: [seo, aeo]
date_published: 2026-05-13
date_ingested: 2026-08-06
origin: raw/studies/xu-measuring-google-ai-overviews-2026.pdf
---

# Xu, Iqbal & Montgomery — Measuring Google AI Overviews (arXiv 2026)

**Citation:** Haofei Xu, Umar Iqbal, Jacob M. Montgomery (Washington
University in St. Louis), "Measuring Google AI Overviews: Activation,
Source Quality, Claim Fidelity, and Publisher Impact." arXiv:2605.14021v1,
May 13 2026. Study window Mar 13–Apr 21 2026.
https://arxiv.org/html/2605.14021v1 · Ingested 2026-08-06.

**High rigor.** Independent academic (not vendor), large-scale
longitudinal audit: 55,393 trending queries × 19 categories × 40 days,
7,583 AIOs, 61,212 reference URLs, 98,020 atomic claims. Disclosed
methodology, human-validated LLM pipelines (extraction F1 90.1%,
verification 95.6% accuracy), explicit limitations. One of the most
rigorous AIO-composition sources in the wiki.

## Why it matters

Four findings, three of which corroborate/sharpen existing wiki claims
with independent academic data, and one (**claim fidelity**) opening a
topic the wiki hadn't covered at all — the *factual accuracy* of what
AIOs say about the sources they cite.

## Key takeaways

**1. Activation is 13.7% overall, format-driven.** Question-form queries
trigger AIOs **64.7%** of the time vs **9.5%** for non-questions (6.8×);
longer non-question queries trigger more (1 word 9.9% → 6+ words 38.7%).
By category: Hobbies & Leisure 46.1% and Science 39.9% highest; **Politics
7.5%** and Beauty & Fashion 3.5% lowest — the authors flag the political
suppression as an undisclosed editorial choice. (Sampling frame: *trending*
Google Trends queries, which skew toward news/entertainment and differ
from keyword-panel samples — see the prevalence caveat on [[aio-ctr-impact]].)

**2. AIO sources are more credible than the SERP, and ~30% are off-page.**
AIO-cited domains score higher on the PC1 credibility index (0.732 vs
0.645 for co-displayed first-page results, p≪0.001) and carry far less
UGC (14.2% vs 41.4% of first-page results). **29.8% of AIO-cited domains
don't appear on the query's first page at all** (70.2% overlap across the
full first page; 41.4% at top-10; 25.0% at top-5) — direct evidence that
AIO source selection is a mechanism *distinct from* Google's ranking
algorithm. Off-page refs are even higher-quality/lower-UGC than on-page.
Top-cited domains: youtube.com 5.49%, en.wikipedia.org 4.39%, facebook.com
3.68%, instagram.com 3.65%, usatoday.com 2.80%.

**3. 11.0% of AIO claims are unsupported by their cited sources.** Of
98,020 atomic claims, 89.0% were Consistent (Clear/Vague) and **11.0%
Inconsistent** — dominated by **omission (7.0%)**, then Incorrect (2.66%)
and Ambiguous (1.39%); omission outweighs contradiction ~2.6:1. Fidelity
is **independent of source quality** (r≈0.045) — curating better sources
doesn't fix it. Highest fidelity in YMYL categories (Health 94.8%,
Politics 93.7%, Science 91.8%); lowest in Autos/Sports/Jobs (~77–82%).
Even under the most generous assumption (all UGC-sourced claims counted
supported), a ~5.3% residual inconsistency floor remains. Authors frame
unsupported claims as "inherent to generative AI at its current state."

**4. Publishers lose the click while Google keeps the ad.** **50.63%** of
AIO-cited pages carry visible display ads (a conservative lower bound —
social/video refs weren't crawled), so AIO click-suppression directly
cuts publisher ad revenue, while Google's own sponsored ads persist on
the same SERP. The paper imports (doesn't independently measure) the
downstream traffic effects: ~38% organic-click reduction and ~33% more
zero-click searches (Agarwal & Sen 2026), Wikipedia −15% (Khosravi &
Yoganarasimhan 2026), and case losses (Stereogum −70% ad revenue, The
Planet D −90% traffic).

## Rigor caveats / limitations (stated)

- Trending-query sampling frame (not a general keyword panel) — prevalence
  figures aren't directly comparable to Semrush/Seer keyword-set studies.
- No direct traffic measurement — publisher-impact click figures are
  imported from other papers, not measured here.
- Social/video platform content excluded from scraping (auth barriers), so
  UGC-supported claims may be *undercounted as unsupported* (hence the
  5.3% generous floor). Real-time-data queries (weather/forecasts) create
  a fidelity pipeline artifact (Climate 48.2%). Paywalled pages partial.

## Pages created / updated

- Updated [[aio-ctr-impact]] — activation/prevalence data point (added to
  the prevalence-debate Conflicting Evidence), publisher-ad/click-loss
  economics, and the corroboration of the ~38% below-no-AIO click figure.
- Updated [[ai-citation-landscape]] — the 29.8%-off-page / top-10-overlap
  AIO↔SERP-divergence data point, the AIO-vs-SERP UGC-suppression finding
  (with a reconciliation against BrightEdge's "UGC-first engine" framing),
  and a **new section on claim fidelity** (being cited ≠ being represented
  accurately).
