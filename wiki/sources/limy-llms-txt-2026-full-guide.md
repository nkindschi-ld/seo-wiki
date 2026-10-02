---
type: source
tags: [aeo, seo]
date_published: 2026-05-12
date_ingested: 2026-10-02
origin: raw/articles/limy-llms-txt-2026-full-guide.md
---

# LLMs.txt in 2026: The Full Guide (Limy, 2026-05-12)

**Citation:** Oren, Yahel (Data Scientist, Limy). "LLMs.txt in 2026: The
Full Guide." Limy blog, 2026-05-12.
https://limy.ai/blog/llms-txt-in-2026-the-full-guide

**Rigor note:** a vendor guide (Limy sells AI-visibility analytics and builds
`llms.txt` files for clients) with one piece of first-party data. Treat the
data and the advice separately:

- **The dataset:** 515,382,577 LLM-bot events across Limy's client brands
  over ~90 days, of which **408 requested `/llms.txt`**. The client mix,
  site types and per-bot breakdown aren't disclosed.
- **Filter problems.** The filter was GPTBot, ClaudeBot, PerplexityBot,
  OAI-SearchBot and Google-Extended, which Limy calls the bots "that
  actually drive citations." But GPTBot is a *training* crawler (see
  [[robots-txt-strategy]]). And **Google-Extended is a robots.txt control
  token, not a user agent**, so it can't match any request. The filter also
  leaves out the user-triggered fetchers (ChatGPT-User, Claude-User,
  coding-agent UAs) that its own business-to-agent argument depends on. So
  the dataset supports "search and training crawlers ignore `llms.txt`" and
  says nothing about coding agents.
- **The coding-agent claims are asserted.** "IDE agents fetch llms.txt
  routinely" comes with no data.
- **Sloppy example.** The "annotated example" breaks the article's own
  format rules (no H1 or blockquote, link lines without `- ` list markers)
  and its commentary describes a different file ("Northwind," pricing
  tiers).
- Secondhand figures (SE Ranking's 10.13%, "up to 10x token reductions,"
  the Illyes and Mueller quotes) come without links to the originals.

## Key takeaways

- **Search and training crawlers essentially never fetch it:** 408 of
  ~515M events. Limy's verdict: "not a GEO ranking factor," and any agency
  promising a citation lift "is overselling."
- **Adoption:** 10.13% of 300K domains (SE Ranking, secondhand). Google
  (Illyes, July 2025) doesn't support it and has no plans to. Mueller
  compared it to the keywords meta tag.
- **The reframe:** `llms.txt` is "Business-to-Agent (B2A)" infrastructure,
  not GEO. It's a routing file for agents acting for users: IDE agents,
  MCP servers (LangChain's `mcpdoc` exposes `llms.txt` files as a
  `fetch_docs` tool), docs platforms (Mintlify's late-2024 rollout gave
  thousands of sites the file at once). Limy extends this speculatively to
  e-commerce, finance, pharma, travel, B2B vendor research and publishing.
  It's a business-to-agent version of [[agentic-web-optimization]], with no
  evidence outside dev tools.
- **Format rules:** a literal-name H1, a blockquote, H2 sections, and
  `- [Title](URL): Description` link lines. It says `## Optional` has
  "semantic meaning" agents act on. That's **outdated**: spec v2
  (2026-08) dropped it (see [[llms-txt]] Conflicting Evidence).
- **Build process (about half a day):** pick 20–50 canonical URLs in 4–7
  sections, write a factual blockquote, write one-sentence descriptions
  with concrete facts (an agent may use the description without fetching
  the page), ship `llms-full.txt` only for docs-heavy sites, audit
  robots.txt, test with Claude Code or Cursor, and instrument CDN logs.
- **Placement claims that contradict the spec:** "must live at" the root,
  with a `/.well-known/` mirror "supported." It also suggests one file per
  language root (`/en/llms.txt`), which the spec's subpath rules do allow.
- **Useful mistakes list:**
  - Don't create *indexable* `.md` duplicates of every page (duplicate
    content, wasted crawl). Either noindex them or canonicalize them to
    the HTML.
  - Skip pages that need JavaScript to render.
  - Don't list duplicate links.
  - Don't gate or rate-limit the file.
  - Embed a honeypot link to detect automated readers.

## What this updated

- [[llms-txt]]: the evidence table (408 / 515M), the coding-agent "for"
  case (asserted), the build and maintenance checklist items, the `.md`
  duplicate-content item and the measurement item (including the
  Google-Extended pitfall).
- Conflicting Evidence on [[llms-txt]]: root-only / `.well-known` placement
  (contradicted by the spec), `## Optional` semantics (superseded by v2),
  and coding agents fetching routinely (in tension with
  [[evilmartians-which-ai-reads-your-site-2026]]).
- [[geo-content-optimization-tactics]]: a third traffic-side null result
  for the "Also don't bother" `llms.txt` entry.
