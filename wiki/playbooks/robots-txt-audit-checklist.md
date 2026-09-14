---
type: playbook
tags: [seo]
updated: 2026-09-10
---

# Robots.txt Audit Checklist

Robots.txt is a crawl-management tool, not an indexing-control tool. Audit your robots.txt to optimize crawler allocation to important pages and prevent wasted crawl budget. Use `noindex` for actual indexing control.

**When to use:** During technical SEO audits, after site migrations, when adding new sections, or when troubleshooting crawl issues. Run this quarterly to catch rule drift.

## Existence & Accessibility

- [ ] Verify robots.txt exists at `https://yoursite.com/robots.txt`
- [ ] robots.txt must be in the **root directory only** (not `/blog/robots.txt` or other subdirectories)
- [ ] Test accessibility: Visit the URL directly; should return 200 and plain text, not HTML error pages
- [ ] Avoid password-protecting robots.txt (defeats the purpose; Googlebot needs to read it)
- [ ] Check for HTTPS/HTTP mismatch: same directives on both?

## Syntax & Format

- [ ] File location: Root directory only (`domain.com/robots.txt`), NOT subdirectories
- [ ] File size: Check that robots.txt is under ~500KB (rarely an issue)
- [ ] Valid structure: Start with `User-agent:` declarations (use `*` for all, or specific crawlers: Googlebot, Bingbot, Slurp, Baiduspider, DuckDuckBot)
- [ ] Disallow rules: Format is `Disallow: /path/` (leading slash required)
- [ ] **Trailing slashes CRITICAL**: 
  - `Disallow: /de/` = blocks only `/de/` directory
  - `Disallow: /de` = blocks `/de/`, `/designer-dresses/`, `/delivery-info.html` (DANGEROUS overgeneralization)
- [ ] Allow rules: `Allow: /path/` to permit subdirs within blocked areas
- [ ] Pattern matching: Use `*` for wildcard, `$` for end-of-string (e.g., `Disallow: /*?*` blocks all query strings)
- [ ] Each rule on its own line
- [ ] Comments: Start with `#` and on their own line (no HTML, no extra formatting)
- [ ] Sitemap reference: Include `Sitemap: https://domain.com/sitemap.xml` for discovery
- [ ] Test syntax via Google Search Console's robots.txt tester
- [ ] For subdomains: Maintain separate robots.txt per subdomain (e.g., `blog.domain.com/robots.txt`)

## Crawl Optimization Rules

- [ ] **Exclude parameter/session URLs**: Block query strings that create duplicate content (`Disallow: /*?*` or specific params)
- [ ] **Block admin/staging**: Disallow `/admin/`, `/wp-admin/`, `/staging/`, `/test/`, `/temp/`
- [ ] **Block search results pages**: Disallow `/search/`, `/results/`, `/query/`, site-internal search
- [ ] **Block thin pages**: Disallow low-value archives, pagination, or auto-generated pages Googlebot wastes time on
- [ ] **Allow canonical versions**: If you have duplicates (e.g., with/without trailing slash), make sure canonical version is NOT blocked
- [ ] **PDF/binary files**: Consider blocking large PDFs if they're not core content (saves crawl budget)
- [ ] **AJAX/JavaScript endpoints**: Block JavaScript-rendered URLs that serve content via JS (Googlebot prefers static HTML)

## Media-Specific Rules

- [ ] **Images**: If you block images with `Disallow: /images/`, they won't appear in Google Image Search (intentional)
- [ ] **Videos/audio**: Similar rule applies—blocking may prevent appearance in specialized results
- [ ] **User-generated content**: If you want to crawl but not rank `/user-uploads/`, use `robots.txt` + `noindex` on those pages

## Avoid Common Mistakes

**Critical:** One character out of place can damage SEO performance. Review carefully.

