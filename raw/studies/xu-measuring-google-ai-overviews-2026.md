# Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact

Authors: Haofei Xu, Umar Iqbal, Jacob M. Montgomery (Washington University in St. Louis)
arXiv:2605.14021v1 · Published May 13, 2026
Study window: March 13 – April 21, 2026 (40 days)
Source: https://arxiv.org/html/2605.14021v1
PDF: raw/studies/xu-measuring-google-ai-overviews-2026.pdf (authoritative raw)
Captured: 2026-08-06 (WebFetch extraction — see PDF for the full text/appendices)

---

## Abstract (verbatim)

"Google AI Overviews (AIOs) are arguably the most widely encountered
deployment of generative AI, reaching over 2 billion users who may not
realize the answers they see are AI-generated. Where search engines have
traditionally surfaced ranked sources and left users to evaluate them,
AIOs synthesize and deliver a single answer — giving Google unprecedented
editorial control over what users read and know. We present a large-scale
longitudinal measurement study, issuing 55,393 trending queries across 19
topical categories over a 40-day window (March 13–April 21, 2026). We
report four main findings. First, overall AIO activation is 13.7%, rising
to 64.7% for question-form queries, while politically sensitive topics see
markedly lower rates. Second, AIO-cited domains are more credible than
co-displayed first-page results, yet nearly 30% do not appear in those
results at all, indicating a source selection mechanism distinct from
Google's ranking algorithm. Third, decomposing responses into 98,020
atomic claims, 11.0% are unsupported by the cited pages — with omission
the dominant failure mode — and source quality and claim fidelity are
largely independent. Fourth, well over half of AIO-cited pages carry
display advertising, meaning publishers lose revenue when AIOs suppress
the click-through, even as Google's own sponsored ads continue to appear
on the same page. Together, these findings document a rapid transformation
of the online information ecosystem whose consequences for epistemic
security remain poorly understood."

## Methodology

- 55,393 trending queries from US Google Trends (extracted every 24h), 19
  topical categories, 40 days (Mar 13–Apr 21 2026). Puppeteer/Chrome on AWS
  Lambda (us-east-1), stateless profiles, bot-detection mitigation.
- AIO detection via rule-based DOM anchoring; "Show more" expanded; captured
  references (titles, URLs, text fragments) plus all first-page SERP URLs.
- Source scraping: Readability-lxml + BS4; social platforms excluded
  (auth/bot barriers); <1% capture failure; 262 paywalled pages partial.
- Source quality: PC1 domain-credibility score (0–1) from Lin et al. (2023),
  11,520 domains (reuters.com=1.000, nytimes.com=0.859, facebook.com=0.407).
- Claim fidelity: two-stage LLM pipeline (Grok 4.1 Fast Reasoning, temp=0) —
  Stage 1 extract atomic claims, Stage 2 label Clear/Vague/Ambiguous/
  Incorrect/Omitted. Human-validated: extraction F1 90.1% (κ=0.85);
  verification 95.6% weighted accuracy (κ=0.94).
- Ad detection: DOM <iframe> vs EasyList; Google sponsored ads via
  "Sponsored" labels (above/below AIO).

## Findings

### (a) Activation / prevalence
- Overall: 7,583 AIOs / 55,393 queries = **13.7%**.
- Question-form **64.7%** vs non-question **9.5%** (6.8x). Interrogatives:
  does/which/do 100%, can 97.1%, how 84.3%, why 73.4%, what 60.6%, who 47.9%.
- Non-question by length: 1 word 9.9% → 6+ words 38.7%.
- By category (high→low): Hobbies & Leisure 46.1%, Science 39.9%, Health
  26.6%, Business & Finance 26.2%, Food & Drink 24.6%, Technology 18.5% …
  Politics 7.5% (suppressed), Climate 7.4%, Beauty & Fashion 3.5%.
- Daily rate broadly stable; spikes on major events (Oscars, NCAA, Artemis II).

