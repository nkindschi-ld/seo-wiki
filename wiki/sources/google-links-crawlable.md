---
type: source
tags: [seo]
date_published: 2025-12-10  # living doc; page "Last updated" date, checked 2026-11-04
date_ingested: 2026-07-07
origin: raw/articles/google-links-crawlable.md
---

# Make links crawlable

**Citation:** Google Search Central. "Make links crawlable."
https://developers.google.com/search/docs/crawling-indexing/links-crawlable
(no last-updated date shown on page)

## Key takeaways

- Google can only crawl a link if it's a real `<a>` element with an
  `href` attribute pointing to a resolvable URL. `<span href="...">`,
  framework-specific attributes like `routerLink`, `onclick`-only
  navigation, and `javascript:` pseudo-URLs are not reliably crawled.
- Anchor text (or `title` as fallback when link text is empty, or an
  image's `alt` text for image links) is how Google — and users —
  understand what a linked page is about.
- Good anchor text is descriptive, concise, and makes sense read out of
  context; avoid generic text ("click here", "read more"), keyword
  stuffing, excessive length, and chains of adjacent links with no
  separating context.
- Internal linking guidance: every page you care about should be linked
  from at least one other page on the site; no magic number of links,
  but "if you think it's too much, then it probably is."
- External linking is encouraged for trustworthiness/citing sources.
  `rel` qualifiers: `nofollow` for untrusted sources, `sponsored` for
  paid links, `ugc` for user-generated content links.

## What this updated in the wiki

- Created [[link-and-anchor-text-best-practices]] (playbook): crawlable
  link markup, anchor text writing rules, internal/external linking
  guidance, and `rel` attribute usage.
- Cross-linked from [[how-google-search-works]] (crawling stage — this
  source gives the link-level mechanics of URL discovery via links) and
  [[traditional-seo-ranking-factors]] (backlinks/anchor text as a
  ranking signal).
- No conflicts — net-new, foundational technical guidance.
