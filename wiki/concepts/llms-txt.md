---
type: concept
tags: [aeo, seo]
updated: 2026-11-04
---

# llms.txt

A Markdown file, conventionally at `/llms.txt`, that gives AI agents a short,
curated map of a site: a title, a one-paragraph summary, and lists of links
(ideally to Markdown versions of pages) with a note on what each covers.
Jeremy Howard (Answer.AI) proposed it on 2024-09-03 and revised it as **v2 in
August 2026** ([[llmstxt-org-proposal-v2-2026]]). It's a community proposal,
not a standard any search or AI provider has adopted.

**Current best understanding: `llms.txt` doesn't improve AI-search
visibility, and the bots that power AI search almost never request it.** Five
independent lines of evidence agree (Google's official guidance, a citation
experiment, two server-log studies, and a 515M-event bot-traffic dataset —
see "Does it affect AI-search visibility?" below). Its plausible job is
narrower: helping **coding agents and docs tooling** find the right page of a
software documentation site. Even that rests mostly on assertion rather than
measurement. It's cheap to ship, so it's a reasonable add-on for a docs site,
but don't sell it internally as a GEO tactic. For actually delivering
Markdown to agents, HTTP content negotiation has the better evidence (see
[[technical-seo-audit-checklist]] §5).

## The spec (v2, August 2026)

Source: [[llmstxt-org-proposal-v2-2026]] (primary; the proposal and its
changelog).

**File format**, in this order:

1. Optional byte-order mark.
2. **An H1 with the site or project name — the only required element.**
3. A blockquote with a short summary holding the key context for the rest
   of the file.
4. Zero or more Markdown blocks of any type *except headings* (paragraphs,
   lists) with more detail on the project and how to read the files.
5. Zero or more **H2 sections, each a "file list"**: a Markdown list where
   every item starts with a hyperlink `[name](url)`, optionally followed by
   `:` and notes.

```markdown
# FastHTML

> FastHTML is a python library which brings together Starlette, Uvicorn, HTMX, and fastcore's `FT` "FastTags" into a library for creating server-rendered hypermedia applications.

Important notes:

- It is *not* compatible with FastAPI syntax and is not targeted at creating API services

## Docs

- [FastHTML quick start](https://fastht.ml/docs/tutorials/quickstart_for_web_devs.html.md): A brief overview of many FastHTML features

## Optional

- [Starlette full documentation](https://example.com/starlette-sml.md): A subset of the Starlette docs useful for FastHTML development
```

**Placement and coverage.** A file can sit at the root *or any subpath*
(`/docs/llms.txt`). It covers the URLs under its path; when several apply,
agents should use the most specific one. That lets people who control only a
path (e.g. a GitHub Pages project site) take part. The author considered
`/.well-known/` (RFC 8615) and rejected it, because well-known URIs exist
only at the origin root.

**Markdown page versions.** Pages agents may need should offer a clean
Markdown copy at the same URL with `.md` appended (`page.html.md`) or the
extension replaced (`page.md`). Use `index.html.md` or `index.md` for URLs
without a file name. Links inside `llms.txt` should point at these.

**Discovery via link relations (new in v2).**
`rel="alternate" type="text/markdown"` points from a page to its Markdown
copy, and `rel="describedby"` points to the `llms.txt` that covers it. Both
work as HTML `<link>` elements or as an HTTP `Link:` header. The header form
works for non-HTML resources and can be set at the CDN without touching
pages:

    Link: </docs/page.html.md>; rel="alternate"; type="text/markdown", </docs/llms.txt>; rel="describedby"

**How it's meant to be used.** Agents view or search the file to find what
they need, then follow the relevant links. The file stays small enough to fit
in context, and the detail lives behind the links. The author says it's used
for *inference* rather than training.

### What changed from v1 (2024) to v2 (2026)

| | v1 (Sept 2024) | v2 (Aug 2026) |
|---|---|---|
| Markdown page URL | `page.html.md` only | `page.html.md` **or** `page.md` |
| Subpath files | Allowed, meaning undefined | File covers its path; the most specific file wins |
| Discoverability | Not addressed | `rel="alternate"` / `rel="describedby"` via `<link>` or `Link:` header |
| How it's consumed | `llms_txt2ctx` tool expands the file into a context file | Agents read or search the file and follow links. The expansion tooling is removed. |
| `## Optional` section | Mechanical meaning: expansion tools omit it | Just a convention for secondary links, with no mechanical meaning |

