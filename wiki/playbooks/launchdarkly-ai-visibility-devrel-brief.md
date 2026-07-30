---
type: playbook
tags: [seo, aeo]
updated: 2026-07-29
---

# LaunchDarkly AI-Visibility DevRel Brief (~15 min)

> **Status: working draft (v2) — owner (Neal) will update.** Reframed
> around LaunchDarkly's May-2026 repositioning: *the runtime control
> layer for the AI era* ("Move at AI speed. Stay in control."), two
> solutions on one platform — **CodeControl** (AI-built code) and
> **AgentControl** (AI agents in production). Feature flags are the
> foundation, not the focus. Data points cite wiki sources; LD-specific
> figures come from internal Glean docs (Platform Messaging Framework,
> AI deal deck, DevRel strategy, repo/docs AEO audit).

Why/when to use this: a short, awareness-oriented briefing to show DevRel
why LaunchDarkly's *repositioning* only succeeds if it also lands in the
AI layer — where developers now form first impressions — across both
coding agents and LLM chat/search, and where DevRel plugs in. Built on
[[optimizing-for-coding-agent-recommendations]],
[[ai-coding-agent-tool-selection]], [[geo-content-optimization-tactics]],
[[ai-shortlist-effect]], and [[brand-entity-seo-strategy]].

## 0. Cold open — AI still thinks we're the feature-flag company (1–2 min)

- We just repositioned as **the runtime control layer for the AI era** —
  CodeControl + AgentControl, not "the feature-flag company." The AI
  layer hasn't gotten the memo.
- Proof it's stuck on the old model: asked to "add feature flags" in a
  fresh repo, LaunchDarkly is the **primary pick 0% of the time despite
  a ~38% mention rate** ([[ai-coding-agent-tool-selection]]). Agents know
  the *old* LD and still pass us over — the research calls this "**known
  but rejected**," *worse* than being invisible.
- The bigger miss isn't the flags category — it's that our whole
  runtime-control and **AgentControl** story is **absent** from AI
  answers. We're being evaluated on a narrow, outdated identity.
- **Point:** the repositioning campaign runs on the website, ads, and
  field. But developers increasingly meet us through an AI first — and
  that channel is still describing the company we used to be.

## 1. WHAT "showing up in AI" means for the new LD (2 min)

Two surfaces, one story — and both must reflect *runtime control*, not
just flags:

- **Surface A — Coding agents (Claude Code, Copilot, Codex):** when a dev
  says "let me ship this AI feature safely" or "add feature flags," does
  the agent reach for LaunchDarkly and wire it up? Build-vs-buy +
  training-data + repo-readiness game.
- **Surface B — LLM chat & AI search (ChatGPT, Perplexity, AI
  Overviews):** for "how do I control AI agents in production," "safe
  AI-generated code," or "progressive delivery," do we get
  cited/recommended? Content + citation game — and **AgentControl is a
  young category where the AI mental model isn't set yet.**
- **Upstream of both — entity understanding:** does AI know LD = "runtime
  control for the AI era," spanning code *and* agents? Right now the
  model's picture of us is stale, and both surfaces inherit it
  ([[brand-entity-seo-strategy]], [[ai-entity-footprint-audit]]).

## 2. WHY it matters now (2–3 min)

- **The first impression is now an AI answer.** Developers ask an agent
  before they ask Google — so if AI still says "feature-flag company,"
  the repositioning stalls where it matters most. Showing up in the AI's
  answer is most of the battle: the tools AI surfaces are usually the
  ones developers pick ([[ai-shortlist-effect]]).
- **We're fighting on two fronts, both quiet:**
  - *CodeControl / flags:* agents **build it themselves** — DIY is the #1
    "competitor" in this category (~69% custom code) and accelerating.
  - *AgentControl:* the category is **new and unclaimed** in AI answers —
    whoever the models learn to associate with "governing agents in
    production" wins the default. That's ours to take or lose.
