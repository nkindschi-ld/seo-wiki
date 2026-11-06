---
type: playbook
tags: [aeo, seo]
updated: 2026-11-06
---

# AI Pricing Visibility Audit

**Why / when to use this:** use this when AI engines describe your
pricing badly: negative, wrong, out of date, or sourced from Reddit and
Vendr instead of you. Also use it before a pricing change, or whenever
you need to know what a buyer hears when they ask ChatGPT "how much
does X cost?" Pricing is where wrong AI answers cost the most. They can
scare off a buyer or give them leverage in a negotiation. The main
source is [[tryprofound-ai-pricing-visibility-2026]] (Profound /
Growth Unhinged, ~7,600 responses across 6 engines, Cloud 100 companies,
July–Aug 2026). It sits under [[ai-shortlist-effect]], where accurate,
current pricing is one of the four framing levers that decide
selection, and [[ai-citation-landscape]], which covers where pricing
answers come from.

## The baseline problem (why this needs its own audit)

- **Pricing is the topic AI gets wrong most often.** Per
  [[tryprofound-where-inaccurate-ai-claims-come-from]] (Profound
  FactCheck, 158K+ claims, Apr–Aug 2026), pricing and billing is 12% of
  evaluated claims but 24% of inaccurate ones. For 66% of brands with
  enough pricing claims to judge, it's their worst topic. On pricing,
  claims citing earned media are wrong about 12% of the time, and even
  the brand's own site about 5%.

- **Your pricing page is usually cited, but rarely first.** It appears
  in 46% of AI pricing answers but is the *first* citation in only
  12%. No Cloud 100 company was cited first in a majority of runs.
- **Engines differ.** ChatGPT cites the owned page first 38% of the
  time. This fits [[lilyray-chatgpt-fanout-queries-2026]]'s finding
  that ChatGPT fan-outs `site:`-target brand domains for pricing
  queries. Google AI Mode, AI Overviews and Gemini usually bury it.
  Audit each engine separately, not as one "AI".
- **Outside domains fill the gap:** Vendr (18.7% of runs), Reddit
  (18.6%) and G2 (15.9%). Hiding pricing doesn't stop AI discussing
  it. It just hands the answer to these sites.
- **Pricing pages are a weak page type for citations in general**
  (Otterly: −21% vs. baseline, per [[ai-citation-landscape]]). So the
  goal isn't only a better pricing page. It's a set of pages, which
  the source calls the answer stack.

## The pricing answer stack (target state)

The best performers (Plaid, Fireworks AI, Fal AI, ElevenLabs) give AI
engines a set of first-party sources that link to and agree with each
other, not one page:

1. **One clear pricing page** with plan and price information.
2. **FAQs written as natural-language pricing questions** ("Is there a
   free plan?", "What counts as a billable seat?").
3. **Supporting content** on product value, operational implications
   and edge cases.
4. **Technical billing documentation.** This is often the most-cited
   piece. Plaid's billing docs were cited in 70% of answers vs. 64% for
   its pricing page, because docs are denser. They define the billing
   model per product or endpoint, cover costly edge cases, and say
   outright which numbers aren't public. That gives AI an authoritative
   reason for a missing dollar figure, instead of leaving it to
   speculate.
5. **AI-readable infrastructure for all of the above** (see step 3).

## The audit: 10 steps

1. **Establish a baseline.** Run `Evaluate [Company Name] on pricing`
   in ChatGPT, Claude and Gemini once a day for a week (add Google AI
   Mode, Copilot and Perplexity if they matter to your buyers). For each
   answer, record:
   - every citation, and whether your own page was **first**, present,
     or absent
   - sentiment (positive / neutral / negative)
   - any wrong numbers

   Running it daily for a week smooths out run-to-run variation (see
   [[ai-answer-volatility]] for how large it is, and
   [[ai-visibility-measurement-methodology]]).
2. **Build three sources of truth:** `/pricing`, billing docs and
   FAQs, all linking to each other. If exact pricing isn't public, say
   so explicitly on those pages rather than leaving a gap.
3. **Check that bots can actually read the pricing content.** This is
   the cheapest fix for anyone who already has a pricing page. 20 of
   77 Cloud 100 pricing pages weren't fully readable, and 10 hid 40% or
   more of their content. Test it the way a bot sees it:

   ```bash
   curl -sL -A "Mozilla/5.0 (compatible; GPTBot/1.0)" https://example.com/pricing | grep -i '\$[0-9]'
   ```

   Or disable JavaScript and reload. Look for the four failure modes:
   - **Client-side rendering:** price tables filled in by JavaScript.
     Most AI crawlers don't execute JS (two-source-confirmed in
     [[technical-seo-audit-checklist]]). Fix it with SSR, SSG or ISR.
   - **Interactive elements:** tabs, accordions, "calculate your price"
     sliders. If content only reaches the page after a click, a crawler
     never sees it. Put the default and all-plans view in the initial
     HTML.
   - **robots.txt and other blocks**, often inherited and never cleaned
     up. Check with [[robots-txt-audit-checklist]].
   - **iFrames:** pricing widgets loaded from a separate, uncrawlable
     domain.

   Reference case: Profound found its own self-serve prices were
   invisible to bots and moved them to server-side rendering. Citation
   bot traffic rose 13% week over week, and the pricing page became
   its #2 most-cited page. That's one vendor reporting on itself, but
   the direction matches every JS-rendering source in the wiki.
