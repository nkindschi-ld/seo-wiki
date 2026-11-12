---
type: playbook
tags: [seo]
updated: 2026-11-12
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

- File location: root directory only (see Existence & Accessibility above)
- [ ] File size: Check that robots.txt is under ~500KB (rarely an issue)
- [ ] Valid structure: Start with `User-agent:` declarations (use `*` for all, or specific crawlers: Googlebot, Bingbot, Slurp, Baiduspider, DuckDuckBot)
- [ ] Disallow rules: Format is `Disallow: /path/` (leading slash required)
- **Trailing slashes CRITICAL**: see the trailing-slash item under Avoid Common Mistakes below
- [ ] Allow rules: `Allow: /path/` to permit subdirs within blocked areas
- [ ] Pattern matching: Use `*` for wildcard, `$` for end-of-string (e.g., `Disallow: /*?*` blocks all query strings)
- [ ] Each rule on its own line
- [ ] Comments: Start with `#` and on their own line (no HTML, no extra formatting)
- Sitemap reference: see Referencing in robots.txt below
- [ ] Check for parse errors in Search Console's robots.txt report (see Monitoring & Testing below)
- [ ] For subdomains: Maintain separate robots.txt per subdomain (e.g., `blog.domain.com/robots.txt`)

## Crawl Optimization Rules

- [ ] **Exclude parameter/session URLs**: Block query strings that create duplicate content (`Disallow: /*?*` or specific params)
- [ ] **Block admin/staging**: Disallow `/admin/`, `/wp-admin/`, `/staging/`, `/test/`, `/temp/`
- [ ] **Block search results pages**: Disallow `/search/`, `/results/`, `/query/`, site-internal search
- [ ] **Block thin pages**: Disallow low-value archives or auto-generated pages Googlebot wastes time on. **Don't block pagination**: paginated pages need to stay crawlable (real `<a href>` links, each canonicalized to itself) so Google can reach the items listed on them; see [[link-and-anchor-text-best-practices]]. _Corrected 2026-11-12: an earlier version listed pagination as something to disallow._
- [ ] **Allow canonical versions**: If you have duplicates (e.g., with/without trailing slash), make sure canonical version is NOT blocked
- [ ] **PDF/binary files**: Consider blocking large PDFs if they're not core content (saves crawl budget)
- [ ] **JavaScript and CSS resources**: Don't block the JS, CSS or API endpoints a page needs to render. Google renders JavaScript with a recent Chrome, so blocking those resources can stop it seeing JS-dependent content; see [[how-google-search-works]]. _Corrected 2026-11-12: an earlier version said to block JavaScript-rendered URLs because Googlebot prefers static HTML._

## Media-Specific Rules

- [ ] **Images**: If you block images with `Disallow: /images/`, they won't appear in Google Image Search (intentional)
- [ ] **Videos/audio**: Similar rule applies—blocking may prevent appearance in specialized results
- [ ] **User-generated content**: If you want `/user-uploads/` crawled but not indexed, use `noindex` on those pages and **don't** disallow them in robots.txt. A disallowed URL is never fetched, so Google can't see its `noindex` and may still index the bare URL (see "Don't use robots.txt for indexing control" below and [[robots-txt-strategy]]). _Corrected 2026-11-12: an earlier version recommended robots.txt + `noindex` together._

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

- [ ] **Pattern-matching clarity**: When using `*` or `$`, test sample URLs against the rules (URL Inspection live test, or Google's open-source robots.txt parser) to confirm intended scope

## Monitoring & Testing

- [ ] **GSC robots.txt report**: Confirm Google fetched the current file for each host, and check its warnings and errors. This report replaced the robots.txt Tester, which Google retired in November 2023 ([robots.txt report help](https://support.google.com/webmasters/answer/6062598)). It has no interactive rule tester, so check individual URLs with URL Inspection (next item).
- [ ] **GSC URL Inspection tool**: Check if important URLs are blocked by robots.txt (red flag: "Blocked by robots.txt"); the live test checks a URL against the current rules
- [ ] **GSC Page indexing report** (formerly the Coverage report; [help](https://support.google.com/webmasters/answer/7440203)):
  - Review URLs under "URL blocked by robots.txt" for anything that shouldn't be blocked
  - Review "Indexed, though blocked by robots.txt": these are indexed without being crawled, so they need `noindex` (and the block removed) if you want them out
  - Look for unexpected drops in crawl activity in the Crawl Stats report (may indicate robots.txt over-blocking)
- [ ] **GSC submitted vs. indexed**: Are submitted URLs being indexed? If not, robots.txt may be the culprit
- [ ] **Server logs**: A URL disallowed in robots.txt is never requested, so it doesn't show up in logs at all. 401/403 responses to Googlebot are server-side denials (auth, firewall or bot blocking), not robots.txt; check that they aren't hitting pages you want crawled. Also check the robots.txt fetch itself: Google treats any 4xx on robots.txt except 429 as "no robots.txt" (no restrictions), and a 5xx as a reason to pause crawling ([Google robots.txt spec](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt)). _Corrected 2026-11-12: an earlier version said 401/403s indicate robots.txt denials._
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

## Small and new sites (crawl budget rarely matters)

- [ ] Keep robots.txt minimal: only block truly wasteful paths (admin, staging, internal search)
- [ ] Let Googlebot crawl freely; it's smart about discovering important pages
- [ ] Keep the sitemap current and watch the Page indexing report; per Google, that's adequate for sites without a large number of rapidly changing pages

## Large or fast-changing sites (crawl budget can be a constraint)

Google's crawl-budget guide applies roughly to sites with 1M+ unique pages changing about weekly, or 10K+ pages changing daily, or many URLs stuck in "Discovered - currently not indexed" ([Google crawl budget guide](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget)).

- [ ] Block large wasteful URL spaces: parameter/faceted duplicates, session IDs, internal search results
- [ ] Use robots.txt (not `noindex`) for URLs you never want crawled; `noindex` pages are still fetched, which spends crawl
- [ ] Don't block pages temporarily to "free up" budget for others: Google only reallocates it if you're already at your crawl capacity limit
- [ ] Use robots.txt for parameter cleanup, not for content filtering

_Corrected 2026-11-12: an earlier version said to block aggressively on new or small sites and to keep robots.txt minimal on large ones. Google's guidance is the reverse: crawl budget is mainly a large-site concern._

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