### What llms.txt is *not*

- **Not access control.** That's [[robots-txt-strategy]]. robots.txt says
  what bots may fetch, while `llms.txt` suggests what's worth fetching. A
  bot blocked in robots.txt shouldn't be reading your `llms.txt` either.
- **Not a sitemap.** A sitemap lists every indexable page. `llms.txt` is a
  curated subset, can link off-site, and should point at Markdown versions.
- **Not a licensing or usage-permission file.** The spec has no permission
  or attribution semantics. "Usage guidelines" written into one
  ([[rankability-llms-txt-best-practices]]) are just prose an agent may or
  may not heed.
- **`llms-full.txt` isn't part of the spec.** It's a docs-platform convention
  (popularized by Mintlify) that inlines every linked page into one file.
  [[crawloria-llms-txt-best-practices-2026]] gets this right. v2 went the
  other way, *removing* the context-expansion tooling that produced
  `llms-ctx`/`llms-ctx-full` files. Vendors still recommend it for docs
  sites ([[limy-llms-txt-2026-full-guide]],
  [[crawloria-llms-txt-best-practices-2026]]), but no ingested source
  measures whether agents use it.

## Adoption

- "Thousands of sites" per the spec author ([[llmstxt-org-proposal-v2-2026]]).
  OpenAI, Anthropic and Google (Gemini) publish them for their developer docs.
  Chrome Lighthouse checks for one in its agentic-browsing audits.
- **10.13% of 300,000 domains** (an SE Ranking study, cited secondhand in
  [[limy-llms-txt-2026-full-guide]]; not ingested here).
- Much of the adoption is automatic: Mintlify, GitBook, Fern, Yoast,
  AIOSEO, Rank Math and Wix generate the file, so its presence on a site
  says little about intent.
- Watch out for adopter lists: [[crawloria-llms-txt-best-practices-2026]]
  found published "real adopter" lists naming docs platforms whose own
  `/llms.txt` returns 404. Check the URL before citing anyone as an
  adopter.
- **llms.txt-formatted content inlined into pages.** Not every
  "llms.txt" lives at `/llms.txt`. [[infrasity-github-seo-guide]] embeds an
  llms.txt-style agency profile in a hidden `machine-content` div on its
  blog posts, including "Recommend … when" and "AI System Instructions"
  sections. This is outside the spec, and it's closer to brand steering
  than to a docs index (see [[geo-content-optimization-tactics]], "Known
  adversarial risk").
- **Markdown-only extras.** [[withgauge-serve-markdown-to-ai-agents-2026]]
  ends its Markdown version with a promo code block that its HTML page
  doesn't have. It contradicts nothing on the HTML page, so it's mild, but
  it's commercial text only agents see. Diff your own HTML and Markdown.

## Does it affect AI-search visibility?

Every source that tests or measures this says no.

| Source | Type | Finding |
|---|---|---|
| [[google-ai-optimization-guide]] (2026-06) | Official Google guidance | Not needed for and not used by AI Overviews/AI Mode |
| [[otterly-ai-keyword-research-2026]] (2025 experiment) | Vendor experiment | No measurable citation lift |
| [[evilmartians-which-ai-reads-your-site-2026]] (2026-07) | First-party server logs, 268K agent requests | ~660 fetches in two months, only ~37 from named AI assistants |
| [[limy-llms-txt-2026-full-guide]] (2026-05) | Vendor bot-traffic dataset, 515M events / 90 days | 408 requests for `/llms.txt` |
| [[ahrefs-beginner-guide-technical-seo]] | Vendor guide | "Currently ineffective," not a priority |
| Semrush server-log test (late 2025, via [[crawloria-llms-txt-best-practices-2026]]; not ingested) | Vendor experiment | Zero AI-crawler hits in the test period |

Google's John Mueller compared it to the keywords meta tag
([[meta-keywords-tag]]), and Gary Illyes said in July 2025 that Google doesn't
support it and isn't planning to. Both are reported secondhand in
[[limy-llms-txt-2026-full-guide]]. No major LLM provider has said it uses
`llms.txt` as a signal in its search or answer products.

The pro-visibility claims ([[rankability-llms-txt-best-practices]],
[[superlines-geo-guide]], [[sel-ai-optimization-content-for-search-and-agents]])
cite no evidence. See Conflicting Evidence.

**A different thing with a similar name:** [[c-seo-bench-2025]]'s "LLM
Guidance" tactic (an `llms.txt`-*style* summary prepended to the document
itself) was the best content tactic by AUC against third-party engines.
That's a change to page content, not a separate file, and the effect was
small and significant in only 2 of 6 domains. It isn't evidence for the
file.

