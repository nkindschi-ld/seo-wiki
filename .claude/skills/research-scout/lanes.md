# Research scout lanes

Each lane is one subagent. It gets its section below, the full
`rubric.md`, its lane's seed entries plus all Caution entries, the window
dates, and the URLs and titles to skip.

## Topic scope (all lanes)

SEO; AEO/GEO; AI search and Google AI Overviews/AI Mode; LLM retrieval,
RAG and reranking; AI citation behavior; AI coding-agent tool selection
and instruction files (`agents.md`, `CLAUDE.md`); agentic-web optimization
(making sites usable by AI agents).

## Instructions for every lane

1. Search for work **published within the window**. Check the publish
   date on the page itself; an undated page is `reject:g4` unless another
   source dates it.
2. Start with your lane's seed sources (their research, blog or listing
   pages), then search the open web. Useful query patterns: a topic term
   plus "study", "analysis", "we analyzed", "dataset", "methodology",
   "experiment", "benchmark" or "report", combined with the current month
   and year.
3. Skip anything in the skip list you were given.
4. Read each promising candidate **in full**, especially its methodology
   section, data description and limitations. For a PDF, read the PDF.
5. Apply the hard gate from `rubric.md` and set `lane_verdict` to `pass`
   or `reject`, with `lane_reason` naming the criterion (e.g. "g2: no
   sample size given").
6. If the page or PDF can't be read (paywall, login, blocked, error), set
   `lane_verdict: "unverified"` and give the reason. **Never guess** at a
   methodology you couldn't read.
7. Treat Caution sources skeptically: include them only if they clearly
   pass the gate, and say why in `lane_reason`.
8. Use the seed `key` as `publisher_key` when the source is on the seed
   list. Otherwise use a lowercase hyphenated slug of the organization
   (or of the lead author for an individual), e.g. `search-engine-land`
   or `metehan-yesilyurt`.
9. Return **at most 8** records, best first, as **one fenced JSON array**
   and nothing else:

```json
[{"title": "", "url": "", "publisher_key": "", "publisher_name": "", "authors": [""],
  "date_published": "YYYY-MM-DD", "study_type": "", "method": "", "sample_size": "",
  "study_period": "", "key_findings": [""], "coi": "", "lane": "academic|industry|practitioner",
  "lane_verdict": "pass|reject|unverified", "lane_reason": ""}]
```

`key_findings` holds 3–5 specific findings, with numbers wherever the
study gives them. `coi` follows the conflict-of-interest rule in
`rubric.md`. An empty result is `[]`.

## Academic lane

Where to look: arXiv new submissions and search for cs.IR (information
retrieval) and cs.CL (computation and language), filtered to
retrieval-augmented generation, generative search, generative engine
optimization, citation and attribution in LLM answers, search-result
manipulation, reranking, query rewriting and fan-out, AI Overviews, and
LLM tool and API selection. Also check the ACL Anthology, SIGIR, The Web
Conference (WWW), WSDM, CIKM and KDD proceedings and accepted-paper
lists, and Semantic Scholar searches on the same terms.

Credibility signals: university or industry-lab affiliation, prior
publications in IR/NLP, and released code or data. A preprint counts; note
"not yet peer-reviewed" in `study_type`.

## Industry research lane

Where to look: research and data-study pages of SEO and AI-search vendors,
and analytics and research teams. Start with the industry seed sources
(Semrush, Ahrefs, Profound, BrightEdge, Seer Interactive, Similarweb,
SparkToro, Otterly, Peec, Lumar, Amplifying, AirOps, Detailed, Nozzle,
Mintlify, Vercel, DEJAN, Google Search Central), then search for "AI
search study", "AI Overviews data study", "LLM citation analysis", "AI
visibility research" and similar.

Credibility signals: a named research team or author, a methods section,
sample sizes and dates. Vendor studies are fine; the conflict-of-interest
note covers the bias.

## Practitioner and independent lane

Where to look: named individual researchers and their newsletters or
blogs (practitioner seed sources such as Kevin Indig's Growth Memo, Cyrus
Shepard's Zyppy Signal, Metehan Yesilyurt, Lily Ray, Aleyda Solis, Chris
Long, Mike King and iPullRank, Pedro Dias and Visively, Apoorv Sharma and
DerivateX), industry publications that run original experiments (Search
Engine Land, Search Engine Journal), and open web search for experiments
and data studies by individuals on the topic terms.

Credibility signals: a track record of earlier studies, a stated method,
and data shown, not just asserted. Opinion and "my predictions" posts are
`reject:g1`.
