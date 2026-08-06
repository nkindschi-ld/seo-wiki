---
type: playbook
tags: [aeo, seo]
updated: 2026-08-03
---

# Competitor Citation Displacement

**Why / when to use this:** use when a competitor is being named/cited by AI
engines (ChatGPT, Perplexity, Google AI Overviews) for your commercially important
queries and you are not — and you want to know *why* at the artifact level, then
systematically displace them. This is the **competitor-facing** counterpart to
[[ai-entity-footprint-audit]] (which diagnoses how well AI understands *your own*
brand). Based on [[derivatex-competitor-citation-steal-prompt-2026]] (DerivateX /
Apoorv Sharma), an original tactical framework; the underlying build tactics it
invokes live in [[geo-content-optimization-tactics]] and [[brand-entity-seo-strategy]].

## The core distinction: gap vs. root cause

Standard AI-visibility tools show *that* a competitor is cited and you aren't — a
**citation gap** ("they appear in ChatGPT; I don't"). They rarely show the **citation
root cause** ("they appear because they own a proprietary benchmark, a category
definition, or a Reddit presence I lack"). Displacement work targets the root cause,
not the gap. The premise — that this can happen even when you outrank the competitor
on Google — is the same "two separate discovery layers" finding measured in
[[derivatex-two-googles-one-query-aio-vs-serp-2026]]: "a company can rank first on
Google and be absent from every AI recommendation in its category simultaneously."

## The seven-step method

Executable inside any LLM with web browsing (the source packages it as one copy-paste
prompt; the steps matter more than the exact wording):

1. **Citation Mapping.** Pick ~10 buyer-intent queries. For each, record which
   competitors the engine cites, at what position, and — critically — the *exact
   mechanism* it's citing. Force specificity: not "they have good content" but "they
   own the benchmark page," "a comparison table," "a Reddit thread," "the category
   definition." Then note whether you appear and, if not, what artifact they have
   that you don't. (The source's prompt returns this as a fixed-column table.)
2. **Gap Autopsy.** For each miss, diagnose four things: the specific **artifact**,
   the **entity relationship** being asserted, the **language pattern** the engine
   reused, and the **fastest build path** to your own version.
3. **Steal Matrix.** Rank every gap by **citation value ÷ steal difficulty** and work
   the highest-ratio targets first — the same "concentrate effort where it moves
   citations, don't spread thin" logic as [[geo-content-optimization-tactics]]'s
   third-party-authority guidance, applied to competitive displacement.
4. **Artifact Blueprints.** For your top ~3 targets, spec: the URL slug, the *target
   citation sentence* you want the engine to lift, the content structure, the
   **proprietary data point** the artifact must contain, and the off-site seeding
   targets. This operationalizes the wiki's "publish citation-ready primary
   research/benchmarks" tactic — see that section in
   [[geo-content-optimization-tactics]] (frame as a comparison, lead with the result,
   put it in the first 30% of the page).
5. **Entity Line Standardization.** Write one consistent brand definition and use it
   verbatim across every surface (homepage, G2, Reddit, guest posts) so engines
   assemble a single coherent entity. This is the [[brand-entity-seo-strategy]]
   semantic-triple/consistent-definition step and the "consistency" dimension of
   [[ai-entity-footprint-audit]], scoped to the specific claims competitors currently
   own.
6. **30-Day Steal Calendar.** Sequence the build + off-site seeding week by week. The
   source's framing: "an artifact without seeding is a page that exists; an artifact
   with seeding is a citation source" — i.e. publishing the artifact is necessary but
   not sufficient; earned third-party placement is what converts it into a cited
   source (consistent with the wiki's third-party-authority findings).
7. **Weekly Diagnostic.** Re-run a tracking prompt every week to watch citation
   position move on the targeted queries — a lightweight version of the measurement
   cadence in [[ai-visibility-measurement-methodology]].

## What actually earns the steal (grounding, with provenance flags)

The framework leans on tactics the wiki already validates from primary sources — use
these as the "how," and treat the framework as the diagnostic wrapper around them:

- **Own an extractable artifact** (benchmark, comparison table, category definition)
  with a proprietary data point. ChatGPT retrieves far more than it cites (AirOps:
  ~100 retrieved, ~15 cited), favoring data-table/short-sentence structure — see
  [[airops-fan-out-effect-2026]].
- **Put the target citation sentence high on the page.** Content in the first third
  is cited disproportionately (the source cites SE Land "~2x"; the wiki's
  better-sourced figure is 44.2% of citations from the first 30% — see
  [[geo-content-optimization-tactics]]).
- **Build off-site presence, especially community.** Reddit/Quora presence correlates
  with materially higher citation likelihood (source cites SE Ranking "~4x"; the
  wiki's disclosed-methodology figure is Otterly's 9x engagement multiplier — see
  [[otterly-reddit-geo-ai-search-citations-2026]]).
- **Distribute across multiple publications, not one domain.** *New to the wiki but
  cited secondhand:* the source attributes "up to **325%** more AI citations" from
  multi-publication distribution vs. single-domain publishing (Stacker, late 2025) —
  directionally consistent with the wiki's "seed presence across many high-signal
  channels" guidance, but treat the 325% figure as unverified pending a primary
  source.
- **Listicles dominate commercial queries; definition pages with proprietary data
  earn the most citations** (Wix) — see [[listicles-in-ai-search]] and
  [[wix-generative-engine-optimization]].

## Caveats

- **This is a vendor framework, not a study.** The seven-step process and steal-matrix
  are original DerivateX tactical guidance; they're sound because they operationalize
  independently-validated tactics, not because the framework itself was tested.
- **Case-study numbers are vendor claims with no disclosed methodology** — REsimpli
  ("zero to top-cited across 10+ prompts in 90 days") and Gumlet ("20% of inbound
  revenue attributed to ChatGPT/Perplexity discovery"). Cite as illustration of
  ambition, not as evidence of a reliable effect size.
- **Displacement is competitive and can be a zero-sum race.** Per [[c-seo-bench-2025]],
  content tactics erode toward zero as competitors adopt the same ones — an early
  displacement win may not persist once the target notices and rebuilds.

## Checklist

- [ ] Mapped 10 buyer-intent queries: who's cited, position, and *exact artifact*.
- [ ] Autopsied each miss to a root cause (artifact / entity / language), not just a gap.
- [ ] Ranked targets by citation value ÷ steal difficulty; picked the top ~3.
- [ ] Blueprinted each: slug, target citation sentence, proprietary data point, seeding.
- [ ] Standardized one brand definition across all surfaces.
- [ ] Sequenced a 30-day build + off-site seeding calendar.
- [ ] Set a weekly citation-position tracking prompt.
