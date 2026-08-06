---
type: concept
tags: [aeo, seo]
updated: 2026-08-06
---

<!-- updated 2026-08-06: added MCP server discoverability section from mcp-focus-server-retrieval-2026 -->


# Docs Over MCP (Documentation as an Agent-Callable Tool)

Serving documentation to AI agents over the **Model Context Protocol**
rather than as HTML pages an agent has to find, fetch, render, and infer
from. The mental shift: docs stop being *a page an agent reads* and
become *a tool an agent calls* — the agent queries a structured endpoint
and gets back exactly the slice it asked for. You are now designing an
**interface**, not a page.

This is the docs-specific application of the protocol layer in
[[agentic-web-optimization]] (layer 5), and a concrete tactic within
[[optimizing-for-coding-agent-recommendations]]. Two distinct use cases
share the pattern:

- **Public / product docs** — a vendor exposes an MCP server so any
  developer whose coding agent has it installed pulls live, correct API
  docs (attacks the hallucinated/outdated-code failure mode).
- **Internal / private docs** — an org fronts its own component
  libraries so coding assistants generate code aligned to in-house
  patterns without leaking IP. This is the focus of
  [[aluri-mcp-documentation-retrieval-2025]].

## Why judge it differently from citation-focused GEO

[[generative-engine-optimization]] optimizes to be *quoted* in a
generated answer. Docs-over-MCP optimizes to be *retrieved and acted
on*: the endpoint is working code, not a citation. Evaluate the
"agentic experience" on four axes:

1. **Retrieval** — can the agent get the *right chunk* for its task, not
   the whole doc set? (tool descriptions, search granularity, chunking)
2. **Actionability** — does a returned chunk let the agent do the next
   thing (working code, exact param names, versioned signatures)?
3. **Trust / freshness** — is it live from source-of-truth, vs. a stale
   crawl or the model's training cutoff?
4. **Cost** — tokens/round-trips per typical task.

## What's good about the format

- **You control the payload** — clean structured content, no render
  ambiguity, no nav chrome, no pricing-locked-in-an-image problem. The
  highest tier of "agent readiness."
- **Freshness & authority** — agent pulls live from your source of
  truth; the single biggest win against a fast-moving API.
- **Task-scoped retrieval** — return the one relevant method, not 40
  pages → fewer tokens, less context pollution → likelier-correct code →
  your product becomes the default pick.
- **Tool descriptions are an optimization surface** — they are how the
  agent decides *when* to call you.

## What's bad / the risks

- **Opt-in and narrow reach.** Only helps users whose agent has your
  server installed — a subset, unlike open crawlable docs. A
  **complement to, not a replacement for**, well-structured public docs
  (which AI Overviews and untooled agents still crawl).
- **Bad chunking is worse than a good page.** Huge blobs or wrong-
  section retrieval burns the token budget and still leaves the agent
  inferring. Retrieval quality is now *your* engineering problem.
- **Discoverability / tool-selection competition.** The agent must
  choose your tool over generic web search or a competitor's server;
  vague or overlapping tool descriptions get skipped. This is now a
  measured IR problem — see "MCP server discoverability" below.
- **Maintenance surface.** It's software — versioning, auth, uptime,
  rate limits. A broken server mid-task fails harder than a stale page.
- **Measurement is hard.** No pageview model; you need server-side
  logging of tool calls to see what agents actually ask for.

## Design patterns (for building one)

Drawn from [[aluri-mcp-documentation-retrieval-2025]] (architecture
sound; its outcome claims are unmeasured — see that page's caveat):

- **Code-aware chunking** that preserves code-block integrity and keeps
  examples attached to their explanations (generic splitters break
  this).
- **Hard vs. soft metadata filters** with adaptive relaxation so a
  query never dead-ends in an empty result set.
- **Per-collection similarity thresholds** — tight for API refs, looser
  for examples/patterns.
- **Context-window transformation/ranking** — condense to
  implementation-critical detail before feeding the model, don't dump
  raw docs.
- **Selective disclosure + access logging** for private docs, so
  proprietary content augments an external model without leaking IP.

## MCP server discoverability (retrievability)

A distinct layer from within-server doc quality: before an agent can
call your server, a router/registry has to **retrieve it out of
thousands of candidates** for the user's query. This is its own
information-retrieval problem, and [[mcp-focus-server-retrieval-2026]]
(SIGIR '26) measures it:

- **Raw self-reported docs retrieve poorly.** A server's README and its
  tool `name`/`description`/`input schema` are shallow, inconsistent,
  and often disconnected from what the tool actually does — weak
  retrieval signals (in the paper's audit, tool *output* info is missing
  or poor for ~85% of popular servers).
- **Implementation-grounded docs retrieve better.** Documentation
  generated from *what the code actually does* (MCP-Focus: Tool
  Extractor → Tool Document Refiner via white-box code tracing → Server
  Document Refiner) beat raw-README baselines across **all 6 retrievers
  and all metrics** on a 3,763-server benchmark — e.g. BM25 recall@10
  jumped from ~0.48 to ~0.73, and gains *widened* for multi-tool queries.
  It also beat a generic repo-doc generator (RepoAgent) using the same
  LLM, so the win is retrieval-oriented design, not model size.
- **Implication:** tool descriptions and server overviews are a
  **retrieval-optimization surface** — the MCP-era analogue of on-page
  SEO for being *found* among many servers. This is upstream of, and
  distinct from, the chunking/actionability that governs the answer
  *once you're selected*. Write docs that reflect real tool behavior,
  not a hand-written blurb.

This upgrades the "tool descriptions are an optimization surface" point
above from asserted (via the low-rigor
[[aluri-mcp-documentation-retrieval-2025]]) to empirically supported.

## One-line takeaway

Docs-over-MCP is the strongest available agent-ready format *when the
agent has your server* — you trade broad passive reachability for
precise, fresh, controllable, low-token retrieval. Judge it by whether
an agent can pull the *right chunk* and *act on it immediately*, and
treat it as an addition on top of clean public docs, not a substitute.

## See also

- [[agentic-web-optimization]] — MCP as the protocol layer; this is the
  docs-specific application.
- [[optimizing-for-coding-agent-recommendations]] — a docs-MCP server
  as a vendor tactic to become the agent's default pick.
- [[ai-coding-agent-tool-selection]] — the broader "be the agent's pick"
  domain.
- [[aluri-mcp-documentation-retrieval-2025]] — architecture source
  (internal-docs focus; rigor caveat applies).
- [[mcp-focus-server-retrieval-2026]] — SIGIR '26 source for the MCP
  server discoverability / retrievability section.
