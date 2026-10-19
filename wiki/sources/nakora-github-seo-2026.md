---
type: source
tags: [seo, aeo]
date_published: 2026-01-01
date_ingested: 2026-10-19
origin: raw/articles/nakora-github-seo.md
---

# GitHub SEO: Rank Your Repo and Get Adoption in 2026 (Nakora)

Enric Baltasar (fractional GTM consultant and AI SEO, Nakora), published
2026-01-01. A consultant's blog post with a lead-generation pitch ("over $8M
with SEO") and a link to the author's own free repo-visibility analyzer.

**Rigor:** practitioner reverse-engineering ("70+ hours"). No method,
sample or data was published. Examples are single searches. It is still an
**independent** look at GitHub ranking, separate from the Markepear lineage
([[markepear-github-search-engine-optimization]]), and the only source here
that separates topic pages from search results. It cites three outside
sources (Backlinko on ChatGPT using Google; "Scoring Popularity in GitHub",
the 0.925 stars-popularity correlation; and a Wiley *Software: Practice and
Experience* paper on ranking for multiple terms). None of them were
ingested here.

## Key takeaways

1. **There are two ranking environments, not one.** The **topic page**
   (e.g. `github.com/topics/cicd`) is "almost exclusively" about stars. The
   **search results page** varies more: for "CI/CD" a 544-star repo
   outranked repos with 2.5k and 14.06k stars.
2. **Topic pages are where Google traffic lands.** Developers add "github"
   to Google searches ("headless cms github"), and the result is often a
   topic page (Strapi wins that one). He calls topic pages "the most
   important environment", the one that reaches "where 99% of the searches
   happen: on Google and ChatGPT". That figure is asserted, with no data.
3. **His ranking-factor groups:** *search proximity* (name, About,
   **README content**), *popularity* (topic tags), *engagement* (stars,
   forks, watchers, issue count, click-through rate), *messaging* (clarity,
   consistency). The README entry conflicts with GitHub's own docs for
   default search. See [[github-repository-seo]].
4. **Name:** descriptive names (`ai-chatbot-framework` ranks #1 for
   "chatbot framework") beat branded ones (`botasaurus`) for SEO. Branded
   repos can still win through topic pages.
5. **Keyword:** brainstorm what developers type, check volume (Ahrefs'
   free Keyword Generator), and put the keyword in name, About and README.
   Use variants to avoid stuffing. Example: Azure's `GPT-RAG` ranks for
   "rag gpt" and the misspelled brand query "azure gtp" (820 Google
   searches a month).
6. **About:** answer what it is, who it's for, when you need it, how it's
   different, what it integrates with and how it works. Length: **under 120
   characters is ideal, 120–250 is sometimes acceptable, over 250 is too
   long**. The About text also appears on topic pages.
7. **Topics:** called "the most underoptimized" lever for GitHub, Google
   and LLMs. Use **at least 6** (20 max), mixing purpose
   (`text-classification`, `data-visualization`), stack (`nextjs`, `aws`)
   and field (`machine-learning`, `nlp`). Pick tags with **middling
   competition**, not empty ones or ones you can't win. Don't tag your
   primary language, since GitHub already filters by it. Skip junk tags
   (`beta-feature`, `2027`, `draft`, `app`). Case study: Oxylabs'
   `amazon-scraper` (about 2.5k stars) ranks for "amazon scraper", "amazon
   scraper api" and "ecommerce scraper" by combining topic tags with
   on-page SEO.
8. **Freshness:** developers skip stale repos, and he asserts search
   engines penalize old dev content more than other industries. Make small
   doc updates regularly and release often.
9. **README heading hierarchy:** one H1, then H2s (Quickstart, Examples,
   FAQs) and H3 questions. Check it with the Detailed SEO extension, even
   though GitHub's rendered markup is messy.
10. **"Rank in Google, and you'll rank in AI."** Based on one Backlinko
    post. The wiki's evidence is more mixed. See the conflict on
    [[github-repository-seo]].

## What this updated

- [[github-repository-seo]] (new): two-environment model, topic-page
  routing from Google, About length guide, topic-selection rules.
- [[github-repo-optimization-checklist]] (new): topic mix, freshness,
  README headings.
- Two conflicts logged against [[markepear-github-search-engine-optimization]]
  (README as a GitHub-search factor; single-word vs. hyphenated topics),
  plus a flagged overstatement (rank in Google = rank in AI) against
  [[ai-citation-landscape]].
