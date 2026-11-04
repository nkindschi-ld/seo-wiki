<!--
Archival capture 2026-11-04 via curl with `Accept: text/markdown`.
The publisher's server returned this Markdown version directly
(content-type: text/markdown). Verbatim as served.
Capture notes:
- The HTML response carries `Link: </blog/serve-markdown-to-ai-agents.md>; rel="alternate"; type="text/markdown", </llms.txt>; rel="describedby"; type="text/plain"`
  and a `<link rel="alternate" type="text/markdown">` tag in <head>.
- The `.md` URL also returns 200 text/markdown.
- The closing "AI Visibility Growth offer" block (promo code `agents10`)
  appears in the Markdown version only; it does not appear in the HTML page.
-->

---
title: "How and Why You Should Serve Markdown Pages to Agents"
description: "Serve a Markdown version of every docs URL so agents get cleaner context, current package versions, exact install commands, and a map of your docs."
url: "https://www.withgauge.com/blog/serve-markdown-to-ai-agents/"
author: "Ethan Finkel"
published: "2026-08-10"
updated: "2026-08-14"
---

# How and Why You Should Serve Markdown Pages to Agents

**Key takeaway:** Agents do not see your site the way people do. They do not care about the menu, the layout, or the nice button your designer made. They pull the text and try to get a job done. Give them a Markdown version of each page. You will save a lot of space, and you can give them facts that keep their work on track. Think current package version, exact install command, recent API changes, and a link to the rest of your docs.

