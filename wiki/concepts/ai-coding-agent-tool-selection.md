---
type: concept
tags: [aeo]
updated: 2026-07-22
---

# AI Coding Agent Tool Selection

A sibling domain to [[generative-engine-optimization]]: instead of a
chat/search answer engine choosing which *content* to cite, a coding
agent (Claude Code and similar) chooses which *tool or library* to
recommend and install when a developer asks an open-ended question
("add a database," "how do I deploy this?") without naming a specific
product. For a tool/library vendor, "visibility" here means being the
thing the agent actually reaches for — the audience is developers using
AI coding agents, not searchers or chat users. Based on
[[amplifying-claude-code-picks-2026]] (Claude Code, 2,430 prompts, 20
categories, 3 models), [[amplifying-codex-vs-claude-code-picks-2026]]
(Codex vs. Claude Code head-to-head, 1,452 picks, 12 contested
categories), [[amplifying-claude-code-picks-fable-2026]] (newer-model
follow-up: Opus 4.8/Fable 5), and
[[amplifying-claude-code-hardcoded-vendors-2026]] (leaked-source
analysis of hardcoded vendor allowlists).

## Agents build rather than buy, often

In 12 of 20 tool categories studied, a coding agent's most common
response is to write a custom/DIY implementation rather than recommend
a third-party tool — 12% of all primary picks overall, rising to 100%
for Python authentication and 69% for feature flags. This is the
single largest "competitor" to any given tool: it's not just other
vendors, it's the agent's own code-generation capability.

## A default stack exists, where agents do pick a tool

Where third-party tools are chosen, agents converge heavily on a small
consistent set — near-monopolies in some categories (CI/CD: GitHub
Actions 93.8%; Payments: Stripe 91.4%; UI: shadcn/ui 90.1%), strong
defaults in others (Styling: Tailwind 68.4%; State: Zustand 64.8%;
Observability: Sentry 63.1%), and genuinely competitive/fragmented
markets in the rest (Auth, Caching, ORM, Background Jobs, Real-time).
Deployment, testing, and ORM choice are ecosystem-specific (Vercel vs.
Railway, Vitest vs. pytest, Drizzle vs. SQLModel) rather than one
universal winner — the agent picks contextually, not by rote.

## "Known but unpicked" is a distinct, worse state than invisible

Some tools are actively considered and then passed over every time:
Redux (0 primary picks despite 23 mentions), MongoDB (0 primary despite
30 mentions), Prisma (0 picks from the newest model tested despite
being dominant in the older model). This is a stronger negative signal
than never appearing in training data at all — the agent has evaluated
the tool and rejected it as the default. Conversely, tools with a high
*alternative*-pick rate but low primary rate (Netlify, SendGrid, Yarn,
TanStack Query in some categories) are "known and viable" — closer to
becoming the default than a tool that never surfaces.

## Recency gradient: newer models favor newer tools

Comparing successive model versions on the same prompts shows a
systematic drift toward newer tools, sometimes total: Prisma (2019)
drops from 79% pick share to 0% while Drizzle (2022) rises from 21% to
100%, across Sonnet 4.5 → Opus 4.5 → Opus 4.6. Similar shifts appear in
background-job libraries and caching choices. This implies incumbency
in an older model's training data is not durable — a tool's position
can erode purely from newer models being trained on more recent code
examples, independent of any change in the tool itself. It also implies
a feedback loop risk: newer tools get recommended more → gain adoption
→ generate more training data → get recommended even more.

## Stability varies sharply by category

Some categories are highly stable — the same tool wins regardless of
prompt phrasing or which of 3 runs you check (CI/CD, Payments,
Deployment, Databases, Authentication, API Layer). Others are
genuinely fragmented or context-sensitive (Background Jobs, Caching,
File Storage, Real-time, ORM choice) — multiple tools compete with no
clear agent-side consensus, so a vendor in one of these categories has
more room to shift the outcome than a vendor competing against a
near-monopoly incumbent.

## Build-over-buy is accelerating across model generations

[[amplifying-claude-code-picks-fable-2026]] reruns the same 20-category
methodology on newer models (Opus 4.8, Fable 5) and finds Custom/DIY
share nearly doubled from the earlier generation: 11% → 21.4% of all
picks, with Opus 4.8 independently landing at 20.5% — evidence this is
a generational trend, not one model's quirk. Caching went from 0% to
57% custom code in a single generation.

## The "deferred buy" pattern: DIY now, vendor named as the upgrade path

The same source's sharpest new finding: 32.5% of custom
implementations (53 of 163 builds studied) explicitly name an upgrade
vendor inside code comments — e.g. a hand-rolled cache documenting
"swap to Redis once multiple workers exist." The model isn't simply
choosing DIY over a vendor; it's writing DIY code today while
pre-authoring that vendor's eventual on-ramp. This reframes "known but
unpicked" (below): being named as the deferred upgrade is a *stronger*
position than being an unmentioned alternative, even at 0% primary
picks.

