---
name: seo-wiki
description: Answer SEO, AEO, GEO and AI-search questions from LaunchDarkly's SEO/AEO research wiki, a curated, cited knowledge base of studies, best practices, checklists and playbooks. Covers AI Overviews and AI Mode, ChatGPT/Perplexity/Claude/Gemini citation behavior, llms.txt, robots.txt and AI crawlers, schema and entity SEO, E-E-A-T, technical SEO audits, keyword research, topic clusters, link building, content pruning, meta tags, glossary pages, SaaS SEO, AI visibility measurement and coding-agent tool selection. Use it whenever someone asks what works in SEO or AI search, what the research says, how to approach a tactic, for a checklist or playbook, or for evidence behind an SEO/AEO claim, even if they never mention the wiki. Not for reviewing a draft (seo-review, content-review), writing title tags (seo-meta-tags) or writing a content brief (content-brief), though it can supply evidence for those.
---

# SEO/AEO Research Wiki

This skill holds a read-only snapshot of LaunchDarkly's SEO/AEO research
wiki. Every page was written from real sources (studies, reports, official
Google docs, practitioner articles) and cites them, so answers from here
carry evidence instead of general SEO folklore. That's the whole point: when
someone asks "does X work?", the useful answer is what the evidence says,
how strong it is, and where it disagrees.

Most people asking are not SEO specialists: writers, PMs, marketers who
want to know what to do. So the default answer is short and plain, and the
full evidence breakdown is there on request (see "Pick the depth" below).
Do the careful reading either way; the depth setting changes only how much
of it goes into the reply.

{{BUILD_INFO}}

## What's in `references/`

- `index/concepts.md`, `index/playbooks.md`, `index/sources.md`: the catalog.
  One line per page, a `[[slug]]` link plus a summary. Start here.
- `page-map.md`: one line per page, `slug | file | title`. Use it to turn a
  `[[slug]]` into a readable title and see which file holds it.
- `../scripts/page.sh`: prints any page by slug, wherever it lives:
  `bash scripts/page.sh llms-txt` (run from the skill folder).
- `concepts/`: synthesis pages on a topic (what it is, current best
  understanding, evidence, and a **Conflicting Evidence** section where
  sources disagree).
- `playbooks/`: actionable checklists, steps and tactics.
- `sources/`: one page per study or article, bundled by first letter
  (`sources/a.md`, `sources/b.md`, ...) to keep the skill under claude.ai's
  file limit. Each page starts with a `<!-- page: slug -->` line. The
  `**Citation:**` line near the top of a page has the author, title, date
  and original URL (when known).
- `timeline.md`: dated real-world events (algorithm updates, launches,
  study publications), newest at the bottom.

## How to answer a question

1. **Find the pages.** Search the index for the question's key terms rather
   than reading it whole, because the sources index alone is long:
   `grep -i -n "term" references/index/*.md`. Try a couple of synonyms
   (e.g. "AI Overviews" / "AIO", "GEO" / "AEO" / "AI search"). For a broad
   question, read `index/concepts.md` and `index/playbooks.md` in full; they
   are short.
2. **Open the pages.** Print each `[[slug]]` with
   `bash scripts/page.sh slug`; look up its title with
   `grep '^slug |' references/page-map.md`. Concept and playbook pages are
   the main material; open a source page when you need a specific number,
   method or citation. Often one or two pages are enough.
3. **Read long pages by section.** Some pages run past 400 lines. List the
   headings first (`bash scripts/page.sh slug | grep -n '^#'`), then read
   the sections that match the question, plus any Conflicting Evidence or
   checklist section.
4. **Weigh it before you write.** Note how strong the support is (study
   size, vendor data vs. independent, official Google statement vs.
   practitioner opinion), whether a Conflicting Evidence section touches
   the question, and whether the evidence is about a different engine or
   context than the one asked about (Google data for a ChatGPT question,
   say). Both answer depths depend on this; they differ only in how much
   of it they show.
5. **Pick the depth and write the answer** (next section).

## Pick the depth

**Deep** when any of these hold:
- the arguments start with `deep` (e.g. `/seo-wiki deep does llms.txt work?`);
- the person asks for the evidence, the studies, the research, sources,
  methodology, "the full breakdown", or how strong a claim is;
- your own instructions or preferences say to always answer this skill in
  deep mode.

**Short** otherwise. That's the default.

### Short answer (default)

Write for a smart reader who doesn't work in SEO. Aim for about 150 words;
go a little over only when the question really needs it.

1. **The answer**, in 2–4 plain sentences. No unexplained jargon: say "the
   AI summary at the top of Google results" the first time rather than
   just "AIO", and skip acronyms the reader doesn't need.
2. **What to do**, as 2–4 bullets, if the question has a practical side.
3. **How sure we are**, in a few words: "well supported", "mixed
   evidence", "mostly practitioner opinion", "only one vendor study". If
   sources disagree, or the evidence is about a different engine than the
   one asked about, one sentence says so. Don't dress an open question up
   as settled just because the answer is short.
4. **Sources**: 1–3 links, the wiki page titles or original URLs the
   reader is most likely to want. No study-by-study rundown.
5. **One closing line** offering more: "Want the full evidence breakdown?"

Leave out study sizes, methods, vendor-vs-independent notes and page
dates unless one of them changes the answer (for example, a finding that
is old enough to be superseded).

### Deep answer

For SEO practitioners and anyone who wants to check the reasoning.

- Lead with the direct answer, then the support. Name the studies behind
  key claims and how strong they are (study size, vendor data vs.
  independent, official Google statement vs. practitioner opinion).
- If the evidence is about a different engine or context than the one
  asked about, say so rather than letting it stand in silently.
- If a page has a Conflicting Evidence section that touches the question,
  lay out the disagreement and give the current best guess the page
  records.
- List the wiki pages you used by title (from `page-map.md`) and give the
  original source URL from the Citation line for claims the reader may
  want to check or quote. Pages carry an `updated:` date and sources a
  `date_published:`; mention dates when recency matters (AI search changes
  fast, and older findings may be superseded).

### Checklists and how-tos

For "give me a checklist / how do I do X" requests, start from the
matching playbook and adapt it to the reader's situation rather than
pasting it. In short mode, give the 5–7 steps that matter most and offer
the full playbook; in deep mode, give the adapted playbook in full.

## When the wiki doesn't cover it

An index grep with a few synonyms plus one full-text search
(`grep -rn -i "term" references`) is enough to decide. A hit inside a
`sources/` bundle belongs to the nearest `<!-- page: slug -->` line above it. If neither turns up
the topic, say plainly that the wiki doesn't cover it, then answer from
general knowledge and label that part as not from the wiki, so the reader
knows which parts are backed by the research. If the wiki has something
closely related, mention it briefly at the end. The same short/deep
choice applies to that answer.

## Things to keep in mind

- This is a snapshot. The build date above is when it was last refreshed;
  for very recent events, check `timeline.md` and say if something may have
  changed since.
- Mention pages to the reader by title, not the raw `[[slug]]` syntax.
- If two pages (or two parts of one page) disagree on a detail, go with the
  one the underlying source supports, or note the inconsistency briefly.
- The wiki is read-only here. Its maintainer adds and updates sources; if
  someone wants a new study added, suggest they send it to the wiki owner.
