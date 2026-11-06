# What AI agents really think about your pricing

**Authors:** Kyle Poyar (Founder & CEO, Growth Unhinged), Nikolas Laskaris (AI Strategist, Profound)
**Publication:** Profound Blog (cross-post with Growth Unhinged)
**Published:** 2026-09-03
**URL:** https://www.tryprofound.com/blog/what-ai-agents-really-think-about-your-pricing
**Data window:** 2026-07-29 to 2026-08-10

---

## Full text (extracted from HTML via curl, 2026-10-02; nav, duplicated pull-quotes, and footer removed)

More than two-in-three software buyers already do their research on AI engines like ChatGPT.
While this started as a top-of-funnel behavior it’s now across the entire funnel, including for pricing and negotiations. New data shows that the share of ChatGPT queries with commercial intent rose from 13.9% to 19.2% over the past year. AI increasingly shapes what B2B products get bought and how they’re negotiated.
I’ve been wondering: how does AI make sense of pricing and what influences their POV? For help I partnered with Nikolas Laskaris, a researcher at Profound, the AI marketing platform with a dataset built from over 1.5 billion real AI conversations. (Profound is also a Growth Unhinged partner.)
We tested 7,600 AI responses to pricing queries across the Cloud 100, a list of the top private cloud companies including brands like OpenAI, Anthropic, and Stripe. The research tracked differences across six AI engines: ChatGPT, Google AI Mode, Google AI Overviews, Google Gemini, Microsoft Copilot, and Perplexity. AI engines regularly change citation behavior; this data was collected July 29 to August 10, 2026.
Here’s a preview of the most interesting takeaways:
- AI is talking about your pricing (and not always favorably…)
- Company-owned pricing pages are rarely the primary source of AI answers
- The first factor that matters is AI readability, but only 57% have AI-readable pricing pages
- AI readability can be improved with some simple fixes
- Three external websites impact what AI thinks about pricing
- The winning companies build a pricing answer stack rather than a pricing page

### 1. AI is talking about your pricing (and not always favorably…)
Prompts containing cost or pricing-related keywords now represent between 1–2% of all LLMs queries according to Profound data. That might sound small, but 1% of 3 billion daily queries is a lot of buyer demand!
We gave each AI engine a simple prompt: “Evaluate Company X on pricing.”
The responses were sometimes factual and to the point, plus provided a direct link to the company-owned pricing page. This is the happy path.
“Checkr offers transparent, pay-per-report pricing – starting at $29.99 for basic tiers up to $89.99 for comprehensive domestic packages. It requires no monthly subscription fees for standard screening, but real-world costs often run 40% to 70% higher due to external court and state fees. Review full details on the [Checkr Pricing Page].”
“Calendly uses a tiered, per-seat subscription model ranging from a robust free tier to customized enterprise options. Paid tiers start at $10 per user per month (billed annually) for individuals and small teams, scaling up to $16 per user per month for collaborative routing features. You can view full tier details directly on the [Calendly Pricing Page].”
More often than not, the AI responses read like an indictment and cited dubious sources. This isn’t a one-off finding, either. Profound data shows AI gets pricing and billing information wrong more than any other topic.
For one prominent software company that shall go unnamed, negative pricing language appeared in 72 of 76 AI responses. Google AI Mode described it as “notoriously opaque, premium-priced, and scales aggressively.” This company’s owned pricing page was rarely cited as the primary source for the AI response.
For a vertical AI unicorn, negative pricing language appeared in 67 of 76 AI responses. Since the company doesn’t have a public pricing page, AI responses pulled from third-party sources (often Reddit threads). The AI responses claimed that pricing “ranges from roughly $100 to $2,400 per user per month depending on platform and scenario” – a 24x difference for the same product!
The so-what: inaccurate pricing claims could scare away a prospective buyer or arm them with leverage in a negotiation. Neither is a great position to be in.

