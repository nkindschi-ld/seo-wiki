<!--
Archival capture 2026-11-04 of RESULTS.md and README.md from
https://github.com/mintlify/url-discovery-bench (MIT), commit 5f055a89336cb94050e36eaa479374b390e92462.
Verbatim. RESULTS.md first, then README.md.
-->

# Results

Two agents, Claude Code on claude-sonnet-5 and Codex CLI on
gpt-5.5, each answered the same 100 questions across 20 Mintlify sites, under all
four serving formats, three times over: **2,400 attempts, n=300 per cell.** Everything ran
through a local proxy in `record` mode, so the numbers reflect the live sites while every
response was frozen to `snapshots/` for replay.

Full run: July 2026, on `claude-sonnet-5` and `gpt-5.5` as of then. CLI versions:
Claude Code 2.1.202 (recorded in each transcript's `init` event). The Codex CLI version
was not captured for this run — a gap; the harness now records both CLIs' versions into
every results row. Models and upstream content both drift, so the committed
`data/full/results.jsonl`, not a live re-run, is what regenerates every table below. Three
further models (Opus 4.8, Fable 5, GPT-5.6) were run for replication; see
[Replication across five models](#replication-across-five-models).

Any table below regenerates with `python -m url_discovery_bench.report data/full`.

## 404s per task

| arm | Claude | Codex |
| --- | --- | --- |
| html | 1.1 | 3.3 |
| md | 0.8 | 2.0 |
| md-link | 0.1 | 0.2 |
| md-inline | 0.0 | 0.2 |

Adding the `llms.txt` index, linked or inline, wipes out ~91% (Claude) / ~94% (Codex) of
the 404s an HTML-only site throws. One caveat before quoting that: most of these 404s are
agents probing for `.md`/`llms.txt`, not getting lost. The next section breaks it down.

## Full table

n=300 each. Brackets = 95% CI, bootstrapped over attempts, so for defensible significance
use the site-clustered tests below, not these.

| agent / arm | accuracy % | 404s/task | fetches | input tok (k) | sec |
| --- | --- | --- | --- | --- | --- |
| claude / html | 96.0 | 1.1 [1, 1.3] | 6.7 | 296 | 44 |
| claude / md | 94.3 | 0.8 [0.5, 1.1] | 7.0 | 215 | 31 |
| claude / md-link | 97.3 | 0.1 [0, 0.2] | 4.1 | 175 | 25 |
| claude / md-inline | 99.0 | 0.0 [0, 0] | 4.6 | 226 | 31 |
| codex / html | 97.7 | 3.3 [2.7, 4.6] | 26.5 | 285 | 67 |
| codex / md | 96.0 | 2.0 [1.5, 3.1] | 24.9 | 156 | 57 |
| codex / md-link | 97.7 | 0.2 [0.1, 0.2] | 13.2 | 115 | 45 |
| codex / md-inline | 99.3 | 0.2 [0.1, 0.2] | 10.8 | 127 | 41 |

Token and turn columns aren't comparable *across* agents; the two use different accounting
(Claude folds cache-read/creation into input tokens and reports `num_turns`; Codex sums raw
input tokens across turns and counts command + message items).

## Attempts and exclusions

`data/full/results.jsonl` contains 2,672 rows: the 2,400 valid attempts behind every table
above, plus 272 failed attempts that the retry loop reran until each cell reached n=300.
The failures: 256 Codex CLI crashes (`no agent_message event` — the CLI died before
producing a reply, a harness failure rather than a task failure) spread almost evenly
across Codex's four arms (66/64/64/62), 7 timeouts, 6 Claude CLI network errors, and 3
Claude attempts hard-failed by the contamination gate. Because the Codex crashes land
near-uniformly on every arm, excluding them doesn't bias any within-agent comparison. All
272 rows remain in the file for inspection.

Separately, 13 fetches (across 7 otherwise-valid attempts: 1 claude/html, 6 codex/html,
4 codex/md, 2 codex/md-link) invoked curl with a shell variable in place of a literal URL,
so the audit could not statically confirm the host. They are surfaced in the report's
`unaudited` column rather than silently passed. Manual inspection of all seven transcripts
confirms each such command builds its URLs from the proxy's own sitemap or `llms.txt`
(loops over matches anchored to `http://127.0.0.1:<port>/...`), so all 13 resolve to the
proxy.

## What the 404s actually are

The raw 404 count is real, but it's content-negotiation
friction, not agents getting lost. Left to their own devices, the agents kept reaching for
machine-readable formats, tacking `.md` onto URLs and asking for `/llms.txt`, and the HTML
arm has nothing to hand back.

Classifying by suffix alone would flatter this story (a `.md` request on a nonexistent
path is a wrong guess in disguise), so every 404'd path is instead checked against the
site's real page inventory (llms.txt + sitemap) by `analysis/breakdown_404.py`. The
verified composition, both agents combined:

| arm | `.md` of a page that exists | `/llms.txt` request | wrong page (incl. `.md` on nonexistent paths) |
| --- | --- | --- | --- |
| html | 59% | 34% | 7% |
| md | — (`.md` resolves) | 43% | 57% |

Two findings. On HTML, 96% of the `.md` probes named pages that exist: the agent was
already on the right page and asking for a better format. And on markdown without an
index, the single biggest failure mode is still the missing `/llms.txt` (43% of dead
ends), with the rest being genuinely wrong guesses.

Counting only verified wrong guesses (existence-checked, not suffix-stripped), the
navigation-only picture per task:

| arm | Claude | Codex |
| --- | --- | --- |
| html | 0.12 | 0.20 |
| md | 0.46 | 1.15 |
| md-link | 0.10 | 0.15 |
| md-inline | 0.02 | 0.16 |

So two things. Agents rarely struggle to *find* the right page on HTML, as the dead-ends
are failed format requests, not bad guesses. And markdown without an index makes agents
guess *more* wrong URLs than HTML (they learn the site speaks markdown and start
constructing `.md` paths), so adding the index pays off even on the clean metric —
md → md-link cuts verified wrong guesses roughly 4–8×. "It's the index, not the markdown"
holds up.

Regenerate with `python analysis/breakdown_404.py data/full dataset/full.json --per-agent
--inventory data/full/page-inventory.json`. Both inputs ship in the repo: the run's proxy
logs are committed under `data/full/logs/`, and `data/full/page-inventory.json` freezes
the July 2026 page inventories so the classification is reproducible after sites drift.

## Takeaways

- The real win is content negotiation, not discovery. Agents natively expect `.md` and
  `llms.txt`; an HTML-only site 404s ~90% of those requests, and serving them (as `md-link`
  does) makes the waste disappear.
- Accuracy hardly moves (94–99%) across all four arms and both agents, as they reach the right
  page regardless. The cost lands on wasted requests and tokens, not wrong answers.
- `md-link` is the sweet spot: the same 404 reduction as inlining the whole index, at a fraction of the token cost for a user.
- Codex is far more fetch-hungry than Claude, but the shape of the result is identical.

## Limitations

- **curl-only fetching.** Every fetch goes through `curl`, so each request is one observable,
  countable hit through the proxy. That makes the absolute 404 counts method-dependent (a
  fetch tool that converts HTML to markdown client-side would show a smaller absolute gap),
  but the relative index win (`html → md-link`) and its direction hold, and curl-only if
  anything understates HTML's disadvantage rather than inflating it.
- **Exact-path grading.** Answers are graded by exact normalized path against `expected`.
  Questions with more than one valid answer page must list every acceptable path, or a
  correct answer is scored wrong. Since accuracy sits at 94–99% across arms, any such
  undercount is small and applies equally to every arm.
- **Command-line contamination audit.** The audit recognizes fetches by binary name
  (`curl`, `wget`, …) in transcript commands. A fetch made through a language runtime
  (e.g. `python -c`) would not be attributed, and a curl whose URL comes from a shell
  variable is counted as `unaudited` rather than resolved (13 such fetches in this run,
  all manually verified on-proxy — see "Attempts and exclusions"). Claude cannot make
  unattributed fetches (tool-restricted to `curl`); for Codex, whose sandbox needs
  network access to reach the proxy, the gate is best-effort. The core 404/fetch metrics
  are unaffected either way: they are counted from the proxy's own logs, which record
  only traffic that actually reached the proxy.

## Significance (site-clustered, n=20 paired)

- **The index wins on every site: 20/20, both agents.** Not an average hiding exceptions.
- **The p-values bottom out** at 1.9e-6 (Wilcoxon), the lowest possible at n=20, which only happens when all 20 sites move the same way.
- **Even the strict test holds:** adding just the llms.txt link to already-markdown pages is significant for both agents.
- **Fetches drop significantly too,** on every comparison (Wilcoxon 3.8e-6 → 3.2e-3).

| agent | contrast | Δ/task | sites improved | Wilcoxon p | paired-t p |
| --- | --- | --- | --- | --- | --- |
| claude | html → md-link | −1.02 | 20/20 | 1.9e-6 | 9.8e-12 |
| claude | md → md-link (index only) | −0.69 | 18/20 | 1.1e-4 | 0.011 |
| codex | html → md-link | −3.18 | 20/20 | 1.9e-6 | 2.5e-5 |
| codex | md → md-link (index only) | −1.90 | 20/20 | 1.9e-6 | 2.3e-4 |

*Method: each site collapsed to one number per format, then paired across the 20 sites; Wilcoxon signed-rank primary (counts aren't normal), paired t as backstop (borderline on Codex fetches, where outliers inflate variance).*

## Replication across five models

The core run above is two models in `record` mode. To check the result isn't a quirk of
one model family, three more were run over the same 20 sites × 5 questions × 4 arms × 3
attempts (n=300/cell): **Claude Opus 4.8, Claude Fable 5, and GPT-5.6** (`gpt-5.6-sol`).
These ran in `replay` mode against the frozen July 2026 snapshots, so `404-adj` below
subtracts `snapshotMisses`, the replay-only artifact where an agent reaches a path the
crawl never captured and gets a synthetic 404, leaving genuine navigation/negotiation
404s only. The artifact is small (0.1–0.6/task) and lands on every arm, so it doesn't
change the direction of any comparison.

`404-adj` = adjusted 404s per task; `tok` = mean input tokens (k). Regenerate with
`python analysis/multimodel.py` (reads the committed `data/full` + `data/multimodel`).
Like `data/full/results.jsonl`, `data/multimodel/results.jsonl` keeps genuine failures for
inspection (GPT-5.6 logged 155 `no_agent_message` CLI crashes and Opus one timeout, all
excluded from the tables above); rate-limit retries from the constrained replay run are an
execution artifact, not a benchmark failure, and are not committed.

| model | arm | acc % | 404-adj | tok (k) |
| --- | --- | --- | --- | --- |
| Opus 4.8 | html | 98.3 | 2.11 | 207 |
| Opus 4.8 | md-link | 98.3 | 0.08 | 149 |
| Opus 4.8 | md-inline | 98.3 | 0.06 | 154 |
| Fable 5 | html | 99.7 | 1.13 | 188 |
| Fable 5 | md-link | 99.3 | 0.00 | 140 |
| Fable 5 | md-inline | 100.0 | 0.00 | 201 |
| GPT-5.6 | html | 94.0 | 6.79 | 220 |
| GPT-5.6 | md-link | 96.7 | 0.02 | 96 |
| GPT-5.6 | md-inline | 98.3 | 0.00 | 96 |

Same shape as the core two, on every model:

- **`html → md-link` drops 404s to near-zero** (2.11→0.08, 1.13→0.00, 6.79→0.02) and cuts
  input tokens 26–56% (Opus −28%, Fable −26%, GPT-5.6 −56%), with no accuracy cost
  (accuracy barely moves). The model that over-explores raw HTML most (GPT-5.6, 6.79
  404s/task) gains the most.
- **`md-inline` is never worth it.** It matches `md-link`'s accuracy and 404s but costs the
  same or more tokens every time (Fable 201k vs 140k, Opus 154k vs 149k), so inlining the
  full index into every page is pure overhead once the link exists.

The site-clustered test holds for the three new models exactly as it does for the core
two, on raw 404s/task (unadjusted, same as the core significance table), paired across the
20 sites. The `snapshotMisses` artifact is too small to flip any result: Opus `html →
md-link` is significant on 19/20 sites, every other contrast on 20/20:

| model | contrast | Δ/task | sites improved | Wilcoxon p |
| --- | --- | --- | --- | --- |
| Opus 4.8 | html → md-link | −2.27 | 19/20 | 3.8e-6 |
| Opus 4.8 | md → md-link (index only) | −3.85 | 20/20 | 1.9e-6 |
| Fable 5 | html → md-link | −1.20 | 20/20 | 1.9e-6 |
| Fable 5 | md → md-link (index only) | −1.33 | 20/20 | 1.9e-6 |
| GPT-5.6 | html → md-link | −6.78 | 20/20 | 1.9e-6 |
| GPT-5.6 | md → md-link (index only) | −1.71 | 20/20 | 1.9e-6 |

Regenerate with `python analysis/stats.py data/full/results.jsonl data/multimodel/results.jsonl
--by-model`.

Across all five models and 20 sites, `md-link` is the efficiency winner.


---

# README.md

# Docs URL Discovery Bench

Benchmarks coding agents on **URL discovery**: given a question, how efficiently does an
agent find the right page on a docs site? It compares four serving formats to measure
whether content negotiation (markdown for agents) and `llms.txt` reduce wasted fetches and
404s.

## Finding

Across 20 Mintlify docs sites and two agents (Claude Code on Sonnet 5, Codex on GPT-5.5),
serving an `llms.txt` index eliminates ~90%+ of 404s versus raw HTML. The main finding is that it's the index, not the markdown, that does it. It replicates on three further models (Opus 4.8, Fable 5, and GPT-5.6), same direction on 19–20 of 20 sites per model. Full numbers and significance are in [`RESULTS.md`](RESULTS.md).

## Arms

| Arm         | Serving behavior                                                |
| ----------- | --------------------------------------------------------------- |
| `html`      | HTML                                                            |
| `md`        | Markdown                                                        |
| `md-link`   | Markdown with the llms.txt pointer                              |
| `md-inline` | Markdown with the full llms.txt content inlined into every page |

All arms serve identical content through a local proxy that rewrites the upstream origin to
itself, so every agent fetch is observable and 404s are counted from proxy logs.

## Metrics

Per arm × agent: **404s per task**, fetches-to-success, tokens, wall time, and, when the
dataset provides expected answers, URL accuracy.

## Setup

```bash
git clone https://github.com/mintlify/url-discovery-bench
cd url-discovery-bench
pip install -r requirements.txt   # requests, numpy, scipy
```

Requires **Python 3.9+**. That's everything Tier 0 needs, but Tiers 1 and 2 additionally need
the [`claude`](https://docs.claude.com/en/docs/claude-code) (Claude Code) and/or
[`codex`](https://github.com/openai/codex) (OpenAI Codex CLI) installed and authenticated.
macOS/Linux only.

## Reproduce

### Tier 0: verify the findings (no API keys, instant)

The raw results of the full run ship in the repo, so every table and p-value is
regenerable without re-running anything.

```bash
python analysis/stats.py data/full/results.jsonl   # aggregate table + site-clustered significance
python -m url_discovery_bench.report data/full      # same aggregate table
python analysis/breakdown_404.py data/full dataset/full.json --per-agent \
  --inventory data/full/page-inventory.json          # 404 composition (proxy logs + frozen inventory, both committed)
python analysis/multimodel.py                       # per-model table across all five models
python analysis/stats.py data/full/results.jsonl data/multimodel/results.jsonl --by-model  # per-model significance
```

### Tier 1: run it on your own docs (live, minutes)

Point the benchmark at any docs site and watch the 404/fetch/token difference across
formats. No ground truth required. `expected` answers are optional; omit them and you get
the efficiency metrics (accuracy shows `n/a`), or add them to also grade correctness.

```bash
cp dataset/example.json dataset/mysite.json
# edit mysite.json: set target, basePath, rewriteOrigins, and a few questions
python -m url_discovery_bench.probe https://docs.mysite.com https://mysite.com/docs   # confirm it's a Mintlify site
python -m url_discovery_bench.run --dataset dataset/mysite.json --agents claude --snapshot-mode record --job mysite
python -m url_discovery_bench.report jobs/mysite
```

`--snapshot-mode record` measures against the live site while freezing every response to
`snapshots/` so the run can later be replayed deterministically (`--snapshot-mode replay`).

### Tier 2: the full study (hours, ~$100, both CLIs)

20 sites × 5 questions × 4 arms × 2 agents × 3 attempts = 2,400 attempts, and re-crawls
~3 GB of snapshots. Exits non-zero while attempts remain, so wrap it in a retry loop:

```bash
until python -m url_discovery_bench.run --dataset dataset/full.json --attempts 3 --job full \
  --agents claude,codex --concurrency 8 --snapshot-mode record; do sleep 120; done
```

## Contamination gate

Every attempt's transcript is audited for commands containing URLs whose host is not the
proxy (`url_discovery_bench/audit.py`). Any hit hard-fails the attempt: it is recorded as an
`error: "contaminated"` row with the offending URLs, excluded from the report, and retried
on resume. Claude is additionally tool-restricted to `Bash(curl:*)` with WebFetch/WebSearch
disallowed and MCP servers disabled; Codex has no per-tool allowlist (its sandbox needs
network to reach the proxy), so the audit gate is the enforcement there. Commands whose URL
can't be statically resolved (e.g. `curl "$u"` in a loop) are counted in the report's
`unaudited` column rather than silently passed; the audit's scope and limits are spelled
out in [`RESULTS.md`](RESULTS.md#limitations).

## Snapshots

`python -m url_discovery_bench.snapshot_crawl --dataset dataset/<file>.json` crawls every page each site
declares (llms.txt + sitemap, both variants) into `snapshots/`. Three proxy modes:

- `live` (default): fetch upstream every request.
- `record`: fetch upstream and persist each response, used for report-quality runs, so
  published numbers reflect real sites while still producing a frozen artifact.
- `replay`: serve purely from disk; no upstream traffic. Deterministic reproduction mode.
  Unknown paths return 404 and are flagged `snapshotMiss` in proxy logs and a
  `snapshotMisses` count per attempt.

Snapshots (~3 GB) and transcripts are gitignored; re-crawl with `python -m url_discovery_bench.snapshot_crawl`.

## Layout

```
url_discovery_bench/proxy.py          # serving proxy: 4 modes, origin rewrite, snapshot record/replay, JSONL log
url_discovery_bench/runners.py        # headless claude (curl-only) + codex exec runners
url_discovery_bench/audit.py          # contamination audit: external-host fetch detection
url_discovery_bench/grade.py          # URL normalization + answer grading (expected optional)
url_discovery_bench/run.py            # orchestrator: task x arm x agent x attempt, one proxy per attempt
url_discovery_bench/report.py         # per-arm aggregate table
url_discovery_bench/snapshot.py       # snapshot read/write + live fetch
url_discovery_bench/snapshot_crawl.py # crawl a site's pages into snapshots/
url_discovery_bench/probe.py          # check whether a site negotiates markdown + serves llms.txt
analysis/stats.py     # aggregate + site-clustered paired significance (Wilcoxon + paired t); --by-model to group by model
analysis/multimodel.py # per-model per-arm table across the core + replication runs
analysis/breakdown_404.py # classify each 404 against the site's real page list (reads <job>/logs)
dataset/              # sites + question -> expected-path ground truth; example.json is a template
data/full/            # committed core-run artifacts (sonnet-5 + gpt-5.5, record mode): results.jsonl, proxy logs, frozen page inventory
data/multimodel/      # committed replication results (results.jsonl): opus-4.8, fable-5, gpt-5.6, replay mode
jobs/                 # run outputs (gitignored): results.jsonl, proxy logs, transcripts
```

## Notes

- Web search and non-curl tools are disabled; the prompt confines the agent to the proxy
  origin and transcripts are audited for external fetches. Answers pointing at any host
  other than the attempt's proxy origin grade incorrect (`offProxy`); a memorized
  production URL never counts as discovery.
- The proxy origin (`127.0.0.1:<port>`) prevents reuse of memorized URLs, but questions
  should still avoid leaking the page slug, and a dataset should span many sites.
- Upstream content can change between runs; run all arms of a comparison in the same
  session, or use `record`/`replay` to freeze content before a report-quality run.
- All fetches go through `curl`, so every request is one observable, countable hit through
  the proxy. That makes the _absolute_ 404 counts method-dependent (a fetch tool that
  converts HTML to markdown client-side would show a smaller absolute gap), but the
  _relative_ index win (`html → md-link`) and its direction are unaffected, and curl-only if
  anything understates HTML's disadvantage rather than inflating it.
- Grading is exact normalized-path match against `expected`. If a question has more than one
  valid answer page, list every acceptable path in `expected` or correct answers score wrong.

## License

MIT, see [`LICENSE`](LICENSE).
