---
type: playbook
tags: [seo]
updated: 2026-07-08
---

# Classic SEO Ranking Factors Playbook

**Why/when to use this:** Apply these for classic organic SERP ranking
(the "ten blue links," not AI-generated answers). For AEO/citation-stage
tactics specifically, see [[geo-content-optimization-tactics]] instead —
the two overlap in places (both de-prioritize keyword stuffing, both
value quality over volume) but this one is grounded in classic-SERP
correlation data. See [[traditional-seo-ranking-factors]] for the
underlying concept.

Based on [[semrush-ranking-factors-study-2024]] (16,298 keywords,
300,000 organic positions, Spearman correlation — correlational, not
causal).

## Do this

1. **Cover the topic comprehensively, not just the exact keyword.**
   Text relevance (topical/subtopic coverage) is the strongest correlate
   with ranking (~90.6% for top-10). Write for the full breadth of what
   a user needs to know, not a single query match.
2. **Build a genuine backlink profile from authoritative, relevant
   sources.** Domain/Page Authority Score correlate meaningfully
   (0.19–0.21). "Create content that catches attention and attracts
   links and mentions," then promote it — don't expect links to appear
   passively. See [[link-building]] and [[link-building-outreach-tactics]]
   for the acquisition strategy/tactics, and
   [[link-and-anchor-text-best-practices]] for the link-markup and
   anchor-text mechanics that make links crawlable and meaningful once you
   have them, including internal linking.
3. **Encourage and respond to reviews.** Star ratings/reviews correlate
   with rankings and directly reinforce E-E-A-T Trust — see
   [[e-e-a-t-and-page-quality]]. For local businesses, prioritize Google
   Business Profile reviews specifically.
4. **Audit and improve pages already ranking 2-20**, not just page one.
   Pages ranking top-1 for a term tend to rank for ~4x as many other
   terms as position-20 pages — improving an already-decent page can
   have compounding returns across many queries at once.
5. **Attribute content to credible authors/teams where relevant.**
   Author experience/expertise is explicitly named in the Search Quality
   Evaluator Guidelines as a rating factor, even though schema markup for
   authorship correlates weakly on its own — the underlying trust signal
   matters more than the markup.

## Don't bother

- **Keyword stuffing in titles/meta descriptions.** Exact-match keyword
  presence in titles/descriptions correlates minimally; semantic
  relevance to the topic correlates better. Write titles/descriptions
  that describe the content naturally.
- **Engineering your backlink anchor-text ratio.** Per
  [[ahrefs-anchor-text-2020]], every anchor-text type (including
  exact-match) shows weak-to-negligible ranking correlation, and
  attempting to control the mix at scale risks a Penguin-style
  penalty. Let backlink anchor text occur naturally — see
  [[link-and-anchor-text-best-practices]] for the full writeup.
- **Padding content length/word count.** No correlation with rankings.
  Match length to what the topic actually needs — don't add filler to
  hit a word-count target.
- **Over-implementing Schema.org markup for ranking purposes.** Very
  low correlation, and manipulative use "can bring on a penalty." Use
  schema where it genuinely helps (rich results, clarity for Google),
  not as a ranking hack.
- **Chasing Core Web Vitals/technical scores as a primary lever.** Weak
  correlation — treat these as a tie-breaker and a genuine UX concern,
  not the main ranking driver. Still worth fixing, just don't expect it
  to move rankings dramatically on its own.
- **Obsessing over bounce rate/time-on-site as ranking signals.**
  Minimal-to-no correlation found. Track them for UX/business reasons if
  useful, not because they're presumed to directly drive rankings.

## Classic SEO vs. AEO tactics: where they align and diverge

| Area | Classic SEO ([[traditional-seo-ranking-factors]]) | AEO/GEO ([[generative-engine-optimization]]) |
|---|---|---|
| Keyword stuffing | Doesn't help | Doesn't help (worse than baseline) |
| Content volume | No correlation | Near-zero correlation |
| Citations/quotes/stats | Not directly measured by this source | Strongest tactics (+40% visibility) |
| Backlinks/Domain authority | Moderate correlation | Weakest correlate of AI-mention visibility |
| Video/YouTube presence | Excluded from this study's dataset | Strongest correlate of AI-mention visibility |

Both agree: **quality and genuine relevance beat volume and
keyword-matching tricks**, in both classic search and AI answers. Where
they diverge most is backlinks (still meaningful for classic SERPs,
weak for AI-mention visibility) and video presence (irrelevant to this
classic-SERP dataset, dominant for AI visibility).
