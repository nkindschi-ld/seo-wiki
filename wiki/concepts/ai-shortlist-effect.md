---
type: concept
tags: [aeo]
updated: 2026-07-22
---

# The AI Shortlist Effect

How ChatGPT-mediated purchase decisions actually happen once a user is
comparing options *inside* the chat itself — the terminal step beyond
[[ai-citation-landscape]] (what sources get cited) and [[aio-ctr-impact]]
(click economics once a user leaves to the open web). This page covers
what happens when the user never leaves the chat at all and a decision
gets made on the spot. Based on
[[tryprofound-shortlist-is-the-new-shelf]] — a 56-participant,
221-task session study (video screen recording + think-aloud protocol)
combined with a 6,882-citation ChatGPT share-of-voice analysis across 36
representative purchase-decision queries.

## Visibility functions like retail shelf space

Chosen brands appeared roughly **twice as often** in ChatGPT's answers
(24% share of voice) as rejected brands (11%), with an overall
visibility-to-selection correlation of **0.57**. The source's framing:
"inside ChatGPT, share of voice is shelf space" — being surfaced
prominently and repeatedly in an AI answer functions like favorable
retail shelf placement, directly shaping which option gets picked. This
is a genuinely new data type for this wiki: [[ai-visibility-correlation-factors]]
measures what correlates with a brand *appearing* in AI answers at all;
this source measures the next stage — what correlates with an
already-appearing brand actually being *chosen*.

## Correlation strength is sharply category-dependent, not universal

| Category | Correlation | Brands / picks |
|---|---|---|
| Grocery | 0.97 | 5 brands, 17 picks |
| Pet insurance | 0.87 | 10 brands, 54 picks |
| Budgeting | 0.76 | 7 brands, 45 picks |
| Nutrition apps | 0.57 | 7 brands, 25 picks |
| Travel insurance | 0.26 | 6 brands, 19 picks |
| Meal delivery | 0.13 | 10 brands, 34 picks |
| Fitness trackers | 0.00 | 3 brands, 7 picks |
| Fitness apps | -0.44 | 5 brands, 12 picks |
| Coaching | -0.98 | 6 brands, 16 picks |

Visibility-driven selection ranges from near-deterministic (grocery,
0.97) to fully reversed (coaching, -0.98 — the *most*-visible option was
*least* likely to be chosen). Practical implication: "more visible = more
chosen" doesn't hold universally — commoditized, low-personalization
categories (grocery, pet insurance) reward visibility almost directly,
while highly personal/trust-driven categories (coaching) may actively
punish generic high-visibility options in favor of a more individually-
matched pick. Categories under 5 brands (fitness trackers, fitness apps)
are flagged by the source's own authors as directional only, not
reliable.

## Most purchase-decision tasks never leave the chat

- **92.8%** of tasks concluded with no meaningful click to an external
  website.
- **48.9%** of tasks ended with the user accepting ChatGPT's
  recommendation with no follow-up at all.
- **38.8%** involved the user asking ChatGPT to justify or expand on
  its recommendation — more chat, not a web click.
- Only **3.2%** of tasks involved the user verifying information on the
  open web.
- **65.4%** of tasks involved scanning rather than close reading; mean
  task duration was 236 seconds.

This is a sharper, task-level confirmation of [[ai-traffic-scale-vs-hype]]'s
and [[aio-ctr-impact]]'s zero-click theme — here measured as the actual
terminal step of a purchase decision, not an aggregate impression-to-
click ratio.

## Users trust the answer and almost never verify it

- **81.9%** of participants reported increased confidence in their
  decision after using ChatGPT.
- **91.1%** rated ChatGPT's information 4-5 out of 5 for reliability.

Combined with the 92.8%/3.2% figures above, this means incorrect or
outdated information in a ChatGPT recommendation is very unlikely to be
challenged or caught by the user in the moment. This creates direct
accountability pressure: a wrong or stale claim about a brand is far
more likely to go unchallenged than corrected, making accuracy of
AI-surfaced information (pricing, features, positioning) a live
reputational risk, not just a visibility opportunity.

