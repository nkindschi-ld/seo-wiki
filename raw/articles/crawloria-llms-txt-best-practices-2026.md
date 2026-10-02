# Crawloria: llms.txt Best Practices: 2026 Practical Guide

**Source:** https://www.crawloria.com/blog/llms-txt-best-practices
**Author:** Max Tsygankov, Founder, Crawloria (AI-crawlability audit / llms.txt generator vendor)
**Type:** Vendor blog guide
**Dates:** Published 2026-06-06
**Accessed:** 2026-10-02

---

TL;DR

- A useful llms.txt file is curated, current, and canonical: list the pages you most want quoted, in markdown, kept up to date, with one summary sentence each. 
- Skip thin pages, archived docs, marketing puffery, and broken links. Most failed llms.txt files fail in the same two or three ways. 
- No major AI provider has publicly confirmed their crawlers consume llms.txt yet. The case for publishing is low-cost insurance plus content-architecture discipline, not promised traffic. 
- Verified real-world adopters (Anthropic, Cloudflare, Vercel, Stripe, Cal.com, Supabase) show three repeated patterns: lean index, full-export companion, and product-vertical organization.   
If you already know what llms.txt is, this guide goes straight to the practices that separate a useful file from a dead one. If you don't, the companion piece llms.txt Explained: Who Uses It and Why covers the spec, the directory, and the decision tree for whether to publish at all.

The rest of this article assumes you have decided to publish. The question becomes: what makes the file actually pay off? The eight practices below are pulled from verified real-world implementations and the most useful framings in the current best-practices writing on the topic. A common-mistakes section at the end covers what to avoid.

## The honest case for publishing in 2026

Before the practices, set expectations honestly. As of late 2025, Semrush's server-log experiment found zero AI-crawler hits to a published llms.txt file in their test period, and Google's public position has been that no AI system formally uses llms.txt yet. Most major LLM providers have not confirmed their retrieval crawlers consume the file.

What is real: several infrastructure providers and dev-doc platforms publish their own llms.txt index (Cloudflare at developers.cloudflare.com/llms.txt is the canonical large example), and emerging developer-agent tools and custom retrieval pipelines do parse llms.txt when they encounter it. The toolchain is moving in that direction even where the major model providers have not committed publicly.

The net call: publish llms.txt as low-cost insurance and as a content-architecture forcing function, not as a promised traffic lift. The file takes an afternoon to ship, costs nothing to host, and gives you a clean curated index of your most important pages whether or not any AI eventually reads it. Skip it only if you can't keep it current; a stale llms.txt is worse than no llms.txt.

## Best practice 1: curate, do not dump

The most common mistake we see in published llms.txt files is treating the file like a sitemap and listing every page. The opposite is right: the file's value is curation. Pick the pages you most want an LLM to ground on, leave the rest out.

Context-window size is no longer the binding constraint; focus is. A 50-link curated file does more work than a 5,000-link dump because the LLM that reads the dump has no signal about which pages matter to you.

Rule of thumb for a first pass:

- Documentation-heavy site: 20-40 links across two or three sections. 
- Marketing site with product pages: 8-15 links, all canonical. 
- Pure marketing site with no product depth: skip llms.txt; you do not yet have the surface to make it useful.  
Anthropic's published file is the canonical lean-index example: a short index at platform.claude.com/docs/llms.txt that points to the deeper developer reference. The index does the curation work; the deep file holds the content.

## Best practice 2: lead with the docs you most want quoted

The first section after your H1 should be your canonical pages, in order of importance. The LLM reading the file gets the strongest signal from what appears first.

Verified patterns:

- Stripe (stripe.com/llms.txt): leads with the financial-infrastructure overview, then organizes by product surface (payments, billing, financial connections). 
- Cal.com (cal.com/llms.txt): leads with the docs index, then AI-agents documentation as the first deep link.  
The pattern: put the page you would point a new engineer at first into position one. Everything else follows.

## Best practice 3: one-sentence answer-shaped descriptions

Each link in your llms.txt should have a one-sentence description that tells the LLM what question this page answers. Vague titles do not give the model anything to retrieve against.

Concrete contrast:

- Weak: [Auth guide](/auth): authentication 
- Strong: [OAuth 2.0 setup](/auth/oauth): step-by-step OAuth 2.0 authorization-code flow with refresh-token handling  
If your pages already have decent meta descriptions, you can often reuse them as llms.txt summaries with minor edits. If your meta descriptions are vague or marketing-puffy, fix them on the source page first, then port the cleaned version.

## Best practice 4: prefer markdown destinations

When possible, link to .md variants of your pages rather than the HTML versions. Many modern docs platforms (GitBook, Mintlify, Docusaurus, Mintlify-style stacks) publish a /page.md companion at the same path as the HTML page. LLMs parse markdown more cleanly than HTML and spend fewer tokens on the parse.

If your stack does not publish markdown companions, this practice is optional rather than required; link to whichever surface gives the cleanest extraction.

## Best practice 5: handle versioning explicitly

If you publish multiple versions of your documentation (API v1, v2, v3; product Classic vs Cloud), make the current one unmistakable in the llms.txt and either omit or section-off the legacy versions.

The trap: an llms.txt that lists v1, v2, and v3 of an API without flagging which is current gives the LLM three different answers to the same question. The model will pick one, sometimes the wrong one, and quote outdated parameters in answers to your users.

