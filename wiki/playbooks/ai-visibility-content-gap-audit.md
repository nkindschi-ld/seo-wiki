---
type: playbook
tags: [aeo]
updated: 2026-11-02
---

# AI Visibility Content Gap Audit

**Why / when to use this:** run when you track AI answers (prompts,
mentions, citations) and want to decide *which content to create or
fix*. It is the prompt-level complement to the page-level
[[geo-diagnostic-checklist]] and the site/brand-level
[[ai-visibility-four-layer-diagnostic]]. Source: [[hubspot-ai-content-gaps]]
(vendor content, no original data).

## Gap types

- **Coverage gap** — no page adequately answers the question.
- **Extractability gap** — a relevant page exists but its answer is hard
  to find, interpret, or reuse.
- **Citation-support gap** — the brand is mentioned or has content, but
  another source supplies the evidence the AI uses.

A page can rank in Google and still show up in none of these answers,
so SEO gap analysis ([[seo-competitive-analysis]]) does not substitute.

## Steps

1. **Collect prompts**, grouped by topic and intent, across ChatGPT,
   Gemini, Perplexity, etc.
2. **Classify mentions and citations separately** in a spreadsheet:
   prompt, platform, date, brands named, sources cited. (Citations
   without mentions are common; see [[ai-citation-landscape]].)
3. **Map prompts to existing content:** does a page cover the question,
   answer it clearly, provide evidence, and match the audience's
   decision criteria?
4. **Prioritize** by business impact vs. effort: high-impact/low-effort
   first, defer low-impact/high-effort and record why.

## Choose the action

- Refresh outdated pages.
- Improve extractability: answer directly and early, descriptive
  headings, related claims next to their evidence, defined terms,
  key information in text (not only images).
- Strengthen evidence: first-hand experience, documented examples,
  research with stated methodology.
- Create new content only when no suitable page exists.
- Study cited sources for the evidence and framing the answer needs —
  don't copy competitors.

## Measure

- Brand mention presence = answers mentioning brand ÷ tracked answers.
- Citation presence = answers citing ≥1 brand URL ÷ tracked answers.
- AI share of voice — entity-based *or* citation-based; choose once.
- AI-referred traffic and outcomes as supporting evidence only.
- Fix the baseline first; same prompts, same platforms; expect
  run-to-run variation.
- Size of that variation, per [[detailed-ai-volatility-2026]]: identical
  brand lists repeat on two random days only 0.3% (ChatGPT) / 1.1% (AIO)
  of the time, while each prompt's leading brand is present 82–89% of
  days. Judge gaps on presence over a window of about two weeks or more,
  not single runs. Treat "first-mentioned" changes as noise. See
  [[ai-answer-volatility]].

## Pitfalls

- [ ] Not chasing every missing mention — look for patterns.
- [ ] Not targeting broad topics over high-impact ones.
- [ ] Not trading readability for structure.
- [ ] AI-generated drafts fact-checked by a human.

## See also

- [[geo-content-optimization-tactics]], [[geo-diagnostic-checklist]],
  [[ai-visibility-four-layer-diagnostic]], [[keyword-research]].
