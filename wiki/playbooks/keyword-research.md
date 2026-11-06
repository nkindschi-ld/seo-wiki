---
type: playbook
tags: [seo, aeo]
updated: 2026-11-06
---

Why / when to use this: run this *before*
[[keyword-mapping-and-cannibalization]] — that playbook assumes you
already have a keyword list to assign to pages; this one is about
discovering and prioritizing which keywords belong on that list in the
first place, including keywords that don't show up in traditional
volume-based tools at all.

## The shift this playbook reflects

Three structural changes from older keyword-research practice:
- **Volume-first → business-value-first**: high-volume head terms are
  increasingly answered directly by AI features before a click happens
  (see [[aio-ctr-impact]]) — chasing raw volume alone is less reliable
  than it used to be.
- **Google-only → search-everywhere**: audiences research across
  Reddit, Amazon, YouTube, and AI chat tools, not just Google's search
  box.
- **Query-matching → prompt research**: AI tools are used with longer,
  conversational prompts rather than short keyword-style queries.

## Six discovery methods (use more than one)

1. **Check existing search visibility.** GSC queries with high
   impressions but low clicks (near-miss content); Bing Webmaster
   Tools' AI-grounding-query report if available; rank-tracking tools
   filtered to positions 11+ with real volume and moderate difficulty —
   these are "almost ranking" opportunities, cheaper to fix than to
   build from scratch.
2. **Mine first-party data.** Sales-call questions and objections,
   support-ticket recurring issues, onboarding-conversation confusion
   points. Zero-cost, high-signal, and hard for competitors to
   replicate since it comes from your own customer conversations.