Stripe's published file surfaces current API products and keeps deprecated ones out of the main index. That pattern transfers to almost any versioned product.

## Best practice 6: review on every docs reorg

Stale is the enemy. Set a trigger rule for when llms.txt gets reviewed:

- Every information-architecture change. 
- Every product launch or major feature addition. 
- Every quarterly content audit, minimum.  
If your team cannot commit to this cadence, do not publish llms.txt at all. A file pointing to moved or deleted pages will train any LLM that consumes it on a broken map of your site. The same trap exists with sitemap.xml, but llms.txt rot is more visible because the file is curated and small.

## Best practice 7: ship llms-full.txt as a companion where it fits

The llms-full.txt convention extends llms.txt by inlining the content of each linked page directly into the file. The LLM that fetches the full version can answer questions about your site without making additional HTTP requests.

This pays off when:

- You have rich technical documentation (Cloudflare's published llms.txt file is large; Vercel's AI SDK companion is larger). 
- Your audience is dev-agent tools that may run inside constrained-fetch environments. 
- Your docs are stable enough to commit to keeping the inline content fresh.  
Skip llms-full.txt when:

- Your site is mostly marketing pages (the inlined content adds little). 
- Your docs change weekly and the file would fall out of sync. 
- Your total useful content is small enough that the regular llms.txt already covers it.  
Crawloria's free llms.txt generator produces both files when the input justifies it.

## Best practice 8: match the pattern to your site shape

Three repeated patterns across verified adopters:

- Catalog pattern: wide API or product surface organized by category. Stripe and Cloudflare follow this. Works for any site with many semi-independent product surfaces. 
- Lean index plus full export: small index file, plus a heavy llms-full.txt companion. Anthropic and Vercel AI SDK follow this. Works when your docs are deep but linear, like a single API reference. 
- Workflow or use-case first: organize by what a developer is trying to do, not by product surface. Cal.com's file leads with AI-agents and scheduling workflows. Works when buyers come in via specific use cases.  
The mistake: copying the pattern of a competitor whose site shape is different from yours. A small SaaS with one product does not need Stripe's catalog structure; an enterprise infrastructure provider does not get away with Cal.com's workflow-first format.

## Common mistakes (what makes an llms.txt useless or harmful)

The failure modes recur. Avoid these:

- Stale file pointing at moved or deleted pages. Trains any consuming LLM on a broken map of your site. 
- Marketing puffery in summaries. "The world's leading X" tells the model nothing. Replace with a one-sentence answer. 
- No curation: every page included. Defeats the purpose of llms.txt. If the file is large enough to be a sitemap, it is too large. 
- Inconsistent format. Bullet links with descriptions in some sections, free prose in others, headings without sections. Parsers handle the canonical bullet-list-under-H2 structure best. 
- Self-referencing as an adopter without verification. Several published "real adopter" lists in 2026 name companies whose /llms.txt returns 404 when checked. We verified this directly: at least two well-known docs platforms named in third-party best-practices articles return 404 on their own llms.txt URL. Before citing an adopter list, verify each one. 
- Publishing once, then forgetting. The same rot trap as sitemap.xml or any other machine-readable file. Set a review trigger.  

## What about llms-full.txt specifically?

Brief recap from best practice 7. The full-export companion is a real win for docs-heavy sites that want LLMs to answer detailed questions without additional fetches. It is a real burden if your content changes weekly or your site is mostly marketing. The honest decision is to start with the lean llms.txt, ship that cleanly, and add llms-full.txt only when you can commit to keeping it current. Most published llms-full.txt files in 2026 are running fresh because their owners treat them as part of the docs build pipeline; manual maintenance does not scale.

## FAQ

Does llms.txt help SEO?

There is no confirmed direct ranking benefit from publishing llms.txt. The possible indirect benefits are real but modest: cleaner content architecture, a forced curation pass on your docs, and a small lift in being chosen as a citation source by emerging dev-agent tools that do parse the file. Treat it as low-cost insurance against future tool adoption, not as a search-ranking lever.

Should a marketing site publish llms.txt?

If you have product pages, how-it-works pages, or a documentation section worth citing, yes. If your site is purely brand and campaign content, skip it; you do not yet have the surface to make the file useful. The threshold is roughly: do you have at least 8-15 canonical pages an LLM should ground on when it answers a category question about you?

How often should llms.txt be updated?

Trigger-based, not calendar-based. Every information-architecture change, every product launch, every quarterly content audit at minimum. If you cannot commit to a review trigger, do not publish the file.

Is llms-full.txt required?

No. The lean llms.txt is the file the spec at [llmstxt.org](https://llmstxt.org/) actually defines. The full-export variant is a widely-used convention, not a requirement. Most adopters benefit from publishing only the lean version; the full export adds value when your docs are deep and stable.

## Where to start

Use Crawloria's free llms.txt generator to produce a clean first-pass file in under two minutes. Then iterate using the practices above: curate the list down to the pages you actually want quoted, rewrite descriptions to be answer-shaped, point at .md versions where possible, and set a review trigger you will actually honor. To see these practices applied to complete files, browse our llms.txt examples. If you are evaluating whether to publish at all, the companion guide llms.txt Explained walks through the decision tree first.

For the broader passive-sense optimization work that llms.txt sits inside, see agentic SEO in 2026 and the LLMO framework. llms.txt is one practice inside a larger discipline; getting it right is one piece of being citable to AI assistants in 2026.

