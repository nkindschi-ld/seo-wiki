# SEO/AEO LLM Wiki

A persistent, AI-maintained knowledge base of SEO and AEO (Answer Engine Optimization) best practices, tactics, strategies, studies, and reports.

Instead of re-deriving answers from raw sources on every question, this wiki incrementally builds and maintains interlinked markdown pages that compound in value over time. It's designed to be viewed in [Obsidian](https://obsidian.md/) (free, local, no account required) and maintained by Claude via natural-language workflows.

## Quick Start

### Viewing the Wiki

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nealkindschi/seo-wiki.git
   cd seo-wiki
   ```

2. **Open in Obsidian:**
   - Download [Obsidian](https://obsidian.md/) (free)
   - Open the `wiki/` folder as a vault
   - You can now browse pages with full link resolution, graph view, and backlink panels

3. **Start reading:**
   - Begin with [`wiki/index.md`](wiki/index.md) for a catalog of all pages
   - Check [`wiki/log.md`](wiki/log.md) for recent additions
   - View [`wiki/timeline.md`](wiki/timeline.md) for SEO/AEO events by date

## Repository Structure

```
├── raw/                          # Immutable source material (do not edit)
│   ├── articles/                 # Articles and blog posts
│   ├── studies/                  # Research studies
│   ├── reports/                  # Industry reports
│   └── assets/                   # Downloaded images/charts referenced by sources
│
├── wiki/                         # AI-maintained knowledge base (Obsidian vault)
│   ├── index.md                  # Catalog of all pages (one-line summary each)
│   ├── log.md                    # Activity log (ingests, queries, lints)
│   ├── timeline.md               # Real-world SEO/AEO events by date
│   ├── concepts/                 # Topic synthesis pages
│   ├── playbooks/                # Actionable checklists & tactics
│   └── sources/                  # One page per ingested source
│
├── docs/
│   └── superpowers/specs/        # Design rationale & architecture
│
└── CLAUDE.md                     # AI operating instructions (schema, workflows)
```

## Page Types

### Concepts
Synthesis pages that explain SEO/AEO topics in depth. Include:
- Overview and current best understanding
- Links to relevant playbooks and sources
- A "Conflicting Evidence" section when sources disagree (with dates and reasoning)

**Frontmatter:**
```yaml
---
type: concept
tags: [seo, aeo]  # or just [seo] or [aeo]
updated: YYYY-MM-DD
---
```

### Playbooks
Actionable reference pages — checklists, numbered steps, tactic writeups. Include:
- Why/when to use this
- Step-by-step guidance
- Links back to supporting concepts

**Frontmatter:**
```yaml
---
type: playbook
tags: [seo]
updated: YYYY-MM-DD
---
```

### Sources
Summary pages for each ingested source (article, study, report). Include:
- Citation and link to original
- Key takeaways
- Which concepts/playbooks it updated

**Frontmatter:**
```yaml
---
type: source
tags: [aeo]
date_published: YYYY-MM-DD
date_ingested: YYYY-MM-DD
origin: raw/studies/<file>
---
```

## How It Works

### Adding Sources (Ingest)
The wiki is maintained by Claude. To add a new source:

1. **Provide the source** to Claude in any form:
   - A URL
   - A file path (e.g., `~/Downloads/report.pdf`)
   - Pasted text
   - An attached file

2. Claude will:
   - Save the source to `raw/` (you don't manually place files there)
   - Discuss key takeaways with you
   - Check for conflicts with existing pages
   - Create or update relevant concept/playbook/source pages
   - Update the index, log, and timeline

### Querying the Wiki
Ask Claude a question about SEO/AEO. Claude will:
- Find relevant pages in `wiki/index.md`
- Read supporting concept/playbook/source pages
- Answer with citations
- Optionally file the answer back into the wiki if it's a valuable synthesis

### Linking Convention
All pages use **Obsidian-style wikilinks**, never relative paths:

```markdown
[[internal-linking-best-practices]]
```

This allows Obsidian to:
- Resolve links automatically
- Power the graph view (visualize topic connections)
- Show backlink panels (what links to this page)
- Keep links valid even if pages move between folders

## Conflict Resolution

When sources disagree, the wiki **surfaces the conflict** rather than silently overwriting:

```markdown
## Conflicting Evidence

- **Claim**: <statement>
  - Supported by: [[source-x]] (date)
  - Contradicted by: [[source-y]] (date), <reason>
