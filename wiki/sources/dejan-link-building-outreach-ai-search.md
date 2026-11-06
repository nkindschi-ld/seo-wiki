---
type: source
tags: [seo, aeo]
date_published: 2026-10-06
date_ingested: 2026-10-08
origin: raw/articles/dejan-link-building-outreach-ai-search.md
---

# Link Building & Outreach for AI Search (DEJAN)

Petrovic, D. (2026-10-06). "Link Building & Outreach for AI Search."
DEJAN AI blog, dejan.ai/blog/outreach/.

**Nature of source**: practitioner essay by an AI-SEO agency founder,
partly promoting DEJAN's own tools (Link Optimizer, Adversarial Link
Integration). The link-prediction model, paid-link detector, and
grounding-funnel numbers are proprietary and not independently
validated. Treat the framework as well-reasoned practitioner opinion,
not measured evidence.

## Key takeaways

1. **Two paths into an AI answer.** Brands that appear widely and
   consistently in training data are answered from parametric memory —
   no retrieval, no citation. Anything past the knowledge cutoff, or
   weakly encoded, exists for the model only via web-search grounding,
   which puts weight on crawlability and freshness. Cites Allen-Zhu & Li
   (2024): ~2 bits/parameter of knowledge capacity at ~1,000 exposures
   per fact, ~1 bit at 100 — exposure count is the binding constraint.
   See [[parametric-memory-vs-grounding]].
2. **Grounding funnel (single query, anecdotal)**: pages received →
   readable → cited. Google 7 received / 7 cited; OpenAI 39 / 2;
   Anthropic 14 / 9.
3. **Incongruence kills outreach value.** The core test: "Who wanted the
   link/mention on this page?" If an experienced SEO can guess the paid
   link, so can Google's spam team and algorithms. Claims most
   outreach-based links are ignored or treated as a small negative
   signal, and dismisses DA/PA-style third-party authority metrics.
4. **Linking is predictable human behaviour.** DEJAN trained a model on
   organic and inorganic link patterns; at a 93% confidence threshold
   it closely reproduced a domain expert's ("Mike", a long-time SEO blogger) actual link
   placements in one article, with a couple of misses/false positives.
5. **The "1 + 2 rule" backfires** (one commercial link + 1–3 "authority"
   links to look natural): less natural, aids algorithmic detection,
   gives manual reviewers a pattern, worse UX. Organic content often
   carries 10–20 links per page; blog networks 2–3.
6. **Four rules for editorial-looking links** — liberal linking, purpose
   (ten link purposes, promotion included), primacy (strongest page for
   the spot), natural anchor text — each with a checklist. Plus
   placement at "link desire" peaks, and content-first sequencing.
7. **Adversarial link integration**: a red-team AI writes the article
   and places the link; a blue-team paid-link detector tries to find
   it; detected articles are discarded.
8. **Published false-positive correction**: an agency (Lawrence
   Hitches) disputed a flagged link as natural. DEJAN's audit says it
   tripped Blend and Independence (the only external editorial link on
   the page, while the case-study subject got no link), sat off the
   link-desire peak, and pointed at a homepage rather than the stronger
   case-study page.

## Wiki pages updated

- Created [[editorial-link-integration]] (playbook) and
  [[parametric-memory-vs-grounding]] (concept).
- Updated [[link-building]] and [[link-building-outreach-tactics]] —
  added Conflicting Evidence on authority metrics and outreach-link
  value.
- Updated [[link-and-anchor-text-best-practices]] — 10–20 organic links
  per page as further support for "no numeric cap"; cross-link.
