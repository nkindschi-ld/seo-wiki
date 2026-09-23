# Open Graph Tags: Implementation & Best Practices

Author: Manick Bhan (Founder, CEO/CTO, Search Atlas)
Publication: Search Atlas blog
Publication Date: 2022-09-12 (updated 2026-01-26)
Source: https://searchatlas.com/blog/open-graph-tags/

## Overview

OG tags are HTML meta tags that control how content appears when shared on
Facebook, LinkedIn, WhatsApp, etc. Described as functioning similarly to
schema.org markup (for social platforms). Contrasts a well-formatted shared
post with a tag-less one to illustrate CTR impact.

## Ranking / SEO impact

Claim: "Open Graph is not a ranking factor that Google relies on when promoting
web pages." Argues for *indirect* benefit only: better-formatted shares drive
engagement, which can lead webmasters to discover the content and link to it.

## Platforms listed

Facebook, LinkedIn, Google+ (defunct — stale list), WhatsApp, Slack. Notes
Twitter uses its own "Twitter Cards" (which in practice fall back to OG tags
when card tags are absent — not stated in the article).

## Required tags and specs

| Tag | Purpose | Best practice |
|---|---|---|
| `og:title` | Page title | 40–60 characters |
| `og:description` | Content summary | 120–160 characters |
| `og:image` | Visual | 1.91:1 aspect ratio; include width/height tags |
| `og:url` | Canonical URL | SEO-friendly format |
| `og:type` | Content category | `article` for blog posts, `website` for other pages |
| `og:locale` | Language | Set for non-English content |

## Common errors

1. Missing tags entirely (most frequent)
2. Titles/descriptions outside the recommended character ranges
(Both flagged by Search Atlas's own Site Audit tool.)

## Implementation

- CMS plugins: WordPress (Yoast SEO most common), Wix, Shopify plugins
- Manual: place tags in the page head; validate with an OG generator/debugger

## Statistics

No primary research. Page promotes unrelated Search Atlas client case studies
(e.g. orthodontist +472% organic traffic) that are not attributed to OG work.

## Extraction note

Vendor blog (Search Atlas sells an SEO platform). Originally 2022, lightly
updated 2026; platform list is dated.
