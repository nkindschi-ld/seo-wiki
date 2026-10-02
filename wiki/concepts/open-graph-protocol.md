---
type: concept
tags: [seo, aeo]
updated: 2026-09-23
---


# Open Graph Protocol (`og:` tags)

A set of `<meta property="og:…">` tags in a page's `<head>` that tell
platforms how to render the page as a **link preview card** when someone
shares its URL. Facebook introduced it in 2010 to replace ad-hoc scraping
([[stream-open-graph-protocol-glossary]]); the spec lives at ogp.me.
Facebook, LinkedIn, X (as a fallback to Twitter Cards), Slack, WhatsApp
and similar apps all read it.

```html
<meta property="og:title" content="What Is a Runtime Control Plane?">
<meta property="og:description" content="How teams change what users experience in production without redeploying.">
<meta property="og:image" content="https://example.com/og/runtime-control-plane.png">
<meta property="og:url" content="https://example.com/blog/runtime-control-plane">
<meta property="og:type" content="article">
<meta property="og:site_name" content="LaunchDarkly">
```

**Current best understanding: OG is a social-preview / share-CTR lever.
It is not a Google ranking factor, and there's no evidence it affects
AI-search retrieval, ranking, or citation.** Only a page that people
actually share gets much out of it. Fix OG after crawlability, canonicals,
content structure and schema.

## The tags

| Tag | Status | What it controls |
|---|---|---|
| `og:title` | Required (ogp.me minimum) | Preview headline |
| `og:type` | Required | `article` for posts, `website` for everything else |
| `og:image` | Required | Preview image; use an absolute HTTPS URL |
| `og:url` | Required | Should match the page's canonical URL |
| `og:description` | Optional, but set it | Text under the headline |
| `og:site_name` | Optional | Brand label on the card |
| `og:locale` | Optional | Language/region; set it for non-English pages |

If these are missing, platforms guess from whatever they can scrape, which
often yields the wrong title or a random image
([[siteimprove-open-graph-ai-search-visibility-2026]],
[[opengraph-io-og-tags-vs-schema]]).

## OG vs. meta description vs. schema

These three are often confused because they all live in the `<head>` and
all describe the page:

| Element | Consumed by | Job | How to test |
|---|---|---|---|
| Title tag + meta description | Search engines | SERP snippet (title is a ranking factor; description drives CTR) — see [[writing-meta-tags]] | SERP preview tools |
| Open Graph | Social/messaging platforms | Share preview card | Platform debuggers (Facebook Sharing Debugger, LinkedIn Post Inspector) |
| Schema.org JSON-LD | Search engines and other parsers | What the page *is* (Article, Product, FAQPage…); rich-result eligibility (not a guarantee) | Google Rich Results Test / schema validators |

Sources: [[opengraph-io-og-tags-vs-schema]],
[[siteimprove-open-graph-ai-search-visibility-2026]]. They aren't
alternatives. A page that gets shared *and* needs to rank should have all
three, and they should agree with each other (see the checklist).

## Does OG affect rankings or AI visibility?

- **Google rankings: no.** Google doesn't use OG as a ranking factor
  ([[searchatlas-open-graph-tags-best-practices]]). This matches
  [[ahrefs-site-audit-study-2023]], which treats incomplete OG (found on
  56% of domains) as a low-priority issue. Any benefit is indirect: a
  better card gets more share clicks, which *may* earn links.
- **AI search: no evidence either way.**
  [[siteimprove-open-graph-ai-search-visibility-2026]] argues AI search
  has four stages (retrieval → ranking → summarization → preview
  generation) and that OG only touches the last. The argument is
  plausible but comes with **no tests or data**. That puts OG in the same
  evidence bucket as [[meta-keywords-tag]] and [[llms-txt]] (see also
  [[geo-content-optimization-tactics]]): nobody has shown AI engines use
  it for selection. The head-level elements that *do* matter for AI
  retrieval are crawl access, canonicals, `<title>`, and structured data
  (see [[technical-seo-audit-checklist]] §5).
