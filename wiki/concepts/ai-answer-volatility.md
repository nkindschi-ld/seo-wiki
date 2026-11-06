---
type: concept
tags: [aeo]
updated: 2026-11-02
---

# AI Answer Volatility

How much AI answers for the same prompt change from run to run and day
to day, and what that means for measuring AI visibility. Primary
source: [[detailed-ai-volatility-2026]] (28 days, 1,300+ commercial
prompts, ChatGPT and Google AI Overviews, 70k+ responses).

## Current best understanding

- **The answer is volatile; the leaders are not.** Identical brand
  lists across two random days are near-zero (0.3% ChatGPT, 1.1% AIO),
  yet the most-named brand per prompt shows up on 82–89% of days.
- **Core vs. tail.** Think of each prompt's answer as a small stable
  core (brands present ≥80% of days, churning ~11–13% day to day) plus
  a large rotating tail (65–78% churn). Many prompts have no core at
  all — about half in ChatGPT.
- **Presence > position.** Being named or cited is far more stable than
  being named or cited *first*. The leading domain appears on most days
  but leads the citation list on under half of them (43% ChatGPT, 28%
  AIO).
- **Leadership is contestable.** The gap between #1 and #2 is usually
  ~2 days in 28, and the leader flips between fortnights on about half
  of prompts — small changes could plausibly swap them.
- **Engines differ.** AI Overviews are more stable than ChatGPT on most
  brand measures and on URL re-citation (~50% vs ~25% next day), but
  less stable on exact cited-domain sets (0.3% vs 2.4%).
- **Content-type mix is stable even when URLs churn.** Articles ≈60% of
  citations on both engines; a specific URL being cited is a weak signal,
  the *type* of page cited is a strong one. Ties into
  [[listicles-in-ai-search]] and the source-type mix on
  [[ai-citation-landscape]].
- **Mixes still drift over weeks.** AIO video citations fell from ~14%
  to ~8% within the 28 days, so a source-mix snapshot can go stale fast.

## Measurement implications

- Don't report single-run screenshots or exact-match rank as AI
  visibility.
- Track **presence rate** and **share of voice** over a rolling window
  (weeks, not a day), per engine. This complements the presence /
  portability / concentration split on [[ai-citation-landscape]].
- Classify brands per prompt as core / tail / absent; moving from tail
  to core is the meaningful win.
- Treat position-1 changes as noise unless they persist.
- A 14-day window predicted the next 14 days' leader reasonably well
  (79–85% presence), which suggests two weeks as a usable minimum
  baseline. This is an inference from one study, not a tested rule.

Applied in [[ai-visibility-content-gap-audit]] and [[seo-reporting]].
Related: [[generative-engine-optimization]],
[[ai-coding-agent-tool-selection]] (category-level stability of agent
picks).

## Conflicting Evidence

None yet. Only one dedicated volatility study in the wiki; the video
share figure (~8–14% of AIO citations) is a different metric and period
from the single-video-platform 10.6% on [[ai-citation-landscape]], so
it is noted, not treated as a conflict.