## Comparison grids are the real decision surface

Product/brand comparison grids held user attention longest — **35.9%**
of tasks — and feature-comparison grids specifically drove **15% more**
attention than prose-based answers. Participant quotes: "These tables
are epic"; "This table format makes it easier to scan through the
differences quickly"; "I love that it's telling me right off the
biggest downside of each." The source's framing: "getting lifted into
that table is the AEO equivalent of owning a featured snippet," and
"your row is your shelf placement."

## Four framing levers control outcomes, independent of raw visibility

1. **Appearing in the comparison grid at all** — the single largest
   lever; a brand mentioned only in prose, not lifted into the grid,
   competes on much worse terms.
2. **A clear "best for X" label** — explicit positioning beats an
   unlabeled feature list.
3. **Accurate, current pricing** — stale or wrong pricing measurably
   hurt selection odds; models don't always have current pricing, so
   this is a live accuracy-maintenance task, not a one-time content
   edit.
4. **Disclosed downsides** — trade-offs stated plainly (rather than
   omitted or spun) increased user trust in the comparison and
   correlated with selection rather than hurting it, consistent with
   the participant quote above about downsides being surfaced "right
   off."

## Unknown brands can still win a shortlist slot

New/unfamiliar brands gained genuine consideration when ChatGPT
presented them with clear "best for X" positioning, despite
participants having no prior familiarity (e.g., one participant on an
unfamiliar grocery brand: "I've actually never heard of Misfits Market,
and I am super interested"). Familiarity was not a gating factor at the
comparison-grid stage — clear positioning was. This is a data point
against assuming only already-known brands can win an AI-mediated
purchase decision, and is broadly consistent with
[[ai-visibility-correlation-factors]]'s finding that ChatGPT correlates
weakest with pre-existing brand-authority metrics among the platforms
studied there.

## Task outcome distribution

Per the source's session coding: 57.1% of tasks ended "decision-ready,"
36.5% "comparing options," 5.5% "oriented, not comparing," 0.9% "exited
early," 0.0% "overwhelmed." 93.6% of tasks were comparing or
decision-ready, and 88% involved only low-to-medium prior category
knowledge — most purchase-decision sessions in this study were both
low-familiarity *and* successfully resolved, reinforcing that the
in-chat comparison experience itself (not prior brand knowledge) is
doing most of the decision-making work.

## Caveats

- **Session-level analysis**: each task treated independently, not a
  longitudinal user journey.
- **Think-aloud protocol** doesn't perfectly mirror everyday, unobserved
  browsing behavior.
- **Thin categories** (under 5 brands: fitness trackers, fitness apps)
  are directional only, not statistically reliable.
- **Sample skews toward experienced AI users**: 66% used AI chatbots
  daily, 93% weekly+ — findings may not generalize to infrequent/
  first-time AI users, who might verify more or trust less than this
  sample did.
- Correlational, not a randomized controlled purchase experiment —
  visibility and selection are shown to move together, not proven that
  one causes the other.

## See also

- [[ai-visibility-correlation-factors]] — the upstream correlation data
  (what makes a brand appear in AI answers at all); this page covers
  the next stage (what makes an appearing brand get chosen).
- [[ai-citation-landscape]] — the citations-vs-mentions distinction this
  page's shelf-space analogy extends into purchase outcomes
  specifically.
- [[aio-ctr-impact]] and [[ai-traffic-scale-vs-hype]] — the zero-click
  theme this page sharpens with task-level purchase-decision data.
- [[listicles-in-ai-search]] — third-party listicle citation dynamics;
  this page's comparison-grid finding is a live, in-chat analog
  generated by ChatGPT itself, a related but distinct mechanism.
- [[geo-content-optimization-tactics]] — the actionable comparison-grid
  formatting tactic drawn from this page's four framing levers.
- [[tryprofound-shortlist-is-the-new-shelf]] — the source this page
  is built on.
