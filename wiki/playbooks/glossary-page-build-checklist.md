---
type: playbook
tags: [seo, aeo]
updated: 2026-11-02
---

Why / when to use this: use it when your subject has jargon your
audience searches for ("what is X"), and you want a definition-intent
content layer that feeds internal links into guides and product pages.
Concept, rationale, and the open structure conflict are in
[[glossary-pages-for-seo]].

## 1. Source terms

- [ ] GSC queries containing "what is", "meaning", "definition", or
      "vs" ([[keyword-research]]).
- [ ] Keyword tools (Semrush/Ahrefs) for volume and difficulty. Favor
      reasonable volume and manageable competition.
- [ ] Question tools: People Also Ask, AnswerThePublic, AlsoAsked.
- [ ] Competitor glossaries (models: Semrush, HubSpot, Salesforce,
      Zoho).
- [ ] **Customer language**: terms that come up in sales calls,
      support chats, and transcripts ([[airfleet-why-websites-need-glossaries]]).
- [ ] Dedupe against existing posts that already target the same "what
      is X" query ([[keyword-mapping-and-cannibalization]]).

## 2. Choose the architecture

- [ ] Group terms **by topic/meaning**, not just A–Z: core terms,
      technical definitions, intent variants, problem-based queries
      ([[seomyclicks-glossary-page-seo-2026]]).
- [ ] Per term, decide whether it gets its **own URL** or stays an
      **anchored entry** on a hub. Give it its own URL only if it has
      its own search demand *and* you can write substantive content.
      This is an unresolved conflict: see [[glossary-pages-for-seo]].
- [ ] Keep A–Z navigation and on-page search on the hub for usability.
- [ ] Split into topic sub-hubs once the glossary gets large.

## 3. Write each entry (consistent template)

- [ ] Put the one-to-two-sentence plain-English definition **first**,
      written so it makes sense alone (snippet/AI-citable;
      [[geo-content-optimization-tactics]]).
- [ ] Add a use-case example or context.
- [ ] List related terms, linked.
- [ ] Link to the deeper guide, product, or service page (or add a CTA).
- [ ] Add a diagram or visual where it clarifies a concept
      ([[goodspeed-seo-glossary-visibility]]).
- [ ] Store entries as structured CMS fields (term, definition,
      synonyms, related terms, meta description) so the template stays
      consistent and related-term links can be generated.
- [ ] Don't mass-produce templated or AI-boilerplate definitions. That
      is a Scaled Content Abuse risk ([[e-e-a-t-and-page-quality]]).
- [ ] If you use accordions, make sure the text is in the HTML on load
      (crawlable), not fetched only on click.

## 4. Link it into the site

- [ ] Glossary → deeper content, and term → sibling terms.
- [ ] Blog posts, docs, and product pages → glossary on first use of a
      term. Use descriptive anchors ([[link-and-anchor-text-best-practices]]).
- [ ] Link the glossary hub from navigation or the footer
      ([[footer-optimization]]) so it isn't an orphan.
- [ ] Promote it through the blog, social, and newsletters. Point
      guest-post links at term pages ([[link-building-outreach-tactics]]).

## 5. Markup and accessibility

- [ ] `DefinedTerm` per term and `DefinedTermSet`/`ItemList` for the
      collection.
- [ ] Don't rely on FAQ rich results (restricted since Aug 2023).
- [ ] Make it mobile-friendly, screen-reader and keyboard navigable,
      and use semantic headings per term.

## 6. Measure and maintain

- [ ] Track glossary query coverage, impressions, and clicks in GSC.
      Also track clicks *through* to linked pages, not just
      time-on-page/bounce.
- [ ] Track AI citations of definitions where you can
      ([[seo-reporting]]).
- [ ] Each quarter: review definitions, add emerging terms, fix broken
      links, and prune or consolidate terms with no impressions
      ([[content-pruning-playbook]]).

## Related

[[glossary-pages-for-seo]] · [[topic-cluster-strategy]] ·
[[entity-based-seo-implementation]]
