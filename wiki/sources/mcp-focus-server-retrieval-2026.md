---
type: source
tags: [aeo, seo]
date_published: 2026-07-20
date_ingested: 2026-08-06
origin: raw/studies/mcp-focus-server-retrieval-2026.pdf
---

# MCP-Focus — Function-Oriented Document Enhancement for MCP Server Retrieval (SIGIR '26)

**Citation**: Wenchun Jing, Haiyang Shen, Haoran Wang, Qi Liu, Ningyuan
Li, Chaoran Luo, Ning Zhang, Yun Ma, "MCP-Focus: Leveraging
Function-Oriented Document Enhancement for MCP Server Retrieval,"
*Proc. 49th Int'l ACM SIGIR Conference (SIGIR '26)*, Melbourne, Jul
20–24 2026. DOI 10.1145/3805712.3809582. Code/data:
github.com/JingWC/MCP-Focus. Full PDF held at `origin`.

**Provenance note**: first ingested from public sources (ACM listing +
authors' repo) because the ACM PDF returned 403; the user then supplied
the PDF, and all claims/figures below were **verified against the actual
paper** on 2026-08-06.

## Why it matters here

A **high-rigor (SIGIR) empirical answer to the "discoverability"
risk** flagged in [[docs-over-mcp]]: when an agent or registry must pick
the right MCP server out of thousands, the quality of a server's
*documentation* measurably determines whether it gets retrieved — and
raw self-reported docs (README + tool `name`/`description`/`input
schema`) are weak signals. This is the rigorous counterpart to the
low-rigor [[aluri-mcp-documentation-retrieval-2025]]: where Aluri only
*asserted* doc quality matters, MCP-Focus *measures* it.

## Key takeaways

1. **MCP server retrieval is its own IR problem.** As the MCP ecosystem
   grows, selecting the correct server/tool for a query out of thousands
   is a retrieval task — and a bottleneck for agent reliability.
2. **Raw MCP docs retrieve poorly.** READMEs are the de-facto only doc
   and are structurally thin / semantically unclear (Table 1: tool
   *output* info missing or poor for ~85% of 1,247 popular servers).
3. **Implementation-grounded docs retrieve better.** MCP-Focus's
   bottom-up pipeline — **Tool Extractor → Tool Document Refiner**
   (white-box code tracing + contrastive differentiation of similar
   tools) **→ Server Document Refiner** (chunk = server overview ⊕ tool
   doc) — beats the README baseline across **all 6 retrievers and all
   metrics**. E.g. BM25 r@10 0.479/0.465/0.536 → 0.728/0.756/0.796
   (1/2/3-func); BGE strongest (r@10 up to 0.891). Gains **widen with
   more function points** (3-func n@10 +0.25 for BM25). It's
   data-centric — enhance the *docs*, not the retriever.
4. **Generalizes & beats a generic baseline.** Improves README-indexing
   on two external benchmarks (MCP-Bench, MCP-Universe) and beats
   RepoAgent (general repo-doc generator, same LLM backbone) — so the
   win is the MCP-specific retrieval-oriented design, not model capacity.
   Ablation: the **Tool Document Refiner matters most** (schema alone
   isn't enough).
5. **Purpose-built benchmark**: 3,763 real-world open-source MCP servers
   (Glama.ai) + 1,000 queries each for 1/2/3-function settings, varied
   on semantic ambiguity, constraint specificity, and functional volume.

## Practical implication (for the wiki's audience)

The vendor-facing version: **your MCP server's discoverability depends
on documentation that reflects what your tools actually do, not just a
hand-written blurb.** Tool descriptions and server overviews are a
retrieval-optimization surface — the MCP-era analogue of on-page SEO for
being *found* among many servers, distinct from the within-server
chunking that governs the answer once you're selected.

## What it updated

- Extended [[docs-over-mcp]] — added an "MCP server discoverability /
  retrievability" section; upgraded the "tool descriptions are an
  optimization surface" claim from asserted to empirically supported.
- Annotated [[aluri-mcp-documentation-retrieval-2025]] — its
  doc-quality-matters claim now has rigorous corroboration.
