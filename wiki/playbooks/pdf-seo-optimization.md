---
type: playbook
tags: [seo]
updated: 2026-09-04
---

# PDF SEO Optimization

Why / when to use this: use when a PDF (whitepaper, lead magnet,
downloadable guide) needs to be discoverable in Google, not just
functional. PDFs are a weaker ranking vehicle than HTML — "a Web
document is more likely to rank higher than a PDF in 9 out of 10 cases"
([[digitalchakra-optimise-pdf-files-for-seo]]) — so treat this as
damage control / incremental visibility for a distribution asset, not a
primary-ranking strategy. If a lead magnet is being delivered as a PDF,
see [[lead-magnet-checklist]] for the opt-in/conversion side.

## Checklist

1. **Unique content.** Don't duplicate an existing web page inside the
   PDF — Google flags matching PDF+HTML content as duplicate content
   and the HTML version typically wins the ranking. Make the PDF's
   content genuinely distinct.
2. **Title & description metadata.** SEO-style title (50-60 characters,
   keyword at the start) and a description under 160 characters.
   Include the target keyword in the filename, the PDF's Subject/Title
   metadata field, and the URL.
3. **Filename.** Keyword-rich, concise, hyphen-separated, no
   punctuation or stop words (e.g. `seo-detailed-guide.pdf`).
4. **URL.** Keywords separated by dashes in the PDF's URL path
   (straightforward on self-hosted/WordPress setups; limited on hosted
   platforms like Wix/Shopify).
5. **Anchor text linking to the PDF.** Links from your own site pages
   to the PDF are a real SEO signal — use descriptive anchor text, not
   "click here."
6. **Internal linking from the PDF.** Link out from the PDF back to
   relevant site pages to pass authority signal and route readers
   onward. Note: nofollow cannot be applied to links inside a PDF.
7. **Real header tags, not bold text.** Use actual h1/h2/h3 structure
   (most PDF authoring tools support this in export/tagging), not
   visually-bolded pseudo-headers. Work keywords into headers
   naturally.
8. **Alt text on images** — descriptive, ≤100 characters. Note: images
   inside PDFs currently are not indexed by Google regardless of alt
   text; alt text here is for accessibility more than search.
9. **Compress file size** for faster loading — Adobe Acrobat's "Reduce
   File Size," or a tool like ilovepdf.com.
10. **Standard fonts only** (Times, Helvetica, Courier, Symbol, Zapf
    Dingbats) to avoid file bloat from embedded custom fonts.
11. **Mobile-readable formatting** — left-align text, bullet points,
    heading hierarchy, short paragraphs.

## Technical constraints to know

- Google indexes searchable (text-layer) PDFs the same way as HTML
  pages, but recrawls/refreshes them less frequently.
- Password-protected, encrypted, or non-static-HTML PDFs are **not**
  indexed at all.
- To deliberately keep a PDF out of the index, apply an
  `X-Robots-Tag: noindex` HTTP header, or use Search Console's URL
  removal tool — see [[robots-txt-strategy]] for why robots.txt itself
  is the wrong tool for this (it blocks crawling, not indexing).
- Standard Google Analytics does not track PDF downloads — instrument
  via Google Tag Manager, header code, or a plugin.
- Compression and alt-text overlap with [[image-seo-checklist]]; the
  noindex mechanics overlap with [[technical-seo-audit-checklist]] —
  this page covers the PDF-specific application of both.

## Sources
[[digitalchakra-optimise-pdf-files-for-seo]] — single-source playbook,
no conflicting claims found elsewhere in the wiki.
