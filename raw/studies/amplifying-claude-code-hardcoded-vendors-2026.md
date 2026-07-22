# Claude Code Hardcoded Vendor Analysis (Amplifying, Mar 2026)

**Authors:** Edwin Ong & Alex Vikati
**Publisher:** Amplifying / agent-intelligence
**Date:** March 31, 2026
**URL:** https://amplifying.ai/research/claude-code-hardcoded-vendors

## Methodology

Researchers examined Claude Code's leaked TypeScript source, extracted
from publicly available npm source maps in March 2026, searching
systematically across seven distinct codebase sections for hardcoded
vendor/tool references. Published by the authors "for educational and
research purposes."

## Key findings

1. **MCP UI allowlist — 489 unique tool names.** `classifyForCollapse.ts`
   hardcodes two Sets (SEARCH_TOOLS, READ_TOOLS) totaling 495 typed
   entries → 489 unique normalized tool names. Listed tools get compact
   output rendering; unlisted tools render as raw JSON. Top vendors by
   tool count: GitHub (56), Grafana (38), Datadog (30), Asana (29),
   PagerDuty (28).
2. **Claude.ai-hosted connectors — 6 explicit labels.** Six vendors get
   a special "claude.ai-hosted" designation with OAuth and proxy
   infrastructure through `mcp-proxy.anthropic.com`: PubMed (24
   entries), Slack (13, with custom OAuth error handling), Gmail (6),
   Google Calendar (6), BigQuery (6), Google Drive (3). Datadog's status
   is ambiguous due to conflicting source comments.
3. **WebFetch preapproval — 89 host entries.**
   `Tools/WebFetchTool/preapproved.ts` lists 89 preapproved hosts (88
   unique scopes) for unauthenticated GET requests, spanning languages,
   frameworks, cloud platforms, and databases — letting Claude Code
   fetch their docs without the user supplying a URL.
4. **Environment detection — 29 explicit platform labels.**
   `utils/env.ts` detects 29 deployment platforms for telemetry: cloud
   (Codespaces, Gitpod, Replit, Vercel, AWS Lambda, GCP Cloud Run),
   CI/CD (GitHub Actions, GitLab CI, CircleCI, Buildkite), orchestration
   (Kubernetes, Docker).
5. **Secret scanner — 36 rules across 23 credential families.**
   `services/teamMemorySync/secretScanner.ts` has 36 high-confidence
   regex rules preventing API-key leakage into team memory, covering
   AWS, GCP, Azure, Anthropic, OpenAI, GitHub, Stripe, and others.
6. **API gateway detection — 7 gateways.** `services/api/logging.ts`
   fingerprints traffic through LiteLLM, Helicone, Portkey, Cloudflare
   AI, Kong, Braintrust, and Databricks via headers/hostnames.
7. **Plugin tips — 1 third-party vendor.** Only Vercel gets a dedicated
   plugin-installation tip when `vercel.json` is detected; the only
   other entry is Anthropic's own frontend-design plugin.

## Implications (source's framing)

- **Inclusion advantages:** clean output rendering, zero-config OAuth
  onboarding, preapproved documentation fetching, visible platform
  telemetry, named credential-pattern protection, proactive plugin
  recommendations.
- **Exclusion disadvantages:** raw JSON output, manual local MCP
  configuration, no opportunistic doc access, invisible telemetry,
  generic (not vendor-named) credential detection, no automatic
  discovery.
- The report notes "the MCP allowlist is entirely manual," flagging both
  a scaling problem for Anthropic and a risk that today's ad hoc
  inclusions harden into a de facto ecosystem ranking.
