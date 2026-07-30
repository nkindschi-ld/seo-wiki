---
type: concept
tags: [seo]
updated: 2026-07-23
---

# Robots.txt Strategy: What It Is, What It Isn't

Robots.txt is a crawler-management tool that lives in your site root and tells search engines which URLs they *can* crawl. It is **not** a hiding mechanism, indexing control tool, or security barrier—a widespread misconception that leads to misuse.

## What robots.txt actually does

- **Manages crawler traffic**: Tells Googlebot (and other crawlers) which URLs to crawl, helping prevent server overload
- **Optimizes crawl allocation**: Directs crawler resources toward important content, away from duplicate/parameter pages
- **Controls media appearance**: Prevents images, videos, and audio from appearing in Google's image/video results
- **Reduces redundant crawling**: Keeps crawlers out of admin areas, staging sites, search results pages, test URLs, etc.

## File structure & syntax

- **Location**: Must be in site root: `domain.com/robots.txt` (not subdirectories)
- **Size limit**: ~500KB max (rarely an issue for most sites)
- **Format**: User-agent declarations followed by directives, one per line
- **Comments**: Use `#` for clarity; each comment on its own line

## User-agents (crawler targeting)

Robots.txt can target specific crawlers or all crawlers:

- **Googlebot** — Google's general search crawler
- **Googlebot-Image** — Google Image Search crawler (images only)
- **Bingbot** — Bing/Microsoft search crawler
- **Slurp** — Yahoo search crawler
- **Baiduspider** — Baidu (Chinese search engine)
- **DuckDuckBot** — DuckDuckGo crawler
- **`User-agent: *`** — Applies rules to all crawlers (wildcard, most common)

LLM/AI-chat products also publish their own user agents, distinct from
the training/indexing/retrieval bot taxonomy in
[[how-google-search-works]] — useful when deciding whether to allow or
block a specific LLM's crawler (per
[[wix-generative-engine-optimization]]):

