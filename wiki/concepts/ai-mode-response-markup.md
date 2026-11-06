---
type: concept
tags: [aeo]
updated: 2026-11-06
---

# AI Mode Response Markup (unverified)

> **Low confidence.** Everything on this page comes from one source,
> [[dejan-ai-mode-tags-2026]], which gives no method, appears partly
> LLM-written, and may include model confabulation. Google has not
> confirmed any of it. Use it as a hypothesis about how Google AI Mode
> structures answers, not as documentation.

## The claim

Google AI Mode is said to generate answers as text interleaved with
internal tags that the interface renders as rich modules — lists,
carousels, maps, product cards, merchant offers, widgets — and to fall
back to plain markdown when the data doesn't meet each module's
requirements.

## Reported tag families

- **Conversation and tools**: `<FollowUp>` (closing clarifying
  questions), `<Generate>` / `<Widget>` (on-the-fly interactive tools,
  session-only state), `<Python>` sandbox, `<File>`, `<DataViz>`,
  `<InlineQuiz>`.
- **Layout**: `<layout type="map">`, `"comparison"` (spec table),
  `"inspiration"` (full-width image gallery); `<Carousel>`,
  `<ImageGrid>`, `<Image srcId>`.
- **Entities and commerce**: `<List>` of `<Entity type=…>`, `<Product>`
  (catalog-level identity), `<ShoppingOffers>` (live merchant prices for
  one concrete product), `<Event>`, `<FlightStatus>`, `<Video>`.

## Entity types and their "required grounding attributes"

The source lists 30 entity types, each paired with a layout and the
attributes it supposedly needs. Examples:

| Entity type | Layout | Attributes |
|---|---|---|
| `SkuLevelProduct` | `<ShoppingOffers>` | GTIN, manufacturer |
| `LocalServiceOrTradeBusiness` | `<List>` | service area, license verification |
| `PhysicalStoreOrLocalBusiness` | map | address, opening hours |
| `LodgingPlace` | `<Carousel>` | price per night, review score |
| `SpecificPurchasableSoftwareSystem` | comparison | license type, OS compatibility |
| `FinancialProductOrService` | comparison | interest rates, fees, disclaimers |
| `Event` | `<Event>` | timeline, ticket link |

## Reported fallback rules

- Items in a `<List>` or `<Carousel>` must share one entity type, or the
  module degrades to bullet points.
- Carousels and image grids need at least 3 validated items.
- Video cards render only if a verified video asset exists in the search
  payload.

## If true, what it would mean

These are inferences, not tested findings:

- Being shown as a rich card depends on the engine being able to type
  your entity and find its key attributes. That aligns with existing
  advice to publish clean structured data and product feeds
  ([[entity-based-seo-implementation]], [[controlling-ai-feature-inclusion]]).
- For commerce, merchant-feed data (price, stock, shipping) would feed
  `<ShoppingOffers>`; for local services, service area and licensing
  would need to be stated explicitly and findably.

Revisit this page if a second, independent source confirms or
contradicts it.

## See also

- [[entity-oriented-search-fundamentals]] — entity typing background.
- [[query-fanout]], [[grounding-snippets]] — the retrieval steps before
  rendering.
- [[structured-data-and-ai-search]] — no AI-citation lift from schema, and facts that exist only in markup aren't extracted; put the "required attributes" in visible text.