## Bundling can beat a dedicated best-in-category tool

In the same study, PostHog reached 27% share in Feature Flags by
bundling flags with analytics — beating dedicated competitor
LaunchDarkly, which had 0% primary picks despite a 38% mention rate.
This is a category-structure effect (does the agent see your feature as
a package deal or a standalone tool it has to justify separately), not
a pure quality or training-data-presence question.

## Provider vs. technology is a distinct axis models track separately

Models distinguish an underlying technology choice from a
hosting/provider choice: PostgreSQL wins "which database technology,"
while Neon, Supabase, and RDS appear only as deployment-time provider
options rather than competitors to Postgres itself
([[amplifying-claude-code-picks-fable-2026]]). A provider-tier vendor
should benchmark against other providers, not against the underlying
technology's adoption rate.

## Hardcoded platform integration is a separate visibility layer from model picks

Everything above concerns which tool a *model* recommends when
generating code — a training-data/prompting dynamic. A different,
engineering-controlled mechanism also determines vendor treatment:
Claude Code's own source code hardcodes vendor-specific allowlists,
independent of any model's judgment
([[amplifying-claude-code-hardcoded-vendors-2026]], leaked-source
analysis, Mar 2026):

- **489 tools get compact MCP output rendering** via a hardcoded
  allowlist (`SEARCH_TOOLS`/`READ_TOOLS`); everything else renders as
  raw JSON.
- **6 vendors get "claude.ai-hosted" OAuth connector status**
  (zero-config onboarding) vs. manual local MCP setup for everyone
  else.
- **89 hosts are preapproved for unauthenticated WebFetch**, letting
  Claude Code pull their docs without the user supplying a URL.
- Only **one third-party vendor (Vercel)** gets a proactive plugin
  install tip.

This is a fundamentally different lever than everything else on this
page: it's not about training data, prompting, or default-stack
convergence — it's a direct engineering decision by Anthropic, and the
source notes the allowlist is "entirely manual," meaning today's
inclusions could harden into a de facto ranking that's much harder to
contest later than a model-driven preference would be.

## Different agents pick differently — and it correlates with parent company

Comparing Codex (OpenAI/GPT-5.3) against Claude Code (Anthropic/Opus
4.6) head-to-head on 12 contested categories (search, secrets, rate
limiting, edge compute) finds agreement on only 7 of 12 top picks — and
6 of those 7 are agreement on Custom/DIY, not a named tool. Where they
diverge, the pattern often lines up with each agent's parent company:
Codex picks OpenAI-acquired **Statsig** as primary in 27% of feature-
flag responses vs. Claude's 0% (despite Claude *mentioning* Statsig
28% of the time); Claude picks Anthropic-acquired **Bun** as primary
63% of the time for JS runtime vs. Codex's 13% (despite Codex
mentioning Bun 73% of the time). Beyond the two acquired-tool cases,
both agents show broader platform affinity: Codex leans Cloudflare (47
Cloudflare-branded picks vs. Claude's 9), Claude leans Vercel (29
Vercel-branded picks vs. Codex's 17).

The researchers are careful to frame this as **correlation, not proven
causation** — an acquired tool may already have been best-in-class,
which is presumably why it got acquired. But the sharper finding is
about *awareness vs. conversion*: both agents mention the same
competing tools at similar rates, yet convert to a primary pick at very
different rates ("conversion differs much more than awareness does").
Being mentioned by a coding agent is not the same as being chosen by
it, and which one happens seems to depend partly on which company built
the agent.

## Practical relevance

This is a build-vs-buy and default-stack dynamic, not a citation/
ranking dynamic — closer to "which library does the agent `npm
install`" than "which page does the agent quote." See
[[optimizing-for-coding-agent-recommendations]] for the resulting
vendor-facing tactics.

## See also

- [[generative-engine-optimization]] — the broader GEO/AEO concept this
  is a sibling of: visibility inside an AI-generated answer, for a
  different engine type (coding agent vs. chat/search) and audience
  (tool vendors vs. content publishers).
- [[optimizing-for-coding-agent-recommendations]] — actionable tactics
  drawn from this concept.
- [[amplifying-codex-vs-claude-code-picks-2026]] — the Codex-vs-Claude-
  Code cross-agent comparison underlying the parent-company/platform-
  affinity findings above.
- [[amplifying-claude-code-picks-fable-2026]] — the newer-model
  follow-up behind the accelerating-build-over-buy, deferred-buy, and
  provider-vs-technology findings above.
- [[amplifying-claude-code-hardcoded-vendors-2026]] — the leaked-source
  analysis behind the hardcoded-allowlist findings above.
- [[agentic-web-optimization]] — a sibling domain: general-purpose AI
  agents acting on marketing/ecommerce sites, rather than coding agents
  choosing tools/libraries.
- [[agents-md-instruction-files]] — a different coding-agent layer:
  how a repo owner instructs the agent's *behavior* inside their own
  repo (commands, boundaries, style), rather than which third-party
  tool/library the agent picks.