- **Current best guess**: <leaning>, flagged as unresolved
```

Old claims are marked with dates and reasoning, never deleted — SEO/AEO practices shift over time and it's valuable to know *when* something was true.

## Activity Tracking

### Log (`wiki/log.md`)
Append-only record of wiki activity, dated by when work was done:
```
## [2026-07-07] ingest | Title of Source
## [2026-07-07] query | "Question asked"
## [2026-07-07] conflict | Topic — brief description
## [2026-07-07] lint | findings summary
```

### Timeline (`wiki/timeline.md`)
Append-only record of real-world SEO/AEO events, dated by source publish/event date:
```
## 2026-07-07 — Event description
[[source-slug]] · [[concept-that-updated]]
```

## Viewing in Obsidian

The `wiki/` folder is a complete Obsidian vault. When you open it:

- **Graph view**: See how concepts, playbooks, and sources connect
- **Backlinks panel**: Find all pages linking to the current page
- **Wikilink resolution**: Click `[[links]]` to navigate instantly
- **Search**: Full-text search across all pages
- **Optional plugins**: Install [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) to query frontmatter metadata (not required)

## Sharing the wiki as a skill

Teammates without GitHub use the wiki through the `seo-wiki` skill on
claude.ai, which works in claude.ai chat, Claude Desktop and Claude Code.
The skill holds a snapshot of the wiki pages, so refresh it after you
update the wiki.

The snapshot includes concept, playbook and source pages, the index and
the timeline (source pages bundled by first letter to stay under
claude.ai's 200-file limit). It leaves out `raw/`, `drafts/`, `research-digests/`,
`wiki/log.md` and `CLAUDE.md`. The skill's instructions live in
`share/seo-wiki/SKILL.md`.

By default the skill gives a short, plain-language answer for readers who
don't work in SEO. For the full evidence breakdown (studies, strength of
evidence, conflicting findings), start the request with `deep`
(`/seo-wiki deep does llms.txt work?`) or ask for the evidence. To get deep
answers every time, add a line to your own instructions: "When I use the
seo-wiki skill, always answer in deep mode." In Claude Code that goes in
`~/.claude/CLAUDE.md`; in claude.ai and Claude Desktop, in
Settings → Profile preferences.

**First time:**

1. Build the zip: `./scripts/build-shared-skill.sh` (writes `dist/seo-wiki.zip`).
2. On claude.ai, upload `dist/seo-wiki.zip` in your Skills settings.
3. Share the skill with teammates or a group. They add it once.

**After each wiki update:**

1. Run `./scripts/build-shared-skill.sh` again.
2. Upload the new zip as an update to the existing `seo-wiki` skill.
   People you've shared it with get the new version the next time they
   use it.

The build date and wiki commit are stamped into the skill, so Claude can
tell readers how current the snapshot is. `dist/` is ignored by git.

## Tags

Pages are tagged `[seo]`, `[aeo]`, or `[seo, aeo]` to indicate scope:
- **SEO**: Search Engine Optimization (classic Google Search)
- **AEO**: Answer Engine Optimization (AI/generative search visibility)
- **Both**: Topics that apply to both ranking systems

## Future Extensions (Out of Scope)

These are not yet implemented:
- **Live SEO tool integration** — pulling live data from Semrush/Ahrefs during queries to check claim staleness
- **Search tooling** — `index.md` is sufficient for current scale; may add if wiki grows past ~100 sources
- **Dataview plugin** — not required; optional for advanced querying
- **Auto-ingestion** — natural-language ingestion (handing sources directly to Claude) was chosen over folder-watching

## Contributing

This is an AI-maintained wiki, but improvements are welcome:

- **Found an error?** Open an issue or PR
- **Have a source to add?** Open an issue with the link/file
- **See a conflict that needs resolving?** Open an issue describing the disagreement

## License

This repository contains synthesized knowledge from multiple published sources (articles, studies, reports). Each source page links back to the original. See individual source pages for licensing of the original material.

## Related

- Full design rationale: [`docs/superpowers/specs/2026-07-07-seo-aeo-llm-wiki-design.md`](docs/superpowers/specs/2026-07-07-seo-aeo-llm-wiki-design.md)
- Operating instructions for Claude: [`CLAUDE.md`](CLAUDE.md)
- Activity log: [`wiki/log.md`](wiki/log.md)
- Real-world timeline: [`wiki/timeline.md`](wiki/timeline.md)
