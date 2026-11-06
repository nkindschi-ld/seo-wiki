---
type: concept
tags: [aeo, seo]
updated: 2026-10-08
---

# Agent Experience (AX)

**AX (agent experience)** is whether a buyer's AI agent can **find,
read, and verify** your own website while researching a question on a
user's behalf. The term comes from [[ora-ax-is-the-new-aeo-2026]], which
frames it as the successor to off-site-seeding AEO: **"AEO is now SEO
plus AX."** SEO decides whether agents find you; AX decides whether
they can reach, read, and use your site, and therefore what the answer
says about you.

AX sits inside [[agentic-web-optimization]]. It is that concept's
"agent readiness" layer (plus the crawlability floor beneath it), but
with a measured outcome attached. Agentic-web optimization's endpoint
is a completed action. AX's endpoint is an *accurate, confident
recommendation* built from your own pages. The agentready.org spec
that ora points to splits readiness into **find / read / act**, so AX
spans both.

## Why it matters now: answers are grounded, not remembered

Per [[ora-ax-is-the-new-aeo-2026]]:

- Training knowledge supplies only **7–10%** of a finished answer in
  current agent models (vs ~50% for gpt-4.1, the last non-reasoning
  OpenAI flagship). Stable facts still come from memory, but pricing,
  setup, and comparison questions need current information, and in
  agent harnesses fetching is the default.
- External corroboration cited by the study: frontier models invoke
  search ~88–94% of the time on recency-dependent questions; ChatGPT
  searches anchored to the current year went from ~6% (GPT-5.2) to 87%
  (GPT-5.5).
- From **Aug 8, 2026**, `site:` queries went from ~0% to 23–24% of
  ChatGPT's background searches, aimed at official sites instead of
  discussion threads. Reddit's share of ChatGPT citations fell ~86% in
  a week (Promptwatch; Qwairy measured 95% on its own panel) and has
  only partly recovered (~1.5%).

This is the same static → search-augmented → reasoning-with-search
progression described in [[generative-engine-optimization]], now
quantified at the answer-composition level.

## What happens when an agent can't read you

| Finished-answer composition | Your pages | External sites | Web search | Training |
|---|---|---|---|---|
| Agent-ready site | 78% | 3% | 12% | 7% |
| Not agent-ready | 58% | 7% | 25% | 10% |

- **Agents don't give up.** In ~99% of journeys that hit a dead end
  (403, block, unreadable page), the agent answered anyway from other
  sources. Web searches per run rise 2.6× from the most to the least
  readable sites, and every extra search is a chance to pick up
  competitors' pages, stale mirrors, or aggregator write-ups.
- **The answer gets hollow, not wrong.** Off-site answers are 3.7× more
  likely to contain none of the facts the buyer asked for (25% vs 7%).
  Wrong facts stay rare (4% vs 6%), but "never mentioned" rises from
  29% to 45%. These answers read fluently, so hallucination metrics and
  AEO visibility dashboards don't flag them. This matches the
  omission-dominant failure pattern in
  [[ai-overview-grounding-and-fidelity]], now seen on agent harnesses
  as well as AI Overviews.
- **The recommendation weakens.** A clear endorsement occurs 20% vs
  11% of the time (1.9×, matched on brand fame, prior model knowledge,
  and off-site citation breadth). The lift is up to 2.6× by stack, and
  2.5× in IT infrastructure, 2.3× in sales & marketing. The hedges
  that grow most: "couldn't access the site" (4.4×), vouching via
  aggregators instead of the business (3.0×), vague no-specifics
  endorsement (1.8×), "contact sales" punts (1.4×).

### Where own-site reading pays (and where it doesn't)

- **Pricing** has one fresh source, your own pages: 60% accuracy when
  read from the site vs 37% from elsewhere.
- **Features**: 46% vs 39%.
- **Setup**: 24% either way. Two-thirds of setup facts never surface
  at all. What moves setup is *findability*: sites where agents could
  ground setup answers scored 31% vs 18% from both sources.
