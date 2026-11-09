# Research scout ledger

Every candidate the research-scout skill has considered, one line each.
Append-only; written by the skill. Used to skip repeats and to count gate
passes and failures for the seed-list rules.

Format: `YYYY-MM-DD | verdict | publisher-key | title | url | reason`

- Date is the run date.
- Verdict is `pass:<1-5>` (rigor score), `reject:g<1-4>` (first failed
  gate criterion, see `.claude/skills/research-scout/rubric.md`), or
  `unverified` (couldn't be read).
- Fields are separated by ` | `, so titles and reasons must not contain
  that sequence.

