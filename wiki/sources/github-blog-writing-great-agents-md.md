---
type: source
tags: [aeo]
date_published: 2025-11-19
date_ingested: 2026-07-21
origin: raw/articles/github-blog-writing-great-agents-md.md
---

# How to Write Great agents.md Files (GitHub Blog)

**Citation:** Nigh, Matt. "How to Write a Great agents.md: Lessons from
Over 2,500 Repositories." GitHub Blog. Published 2025-11-19, updated
2025-11-25.
https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/

## Key takeaways

- Analysis of **2,500+ public `agents.md` files** finds a clear split
  between vague agent definitions that fail and specific "specialist"
  definitions that succeed.
- Five characteristics distinguish effective files: prominent
  executable commands (with flags, e.g. `pytest -v`, not just tool
  names), a single real code example over lengthy prose descriptions,
  explicit boundaries (never-touch files/dirs — "never commit secrets"
  is the single most common beneficial constraint), specific tech-stack
  descriptions with versions ("React 18 with TypeScript, Vite, and
  Tailwind CSS" vs. "React project"), and coverage of **six essential
  areas**: commands, testing practices, project structure, code style,
  git workflow, and operational boundaries.
- Recommends a **three-tier boundary framework** (always do / ask first
  / never do) rather than a flat list of restrictions.
- Proposes six specialist agent archetypes as a starting taxonomy:
  `@docs-agent` (docs only, never touches `src/`), `@test-agent` (never
  removes failing tests without authorization), `@lint-agent`
  (low-risk, auto-fixable), `@api-agent` (can modify routes, asks before
  schema changes), `@dev-deploy-agent` (dev-only, requires approval for
  anything risky) — framed as illustrative, not exhaustive.
- Implementation guidance favors starting minimal (one task, three
  essentials: name/description/persona) and iterating, over comprehensive
  upfront planning — "the best agent files grow through iteration, not
  upfront planning." Suggests using Copilot itself to draft an initial
  `agents.md` by specifying testing focus, directory restrictions, and
  boundaries in the prompt.

## Relevance to this wiki

This source is about a different layer than [[ai-coding-agent-tool-selection]]:
that concept covers how a coding agent picks *which third-party tool/library*
to use in generated code. This source instead covers how a **repository
owner instructs the coding agent working inside their own repo** — i.e. how
well-specified operating instructions change agent behavior and reliability
when it edits your codebase. Filed as a new pairing:
[[agents-md-instruction-files]] (concept) and
[[writing-effective-agents-md-files]] (playbook).
