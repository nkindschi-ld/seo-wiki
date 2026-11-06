---
type: playbook
tags: [aeo, seo]
updated: 2026-10-25
---

# AI Visibility Four-Layer Diagnostic

**Why / when to use this:** when a brand is missing, misdescribed, or
unrecommended in AI answers and the instinct is "publish more content".
Triage which layer is failing first. Source:
[[semrush-ai-search-strategy-4-layers]] (vendor content; the layers are
a diagnostic model, not confirmed ranking factors, and are not a fixed
sequence). Page-level counterpart: [[geo-diagnostic-checklist]].

## The four layers

| Layer | Question | Check |
|---|---|---|
| Discoverability | Can AI systems find and retrieve it? | Crawlable, indexable, text-readable; AI crawlers not blocked by robots.txt or CDN/WAF; canonicals |
| Clarity | Do they describe the brand correctly? | Verified source of truth vs. what AI says |
| Authority | Does the brand look qualified for shortlists? | Information gain, third-party mentions, comparative visibility |
| Trust | Will they confidently recommend it? | Sentiment, reviews, corroboration, caveats |

## Symptom → layer

- Pages inaccessible → **discoverability**.
- Repeatedly wrong facts → **clarity**.
- Fetched but rarely cited → **authority**.
- Mentioned but rarely recommended, or recurring caveats → **trust**.
- Citations rising while mentions/recommendations don't → trust or
  representation.
- AI visibility up without leads or revenue → measurement or relevance.
- Competitor cited on evidence you lack → authority; in the comparison
  but not recommended → trust.

## Steps

1. **Discoverability:** confirm priority pages render as text; check
   robots.txt, CDN/firewall logs (403/429, challenges) for AI crawlers —
   see [[robots-txt-audit-checklist]] and [[robots-txt-strategy]].
   Google states AIO/AI Mode need no special schema or technical
   requirements ([[google-ai-features-appearance-guide]]). Crawling is
   access, not citation.
2. **Clarity:** write a source of truth (positioning, product facts,
   pricing, terminology); audit AI descriptions against it; correct
   owned pages or request updates from third-party sources the AI
   cites. The source's example: fixing third-party descriptions, not
   publishing more own-site content, corrected how the AI described the
   vendor.
3. **Authority:** add evidence competitors can't copy (proprietary
   data, first-hand tests, original frameworks); make it extractable
   with clear summaries, Q&A, sectioning, visible lists/tables. Find
   recurring category sources and see where the brand is absent
   ([[growth-memo-why-proprietary-data-is-your-most-defensible-asset]]).
4. **Trust:** review sentiment, reviews, and corroboration; avoid
   manufactured third-party consensus.
5. **Baseline:** 20-25 buyer-decision prompts from sales calls, support,
   GSC, review language, stalled deals; grouped by persona and journey
   stage; tracked across platforms. Measure presence, representation,
   source influence, and business outcomes separately.
6. **Fix one layer, change one thing, retest** the same prompts.

## Data points from the source

Cited pages beat top-20 ranking pages on clear summarization (+32.83%),
E-E-A-T signals (+30.64%), Q&A formatting (+25.45%), section structure
(+22.91%), and visible structured data (+21.60%). 62% of 3,981 brand
appearances were citations without the brand being named. See
[[ai-citation-landscape]].

## Mistakes to avoid

- A page for every prompt variation (volume without evidence).
- Treating crawler activity as visibility.
- Conflating citations, mentions, and recommendations.
- Treating schema or llms.txt as citation switches — Google says it
  doesn't use AI-specific files; no published evidence they raise
  citations.
- Making content worse for people through machine-first formatting.

**Strategic vs. experimental filter:** a tactic that would still improve
how the brand is understood if the platform changed tomorrow is strategic;
one that depends on a single crawler, file format, or citation pattern is
an experiment.

## See also

- [[ai-visibility-content-gap-audit]], [[geo-content-optimization-tactics]],
  [[agentic-web-optimization]], [[brand-entity-seo-strategy]].
