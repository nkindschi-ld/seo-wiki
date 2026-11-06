---
type: source
tags: [seo]
date_published: unknown
date_ingested: 2026-10-19
origin: raw/articles/github-docs-repository-search-and-topics.md
---

# GitHub Docs: Searching for repositories, and topic rules (first-party)

GitHub's official documentation, undated living pages:
[Searching for repositories](https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories)
and the topic rules from
[Classifying your repository with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics).
Added during the 2026-10-19 GitHub SEO ingest, with the user's go-ahead, to
check practitioner claims against GitHub's own docs.

**Rigor:** first-party and authoritative on **what is searched and what the
rules are**. It says **nothing about how results are ranked** (best-match
weighting, star influence), so every ranking-factor claim in the wiki
remains practitioner inference.

## Key takeaways

1. **Default repository search covers name, description and topics
   only.** Quote: "When you omit this qualifier, only the repository name,
   description, and topics are searched." The README is searched only with
   an explicit `in:readme`. Apart from `in:readme`, repo contents can't be
   searched through repository search (code search is separate).
2. **Stars, forks, followers, size, language, topics, license, created and
   pushed dates, and archived/template/mirror status** are all *filter*
   qualifiers (`stars:>=500`, `pushed:>2026-01-01`,
   `good-first-issues:>2`). Developers can use them to exclude repos, but
   the docs don't say they affect default ranking.
3. **Topic rules:** "Add no more than 20 topics." "Use lowercase letters,
   numbers, and hyphens." "Use 50 characters or less." The most-used topics
   are browsable at `github.com/topics/`, and GitHub keeps a set of
   *featured* topics that anyone can contribute to through the
   `github/explore` repo.
4. **`good-first-issue` and `help-wanted` labels are searchable
   qualifiers.** Labeling issues makes a repo findable by contributors
   filtering on them.

## What this updated

- [[github-repository-seo]] (new): first-party evidence that the README
  isn't a default GitHub-search field. It supports
  [[markepear-github-search-engine-optimization]] over
  [[nakora-github-seo-2026]] in the README conflict, but only for the
  default search box, not for Google, topic pages or AI answers.
- [[github-repo-optimization-checklist]] (new): the 20-topic, 50-character,
  lowercase-and-hyphen limits, and the issue-label tip.