4. **Give at least one concrete entry point:** a free trial, a free
   plan, or a "starting at" price. Pages with plans but no prices can
   still be cited (Personio, Pendo, Carta, Gong). But a company with no
   public pricing at all got a 24x price range invented from Reddit
   threads.
5. **Spell out billing mechanics, not just plans:** billable events,
   minimums, commitments, overages, cancellation behavior, regional
   premiums, hidden or pass-through costs. These are the details AI
   engines most want to cite, and the ones they invent when you don't
   provide them.
6. **Make content extractable:** descriptive headings, short
   definitions, comparison tables, bullets, self-contained paragraphs.
   Use normalized facts with explicit units (Fireworks AI's tables need
   "very little interpretation" before they can be quoted). See
   [[geo-content-optimization-tactics]] and [[explainable-to-ai-4cs]].
7. **Use evaluation-oriented language.** Phrases like "best for X" and
   "predictable costs" let the engine *evaluate* your pricing, not just
   describe it. This matches the "best for X" label lever in
   [[ai-shortlist-effect]].
8. **Build pricing consensus off-site.** Some sources you control
   directly: G2, Capterra, YouTube. Others need outreach to correct
   errors: Vendr, Reddit. Keep numbers consistent everywhere a model
   might look. Contradictory descriptions across sources are "actively
   harmful," per [[derivatex-4cs-explainable-to-ai-2026]] (see
   [[ai-citation-landscape]]).
   - **Find your own error sources, not a generic list.** Vendr,
     Reddit and G2 dominate pricing *citations*, but the domains behind
     pricing *errors* are scattered: the top 10 account for only 15% of
     pricing inaccuracies. A typical brand's earned-media errors come
     from about 4 sites, often unique to it
     ([[tryprofound-where-inaccurate-ai-claims-come-from]]). Use the
     baseline in step 1 to trace each wrong number to the page it
     cites, then do outreach to those pages. Earned media is the
     highest-leverage outside target: it's the most error-prone source
     on pricing (~12%), and 35% of all earned-media errors are about
     pricing.
   - **Audit your own pages first.** 54% of brands had at least one AI
     error traced to their own site. Stale prices on your site
     reinforce wrong answers everywhere else.
9. **Keep freshness signals visible:** current plan definitions, dated
   announcements, visible "last updated" dates, and scheduled price
   changes. Fireworks AI shows "up to Aug 31" and "from Sep 1" side by
   side. Stale pricing hurt selection in [[ai-shortlist-effect]], so
   this is ongoing upkeep, not a one-time edit.
10. **Offer AI-readable versions** of pricing and billing docs:
    [[llms-txt]], Markdown page versions, documentation indexes,
    "copy for LLM" controls. **Lowest confidence step:** the source
    itself says it "can't prove causal impact." The wiki's evidence
    that llms.txt moves AI-search visibility is null so far (see
    [[llms-txt]]). A randomized test of serving Markdown pages to LLM
    bots found no significant lift in bot visits
    ([[punturo-markdown-llm-bot-traffic-rct-2026]], CI −11% to +47%).
    Markdown delivery by content negotiation has better evidence for
    agent clients (see [[evilmartians-which-ai-reads-your-site-2026]]).
    Do it for docs-heavy pricing and billing pages, but don't expect it
    to fix citation position.
