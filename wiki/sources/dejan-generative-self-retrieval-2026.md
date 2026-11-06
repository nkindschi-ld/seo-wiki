---
type: source
tags: [aeo]
date_published: 2026-06-27
date_ingested: 2026-11-06
origin: raw/articles/dejan-generative-self-retrieval-2026.md
---

# Generative Self-Retrieval: How AI Models Recall Brand Facts From Memory (DEJAN)

Petrovic, D. / DEJAN AI (2026-06-27). dejan.ai/blog/generative-self-retrieval/.

**Nature of source**: practitioner interpretation of
[[gekhman-thinking-to-recall-2026]] for an SEO audience. The paper's
findings are measured; the brand/visibility framing (internal ranking,
subscription-tier slant) is DEJAN's inference.

## Key takeaways

1. **Generative self-retrieval** = when reasoning, a model writes out
   facts related to the question, and writing them is itself the act of
   retrieving them from its weights (spreading activation). The
   candidate best supported by recalled facts becomes the answer — an
   **internal ranking** that runs alongside external retrieval.
2. Repeats the parametric-memory background already in
   [[parametric-memory-vs-grounding]] (Lewis 2020, Geva 2021, ROME,
   Allen-Zhu & Li capacity figures).
3. **Pipeline placement**: prompt → fanout → working set → grounding
   snippets → context (prompt + snippets + personalization) → generative
   self-retrieval ranks candidates against everything in context.
   Grounding narrows the field; the model still orders and picks.
4. **Grounding is just context tokens** to the model; models are trained
   to weigh provided context heavily, but grounding doesn't bypass the
   internal ranking.
5. **Fragility**: hallucinated intermediate facts make wrong answers
   more likely (41%→26% and 71%→32% correct). A brand can climb or fall
   on attributes the model invented — so audit the *facts* models
   associate with you, since the "best pick" verdict itself has no truth
   value to check.
6. **Access slant** (DEJAN's inference): reasoning mode depends on
   subscription tier and settings, so paying users may get a sharper,
   more accurate picture of a brand than free-tier users.

## Wiki pages updated

- [[parametric-memory-vs-grounding]] — new "Generative self-retrieval"
  section.
