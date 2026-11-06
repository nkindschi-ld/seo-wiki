---
type: source
tags: [aeo, seo]
date_published: 2026-06-06
date_ingested: 2026-10-02
origin: raw/articles/crawloria-llms-txt-best-practices-2026.md
---

# llms.txt Best Practices: 2026 Practical Guide (Crawloria, 2026-06-06)

**Citation:** Tsygankov, Max (Founder, Crawloria). "llms.txt Best
Practices: 2026 Practical Guide." Crawloria blog, 2026-06-06.
https://www.crawloria.com/blog/llms-txt-best-practices

**Rigor note:** a vendor guide (Crawloria sells AI-crawlability audits and a
free `llms.txt` generator) with no original data. It's the most careful of
the three vendor guides ingested on 2026-10-02:

- It sets honest expectations ("low-cost insurance," not traffic).
- It correctly says `llms-full.txt` isn't in the spec.
- It names the adopters it says it verified.

Its curation sizes and "the strongest signal comes from what appears first"
are reasoned, not tested. The Semrush server-log result it cites wasn't
linked or ingested.

## Key takeaways

- **The honest case:** a Semrush server-log experiment (late 2025) found
  zero AI-crawler hits to a published `llms.txt`, Google says no AI system
  formally uses it, and no major provider has confirmed consuming it.
  Publish as cheap insurance and as a "content-architecture forcing
  function," or not at all if you can't keep it current. "A stale
  llms.txt is worse than no llms.txt."
- **Eight practices:**
  1. Curate, don't dump: 20–40 links in 2–3 sections for docs, 8–15 for
     a marketing site with product pages, and skip it for pure
     brand/campaign sites.
  2. Put the most important canonical pages first.
  3. Write one-sentence, answer-shaped descriptions (meta descriptions
     can be reused if they're good).
  4. Link to `.md` versions where they exist.
  5. Make the current API or product version unmistakable and leave legacy
     versions out.
  6. Review on every reorg or launch and at least quarterly.
  7. Add `llms-full.txt` only for deep, stable docs.
  8. Match the structure to the site's shape (below).
- **Three adopter patterns:** *catalog* (Stripe, Cloudflare: wide product
  surface by category), *lean index + full export* (Anthropic, Vercel AI
  SDK), and *workflow-first* (Cal.com leads with AI-agent and scheduling
  workflows). Don't copy a competitor whose site has a different shape.
- **Verify adopter lists:** at least two well-known docs platforms named in
  third-party best-practice articles return 404 on their own `/llms.txt`.
- **Common mistakes:** stale links, marketing puffery, no curation,
  inconsistent formatting (parsers handle bullet-lists-under-H2 best), and
  publishing once and then forgetting it.

## What this updated

- [[llms-txt]]: "what it's not" (`llms-full.txt` isn't in the spec), the
  adoption section (adopter-list 404 warning), the Semrush row in the
  evidence table (secondhand), and the curation, versioning and maintenance
  items in the checklist.
- Agrees with the wiki's existing "no AI-visibility effect" position on
  [[geo-content-optimization-tactics]]. No conflicts.