11. **Treat pricing schema as a consistency layer, not a fix.** Mark up
    plans as `Offer`s that mirror the visible prices exactly, generated
    from the same pricing source. Don't expect markup to carry a price
    that isn't visible: in two small layer tests, a price present only
    in JSON-LD was returned by 0 of 5 AI systems and in 0 of 9 runs, and
    when markup and visible text disagreed, answers used the visible
    price ([[coreaex-saas-pricing-schema-2026]]). Type choice and the
    enterprise / no-rating rules are in [[saas-pricing-page-checklist]];
    the evidence is in [[structured-data-and-ai-search]].

**When an answer gets a price wrong, diagnose before you fix.** Don't
start by adding schema. Find the first layer where the current fact
stops being available ([[coreaex-saas-pricing-schema-2026]]):

- absent from the page;
- present but inaccessible (JS, tabs, robots, iframes: step 3);
- contradicted elsewhere on your own site;
- stale in a cache or index;
- ambiguous between plans, currencies or units;
- transformed in the answer itself.

More than one can be true at once.

## Quick-reference checklist

- [ ] Baseline run: 1 prompt × 3+ engines × 7 days, with citations
      (first/present/absent), sentiment and accuracy logged
- [ ] Each wrong pricing claim traced to the page it cites (own site,
      competitor, earned, social)
- [ ] `/pricing`, billing docs and pricing FAQs exist and link to each
      other
- [ ] Pricing content is in the initial HTML (curl / JS-off test passes)
- [ ] No pricing content hidden behind tabs, sliders or iframes in the
      default view
- [ ] robots.txt doesn't block `/pricing` or billing docs (watch
      prefix rules like `Disallow: /p`)
- [ ] At least one concrete price or entry point is public, or the
      absence is explained explicitly
- [ ] Billing mechanics documented (billable events, minimums,
      overages, cancellation, regional pricing)
- [ ] Tables with explicit units; descriptive headings; self-contained
      paragraphs
- [ ] "Best for X" and other evaluation language present
- [ ] G2/Capterra listings current; Vendr/Reddit errors flagged for
      outreach
- [ ] Visible update dates; upcoming price changes shown in advance
- [ ] (Optional, unproven) llms.txt / Markdown versions / copy-for-LLM
      control on pricing and billing docs
- [ ] Pricing schema (if used) mirrors visible prices exactly, from one
      source; no fact lives only in markup; no placeholder 0 on custom
      tiers
- [ ] Each wrong answer diagnosed by layer (absent / inaccessible /
      contradicted / stale / ambiguous / transformed) before fixing

## Limits of the evidence

- Both sources are from one vendor (Profound sells AI-visibility and
  FactCheck tooling).
- The visibility study used one prompt template, a two-week window,
  and large well-known companies only.
- The accuracy data comes from FactCheck customers, and the post
  doesn't say how verdicts are reached.
- The only before/after result is Profound's own site, with no control.
- Re-run the baseline after each fix. Citation behavior changes over
  time, and position-one share is the metric to watch, not just
  presence.

## Related

- [[saas-pricing-page-checklist]] — the on-page half: layout, query
  targeting, unit/overage copy, crawlability and the schema model for
  `/pricing` itself.
- [[structured-data-and-ai-search]] — what schema does and doesn't do
  for AI answers.
- [[ai-shortlist-effect]] — why pricing accuracy changes purchase
  decisions, not just visibility.
- [[ai-citation-landscape]] — pricing-page citation rates, review
  platforms, and Reddit's role.
- [[ai-overview-grounding-and-fidelity]] — the general problem of AI
  answers making claims their cited sources don't support.
- [[technical-seo-audit-checklist]] — the JavaScript-rendering and
  AI-crawler checks this audit relies on.
- [[ai-entity-footprint-audit]] — the broader version of step 1
  (how AI describes your brand overall).
- [[competitor-citation-displacement]] — when a competitor's pricing
  story is the one being cited.
- [[ai-answer-volatility]] — sizes the run-to-run variation the step-1 baseline is meant to smooth; first-citation position is noisier than presence
- [[agent-experience-ax]] — readable own pages raise pricing accuracy and recommendation strength in agent answers
