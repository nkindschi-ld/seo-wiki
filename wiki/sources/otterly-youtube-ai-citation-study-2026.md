---
type: source
tags: [seo, aeo]
date_published: 2026-03-02
date_ingested: 2026-07-23
origin: raw/articles/otterly-youtube-ai-citation-study-2026.md
---

# The YouTube Citation Study 2026 (Otterly.ai)

**Citation:** Rick Tousseyn. "The YouTube Citation Study 2026." Otterly.ai
Blog, 2026-03-02. https://otterly.ai/blog/youtube-ai-citation-study-2026/

## What this source is

A large-scale, disclosed-methodology study of YouTube-specific AI
citation behavior: **100+ million AI citation instances** over a 30-day
window, across six engines (ChatGPT, Google AI Overviews, Google AI
Mode, Perplexity, Microsoft Copilot, Gemini). Same author/methodology
family as [[otterly-url-ai-citations-study-2026]] and
[[otterly-linkedin-ai-citations-study-2026]], narrowed to YouTube.
Scope limitation the source itself flags: it studies **already-cited**
videos, so it's strongest for explaining repeated-citation behavior, not
initial eligibility for being cited at all.

## Key findings

- **YouTube is the 2nd-biggest social-media citation source**: YouTube
  and Reddit together make up 78.2% of AI citations on social media.
  Within the 5.54% of total AI citations coming from social platforms,
  the ranking is Reddit 46.4%, YouTube 31.8%, LinkedIn 13%, Facebook 5%,
  Instagram 2.2%.
- **Sharp platform divergence in how much each engine relies on
  YouTube**: Perplexity 38.7% of its citations are YouTube, Google AI
  Overviews 36.6%, Google AI Mode 19.6%, ChatGPT only 4.4%, Copilot
  0.5%, Gemini 0.2%.
- **Long-form dominates overwhelmingly**: 94% of AI citations go to
  long-form YouTube videos, only 5.7% to Shorts.
- **Timestamps are a Google-only citation mechanism**: timestamped
  citations appear exclusively within Google AI Overviews (73%) and
  Google AI Mode (27%) — zero instances in ChatGPT, Gemini, Copilot, or
  Perplexity. Only 31% of cited videos have timestamp signals at all,
  but 78% of those are cited repeatedly across 2-5 different chapters —
  multiplying one video's citation surface area.
- **Cited videos cluster in the 10-20 minute range** (32.1% of
  citations, the largest bucket); median cited-video duration is under 8
  minutes.
- **Popularity signals don't predict citation**: view count (r = -0.03),
  likes (r = -0.02), subscriber count (r = -0.03), channel total views
  (r = -0.03), and video duration (r = 0.02) are all effectively
  uncorrelated with citation frequency. 40.83% of cited videos have
  under 1,000 views; 35% come from channels with under 10k subscribers.
- **Weak positive correlates**: description length (r = 0.31),
  description hashtags (r = 0.20), recency (~0.3). Average cited-video
  description runs 334 words; average title 19 words.

## Relationship to existing wiki claims

- **Sharpens and partly conflicts with an existing per-provider YouTube
  figure**: [[ai-citation-landscape]]'s "Wikipedia, Reddit, and YouTube
  diverge sharply by provider" section (via
  [[muckrack-generative-pulse-ai-reading-may-2026]]) states YouTube is
  "~2% of citations for both ChatGPT and Gemini." This study's ChatGPT
  figure (4.4%) is the same order of magnitude, but its Gemini figure
  (0.2%) is an order of magnitude *lower* — the opposite direction from
  "roughly on par with ChatGPT." See [[ai-citation-landscape]] for the
  updated section and a flagged, unresolved discrepancy on the Gemini
  number specifically.
- **Consistent with the wiki's broader "engagement doesn't predict
  citation" pattern**: the null correlations for views/likes/subscribers
  echo [[otterly-linkedin-ai-citations-study-2026]]'s near-zero
  engagement correlations on LinkedIn and
  [[airops-fan-out-effect-2026]]'s finding that domain authority doesn't
  positively predict ChatGPT citation. Same underlying claim
  (popularity/authority signals aren't what gets content cited;
  structure/relevance is), now shown on a third platform.
- **Adds nuance to the existing "publishing YouTube content shows no
  citation lift" finding**: [[otterly-ai-keyword-research-2026]] found
  no measurable citation lift from *publishing* YouTube content at the
  page level. This study is consistent with that — since channel size
  and view count don't predict citation either, the lever isn't "publish
  more/bigger," it's video structure (long-form, timestamped chapters,
  well-written descriptions).
- **New to this wiki**: the Google-exclusive timestamp/chapter citation
  mechanism, and the sharp long-form-vs-Shorts citation gap (94% vs.
  5.7%).

## See also

- [[ai-citation-landscape]] — updated YouTube-by-provider section and
  the flagged Gemini discrepancy.
- [[geo-content-optimization-tactics]] — new YouTube-specific tactics
  (long-form, chapters/timestamps for Google surfaces, description
  optimization) added from this source.
- [[otterly-url-ai-citations-study-2026]] and
  [[otterly-linkedin-ai-citations-study-2026]] — companion studies from
  the same author/methodology family.
- [[otterly-ai-keyword-research-2026]] — the earlier "no citation lift
  from publishing YouTube content" finding this study adds structural
  nuance to.
- [[ai-visibility-correlation-factors]] — the brand-level (not
  page-level) YouTube-mentions correlation (~0.737), a different
  question from this study's page-level citation-structure findings.
