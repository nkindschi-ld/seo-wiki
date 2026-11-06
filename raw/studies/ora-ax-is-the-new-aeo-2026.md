# AX is the New AEO

Source: https://ora.ai/blog/ax-is-the-new-aeo
Paper: arXiv:2609.34951 — Finder, I., Elovic, A., Shalev, G., & Yosef, L. (2026). "AX is the New AEO." ora research (era labs).
Data/code: https://github.com/ora/research/tree/main/ax-is-the-new-aeo
Published (blog): 2026-10-08 (paper dated September 2026)
Captured: 2026-10-08 (structured notes + data points from the blog post; not a verbatim copy)

Vendor note: ora sells the agent-readiness ranker ("ora accessibility score", 100+ checks) used to split the sample, and is
associated with the agentready.org "Agent Readiness Standard" (find / read / act). Treat as vendor-run research with
released data and a matched-pair design.

## Thesis

- 2023-era AEO = seeding what models learned in training (Reddit threads, listicles, citations on other sites).
- Claim: in August 2026 that playbook "broke" — ChatGPT began querying official sites directly via `site:` searches.
- AX (agent experience) = whether a buyer's agent can **find, read, and verify** your own site.
- Conclusion: "AEO is now SEO plus AX." SEO governs how you surface in search; AX decides what the answer says about you.

## Study design

- 1,056 live business sites; 37,927 agent journeys; 140,000+ page fetches; each journey in an isolated environment.
- 4 harnesses: claude-agent-sdk (claude-sonnet-4-6), claude-code (claude-haiku-4-5), openclaw (gpt-5.4-mini), eve (gpt-5.4).
  GPT stacks searched via Tavily; Claude stacks used built-in search.
- Real buyer questions (pricing, features, setup, comparisons, "what can I try for free?").
- Sites scored for agent readiness on 2026-08-24; journeys ran late Aug–Sep 2026.
- Matched pairs: each agent-ready business paired with a not-agent-ready one in the same industry, matched on brand fame,
  model's prior knowledge of the brand, and off-site citation breadth (measured via Tavily). Groups indistinguishable on all
  three → the 1.9× recommendation gap is presented as the controlled number.
- Ambiguous middle band of readiness scores (0.50–0.65) excluded by design.
- Recommendation strength judged by two blind judges (Claude and GPT); "clear endorsement" requires both to give top grade;
  judges agree within a point on 88%.
- Accuracy: 31,127 asked facts across 2,499 answers from a sample of 131 businesses, graded vs ground truth captured from each
  business's own site.

## 00 — Shift toward grounding (training data share)

- Same buyer questions put to each OpenAI generation since gpt-4.1 (630 runs, 90 questions per generation, web tools optional).
- gpt-4.1 (last non-reasoning flagship) built ~half its answer from memory; in today's agent models training knowledge
  supplies 7–10% of the answer.
