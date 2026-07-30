---
type: concept
tags: [aeo, geo]
updated: 2026-07-30
---

# Topical Authority in AI Search

How brand *ownership of a topic* behaves inside AI answer engines: how
concentrated or contested topics are, which topics are winnable, and how
stable a lead is once earned. Distinct from
[[ai-visibility-correlation-factors]] (which brand/SEO metrics correlate
with being mentioned *at all*) and [[ai-citation-landscape]] (which
source domains/media get cited) — this page is about *who owns a topic
and how durably*.

Primary source: [[semrush-chatgpt-topic-authority-study]] (Semrush ×
Kevin Indig / Growth Memo, 1,094 US categories, ChatGPT, Jan–Jun 2026;
220K+ domains, 600K+ citations). A "category" = a topical cluster of
five representative prompts (definition, comparison, alternatives, use
case, purchase); ownership is measured on **brand mention share** across
those five prompts.

## Ownership is the exception, not the rule

Across 1,094 categories:

| State | Share | Definition |
|---|---|---|
| Clear owner | 15.2% | Leads mention share in ≥4 of 5 prompts, with a ≥5-point margin over the runner-up |
| Emerging leader | 31.2% | Tops ≥3 prompts but misses the owner threshold |
| Unsettled | 53.7% | No brand appears in ≥3 prompts |

The strategic reading: **most topics are still up for grabs.** More than
half have no consistent brand answer, and only ~1 in 7 is locked down.
This is the ChatGPT-topic-level analogue of the brand-level "visibility
cliff" in [[ai-visibility-correlation-factors]] (26% of 75K brands had
zero AI Overview mentions) and the frontier-concept land-grab framing in
[[generative-engine-optimization]] / [[vercel-adapting-seo-for-llms]].

**The recognition–mention gap (independent corroboration, 2026-07-30):**
per [[victorious-q2-2026-quarterly-search-report]] (175 brands, 8
platforms), **96%** of brands were *described accurately* by AI but
**89%** never *appeared* in answers to category-research questions.
Recognition (the model knows who you are) is near-universal; ownership /
mention of your category is rare. This is the same "known but not
recommended" phenomenon on a different, cross-platform dataset — and the
core problem behind [[launchdarkly-ai-visibility-devrel-brief]]. Victorious
also found brands with **<2,000 indexed pages mentioning them** were named
just **3%** of the time, and that brand naming rises **>12x** from
problem-awareness to category-research prompts — mentionability is earned
off-site and concentrated down-funnel.

## The inverse-demand paradox

Higher search volume normally means stronger competition. In ChatGPT the
study found the opposite: only **11.3%** of high-demand topics had clear
owners vs. **19%** of lower-demand topics. High-visibility topics attract
more candidate brands, fragmenting mention share; lower-demand niches are
easier to own outright. Practical implication (see
[[geo-content-optimization-tactics]]): a challenger is often better off
owning a specific lower-demand subtopic than contesting the head term —
consistent with AirOps' "focus beats comprehensive coverage" finding in
[[airops-fan-out-effect-2026]] and the 2–3-category concentration advice
below.

## Leadership is sticky once earned (the 5-point moat)

Once a brand becomes a clear owner, the position is durable: owners held
#1 in **90.4%** of month-over-month comparisons. The margin is what
matters —

- Topics where the leader **held**: median lead **2.9 points**.
- Topics where the leader **flipped**: median lead **1.3 points**.

So roughly a **5-percentage-point mention-share margin** is the
stability threshold; narrower leads churn month to month. This makes
early topic ownership a compounding, defensible asset — reaching the
moat first is worth more than incremental gains once contested. Contrast
with the broader-web volatility figures (40–60% month-to-month
citation-source churn in
[[sel-what-is-generative-engine-optimization-geo-2026]]): *source*
citations churn a lot, but an established *brand owner* of a topic is
comparatively stable.

## Mentions vs. citations are decoupled

Only **21%** of the most-cited *domains* in a category were also the
most-mentioned *brand*, and the two correlate **slightly negatively
(-0.229)**. Being the source ChatGPT quotes and being the brand ChatGPT
recommends are largely different games. This corroborates the
citation-vs-recommendation split tracked in [[ai-citation-landscape]]
and [[listicles-in-ai-search]] (Google AIO's 69% citation-without-
recommendation rate in [[sej-why-calling-yourself-the-best-2026]]), and
matters because — per Kevin Indig's *earlier* Growth Memo research —
**74% of users chose the top-*mentioned* brand as their final pick**.
Mention share, not citation share, is the lever closest to selection
(see [[ai-shortlist-effect]] for the selection-stage data).

## SEO metrics don't predict topic winners

Comparing owners against runners-up, traditional domain-level signals
were near coin-flips: owners had higher branded search volume in only
**55.7%** of pairs, higher organic traffic in **48.4%**, higher
Authority Score in **52.5%**. Only branded search volume was
statistically significant, and modestly. See
[[ai-visibility-correlation-factors]] for how this fits (and refines)
the wiki's unresolved authority-vs-AI-visibility conflict — including the
notable wrinkle that Kevin Indig co-authored *both* this study (Authority
Score not a significant differentiator of topic ownership) and the Growth
Memo study that found Authority Score the strongest AI-mention correlate
(0.65 Pearson); they measure different things (topic ownership vs.
brand-level mention presence) and don't actually contradict.

## What to do about it

See [[geo-content-optimization-tactics]] and
[[growth-memo-topics-matter-for-third-party-authority]]. In short:
compete at the **topical-cluster** level, not per prompt; pick **2–3
categories where you already have signal** rather than spreading thin;
prefer winnable lower-demand subtopics over contested head terms; and
push for a ≥5-point mention-share margin to reach the durable-owner moat.

## See also

- [[ai-visibility-correlation-factors]] — brand-level metric correlates
  with being mentioned at all; carries the Authority Score conflict.
- [[ai-citation-landscape]] — the citation-vs-mention decoupling in
  detail.
- [[ai-shortlist-effect]] — the downstream mention-share → purchase-
  selection link (0.57 correlation).
- [[growth-memo-topics-matter-for-third-party-authority]] — Kevin Indig's
  companion topic-authority work (topic-specific source trust, tiered
  authority accumulation).
- [[airops-fan-out-effect-2026]] — "focus beats comprehensive coverage,"
  the page-level analogue of the inverse-demand paradox.
- [[victorious-q2-2026-quarterly-search-report]] — the recognition-vs-
  mention gap (96% described / 89% never mentioned) and off-site
  correlates across 8 platforms and 5 verticals.
- [[launchdarkly-ai-visibility-devrel-brief]] — the "known but rejected"
  problem this study quantifies, applied to LaunchDarkly.
