---
type: playbook
tags: [aeo, seo]
updated: 2026-07-27
---

# AI Entity Footprint Audit

Why / when to use this: use as a **diagnostic** when you want to know how well
AI systems actually *understand* your brand — its identity, what it does, why
it's different, and whether it's trustworthy — before or alongside chasing
citations and rankings. It sits upstream of visibility: if AI can't coherently
describe you, citation tactics have nothing solid to attach to. Complements
[[brand-entity-seo-strategy]] (which *builds* the entity signals this audit
inspects) and [[ai-visibility-measurement-methodology]] (which measures
citation/traffic *outcomes*, not understanding). From
[[sel-ai-entity-footprint-audit]] (Rich Sanger, Search Engine Land, 2026).

## Core reframe

Audit the **collective** understanding your digital presence creates, not each
asset in isolation. The question is not "is this page optimized?" but "does
everything together let AI explain who we are, what we do, and why we matter?"
This is an entity-level view — see [[entity-oriented-search-fundamentals]] for
why AI models a brand as an entity assembled from many signals.

## The six dimensions

Score each 0–5 (rubric below):

1. **Identity** — Can AI consistently explain what you do, who you serve, and
   where you operate — the *same way* across platforms?
2. **Differentiation** — Is it clear why a customer should pick you over
   competitors, with evidence behind the claim?
3. **Evidence** — Are claims backed by independent validation (reviews,
   certifications, media, testimonials) rather than self-assertion?
4. **Consistency** — Do multiple sources reinforce one coherent story, or do
   they contradict each other?
5. **Relationships** — Are connections to your industry, partners,
   associations, and communities clearly established?
6. **Specialization** — What are you *genuinely known for*, judged by recurring
   themes across touchpoints (not by what you claim)?

## The four signal categories

Each dimension is fed by signals in four buckets — audit all four, and note
which bucket a given weakness lives in:

- **Owned** — website, service pages, structured data, team profiles
- **Customer** — reviews, testimonials, case studies
- **Third-party** — press mentions, awards, business directories, certifications
- **Ecosystem** — partnerships, associations, speaking engagements, community
  involvement

## Scoring rubric (0–5 per dimension)

| Score | Meaning |
|-------|---------|
| 0 | No meaningful evidence |
| 1 | Very limited evidence |
| 2 | Basic but fragmented evidence |
| 3 | Clear foundational understanding |
| 4 | Strong, consistent, well-supported |
| 5 | Exceptional understanding across independent sources |

Sum or track per-dimension over time; the per-dimension scores tell you *where*
to invest (e.g. strong Identity but weak Evidence → go get independent
validation).

## The audit process

1. **Probe the AI directly.** Ask "Tell me everything you know about
   [Business Name]" across multiple AI platforms (ChatGPT, Claude, Gemini,
   Perplexity, Google AI Mode). Capture how each describes identity,
   specialization, differentiation, and supporting evidence — and where they
   go vague, wrong, or contradictory.
2. **Website review.** Do the homepage, About page, service pages, and
   structured data clearly communicate identity and differentiation? (Cross-ref
   the `Organization`-schema and entity-home work in
   [[brand-entity-seo-strategy]].)
3. **Google Business Profile comparison.** Check consistency between the site
   and GBP — same services, same specializations, same wording where it counts.
4. **Customer analysis.** Find recurring themes in reviews — what customers
   *actually* recognize you for (feeds the Specialization dimension).
5. **Third-party validation.** Search for independent evidence: press, podcast
   appearances, certifications, awards (feeds Evidence).
6. **Holistic evaluation.** Step back: does the total evidence answer the
   fundamental questions of identity, differentiation, trustworthiness, and
   uniqueness? Gaps here are the audit's output.

## Industry variation

The framework is constant; the evidence sources differ:

- **Local businesses** — Google Business Profile, reviews, citations
- **Professional services** — expertise signals: publications, speaking
- **SaaS** — integrations, partnerships, ecosystem relationships
- **Ecommerce** — product reviews and comparisons

## Checklist

- [ ] Ran the "tell me everything you know about [Business]" probe across ≥3 AI
      platforms and logged the answers
- [ ] Scored all six dimensions 0–5 with a note on the weakest signal bucket
      per dimension
- [ ] Website (home/About/services) + structured data reviewed for clear
      identity & differentiation
- [ ] Website ↔ Google Business Profile consistency verified
- [ ] Recurring review themes extracted (Specialization signal)
- [ ] Independent third-party validation inventoried (Evidence signal)
- [ ] Cross-source contradictions flagged (Consistency signal)
- [ ] Gaps translated into an action list feeding [[brand-entity-seo-strategy]]

See [[sel-ai-entity-footprint-audit]] for the source writeup.
