# The AI Mention Effect

**Author:** Nikolas Laskaris, AI Strategist
**Publication:** Profound Blog (Data & Research)
**Published:** 2026-07-01
**URL:** https://www.tryprofound.com/blog/the-ai-mention-effect

---

## Summary (extracted via WebFetch, 2026-07-22)

### Primary finding

Following an AI assistant's brand mention, users visit that brand's
website at **1.5–2.5x their forecasted baseline rate over 7 days**.

### Platform-specific results

| Platform | Treated Rate | Baseline | Lift |
|---|---|---|---|
| Gemini | 5.42% | 2.21% | +3.21pp (+145% relative) |
| Google AI Overviews | 7.79% | 4.83% | +2.96pp (+61% relative) |
| ChatGPT | 6.39% | 4.33% | +2.07pp (+48% relative) |

Gemini shows the largest relative increase (~2.5x baseline); Google AI
Overviews has the largest absolute lift and exposure volume.

### Industry variation

- Financial Services via Gemini: +5.7pp (+132%)
- Retail via Gemini: +5.6pp (+140%)
- Software via Google AI Overviews: +4.0pp (+128%)

### Timing distribution

- 20.5% of first visits occur within 1 hour
- 42% occur within 24 hours
- Majority of visits extend beyond day one
- Google AI Overviews is fastest (45.7% within 24 hours)

### Attribution gap

Even after ChatGPT's May 2026 update made links more clickable, only
~2.5% of downstream visits carried trackable AI-referral parameters.
Over 97% of post-mention brand visits lack UTM tags.

- Before 2026-05-07 (ChatGPT update): +2.00pp lift
- After 2026-05-07: +2.16pp lift (moderate improvement)

### Methodology

- **Data source**: double-opt-in privacy panel of US users with AI
  interaction and browsing data
- **Sample size**: 2M+ AI conversations, January–June 2026
- **Platforms**: ChatGPT, Gemini, Google AI Overviews
- **Key definition**: "AI-exposures" are brand mentions appearing in AI
  responses but *not* in the user's own prompt — isolating genuine
  brand discovery from pre-existing interest.
- **Analysis method**: forecasted backward-placebo design, comparing
  7-day post-exposure visit rates against three prior 7-day placebo
  windows to establish a baseline expectation.
- **Filters**: removes users with prior-week brand searches/visits;
  excludes common-platform and generic high-traffic domains;
  confidence intervals via user-clustered bootstrap (2,000 replicates).

### Caveats (stated by the authors)

Site-visit study, not a purchase/conversion study. Not a randomized
experiment — the methodology controls for individual user baselines but
doesn't fully eliminate selection bias between exposed and non-exposed
populations.