| LLM | User agent |
|---|---|
| ChatGPT | `OAI-SearchBot`, `ChatGPT-User`, `GPTBot` |
| Copilot | `BingBot` |
| Gemini | `Google-Extended` (inferred — Google hasn't explicitly confirmed this maps to Gemini), `GoogleOther` |
| Claude | `ClaudeBot` |
| Perplexity | `PerplexityBot` |
| Andi | `AndiBot` |
| Exa | `ExaBot` |
| Phind | `PhindBot` |
| You.com | `YouBot` |
| Firecrawl (agent framework) | `FirecrawlAgent` |
| Common Crawl (training corpus used by many LLMs) | `CCBot` |

**Coverage gap**: this table doesn't yet document bots from Meta,
Amazon, xAI, ByteDance, Cohere, Mistral AI, DeepSeek, Allen Institute
for AI, Zhipu AI, or Apple. Per [[stackfox-ai-crawlers-directory]], a
living third-party directory tracks ~94+ AI/archive bots across ~28+
organizations, including all of the above — useful as a reference to
check the current fuller bot landscape, but verify exact user-agent
strings against each vendor's own crawler documentation before adding
them here (the directory's per-bot detail sits behind an interactive UI
this wiki couldn't fully extract).

These crawlers exist to help the LLM understand/summarize content
rather than to rank it — they generally don't need access to
navigation or pagination pages the way a ranking crawler benefits from;
prioritize their access to brand/product/service content instead.

**A three-category allow/disallow split**, per
[[sel-ai-optimization-content-for-search-and-agents]], is a practical
way to apply this distinction in an actual robots.txt file:

```
# Allow AI search/agent crawlers (real-time retrieval — help them cite you)
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: PerplexityBot
User-agent: FirecrawlAgent
User-agent: AndiBot
User-agent: ExaBot
User-agent: PhindBot
User-agent: YouBot
Allow: /

# Disallow AI training-data collection bots, if you don't want your
# content used to train a model (a separate decision from search visibility)
User-agent: GPTBot
User-agent: CCBot
User-agent: Google-Extended
Disallow: /

# Traditional search indexing
User-agent: Googlebot
User-agent: Bingbot
Allow: /

User-agent: *
Disallow: /admin/
Disallow: /internal/
Sitemap: https://www.domain.com/sitemap.xml
```

Also watch for **overly aggressive bot-protection services**
(Cloudflare, AWS WAF) blocking AI crawlers/agents outright at the
network layer, bypassing robots.txt entirely — allowing major U.S.
datacenter IP ranges is one mitigation if a WAF is blocking legitimate
AI crawlers. This is the same third-party-blocking risk already flagged
in [[technical-seo-audit-checklist]] (via
[[ahrefs-beginner-guide-technical-seo]]), extended here with a concrete
fix.

Example targeting a specific crawler:
```
User-agent: Googlebot
Disallow: /admin/

User-agent: Bingbot
Disallow: /staging/

User-agent: *
Disallow: /private/
```

## Directives (core rules)

### Disallow
Prevents crawler access to a path:
```
Disallow: /admin/
Disallow: /staging/
Disallow: /temp/
```

### Allow
Permits access to subdirectories within a blocked path. Useful for granular control:
```
Disallow: /blog/
Allow: /blog/public-posts/
```
(Blocks everything in `/blog/` except `/blog/public-posts/`)

### Sitemap
References sitemap location for better discovery:
```
Sitemap: https://www.domain.com/sitemap.xml
Sitemap: https://www.domain.com/sitemap-news.xml
```

## Syntax gotchas

- **Trailing slashes matter**: 
  - `Disallow: /de/` blocks only the `/de/` directory
  - `Disallow: /de` blocks `/de/`, `/designer-dresses/`, `/delivery-info.html` — dangerous overgeneralization
- **Pattern matching**:
  - `*` = wildcard (matches anything)
  - `$` = end-of-string (exact match)
  - Example: `Disallow: /*?*` blocks all URLs with query parameters
- **One character misplaced** = SEO damage. Double-check trailing slashes and prefixes

## Subdomain strategy

Maintain separate robots.txt for each subdomain:
- `domain.com/robots.txt`
- `blog.domain.com/robots.txt`
- `staging.domain.com/robots.txt`

Each subdomain has its own root; robots.txt doesn't cascade.

## Critical misconception: robots.txt does NOT prevent indexing

**This is the #1 robots.txt mistake.** Even if a URL is blocked in robots.txt:
- Google can still crawl and index it if another website links to it
- It may appear in search results (though "without a description," since Google can't access the page)
- It wastes your robots.txt directive

Example: You block `/admin/` in robots.txt. Another site links to `/admin/user123`. Google may still index that URL—robots.txt has no authority over incoming links.

### For actual indexing prevention, use:
1. **`noindex` meta tag** — Most reliable for HTML pages
2. **`X-Robots-Tag: noindex` HTTP header** — For PDFs, images, API responses
3. **Password protection** — Prevents crawling entirely (most secure)
4. **Content removal** — Delete the page from your server
5. **HTTPS + robots.txt** — Prevents Googlebot from seeing robots.txt (only for truly private content)

## What it can do by type

### HTML/PDF web pages
- Manage crawl traffic and server load
- Save crawl budget for canonical content
- **Cannot** hide from search results (if externally linked)

### Images/videos/audio
- Prevent from appearing in Google Image Search, Video Search results
- **Cannot** stop others from linking to them
- **Cannot** prevent Googlebot from discovering them via other sites' links

## Key limitations

1. **Not universal**: Not all crawlers respect robots.txt (bad actors, AI crawlers, etc.)
2. **Syntax interpretation varies**: Different crawlers may handle edge cases differently
3. **Linkage overrides it**: External backlinks can bypass your robots.txt rules
4. **No security value**: Google treats it as advisory only, not a security boundary
5. **Crawler still sees directives**: Googlebot still accesses robots.txt to read your rules (it's not hidden from crawlers)

## Conflicting Evidence

Some SEO practitioners recommend using robots.txt as a "quick fix" for duplicate content or low-quality pages. This is technically true for *crawl optimization* (saving budget for better pages) but **false** for *indexing control*. The wiki follows Google's official stance: use robots.txt for crawl management, use `noindex` for indexing control.

## Related pages

- [[robots-txt-audit-checklist]] — Operational audit checklist with syntax rules, dangerous mistakes, GSC monitoring
- [[technical-seo-audit-checklist]] — Broader crawl/index/serve audit; robots.txt is one section
- [[how-google-search-works]] — Crawl stage and crawl budget allocation
- [[google-robots-txt-intro]] — Official Google guidance on robots.txt purpose and limitations
- [[ahrefs-robots-txt-guide]] — Practical implementation details, trailing-slash syntax gotchas, common mistakes
- [[sel-ai-optimization-content-for-search-and-agents]] — the source for the extended AI-bot-name table and three-category allow/disallow template above