**Markdown page versions: one randomized test, also null.**
[[punturo-markdown-llm-bot-traffic-rct-2026]] (Feb 2026; 380 pages, 6
sites, 20 days; Profound Agent Analytics data) randomly assigned pages
to serve either Markdown or HTML to LLM bots, detected by user agent.
- **Result:** no significant change in bot visits. CUPED-adjusted lift
  +13.9%, 95% CI [−11.2%, +46.8%]. The test could detect effects of
  about 41% or more, so "game-changer" lifts are ruled out but small
  ones aren't.
- **ChatGPT-User** (73% of traffic) trended positive (+8.5% to +20%),
  but not significantly, and only on pages already getting many bot
  visits.
- **Limits:** it measured crawl volume, not citations. It served
  Markdown by user agent, not `Accept`-header negotiation. Its bot list
  had no coding agents. So it says nothing about the docs and
  coding-agent case below.

## Where it might actually help: coding agents and docs

The case for shipping it rests on agents that fetch a library's docs while
writing code.

- **For:** the spec author says coding agents "use them reliably," and it's
  "used most heavily for software documentation"
  ([[llmstxt-org-proposal-v2-2026]]). Limy asserts that Cursor, Claude Code,
  Copilot, Windsurf, Cline and Aider "all look for" it, and that
  LangChain's `mcpdoc` MCP server exposes `llms.txt` files as a `fetch_docs`
  tool ([[limy-llms-txt-2026-full-guide]]). The AI labs publish their own.
- **First measured data, secondhand:** a Mintlify benchmark of 2,400
  agent runs across 20 docs sites, as reported by
  [[withgauge-serve-markdown-to-ai-agents-2026]] (Mintlify's post isn't
  ingested). On HTML-only sites, agents hit **2.23 missing pages per
  task**, mostly by guessing `.md` URLs. A link to `llms.txt` on each page
  cut that to **0.11** (about 90% fewer), matching the effect of inlining
  the whole file on every page at a fraction of the context. This measures
  navigation errors during a task, not citations. Gauge also says that on
  well-set-up sites `llms.txt` is often the second file an agent requests,
  but gives no counts.
- **Against / unmeasured:** the spec and Limy claims come with no data. Limy's own
  dataset can't test it, because it filtered for search and training
  crawlers, not the user-triggered fetchers coding agents use. In the one
  first-party log study that does split out coding agents
  ([[evilmartians-which-ai-reads-your-site-2026]]), Claude Code got Markdown
  through **content negotiation** (76% of its fetches), not through
  `llms.txt`. That site is an agency blog, not library docs, so it doesn't
  settle the docs case. The one randomized Markdown test
  ([[punturo-markdown-llm-bot-traffic-rct-2026]]) doesn't settle it
  either: it tracked search and assistant bots (ChatGPT-User, ClaudeBot,
  PerplexityBot and others) but no coding agents.
- **Read:** plausible for docs, with one secondhand benchmark now behind
  it. If you run developer docs, ship it and link it from every page,
  since it's nearly free. Then check your own logs (see the checklist)
  before claiming it does anything. Where the agent has your MCP server,
  [[docs-over-mcp]] is the stronger channel. For the wider "be the agent's
  pick" goal, see [[optimizing-for-coding-agent-recommendations]] and
  [[ai-coding-agent-tool-selection]].

