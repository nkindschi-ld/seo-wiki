---
type: source
tags: [seo, aeo]
date_published: 2026-07-30
date_ingested: 2026-08-06
origin: raw/articles/openai-publishers-developers-faq.md
---

# OpenAI — Publishers and Developers FAQ

**Citation:** OpenAI Help Center, "Publishers and Developers - FAQ"
(living document; "Updated 7 days ago" as of capture ≈ 2026-07-30).
https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
· Ingested 2026-08-06 (via in-app browser; the page 403s WebFetch).

**First-party / authoritative.** OpenAI's own publisher/developer
guidance for ChatGPT search and the ChatGPT Atlas agent. Part of a
three-source cluster with [[sel-accessibility-tree-seo-use-cases-2026]]
and [[microsoft-playwright-mcp]] — this is the primary source behind the
article's "OpenAI confirms agents read ARIA" claim.

## Key takeaways

- **Agents read ARIA / the accessibility tree (first-party confirmation):**
  "Making your website more accessible helps ChatGPT Agent in Atlas
  understand it better. ChatGPT Atlas uses ARIA tags — the same labels and
  roles that support screen readers — to interpret page structure and
  interactive elements." Guidance: follow WAI-ARIA best practices (roles,
  labels, states on buttons/menus/forms).
- **Three user agents by function (first-party):**
  - **OAI-SearchBot** — ChatGPT search indexing; allow it (in robots.txt)
    to be discoverable/cited/linked in ChatGPT search.
  - **GPTBot** — training; disallow it to exclude pages from potential
    training. Respected even for content acquired via Atlas user
    interactions (though user opt-in to training doesn't override a
    GPTBot opt-out).
  - **ChatGPT-User / ChatGPT Agent** — live user-triggered fetching /
    agent action in Atlas.
- **robots.txt ≠ suppression of the link itself:** if OpenAI gets a
  *disallowed* page's URL from a third-party search provider or via
  crawling other pages and has relevance signals, it may surface **just
  the link + page title in ChatGPT Atlas**. To prevent even that, use the
  **`noindex` meta tag** — but the page must be crawlable for the tag to
  be read (the same robots-blocks-the-noindex trap in
  [[robots-txt-strategy]]).
- **Referral tracking:** ChatGPT appends **`utm_source=chatgpt.com`** to
  referral URLs, so allowed publishers can track ChatGPT-search referral
  traffic in analytics (cf. [[seoclarity-track-ai-search-traffic]]'s
  GA4 regex method).
- **Apps SDK in Atlas:** naming an available app in a message surfaces it;
  test at Chat-sidebar widths.

## Pages created / updated

- Updated [[robots-txt-strategy]] — authoritative first-party detail on
  OAI-SearchBot vs GPTBot vs ChatGPT-User, and the noindex/Atlas
  link-surfacing nuance (upgrading the previously-inferred per-LLM table).
- Updated concept [[agentic-web-optimization]] — the ARIA/accessibility-
  tree perception mechanism.
- Supports playbook [[accessibility-tree-audit-for-ai-agents]].
