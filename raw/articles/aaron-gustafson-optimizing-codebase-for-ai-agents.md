# Optimizing Your Codebase for AI Coding Agents

**By Aaron Gustafson | Published 21 Oct 2025 | 3 min read**
**URL:** https://www.aaron-gustafson.com/notebook/optimizing-your-codebase-for-ai-coding-agents/

## Main Article Content

Gustafson shares findings from experimenting with GitHub Copilot as an
autonomous agent. While watching the agent work through a task, he
discovered that most difficulties stemmed from organizational and
documentation problems rather than code issues themselves.

### Key Findings

**1. Documentation sprawl is an efficiency killer**

The agent spent approximately 40% of its time determining which
documentation to trust. Instructions were scattered across workflow
comments, README files, and task-specific guides with inconsistencies
and contradictions. The solution involved establishing a single
authoritative source, consolidating all information into one
comprehensive guide, and redirecting deprecated documentation.

**2. Agents won't optimize themselves**

The agent ran full production builds — including image processing and
template compilation — merely to validate markdown formatting,
consuming 30-60 seconds per validation. Rather than requiring
comprehensive builds for simple checks, Gustafson implemented focused
validation scripts with explicit instructions for their use.

**3. Ambiguity breeds confusion (and wasted tokens)**

The agent spent over 15 minutes deliberating whether to process test
data, lacking clear edge case guidance. Adding a dedicated section
addressing test form submissions resolved this issue.

### Root Cause

All three issues trace back to implicit assumptions that AI agents
cannot navigate. They require explicit instructions, clear boundaries,
and unambiguous inputs.

### Results

After implementing changes, early testing confirmed:
- Approximately 40% reduction in processing time
- Approximately 75% reduction in token usage
- Greater than 80% reduction in confusion and circular reasoning

### Core Insight

"Optimizing for AI agents isn't really about AI. It's about removing
ambiguity, eliminating redundancy, and making implicit knowledge
explicit."

These improvements benefit humans too — better documentation, faster
tools, and clearer processes. Gustafson argues this represents good
engineering practices applicable beyond AI agent optimization.