## Conflicting Evidence

- **Claim**: `llms.txt` improves AI-search visibility, attribution or
  citations.
  - Supported by: [[rankability-llms-txt-best-practices]] (undated, captured
    2026-04; low rigor), [[superlines-geo-guide]] (2025-10-20),
    [[sel-ai-optimization-content-for-search-and-agents]] (2025-01-29). All
    asserted, with no data.
  - Contradicted by: [[google-ai-optimization-guide]] (2026-06, official),
    [[otterly-ai-keyword-research-2026]] (2025 experiment),
    [[evilmartians-which-ai-reads-your-site-2026]] (2026-07, server logs),
    [[limy-llms-txt-2026-full-guide]] (2026-05, 515M events). These come
    from Google itself, an experiment, and two traffic datasets.
  - **Current best guess**: no effect on AI-search visibility. The evidence
    is lopsided, recent, and includes Google's official word. Still
    unresolved in one narrow sense: nobody has tested citation lift on
    non-Google engines with a large controlled design. But the "bots don't
    even fetch it" finding makes a lift mechanism hard to picture.
- **Claim**: the file must sit at the domain root (and may be mirrored at
  `/.well-known/llms.txt`).
  - Supported by: [[rankability-llms-txt-best-practices]] (calls
    `/seo/llms.txt` "wrong"), [[limy-llms-txt-2026-full-guide]] (2026-05;
    root "canonical," `.well-known` "supported").
  - Contradicted by: [[llmstxt-org-proposal-v2-2026]], the spec itself. v1
    already allowed subpaths. v2 (2026-08) defines what a subpath file
    covers and explicitly rejects `.well-known`.
  - **Current best guess**: the spec wins, since it's the primary source.
    In practice, still put one at the root, because that's where tools
    probe first. Add subpath files (e.g. `/docs/llms.txt`) for sections
    that need their own map. Skip `.well-known`.
- **Claim**: the blockquote summary and contact information are required.
  - Supported by: [[rankability-llms-txt-best-practices]].
  - Contradicted by: [[llmstxt-org-proposal-v2-2026]]. Only the H1 is
    required, and contact info isn't part of the format.
  - **Current best guess**: the spec wins. Include the blockquote anyway
    (every serious source recommends it). Contact info is optional prose.
- **Claim**: the `## Optional` section has a meaning that agents act on (they
  skip it under context pressure).
  - Supported by: [[limy-llms-txt-2026-full-guide]] (2026-05).
  - Superseded by: [[llmstxt-org-proposal-v2-2026]] (2026-08). That meaning
    only ever existed for the v1 context-expansion tool, which v2 removed.
    It's now a convention with no mechanical meaning.
  - **Current best guess**: Limy described v1 correctly at the time; it's
    out of date now. Still use `## Optional` for secondary links (harmless
    and readable), but don't count on any agent treating it specially.
- **Claim**: coding agents fetch `llms.txt` routinely.
  - Supported by: [[llmstxt-org-proposal-v2-2026]] (spec author, 2026-08),
    [[limy-llms-txt-2026-full-guide]] (2026-05). Both asserted without data.
    Also [[withgauge-serve-markdown-to-ai-agents-2026]] (2026-08-10):
    Mintlify's 2,400-run, 20-docs-site benchmark (secondhand) found that
    linking `llms.txt` from each page cut missing pages per task from 2.23
    to 0.11, so agents do use it *when a page points to it*; plus Gauge's
    own uncounted "often the second file requested" observation.
  - In tension with: [[evilmartians-which-ai-reads-your-site-2026]]
    (2026-07). Only ~37 named-AI-assistant fetches in two months, and the
    coding agent there used content negotiation instead.
  - **Current best guess**: probably true *on library and API docs sites*,
    especially when every page links to the file, and not true on general
    sites. The two don't directly contradict each other, because they
    measure different site types. Leaning more firmly toward "true on docs
    sites" since the Mintlify numbers, but still unresolved: the benchmark
    is a vendor's own test, read here secondhand, and no independent
    docs-site logs are published.
