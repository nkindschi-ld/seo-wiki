---
type: source
tags: [aeo, seo]
date_published: 2026-02-20
date_ingested: 2026-10-02
origin: raw/studies/punturo-markdown-llm-bot-traffic-rct-2026.pdf
---

# Does Markdown Increase LLM Bot Traffic? A Randomized Controlled Experiment (Punturo, 2026)

**Citation:** Punturo, Brandon. "Does Markdown Increase LLM Bot Traffic?
A Randomized Controlled Experiment." February 2026 (PDF dated
2026-02-20), 18 pp.
https://23651831.fs1.hubspotusercontent-na1.net/hubfs/23651831/markdown_llm_paper%20(1).pdf

The paper doesn't state the author's affiliation. The data comes from
Profound's Agent Analytics product. It's a whitepaper, not
peer-reviewed. Extracted text:
`raw/studies/punturo-markdown-llm-bot-traffic-rct-2026.md`.

## Design

- **Sample:** 380 pages on 6 partner websites in different verticals,
  after removing 1 outlier. Pages were randomly assigned within each
  site: 189 control (HTML) and 191 treatment (Markdown).
- **Treatment:** middleware detected LLM bots **by user agent** and
  served them a clean Markdown version of the page. Humans and other
  crawlers got the standard HTML. This is user-agent-based serving, not
  `Accept`-header content negotiation.
- **Bots counted:** ChatGPT-User, OAI-SearchBot, GPTBot, ClaudeBot /
  Claude-Web, PerplexityBot, Meta-ExternalAgent / FacebookBot /
  facebookexternalhit, and DuckAssistBot. Googlebot and Bingbot were
  excluded, because AI activity can't be separated from search
  indexing.
- **Outcome:** bot visits per page, deduplicated per bot per page per
  minute. 8,151 raw requests became 7,194 visits. This measures crawl
  volume, not citations.
- **Timeline:** pre-period Jan 2–12, 2026, used for the CUPED
  adjustment. Implementation Jan 13–18. Experiment Jan 19–Feb 8, 2026
  (20 days).
- **Analysis:** Mann-Whitney U, a CUPED-adjusted mean (CUPED adjusts
  for each page's pre-experiment traffic and cut variance by about 40%),
  and a median permutation test.

## Key takeaways

- **No statistically significant effect.**

  | Metric | HTML | Markdown |
  |---|---|---|
  | Median visits per page | 6.0 | 7.0 |
  | Mean visits per page | 13.5 | 15.7 |

  The raw lift is about +16.5%. With CUPED it's **+13.9%, 95% CI
  [−11.2%, +46.8%]**. Mann-Whitney gives p=0.62, and the median
  permutation test p=1.0.
- **Large effects are ruled out; small ones aren't.** The minimum
  detectable effect at 80% power is about 41% with CUPED (about 53%
  raw). The data fit a small positive effect, no effect or a small
  negative one. They don't fit a "game-changer." Effects of 10–15% would
  need a larger study.
- **ChatGPT-User is the only bot with a positive trend.** It was 73% of
  bot traffic (Meta 20%, OAI-SearchBot 4%, ClaudeBot 2%, GPTBot 1%).
  Its lift was +8.5% with CUPED and +20% winsorized, neither
  significant (Mann-Whitney p=0.38). Meta was 0%, OAI-SearchBot −1% and
  ClaudeBot −4%.
- **The trend sits in pages that already get the most bot visits.**
  Below the median (4 or fewer ChatGPT-User visits) there's no
  difference. The gap opens around the 60th percentile. The authors'
  reading is that Markdown may amplify crawling of already-busy pages
  rather than drive discovery of new ones.
- **Per-site lifts follow pre-existing imbalances.** For example, one
  site showed +27% during the experiment, but its Markdown pages
  already had +61% more traffic beforehand. Another showed −8% both
  before and during. Daily lift swung between −40% and +60% even in the
  pre-period, when both groups got HTML.
- **The authors' explanation:** LLMs already parse HTML well, and the
  web is still HTML-first. They cite Google's John Mueller and
  Microsoft's Fabrice Canel (via Search Engine Land, Feb 2026) as
  skeptical of separate bot-only Markdown.
- **Their advice:** don't treat Markdown as a silver bullet. Focus on
  crawlable, well-structured, fast pages that bots can access. They
  plan to re-run the test later in 2026.

## Caveats

- Underpowered for moderate effects; 20 days; 6 sites with unnamed
  verticals; no citation measurement.
- **It doesn't test the coding-agent case.** Its bot list leaves out
  Claude Code and other coding agents, which are the clients shown to
  *request* Markdown through `Accept: text/markdown`
  ([[evilmartians-which-ai-reads-your-site-2026]]).
- **Built-in limit of the design.** A bot can't know a page will be
  Markdown before fetching it. So the visit-volume outcome can only move
  through indirect channels, such as re-crawl frequency or retrieval
  systems learning which pages parse better. Crawl volume is a narrow
  test of "does Markdown help."
- User-agent-based serving of different content to bots and humans is
  a different practice from content negotiation, with its own search
  risk (Google and Bing don't recommend separate bot-only Markdown
  pages).
- Profound's tooling, unstated affiliation, not peer-reviewed.

## Relationship to existing wiki claims

- **The first randomized controlled test in the wiki** of any
  "Markdown for AI" tactic. It extends the run of observational null
  results on [[llms-txt]] (Google guidance, Otterly, Evil Martians,
  Limy) from the llms.txt file to serving Markdown pages themselves.
- **Agrees with** [[evilmartians-which-ai-reads-your-site-2026]].
  ChatGPT-User is about 73% of agent traffic in both studies. It takes
  HTML when it has the choice (Evil Martians) and isn't significantly
  moved when given Markdown (here). This supports the existing advice
  in [[technical-seo-audit-checklist]] that rendered HTML quality comes
  first and content negotiation is an add-on for coding agents.
- **Leaves open** the coding-agent and docs case in [[llms-txt]] and
  [[docs-over-mcp]], because no coding agents were in the bot set.
- **Qualifies** step 10 of [[ai-pricing-visibility-audit]] ("AI-readable
  versions… probably improve retrieval"). At least for crawl volume, a
  randomized test found no significant effect.
- No conflict logged. No page in the wiki claims Markdown serving
  causes a measured lift.

## Updated pages

- [[llms-txt]]
- [[technical-seo-audit-checklist]]
- [[geo-content-optimization-tactics]]
- [[ai-pricing-visibility-audit]]