- Overall, accuracy climbs from 41% to 56% as the share of evidence
  read from the business's own pages rises.

## The operator-cost argument

Blocked or unreadable sites make agent runs more expensive: 23% more
turns, 2.1× more blocks, 15% longer, and only 56% of runs end grounded
in the business (vs 78%). Cost per grounded answer is +64% on average
and up to +93% on some stacks. The study's inference, not yet measured,
is that harness builders have an economic incentive to route around
sites that behave this way. Compare [[robots-txt-strategy]]: blocking
AI agents isn't just a visibility trade-off. It shifts the answer onto
third-party evidence you don't control.

## The next shift: connectors and registries (unmeasured)

Every journey in the study began with search → your site. The authors
flag that assistants are building their own front doors to businesses:

- **Agentic Resource Discovery (ARD)**, a draft open spec (June 2026)
  from Microsoft, Google, and Hugging Face with GitHub, Snowflake and
  others. Agents search a registry for tools, MCP servers, and other
  agents before calling anything.
- **ChatGPT plugin directory**, which replaced the app directory as of
  July 9, 2026.
- **Meta Muse** (launched Sep 8, 2026) uses a service's API/connector
  when one exists and a browser only when none does. When Amazon
  blocked Muse, Shopify merchants stayed reachable through a declared
  Shop Pay checkout path.

If assistants check connectors first, the web becomes the fallback and
AX's "find" layer expands to include the assistant's own catalog. This
extends [[agentic-web-optimization]]'s protocol layer (MCP, WebMCP,
ACP, UCP). The authors explicitly haven't measured it yet.

## Practical relevance

See [[optimizing-for-the-agentic-web]]'s "Unblock and verify" section
for the actionable checklist. [[technical-seo-audit-checklist]] covers
the crawlability floor.

## Conflicting Evidence

- **Claim**: Off-site presence (brand mentions, YouTube, Reddit
  threads, third-party listicles, co-occurrence seeding) is the
  strongest lever for AI visibility.
  - Supported by: [[ahrefs-ai-brand-visibility-correlations]]
    (correlation study; YouTube ~0.737 and branded web mentions
    0.656–0.709 as the top factors), plus the co-occurrence tactic in
    [[malte-landwehr-llmo-geo-aio-guide]] (Jan 2024).
  - Contradicted by: [[ora-ax-is-the-new-aeo-2026]] (2026-10-08). With
    off-site citation breadth and brand fame held equal, own-site
    readability alone produced a 1.9× recommendation gap. The authors
    argue off-site tactics "lose leverage each time agents go to the
    source."
  - **Current best guess**: these mostly measure different things.
    The correlation data measures brand *mentions* in chat answers; ora
    measures *recommendation strength and accuracy* from agents doing
    live buyer research. Off-site presence likely still drives whether
    you're surfaced and named. Own-site readability decides how
    strongly and accurately you're recommended once an agent is
    researching you. Leaning: treat both as necessary, and weight
    own-site readability higher for commercial, agent-driven queries
    (pricing, features, comparisons). The ora study is a single
    vendor-run study whose readiness score is proprietary. **Flagged
    unresolved.**

## See also

- [[agentic-web-optimization]] — parent domain (the five-layer stack
  and protocol standards).
- [[optimizing-for-the-agentic-web]] — actionable checklist.
- [[ai-overview-grounding-and-fidelity]] — the same omission-dominant
  failure, measured on Google AI Overviews.
- [[ai-citation-landscape]] — citation-source mix, including the
  pre-August-2026 Reddit data this source suggests is now dated.
- [[ai-visibility-correlation-factors]] — the off-site correlation
  data in tension with this concept.
- [[robots-txt-strategy]] — controls that can accidentally make a site
  not agent-ready.
- [[ai-coding-agent-tool-selection]] — a sibling agent-choice domain
  (coding agents picking tools).
