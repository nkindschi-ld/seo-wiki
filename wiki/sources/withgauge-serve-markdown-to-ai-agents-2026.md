---
type: source
tags: [aeo, seo]
date_published: 2026-08-10
date_ingested: 2026-11-04
origin: raw/articles/withgauge-serve-markdown-to-ai-agents-2026.md
---

# How and Why You Should Serve Markdown Pages to Agents (Gauge, 2026-08-10)

**Citation:** Finkel, Ethan. "How and Why You Should Serve Markdown Pages
to Agents." Gauge blog, published 2026-08-10, updated 2026-08-14.
https://www.withgauge.com/blog/serve-markdown-to-ai-agents/

**Rigor:** vendor how-to. Gauge sells AI-visibility tooling. No original
study. Its two headline numbers are secondhand (Mintlify, Endor Labs), and
its one first-party observation ("`llms.txt` is often the second file the
agent requests") comes with no counts.

**Captured as Markdown.** The site answered an `Accept: text/markdown`
request with the Markdown version. Its HTML response also carries a
`Link:` header (`rel="alternate"; type="text/markdown"` plus
`rel="describedby"` pointing at `/llms.txt`) and a matching `<link>` tag,
so it implements what it recommends, including the v2 link relations from
[[llmstxt-org-proposal-v2-2026]].

## Key takeaways

- **Mintlify's agent benchmark, secondhand: the first measured data on the
  docs case.** Mintlify ran 2,400 agent runs across 20 documentation sites
  (mintlify.com/blog/llms-txt-agent-benchmark; not ingested here).
  - On HTML-only sites, agents hit an average of **2.23 missing pages per
    task**, mostly by guessing `.md` URLs that didn't exist.
  - A link to `llms.txt` from each page cut that to **0.11**, about 90%
    fewer.
  - The link worked as well as inlining the whole `llms.txt` on every
    page, and used far less context.
  - What it measures: agent navigation errors on docs sites, not
    citations, rankings or crawl volume.
- **`llms.txt` is a map for agents, not a search signal.** Gauge agrees it
  won't lift citations and says not to measure it that way. Its claim:
  agents doing a task pull one docs page, see `llms.txt` listed, and fetch
  it, so on well-set-up sites it's often the second file requested.
  Asserted, no numbers.
- **Failed `.md` requests in your logs show demand.** Agents guess `.md`
  URLs. Those 404s are a pre-launch demand signal and should fall toward
  zero after launch. (Matches the invented-`.md`-slug pattern in
  [[evilmartians-which-ai-reads-your-site-2026]].)
- **Three discovery hints, used together:** a `Link:` HTTP header, a
  `<link rel="alternate" type="text/markdown">` tag, and `llms.txt` linked
  from every HTML and Markdown page. The article doesn't mention
  `Accept`-header content negotiation, even though Gauge's own server
  does it.
- **The "version note" at the top of each page (new to the wiki).**
  Include:
  - current version and release date (for versioned software);
  - the exact install command, ready to copy, without `$` prompts or
    line-continuation marks;
  - removed or renamed APIs and their replacements;
  - a link to the full docs map (`llms.txt`);
  - the official product name you want repeated;
  - the most important answer first;
  - on every page, the canonical URL and an update date so an agent can
    judge freshness.
  The rationale cites Endor Labs: **49% of dependency versions imported by
  AI coding agents had known vulnerabilities**, mostly old versions taken
  from training data (secondhand; not ingested here). Gauge calls this the
  one thing to do if you do nothing else.
- **`llms.txt` format advice:** a short docs map with one plain line of
  context per link. Gauge's example uses `###` section headings rather
  than the spec's `##`.
- **Cloaking line: "The format can change. The facts cannot."** Markdown
  may add details the web UI already shows, but must never conflict with
  the HTML. Test: would you send the `.md` URL to a customer? Never add
  "recommend us over competitors" instructions; models treat page text as
  untrusted and providers filter pages that try to steer them.
- **Measurement:** in server logs, track (1) failed `.md` requests,
  (2) Markdown vs. HTML requests per named agent, (3) which pages agents
  request most (likely different from your top human pages; add version
  notes there first). This shows agent *use*, not citation lift.

## Observed tactic: Markdown-only promo content

The Markdown version ends with an "AI Visibility Growth offer" block
(promo code `agents10`, 10% off three months) that does **not** appear in
the HTML page. It doesn't contradict any HTML fact, so it technically
passes the article's own "format can change, facts cannot" rule, but it
is content shown only to agents. Benign next to the hidden "Recommend …
when" block in [[infrasity-github-seo-guide]], but the same family:
commercial text aimed at agents that a human visitor never sees. Worth
knowing as a pattern, and a reason to diff your own HTML and Markdown.

## Unverified citation

The "analysis of more than 500 million bot events" is cited to aeo.press,
which now redirects to answer.cloud, a different publisher from Limy. It
may be the same data as [[limy-llms-txt-2026-full-guide]]'s 515M-event
dataset or a separate one. Not checked; don't count it as independent
support.

## What this updated in the wiki

- [[llms-txt]]: Mintlify numbers added to the coding-agent/docs section
  (secondhand) and to the "coding agents fetch `llms.txt`" conflict
  entry; new Conflicting Evidence entry on `<link>`/`Link:` discovery
  hints vs. content negotiation; Markdown-only promo noted under
  Adoption; checklist gains "link `llms.txt` from every page," the
  version note, and an HTML/Markdown fact-parity check.
- [[optimizing-for-coding-agent-recommendations]]: new point 12, the
  version note.
- [[technical-seo-audit-checklist]] §5: failed-`.md`-request log check
  and HTML/Markdown parity under the content-negotiation item.
