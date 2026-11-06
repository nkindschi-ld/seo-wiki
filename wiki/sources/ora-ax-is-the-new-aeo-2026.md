---
type: source
tags: [aeo, seo]
date_published: 2026-10-08
date_ingested: 2026-10-08
origin: raw/studies/ora-ax-is-the-new-aeo-2026.md
---

# AX is the New AEO (ora research)

Finder, I., Elovic, A., Shalev, G., & Yosef, L. (2026). "AX is the New
AEO." ora research (era labs), arXiv:2609.34951. Blog version published
2026-10-08 at ora.ai/blog/ax-is-the-new-aeo; analysis code and a sample
of derived data released at github.com/ora/research.

**Design**: 37,927 agent journeys (140k+ page fetches) across 1,056
live business sites, four agent harnesses (claude-agent-sdk/Sonnet 4.6,
claude-code/Haiku 4.5, openclaw/GPT-5.4-mini, eve/GPT-5.4), real buyer
questions. Sites split by an agent-readiness score and matched in pairs
within industry on brand fame, prior model knowledge of the brand, and
off-site citation breadth. Recommendation strength rated by two blind
LLM judges (Claude + GPT); accuracy graded on 31,127 asked facts across
2,499 answers (131-business sample) against each site's own content.
Sites scored 2026-08-24; runs late Aug–Sep 2026.

**Vendor caveat**: ora sells the agent-readiness ranker that defines
the "agent-ready" vs "not agent-ready" split, and points readers to the
agentready.org spec it's associated with. The matched-pair design and
released data mitigate this, but it is a single vendor-run study and
the readiness score's internals (100+ checks) aren't defined in the
post.

## Key takeaways

1. **Training data is a shrinking slice of the answer.** In today's
   agent models training knowledge supplies 7–10% of the finished
   answer, vs ~half for gpt-4.1. Corroborated by external data:
   frontier models search ~9 in 10 times on recency-dependent
   questions; ChatGPT searches anchored to the current year rose from
   ~6% (GPT-5.2) to 87% (GPT-5.5).
2. **Readability → recommendation.** Clear endorsement (both judges)
   20% for agent-ready vs 11% not → **1.9×** (controlled number); up to
   2.6× by stack, 2.5× in IT infrastructure. "Too weak to recommend"
   answers 2.5× more common when the site isn't agent-ready.
3. **Blocked agents don't give up.** ~99% of dead-end journeys still
   produced an answer. Web search's share of the answer doubles
   (12% → 25%); own-page share falls 78% → 58%; training knowledge
   stays 7–10% either way.
4. **Omission, not error.** Off-site answers are 3.7× more likely to
   contain *none* of the asked facts (25% vs 7%). Wrong facts stay rare
   (4% vs 6%); "never mentioned" grows 29% → 45%. These answers read
   fluent and confident, so hallucination metrics don't catch them.
5. **Pricing is where own-site reading pays most** (60% vs 37%
   accuracy). Setup is limited by findability: two-thirds of setup
   facts never surface from either source.
6. **Blocking is costly for the agent operator**: 23% more turns, 2.1×
   more blocks, +64% average (up to +93%) cost per grounded answer. The
   authors infer harnesses will be pushed to route around such sites.
7. **Aug 8, 2026 ChatGPT shift**: `site:` queries rose from ~0% to
   23–24% of ChatGPT background searches; Reddit's share of ChatGPT
   citations fell ~86% (Promptwatch; Qwairy measured 95% on a
   different panel), partly recovering to ~1.5%.
8. **Unmeasured next frontier**: assistant-owned connectors/registries
   (Agentic Resource Discovery spec, ChatGPT plugin directory, Meta
   Muse) could make the open web a fallback; the authors explicitly
   don't claim this yet.

Authors' framing: **"AEO is now SEO plus AX"** — SEO governs whether
agents find you; AX (agent experience) governs whether they can reach,
read, and verify your site, and therefore what the answer says.

## What this updated

- New concept [[agent-experience-ax]] (this source's primary
  contribution).
- [[agentic-web-optimization]] — AX as measured evidence for the
  "agent readiness" layer; connectors/registries added to the protocol
  landscape; new Conflicting Evidence section on off-site presence.
- [[optimizing-for-the-agentic-web]] — new "Unblock and verify" section
  ahead of layer 2.
- [[ai-visibility-correlation-factors]] — Conflicting Evidence: off-site
  mention correlation vs. own-site readability as the bigger lever.
- [[generative-engine-optimization]] — co-occurrence/training-data
  tactic flagged as targeting a shrinking slice.
- [[ai-citation-landscape]] — time-sensitivity note on pre-August-2026
  Reddit data.
- [[ai-overview-grounding-and-fidelity]] — cross-surface corroboration
  of omission as the dominant failure mode.
- [[robots-txt-strategy]] — measured cost of blocking agents.

## Conflicts

Logged as unresolved: this source argues off-site seeding (Reddit
threads, third-party listicles, citation placement) is losing leverage,
against existing correlation data ranking off-site mentions as the
strongest AI-visibility factors. See [[ai-visibility-correlation-factors]]
and [[agentic-web-optimization]].