- **It compounds.** Recommended → adopted → more training data → more
  recommended. Claiming the AgentControl mental model early is
  defensible; reclaiming it late is expensive.
- **It's the same goal DevRel already owns:** "beyond the feature-flag
  company," measured in the channel developers actually use.

## 3. HOW we win — four plays (5–6 min)

DevRel touches all four as a contributor/quality layer.

**Play 1 — Be agent-ready where agents look first (repos & docs)**
- `AGENTS.md` / `CLAUDE.md` on every SDK repo (audit: **0 of 7 flagship
  SDK repos** have one today), copy-pasteable quickstarts, and our MCP
  server + agent skills cross-linked from READMEs — we already ship an
  onboarding skill (`npx skills add launchdarkly/agent-skills`); make
  agents find it ([[writing-effective-agents-md-files]]).
- **Test it, don't assume it:** run Claude Code / Copilot against our
  repos and watch — can the agent install, configure, and reach a working
  flag *or a governed AgentControl config* unattended? Treat agent
  success rate as a first-run metric.

**Play 2 — Get into the training data**
- Idiomatic LD examples in the stacks agents build in (Next.js/TS,
  FastAPI/Python), for both CodeControl *and* AgentControl patterns; keep
  them current or they teach the old, flags-only picture.
- Shape the simple-case SDK API to match the DIY code a model writes, so
  LD is the natural "deferred buy" upgrade path.

**Play 3 — Be citable in chat & AI search (content)**
- Q&A-format headers, comparison tables (e.g. "Observability vs. Runtime
  Control," "Offline eval vs. runtime control of agents"), and **original
  data** — the AI Control Gap Report (48% fewer daily prod incidents vs.
  homegrown) is exactly the unique, citable data LLMs reward
  ([[geo-content-optimization-tactics]]).
- Own the emerging vocabulary: publish the definitive answers to "what is
  runtime control," "how do I govern AI agents in production" before the
  category's mental model hardens around a competitor.
- Off-site presence where AI sources: Reddit (9x citation multiplier in
  controlled tests), YouTube long-form, LinkedIn Pulse, third-party
  listicles.

**Play 4 — Build free, useful tools as link & mention magnets**
- Calculators, sandboxes, open utilities (we already have a power-analysis
  calculator) earn the links and named mentions that feed AI citations
  and traditional authority — and double as PLG top-of-funnel.

**Cross-cutting — reframe the category, don't fight on flags.** PostHog
beat us in flags by *bundling*. Our stronger move is to stop being scored
as a standalone flag SDK: position LD as *the runtime control layer* code
and agents run on top of — a category where we define the terms
([[optimizing-for-coding-agent-recommendations]] point 9).

## 4. Where DevRel fits (1–2 min)

- DevRel is the **contributor and quality layer, not the owner** (per the
  DevRel strategy) — but this channel runs on exactly what DevRel makes:
  credible repos, runnable CodeControl/AgentControl examples, technical
  content, authentic community presence. It *is* the "credibility engine
  for the AI-era repositioning" DevRel already signed up for.
- SEO/AEO owns measurement, structure, and the citation playbook; DevRel
  owns the credible raw material and the agent-facing developer
  experience.

## 5. The one thing to remember (30 sec)

- **Developers meet LaunchDarkly through an AI first — and it's still
  describing the company we used to be.** The repositioning isn't done
  until the AI layer says "runtime control for the AI era," across both
  the coding-agent and the chat surface.

## See also

- [[optimizing-for-coding-agent-recommendations]] — vendor-facing tactics
  behind Plays 1, 2, and the category reframe.
- [[ai-coding-agent-tool-selection]] — study data behind the 0%/38% and
  bundling findings.
- [[geo-content-optimization-tactics]] — content/citation tactics behind
  Play 3.
- [[ai-shortlist-effect]] — the visibility-to-selection link behind
  "why now."
- [[brand-entity-seo-strategy]] / [[ai-entity-footprint-audit]] — the
  entity-understanding layer upstream of both surfaces (most relevant
  given the repositioning).
