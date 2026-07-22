---
type: concept
tags: [aeo]
updated: 2026-07-22
---

# agents.md Instruction Files

A distinct layer from [[ai-coding-agent-tool-selection]]: rather than a
coding agent choosing *which third-party tool/library* to reach for,
`agents.md` (and equivalents like `CLAUDE.md`, `.github/copilot-instructions.md`)
is a repo-owned file that instructs the agent on **how to operate inside
that specific repository** — commands to run, boundaries to respect,
code style to match. This is the mechanism by which a maintainer shapes
agent *behavior*, not agent *preference between vendors*. Based on
[[github-blog-writing-great-agents-md]], an analysis of 2,500+ public
`agents.md` files.

## Specificity is the dividing line

Across the 2,500+ files analyzed, there's a clear split between vague
agents that fail ("a helpful coding assistant") and specialist agents
that succeed. The gap is precision, not length — a short, specific file
outperforms a long, generic one.

## Six essential coverage areas

Effective files consistently cover: **commands** (exact, executable,
with flags — `pytest -v`, not "run the tests"), **testing practices**,
**project structure**, **code style** (one real code snippet beats a
paragraph of description), **git workflow**, and **operational
boundaries**.

## Boundaries work best as three tiers, not a flat list

The most effective boundary framing splits into **always do / ask first
/ never do**, rather than one undifferentiated list of restrictions.
"Never commit secrets" is the single most common beneficial boundary
found across the corpus; other common never-touch targets are vendor
directories and production configs.

## Specificity extends to the tech stack description itself

"React project" is not specific enough to be useful; "React 18 with
TypeScript, Vite, and Tailwind CSS" is. Naming exact versions and key
dependencies lets the agent match idiom and avoid deprecated patterns.

## A taxonomy of specialist agents, not one general agent

The source proposes splitting responsibilities across narrow specialist
agents rather than one broad one — illustrated with six archetypes
(`@docs-agent`, `@test-agent`, `@lint-agent`, `@api-agent`,
`@dev-deploy-agent`, plus organization-specific ones), each scoped to a
narrow blast radius (e.g. `@docs-agent` writes only to `docs/`, never
`src/`). This mirrors a general operational-security principle: narrower
write scope per agent reduces the cost of a mistake.

## Build iteratively, not comprehensively upfront

Recommended starting point is one task and three essentials (name,
description, persona), then iterate — "the best agent files grow through
iteration, not upfront planning." This contrasts with treating
`agents.md` as a one-time comprehensive spec to get right on day one.

## Getting it wrong has a quantified cost, not just a vague one

[[aaron-gustafson-optimizing-codebase-for-ai-agents]], a first-hand case
study of watching GitHub Copilot's autonomous agent work a real task,
puts numbers behind the abstract "be specific" guidance above: scattered,
inconsistent docs cost the agent ~40% of its time just deciding what to
trust; unaddressed edge cases caused 15+ minutes of token-burning
deliberation over a single ambiguous case. After consolidating docs and
documenting edge cases, the reported deltas were ~40% less processing
time, ~75% less token usage, and >80% less circular reasoning (early,
single-case-study numbers — not a controlled study, but directionally
consistent with the specificity-divide finding above).

## Two tactics beyond specificity: one source of truth, and agent-proof validation

The same source adds two mechanisms not covered by the specificity/
boundaries/taxonomy framing above:

- **Consolidate to one authoritative doc source.** Scattered
  instructions across workflow comments, READMEs, and task-specific
  guides create contradictions an agent can't resolve on its own;
  deprecated docs should redirect rather than sit live alongside the
  current version.
- **Don't rely on the agent to pick an efficient validation step.**
  Left to its own judgment, an agent may run an expensive full build to
  check something trivial (e.g. markdown formatting). Purpose-built,
  narrow validation scripts — with explicit instructions on when to use
  them — avoid this.

## Practical relevance

This is a repo-operations concern, not a citation/visibility dynamic —
closer to "how reliably does the agent edit my code the way I want" than
"does the agent recommend my product." See
[[writing-effective-agents-md-files]] for the resulting checklist.

## See also

- [[writing-effective-agents-md-files]] — actionable checklist drawn
  from this concept.
- [[ai-coding-agent-tool-selection]] — the sibling concept for the
  *other* coding-agent layer: which third-party tool/library an agent
  recommends, rather than how it behaves inside your own repo.
- [[github-blog-writing-great-agents-md]] — the underlying source for
  the specificity/boundaries/taxonomy findings above.
- [[aaron-gustafson-optimizing-codebase-for-ai-agents]] — the source for
  the quantified-cost, doc-consolidation, and validation-tooling points
  above.
