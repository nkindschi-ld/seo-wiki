# The Complete List: Every Search Engine Hidden Inside ChatGPT's Retrieval Leak

**Author:** David Konitzny
**Published:** 2026-09-17
**Source:** LinkedIn Pulse
**URL:** https://www.linkedin.com/pulse/complete-list-every-search-engine-hidden-inside-leak-david-konitzny-uwofe/
**Captured:** 2026-09-17

---

## Framing (author's own summary)

Metehan [Yesilyurt] uncovered a leak in ChatGPT's server-sent events (SSE) that
exposes internal retrieval metadata. Per the author, it reveals: which search
queries are generated, which engines are called, what results they return, how
those results are scored, what gets fetched, and what ultimately makes it into
the final answer.

This article shares one specific piece: the complete list of search engines
extracted from that retrieval leak. The author notes some engines were already
known and observed live; others remain unexplained. The engines split cleanly
into **internal** and **external**. Internally, one engine family dominates:
`labrador`, in dozens of variants (wiki, arxiv, news, reddit, local, finance,
legal, medical, and its own image search). Externally: Bing, Getty, SerpAPI,
Yelp, Foursquare.

The post is framed as an open community data-sharing exercise, inviting others
to contribute findings on when each engine is triggered and what the unknown
names do.

---

## INTERNAL ENGINES

### Source: `labrador`

| Engine name | source | tags | result_types | rewriter_name |
|---|---|---|---|---|
| labrador-aixiv | labrador | internal | aixiv | literature_search_query |
| labrador-arxiv | labrador | internal | arxiv | bing_query |
| labrador-arxiv-web | labrador | internal, oai-web, oai-web-aux | arxiv | bing_query |
| labrador-finance | labrador | internal | finance | finance_search_query |
| labrador-images | labrador | internal, image | images | image_query |
| labrador-images-nocache | labrador | internal, image | images | image_query |
| labrador-knowledge-legal-pdf | labrador | internal | knowledge-legal-pdf | bing_query |
| labrador-knowledge-legal-text | labrador | internal | knowledge-legal-text | bing_query |
| labrador-knowledge-medical-pdf | labrador | internal | knowledge-medical-pdf | bing_query |
| labrador-knowledge-medical-text | labrador | internal | knowledge-medical-text | bing_query |
| labrador-legal | labrador | internal | legal | legal_search_query |
| labrador-local | labrador | internal, local | places | null |
| labrador-news-1d | labrador | internal, news | news | bing_query |
| labrador-news-7d | labrador | internal, news | news | bing_query |
| labrador-news-all | labrador | internal, news | news | bing_query |
| labrador-news-google-redirect-fallback | labrador | internal, news | news | bing_query |
| labrador-reddit-web | labrador | internal, oai-web, oai-web-aux | reddit | bing_query |
| labrador-stem | labrador | internal | stem | bing_query |
| labrador-synthetic | labrador | internal | synthetic | bing_query |
| labrador-synthetic-index | labrador | internal | synthetic-index | bing_query |
| labrador-web-pdf | labrador | internal, oai-web, oai-web-aux | web-pdf | bing_query |
| labrador-web-youtube | labrador | internal, oai-web, oai-web-aux | web-youtube | bing_query |
| labrador-wiki | labrador | internal | wiki | bing_query |
| labrador-wiki-web | labrador | internal, oai-web, oai-web-aux | wiki | bing_query |
| system1-arxiv | labrador | system1, internal | arxiv | system1_search_query |
| system1-labrador-news-google-redirect-fallback | labrador | system1, internal, news | news | system1_search_query |
| system1-news-1d | labrador | system1, internal, news | news | system1_search_query |
| system1-news-7d | labrador | system1, internal, news | news | system1_search_query |
| system1-news-all | labrador | system1, internal, news | news | system1_search_query |
| system1-stem | labrador | system1, internal | stem | system1_search_query |
| system1-wiki | labrador | system1, internal | wiki | system1_search_query |
| system2-arxiv | labrador | internal, oai-web, oai-web-aux, system2 | arxiv | system2_search_query |
| system2-image | labrador | system2, internal, image | images | system2_image_query |
| system2-labrador-news-google-redirect-fallback | labrador | system2, internal, news | news | system2_search_query |
| system2-news-1d | labrador | system2, internal, news | news | system2_search_query |
| system2-news-7d | labrador | system2, internal, news | news | system2_search_query |
| system2-news-all | labrador | system2, internal, news | news | system2_search_query |
| system2-reddit | labrador | internal, oai-web, oai-web-aux, system2 | reddit | system2_search_query |
| system2-stem | labrador | internal, oai-web, oai-web-aux, system2 | stem | system2_search_query |
| system2-web-pdf | labrador | internal, oai-web, oai-web-aux, system2 | web-pdf | system2_search_query |
| system2-web-youtube | labrador | internal, oai-web, oai-web-aux, system2 | web-youtube | system2_search_query |
| system2-wiki | labrador | internal, oai-web, oai-web-aux, system2 | wiki | system2_search_query |