### 2. Company-owned pricing pages are rarely the primary source of AI answers
I thought AI would immediately look for pricing on the company’s website. After all, 77% of the Cloud 100 do have a public pricing page. And this is obviously the most official and up-to-date source for pricing.
What the data shows: company-owned pricing pages are usually part of AI citations, but they’re rarely the primary source:
Company-owned pricing pages appeared somewhere in 3,532 of 7,675 responses – 46% of all AI responses.
But company-owned pricing pages only appeared first in 12% of the responses!

No company had its pricing page cited first in a majority of AI runs. That’s still mind blowing to me.
Worth calling out: each LLM has its own quirks. ChatGPT responses tend to default to company-owned pricing pages, citing these first 38% of the time. Google AI Mode, Google AI Overviews, and Gemini usually bury them.

### 3. The first factor that matters is AI readability, but only 57% have AI-readable pricing pages
Interestingly, a pricing page doesn’t need much information in order to be cited.
Personio sits well above the median despite not having transparent pricing on their website. They show plans but no actual price points. The same is true for companies like Pendo, Carta, and Gong. At the same time, having highly transparent pricing isn’t enough to get cited first.
The first factor that matters is AI readability. 57 of the 77 public pricing pages were AI-ready, meaning that they were fully readable to bots. The remainder need attention.
10 pricing pages hid at least 40% of body content from bots, meaning that AI engines couldn’t actually read much of what was on the website. Usually, this is caused by one of four things:
- Client-side rendering: pricing tables that only populate after JavaScript executes. Most AI crawlers execute limited or no JavaScript, so they see an empty shell.
- Interactive elements: tabs, accordions, 'calculate your price' sliders. If content only exists in the DOM after a click, it doesn't exist for a crawler.
- Robots.txt and other blocks: sometimes intentional, sometimes inherited and never cleaned up in production. Either way, the crawlers can’t access pricing.
- iFrames: pricing widgets are pulled from a separate domain that isn't itself crawlable.
A quick check: test your pricing page like a bot. Curl the page or disable JavaScript, then see what’s actually served.

### 4. AI readability can be improved with some simple fixes
When Profound was building a tool to see whether AI could effectively crawl different website pages, they first tested it on themselves. I think you can guess what they found…
While the pricing page appeared normal to human visitors, it was partially hidden to bots. Key self-service pricing and product content couldn’t be crawled. An external post about Profound that was published around the same time independently surfaced the same problem, confirming that AI couldn’t see Profound’s self-service pricing.
Profound updated the marketing site’s rendering logic to make the missing content accessible to AI bots. The fix was deployed on June 25th.
The AEO impact was almost immediate. The pricing page is now Profound’s second most-cited page across the entire website. Citation bot traffic rose by 13% week-over-over after the deployment and has continued to increase since then.

Here’s the fix: Profound’s marketing site’s pricing was rendered client-side in JavaScript, so AI crawlers fetching the raw HTML never saw the prices. The fix moved pricing to server-side rendering. Now prices appear in the initial HTML response and are ingestible by bots.

### 5. Three external websites impact what AI thinks about pricing
Looking across the entire dataset of 7,600 responses, three external domains appeared again and again.
- The most-cited was Vendr (18.7% of runs), a pricing data and negotiation provider.
- Very close behind was Reddit, cited in 18.6% of runs.
- G2 came in third, appearing in 15.9% of responses. (This should come as a relief since pricing information on G2 can be easily influenced, unlike Reddit threads.)

The implication: Even if you try to hide your pricing, it’s being talked about elsewhere.

### 6. The winning companies build a pricing answer stack rather than a pricing page
The best performers were Plaid (its pricing page was cited first 42% of the time) followed by Fireworks AI, Fal AI, and ElevenLabs. (The lowest performers were enterprise-focused companies with hidden pricing and limited documentation.)
These companies are winning because they’ve built their own pricing answer stack rather than simply one-off pricing pages. The pricing answer stack gives AI engines everything they need to know to assess pricing, all of which is mutually reinforced with first-party sources.
The answer stacks include five components:
- One clear pricing page with plan and pricing information
- FAQs and FAQ pages matching natural language pricing questions
- Supporting content explaining product value, operational implications, and edge cases
- Technical billing documentation
- AI-readable infrastructure for all of the above

