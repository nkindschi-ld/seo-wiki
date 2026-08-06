# Competitor Citation Steal Prompt (Framework)

- **Publisher:** DerivateX
- **Author:** Apoorv Sharma (co-founder)
- **Published:** 2026-04-10
- **URL:** https://derivatex.agency/frameworks/competitor-citation-steal-prompt/
- **Archived:** 2026-08-03 (structured extract via fetch)
- **Content type:** Original tactical framework + executable LLM prompt template
  (not a research study). Companion to DerivateX's "Two Googles, One Query"
  benchmark ([[derivatex-two-googles-one-query-aio-vs-serp-2026]]).

## Core idea

Standard AI-visibility monitoring shows *that* a competitor gets cited and you don't,
but not *why*. This framework does artifact-level diagnosis: identify the specific
content pieces, data points, or entity claims driving a competitor's citations, then
build to displace them. Distinguishes:

- **Citation gap:** "My competitor appears in ChatGPT; I don't."
- **Citation root cause:** "They appear because they own a proprietary benchmark,
  definition, or Reddit presence I lack."

## Seven-step method (executable in any LLM with web browsing)

1. **Citation Mapping** — audit 10 buyer-intent queries; identify which competitors
   ChatGPT cites and why.
2. **Gap Autopsy** — for each miss, diagnose the exact artifact, entity relationship,
   language pattern, and fastest build path.
3. **Steal Matrix** — rank gaps by **citation value ÷ steal difficulty**; prioritize
   highest-ratio targets.
4. **Artifact Blueprints** — for top 3 targets: URL slug, target citation sentence,
   content structure, proprietary data point required, off-site seeding targets.
5. **Entity Line Standardization** — one consistent brand definition across all
   surfaces (homepage, G2, Reddit, guest posts).
6. **30-Day Steal Calendar** — week-by-week execution plan with specific off-site moves.
7. **Diagnostic Prompt** — weekly Friday tracking prompt to measure citation-position
   changes.

## Prompt template (paraphrased — not reproduced verbatim)

A single copy-paste prompt casts the LLM as an "LLM Citation Intelligence Analyst."
For each of 10 queries it returns a table: Query | who ChatGPT cites | citation
position | why they get cited (exact mechanism) | do I appear? | if not, what do they
have that I don't. The prompt insists on specificity in the "why" column — name the
exact artifact doing the work (benchmark page, comparison table, Reddit thread…),
not "they have good content."

## Evidence cited (mostly corroborates sources the wiki already holds)

- **AirOps (early 2026):** ChatGPT retrieves ~100 pages but cites ~15; favors pages
  with data tables and short sentences. (cf. [[airops-fan-out-effect-2026]])
- **Search Engine Land:** content in first third of a page cited ~2x the final third.
  (cf. the first-30% finding in [[geo-content-optimization-tactics]])
- **SE Ranking (2025):** domains with Reddit/Quora presence ~4x higher citation
  likelihood. (cf. [[otterly-reddit-geo-ai-search-citations-2026]])
- **Stacker (late 2025):** content distributed across multiple publications increases
  AI citations up to **325%** vs. single-domain publishing. (NEW to wiki, secondhand)
- **Wix (early 2026):** listicles dominate commercial queries; definition pages with
  proprietary data earn most citations. (cf. [[wix-generative-engine-optimization]])

## Case studies (VENDOR CLAIMS — no disclosed methodology)

- **REsimpli:** zero to top-cited across 10+ real-estate-investor prompts in 90 days.
- **Gumlet:** 20% of inbound revenue attributed to ChatGPT/Perplexity discovery via
  deliberate citation engineering. (Same Gumlet case referenced in the "Two Googles"
  report.)

## Notable quotes

- "When ChatGPT or Perplexity recommends your competitor by name and ignores your
  brand, you lose the deal before the buyer ever visits your website… The loss is
  silent."
- "An artifact without seeding is a page that exists. An artifact with seeding is a
  citation source."
- "A company can rank first on Google and be absent from every AI recommendation in
  its category simultaneously."