- [ ] **Trailing slash errors** (DANGEROUS):
  - ❌ `Disallow: /de` blocks `/de/`, `/designer-dresses/`, `/delivery-info.html` (unintended)
  - ✅ `Disallow: /de/` blocks only the `/de/` directory (intended)
  - Always use trailing slashes for directory-specific blocks

- [ ] **Overly broad directives**:
  - ❌ `Disallow: /` (blocks entire site)
  - ❌ `Disallow: /p` (blocks /page/, /product/, /pricing/)
  - ✅ `Disallow: /private/` (specific, directory-scoped)

- [ ] **Don't use robots.txt for security**: It doesn't hide content. Use password protection for truly private files.

- [ ] **Don't block internal links**: If a URL is internally linked, blocking it in robots.txt wastes crawl budget and sends mixed signals

- [ ] **Don't use robots.txt for indexing control**: Blocked URLs can still be indexed if externally linked. Use `noindex` meta tag or `X-Robots-Tag: noindex` header instead.

- [ ] **Don't forget `Allow` rules**: Permit subsets within blocked directories (e.g., `Disallow: /private/` then `Allow: /private/public-docs/`)

- [ ] **Pattern-matching clarity**: When using `*` or `$`, test via GSC tester to confirm intended scope

## Monitoring & Testing

- [ ] **Google Search Console robots.txt tester**: Verify each rule works as intended (test one rule at a time for clarity)
- [ ] **GSC URL Inspection tool**: Check if important URLs are blocked by robots.txt (red flag: "Blocked by robots.txt")
- [ ] **GSC Coverage report**: 
  - Monitor for "Crawled - currently not indexed" URLs that shouldn't be blocked
  - Look for unexpected drops in crawled page count (may indicate robots.txt over-blocking)
- [ ] **GSC submitted vs. indexed**: Are submitted URLs being indexed? If not, robots.txt may be the culprit
- [ ] **Server logs**: Check HTTP logs for 401/403 responses from Googlebot (indicates robots.txt denials)
- [ ] **Real-world test**: Temporarily remove a `Disallow` rule for low-priority content and monitor crawl frequency in GSC (should increase)
- [ ] **Backup & version control**: Keep robots.txt in version control; track changes over time to catch accidental blocks
- [ ] **Dangerous mistakes check**: Manually review all `Disallow` rules for trailing-slash errors or overly broad patterns

## Referencing in robots.txt

- [ ] Include a reference to your sitemap(s) at the end:
  ```
  User-agent: *
  Disallow: [your rules]
  
  Sitemap: https://yoursite.com/sitemap_index.xml
  ```
- [ ] This helps crawlers discover your sitemaps efficiently

## When crawl budget is abundant (large sites)

- [ ] Keep robots.txt minimal: only block truly wasteful paths
- [ ] Let Googlebot crawl freely; it's smart about discovering important pages
- [ ] Use robots.txt for parameter cleanup, not for content filtering

## When crawl budget is constrained (new/small sites)

- [ ] Block aggressively: `/admin/`, `/staging/`, all duplicates, parameter pages
- [ ] Every blocked directive saves crawl for canonical, unique content
- [ ] Prioritize blocking over allowing

## Related pages

- [[ai-assistants-robots-txt-compliance-2026]] — empirical evidence
  that several AI assistants (DeepSeek, Gemini, Grok, Qwen) don't
  reliably respect robots.txt disallow rules, and that generic
  user-agents can make assistant-specific rules unenforceable.
- [[robots-txt-strategy]] — What robots.txt is, what it's NOT, misconceptions, syntax, directives, user-agents
- [[technical-seo-audit-checklist]] — Broader crawl/index/serve audit; robots.txt is one section
- [[how-google-search-works]] — Crawl stage and how robots.txt fits in the pipeline
- [[google-robots-txt-intro]] — Official Google guidance on robots.txt purpose and limitations
- [[ahrefs-robots-txt-guide]] — Practical syntax rules, dangerous mistakes (trailing slashes), GSC auditing
