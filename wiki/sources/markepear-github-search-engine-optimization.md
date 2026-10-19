---
type: source
tags: [seo]
date_published: 2024-07-03
date_ingested: 2026-10-19
origin: raw/articles/markepear-github-search-engine-optimization.md
---

# GitHub Search Engine Optimization: how to rank your repository in GitHub search (Markepear)

Jakub Czakon (CMO at a dev tool startup, dev marketing advisor), Developer
Markepear blog. Dated 2024-07-03 in the page's meta description; the
screenshots and examples appear to date from about March 2022.

**Rigor:** practitioner observation. The author ran a handful of live GitHub
searches and explained the orderings he saw. There was no controlled test,
no sample size, and the ranking factors are his inference. It is still the
**original source** for the GitHub-search framework that later guides
(including [[infrasity-github-seo-guide]]) repeat almost step for step. On
which fields are searched, [[github-docs-repository-search-and-topics]]
backs it up.

## Key takeaways

1. **The README revamp didn't move GitHub search traffic.** That is what
   prompted the investigation. His conclusion: About and Topics matter
   more. GitHub's docs agree that the README isn't searched by default
   ([[github-docs-repository-search-and-topics]]).
2. **Inferred ranking factors**, in no order: Name, About, Topics, Stars,
   Watchers, Forks.
3. **The keyword in the repo name beats popularity.** For "deep learning
   python", `deep-learning-with-python-notebooks` ranked above Keras, which
   has about 4× the stars. `DeepLearningPython` (about 2.2k stars) ranked
   above fastai (about 22k).
4. **About: core keywords and little else.** He thinks the *share of the
   About text that is search terms* matters. `cgm-remote-monitor` (3-word
   About) outranked Prometheus (8 words, 20× the stars) for "monitoring".
   Keep it readable and different from the other results, because it also
   has to earn the click. One contrasting emoji helps it stand out, but
   emoji count toward word count.
5. **Topics need an exact match.** Name and About match keyword variants,
   but Topics don't. Multi-word topics are hyphenated, so
   `data-science` only matches a query typed as "data-science". He
   recommends **single-word topics**, using the 20-topic limit carefully
   and **dropping keywords already in Name or About**. Topics also let a
   repo be nearly the only result for a narrow query ("orchestration
   keras" returned 4 results, and Polyaxon won by having `keras` as a
   topic).
6. **Stars, watchers and forks matter but can't be changed directly.** You
   raise them through traffic (Reddit, Twitter, Medium, Slack), a README
   built to convert (what it does, how to start, what it supports, how to
   install, a visual or GIF, copy-paste code, badges) and a "hello bar"
   asking for a star. His example is Algolia DocSearch.

## What this updated

- New concept page [[github-repository-seo]] and new playbook
  [[github-repo-optimization-checklist]], both built mainly from this
  source.
- Sits on one side of two conflicts recorded on [[github-repository-seo]]:
  whether the README affects GitHub search (against
  [[nakora-github-seo-2026]]), and single-word vs. hyphenated topics (also
  against Nakora).