### (b) Source quality
- AIO-cited domains PC1 **0.732** vs first-page **0.645** (+0.087, p≪0.001).
  Positive in nearly every category (Autos slightly negative, non-sig).
- 7,583 AIOs cited 61,212 reference URLs / 7,479 unique hosts; median 8 refs.
- Top-cited: youtube.com 5.49%, en.wikipedia.org 4.39%, facebook.com 3.68%,
  instagram.com 3.65%, usatoday.com 2.80%. AIO citations less concentrated
  than SERP (top-10: 29.7% vs 49.6%).
- Overlap with first page: 25.0% at top-5, 41.4% at top-10, **70.2% across
  full first page → 29.8% of AIO domains are "off-page"** (28.5% at URL level).
  Off-page refs are *higher* quality (PC1 0.758, UGC 3.4%) than on-page
  (0.724, UGC 18.5%).
- **UGC share: AIO 14.2% vs first-page 41.4%** (−27.25pp, p<0.001). UGC =
  FB/IG/LinkedIn/Pinterest/Reddit/Threads/TikTok/X/YouTube (excl. Wikipedia).

### (c) Claim fidelity (98,020 claims / 7,491 verifiable AIOs)
- Clear 84.61%, Vague 4.36% → **Consistent 89.0%**; Omitted 7.0%, Incorrect
  2.66%, Ambiguous 1.39% → **Inconsistent 11.0%**. Omitted:Incorrect ≈ 2.6:1.
- AIO-level: median consistency 93.33%; 41.9% perfectly grounded; 61.8% ≥90%;
  2.74% <50%; 0.85% zero consistent claims.
- By category: Health 94.77% (highest), Politics 93.65%, Science 91.82% …
  Sports 81.85%, Autos 80.65%, Jobs & Education 76.85%; Climate 48.23%
  (real-time-data pipeline artifact). Non-artifact range ~85.9–94.8%.
- Claim fidelity ~independent of activation (r≈0.313, p=0.192) and of source
  quality (r≈0.045).
- 59.9% of inconsistent claims come from AIOs citing ≥1 (uncrawled) UGC
  source; most-generous residual inconsistency floor ≈5.3%.

### (d) Publisher impact
- **50.63%** of AIO-cited pages (30,994 / 61,212) carry visible display ads
  (conservative lower bound; social/video refs uncrawled). By category:
  Hobbies & Leisure 63.14%, Sports 60.19%, Food & Drink 57.93% … Health
  27.77%, Travel 27.24%, Autos 28.49%.
- Google's own sponsored ads on AIO-bearing SERPs: 2.16% carry ≥1; 0.51%
  above the AIO; none inside the AIO container.
- Cited external research (not this paper's own measurement): AIOs reduce
  organic clicks ~**38%** and raise zero-click ~**33%** (Agarwal & Sen 2026);
  Wikipedia traffic −~**15%** (Khosravi & Yoganarasimhan 2026); DCN survey
  median YoY Google referral −10% (2025); Stereogum −70% ad revenue; The
  Planet D −90% traffic.

## Conclusions / recommendations
- Genuine quality investment (more credible sources, UGC suppression, highest
  fidelity in YMYL categories Health/Politics/Science) — but hallucination is
  inherent (11% floor ~5.3% even generously); better sources ≠ better fidelity.
- Opaque triggering (politics suppression undisclosed; question-form 6.8x).
- Source selection distinct from ranking (29.8% off-page).
- Economic asymmetry: publisher clicks suppressed while Google ad inventory
  intact; feedback-loop risk to content-quality incentives.
- Recommends: drive down unsupported-claim rate, limit high-consequence
  deployment, revenue-sharing/licensing, more citation prominence/click
  facilitation, transparent activation policies + per-category targets,
  audit-ready APIs.

## Limitations (stated)
- No direct traffic-loss measurement (inferred from cited literature).
- Social-platform content excluded → UGC-supported claims possibly
  undercounted as unsupported. Real-time-data pipeline artifacts (Climate).
  Paywalled content partial.
