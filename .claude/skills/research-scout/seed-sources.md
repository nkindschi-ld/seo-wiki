# Research scout seed sources

Lanes start here, then search the open web. This is not a whitelist: a
source not listed here can still get into the digest by passing the gate.

- **Curated** belongs to you. The agent never edits or removes these
  entries. Move a Discovered entry here to make it permanent.
- **Discovered** is maintained by the agent. A source is added after one
  gate pass with rigor ≥ 4, or gate passes on two separate run dates.
- **Caution** sources failed the gate (g1–g3) on two separate run dates,
  or were flagged by you. Lanes treat them skeptically.

Entry format: `- key: <key> | name: <name> | …` (one line per entry; the
scripts in `scripts/` parse these lines).

## Curated

### Academic
- key: arxiv-cs-ir | name: arXiv cs.IR (Information Retrieval) | url: https://arxiv.org/list/cs.IR/recent | note: core venue for retrieval, RAG, generative search papers
- key: arxiv-cs-cl | name: arXiv cs.CL (Computation and Language) | url: https://arxiv.org/list/cs.CL/recent | note: LLM citation, attribution, manipulation papers
- key: acl-anthology | name: ACL Anthology | url: https://aclanthology.org/ | note: ACL/EMNLP/NAACL proceedings
- key: sigir | name: ACM SIGIR | url: https://sigir.org/ | note: premier IR conference
- key: the-web-conference | name: The Web Conference (WWW) | url: https://www2026.thewebconf.org/ | note: web search and generative-engine papers
- key: semantic-scholar | name: Semantic Scholar | url: https://www.semanticscholar.org/ | note: cross-venue paper search

### Industry research
- key: semrush | name: Semrush | url: https://www.semrush.com/blog/ | note: most-cited publisher in the wiki (24 sources); large AI-search data studies
- key: ahrefs | name: Ahrefs | url: https://ahrefs.com/blog/ | note: 13 wiki sources; large-sample citation and AIO studies
- key: google | name: Google Search Central | url: https://developers.google.com/search/blog | note: official guidance and announcements; primary source for Google behavior
- key: dejan | name: DEJAN AI (Dan Petrovic) | url: https://dejan.ai/blog/ | note: 10 wiki sources; grounding and model-internals experiments
- key: otterly | name: Otterly.AI | url: https://otterly.ai/blog/ | note: AI-search monitoring studies
- key: tryprofound | name: Profound | url: https://www.tryprofound.com/blog | note: 680M-citation cross-platform analyses
- key: peec | name: Peec AI | url: https://peec.ai/blog | note: ChatGPT query fan-out studies
- key: lumar | name: Lumar | url: https://www.lumar.io/blog/ | note: candidate page selection and semantic relevance
- key: amplifying | name: Amplifying | url: https://amplifying.ai/research | note: coding-agent tool-selection studies (Claude Code, Codex)
- key: similarweb | name: Similarweb | url: https://www.similarweb.com/corp/ | note: AI-referral traffic data
- key: sparktoro | name: SparkToro (Rand Fishkin) | url: https://sparktoro.com/blog/ | note: clickstream research on AI vs. search traffic
- key: brightedge | name: BrightEdge | url: https://www.brightedge.com/resources | note: AI Overviews prevalence research
- key: seer-interactive | name: Seer Interactive | url: https://www.seerinteractive.com/insights | note: AIO CTR-impact studies
- key: airops | name: AirOps | url: https://www.airops.com/report | note: fan-out effect reports
- key: detailed | name: Detailed (Glen Allsopp) | url: https://detailed.com/ | note: AI answer-volatility study
- key: nozzle | name: Nozzle | url: https://nozzle.io/research | note: SERP research
- key: mintlify | name: Mintlify | url: https://www.mintlify.com/blog | note: llms.txt and agent docs-retrieval benchmarks
- key: vercel | name: Vercel | url: https://vercel.com/blog | note: AI crawler traffic data
- key: rankability | name: Rankability | url: https://www.rankability.com/blog | note: SEO and AI-search research
- key: nngroup | name: Nielsen Norman Group | url: https://www.nngroup.com/articles/ | note: user research on AI search behavior
- key: github | name: GitHub Blog | url: https://github.blog/ | note: agents.md and coding-agent guidance

### Practitioner
- key: growth-memo | name: Growth Memo (Kevin Indig) | url: https://www.growth-memo.com/ | note: data-driven AI-search analyses; 4 wiki sources
- key: zyppy | name: Zyppy Signal (Cyrus Shepard) | url: https://signal.zyppy.com/ | note: fan-out and AI visibility studies
- key: ipullrank | name: iPullRank (Mike King) | url: https://ipullrank.com/ | note: AI Mode / personal-intelligence experiments
- key: metehan-yesilyurt | name: Metehan Yesilyurt | url: https://metehan.ai/ | note: ChatGPT/Perplexity retrieval reverse-engineering
- key: lily-ray | name: Lily Ray | url: https://lilyraynyc.substack.com/ | note: E-E-A-T and AI-search analyses
- key: aleyda-solis | name: Aleyda Solis | url: https://www.aleydasolis.com/en/ | note: AI-search optimization research and checklists
- key: chris-long | name: Chris Long | url: https://www.linkedin.com/in/chris-long-marketing/ | note: frequent original AI-search tests
- key: visively | name: Visively (Pedro Dias) | url: https://visively.com/kb | note: ranking-fundamentals research
- key: derivatex | name: DerivateX (Apoorv Sharma) | url: https://derivatex.agency/ | note: AIO vs. SERP benchmark studies
- key: search-engine-land | name: Search Engine Land | url: https://searchengineland.com/ | note: original experiments and study coverage (prefer the primary study it covers)
- key: search-engine-journal | name: Search Engine Journal | url: https://www.searchenginejournal.com/ | note: original experiments and study coverage (prefer the primary study it covers)
- key: gofishdigital | name: Go Fish Digital | url: https://gofishdigital.com/blog/ | note: AI-search experiments

## Discovered

## Caution
- key: thedigitalbloom | name: The Digital Bloom | added: 2026-08-03 | reason: "reports" are secondary aggregations of other studies, with a provenance red flag (relabeled Profound's 680M figure as its own)
- key: jisem | name: Journal of Information Systems Engineering and Management (JISEM) | added: 2026-08-06 | reason: low-rigor venue; papers observed with zero quantitative results
