---
type: playbook
tags: [seo, aeo]
updated: 2026-10-08
---

# Editorial Link Integration

Why/when to use this: apply whenever a link or brand mention is being
*placed* rather than earned — guest posts, sponsored/outreach articles,
digital PR copy, partner content — and when reviewing placed content
before it ships. Acquiring the placement is covered by
[[link-building-outreach-tactics]]; this page covers making the link
read as editorial once you have it. Based on
[[dejan-link-building-outreach-ai-search]] (practitioner framework; see
the caveats on that page). Belongs to [[link-building]].

## The core test

> "Who wanted the link/mention on this page?"

Show the finished piece to another SEO who doesn't know which link you
placed. If they can guess it, integration isn't good enough — and the
premise is that Google's spam team, its algorithms, and LLMs can guess
it too. Don't self-certify: the effort you just put in biases you toward
"good enough."

## Step zero: content first, links second

"Links should be there in support of content, not the other way
around." As soon as the link becomes the primary goal, the content
becomes secondary — even a seasoned writer paid to include a link will
usually integrate it worse than their normal links. If there's nothing
worth linking to, no integration technique fixes that (consistent with
[[link-building]]'s "something of value to build links to").

1. Start from the content and what's genuinely useful to the reader.
2. Consider everything of value on the topic and where it lives.
3. Write, and link out generously to the best pages on all relevant
   domains, in tune with reader expectations.

## Avoid the "1 + 2 rule"

Many publishers require one commercial link plus 1–3 "authority" links
to news/government sites "to look natural." This works against itself:
it makes the post less natural, aids algorithmic detection, gives
manual reviewers a pattern, degrades UX, and encourages poor
integration. Per the source, organic content often carries 10–20 links
per page while blog-network posts carry 2–3.

## Rule 1 — Liberal linking

Link to every page that helps the reader, on every relevant domain,
including domains you have no stake in.

| Signal | Question to ask |
|---|---|
| Coverage | Does the page link to the sources, terms and entities a reader may want to follow? |
| Openness | Does it link to other domains as readily as to its own? |
| Consistency | Does its link density match the host site's editorial posts? |
| Independence | Would the links still be there if no link had been paid for? |
| Blend | Does any single link stand out from the rest? |

## Rule 2 — Purpose

Every link needs a clear job. Ten purposes: **attribution** (credit a
quote/image/idea), **reference** (source of a fact or figure),
**definition** (explain a term), **expansion** (more depth),
**identification** (which person/company/product/place is meant),
**example**, **action** (buy, sign up, download), **relationship**
(connect to a related person/org/story), **proof** (evidence for a
claim), and **promotion**. A commercial link is fine when it passes the
same test as every other link on the page.

## Rule 3 — Primacy

The link must go to the strongest possible page for that spot. If a
better page exists for the anchor, the link is in the wrong place
(e.g. a homepage where a specific case-study page exists).

| Test | Question to ask |
|---|---|
| Logic | Is this the page the anchor text promises? |
| Situation | Does it suit what the reader needs at this point? |
| Narrative | Does it continue the story the article tells? |
| Utility | Is it the most useful page on the subject? |
| Relevance | Does it match the sentence the link sits in? |

## Rule 4 — Natural anchor text

Match the host site's existing anchor-text patterns. Consistent with
[[link-and-anchor-text-best-practices]]'s advice to use branded/generic
anchors when you write the anchor yourself.

| Signal | Question to ask |
|---|---|
| Pattern fit | Does the anchor match how the host site phrases its own links? |
| Plain wording | Does it describe the source or the action, with no target keyword? |
| Grammar | Does it read as a natural part of the sentence? |
| Rarity | Is the exact phrase uncommon, like most anchors in the long tail? |
| Click point | Does it sit on the words a reader would expect to click? |

## Placement: link at the peaks of "link desire"

A reader's desire for a link rises and falls through the text. It peaks
where the text names a source, makes a claim, or mentions something the
reader may want to look up. Natural links sit at those peaks; how many
peaks get linked depends on the site's threshold (essentials-only →
conservative → liberal). Red flags:

- A sentence that exists only to carry the link — one such line is
  enough to expose it.
- A client link in a passage that gives the reader no reason to want a
  link there ("links as an afterthought").
- The link sits off-peak while the actual peak (the case-study subject,
  the result) goes unlinked.

## Worked example: how a flagged link trips the signals

DEJAN's detector flagged an agency's case-study link (the agency
disputed it as natural — a published false positive, useful precisely
because it shows what *looks* inorganic):

- **Blend** — the only outbound editorial link on a page otherwise
  linking internally.
- **Openness/Independence** — no other third party linked, so the link
  looks like it exists because of an arrangement.
- **Placement** — reader desire peaks at the client (Hunter Talent) and
  results, which got no link; the provider link sits off-peak.
- **Primacy** — a specific case-study page would beat a homepage.

## Optional: adversarial review

DEJAN's own workflow pairs a "red team" AI that researches, writes and
places the link with a "blue team" paid-link detector; any article the
detector cracks is discarded. The tooling is proprietary, but the human
version is the core test above: blind-review by someone trying to find
the paid link.

## Checklist

- [ ] The piece is worth reading without the link.
- [ ] Link density matches the host site's normal editorial posts (no
      1 + 2 pattern).
- [ ] Multiple third-party domains are linked, not just the placed one.
- [ ] Every link has one of the ten purposes.
- [ ] Each link goes to the strongest page for its spot.
- [ ] Anchor text matches the host's style, plain wording, no target
      keyword.
- [ ] The placed link sits at a natural link-desire peak; no sentence
      exists only to carry it.
- [ ] A blind reviewer cannot pick out the placed link.
- [ ] Paid placements carry `rel="sponsored"` per
      [[link-and-anchor-text-best-practices]].

## See also

- [[link-building]] — concept, including the Conflicting Evidence on
  authority metrics and outreach-link value this source raises.
- [[link-building-outreach-tactics]] — getting the placement.
- [[digital-pr-strategy]] — earning coverage where links arise
  editorially.
- [[parametric-memory-vs-grounding]] — why the same integration logic
  applies to brand mentions aimed at AI answers.
