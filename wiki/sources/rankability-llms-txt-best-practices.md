---
type: source
tags: [aeo, seo]
date_published: unknown
date_ingested: 2026-10-02
origin: raw/articles/rankability-llms-txt-best-practices.md
---

# LLMS.txt Best Practices & Implementation Guide (Rankability, undated)

**Citation:** Rankability. "LLMS.txt Best Practices & Implementation
Guide." Rankability blog, undated (earliest Wayback Machine capture
2026-04-18). https://www.rankability.com/blog/llms-txt-best-practices/

**Rigor note: low.** It's a vendor guide that funnels to Rankability's own
`llms.txt` generator and validator. It has no data or citations, and several
statements contradict the spec ([[llmstxt-org-proposal-v2-2026]]). Kept as a
record of common misconceptions and for its hosting how-tos. **It doesn't
support any claim on [[llms-txt]]**; it shows up only on the "supported by"
side of a conflict.

## Key takeaways

- **Unevidenced benefit claims:** "improved attribution in AI responses,"
  "control over content usage," "enhanced discoverability in AI systems."
  It frames the file as a robots.txt-like channel for "intended usage,"
  with "Usage Guidelines" and "Attribution Preferences" sections. The spec
  has no permission or attribution semantics.
- **Where it contradicts the spec:**
  - It says the file must be at the root and that `yoursite.com/seo/llms.txt`
    is a mistake. The spec allows subpaths, and v2 defines what they cover.
  - It marks the blockquote as "Required" and lists missing contact info as
    a mistake. Only the H1 is required.
  - Its templates put prose and contact details under H2s and use
    `- **Label**: [Title](URL) - description` link lines. Under the spec,
    H2 sections are link-only file lists of the form
    `- [Title](URL): notes`.
- **Unsourced numbers:** under 10KB, 10–20 key pages, under 200ms response
  time, 24-hour cache. None of these appear in the spec.
- **Usable parts:** hosting steps for static generators, WordPress (root
  upload or plugin), Shopify (theme asset) and custom routes. Serve it with
  HTTP 200 over HTTPS with no auth. Use clean URLs, not staging or query
  strings. Check it with `curl -I`. Review it quarterly and on
  restructures. Use language-specific files for multilingual sites.
- Its `text/plain` MIME recommendation is reasonable, though the spec
  doesn't specify one. Limy allows `text/markdown` as well.

## What this updated

- [[llms-txt]] Conflicting Evidence: on the "supported by" side of the
  AI-visibility-benefit claim, the root-only placement claim and the
  required-elements claim. The checklist's warning against
  `**Label**: [link]` and `link - description` patterns comes from its
  templates.
- No changes to existing claims elsewhere. It adds a third unevidenced
  pro-`llms.txt` voice alongside [[superlines-geo-guide]] and
  [[sel-ai-optimization-content-for-search-and-agents]].
