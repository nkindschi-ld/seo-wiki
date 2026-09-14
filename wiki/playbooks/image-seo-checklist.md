---
type: playbook
tags: [seo]
updated: 2026-09-04
---

## File type selection

- **JPEG**: photographs and complex images (lossy, smallest files).
- **PNG**: line drawings, text, icons (lossless, larger than JPEG).
- **GIF**: animated images (limited color palette).
- **SVG**: logos, icons, simple vector art — scalable without quality
  loss; minify and enable GZIP compression (verify with
  checkgzipcompression.com).
- **WebP/AVIF**: superior compression on supporting browsers.

Why / when to use this: image search (Google Images tab, Discover, and
image results embedded in text SERPs) is a distinct discovery/ranking
surface with its own technical requirements — use this alongside
[[technical-seo-audit-checklist]] (general crawlability) and
[[xml-sitemap-optimization-checklist]] (sitemap strategy) when auditing
a site's images or launching an image-heavy page.

## Markup requirements

- Use standard `<img src>` elements (including inside `<picture>` for
  responsive variants) — **Google does not index CSS background
  images**, so any image conveying real content must be a real `<img>`
  tag, not a `background-image` style.
- Supported formats: BMP, GIF, JPEG, PNG, WebP, SVG, AVIF.
- Responsive images: use `srcset` or `<picture>`, and always include a
  fallback `src` — some crawlers/browsers don't parse those attributes.

## Discoverability

- Submit an **image sitemap** to surface images Google might not
  otherwise crawl, including images served from a separate CDN domain
  (see [[xml-sitemap-optimization-checklist]] for general sitemap
  hygiene). Use the `<image:loc>`, `<image:title>`, and
  `<image:caption>` tags; Yoast SEO auto-generates these for WordPress.
- Position images near the text they're relevant to, on a page
  topically aligned with the image subject — context is part of how
  Google's computer-vision + page-context system understands the image.

## Descriptive metadata (highest-impact items)

- **Alt text** is the single most important image attribute. Write
  specific, informative descriptions ("Dalmatian puppy playing fetch"),
  never keyword-stuffed, and never omit it — missing alt attributes are
  the most common technical SEO issue found across audited sites (80.4%
  of sites per [[ahrefs-site-audit-study-2023]]), so this is a
  near-universal quick win. Authoring formula: complete "This is a(n)
  ___ of ___" and use the result as alt text; include product numbers
  for product images. Don't skip alt text just because ML image
  understanding has improved — Google's own Cloud Vision API nailed cat
  photos but confused butter for cheese at 91% confidence, so text
  context still matters. Add captions where they help.
- **Filenames**: short and descriptive (`black-labrador-puppy.jpg`), not
  generic (`IMG_00234.jpg`, `image1.jpg`).
- **Preferred image declaration**: mark the canonical image for a page
  via `schema.org` `primaryImageOfPage` or the `og:image` meta tag.
  Avoid generic stock images, extreme aspect ratios, or generic logos
  as that designated image.
- **Structured data**: adding relevant structured data (recipe, product,
  article, etc.) can make a page's images eligible for rich
  results/badges in Google Images — check the type-specific schema for
  which image properties are mandatory.

## Quality and performance

- High-resolution, sharp images outperform blurry/low-quality ones for
  user engagement.
- **Resize to display dimensions** — upload at max display width only;
  don't ship an oversized original and rely on CSS to shrink it.
- **Compress aggressively** — Google's own advice: "don't be afraid to
  dial down quality." Benchmark (default settings, JPEG/PNG reduction):
  ImageOptim 69%/40%, ShortPixel 42%/59%, TinyPNG 27%/65%. Optionally
  preserve EXIF data where it supports local SEO. Verify with PageSpeed
  Insights.
- **Lazy-load** below-the-fold images to speed long, image-heavy pages
  (PageSpeed Insights recommends this; WordPress: A3 Lazy Load).
- **Browser caching**: set expiration headers so repeat visits load
  faster (WordPress: W3 Total Cache; otherwise via `.htaccess`).
- **CDN**: serve images from a server geographically close to users
  (Cloudflare, KeyCDN, CloudFront, Google Cloud CDN, or an image CDN
  like Cloudinary/imgix for automated optimization). Use a CNAME
  (`cdn.yourdomain.com`) rather than linking directly from a bare CDN
  domain, or the CDN's domain — not yours — accrues the SEO value.

## Link equity recovery (bonus tactic)

- Find backlinks that point directly at an image file (`.jpg`, `.png`,
  `.gif`) rather than the article it's embedded in (e.g. via Ahrefs Site
  Explorer). Reach out to ask the linking site to point to the source
  article instead — this outreach reportedly converts well, since
  you're recovering equity from a link that already exists.

## SafeSearch

- Make sure the surrounding page content clearly signals your site's
  content nature, so SafeSearch filtering is applied correctly to your
  images.

## Checklist

- [ ] Content images are real `<img>` elements, not CSS backgrounds
- [ ] Responsive images use `srcset`/`<picture>` with a fallback `src`
- [ ] Image sitemap submitted (especially for CDN-hosted images)
- [ ] Every content image has specific, non-keyword-stuffed alt text
- [ ] Filenames are descriptive, not generic
- [ ] Preferred image declared (`primaryImageOfPage` or `og:image`)
- [ ] Relevant structured data present where applicable
- [ ] Images resized to display dimensions and compressed (benchmarked tool)
- [ ] Below-the-fold images lazy-loaded
- [ ] Browser caching / expiration headers set
- [ ] CDN in use via CNAME (not bare CDN domain links)
- [ ] Checked Site Explorer for direct image-file backlinks to recover

## See also

- [[how-google-search-works]] — the parent concept: images have to be
  discovered, crawled, and indexed through the same pipeline as pages,
  which is why the discoverability items above come first.
- [[traditional-seo-ranking-factors]] — where image/page-speed and
  media signals sit among classic ranking factors.
- [[technical-seo-audit-checklist]] — the broader audit this checklist
  is the image-specific section of.

See [[google-images-seo]] and [[ahrefs-image-seo]] for the full source
writeups.