3. **Study social platforms and forums.** Reddit, Quora, YouTube
   comments, TikTok discussions. Practical workflow: paste raw comment/
   thread text into an LLM (ChatGPT/Claude) with a targeted extraction
   prompt ("generate a list of keywords based on unanswered questions,
   pain points, or keyword opportunities in this text") to surface
   zero-search-volume-but-real-demand keywords that standard tools miss
   entirely.
4. **Search keyword databases.** Standard keyword-research tooling for
   related terms; filter to "Questions" for long-tail phrasing. Note:
   long-tail keywords specifically align with AI **query fan-out**
   behavior (an AI system running several related sub-searches per
   prompt to build a comprehensive answer) — long-tail content gets a
   second visibility channel through fan-out sub-queries beyond direct
   search matching.
5. **Run keyword gap analysis** — both traditional (terms competitors
   rank for that you don't) and **AI-search gap analysis** (competitor
   prompts in an AI-visibility tool where they appear and you don't,
   filtered to "Missing"/"Weak").
6. **Analyze SERP features.** People Also Ask (matches conversational
   AI-query phrasing directly); Related Searches; AI Overviews — note
   which topics they already cover fully (low remaining click
   potential) vs. partially (opportunity remains).

## Zero-volume and "new tail" queries

Keyword databases miss two kinds of real demand. Both are worth a
deliberate pass.

**Zero-volume converting queries** ([[dejan-stealthy-queries-2026]]):

- Zero volume in a tool isn't zero demand. One paper-title query showed
  zero in a keyword database but 1,020 impressions and 37 clicks in GSC
  in a month, across many phrasing variants. Check GSC, not just tools.
- Side benefit: traffic estimators undercount these sites, so
  competitors overlook them. Jumping early on trending research and data
  can make you the default result during the spike.
- Best raw sources: internal site search logs, support and chatbot
  transcripts, quote requests and CRM notes joined to closed deals
  ("furnace shuts off after five minutes", not "furnace repair"), sales
  calls, community threads. Broad-match Google Ads with heavy negatives
  can surface converting queries no tool records.
- Synthetic expansion (LLM or embedding-based) produces candidates, but
  confirm real people use the phrasing before building pages.
- Workflow: collect raw queries → classify intent with an LLM → cluster
  into canonical variants → map to an entity graph of topics, problems,
  and offerings → build content and internal links from it.

**New-tail queries** ([[dejan-new-tail-keyword-research]]):

- What people type when they don't know a product's name: descriptions
  by look, location, use, or analogy ("moss-like grass"). Often short.
- Method: show ~100 people a product photo (open-ended answers) and ask
  what they'd search for. In the original case, 44 of 68 terms were
  missing from the top-ranking page, which was stuck on the owner's own
  framing ("no mow").
- Tag and cluster the answers, then add a natural-language attributes
  section, improve alt text, or create a "types of…" page. Don't stuff.
- AI-era extension: assistants write their own [[query-fanout]]
  sub-queries, which never appear in GSC. Ask a model the same photo
  question many times too; where its vocabulary differs from the human
  survey, cover both.

## Prioritization framework (6 dimensions)

- **Conversion potential** — keywords tied to direct business actions
  (sign-up, purchase, demo) outrank purely informational terms, all
  else equal.
- **Search volume** — still a real signal, but not sufficient alone.
- **Click potential** — high: comparisons, best-of lists, complex
  how-tos. Low: simple definitions/facts an AI feature can fully answer
  inline.
- **Real-world demand signals** — appearing in sales calls, Reddit
  threads, support tickets, or YouTube comments indicates genuine
  interest even at zero measured search volume.
- **Trend analysis** — favor stable/growing trends; treat declining
  trends as higher-risk unless backed by real-world demand signals or
  known seasonality.
- **Attainability** — new/smaller sites: target lower difficulty
  (roughly 0-49%); established sites can pursue more competitive terms.

## Niche-specific additions

When the target is a narrow niche rather than a broad topic:
- Add audience-qualifier terms to seeds in autocomplete (e.g. "micro
  business", "non-profits"), and sort Keyword Planner results from low
  to high volume — low volume is a niche signal
  ([[semrush-niche-keyword-research]]).
- Group keywords by awareness stage — problem-aware, solution-aware,
  transaction-adjacent, authority — rather than by volume alone
  ([[surnex-finding-a-niche]]).
- Check the niche is worth entering at all before building the list:
  [[niche-validation-playbook]] and [[niche-selection-and-validation]].

**Quick filter before adding any keyword to the working list** — confirm
at least one applies: builds brand awareness, improves AI visibility,
attracts qualified leads, or drives direct purchases.

## Ongoing process, not a one-time project

Keyword research needs revisiting as search behavior shifts (new AI
features, new competitor content, seasonal changes) — treat the list as
a living document, not a single deliverable to hand off once.

## Checklist

- [ ] Discovery drew from at least 3 of the 6 methods above, not just a
      keyword database export.
- [ ] First-party data (sales/support/onboarding) reviewed for
      keyword signal.
- [ ] Both traditional and AI-search gap analysis run against
      competitors.
- [ ] Each shortlisted keyword scored against all 6 prioritization
      dimensions, not volume alone.
- [ ] Every keyword on the final list passes the quick filter (brand
      awareness / AI visibility / qualified leads / direct purchases).
- [ ] Revisit cadence scheduled — not treated as a one-time exercise.
- [ ] Zero-volume queries checked in GSC and first-party logs, not
      dropped because a tool shows no volume.
- [ ] For products people may not know by name, a new-tail survey (human,
      and repeated model sampling) has been run.

## See also

- [[keyword-mapping-and-cannibalization]] — assigns discovered
  keywords to specific pages and diagnoses cannibalization once mapped.
- [[topic-cluster-strategy]] — groups discovered keywords into
  pillar/subpage clusters.
- [[generative-engine-optimization]] and [[geo-content-optimization-tactics]]
  — background on AI query fan-out and AI-visibility measurement
  referenced above.

See [[semrush-keyword-research-2026]] for the full source writeup.
Niche-specific tactics: [[semrush-niche-keyword-research]],
[[surnex-finding-a-niche]].
