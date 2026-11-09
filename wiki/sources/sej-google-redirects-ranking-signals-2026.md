---
type: source
tags: [seo, aeo]
date_published: 2026-11-05
date_ingested: 2026-11-09
origin: raw/articles/sej-google-redirects-ranking-signals-2026.md
---

# Google Explains How Redirects Affect Ranking Signals (Search Engine Journal)

**Citation:** Montti, Roger. "Google Explains How Redirects Affect Ranking
Signals." Search Engine Journal. Published 2026-11-05.
https://www.searchenginejournal.com/google-explains-how-redirects-affect-ranking-signals/595967/

**Source type:** a news write-up of a Google discussion between Gary Illyes
and Cherry Prommawin (Google Search). The quoted statements come from Google.
The "My Takeaway" section is Montti's own opinion and carries less weight (see
below).

## Key takeaways

- **301 = permanent, 302 = temporary.** A 301 tells Google to update the index
  to the new URL. A 302 says the old URL will come back.
- **Both redirect types help clustering; only a 301 sets the canonical.**
  During deduplication, Google groups pages with similar main content into a
  cluster, then picks one representative URL (canonicalization). Both 301s
  and 302s count as clustering signals. Only the 301 has a canonicalization
  effect.
- **A 301 passes all ranking signals; a 302 doesn't.** Illyes: Google "takes
  all the ranking signals of the old page and hands them to the new page."
  With a 302, Google "keeps the old URL in the search results, and basically
  ignores the new URL."
- **308 and 307 are the modern versions of 301 and 302.** They serve the same
  permanent/temporary purposes. The only major difference is that 307/308
  keep the request as a POST and forward the submitted form data. A 302
  doesn't. Illyes' example is a checkout form failing over to a backup
  payment server. This matters for site functionality, not ranking.
- **Use server-side redirects, not JavaScript or meta refresh.** A server-side
  HTTP redirect is "a clean, instant instruction." JS and meta-refresh
  redirects make the browser download, parse, and execute the page first.
- **Mistakes aren't fatal.** Prommawin: whichever redirect you pick, "one of
  your pages will stay in search and be part of AI training." The choice
  decides *which URL* shows up, not whether the content is indexed. Google's
  crawlers themselves "don't care at all" which code is used; the difference
  shows up in deduplication.

## Author opinion (lower weight): "cannibalization is a myth"

Montti argues that keyword cannibalization contradicts how Google works:
Google clusters similar pages, picks one canonical, and consolidates the
signals there. On this view, what SEOs call cannibalization is really thin
content or a lack of uniqueness. Google didn't say this. Illyes and Prommawin
only described how near-duplicate content is clustered. Their description
doesn't cover pages that are distinct but compete for the same query, which
is the case [[keyword-mapping-and-cannibalization]] addresses. Filed there as
a flagged dissent, not a conflict to resolve.

## Gaps and caveats

- Doesn't address what happens to a 302 that stays in place for a long time,
  or whether Google eventually treats it as permanent. Don't read "302s never
  pass signals" as settled for long-lived 302s.
- Doesn't discuss redirect chains or hop limits. The chain guidance in
  [[technical-seo-audit-checklist]] ([[ahrefs-site-audit-study-2023]]) stands.
- Secondhand: an SEJ write-up, not the original Google recording or
  transcript.

## Relationship to existing wiki claims

- **Conflicts with** [[url-structure-best-practices]] /
  [[visively-url-structure-fundamentals]], which say every redirect hop
  "dilutes link equity *even when done correctly*." Google now says a 301
  hands over *all* ranking signals. Filed as Conflicting Evidence on
  [[url-structure-best-practices]]; logged as a `conflict`.
- **Extends** [[how-google-search-works]]'s indexing-stage canonicalization
  description with how redirects feed it (clustering signal vs. canonical
  signal).
- **Extends** [[technical-seo-audit-checklist]] with redirect-type selection
  (301/308 vs. 302/307, server-side only).
- **Supports** [[content-pruning-playbook]]'s 301-on-consolidation rule, and
  adds that a 302 used for a merge leaves the *old* URL in results.

## Pages updated

[[url-structure-best-practices]], [[how-google-search-works]],
[[technical-seo-audit-checklist]], [[content-pruning-playbook]],
[[keyword-mapping-and-cannibalization]]
