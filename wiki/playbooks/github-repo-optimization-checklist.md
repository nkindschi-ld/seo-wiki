---
type: playbook
tags: [seo, aeo]
updated: 2026-10-19
---

# GitHub Repo Optimization Checklist

**Why / when to use this:** use it when launching or reworking a public
repo (an SDK, an open-source tool, examples, or a docs-style repo that leads
to a paid product) that should be found through GitHub search, GitHub topic
pages, Google and AI answers. The concept, evidence and conflicts are on
[[github-repository-seo]]. Most items rest on practitioner inference. Items
backed by GitHub's own docs are marked **(docs)**.

## 1. Pick the target query

- [ ] Brainstorm what a developer would type on GitHub or Google ("python
  testing", "headless cms github"). Check Google volume with a keyword tool
  ([[nakora-github-seo-2026]]).
- [ ] Choose **one core keyword** and a few variants and synonyms. Don't
  stuff.

## 2. Name

- [ ] Put the core keyword in the repo name if you can. A descriptive name
  beats a branded one in search. Adding the stack helps
  (`microsoft-authentication-library-for-js`).
- [ ] If the name has to stay branded, rely more on About, topics and
  topic pages.

## 3. About (description)

**(docs)** The About is one of three fields searched by default.

- [ ] Lead with the core keyword. Say what it does and for whom, not how
  good it is.
- [ ] Keep it short: about 5–15 words, under 120 characters ideally, never
  over 250. Shorter keeps the keyword's share of the text high
  ([[markepear-github-search-engine-optimization]]).
- [ ] Name the platform or integration ("for Kubernetes", "YAML to PDF").
- [ ] Make it distinct from neighboring results. One contrasting emoji is
  fine (it counts as a word). Three is too many.
- [ ] Remember that the About also shows on topic pages, so it has to win
  the click there too.

## 4. Topics

**(docs)** 20 topics max. Lowercase letters, numbers and hyphens only, 50
characters or less. Topics are searched by default and decide topic-page
membership.

- [ ] Use at least 6, mixing **purpose** (`monitoring`,
  `data-visualization`), **stack** (`nextjs`, `kubernetes`, `aws`) and
  **field** (`machine-learning`, `devops`).
- [ ] Include **single-word** topics for search-box matching, and the
  **hyphenated** topics whose `github.com/topics/…` pages you want to
  appear on. The sources disagree on this. See the conflict on
  [[github-repository-seo]].
- [ ] Aim for topics with middling competition, not empty ones or ones
  dominated by repos with far more stars than you.
- [ ] Add one or two niche topics for narrow combinations where you could
  be nearly the only result.
- [ ] Skip your primary language (GitHub already filters by it) and junk
  tags (`draft`, `beta-feature`, `2027`, `app`).

## 5. README

The README doesn't affect GitHub's default search **(docs)**. It matters for
Google, AI retrieval and conversion.

- [ ] One H1 (project name), then H2s such as Quickstart, Examples and
  FAQs, with H3 questions under FAQs.
- [ ] Answer the four conversion questions early: what it does, whether it's
  for me, what it uses or supports, and how to get a first success (install
  and run).
- [ ] Add a screenshot or GIF of the result, copy-paste code, and badges
  (language, license, build).
- [ ] Use precise technical terms (`OAuth2`, `FastAPI`) in headings and in
  `.md` file names ([[infrasity-github-seo-guide]]).
- [ ] Add a star CTA and links to docs, the site and the community.
- [ ] Keep the quickstart scriptable end to end, so coding agents can follow
  it too ([[optimizing-for-coding-agent-recommendations]] point 3).

## 6. Popularity and engagement

- [ ] Distribute: Reddit (r/programming, r/webdev, niche subs), X, Dev.to,
  daily.dev, Medium, LinkedIn, Slack and Discord communities, newsletters,
  or a Product Hunt launch.
- [ ] Add a "hello bar" on docs or the site asking for a star (Algolia
  DocSearch is the example used).
- [ ] Label `good-first-issue` and `help-wanted` issues. **(docs)** They're
  searchable qualifiers for contributors.

## 7. Freshness

- [ ] Push regularly, even small doc updates. Developers filter by `pushed:`
  and skip stale repos.
- [ ] For a new tool, release early and often rather than publishing once
  and going quiet.

## 8. Measure

- [ ] Run the target queries in GitHub search (logged out) and on the
  relevant `github.com/topics/…` page, before and after changes. Practitioners
  report About and topic changes showing up in "almost real time".
- [ ] Track Google rankings for the repo URL and "X github" queries.
- [ ] Check whether AI answers for the query cite the repo or its topic
  page, using the methods in [[ai-visibility-measurement-methodology]].

## Related

- [[github-repository-seo]]: the concept page, with the conflicts.
- [[optimizing-for-coding-agent-recommendations]]: the coding-agent side
  of developer-tool discovery.
- [[llms-txt]]: a machine-readable index for docs sites (not repos).
