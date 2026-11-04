---
type: source
tags: [seo]
date_published: 2026-03-02  # living doc; page "Last updated" date, checked 2026-11-04
date_ingested: 2026-07-11
origin: raw/articles/google-images-seo.md
---

Google, "Google Images and Google Search" (official developer documentation).

## Key takeaways

- Google Images discovery uses computer vision + page context, and only
  indexes images referenced via standard `<img src>` (including inside
  `<picture>`) — **CSS background images are never indexed**. Supported
  formats: BMP, GIF, JPEG, PNG, WebP, SVG, AVIF.
- **Image sitemaps** surface images Google might not otherwise discover,
  including CDN-hosted images on other domains — extends the wiki's
  existing sitemap guidance ([[xml-sitemap-optimization-checklist]],
  [[google-sitemaps-overview]]) with an image-specific use case.
- **Responsive images**: use `srcset`/`<picture>`, always with a
  fallback `src` (some crawlers/browsers don't parse those attributes).
- **Alt text is "the most important attribute"** for image metadata:
  informative and specific, never keyword-stuffed. Confirms/extends
  [[ahrefs-site-audit-study-2023]]'s finding that missing alt attributes
  are the single most common technical SEO issue (80.4% of sites) — this
  source gives the positive guidance (what good alt text looks like) to
  pair with that prevalence data.
- Filenames should be short/descriptive, not generic (`image1.jpg`).
- A **preferred/canonical image** can be declared via `schema.org`
  `primaryImageOfPage` or `og:image` — avoid generic images, extreme
  aspect ratios, or generic logos as the designated image.
- Structured data can make images eligible for Google Images rich
  results/badges (image properties become mandatory fields in that
  markup).

## Created

- [[image-seo-checklist]] — new playbook consolidating this guidance
  into an actionable checklist, cross-linked to the sitemap and
  technical-audit playbooks.
