---
type: playbook
tags: [seo, aeo]
updated: 2026-08-06
---

# Accessibility-Tree Audit for AI Agents

**Why/when to use this:** AI browsing and computer-use agents (ChatGPT
Atlas, and anything built on Microsoft's Playwright MCP) perceive and
operate web pages through the **accessibility tree** — the semantic layer
of ARIA roles, accessible names, and states that browsers build from the
DOM — **not** the visual rendering. If an element isn't in the tree with a
correct role and name, an agent effectively can't see or use it. This
playbook audits and fixes that layer. It's the concrete, agent-perception
counterpart to the Action Layer (layer 4) of
[[optimizing-for-the-agentic-web]], and layer 1's JS-rendering concerns
overlap [[technical-seo-audit-checklist]].

Grounded in [[sel-accessibility-tree-seo-use-cases-2026]] (John McAlpin /
Search Engine Land), with the mechanism confirmed first-party by
[[openai-publishers-developers-faq]] ("ChatGPT Atlas uses ARIA tags … to
interpret page structure and interactive elements") and embodied in
tooling by [[microsoft-playwright-mcp]] ("Uses Playwright's accessibility
tree, not pixel-based input. No vision models needed").

## Principle: native HTML first, ARIA only as a fallback

> "Fix with native HTML first — a real `<button>`, a real `<label>` — and
> reach for ARIA only when native elements can't do the job."

Sloppy ARIA is **worse than none**: it misleads both screen-reader users
and agents. A stale `aria-expanded="false"` left on a panel that visibly
opens "is worse than no attribute at all." The accessibility tree exists
for assistive-technology users first — over **8,600 accessibility lawsuits
were filed in 2025** — and the same correct markup that serves them is
what makes a page legible to agents. Treat agent legibility as a *benefit*
of doing accessibility properly, never as a reason to bolt on fake ARIA.

## The 10 use cases

### 1. Agent-readiness audit on money pages
Extract your top 10–20 revenue pages and verify every important user action
appears in the tree with the correct role and accessible name. Pass/fail:
- Primary CTA is a `<button>`/`<a>` with a clear accessible name.
- All form inputs are labeled.
- `navigation` and `main` landmarks are present.
- Key content actually appears in the tree.

### 2. Diagnose JavaScript-rendering gaps
"Content that never reaches the tree without client-side JavaScript is
invisible to any agent." Check the tree with JS disabled / via a
non-rendering fetch; SSR or pre-render anything critical. Ties to the
JS-rendering AI-crawler risk in [[technical-seo-audit-checklist]] and
[[vercel-rise-of-the-ai-crawler]] (only some AI crawlers execute JS).

### 3. Audit conversion paths for WebMCP
Walk signup/checkout flows and confirm each step's controls are
tree-legible and operable, in preparation for agents transacting via
WebMCP (W3C draft; Chrome origin trial) — see the protocol layer in
[[agentic-web-optimization]].

### 4. Benchmark competitor machine legibility
Capture competitors' accessibility trees on equivalent pages and compare
cleanliness (named controls, landmark structure, content-in-tree). A
machine-legibility analogue of a classic competitive audit.

### 5. Validate heading/landmark hierarchy
Agents use heading hierarchy for content segmentation and extraction.
Ensure a logical `h1→h2→h3` order and correct landmarks; don't use
`aria-level` overrides that scramble the hierarchy.

### 6. Fix anchor text via accessible names
The agent reads a link's *accessible name*, not its visual styling. Avoid
ARIA labels that override good visible anchor text; make link names
descriptive and action-clear (cf. [[link-and-anchor-text-best-practices]]).

### 7. Audit images and alt text
Use empty `alt=""` on decorative images to remove tree noise; for
meaningful images write alt text that includes spatial context. Maximizes
AI extraction/citation potential (cf. [[image-seo-checklist]]).

### 8. ARIA snapshots in CI
Catch regressions before deploy with Playwright's `toMatchAriaSnapshot`:
```js
for (const t of templates) {
  test(`accessibility tree: ${t.name}`, async ({ page }) => {
    await page.goto(t.url);
    await expect(page.locator('body')).toMatchAriaSnapshot({
      name: `${t.name}.aria.yml`,
    });
  });
}
```

### 9. Before/after tree diffs for migrations
On redesigns/replatforms, diff the accessibility tree pre- and post-change
to QA that agent-legible structure survived — the machine-legibility
counterpart to a normal migration QA pass.

### 10. Prioritize fixes by SEO/revenue value
Rank tree fixes by the revenue/SEO value of the pages they affect, not by
raw defect count — allocate effort where agent legibility matters most.

## Tools

- **AXray Extractor** — free; captures the accessibility tree of any live
  URL, with JSON export.
- **Chrome DevTools** — full-page accessibility tree view in the Elements
  panel.
- **Playwright** — `await page.ariaSnapshot()` returns a YAML tree;
  `toMatchAriaSnapshot` powers CI regression tests (use case 8).

## See also

- [[agentic-web-optimization]] — the five-layer concept; this playbook is
  the perception/operability detail beneath layers 2 and 4.
- [[optimizing-for-the-agentic-web]] — the broader agentic-web tactics;
  its "agent-responsive design"/ARIA bullet points here for the deep dive.
- [[technical-seo-audit-checklist]] — layer-1 JS-rendering and agent-
  readiness overlap (use case 2).
- [[sel-ai-optimization-content-for-search-and-agents]] — the earlier
  "agent-responsive design"/ARIA guidance this extends.
- [[sel-accessibility-tree-seo-use-cases-2026]] /
  [[openai-publishers-developers-faq]] / [[microsoft-playwright-mcp]] —
  the three sources behind this playbook.
