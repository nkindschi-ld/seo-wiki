---
type: concept
tags: [seo, aeo]
updated: 2026-08-06
---


# The Meta Keywords Tag (`<meta name="keywords">`)

A `<head>` element that lets a page author declare a comma-separated
list of keywords the page is "about":

```html
<meta name="keywords" content="feature flags, progressive delivery, runtime control">
```

**Current status: deprecated and effectively dead for SEO.** Google
confirmed in 2009 that it does **not** use the tag as a ranking signal,
and that remains true. It is not part of the modern meta-tag toolkit —
see [[writing-meta-tags]] for the tags that *do* matter (title tag, meta
description).

## Are there negative consequences to keeping them?

- **Competitive-intelligence leak (the real one).** The tag sits in your
  public HTML source, so you're handing competitors a plain-text list of
  exactly which terms each page targets. This is the most-cited reason
  SEOs strip it.
- **Page bloat.** Trivial, but it's dead bytes in every page's `<head>`.
- **No ranking penalty.** Google does *not* demote you for having the
  tag — it simply ignores it. The downside is disclosure and clutter,
  not a demotion.

## Are there any advantages?

- **For major engines: none.** Google ignores it; Bing dropped it as a
  ranking signal (~2014) and has said it may read it as a *spam* signal —
  i.e., stuffing it can only hurt, never help.
- **Narrow exceptions.** A few smaller/regional engines (historically
  Yandex) and some internal/site-search products have read it. Marginal
  value only if your traffic depends on one of those — an edge case.

## Do AI crawlers / LLMs read them?

**No meaningful evidence that they do, and good reason to think they
don't.** AI answer engines (ChatGPT, Perplexity, Google AI Overviews,
Claude) inherit the modern paradigm that rewards visible, semantic
*content* over invisible head-tag hints. The consistent finding across
this wiki's AEO/GEO sources is that AI systems reward substance in the
body — answer-first phrasing, structured data, clear headings, citable
facts (see [[generative-engine-optimization]] and
[[ai-citation-landscape]]) — not keyword declarations. A hidden,
easily-gamed keyword list is exactly the kind of signal these systems
are built to ignore. The head-level elements AI crawlers *do* use are
different: `<title>`, meta description (as a snippet/summary source),
canonical tags, and JSON-LD structured data.

## Bottom line

No upside for any engine you likely care about, plus a small but real
downside (telegraphing targeting to competitors). Standard
recommendation: **drop them, or leave them empty.** Removing existing
ones is safe and won't affect rankings or AI visibility.

## Related

- [[writing-meta-tags]] — the meta tags that *do* matter
- [[traditional-seo-ranking-factors]] — Schema/keyword-matching signals
  measured weak even where they exist
- [[generative-engine-optimization]], [[ai-citation-landscape]] — why AI
  engines reward body substance over head-tag hints
