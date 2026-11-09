---
name: research-scout
description: Weekly research digest for the SEO Wiki. Finds recent, credible studies on SEO, AEO/GEO, AI search, AI Overviews, LLM retrieval/RAG, AI citation behavior, coding-agent tool selection and agentic-web optimization; vets each one's methodology against a hard gate and rigor score; and writes a ranked digest with links to research-digests/. Use when asked to "run research-scout", "run the weekly research digest", "find new SEO/AEO studies", or by the weekly scheduled task. Optional argument window=<days> (default 14). Never edits wiki/ or raw/.
---

# Research scout

Find recent credible studies, vet their methodology, and write a digest the
user reviews before choosing what to ingest. Design:
`docs/superpowers/specs/2026-11-09-research-scout-design.md`.

## Hard rules

- **Never edit `wiki/` or `raw/`.** The user ingests from the digest using
  the Ingest workflow in `CLAUDE.md`.
- **No state-changing git commands**: no commit, switch, checkout, stash,
  reset, restore or push. Read-only git (`status`, `log`, `diff`) is fine.
- Write only: `research-digests/<run-id>.md`, `research-digests/seen.md`
  (append only), `.claude/skills/research-scout/seed-sources.md` (the
  Discovered and Caution sections only), and files under
  `research-digests/.work/`.
- **Never edit the Curated section** of `seed-sources.md`.

Paths below are relative to the repo root (`~/Claude Code/SEO Wiki`). Let
`S=.claude/skills/research-scout`.

## Steps

### 0. Set up

- `run_date` = today (YYYY-MM-DD). `window` = the `window=<days>` argument,
  or 14. `window_start` = `run_date` minus `window` days.
- Run id: `run_date`, or `run_date-2`, `run_date-3`… if
  `research-digests/<id>.md` already exists. Let `WORK=research-digests/.work/<run-id>`.
- Snapshot the repo state before writing anything:
  `python3 $S/scripts/check_run.py --snapshot --repo . --work $WORK`
  (expect `OK snapshot`).

### 1. Load context

Read `$S/rubric.md`, `$S/lanes.md`, `$S/seed-sources.md` and
`wiki/index.md`. Build the lane skip list:
- every URL in `research-digests/seen.md`, and
- titles of wiki sources published in the window (replace `<window_start>`):

  ```bash
  python3 -c 'import glob,re,sys
  for f in sorted(glob.glob("wiki/sources/*.md")):
      t=open(f).read(); d=re.search(r"^date_published:\s*(\S+)",t,re.M); h=re.search(r"^# (.+)$",t,re.M)
      if d and h and d.group(1)>=sys.argv[1]: print(h.group(1))' <window_start>
  ```

### 2. Fan out (three lanes in parallel)

Start three general-purpose subagents **in a single message** so they run
in parallel: `academic`, `industry` and `practitioner`. Each prompt
contains, pasted in full:
- the "Topic scope" and "Instructions for every lane" sections plus that
  lane's own section from `lanes.md`,
- all of `rubric.md`,
- that lane's Curated and Discovered seed entries, plus every Caution
  entry labeled "CAUTION",
- the window (`window_start` to `run_date`) and the skip list,
- "Return only one fenced JSON array of at most 8 records."

Save each reply's JSON array to `$WORK/lane-<lane>.json`. If a lane errors,
times out or returns invalid JSON, write `[]`, note `<lane>: failed
(<reason>)` for the digest's Lanes line, and continue with the others.

### 3. Dedupe

Concatenate the three arrays into `$WORK/candidates.json`, then run:

`python3 $S/scripts/dedupe.py --repo . --candidates $WORK/candidates.json --out $WORK/deduped.json`

- `duplicate_of` starting `seen:`: drop silently (already in the ledger).
- `duplicate_of` starting `wiki:`: verdict `reject:g4`, reason "already in
  wiki as <slug>".
- The same study from two lanes: merge into one record, keeping the more
  complete fields.

### 4. Judge

For each remaining record:
1. `lane_verdict: "unverified"`: keep as `unverified` with the lane's
   reason. Don't apply the gate.
2. Otherwise re-apply the `rubric.md` gate yourself; the lane's verdict is
   advice. Check `date_published` is within the window (otherwise
   `reject:g4`). Where the author or organization is unfamiliar, run a
   quick search to confirm a track record (criterion g3).
3. For each pass, give a rigor score (1–5) from the rubric table and keep
   or rewrite the conflict-of-interest note.
4. For each pass, write a **Wiki fit** line from `wiki/index.md`: name the
   most relevant `[[concept-or-playbook]]` and say "agrees with", "extends"
   or "possible conflict with … on <claim>".

### 5. Append to the ledger

Append one line per judged record (pass, reject or unverified, including
the wiki duplicates from step 3) to `research-digests/seen.md`:

`<run_date> | <verdict> | <publisher_key> | <title> | <url> | <reason>`

Verdict is `pass:<score>`, `reject:g<N>` or `unverified`. Replace any
` | ` inside a title or reason with ` / `.

### 6. Apply the seed rules

`python3 $S/scripts/seed_rules.py --seen research-digests/seen.md --seed $S/seed-sources.md`

From the JSON it prints:
- `promote`: append to `## Discovered`:
  `- key: <key> | name: <publisher_name> | lane: <lane of the evidence record, or the best fit> | added: <run_date> | evidence: <evidence_url>`
- `caution`: append to `## Caution`:
  `- key: <key> | name: <name> | added: <run_date> | reason: <reason>`;
  if the key is in Discovered, remove that Discovered line.
- `flag_curated`: **don't edit anything**; list it in the digest for the user.

### 7. Write the digest

Write `research-digests/<run-id>.md` in exactly this shape:

```markdown
# Research digest — <run_date>

**Window:** <window_start> to <run_date> · **Passed:** <n> · **Rejected:** <n> · **Couldn't verify:** <n>
**Lanes:** academic ✓ · industry ✓ · practitioner ✓

## Studies

### 1. <Title> — <Organization> (<Author>), <date_published>
**Link:** <url> · **Type:** <study_type> · **Rigor:** <score>/5
**Method:** <data source, sample size, period, approach>
**Key findings:** • <finding> • <finding> • <finding>
**Conflicts of interest:** <note>
**Wiki fit:** <line from step 4>

## Couldn't verify
- <Title> — <url> — <reason>

## Rejected
- <Title> — <url> — g<N>: <reason>

## Seed list changes
- Added to Discovered: <name> (<lane>) — <reason>, <evidence_url>
- Moved to Caution: <name> — <reason>
- Curated source to review: <name> — <reason>
```

- Mark a failed lane in the Lanes line as `practitioner ✗ (<reason>)`.
- Rank Studies by rigor score, then by how much the study would add to the
  wiki (new topic or open conflict before agreeing evidence).
- Counts: Passed = Studies entries; Rejected = Rejected bullets (including
  wiki duplicates); Couldn't verify = Couldn't-verify bullets. They must
  equal this run's ledger lines.
- Empty sections: Studies holds `_No studies passed the gate this run._`;
  any other empty section holds `_None._`. A quiet week still gets a
  digest.

### 8. Validate

`python3 $S/scripts/check_run.py --repo . --digest research-digests/<run-id>.md --run-date <run_date> --work $WORK`

It must print `OK`. If it lists errors, fix the digest, the ledger lines
from this run, or the seed list, then rerun. If it still fails after two
fix attempts, add this block directly under the digest's H1:

```markdown
> **Validation errors:** <one per line from check_run.py>
```

### 9. Report

Finish by stating the digest path and its summary line. Remind the user
that nothing was committed.
