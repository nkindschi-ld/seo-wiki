# Open Graph Protocol - What is it and how does it work?

Publication: Stream (getstream.io) Glossary
Author: none listed
Publication Date: none listed (retrieved 2026-09-23)
Source: https://getstream.io/glossary/open-graph-protocol/

## Overview

The Open Graph (OG) protocol is a standardized metadata framework that lets web
pages appear as rich link previews when shared on social media. Facebook
developed the standard in 2010 to replace inconsistent, non-standardized
approaches to link previews.

## How it works

OG tags are meta tags embedded in the page's HTML `<head>`. When a URL is
shared on a social platform, the platform's crawler reads these tags to build a
preview card.

## Essential tags

Core required:
- `og:title` — preview heading, e.g. `<meta property="og:title" content="Find Your Perfect Match Today" />`
- `og:type` — object category (website, article, book, video)
- `og:image` — preview image URL
- `og:url` — the page's canonical URL

Optional: `og:site_name`, `og:description`, `og:video`, `og:locale`.

## Implementation best practices (as stated)

- Titles between 60–75 characters
- Descriptions under 200 characters
- Images 1200x630px "or smaller"
- Use canonical URLs only in `og:url`
- Test with Facebook Sharing Debugger or similar
- Implement platform-specific tags (Twitter/X Cards) alongside OG

## Claimed benefits

- Better social appearance and click-through rates
- "Improved social signals supporting search engine rankings" (no evidence cited)
- Increased organic backlink potential
- Consistent cross-platform previews
- Trackable engagement analytics

## Current status

OG remains the active standard for link rendering on Facebook, LinkedIn,
Twitter/X and similar platforms.

## Extraction note

Vendor glossary page (Stream sells chat/activity-feed APIs). No author, date,
sources, or data.