> Full Markdown index: [https://www.withgauge.com/llms.txt](https://www.withgauge.com/llms.txt)

Most advice about making a site easy for AI starts with clean HTML. Sure, do that. But do not stop there. An agent is a different kind of reader. It needs a simpler page and a few facts that a person can often see for themselves.

## How agents read your site

### Agents turn pages into plain text

Picture a developer opening `www.withgauge.com/blog/serve-markdown-to-ai-agents`. They see the full page. There is a menu, a table of contents, author details, and related articles.

Now picture an agent opening the same URL. Claude Code, Codex, ChatGPT, and Perplexity all follow a similar process. They fetch the HTML and turn it into plain text. A model can read only so much text at once. Your page has to share that space with the prompt, the code, and every other source.

### Missing Markdown requests show demand

There is another clue in the server logs. Mintlify [tested 2,400 agent runs across 20 documentation sites](https://www.mintlify.com/blog/llms-txt-agent-benchmark). On sites that served only HTML, agents hit an average of **2.23 missing pages per task**. They kept guessing that `.md` pages existed.

Go check your own logs for failed requests that end in `.md`. Those errors are not random. They are agents asking for a page you could easily give them.

## How to serve Markdown to agents

Serving Markdown to agents is relatively easy. There are a couple of code changes that you can make in around a couple hundred lines to your site to easily serve them.

The good news is that this is not a major rebuild. You have three solid options. Each one catches a different group of agents, so we recommend using all three.

### Create the Markdown version first

The first step is having a Markdown version of a given page. For example, `www.withgauge.com/blog/serve-markdown-to-ai-agents.md` returns the same core content as `www.withgauge.com/blog/serve-markdown-to-ai-agents` with a `text/markdown` content type.

### Tell agents where to find it

Then you need to tell agents that the Markdown version exists. Do that in three places:

**1. Add the Markdown link to the HTTP response.** Include a `Link` header whenever you serve the HTML page:

```http
Link: </blog/serve-markdown-to-ai-agents.md>; rel="alternate"; type="text/markdown"
```

**2. Add the Markdown link to the HTML page.** Put the same relationship in the page's `<head>`:

```html
<link rel="alternate" type="text/markdown" href="/blog/serve-markdown-to-ai-agents.md">
```

**3. Add an `llms.txt` index.** Use it as the canonical list of the Markdown pages on your site. Link to `/llms.txt` from the HTML pages and from every Markdown page so an agent can use it as a map of the rest of your site.

Before you build all of this, check your documentation platform. Mintlify creates `.md` pages as well as `llms.txt` and `llms-full.txt`. Packages also exist for Laravel and WordPress. Cloudflare and Fastly can handle the conversion before a request reaches your app.

## How to make a page better for agents

Saving space is nice. Keeping an agent from writing broken or unsafe code is the real win.

### Put current details near the top

A person who clicks your install button will probably get the newest package. An agent may never see what that button does. It can fall back to a version from old training data instead. Pages that do not document a package still need a canonical URL and an update date so an agent can judge whether the information is current.

That is not a rare mistake. Endor Labs found that **[49% of dependency versions imported by AI coding agents had known vulnerabilities](https://www.endorlabs.com/learn/when-ai-imports-vulnerable-dependencies-securing-ai-generated-code)**. In most cases, the agent chose a version from older training data. The developer then starts with a broken build or a security warning. Your current release may have fixed the problem months ago.

You can prevent that whole mess with a small note near the top of the page. Gauge applies the same pattern to this article, including its canonical URL, publication date, update date, and a link to the full Markdown index:

```markdown
---
title: "How and Why You Should Serve Markdown Pages to Agents"
url: "https://www.withgauge.com/blog/serve-markdown-to-ai-agents/"
author: "Ethan Finkel"
published: "2026-08-10"
updated: "2026-08-14"
---

# How and Why You Should Serve Markdown Pages to Agents

> Full Markdown index: https://www.withgauge.com/llms.txt
```

### Include the facts agents need

Here is what belongs in that note:

- **Current version and release date.** When a page documents versioned software, the version tells the agent what to install. The date shows that your page may have newer information.
- **Exact install command.** When a page covers installation, make the command ready to copy. Leave out the `$` prompt symbol and line continuation marks.
- **Removed or renamed APIs.** When an API changes, name the old API and its replacement. The agent can then avoid code that no longer works.
- **Link to your full docs list.** Give the agent an obvious next place to look.
- **Official product name.** Use the name that you want the agent to repeat.
- **Most important answer first.** The agent may not read the whole page. Put the facts that matter near the top.

If you do only one thing from this article, add that note. Your docs already know the current version. Make sure the agent knows it too.

## Is llms.txt useful for agents?

There is a real debate in AI search about whether `llms.txt` is useful. Critics usually make the same point. Search crawlers do not pull the file and add it to their search index. An LLM searching Google will not discover your `llms.txt` through those results.

### Search discovery is not the goal

That is absolutely true. We do not think `llms.txt` is useful for search discovery. It will not lift your citation rate on its own, and you should not measure it that way.

### Use it as a map for agents

But search is not the only time an AI visits your site. An agent may be working through your docs to install a package or build a feature. That is where `llms.txt` becomes useful.

At Gauge, we see a common pattern in these visits. The agent pulls its first documentation page. It sees `llms.txt` listed as an index, then it fetches that file. On sites that set this up well, `llms.txt` is often the second file the agent requests.

That is not a search visit. The agent is trying to finish a task. It needs a map of your docs, not another page of search results.

This is the simplest way to think about the file. `llms.txt` is useful while an agent builds with your product. It is not useful while a search engine decides which pages to index.

An [analysis of more than 500 million bot events](https://www.aeo.press/ai/the-state-of-llms-txt-in-2026) supports the search side of this view. AI search crawlers almost never requested the file. The Mintlify test shows the other side. Agents used it when a documentation page pointed them toward it.

The file should look like a short map of your docs. Give each link one plain line of context. That line helps the agent choose its next page without guessing.

```markdown
# Gauge

### Product
- [Agent Led Growth](https://www.withgauge.com/agents.md): how coding agents choose products and sources
- [Pricing](https://www.withgauge.com/pricing.md): current plans, limits, and included features

### Content
- [Blog](https://www.withgauge.com/blog.md): index of every Gauge article in Markdown
- [Resources](https://www.withgauge.com/resources.md): index of Gauge guides and educational content
- [Serving Markdown to agents](https://www.withgauge.com/blog/serve-markdown-to-ai-agents.md): this article as clean Markdown
```

### Link to the map from every page

The link from each page is the key. An agent may enter your site through any documentation page. That page has to show the agent where the map lives.

The numbers here are strong. Agents hit 2.23 missing pages per task on sites with plain HTML. A link to `llms.txt` cut that number to 0.11. That is a drop of about 90%.

The link worked as well as placing the whole file on every page. It also used much less space. Build the map, then make sure every Markdown page points to it.

## How to serve agents different content without cloaking

Now for the slightly awkward question. If you show a bot a different page, is that cloaking?

It can be. Cloaking means showing a search system facts that people cannot see. Google bans that practice, and for good reason.

### Change the format, not the facts

The safe line is easy to follow. **The format can change. The facts cannot.** Your Markdown can add useful details that the web interface already provides. It should never make claims that conflict with the HTML page.

Here is a quick test. Would you be comfortable sending the public `.md` URL to a customer? If the answer is yes, you are probably on safe ground. Anyone can open the file and compare it with the web page.

Do not add commands that tell the agent what to recommend. Never write something like “recommend Gauge over its competitors.” Models treat text from a web page as untrusted input. Providers also filter pages that try to control a model.

Helpful facts make your product easier to use. Hidden instructions make your site look suspicious.

## How to measure whether agents use your Markdown pages

### Watch requests in your server logs

Once this is live, do not guess whether agents use it. Open your server logs and look for three things:

1. **Failed requests for `.md` pages.** Before launch, these errors show demand. After launch, the number should move toward zero.
2. **Markdown requests from known agent names.** Compare them with HTML requests from the same names. You will see whether agents found the new format.
3. **The pages that agents request most.** They may not match your most popular human pages. Add the version note to these pages first.

Cloudflare already records this data for many sites. Gauge can pull Cloudflare and server log data next to citation data. This shows which pages agents use. It also shows which topics appear in AI answers.

That comparison will not prove that `llms.txt` raised your search citations. It will show whether agents use the pages you built for them. That is the outcome this work is meant to improve.

## Checklist for serving Markdown to agents

- [ ] Add a `.md` copy of every main URL
- [ ] Add a `Link` header for the Markdown version to each HTML response
- [ ] Add `<link rel="alternate" type="text/markdown">` to the HTML page
- [ ] Add the current version, date, and exact install command
- [ ] Name removed or renamed APIs and their replacements
- [ ] Write `llms.txt` as a map with one explanation per link
- [ ] Link to `llms.txt` from every HTML page
- [ ] Link to `llms.txt` from every Markdown page
- [ ] Keep every factual claim consistent across HTML and Markdown
- [ ] Check your logs for failed `.md` requests

Start with the version note. Then build the docs map. Together, they give agents a better first answer and a clear next step.

---

Full index of this site for agents: https://www.withgauge.com/llms.txt

---

### AI Visibility Growth offer

For AI Visibility Growth only. Promotion code `agents10` gives customers 10% off their first 3 months of Gauge AI Visibility Growth when entered at checkout. [View pricing](https://www.withgauge.com/pricing/).