- **What's untested:** whether AI chat interfaces use `og:image` or
  `og:title` when they render their own citation or link cards. If they
  do, that would be a preview effect, not a selection effect. No
  ingested source has examined it.

## Conflicting Evidence

- **Claim**: OG tags help search rankings via "social signals."
  - Supported by: [[stream-open-graph-protocol-glossary]] (undated
    vendor glossary), asserted without evidence.
  - Contradicted by: [[searchatlas-open-graph-tags-best-practices]]
    (2022, updated 2026-01-26), which says it's "not a ranking factor";
    [[ahrefs-site-audit-study-2023]] (2023, 1M-domain audit), which
    treats OG as a social/CTR lever only.
  - **Current best guess**: not a ranking factor. Treat the only SEO
    upside as indirect (share CTR → possible links). Stream is the
    weakest of the three sources. Flagged but low-stakes.
- **Claim**: recommended `og:title` / `og:description` lengths and image
  size.
  - [[stream-open-graph-protocol-glossary]]: title 60–75 chars,
    description <200 chars, image "1200×630 or smaller."
  - [[searchatlas-open-graph-tags-best-practices]]: title 40–60 chars,
    description 120–160 chars, 1.91:1 image with width/height tags.
  - **Current best guess**: platforms truncate differently and none of
    these ranges is platform-documented. A title of ~60 chars or less
    and a description of ~155 chars or less (the same budgets as
    [[writing-meta-tags]]) are safe everywhere. For images use 1.91:1 at
    **at least** 1200×630. Stream's "or smaller" is likely backwards:
    smaller images tend to render as small thumbnails rather than
    full-width cards. Unresolved; this is spec folklore, not evidence.
- **Claim**: schema markup is the "meaning layer" for AI systems.
  - Supported by: [[siteimprove-open-graph-ai-search-visibility-2026]]
    (2026-08-24), asserted.
  - Tension with: [[traditional-seo-ranking-factors]], where schema
    shows only weak correlation with organic rankings.
  - **Current best guess**: schema is a comprehension and eligibility
    aid, not a ranking lever. Its specific AI-citation effect isn't
    established by these sources. Noted here only as context for the OG
    comparison; not resolved.

## Implementation checklist

**Why / when:** for any page template that gets shared on social,
Slack or in email (blog posts, launch and campaign pages, product
pages, docs landing pages). Low priority for pages nobody shares.
Build it into templates once rather than fixing page by page.

- [ ] The four required tags on every shareable template: `og:title`,
      `og:type`, `og:image`, `og:url`. Add `og:description` and
      `og:site_name`.
- [ ] `og:url` equals the `rel="canonical"` URL.
- [ ] `og:title` agrees with the H1, `<title>`, and schema
      `headline`/`name`. It can be punchier, but not about something
      else.
- [ ] `og:image` is an absolute HTTPS URL, 1.91:1, at least 1200×630,
      set deliberately rather than whatever the CMS happens to pick. Ideally
      it's the same primary image declared in schema (also used as the
      preferred image by Google — see [[image-seo-checklist]]).
- [ ] `og:type` is `article` for posts and `website` for everything else.
- [ ] Set Twitter/X card tags where the X card needs to differ; otherwise
      X falls back to OG.
- [ ] Metadata QA in the publishing workflow: check the card in the
      platform debuggers. After changing tags, **re-scrape** in the
      debugger, because platforms cache previews.
- [ ] Don't prioritize OG over crawl access, canonicals, content clarity
      or schema ([[siteimprove-open-graph-ai-search-visibility-2026]]).

## Sources

- [[stream-open-graph-protocol-glossary]]: basic definition, 2010
  origin (low rigor)
- [[siteimprove-open-graph-ai-search-visibility-2026]]: "no AI-visibility
  effect" argument, three-layer model, prioritization (opinion, no data)
- [[searchatlas-open-graph-tags-best-practices]]: tag specs, "not a
  ranking factor" (vendor, dated platform list)
- [[opengraph-io-og-tags-vs-schema]]: OG vs. schema comparison, caching
  and testing tips (vendor)
- [[ahrefs-site-audit-study-2023]]: OG is incomplete on 56% of domains;
  a low-priority issue
