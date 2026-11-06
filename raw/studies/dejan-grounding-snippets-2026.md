Source: https://dejan.ai/blog/grounding-snippets/
Author: Dan Petrovic (DEJAN AI)
Published: 2026-06-21
Retrieved: 2026-11-06

# Grounding Snippets


![Grounding Snippets](/media/header/posts/grounding-snippets-603cbf16.png)


# Grounding Snippets

![](https://lh3.googleusercontent.com/a/ACg8ocIzPbX1yzNoZGisEyNHQT2qdNnPceJVlyoTQ1N2MGmg9fO-sR1t3A=s96-c)

Grounding snippets are the short, extractive sentences AI systems pull from your page to build their answers: the atomic unit of AI-search visibility, where most of your page never makes the cut.

![](/media/images/misc/arrow-marker-left.svg)

When an AI system answers a question with current information, it does not recall the web from memory. It runs a search, pulls in pages, reads short extracts from them, and writes its answer from those extracts. Those extracts are grounding snippets , and they are the atomic unit of visibility in AI search. You can rank first in traditional search and still be invisible here, because the model, not the user, is now the reader, and a selective one.


## The grounding funnel

Every platform runs the same basic pipeline , tuned differently: search query → pages received → pages with readable content → pages cited . Received is every URL the search step returned; readable is the subset the model actually obtained text for; cited is the few whose sources appear in the answer. The gap between received and cited is where each system shows its character.


## What a grounding snippet is

A grounding snippet is built by extractive summarization, not abstractive: the system pulls exact sentences from your page rather than paraphrasing. The unit of extraction is the individual sentence, scored against the query, and the top sentences are stitched together. Where the chosen sentences are not next to each other on the page, they are joined by an ellipsis, producing the familiar segment … segment … segment shape. This is not unique to Google: testing Claude shows it returns the same ellipsis-joined, sentence-stitched format, so the pattern appears to be a shared convention across assistants.


## How Google builds them

The pipeline runs prompt → query fanout → retrieval → extractive summarization → context assembly → synthesis and attribution. The observed traits of Google's extraction:

- Query-focused. Sentences close to the query are preferred; off-topic sections are skipped, and the same page yields different extracts for different fanout queries.

- Lead bias. Opening paragraphs are extracted almost wholesale, regardless of content.

- Structural noise. Tables of contents, headers, and stray markers get scored as if they were sentences.

- Confidence scores. Each chunk carries a relevance score from 0.1 to 1.0.

We replicate this behaviour closely by fine-tuning the open cross-encoder model microsoft/deberta-v3-large.


## Query fanout

Before retrieval, the model breaks one prompt into several single-intent sub-queries, a separation of concerns where a multi-faceted question is split into individual dimensions of intent. Each sub-query retrieves its own set of sources, typically five to twenty . Because of fanout, a page can be grounded for one angle of a question and absent for another.


## Only about a third survives

Most of your page never reaches the model. Across one sample analysis the system cited about 32% of the available characters, with per-source coverage ranging from roughly 21% to 65%. What gets kept is core service information, process steps, pricing and examples; what gets dropped is navigation, boilerplate, time-sensitive promotions, off-topic sections, and verbatim customer quotes.


## A fixed budget, shared by rank

Grounding behaves like a fixed pie, not an expanding one. From an analysis of 7,060 queries, 2,275 pages and 883,262 snippets :

- Each query has a budget of roughly 2,000 words (median 1,929; p95 2,798), with the average chunk about 15.5 words.

- Rank sets your share. The top source takes about 531 words (28%); the fifth about 266 words (13%). The first source gets roughly double the grounding of the fifth.

- Coverage falls as pages get longer. Under 1,000 words, about 61% of the page is covered; at 3,000+ words, about 13%. Selection plateaus around 540 words, or about 3,500 characters.

The lesson is blunt: density beats length . More content dilutes your coverage without increasing what gets selected; you are competing for share of a fixed pie.


## Grounding is transient

The snippets do not stick around. AI search is single-turn transient : the raw extracts are injected into the context for one turn, then purged the moment the answer is finished, to save token space. Ask a follow-up and the model is working from its own earlier summary, not the original page. What persists of you is whatever was captured in that first snippet, filtered through the model's reading of it, not the broader page.


## Every platform decides differently

The same query, asked the same day, produced very different evidence on each platform:

- Google (Gemini) is economical, with a near one-to-one funnel: it tends to cite what it received and does not expose pages it did not use. Internally it indexes results as query.result pairs , around ten results per query, holding an ordered cache rather than loose text.

- OpenAI (GPT) casts the widest net and cites the least, a roughly twenty-to-one drop we call a visibility trap. It sees the web as a small structured card per result (title, URL, a one-to-three sentence snippet, an ID) and “scrolls” by opening fixed windows of text, never the full page.

- Anthropic (Claude) grounds in two passes, is the most token-hungry, and keeps some unselected pages visible so you can see what it considered.


## A caveat on the evidence

The snippets a model exposes are not always reliable, even about themselves. In one case Gemini recited a grounding citation for a paper that does not exist , hallucinating while reporting its own grounding context. And the quantitative work above comes from our own measurements: we did not control for confounders such as authority and freshness, and we keep the raw data private for client confidentiality. Treat the numbers as strong directional signal rather than settled fact.


## What it means for your content

- Write dense, self-contained sentences that stand on their own when extracted.

- Front-load the key information, since opening text is favoured.

- Cover the fanout angles a question splits into, not just the headline query.

- Strip structural noise so menus and boilerplate do not compete with your substance.

- Think in modular blocks , since the unit that wins is the sentence, not the page.

You can see this for yourself: our free grounding snippet tool at snippets.dejan.ai runs a live grounded search and shows which URLs Gemini pulls and the exact sentences it extracts, the practical groundwork behind Selection Rate Optimization .


## Related concepts

- Grounding

- Grounding Snippet

- Query Fanout

- Selection Rate

- Selection Rate Optimization

- Primary Bias

- AI Visibility


## Evidence and sources

- How AI search grounding works (the grounding funnel)

- What extraction method Google uses for grounding snippets

- How much of your content survives the AI search filter

- How big are Google’s grounding chunks

- Search grounding is transient

- How GPT sees the web

- How Google grounds Gemini

- Grounding snippet extraction tool

- SRO and grounding snippets