#### Plaid
Looking at Plaid, for example, AI answers cited multiple Plaid-owned content sources including its billing docs (cited in 70% of answers), pricing page (cited in 64% of answers), and FAQs (cited in 50% of answers). The page counts overlap because AI cites several Plaid-owned pages in one response.
The documentation is Plaid’s most important pricing page for AI, not the pricing page itself. Docs are frankly way more information-dense, and AI agents crave details over simplification. In Plaid’s case the docs define one-time, subscription, per-request, flexible, and other billing models at the product and endpoint level. They cover costly edge cases. And everything is cleanly segmented out by plan type.
Another win: Plaid’s docs acknowledge which information is unavailable. This gives AI an authoritative explanation for the lack of public dollar amounts.

#### Fireworks AI
Fireworks AI follows similar patterns to Plaid, although they’re even more transparent about actual numbers.
What we liked: Fireworks keeps pricing visibility current with pricing pages that show currently scheduling pricing changes (separating “up to Aug 31” and “from Sep 1”). This shows a strong freshness signal.
Fireworks’ documentation exposes an llms.txt documentation index prominently on its pages and offers “Copy page” functionality. Why this works: Fireworks gives AI dense, tabular, normalized facts with explicit units. Very little interpretation is required before those facts can be quoted, compared, or cited.

### Playbook: How to audit whether your pricing is AI-ready
Pricing needs a makeover for AI agents. We’ve turned the highest-impact practices into a Claude skill you can run on your own pricing.
📄 Download the skill: AI pricing visibility audit
Here’s a simplified checklist to share with your team:
How to audit whether your pricing is AI-ready
1. Establish your pricing baseline. Run the following prompt through ChatGPT, Claude, and Gemini once per day for a week: Evaluate [Company Name] on pricing. Then categorize the citations in the AI answers along with the general sentiment (positive, neutral, negative).
2. Build three sources of truth for pricing. This should include a pricing page (/pricing), billing docs, and FAQs. If exact pricing isn’t available externally, just reference that. Make sure these pages link to one another.
3. Check whether bots can crawl your pricing content. This is the lowest-hanging fruit for companies that already have a pricing page.
4. Give at least one concrete entry point. This could be a free trial, free plan, or lower-cost “starting at” package.
5. Specify the billing mechanics rather than just plans and pricing. Billable events, minimums, commitments, overages, cancellation behavior, regional premiums, and hidden costs are especially citation-worthy.
6. Ensure that content is extractable. AI engines prefer descriptive headings, short definitions, comparison tables, bullets, and self-contained paragraphs.
7. Provide evaluation-oriented language. Phrases like “best for” or “predictable costs” help AI engines evaluate pricing rather than merely describe it.
8. Develop pricing consensus off-site. Some of this content you control and edit yourself (G2, Capterra, YouTube). For other sources (Vendr, Reddit) you’ll likely need to do outreach to correct inaccuracies.
9. Maintain freshness signals. Current plan definitions, dated announcements, visible update dates, and scheduled price changes make owned sources safer to cite.
10. Expose AI-readable versions of your pricing. llms.txt, Markdown pages, documentation indexes, and copy-for-LLM controls probably improve retrieval and parsing (although we can’t prove causal impact).
Customers increasingly trust AI in the buying process because it’s useful, and many customers don’t want to talk to a sales rep if they can avoid it. This trend is likely to continue, and now is the time to prepare. This doesn’t need to become a science project: AI readability can be improved even with a few simple fixes.
You designed your pricing for humans. Is it ready for AI?