- Supporting public signals cited:
  - "Look It Up" (Kale, arXiv:2511.18931, v2 Aug 2026): on recency-dependent questions, search invocation 91.0% (Claude Haiku
    4.5), 93.9% (Claude Sonnet 4.6), 87.5–92.1% (GPT-5-mini/GPT-5); end-to-end accuracy still caps ~66–71%.
  - TUM & maestra.ai (1,650 runs, 370k results): share of ChatGPT Business-tier searches anchored to current year —
    GPT-5.2 ~6%, GPT-5.3 53%, GPT-5.5 87% (Plus tier 60% / 79%).
  - Promptwatch (Aug 2026, provisional): Reddit share of ChatGPT Search citations 3.83% (Jul 18–Aug 7) → 0.52% (Aug 14–17),
    an ~86% drop; trailing share since recovered to ~1.5%.
  - Qwairy (Aug 2026): `site:` queries rose from ~0% to 23–24% of ChatGPT background searches starting Aug 8, 2026,
    redirecting citations from discussion platforms to official sites; Qwairy measured a 95% Reddit-citation collapse on its
    own fixed brand panel (different panel/window from Promptwatch's 86%).
- Caveat stated by authors: models don't search on everything — stable facts still come from memory; pricing, setup and
  comparison questions need current info, and in agent harnesses fetching is the default.

## 01 — Trace example

- Same question ("what can I try for free?"), same harness (claude-agent-sdk / sonnet-4-6): twilio.com answered from its own
  docs; hashicorp.com blocked the agent twice and the journey ended on two competitors' blogs.

## 02 — Recommendation

- Clear endorsement (both judges): agent-ready 20% vs not agent-ready 11% → 1.9×.
- "Too weak to recommend" answers 2.5× more common when site not agent-ready.

| Category | Ready | Not ready | Lift |
|---|---|---|---|
| IT Infrastructure | 24% | 9% | 2.5× |
| Sales & Marketing | 21% | 9% | 2.3× |
| Artificial Intelligence | 23% | 10% | 2.2× |
| Development | 32% | 14% | 2.2× |

| Stack | Ready | Not ready | Lift |
|---|---|---|---|
| claude-code / haiku-4-5 | 5% | 2% | 2.6× |
| claude-agent-sdk / sonnet-4-6 | 14% | 5% | 2.6× |
| openclaw / gpt-5.4-mini | 25% | 14% | 1.8× |
| eve / gpt-5.4 | 36% | 20% | 1.8× |

Hedge patterns (ready vs not ready):

| Hedge | Ready | Not ready | Ratio |
|---|---|---|---|
| Admits it couldn't access info (e.g. "site returned 403") | 4% | 16% | 4.4× |
| Vouches from secondhand sources (aggregators) | 5% | 15% | 3.0× |
| Vague endorsement (no concrete prices/steps/links) | 7% | 12% | 1.8× |
| Punts user to check themselves ("contact sales") | 15% | 22% | 1.4× |

## 03 — Grounding (composition of finished answer)

| | Your pages | External | Web search | Training knowledge |
|---|---|---|---|---|
| Agent-ready | 78% | 3% | 12% | 7% |
| Not agent-ready | 58% | 7% | 25% | 10% |

- In ~99% of journeys that hit a dead end on a site, the agent answered anyway from other sources.
- Web searches per run rise 2.6× from most- to least-readable sites.
- Search reliance is stack-specific (openclaw navigates by search ~6.9–10.4/run; claude-code barely searches 0.1–0.3/run),
  but losing readability pushes every stack and category the same direction.

| Stack (web searches/run) | Ready | Not ready | Lift |
|---|---|---|---|
| claude-agent-sdk | 0.4 | 0.9 | 2.4× |
| claude-code | 0.1 | 0.3 | 3.5× |
| openclaw | 6.9 | 10.4 | 1.5× |
| eve | 1.2 | 1.9 | 1.6× |

## 04 — Cost & performance

- Not-agent-ready runs: 23% more turns (5.5 → 6.8), blocked 2.1× as often, 15% longer (48s → 55s).
- Only 56% of runs on not-agent-ready sites end with an answer grounded in the business vs 78% on agent-ready.
- Cost per grounded answer +64% averaged across stacks:
  - openclaw +93% ($0.135 → $0.260); claude-agent-sdk +93% ($0.112 → $0.216); claude-code +57% ($0.020 → $0.031);
    eve +11% ($0.091 → $0.101).
- Authors' inference: every harness is under pressure to route around sites that behave this way.

## 05 — Accuracy

- Answers with none of the asked facts: read from site 7% vs from web/other sites 25% → 3.7× (paired within domain,
  harness, question type).
- Fate of each asked fact:

| Evidence source | Right | Half right | Wrong | Never mentioned |
|---|---|---|---|---|
| Read from the site | 40% | 27% | 4% | 29% |
| From web / other sites | 28% | 21% | 6% | 45% |

- Wrong facts rare either way; the growing failure is omission — fluent, confident answers that hallucination metrics and AEO
  dashboards don't flag.
- Own-site answers 1.4× as accurate overall; accuracy climbs 41% → 56% as share of evidence from own pages rises.
- By question type (site vs web accuracy): pricing 60% vs 37% (+64%); features 46% vs 39% (+18%); setup 24% vs 24% (even).
- Setup: two-thirds of setup facts never surface; what moves setup is findability — sites where agents could ground setup
  answers score 31% vs 18% from both sources alike.
- Empty answers by stack (site vs web): claude-code 15% vs 70% (4.8×); claude-agent-sdk 11% vs 21% (1.9×); openclaw 7% vs 9%
  (1.2×); eve 7% vs 7% (1.0×).

## 06 — What to do

- AX = making your own site accessible, readable, and usable for the agent already on it.
- Authors argue the "arbitrage is closing" for off-site tactics (seeded threads, listicles on other sites, citation placement).
- Remaining work: SEO (so agents find you) + AX (so they can reach, read, and use your site).
- Resources pointed to: ora.ai ranker (100+ checks, per-layer breakdown); agentready.org open spec (find, read, act).

## 07 — Not measured (next study)

- Assistants building their own front doors to businesses:
  - June 2026: Microsoft, Google, Hugging Face (+ GitHub, Snowflake) draft Agentic Resource Discovery (ARD) spec — agents search
    a registry for tools, MCP servers, other agents before calling anything.
  - July 9, 2026: OpenAI migrated ChatGPT's app directory to a plugin directory.
  - Sep 8, 2026: Meta launched Muse with connectors (email, restaurants, payments, Shopify); uses a service's API when one exists,
    browser only otherwise. Amazon blocked Muse; Shopify merchants stayed reachable via declared Shop Pay checkout path.
  - Sep 28, 2026: Instinct raised $1B Series C ($10B valuation) for a personal agent working from email/messages/apps.
- Hypothesis (explicitly unmeasured): if assistants check connectors/registries first, the web becomes the fallback; the
  "find" layer of AX would grow to include the assistant's own catalog.

## 08 — Five conclusions (paraphrased)

1. Training knowledge is no longer where the answer comes from (7–10% of finished answer).
2. Readability is the largest single lever measured (1.9× avg, up to 2.6×; 78% vs 58% own-page share).
3. When the agent can't read you, it builds the answer without you (web search share 12% → 25%; 3.7× more empty answers;
   own-page answers 1.4× as accurate).
4. Blocking agents costs the operator (23% more turns, 2.1× blocks, up to +93% per grounded answer), then you.
5. The AEO arbitrage is closing — `site:` queries jumped to 23–24% of ChatGPT background searches from Aug 8, 2026.
