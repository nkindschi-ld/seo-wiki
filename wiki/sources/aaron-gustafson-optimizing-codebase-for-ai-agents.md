---
type: source
tags: [aeo]
date_published: 2025-10-21
date_ingested: 2026-07-22
origin: raw/articles/aaron-gustafson-optimizing-codebase-for-ai-agents.md
---

# Optimizing Your Codebase for AI Coding Agents (Aaron Gustafson)

**Citation:** Gustafson, Aaron. "Optimizing Your Codebase for AI Coding
Agents." Personal notebook. Published 2025-10-21.
https://www.aaron-gustafson.com/notebook/optimizing-your-codebase-for-ai-coding-agents/

## Key takeaways

- First-hand case study of watching **GitHub Copilot's autonomous
  agent** work a real task: most friction traced to organizational/
  documentation problems, not code problems.
- **Documentation sprawl** cost ~40% of the agent's time deciding which
  of several scattered, inconsistent docs (workflow comments, READMEs,
  task guides) to trust. Fix: one authoritative source, deprecated docs
  redirected rather than left live.
- **Agents default to expensive validation** — the agent ran a full
  30-60s production build (image processing, template compilation) just
  to check markdown formatting. Fix: purpose-built, narrow validation
  scripts with explicit instructions on when to use them, instead of
  relying on the agent to pick an efficient check itself.
- **Unaddressed edge cases cause token-burning deliberation** — the
  agent spent 15+ minutes reasoning about whether to process test-form
  submissions with no documented answer. Fix: a dedicated section
  covering that specific edge case.
- Frames the root cause as **implicit assumptions** agents can't
  navigate — the fix in all three cases is making tacit knowledge
  explicit, not smarter prompting.
- Reports concrete before/after deltas: **~40% less processing time,
  ~75% less token usage, >80% less circular reasoning/confusion** after
  the fixes (early/self-reported, single case study — not a controlled
  study).
- Core claim: "optimizing for AI agents isn't really about AI... it's
  about removing ambiguity, eliminating redundancy, and making implicit
  knowledge explicit" — frames it as good engineering practice that
  also helps humans, not an AI-specific discipline.

## Relevance to this wiki

Extends [[agents-md-instruction-files]] rather than conflicting with
it: the GitHub Blog source ([[github-blog-writing-great-agents-md]])
establishes *what* a good instruction file contains (specificity,
boundaries, commands); this source adds *quantified stakes* for getting
it wrong (real time/token costs) and two tactics not previously covered
— consolidating to one authoritative doc source (vs. scattered/stale
docs) and building narrow validation scripts instead of trusting the
agent to pick an efficient check. Added both as new points to
[[agents-md-instruction-files]] and [[writing-effective-agents-md-files]].
No conflicts.
