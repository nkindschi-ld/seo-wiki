---
type: source
tags: [aeo]
date_published: 2026-09-20
date_ingested: 2026-11-06
origin: raw/articles/dejan-ai-mode-tags-2026.md
---

# AI Mode Tags: FollowUp, Generate, Layout, Entity List and @prompt_leaks.ignore (DEJAN)

DEJAN AI (2026-09-20). dejan.ai/blog/ai-mode-tags/.

**Nature of source — low confidence**: catalogue of tags claimed to be
used internally by Google AI Mode to structure responses. No method is
given (presumably prompt leaks / output inspection). The text contains
leftover LLM-review phrasing ("Your draft misses…"), and examples use
DEJAN's own products, so parts appear LLM-generated and the
"restrictions" may be model confabulation. Treat as unverified.

## Key takeaways

1. **Conversation/UI tags**: `<FollowUp>` (closing clarifying questions,
   key terms bolded), `<Generate>` (build a custom widget) and `<Widget>`
   (session-only runtime state), `<Python>`/`<code>` sandbox (no
   network), `<File>` exports, `<DataViz>`, `<InlineQuiz>`.
2. **Layout**: `<layout type="map|comparison|inspiration">`;
   `<Carousel showMetadata>`, `<ImageGrid>`, `<Image srcId>` (assets
   referenced by backend index, not URL).
3. **Commerce/local/live**: `<List>` + `<Entity type=…>`, `<Product>`
   (catalog-level), `<ShoppingOffers>` (merchant feed, single concrete
   product), `<Event>`, `<FlightStatus>`, `<Video>`/`<Media>` (only if a
   verified video asset exists in the search payload).
4. **30 entity types** (e.g. `LodgingPlace`, `LocalServiceOrTradeBusiness`,
   `SkuLevelProduct`, `SpecificPurchasableSoftwareSystem`,
   `FinancialProductOrService`, `ShoppingBrand`, `SpecificPerson`,
   `Event`, `Other`), each mapped to a dominant layout and "required
   grounding attributes" (e.g. SkuLevelProduct → `<ShoppingOffers>`,
   GTIN + manufacturer; LocalServiceOrTradeBusiness → `<List>`, service
   area + license verification).
5. **Degradation rules**: list/carousel children must share one entity
   type; carousels/grids need ≥3 validated items, else fall back to plain
   markdown.
6. `<@prompt_leaks.ignore>` is described as a safety fence separating
   instructions from literal text.

## Wiki pages updated

- Created [[ai-mode-response-markup]] (concept, flagged low-confidence).
