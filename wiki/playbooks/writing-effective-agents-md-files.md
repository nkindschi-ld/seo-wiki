---
type: playbook
tags: [aeo]
updated: 2026-07-22
---

# Writing Effective agents.md Files

Why/when to use this: apply when setting up or revising an `agents.md`
(or `CLAUDE.md` / `.github/copilot-instructions.md`) file so a coding
agent operates reliably and safely inside your repository. Based on
[[agents-md-instruction-files]] /
[[github-blog-writing-great-agents-md]] /
[[aaron-gustafson-optimizing-codebase-for-ai-agents]].

## 1. Replace vague role descriptions with specifics

Don't write "a helpful coding assistant." Name the specific expertise
area and output focus (e.g. "converts code into API documentation and
tutorials, writing only to `docs/`"). Specificity, not length, is what
separates effective files from ineffective ones in the 2,500-repo
analysis.

## 2. Put exact, executable commands up front

List real commands with flags — `pytest -v`, `npm run lint --fix`, not
just "run tests" or "use the linter." An agent that has to guess the
right invocation will guess wrong more often than one that's told
exactly what to run.

## 3. Show one real code example instead of describing style in prose

A single representative snippet of your actual code style outperforms a
paragraph explaining formatting conventions. Pull it from the repo
itself, not a generic example.

## 4. Name your tech stack with versions, not categories

"React 18 with TypeScript, Vite, and Tailwind CSS," not "React project."
Version specificity prevents the agent from reaching for deprecated
APIs or a different ecosystem's idioms.

## 5. Structure boundaries as three tiers

- **Always do**: things the agent should default to (e.g. run the test
  suite before finishing, follow the existing lint config).
- **Ask first**: changes that need a human sign-off (schema changes,
  new dependencies, deleting files).
- **Never do**: hard stops. "Never commit secrets" is the most common
  and most broadly useful never-do rule; also commonly: never touch
  vendor/build-output directories, never modify production config,
  never remove a failing test without authorization.

## 6. Split broad responsibility into narrow specialist agents

Rather than one `agents.md` trying to cover every task, consider
scoping distinct agents to narrow write-domains so a mistake in one has
a small blast radius:

- `@docs-agent` — writes only to `docs/`, never `src/`.
- `@test-agent` — writes tests; never removes a failing test without
  explicit authorization.
- `@lint-agent` — auto-fixable style/formatting only, low risk.
- `@api-agent` — can modify routes; must ask before schema changes.
- `@dev-deploy-agent` — dev/local deploys only; anything with production
  risk requires approval.

Treat this as a starting taxonomy, not a fixed list — define the
specialists your own repo actually needs.

## 7. Start minimal and iterate

Don't try to write a comprehensive spec on day one. Start with one
concrete task and three essentials (agent name, description, persona),
test it against real usage, and expand from there — "the best agent
files grow through iteration, not upfront planning."

## 8. Use the coding agent itself to draft the first version

Prompt your coding agent to generate an initial `agents.md`, explicitly
stating testing focus, directory restrictions, and modification
boundaries in the prompt, then review and tighten the draft rather than
starting from a blank file.

## 9. Consolidate documentation to a single authoritative source

Scattered instructions across workflow comments, READMEs, and
task-specific guides create contradictions an agent has no way to
resolve — it will burn time (one case study reported ~40%) just
deciding which doc to trust. Pick one authoritative source and make
deprecated docs redirect to it rather than leaving stale copies live.

## 10. Give the agent purpose-built validation scripts, don't let it guess

Left unguided, an agent will reach for the most obviously-available
check even when it's overkill — e.g. running a full 30-60s production
build to validate markdown formatting. Write narrow, task-specific
validation scripts and tell the agent explicitly when to use each one,
rather than trusting it to find the efficient path itself.

## See also

- [[agents-md-instruction-files]] — the underlying concept and study
  data this playbook is built on.
- [[aaron-gustafson-optimizing-codebase-for-ai-agents]] — case-study
  source for points 9-10 and the quantified time/token-cost stakes.
- [[optimizing-for-coding-agent-recommendations]] — the sibling
  playbook for the other coding-agent layer: getting *your product*
  chosen by a coding agent, rather than instructing an agent inside
  your own repo.