### Source: `labrador-web`

| Engine name | source | tags | result_types | rewriter_name |
|---|---|---|---|---|
| labrador-web | labrador-web | internal, oai-web | web | bing_query |
| labrador-web-news-google-redirect-fallback | labrador-web | internal, web, news | web, news | bing_query |
| system1-labrador-web-fallback | labrador-web | system1, internal, oai-web | web | system1_search_query |
| system1-labrador-web-news-google-redirect-fallback | labrador-web | system1, internal, oai-web, news | web, news | system1_search_query |
| system2-web | labrador-web | system2, internal, oai-web | web | system2_search_query |

---

## EXTERNAL ENGINES

| Engine name | source | tags | result_types | rewriter_name |
|---|---|---|---|---|
| bing | bing | external, web | webpages, news | bing_query |
| bing-image | bing | external, image | images | image_query |
| fortis | fortis | external, web | webpages, news, business | bing_query |
| fortis-barebone | fortis_barebone | external, web | webpages, news, business | bing_query |
| foursquare | foursquare | external, business | null | null |
| getty-image | getty | external, image | images | image_query |
| labrador-web-fallback | labrador-web | external, web | web | bing_query |
| mai-grounding-bing-query | mai_grounding | external, web | webpages | bing_query |
| system1-mai-grounding-web | mai_grounding | system1, external, web | webpages | system1_search_query |
| mai-grounding-news | mai_grounding_news | external, news, mai-news-beta | news | bing_query |
| system1-mai-grounding-news | mai_grounding_news | system1, external, news, mai-news-beta | news | system1_search_query |
| system2-mai-grounding-news | mai_grounding_news | system2, external, news, mai-news-beta | news | system2_search_query |
| serpapi-image | serpapi_auto_image | external, image | images | image_query |
| system1-image | serpapi_auto_image | system1, external, image | images | system1_image_query |
| serpapi-news | serpapi_auto_news | external, news | news | bing_query |
| serpapi-news-tab | serpapi_auto_news | external, news | news | bing_query |
| serpapi-news-tab-light | serpapi_auto_news | external, news | news | bing_query |
| system1-news-serpapi | serpapi_auto_news | external, news, system1 | news | system1_search_query |
| system2-news-serpapi | serpapi_auto_news | external, news, system2 | news | system2_search_query |
| serpapi | serpapi_auto_web | external, web | webpages, news | bing_query |
| system1-web | serpapi_auto_web | system1, external, web | webpages, news | system1_search_query |
| yelp | yelp | external, business | null | null |

Note: the author's section headings list `Fortis_barbone` (sic) as the source
heading for the `fortis-barebone` engine, whose own `source` field reads
`fortis_barebone`.

---

## Notable comments (engagement: ~37 reactions, 6 comments at capture)

- **Jayson DeMers:** "the separate Reddit engine in that list tells you how much
  weight those threads carry. Nobody builds a dedicated retrieval path for a
  site unless the answers depend on it."
- **Tomek Rudzki:** expresses pride in being part of the team.
- **Brent Bouldin:** asks whether there is any data yet on frequency of calls
  by engine. (Unanswered at capture.)

## Author's related prior articles (context, not ingested here)

- "Inside ChatGPT's New Search Language: How Fresh Does Content Really Need to
  Be?" — 2026-09-01
- "ChatGPT 5.6 Is Eating Deeper Into the Web" — 2026-08-28
- "How Unique Are Domains and URLs in ChatGPT Query Fan-Outs?" — 2026-08-24
- "ChatGPT's New Default Model GPT-5.6: More Retrieval, More Fan-Outs, More
  First-Party Content" — 2026-08-10
