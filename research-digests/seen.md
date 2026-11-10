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

2026-11-09 | pass:5 | university-of-toronto | What Drives AI Citations? Content, Retrieval and Model Knowledge in Generative Engine Optimization (GEO) | https://arxiv.org/abs/2610.15033 | 158K answers, 468K citations, 90 days, 3 engines; within-site design; data and code released
2026-11-09 | pass:5 | university-of-toronto | Location, Location, Generation: Where You Ask Matters for Generative Engine Optimization | https://arxiv.org/abs/2610.24081 | controlled audit, 31,200 answers with noise baseline; data and code released
2026-11-09 | pass:5 | university-of-delaware | Which Metadata Matters for LLM Tool Selection in MCP? Evidence from Controlled Factor-Level Interventions | https://arxiv.org/abs/2610.14334 | single-factor interventions across 5 LLMs; scripts released; model versions stand in for study period
2026-11-09 | pass:4 | fudan-university | From Public Posts to AI-Search Citations: Measuring the Fragility of AI Search | https://arxiv.org/abs/2610.11932 | controlled planting experiments on 10 platforms with stated counts and dates; code release not stated
2026-11-09 | pass:4 | ahrefs | How ChatGPT Does Query Fan-Out (15 Million Queries Studied) | https://ahrefs.com/blog/query-fan-out-chatgpt/ | 66.6M responses, 15M fan-outs, Aug-Sep 2026, limitations stated
2026-11-09 | pass:4 | tryprofound | The half-life of an AI citation is 11 days | https://www.tryprofound.com/blog/the-half-life-of-an-ai-citation-is-11-days | 883K pages, 1.19M lifecycles, 12 months, Kaplan-Meier survival; no limitations section
2026-11-09 | pass:4 | ahrefs | How Stable Are AI Citations? 10 Things We Learned Tracking 37,500 Citations | https://ahrefs.com/blog/how-stable-are-ai-citations/ | 37.5K citations over 20 days across 5 tools; thorough limitations
2026-11-09 | pass:4 | ahrefs | AI Overviews Cut CTR by 23.1% in France | https://ahrefs.com/blog/ai-overviews-france-impact/ | natural experiment with control group, 963 domains; 9-day post window
2026-11-09 | pass:4 | politecnico-di-milano | Auditing Source Exposure in Baidu and Google AI Search | https://arxiv.org/abs/2609.24407 | 500 queries x 4 settings, 23K references, manual validation; accepted at EMNLP 2026 workshop
2026-11-09 | pass:4 | tryprofound | What's changed with Sonnet 5.5 | https://www.tryprofound.com/blog/what-s-changed-with-sonnet-5-5 | 711 prompts x 20 runs per model via API; no significance tests
2026-11-09 | pass:4 | ipullrank | How the Same 16,000 Users Behave in AI Search vs. Google | https://ipullrank.com/ai-search-user-behavior | 16,310 matched clickstream users; Nov 2024 data; limitations stated
2026-11-09 | pass:4 | growth-memo | Organic traffic is down, but it's not all AI | https://www.growth-memo.com/p/organic-traffic-is-down-but-its-not | Similarweb 17,863 domains, Sep 2023-Aug 2026, sensitivity checks; modeled visits
2026-11-09 | pass:3 | discovered-labs | What Drives Citations in Production Large Language Models? An Observational Multi-Method Study of Two Million AI Citations Across Ten Thousand Web Pages | https://arxiv.org/abs/2609.35077 | 2.1M citations, strong stats; vendor COI, data unreleased, internal numeric inconsistencies, exact dates missing
2026-11-09 | pass:3 | aiso-boost | From Prompt to Recommendation: A Fitted Stage Model of Brand Visibility in AI Search | https://arxiv.org/abs/2609.23162 | 34,960 observations, chronological holdout; proprietary data, single vendor author, COI disclosed
2026-11-09 | pass:3 | mintlify | Highlights from the 2026 State of Knowledge Report | https://www.mintlify.com/blog/the-state-of-knowledge-2026-highlights | platform data and 2,400-test benchmark; agent vs human classification method not disclosed
2026-11-09 | pass:3 | semrush | AI Overviews have nearly doubled across five commercial search modifiers | https://www.semrush.com/blog/ai-overviews-commercial-modifiers-study/ | 400-keyword fixed panel, 12 months; small panel, US desktop, no limitations
2026-11-09 | pass:3 | growth-memo | Does AI drive more direct traffic? | https://www.growth-memo.com/p/does-ai-drive-more-direct-traffic | 12 GA4 properties, multiple-testing correction; small B2B sample
2026-11-09 | pass:2 | zyppy | We Opted Out of Google AI Search - Here's What Happened | https://signal.zyppy.com/p/we-opted-out-of-google-ai-search | single-site on/off experiment, 56 days, GSC data
2026-11-09 | pass:2 | gofishdigital | Go Fish Research: What 4,599 ChatGPT Responses Reveal | https://gofishdigital.com/blog/go-fish-research-what-4599-chatgpt-responses-reveal/ | single client, 63 days; exact dates and model version not stated
2026-11-09 | pass:2 | metehan-yesilyurt | Publish stats, get cited: The tactic that put my data all over the web | https://metehan.ai/blog/publish-stats-get-cited-the-tactic-that-put-my-data-all-over-the-web/ | n=1 site field experiment, no control; author works at Peec AI
2026-11-09 | pass:2 | growth-memo | What the prompts of 200 study participants tell us about the software buying process on AI | https://www.growth-memo.com/p/how-software-buyers-use-ai | collection period not stated (current platform data, capped at 3); self-reported survey, recruitment not described
2026-11-09 | reject:g2 | zyppy | Google AI Ranking Factors | https://signal.zyppy.com/p/google-ai-ranking-factors | g2: no fieldwork period, sample only "over 130"; measures expert perception not outcomes
2026-11-09 | pass:3 | ahrefs | Which Types of Mentions Correlate the Strongest With AI Visibility? (260M AI Prompts Analyzed) | https://ahrefs.com/blog/mention-types-ai-visibility/ | collection period not stated (current Brand Radar snapshot, capped at 3); 10K brands, Spearman within volume bands
2026-11-09 | reject:g3 | selvam | CITECHOICE: A Causal Audit of How Document Presentation Redistributes Citation Credit in Agentic Search | https://arxiv.org/abs/2609.15164 | g3: no institution listed and no prior publications found for either author
2026-11-09 | pass:5 | northwestern-university | Does the Citation Matter? Quality, Grounding, and Physician-Rubric Accuracy of Google's AI Overviews for Medical Information | https://arxiv.org/abs/2610.39339 | 3,610 health queries, 2026-09-16 to 09-18, validated classifiers; code and data released
2026-11-09 | pass:5 | nara-institute-of-science-and-technology | Do Coding Agents Follow AGENTS.md? The Effect of Policy Wording on Instruction Compliance | https://arxiv.org/abs/2611.04367 | controlled 86-task experiment, 4 harness/model combos, named versions; replication package
2026-11-09 | pass:4 | ahrefs | AI Overviews Currently Appear for 83% of Branded Searches | https://ahrefs.com/blog/ai-overviews-on-branded-searches/ | 232.8M SERP crawls plus 100-brand weekly panel, Jul-Sep 2026; found by industry and practitioner lanes
2026-11-09 | pass:4 | xi-an-jiaotong-university | Understanding ChatGPT Citations: Evidence from Production Web Search Across Model Generations | https://arxiv.org/abs/2610.15382 | 4,238 ChatGPT Web runs over 4 model settings, Mar-Jul 2026, permutation tests; only 80 queries
2026-11-09 | pass:4 | north-carolina-state-university | When Instruction Files Go Stale: Documentation Debt and Hidden Cost in Coding Agents | https://arxiv.org/abs/2611.09802 | 732 trajectories, named versions, replication package; only 3 stale cases
2026-11-09 | pass:4 | university-of-windsor | Toward an Evidence-Based Template for Agent Instruction Files: An Empirical Study of Adoption, Consistency, and Maintenance | https://arxiv.org/abs/2611.02383 | 1,000 repos, 3,387 files, kappa 0.80; replication package; template tiers heuristic
2026-11-09 | pass:4 | maastricht-university | If I Had to Buy Just ONE: Galaxy S26 Ultra: Auditing AI-Generated Product Recommendations | https://arxiv.org/abs/2609.18729 | 1,536 responses across 5 conditions, Sept 2026, validated annotation; Netherlands vantage only
2026-11-09 | pass:4 | university-of-texas-at-dallas | Breaking News Out of the Filter Bubble: Generative AI Search Diversifies Collective Attention and Raises Shared Information Consumption | https://arxiv.org/abs/2609.38946 | randomized field experiment, 37,561 Washington Post readers, Oct-Nov 2024; data under DUA
2026-11-09 | pass:3 | university-of-michigan | Do GEO Gains Survive the Live Web? Evaluating In-the-Wild Visibility Gains of Generative Engine Optimization via LIVE-GEO | https://arxiv.org/abs/2611.01126 | live-web experiment, 80 brands x 6 variants, 8 evaluators; collection period not stated (capped at 3)
2026-11-09 | pass:3 | otterly | What Content Do AI Engines Cite? A Study of 617,985 Citations Across 7 Engines and 5 Industries | https://otterly.ai/blog/content-types-cited-by-ai-study/ | 617,985 citations, Sept 2026; prompt set skewed to best/top phrasing; Getfluence partnership
2026-11-09 | pass:3 | otterly | Do AI Engines Read Your Open Graph Tags? We Hid Codes in Ours to Find Out | https://otterly.ai/blog/do-ai-engines-read-open-graph-tags/ | canary-token experiment, 2,275 answers, 2026-10-06 to 10-18; 3 test pages on own blog
2026-11-09 | pass:3 | tryprofound | How does personal context change LLM responses? | https://www.tryprofound.com/blog/how-does-personal-context-change-llm-responses | controlled, 2,240 answers, 2 models, synthetic profiles; one day, one category
2026-11-09 | pass:3 | vercel | State of agent skills | https://vercel.com/blog/state-of-agent-skills | first-party registry data, ~1M skills, Jan-Aug 2026; classified sample size undisclosed
2026-11-09 | pass:3 | ahrefs | Every OpenAI Publisher Partnership, and How Often ChatGPT Cites Them | https://ahrefs.com/blog/openai-publisher-partnerships/ | 5.5M US ChatGPT answers, 85 partner domains; simple counts, US only
2026-11-09 | pass:3 | no-hacks | Three AI models picked different products from the same Shopify catalog | https://nohacks.co/blog/three-ai-models-picked-different-products | 1,980 controlled picks with position-reversal tests, Oct 2026; Anthropic models only, keyword coding
2026-11-09 | pass:3 | growth-memo | What channels grow when organic search shrinks? | https://www.growth-memo.com/p/what-channels-grow-when-organic-search | Similarweb estimates, 1,896 shared domains, Jan-Aug 2026 vs 2025; some per-country counts missing
2026-11-09 | pass:3 | graphite | The State of GenAI | https://graphite.io/research/the-state-of-genai | Similarweb sessions for 6 LLMs and 43K domains, Jul 2023-Sep 2026; single data vendor
2026-11-09 | pass:2 | seer-interactive | AI Citations Aren't Your Top KPI: ChatGPT-5.6 Luna Runs More Targeted Searches | https://www.seerinteractive.com/insights/gpt-5.5-vs-gpt-5.6-luna | 346 matched prompts; collection period not stated (capped at 3); tooling and prompt selection not described
2026-11-09 | pass:2 | amplifying | What Dots Actually Choose: OpenAI's Agent Already Has a Stack | https://www.amplifying.ai/research/openai-dots-choose | n=8 builds of one prompt; collection period not stated (capped at 3)
2026-11-09 | pass:2 | marie-haynes | GEO is a distraction | https://www.mariehaynes.com/geo-is-a-distraction/ | 100 sites GA4; collection period not stated (capped at 3); conversions and LLM-traffic identification not defined
2026-11-09 | unverified | tj-digital | 2026 AI Citation Study: What ChatGPT and Google's AI Cite | https://tjrobertson.com/ai-citation-study/ | primary page served the agency homepage twice; method known only from SEJ coverage
2026-11-09 | reject:g2 | chartbeat | 2026 Publisher Playbook (Chartbeat) | https://lp.chartbeat.com/2026-publisher-playbook-chartbeat | g2: no sample size (publisher/site count) stated; gated report read via SEJ coverage
2026-11-09 | reject:g2 | brightedge | Holiday Travel in AI Search: The Travel Brands AI Puts on Its List | https://www.brightedge.com/resources/research-reports/holiday-travel-ai-search | g2: neither prompt count nor study period stated
