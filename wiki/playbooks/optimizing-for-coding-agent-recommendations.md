---
type: playbook
tags: [aeo]
updated: 2026-07-22
---

# Optimizing for Coding Agent Recommendations

Why/when to use this: apply if you're a developer-tool, library, or
platform vendor and want Claude Code (or similar coding agents) to be
the thing a developer actually gets when they ask an open-ended
question like "add a database" or "how do I deploy this?" without
naming your product. Based on [[ai-coding-agent-tool-selection]] /
[[amplifying-claude-code-picks-2026]] /
[[amplifying-codex-vs-claude-code-picks-2026]] /
[[amplifying-claude-code-picks-fable-2026]] /
[[amplifying-claude-code-hardcoded-vendors-2026]].

## 1. Beat the "build it myself" default first

In 12 of 20 categories studied, the agent's own code-generation is the
top competitor, not another vendor — up to 100% of picks in some
categories. Before worrying about competing tools, make sure the agent
has a compelling reason to reach for your product instead of just
writing the feature from scratch:

- Make integration genuinely faster/simpler than a DIY implementation
  for the common case (the agent optimizes for "shortest path to a
  working answer").
- Position as a primitive the agent can build *on top of*, not a
  competing full solution it has to choose *instead of* writing code —
  categories with high Custom/DIY rates (auth, feature flags,
  observability) reward "obviously integrates with existing code"
  framing over "replaces what you'd write."

## 2. Get into the training data agents actually draw on

- Ensure your tool appears in recent, high-quality, idiomatic code
  examples — the recency-gradient finding means newer model versions
  systematically favor tools with more recent representative code in
  their training data, sometimes displacing an established incumbent
  entirely (Prisma → Drizzle, 79%→0% across two model generations).
- Keep example code current with your latest API/idioms — stale
  examples associate your tool with an outdated pattern.
- Publish reference implementations in the specific stacks agents are
  commonly asked to build in (Next.js/TypeScript, FastAPI/Python,
  React SPA — the ecosystems this study covered).

## 3. Ship a getting-started path an agent can follow unattended

- Clear, minimal, copy-pasteable setup docs — the agent is essentially
  following your quickstart on the developer's behalf.
- Avoid setup steps that require manual dashboard clicks/human judgment
  where possible; agents favor tools where the whole flow (install →
  configure → working code) can be scripted.

## 4. Target the right competitive tier for your category

Not all categories behave the same way — check where yours falls before
picking a strategy:

- **Near-monopoly category** (a single tool >75% share, e.g. current
  CI/CD, Payments, UI-component incumbents): displacing the incumbent
  is hard; consider a narrower wedge (a specific sub-case, a specific
  ecosystem) rather than a head-on default-choice fight.
- **Competitive/fragmented category** (no dominant tool, e.g. Caching,
  Background Jobs, Real-time, ORM choice at the time of this study):
  more winnable — the agent has less-settled priors, so training-data
  presence and a strong quickstart can move share meaningfully.
- Get your category tier from a current tool-selection study, not from
  this one indefinitely — these rankings are a snapshot and will shift
  as models retrain (see the recency-gradient finding).

## 5. Don't settle for "known but rejected"

Being actively considered and passed over every time (like this study's
findings for Redux, MongoDB, or Prisma-vs-the-newest-model) is a worse
state than being unknown — it means the agent has evaluated you and
picked something else as default. If your tool is a common "alternative
mention" but rarely the primary pick, treat that as a specific signal:
you're visible enough to be considered, so the blocker is likely
integration friction or perceived complexity relative to the current
default, not discoverability.

## 6. Track this like you'd track SERP rank

Coding-agent tool selection is measurable the same way this study did
it: run a fixed set of open-ended prompts against the target agent(s)
in a clean repo, across the phrasings and stacks relevant to your
category, and check whether you're the primary pick, an alternative
mention, or absent. Re-run periodically — the recency-gradient and
run-to-run variance findings mean a single check is a snapshot, not a
stable measurement.

## 7. Measure per-agent, not against a single coding agent

Codex and Claude Code agree on a named top pick in only ~1 of 12
contested categories — the rest is Custom/DIY consensus or genuine
disagreement. Two implications:

- **Don't assume a win against one agent generalizes.** A tool that's
  the default in Claude Code (e.g. Bun for JS runtime, Twilio for
  SMS/push) may be far behind in Codex, and vice versa (Cloudflare
  Workers vs. Vercel Edge for edge compute). Track your position
  separately per agent.
- **Watch for parent-company/platform affinity.** Codex shows a
  measurable lean toward OpenAI-acquired tools (Statsig) and Cloudflare;
  Claude Code shows a lean toward Anthropic-acquired tools (Bun) and
  Vercel. If you compete directly with an acquired tool or a
  platform-affiliated incumbent on a given agent, expect a structural
  headwind on that agent specifically, and weight your effort toward
  agents without that conflict.
- **Awareness isn't the bottleneck once you're mentioned as an
  alternative.** If an agent already mentions your tool at a healthy
  rate but rarely picks it primary, the fix is unlikely to be more
  training-data presence — the gap is in conversion (integration
  friction, perceived complexity, or the competing pick's structural
  advantage), not discoverability. This mirrors point 5 above, but the
  cross-agent data makes it sharper: "conversion differs much more than
  awareness does."

## 8. Design your interface to be the obvious "deferred buy"

Custom/DIY code is now naming vendors as upgrade paths inside its own
comments 32.5% of the time (e.g. "swap to Redis once multiple workers
exist") — a model builds the simple version now but pre-writes your
on-ramp. Shape your API/interface to match the shape of the DIY code a
model would write for the simple case, so switching from the hand-rolled
version to yours is a near-drop-in replacement, not a rearchitecture.
This matters most in categories with high and rising Custom/DIY rates
(Caching, Observability, Auth, Feature Flags).

## 9. If you compete against a bundled incumbent, bundle back or reframe the category

PostHog beat dedicated feature-flag competitor LaunchDarkly (0% primary
picks despite 38% mentions) by bundling flags with analytics — the
model saw one tool solving two problems instead of two tools to justify
separately. If your category is being won by a bundled adjacent
product rather than a better dedicated tool, the fix is unlikely to be
more training-data presence; consider whether your own product should
bundle an adjacent capability, or lean into positioning that reframes
the bundle as the wrong default for the user's actual case.

## 10. Know your hardcoded-integration status, separately from your model-pick status

Claude Code's own source hardcodes vendor treatment independent of any
model's judgment: a ~489-tool MCP output-rendering allowlist, 6
vendors with "claude.ai-hosted" zero-config OAuth connectors, 89
WebFetch-preapproved hosts, and a single vendor (Vercel) with a
proactive plugin-install tip. This isn't something you can train your
way into — it's an engineering/business-development decision on
Anthropic's side, and the source notes the allowlist is "entirely
manual." It's still worth checking whether a same-category competitor
already has better output rendering, OAuth onboarding, or doc-fetch
access in Claude Code for reasons unrelated to model preference — that
gap is a distinct, non-training-data disadvantage worth knowing about
even if it's not directly actionable today.

## 11. Consider serving your docs over MCP

Expose an MCP server that fronts your API/product docs so a coding agent
pulls live, task-scoped, correct references inline instead of relying on
its training cutoff or a stale crawl — directly attacking the
hallucinated/outdated-code failure mode that costs you the pick. Treat
it as a complement to clean public docs (only agents with your server
installed benefit), and judge it by whether the agent can retrieve the
*right chunk* and act on it immediately. See [[docs-over-mcp]] for the
good/bad tradeoffs and build patterns.

## See also

- [[ai-coding-agent-tool-selection]] — the underlying concept and study
  data this playbook is built on.
- [[docs-over-mcp]] — serving documentation as an agent-callable tool
  (expanded form of point 11).
- [[generative-engine-optimization]] — the broader GEO/AEO discipline;
  this playbook is its coding-agent-specific, tool-vendor-facing
  counterpart to [[geo-content-optimization-tactics]].
- [[amplifying-codex-vs-claude-code-picks-2026]] — the cross-agent
  study behind the per-agent measurement and parent-company-affinity
  guidance in point 7.
- [[amplifying-claude-code-picks-fable-2026]] — the newer-model study
  behind the deferred-buy (point 8) and bundling (point 9) tactics.
- [[amplifying-claude-code-hardcoded-vendors-2026]] — the leaked-source
  analysis behind the hardcoded-integration awareness tactic (point 10).
- [[writing-effective-agents-md-files]] — the sibling playbook for
  instructing an agent's behavior inside your own repo, rather than
  getting your product chosen by an agent working in someone else's.
