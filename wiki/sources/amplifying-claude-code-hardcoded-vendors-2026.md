---
type: source
tags: [aeo]
date_published: 2026-03-31
date_ingested: 2026-07-22
origin: raw/studies/amplifying-claude-code-hardcoded-vendors-2026.md
---

# Claude Code Hardcoded Vendor Analysis (Amplifying, Mar 2026)

**Citation:** Ong, Edwin and Vikati, Alex. "Claude Code Hardcoded
Vendor Analysis." Amplifying (agent-intelligence). Published 2026-03-31.
https://amplifying.ai/research/claude-code-hardcoded-vendors

## Key takeaways

- Distinct mechanism from every other source in
  [[ai-coding-agent-tool-selection]]: not about which tool a model
  *picks* when generating code, but which vendors receive **hardcoded
  special treatment in Claude Code's own source** — examined via leaked
  TypeScript extracted from public npm source maps, March 2026.
- **MCP UI allowlist (489 unique tool names)**: listed tools get compact
  output rendering vs. raw JSON for everyone else. Top vendors by tool
  count: GitHub (56), Grafana (38), Datadog (30), Asana (29), PagerDuty
  (28).
- **6 vendors get "claude.ai-hosted" connector status** (OAuth + proxy
  infra via `mcp-proxy.anthropic.com`): PubMed, Slack, Gmail, Google
  Calendar, BigQuery, Google Drive — zero-config onboarding vs. manual
  local MCP setup for everyone else.
- **89 hosts are preapproved for unauthenticated WebFetch** — Claude
  Code can pull these vendors' docs without the user supplying a URL.
- **29 deployment platforms get explicit telemetry detection**; 7 LLM
  API gateways get explicit fingerprinting (LiteLLM, Helicone, Portkey,
  Cloudflare AI, Kong, Braintrust, Databricks).
- **Only one third-party vendor (Vercel) gets a proactive plugin
  install tip** — triggered by detecting `vercel.json`.
- Source's own framing: "the MCP allowlist is entirely manual" — a
  scaling problem for Anthropic today, but a risk that current ad hoc
  inclusion decisions harden into a de facto ecosystem ranking that's
  much harder to contest later than an open, model-driven pick would be.

## What this updated in the wiki

- Added a new "Hardcoded platform integration is a separate visibility
  layer from model picks" section to [[ai-coding-agent-tool-selection]]
  — this is an allowlist/engineering-decision mechanism (Anthropic
  controls it directly), distinct from every training-data/prompt-based
  mechanism the concept previously covered.
- Added a corresponding (largely non-actionable, but track-worthy)
  tactic note to [[optimizing-for-coding-agent-recommendations]]: getting
  onto these allowlists isn't something a vendor can directly execute
  the way training-data presence is, but it's worth knowing whether your
  product already has better/worse integration ergonomics in Claude Code
  than a same-category competitor for reasons unrelated to model
  preference.
- No conflicts — genuinely new mechanism, first source describing
  engineering-level (not model-level) vendor treatment.
