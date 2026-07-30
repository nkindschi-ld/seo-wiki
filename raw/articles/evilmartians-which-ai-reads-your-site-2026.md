# Which AI actually reads your site? Two months of LLM traffic, measured

**Source:** Evil Martians Chronicles
**Authors:** Rita Klubochkina, Travis Turner
**Published:** 2026-07-21
**URL:** https://evilmartians.com/chronicles/which-ai-actually-reads-your-site-two-months-of-llm-traffic-measured

> Archival capture via WebFetch (2026-07-29). Text below is a faithful
> structured summary of the article's content and figures, not a verbatim
> copy. Numbers preserved as reported.

---

## Premise

Evil Martians instrumented their own site to measure what non-human agents
actually do, rather than relying on external "AI SEO" advice. Client-side
analytics can't see non-rendering agents; server-side instrumentation can.
Over roughly early May to early July 2026 they logged ~268,000 agent
requests vs. ~107,000 human pageviews — a 2.5:1 ratio of software-to-human
reads.

## Methodology

- Server-side middleware deployed as a **Netlify edge function**, running
  before HTML rendering.
- Reads the raw `User-Agent` and `Accept` request headers.
- Classifies each client into one of: `ai`, `browser`, `crawler`,
  `scanner`, `library`.
- Implements HTTP **content negotiation**: serves Markdown in response to
  `Accept: text/markdown`, HTML otherwise.
- Forwards server-side events to Google Analytics 4 via the Measurement
  Protocol (so non-rendering agents are captured, unlike client-side JS
  tags).

## Traffic composition

Total: ~268,000 agent requests vs. ~107,000 human pageviews.

Format split of agent requests:
- **HTML: ~227,000 (85%)**
- **Markdown: ~40,000 (15%)**
- **llms.txt / llms-full.txt: negligible**

## Per-agent behavior

| Agent | Requests | Markdown % | Notes |
|---|---|---|---|
| ChatGPT-User | 196,973 (~73% of total) | 0.1% | Reads rendered HTML almost exclusively |
| Claude Code | 23,300 (~9%) | 76% | Requests Markdown via `Accept: text/markdown` |
| OAI-SearchBot | 7,255 | 26% | Mixed HTML/Markdown |
| GPTBot | 3,579 | 31% | Mixed HTML/Markdown |
| Perplexity | 7,728 | ~0% | HTML-only |

Central point: "AI traffic" is not a monolith. Different clients have
opposite format preferences — a coding agent (Claude Code) overwhelmingly
wants Markdown, while the dominant live-retrieval client (ChatGPT-User)
takes HTML almost exclusively.

## Techniques tested, ranked by measured effectiveness

1. **Content negotiation (HTTP `Accept` header)** — most effective. Delivers
   Markdown to Claude Code (76% of its requests) using standard HTTP,
   requiring no site-specific knowledge from the agent.
2. **`.md` routes** — modest adoption; ~15% of agent traffic overall, mostly
   coding agents and on-demand fetchers. Training crawlers largely ignore
   them.
3. **`llms.txt`** — ineffective for its intended purpose. ~660 direct fetches
   over two months; only ~37 came from named AI assistants (Perplexity,
   ChatGPT, Claude, GPTBot, OAI-SearchBot); the remaining ~95% were search
   crawlers and generic indexer/scanner bots. Referrer analysis: 106 of 117
   "referral" hits traced to a stale `Chrome/111.0` bot, not authentic AI
   following links. Confirms the "nobody meaningfully uses llms.txt"
   consensus.
4. **Hidden AI hint (a `<link>` tag)** — zero measurable impact. A tagged
   URL parameter (`?ref=hint`) produced zero attributable fetches across all
   268,000 requests. "We cannot attribute a single Markdown fetch to the
   hidden hint."

## Unexpected findings

- **URL guessing**: agents request pages that don't exist, trying versioned
  variants (`-2025`, `-2026`) and invented slugs with `.md` extensions
  (e.g. a guessed "how-to-favicon-in-2026"). These are signals for potential
  redirect targets.
- **Domain hallucination**: thousands of requests target wrong TLDs
  (`.dev`, `.app`, `.io`) and bare IP addresses. Owning the variants and
  redirecting recovers this traffic.
- **Noise**: traffic includes SQL-injection probes, readiness scanners, junk
  user-agent strings, and fingerprinting bots alongside legitimate agents —
  hence the need for client classification.

## Recommendations

1. **Prioritize rendered HTML quality** — ChatGPT-User dominates (73%) and
   ignores Markdown.
2. **Implement content negotiation** — the mechanism actually delivering
   Markdown to the coding agents that ask for it.
3. **De-emphasize decorative signals** — hidden hints and `llms.txt` show no
   meaningful AI adoption.
4. **Segment user-agent data before analysis** — coarse "AI traffic"
   classification hides opposite behaviors (Claude Code vs. crawlers).
5. **Measure your own traffic** — external patterns don't predict
   site-specific behavior. "Winning at AI discovery won't come from shipping
   the most `.md` files. It comes from the boring habit of reading your own
   logs."
