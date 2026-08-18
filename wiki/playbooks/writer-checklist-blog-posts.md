---
type: playbook
tags: [seo, aeo]
updated: 2026-07-24
---

# Writer's SEO Checklist: Blog Posts

**Who this is for:** Anyone writing a LaunchDarkly blog post.

**The one idea behind all of this:** People and AI tools (Google AI
Overviews, ChatGPT, Claude, etc.) increasingly answer questions *for* the
reader instead of sending them to us. To get found and quoted in these
systems, write a clear, direct answer to a real question, back it with
proof, and make it easy to lift out.

## Before you write

- **Pick one real question the post answers.** Write it as the question a
  reader would type or ask out loud (e.g. "How do feature flags reduce
  deployment risk?"). *Why: Search and AI both match content to questions.
  A post about "everything on flags" gets beaten by a focused post that
  nails one question.*
- **Check we don't already have a post on it.** Search our blog. If we do,
  update that post instead of writing a competing one. *Why: Two posts on
  the same topic split traffic and rank worse than one strong page.*
- **Know your one new thing.** Ask: "Could a competitor rewrite this
  tomorrow from memory?" If yes, add a stat, an example, a benchmark, or a
  first-hand lesson until the answer is no. *Why: AI tools favor the page
  that adds something new, not the tenth rewrite of the same advice.*

## Writing the post

- **Answer the question in the first paragraph** (2–4 sentences), then
  explain. Don't bury the answer under a long intro. *Why: 44% of AI
  citations come from the first 30% of a page. If the answer isn't near
  the top, it may never be seen.*
- **Write headings as questions or plain statements** a reader would
  actually search (e.g. "What is a feature flag?" not "Diving In"). *Why:
  AI tools match your headings against the reader's question and clever
  headings hide the match.*
- **Back claims with specifics: numbers, dates, named examples.** Prefer
  "cut rollback time by 40%" over "dramatically faster." *Why: Concrete
  statistics are one of the strongest levers for getting quoted by AI and
  they build reader trust.*
- **Cite credible sources** for facts and stats, and link to them. *Why:
  Sourced claims get cited more, especially for content that isn't already
  well-known. Unsupported claims get skipped.*
- **Stay focused; don't pad.** Aim roughly 500–2,000 words. Cover the
  question well, then stop. *Why: Exhaustive, everything-and-the-kitchen-
  sink posts actually get quoted less than tight, focused ones.*
- **Keep it readable.** Short paragraphs, one idea each. Plain language
  over jargon. *Why: Easy-to-follow writing is both easier for readers and
  measurably more likely to be cited.*
- **Add a short FAQ** (2–4 common follow-up questions with direct answers)
  at the end where it fits. *Why: FAQ sections map cleanly to how people
  ask AI tools follow-ups, and are among the most-cited formats. (Ask the
  web team to add FAQ schema, a behind-the-scenes tag that boosts this
  further.)*

## Credibility and links

- **Publish under a named author with a real bio,** not "LaunchDarkly
  Team." *Why: Content from a named, credentialed person gets cited far
  more than faceless brand posts (~92% vs. ~8% in one study).*
- **Link to 2–3 related LaunchDarkly pages** using descriptive link text
  (e.g. "feature flag best practices," not "click here"). *Why: Internal
  links help readers and both search and AI understand how our content
  connects. The link text tells them what the page is about.*

## Before you hit publish

- **Write the page title and meta description.** These are the text people
  see in Google, and often an AI tool's first impression of the page. Keep
  them simple:
  - *Title:* Lead with the topic, use Title Case, keep it under ~65
    characters, and end with " | LaunchDarkly".
  - *Description:* One or two sentences under 155 characters. Start with
    the main topic and end by telling the reader what they'll get.
  - *(A house format exists, so check the seo-meta-tags guidelines or ask
    SEO if you're unsure. Longer walkthrough: [[writing-meta-tags]].)*
- **Set the URL once and don't change it later.** Keep it short, readable,
  and clearly describing the contents of the page
  (/blog/feature-flag-best-practices). *Why: Changing a URL after publish
  drops accumulated search and citation value; broken links take citations
  offline.*
- **Plan to revisit in ~90 days.** Update stats, dates, and examples so the
  post stays current. *Why: Stale content quietly loses ground to fresher
  pages over time.*

## Don't bother

- **Don't stuff keywords.** Repeating a phrase unnaturally does nothing for
  AI visibility and can make results *worse*. Write for the reader.

## Where these rules come from

This is the plain-language, writer-facing distillation of
[[geo-content-optimization-tactics]] — go there (or to the sources below)
for the evidence, caveats, and the tactics that didn't make this list.

- **Answer-first / 44%-of-citations-from-the-first-30%** —
  [[growth-memo-why-proprietary-data-is-your-most-defensible-asset]]
- **Named author over brand account (~92% vs. ~8%)** —
  [[otterly-linkedin-ai-citations-study-2026]]
- **500–2,000 words, original, educational, consistent cadence** —
  [[semrush-linkedin-ai-visibility-study-2026]]
- **Focus beats comprehensive coverage; retrieval rank dominates** —
  [[airops-fan-out-effect-2026]]
- **Your "one new thing" (information gain)** —
  [[growth-memo-why-most-original-data-never-gets-cited]]
- **FAQ sections / FAQ schema citation lift** —
  [[otterly-how-to-optimize-content-for-ai-search-2026]]
- **Question-form headings, answer-shape alignment** —
  [[ai-search-reranking-pipeline]]
- **Set the URL once; don't change it later** —
  [[url-structure-best-practices]]
- **Keyword stuffing doesn't work (term saturation)** —
  [[lexical-ranking-tf-idf-bm25]]
- **One post per question (avoid cannibalization)** —
  [[keyword-mapping-and-cannibalization]]

## See Also

- [[writing-meta-tags]] — the companion writer-facing guide to titles and
  meta descriptions
- [[geo-content-optimization-tactics]] — the full, evidence-cited tactic
  list this checklist simplifies
