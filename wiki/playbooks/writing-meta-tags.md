---
type: playbook
tags: [seo, aeo]
updated: 2026-08-06
---


# Writing Meta Tags (Page Titles & Meta Descriptions)

**Why/when to use this:** A plain-language guide for a non-SEO audience
(writers, PMs, engineers) who need to write or fix a page's title tag and
meta description. Illustrative, not exhaustive — for the strict
LaunchDarkly formatting spec (Title Case, `| LaunchDarkly` suffix,
65/155-char limits, CTA rules) use the `seo-meta-tags` skill. See
[[traditional-seo-ranking-factors]] and [[aio-ctr-impact]] for the
underlying ranking/CTR evidence. For the deprecated
`<meta name="keywords">` tag (skip it), see [[meta-keywords-tag]].

## What they are

Two snippets of HTML text that don't appear on the page itself:

- **Title tag** — the clickable headline in search results and the browser tab.
- **Meta description** — the gray summary line underneath that headline.

```html
<title>Runtime Control Plane for Features & AI | LaunchDarkly</title>
<meta name="description" content="Control what users experience in production without redeploying. Release safely, observe impact in real time, and iterate at AI speed.">
```

## Why they matter

- They're your **ad copy in search results** — often the only thing a person reads before clicking.
- Title tags are a **direct Google ranking factor**. Descriptions are not, but they heavily influence **click-through rate**, which indirectly helps.
- AI answer engines (Google AI Overviews, ChatGPT, Perplexity) read them to decide **what a page is about and whether to cite it**.
- Get them wrong and Google **rewrites them for you** — usually worse than what you'd write.

## The rules

| | Title tag | Meta description |
|---|---|---|
| Length | ~50–60 chars (max ~65) | ~150–155 chars |
| Goal | Match the search, front-load keyword | Sell the click, add detail |
| Keyword | Once, near the front | Once, naturally |
| Uniqueness | Every page unique | Every page unique |

## Good vs. bad

**Title tags**

| ❌ Bad | Why | ✅ Good |
|---|---|---|
| `Home` | Says nothing | `Runtime Control Plane for Features & AI \| LaunchDarkly` |
| `LaunchDarkly \| Release, Observe, Iterate, AI, Flags...` | Brand first, keyword buried, truncated | `Feature Flag Platform & Progressive Delivery \| LaunchDarkly` |
| `Best Feature Flag Tool Buy Now Cheap Flags Flags` | Keyword stuffing | `What Is Progressive Delivery? A Beginner's Guide` |
| `Untitled Page 4` | CMS default | `Guarded Releases: Automated Rollback & Kill Switches` |

**Meta descriptions**

| ❌ Bad | Why | ✅ Good |
|---|---|---|
| `Welcome to our website. We are a company that does many things.` | Generic, no value | `Control what users experience in production without redeploying. Release safely, observe impact in real time, and iterate at AI speed.` |
| *(blank — Google grabs random page text)* | No control | `Compare guarded releases vs. manual monitoring: detection speed, rollback effort, and when each fits. Real examples included.` |
| `flags, ai, runtime, release, observe, deploy` | Keyword list, not a sentence | `Configure, release, and observe AI agents at runtime. Add guardrails and kill switches so you can scale AI without losing control.` |

## By content type

**Informational — "What is X"**
Match the question literally. Lead with the answer, promise clarity.
- Title: `What Is a Runtime Control Plane? Definition & Examples`
- Desc: `A runtime control plane lets teams change what users experience in production without redeploying. Here's how it works, with examples.`

**Product pages**
Name the product + category. Description = value prop + differentiator.
- Title: `Runtime Control Plane for Features & AI | LaunchDarkly`
- Desc: `Release, observe, and iterate on every change at runtime — no redeploys. Trusted by 5,500+ teams to ship with 43% fewer incidents. Start free.`

**Solution pages** (problem/use-case/audience)
Lead with the outcome or the audience's problem, not the product name.
- Title: `Ship AI Agents Safely in Production`
- Desc: `Benchmark prompts and models, watch them at the change level, and roll back in milliseconds. Move at AI speed and stay in control.`

**Thought leadership** (blog, opinion)
Make it a compelling headline. Curiosity + specificity beat keywords here.
- Title: `The Problem Isn't Shipping. It's What Happens After.`
- Desc: `Building and deploying is easy — controlling what happens in production is not. Why release control has to move to runtime in the AI era.`

## Quick checklist

- [ ] Every page has a unique title + description
- [ ] Title front-loads the main keyword, under ~60 chars
- [ ] Description reads like a sentence, under ~155 chars, with a reason to click
- [ ] No stuffing, no defaults, no blanks
- [ ] Title matches the search intent the page targets

## Notes on the examples

Examples use LaunchDarkly's current positioning from the March 2026
Platform Messaging Framework: category **"runtime control plane for
features and agents,"** tagline **"Move at AI speed. Stay in control,"**
and the **Release / Observe / Iterate** pillars. Proof stats (43% fewer
incidents, 5,500+ teams, 99.99% uptime, sub-200ms propagation) are
CTA fuel drawn from that doc. The `CodeControl` / `AgentControl`
two-product naming was intentionally left out — it appears only once in
the framework and isn't yet built out, so leading with it risks
inconsistency.