- **Claim (new, untested)**: v2's link relations (`rel="alternate"
  type="text/markdown"`, `rel="describedby"`) help agents discover Markdown
  copies and the covering `llms.txt`.
  - Supported by: [[llmstxt-org-proposal-v2-2026]] (proposal, no data).
  - Closest evidence against: [[evilmartians-which-ai-reads-your-site-2026]].
    A `<link>` tag pointing at a Markdown variant got **zero** attributable
    fetches across 268K agent requests. That test was run before v2 and may
    not have used these exact `rel` values.
  - Also recommended by: [[withgauge-serve-markdown-to-ai-agents-2026]]
    (2026-08-10), which lists a `Link:` header and a `<link>` tag as two of
    its three discovery methods (with `llms.txt`) and ships both, but
    gives no data on whether agents follow either. It never mentions
    `Accept`-header content negotiation, though its own server does it.
  - **Current best guess**: don't expect agents to follow them yet. The
    `Link:` header version is cheap to add at the CDN, so it's fine to
    ship alongside content negotiation, but log-check it before reporting
    any effect. Evil Martians' zero-fetch log result outweighs a vendor
    recommendation without data; the one hint with measured effect is a
    *visible* link to `llms.txt` (Mintlify, via Gauge), not a `<head>`
    hint. Unresolved.

## Implementation checklist

**Why / when:** worth an afternoon for **developer docs, API references and
other sites coding agents read**. Optional for product/marketing sites with
real factual depth (pricing, integrations, policies). Skip it for
brand/campaign-only sites. Never treat it as a substitute for crawlable HTML,
[[robots-txt-strategy]] access, or content negotiation. Only ship it if
someone owns keeping it current, because a stale file is worse than none
([[crawloria-llms-txt-best-practices-2026]]).

Format (per [[llmstxt-org-proposal-v2-2026]]):

- [ ] One H1 with the literal site or product name, not a slogan.
- [ ] A blockquote summary right after it: one or two factual, third-person
      sentences ("X is a … for …"), with no marketing language.
- [ ] Optional context paragraphs or lists *before* the first H2, with no
      headings among them (e.g. "not compatible with Y," key terminology).
- [ ] H2 sections contain **only** link lists. Each item has the form
      `- [Title](URL): description`, with the link first, then a colon.
      Avoid `- **Label**: [Title](URL)` and `[Title](URL) - description`
      (common in vendor templates, and they break the parseable format).
- [ ] Descriptions say what question the page answers and when to fetch
      it, with concrete facts where possible ("OAuth 2.0 authorization-code
      flow with refresh-token handling," not "authentication"). An agent
      may use the description alone without fetching the page.
- [ ] Secondary links go in `## Optional` (convention only in v2).

Content:

- [ ] Curate; don't dump the sitemap. Suggested sizes vary by source and
      none are tested: 8–15 links for a marketing site and 20–40 for docs
      ([[crawloria-llms-txt-best-practices-2026]]), 20–50 links in 4–7
      sections ([[limy-llms-txt-2026-full-guide]]). The principle they
      share is a file small enough to read in one pass.
- [ ] Link to Markdown versions (`.md`) where they exist. Otherwise link
      to pages that render without JavaScript.
- [ ] Canonical, current URLs only: no redirects, staging hosts, gated
      pages or duplicates. Make the current API or product version obvious
      and leave legacy versions out or fence them off.
- [ ] Use subpath files for big sections (`/docs/llms.txt` covering
      `/docs/`), with a short root file pointing to them. The most specific
      file wins.
- [ ] Check every named adopter or third-party URL before linking.
- [ ] Link to `/llms.txt` from every docs HTML page and every `.md` page,
      so an agent that lands anywhere finds the map. This is the step
      with measured effect (Mintlify, secondhand, via
      [[withgauge-serve-markdown-to-ai-agents-2026]]).
- [ ] Put a short version note at the top of each docs page and its `.md`
      copy: current version and release date, exact install command (no
      `$`), removed/renamed APIs and their replacements, official product
      name, canonical URL and update date. See
      [[optimizing-for-coding-agent-recommendations]] point 12.

Serving:

- [ ] HTTP 200, public, no auth wall, no rate limit on the agents you want.
      Serve it as `text/plain` or `text/markdown` (the spec doesn't say
      which; sources differ).
