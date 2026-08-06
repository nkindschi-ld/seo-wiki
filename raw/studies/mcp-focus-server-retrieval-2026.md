# MCP-Focus: Leveraging Function-Oriented Document Enhancement for MCP Server Retrieval

> **Intake note (updated 2026-08-06):** The full PDF is now saved
> alongside this file as `mcp-focus-server-retrieval-2026.pdf` (provided
> by the user after the ACM Digital Library returned HTTP 403 to
> WebFetch). All details below have been **verified against the actual
> paper**, and the exact result figures have been filled in.

## Citation

- **Title:** MCP-Focus: Leveraging Function-Oriented Document
  Enhancement for MCP Server Retrieval
- **Authors:** Wenchun Jing, Haiyang Shen, Haoran Wang, Qi Liu,
  Ningyuan Li, Chaoran Luo, Ning Zhang, Yun Ma
- **Venue:** Proceedings of the 49th International ACM SIGIR Conference
  on Research and Development in Information Retrieval (SIGIR '26),
  Melbourne, Australia, July 20–24, 2026
- **DOI:** 10.1145/3805712.3809582
- **Code & data:** https://github.com/JingWC/MCP-Focus

## Problem

As LLM agents connect to a growing ecosystem of MCP servers, an agent
(or a router/registry) must **retrieve the right MCP server/tool** for a
given user query out of thousands of candidates. Raw MCP server
documentation — READMEs and the tool `name`/`description`/`input schema`
that servers self-report — are weak retrieval signals: shallow,
inconsistent, and often disconnected from what the tool actually does.
This degrades retrieval of the correct server.

## Method — MCP-Focus (function-oriented document enhancement)

A data-centric approach that improves retrieval by **enhancing the
documents, not the retriever** (explicitly orthogonal to retriever-side
optimization). A multi-stage, LLM-driven agentic pipeline (backbone:
Qwen3-235B-A22B) does **white-box code analysis** of an MCP server repo,
bottom-up:

1. **Tool Extractor** — navigates the full repo (tools are spread across
   files/modules) to find valid MCP tool entry points and extract
   interface metadata (parameter/return schemas), mapping each tool to
   its code location.
2. **Tool Document Refiner** — locates each tool's implementation and
   applies **Contrastive Contextual Refinement**: (a) *Intrinsic Code
   Tracing* — "jump-to-definition" + control-flow trace to ground input/
   return descriptions in real behavior (e.g. a generic `query: string`
   → "SQL statement to execute against the PostgreSQL backend"); (b)
   *Extrinsic Contrastive Differentiation* — compares against sibling
   tools and injects discriminative keywords when two tools overlap
   (e.g. `quick_search` = "local Redis cache" vs. `deep_search` = "full
   table scan").
3. **Server Document Refiner** — synthesizes tool docs into a
   server-level overview. Final indexable unit per tool:
   `Chunk_i = Doc_overview ⊕ Doc_tool_i` (global server context +
   local tool detail).

## Benchmark (MCP-Focus Benchmark)

- **3,763 real-world open-source MCP servers** collected from Glama.ai —
  chosen for heterogeneity in domain, code structure, and doc quality.
- **Semi-automated query construction** (based on MCPEval) from
  Glama-validated tool schemas + LLM drafting + human-in-the-loop
  review. **1,000 queries each** for the 1-, 2-, and 3-function-point
  settings. Queries categorized on three axes: **Functional Volume**
  (1/2/3 tools), **Semantic Ambiguity** (explicit vs. implicit-intent),
  **Constraint Specificity** (explicit technical constraints vs.
  general).
- Motivating stat (Table 1, 1,247 popular Glama servers, LLM-as-judge):
  tool *output* info is missing/poor for ~85% of servers; docs are
  structurally thin and semantically unclear — README is the de-facto
  only doc.

## Findings (verified from PDF)

- **Consistent, non-trivial gains over the README baseline across all 6
  retrievers and all metrics** (BM25 sparse + 5 dense: Contriever,
  co-Condenser, TAS-B, ANCE, BGE; metrics r@5/r@10/n@5/n@10). Dense
  retrievers were fine-tuned on the respective doc set. Examples:
  - BM25 r@10: 0.479 / 0.465 / 0.536 → **0.728 / 0.756 / 0.796**
    (1-/2-/3-func).
  - Contriever r@10: 0.641 / 0.595 / 0.700 → **0.822 / 0.819 / 0.880**.
  - BGE strongest overall: r@10 **0.859 / 0.874 / 0.891**, n@10 **0.705
    / 0.712 / 0.740**.
- **Gap widens as queries need more tools** — 3-func n@10 gains: +0.250
  BM25, +0.226 Contriever, +0.196 ANCE. Fine-grained tool semantics
  matter most for multi-function intents.
- **Generalizes** to two public benchmarks (README→MCP-Focus): MCP-Bench
  (112 queries) BM25 r@10 0.554→0.848; MCP-Universe (157 queries) BM25
  r@10 0.089→0.350 (lower absolute — that set is tool-invocation-shaped,
  not retrieval-shaped).
- **Beats RepoAgent** (general-purpose repo-doc generator, same LLM
  backbone, Python-only 1,464-server subset) — e.g. Contriever r@10
  0.853→0.934. Confirms MCP-*specific*, retrieval-oriented docs beat
  generic code documentation; the win is the framework design, not model
  capacity.
- **Multi-server retrieval** (RRF fusion, r@20): improves on every
  retriever but stays hard (2→3 servers drops) — e.g. BM25 2-server
  0.506→0.647, 3-server 0.359→0.484.
- **Ablation**: all three stages help; removing the **Tool Document
  Refiner** hurts most (BM25 r@10 0.717→0.609), i.e. schema extraction
  alone is not enough — implementation-grounded semantics are the key
  ingredient.

## Rigor

High — peer-reviewed full paper (11 pp.) at SIGIR '26, a top-tier IR
venue, with a purpose-built 3,763-server benchmark, controlled query
design, 6-retriever evaluation, generalization tests on two external
benchmarks, and ablations. Contrast with the low-rigor JISEM
architecture article ingested the same day.
