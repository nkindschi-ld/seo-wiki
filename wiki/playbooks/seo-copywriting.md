---
type: playbook
tags: [seo]
updated: 2026-11-06
---

Why / when to use this: apply at the drafting stage, once a page is
already mapped to a target keyword (see
[[keyword-mapping-and-cannibalization]]) and its cluster role is
decided (see [[topic-cluster-strategy]]) — this playbook is about how
to *write* the page, not what page to write or which keyword it should
target.

## What SEO copywriting is

Writing that's simultaneously optimized for search algorithms and
genuinely engaging for human readers. Two goals held at once: rank for
relevant keywords, and hold the reader's attention once they arrive.

## Tactics

**Research (before writing)**
- Target specific, lower-competition keywords rather than the single
  highest-volume head term (see [[keyword-research]] for discovery
  methods).
- Mine "People Also Ask" and question tools (AlsoAsked, AnswerThePublic,
  Quora, topic-research tools) for content-idea generation — this
  answers "what do people want explained," a different question than
  keyword-volume tools' "what do people type."
- Identify and satisfy the query's **search intent** (informational,
  navigational, commercial, transactional) — match content *format*
  to intent, not just content topic.
- Run a competitor gap check: which ranking pages exist for this
  keyword, what's their format/structure, and what's missing that a
  linkable, more complete asset could fill.

**On-page structure**
- Title tag under ~55-60 characters, primary keyword included.
- Unique meta description under ~120 characters with a clear CTA.
  *(Contested: newer guidance and the house spec use ~155 — see
  Conflicting Evidence below.)*
- Descriptive H1 with proper H2/H3/H4 hierarchy underneath — not just
  visual formatting, an actual outline.
- Title tag and H1 should never be identical. They cover the same topic,
  but the title tag carries more optimization weight: write it first,
  keyword-led and sized for the SERP, then phrase the H1 differently
  (for example a fuller or more conversational version) rather than
  repeating it. *House rule set by the site owner (2026-11-04), not yet
  backed by an ingested source.*
- Table of contents for longer pieces — doubles as a structural
  self-check: if you can't write a clean, specific TOC, the draft's
  structure likely needs work.

**Writing craft**
- Short paragraphs that lead with the main idea (inverted pyramid /
  "bottom line up front") — don't bury the point. This isn't just a
  readability nicety: generative retrieval systems show a measured
  positional bias toward content near the start of a document (see
  [[geo-content-optimization-tactics]]'s "Reduce perplexity and
  front-load core claims").
- Simple vocabulary; explicitly avoid unexplained jargon.
- Include visuals (images, charts, video) where they add real
  information, not decoration — also supports [[image-seo-checklist]]
  and increases time-on-page.
- Place CTAs deliberately, aligned to where a reader would naturally
  want a next step, not just at the very end.

**Linkable-asset framing**
- Build content substantial enough (original research, case studies,
  in-depth guides) to earn links naturally, not just to rank — the same
  quality bar that makes content viable for [[digital-pr-strategy]]
  pitching.

## Checklist

- [ ] Primary keyword chosen with intent verified against the SERP.
- [ ] Content format matches search intent (list/how-to/comparison/
      product page, as appropriate).
- [ ] Title tag ≤ ~60 chars, meta description ≤ ~120 chars with a CTA
      (≤ 155 / 65 with " | LaunchDarkly" for LaunchDarkly pages — see
      Conflicting Evidence).
- [ ] Clear H1 + logical H2/H3 outline; TOC included for longer pieces.
- [ ] H1 worded differently from the title tag (never an exact match).
- [ ] Paragraphs lead with the point; jargon explained or removed.
- [ ] At least one genuinely informative visual included.
- [ ] CTAs placed where a reader would naturally act, not just at the
      end.
- [ ] Content substantial/original enough to be link-worthy, not just
      rank-worthy.

## Conflicting Evidence

- **Claim**: keep meta descriptions under ~120 characters.
  - Supported by: [[semrush-seo-copywriting]] (2023-01-31) — vendor
    blog; a cautious mobile-truncation target.
  - Contradicted by: [[writing-meta-tags]] (updated 2026-09-23) —
    ~150–155 characters; [[writer-checklist-blog-posts]] — under 155;
    and LaunchDarkly's house meta spec (155-char description, 65-char
    title including " | LaunchDarkly").
  - **Current best guess**: use **155 / 65 for LaunchDarkly pages** —
    newer, and it's the site owner's own spec. Keep ~120 as an optional
    tighter target where mobile truncation matters; Google rewrites
    most descriptions anyway (~63% per [[ahrefs-site-audit-study-2023]]).
    Title-length guidance (~55–60 here vs. ~50–60, max ~65) differs only
    slightly and isn't treated as a conflict. Flagged **unresolved**.
    (Filed during the 2026-11-06 wiki merge.)

## See also

- [[keyword-mapping-and-cannibalization]] — decides which keyword this
  page targets before writing starts.
- [[topic-cluster-strategy]] — decides whether this page is a pillar,
  subpage, or target page, which shapes scope/length.
- [[link-and-anchor-text-best-practices]] — anchor text rules for links
  placed within the copy.
- [[e-e-a-t-and-page-quality]] — the underlying quality framework this
  craft-level guidance supports.

See [[semrush-seo-copywriting]] for the full source writeup.
- [[writing-meta-tags]] — title/description length rules, good-vs-bad examples, and the house 65/155 spec
