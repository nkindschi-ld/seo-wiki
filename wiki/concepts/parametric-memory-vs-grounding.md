---
type: concept
tags: [aeo]
updated: 2026-11-06
---

# Parametric Memory vs. Web-Search Grounding

An AI assistant can put a brand or fact into an answer by two different
routes, and they behave differently for visibility:

- **Parametric memory** — knowledge stored in the model's weights during
  pre-training, recalled with no lookup. Term from Lewis et al.'s 2020
  RAG paper, contrasted with non-parametric memory (an external index
  searched at request time).
- **Web-search grounding** — the model runs a live search, reads what
  comes back, and cites some of it. The "dynamic memory layer" of AI
  assistants, and per [[dejan-link-building-outreach-ai-search]] the most
  significant type of retrieval is grounding with organic search.

## Parametric memory

- **Where it sits**: spread across weights, not addressable records.
  Feed-forward layers act as key-value memories (Geva et al., 2021);
  ROME (Meng et al., 2022) traced and edited single facts in middle-layer
  MLP weights.
- **How much fits**: ~2 bits per parameter when a fact appears ~1,000
  times in training, ~1 bit at ~100 exposures (Allen-Zhu & Li, 2024).
  A 7B-parameter model holds roughly 1.75 GB of factual content.
  **Exposure count is the binding constraint** — a fact seen a few times
  is encoded weakly or not at all; one repeated across many sources is
  recalled reliably. Consistent at the brand level: brands mentioned on
  fewer than 2,000 indexed pages were rarely named in answers
  ([[victorious-q2-2026-quarterly-search-report]]).
- **Frozen at the knowledge cutoff**: changing it needs fine-tuning,
  further pre-training, or weight editing — none run per query. A model
  can know today's date and still hold a world months or years old.
- **Failure mode**: a weakly encoded fact still yields fluent text,
  because the weights carry no "never stored" signal — the mechanism
  behind hallucination.

## Grounding funnel

Every platform runs: pages **received** → pages with **readable**
content → pages **cited**. The received-to-cited gap is where platforms
differ. DEJAN's single-query head-to-head (anecdotal, n=1):

| Platform | Received | Cited |
|---|---|---|
| Google | 7 | 7 |
| OpenAI | 39 | 2 |
| Anthropic | 14 | 9 |

Directionally consistent with the provider-level breadth-vs-depth
differences in [[ai-citation-landscape]], but not evidence on its own.
DEJAN's larger follow-up (7,060 queries) on what gets extracted from
each page — the ~2,000-word per-query budget, lead bias, and the
~20:1 GPT drop — is on [[grounding-snippets]].

## Generative self-retrieval (reasoning as recall)

Google Research's [[gekhman-thinking-to-recall-2026]] (closed-book, no
search) shows that turning reasoning on substantially expands what a
model can recall from its weights — including on simple single-hop
facts. Two mechanisms:

- **Computational buffer**: extra tokens give room for latent
  computation, even when they're filler.
- **Factual priming / generative self-retrieval**: the model writes out
  related facts, and writing them is how it retrieves them ("the first
  nine kings of Nepal make the tenth reachable"). Feeding those facts
  back with reasoning off recovers most of the gain.

**The risk**: those self-generated facts can be hallucinated, and a
hallucinated intermediate fact makes a wrong final answer much more
likely (correct answers 41%→26% on SimpleQA-Verified, 71%→32% on
EntityQuestions).

DEJAN's SEO reading ([[dejan-generative-self-retrieval-2026]]):

- The final recommendation to a commercial prompt is the top of an
  **internal ranking**: the model surfaces candidate brands from memory,
  weighs them against recalled facts plus whatever grounding sits in
  context, and picks the best-supported. Grounding narrows the field;
  it doesn't replace this step. Corroborated: brands named in ChatGPT's
  *initial* fan-out query were cited 68.9% of the time vs 2.1% for
  brands only fetched ([[lilyray-chatgpt-fanout-queries-2026]]), and
  brands in a model's top-10 training memory were live-searched 3.2×
  more often ([[geosurge-model-memory-predicts-search-2026]]).
- **Audit the facts, not the verdict.** "Best pick" has no truth value,
  but the attributes a model associates with your product (integrations,
  use cases, features) can be right or fabricated — and fabricated ones
  can carry a recommendation. This sharpens the
  representation-auditing advice in [[geo-content-optimization-tactics]].
- **Uneven by audience** (inference): reasoning mode depends on
  subscription tier and settings, so the most accurate version of your
  brand may reach paying users only. Retrieval also differs by tier:
  ChatGPT's `system2` path reaches Reddit, web-PDF and YouTube engines
  that `system1` doesn't ([[chatgpt-vertical-retrieval-engines]]).

## Implications for SEO/AEO

- **Widely and consistently mentioned brands** get answered from
  memory — with no citation and no link back. Repetition across many
  independent sources is what gets a fact encoded, which is one
  mechanism behind off-site mention correlations in
  [[ai-visibility-correlation-factors]].
- **Newer or less-mentioned brands** exist for the model only through
  retrieval, so crawlability, freshness, and surviving the funnel
  (retrieved → readable → cited) are everything. See
  [[how-google-search-works]] and [[ai-overview-grounding-and-fidelity]].
- Because grounding leans on organic search, AI visibility and organic
  visibility are tightly coupled — and so are their link-building
  inputs. Placed mentions aimed at AI answers face the same
  incongruence detection as placed links; see
  [[editorial-link-integration]].
- Agent research appears to lean much more heavily on retrieval than
  memory: [[ora-ax-is-the-new-aeo-2026]] found training data supplied
  only 7–10% of agent answers.

## See also

- [[generative-engine-optimization]] — the static vs.
  search-augmented vs. reasoning LLM taxonomy.
- [[agent-experience-ax]] — agent-researched answers and own-site
  readability.
- [[grounding-snippets]] and [[query-fanout]] — the retrieval side in
  detail.
- [[topical-authority-in-ai-search]] — "Memory is the upstream input": remembered brands get live-searched 3.2× more often ([[geosurge-model-memory-predicts-search-2026]]).