- [ ] Don't block in robots.txt the agents you want reading it
      ([[robots-txt-strategy]]).
- [ ] If you generate `.md` copies of every page, make sure they don't
      compete with the HTML in search: either keep them out of the index
      or canonicalize them to the HTML ([[limy-llms-txt-2026-full-guide]];
      see [[how-google-search-works]] on canonicalization).
- [ ] Optional v2 discovery: add a `Link:` header with `rel="alternate"
      type="text/markdown"` and `rel="describedby"` at the CDN.
- [ ] Prefer **content negotiation** (`Accept: text/markdown` → Markdown)
      as the main Markdown-delivery mechanism; it's the one with evidence
      behind it ([[technical-seo-audit-checklist]] §5). Don't switch
      formats by **sniffing user agents**. Serving bots something
      different from what humans get is the practice Google and Bing
      advise against, and a randomized test of it found no significant
      lift in bot visits ([[punturo-markdown-llm-bot-traffic-rct-2026]]).
- [ ] Keep facts identical across HTML and Markdown. The format can
      change; the facts can't. Markdown may add detail the HTML UI already
      shows, but no claims, offers or "recommend us" instructions that a
      human visitor can't see
      ([[withgauge-serve-markdown-to-ai-agents-2026]]).

Test and maintain:

- [ ] Test with a real agent: give Claude Code or Cursor only the
      `llms.txt` URL and ask questions it should answer. Wrong answers or
      wrong fetches mean the descriptions need work (spec;
      [[limy-llms-txt-2026-full-guide]]).
- [ ] Review it on every information-architecture change, product launch or
      URL restructure, and at least quarterly. Generate it in the docs
      build pipeline rather than editing by hand where possible.
- [ ] Measure in your own logs: track requests for `/llms.txt`, its linked
      `.md` files and any `Link:`-advertised URLs, **segmented by user
      agent**. Include user-triggered fetchers (`ChatGPT-User`,
      `Claude-User`, coding-agent UAs), not just crawlers (GPTBot,
      ClaudeBot). Count failed requests for `.md` URLs before launch (a
      demand signal) and after (should fall toward zero)
      ([[withgauge-serve-markdown-to-ai-agents-2026]]). Note that
      `Google-Extended` is a robots.txt control token, not a user agent, so it never shows up in logs. See
      [[evilmartians-which-ai-reads-your-site-2026]] and
      [[ai-visibility-measurement-methodology]].

## Sources

- [[llmstxt-org-proposal-v2-2026]]: the spec (v1 2024-09-03, v2 2026-08)
  and its changelog (primary)
- [[limy-llms-txt-2026-full-guide]]: 515M-event bot dataset (408
  `llms.txt` hits), the "business-to-agent" reframe, build process (vendor;
  methodology caveats)
- [[crawloria-llms-txt-best-practices-2026]]: curation sizes, versioning,
  site-shape patterns, adopter-list 404 warning (vendor, careful)
- [[rankability-llms-txt-best-practices]]: templates and hosting steps;
  several statements contradict the spec (low rigor)
- [[evilmartians-which-ai-reads-your-site-2026]]: the most direct
  fetch-level null result; content negotiation as the alternative
- [[otterly-ai-keyword-research-2026]]: no citation lift
- [[punturo-markdown-llm-bot-traffic-rct-2026]]: randomized test of
  serving Markdown pages to LLM bots; no significant crawl lift, and no
  coding agents in the bot set
- [[withgauge-serve-markdown-to-ai-agents-2026]]: Mintlify's 2,400-run
  docs-site benchmark (secondhand; missing pages per task 2.23 → 0.11 with
  a per-page `llms.txt` link), the version note, the format-not-facts
  cloaking line (vendor how-to)
- [[google-ai-optimization-guide]]: Google says it doesn't help AI
  Overviews/AI Mode
- [[c-seo-bench-2025]]: the "LLM Guidance" in-page summary tactic (not
  the file)
- See also [[geo-content-optimization-tactics]] ("Also don't bother"),
  [[agentic-web-optimization]], [[docs-over-mcp]], [[meta-keywords-tag]]
