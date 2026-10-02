---
type: source
tags: [aeo, seo]
date_published: 2026-08-10
date_ingested: 2026-10-02
origin: raw/articles/llmstxt-org-proposal-v2-2026.md
---

# The /llms.txt file, v2 (llmstxt.org, August 2026)

**Citation:** Howard, Jeremy (Answer.AI). "The /llms.txt file, v2."
llmstxt.org. Original proposal 2024-09-03; v2 published August 2026 (page
modified 2026-08-10). https://llmstxt.org/ and the changelog at
https://llmstxt.org/changes.html. Changelog raw copy:
`raw/articles/llmstxt-org-changes-v2-2026.md`.

**Rigor note:** this is the **primary source**, so it's authoritative on what
the format *is*. It's not neutral on whether the format *works*: the author's
adoption claims ("thousands of sites," coding agents "use them reliably")
come with no data. The site serves its own Markdown at `/index.md`, which is
how it was captured here.

## Key takeaways

- **Format:** an H1 name (the only required element), a blockquote summary,
  optional non-heading prose, then H2 "file lists" of
  `- [name](url): notes`. It's Markdown so LLMs can read it and simple
  parsers or regex can process it.
- **Placement:** the root *or any subpath*. A file covers the pages under
  its path, and the most specific file wins. `/.well-known/` was considered
  and rejected (it exists only at the origin root, which shuts out
  path-only publishers such as GitHub Pages project sites).
- **Markdown page versions** at `page.html.md` or `page.md`
  (`index.html.md`/`index.md` for directory URLs). Links in `llms.txt`
  should point to these.
- **New in v2: discovery by link relations.** `rel="alternate"
  type="text/markdown"` points to a page's Markdown version and
  `rel="describedby"` points to the covering `llms.txt`, as a `<link>` or
  an HTTP `Link:` header (CDN-configurable, works for non-HTML resources).
- **Consumption model, stated for the first time:** agents view or search
  the file and follow links. The v1 `llms_txt2ctx` context-expansion tool
  is gone, and with it the mechanical meaning of `## Optional` (now just a
  convention).
- **Positioning against other standards:** robots.txt is about access and
  `llms.txt` about on-demand inference. A sitemap is exhaustive and
  human-page-oriented, while `llms.txt` is curated, can link off-site, and
  fits in context. The author says it's used for inference rather than
  training.
- **Adoption claims:** "thousands" of sites. Docs platforms (Mintlify,
  GitBook), CMS plugins (Yoast, AIOSEO) and Wix auto-generate it. Chrome
  Lighthouse audits for it in agentic-browsing checks. OpenAI, Anthropic
  and Gemini publish files for their developer docs. Most heavily used for
  software documentation.
- **Authoring advice:** concise language, informative link descriptions, no
  unexplained jargon, and test the file by giving an agent only the
  `llms.txt` and asking it questions.

## What this updated

- Created [[llms-txt]]: the spec section, the v1→v2 table, "what it's
  not," and the format half of the checklist.
- Conflicting Evidence on [[llms-txt]]: this source contradicts the
  root-only and required-elements claims in
  [[rankability-llms-txt-best-practices]] and
  [[limy-llms-txt-2026-full-guide]], and supersedes Limy's `## Optional`
  semantics. Its "coding agents use them reliably" claim is recorded as
  asserted, in tension with [[evilmartians-which-ai-reads-your-site-2026]].
  Its new link relations are noted as untested, with the closest evidence
  (Evil Martians' zero-fetch `<link>` hint) pointing the other way.
