---
type: playbook
tags: [seo]
updated: 2026-09-10
---

# XML Sitemap Optimization Checklist

Per [[oncrawl-xml-sitemap-optimization]]. Ensure your sitemaps maximize crawl efficiency by including only pages that drive SEO value and excluding waste. Sitemaps drive ~20% of URL discovery; optimizing their content directly impacts crawl budget allocation to your most important pages.

**When to use:** During technical SEO audits, site restructures, or before major URL cleanup efforts. Run this monthly to catch crawl-budget waste from orphaned or noindexed URLs making it into sitemaps.

## 6-Point Optimization Checklist

### 1. Include only money pages
- [ ] Verify every URL in the sitemap is intended for ranking/indexing
- [ ] Exclude duplicate/mirror pages, testing domains, staging URLs
- [ ] Remove pages that don't drive business value (archived content, admin pages, PDF metadata pages)
- [ ] Focus sitemap on your core content inventory

### 2. Exclude non-200 responses
- [ ] Audit all sitemapped URLs for HTTP status codes (use GSC Sitemaps report or crawl audit tool)
- [ ] Remove 404s, 500s, 301 redirects, 503s immediately
- [ ] Fix any 30x redirect chains before re-sitemapping
- [ ] Redirect waste = crawl budget waste; don't make Googlebot waste cycles on redirects

### 3. Remove noindexed pages
- [ ] Never include pages marked with `noindex` or `<meta name="robots" content="noindex">`
- [ ] Audit via crawl tool or GSC; cross-check against live page headers
- [ ] Sitemapped noindexed pages signal confusion and waste crawl budget

### 4. Exclude canonicalized URLs
- [ ] Don't sitemap pages with `rel="canonical"` pointing elsewhere
- [ ] Sitemap only the canonical version of URL clusters
- [ ] Remove self-referential canonicals or redirect chains
- [ ] Let Google discover alternate versions via link-following; sitemaps should point to canonical targets only

### 5. Follow XML protocol
- [ ] Validate XML syntax: proper `<urlset>` tags, namespace declarations (`xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"`)
- [ ] Ensure every `<url>` entry has a `<loc>` child tag with absolute URL
- [ ] Use optional `<lastmod>` for pages with frequent updates (helps prioritize crawl)
- [ ] Use sitemap index files for sites >50,000 URLs or >50MB (uncompressed)

### 6. Organize by site section
- [ ] Create separate sitemap files per major section: `/sitemap-blog.xml`, `/sitemap-products.xml`, `/sitemap-resources.xml`
- [ ] Use sitemap index file (`sitemap_index.xml`) to list all child sitemaps
- [ ] Benefits: GSC Sitemaps report shows discovered/indexed counts *per section*, making it easy to spot indexation gaps
- [ ] Easier to diagnose section-specific crawl problems

## Submission & Monitoring

- [ ] Submit all sitemaps (or sitemap index) to Google Search Console
- [ ] Submit to Bing Webmaster Tools (different crawl patterns)
- [ ] Check GSC "Sitemaps" report monthly:
  - Are discovered URL counts as expected?
  - Are indexed URL counts growing? (If flat, indexation problem elsewhere)
  - Any errors/warnings? (Malformed XML, non-200 responses, noindex pages)
- [ ] Reference sitemap in `robots.txt` for extra discoverability: `Sitemap: https://yoursite.com/sitemap_index.xml`

## Why this matters

Per Google's own analysis, sitemaps drive ~20% of URL discovery. The other 80% comes from following links. Optimized sitemaps:
- **Direct crawl budget** to your most valuable URLs (remove junk → more crawls of real content)
- **Signal importance** through organized sections (products/blog/resources)
- **Reduce crawl waste** on 404s, redirects, and noindexed pages
- **Enable GSC monitoring** per section so you can spot indexation gaps quickly

## Related pages

- [[oncrawl-xml-sitemap-optimization]] — the source this checklist is
  built from.
- [[google-sitemaps-overview]] — Strategic role of sitemaps, metadata types, when to create
- [[technical-seo-audit-checklist]] — Broader crawl/index/serve audit; sitemaps are one subsection
- [[how-google-search-works]] — Crawling stage and crawl budget mechanics
