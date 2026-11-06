---
type: source
tags: [aeo]
date_published: 2026-07-08
date_ingested: 2026-11-06
origin: raw/studies/dejan-content-optimization-engine-insights-2026.md
---

# Content Optimization Engine Insights (DEJAN)

Petrovic, D. / DEJAN AI (2026-07-08). "Content Optimization Engine
Insights by DEJAN AI." dejan.ai/blog/coe/.

**Nature of source**: vendor experiment report promoting DEJAN's
Content Optimizer. Large (2,249 experiments, 113 client properties,
10,548 edits, ~56,000 ranking passes, 2.71B tokens), but the ranker is
an **LLM re-ranking a page against its real competitors in a
controlled setting** (four leading models), not a live search system.
Raw data is not public. Treat as strong directional evidence about
what sways an LLM choosing between comparable pages.

## Method

Hypothesis-driven loop: baseline-rank the page against current
winners → write testable hypotheses with priors → make one attributable
edit (to the full page or its grounding snippet) → re-rank ~5× and take
the median → keep the edit only if it moves the page up. Belief was
revised downward 5,911 times vs. upward 1,440 — most plausible ideas
failed.

## Key takeaways

1. **Idea-family win rates** (share of tested ideas producing a real
   rank gain): Framing 31.4%, Alignment (query words/intent) 26.2%,
   Architecture (opening line, sentence length, formatting) 25.4%,
   Style 25.2%, Substance (facts, entities, numbers) 25.1%, **Proof
   (awards, endorsements, citations) 15.4%** — roughly half the rest.
2. **Strongest single levers**: "best of"/top-N framing 38.4%, "what
   is"/definition framing 36.7%, clear category definitions 33.3%,
   short concise sentences 33.1%, how-to framing 30.9%, query-intent
   match 27.7%.
3. **Weakest**: awards/certifications 13.1%, expert endorsements 14.8%,
   scale signals 15.6%, statistics and study citations 18.2%, .gov/.edu
   citations 18.9%, more raw numbers 20.7%.
4. **Outcomes**: page reached #1 in 1,554 of 2,246 runs (~69%); average
   +2.74 positions per experiment; ~1 in 4 edits helped (avg +2.31,
   max +10 from one change).
5. **"It depends"**: for Gemini, the top two positive factors also
   appear at the top of the negative list (+1701/+1101 vs. −81/−80) — a
   lever can help in one competitive set and hurt in another, so every
   edit must be tested in context.
6. **Cost shape**: ranking consumed ~83% of tokens; full-page
   optimization was under a third of experiments but 91% of tokens.

## Wiki pages updated

- [[geo-content-optimization-tactics]] — win-rate table; new
  **Conflicting Evidence** entry against the Aggarwal 2023 Statistics
  Addition / Cite Sources findings.
- [[generative-engine-optimization]] — cross-link to that conflict.
- [[listicles-in-ai-search]] — "best of" framing as the top single lever.
