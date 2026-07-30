---
type: source
tags: [aeo]
date_published: 2024-11-12
date_ingested: 2026-07-23
origin: raw/articles/pfrommer-et-al-ranking-manipulation-conversational-search-2024.md
---

# Ranking Manipulation for Conversational Search Engines (Pfrommer et al., UC Berkeley, EMNLP 2024)

**Citation:** Pfrommer, Samuel; Bai, Yatong; Gautam, Tanmay; Sojoudi,
Somayeh (UC Berkeley). "Ranking Manipulation for Conversational Search
Engines." EMNLP 2024, pp. 9523–9552.
https://aclanthology.org/2024.emnlp-main.534.pdf

Peer-reviewed EMNLP 2024 main-conference paper (higher rigor tier than
an arXiv preprint or vendor blog post).

## Key takeaways

- Formalizes conversational-search ranking as an adversarial problem
  and finds baseline (non-adversarial) LLM ranking behavior already
  varies significantly by model in how much weight it gives product
  name/brand vs. document content vs. context position.
- Introduces a tree-of-attacks-based jailbreaking technique (built on
  Tree of Attacks with Pruning) that reliably promotes a designated
  low-ranked product, tested against GPT-3.5 Turbo, GPT-4 Turbo, Llama
  3 70B, and Mixtral 8x22 — mean ranking-score gains of 54-96% of the
  maximum possible gap-to-top-rank across models.
- **Critically, demonstrates black-box transfer to a production
  system**: attacks crafted against GPT-4 Turbo, hosted on real
  webpages, and fed to Perplexity's Sonar Large Online model (as a
  surrogate for perplexity.ai, since full API access wasn't available)
  still achieved a substantial ranking-score gain (mean +2.89
  positions, 54.23% of max gap) — despite the attacker having no
  white-box access to Perplexity's actual closed-source RAG pipeline.
- Notes (anecdotally, not rigorously quantified) that the full
  perplexity.ai product shows similar vulnerability, and that injected
  text could be hidden via conventional black-hat SEO techniques
  (off-screen/under-element positioning) — flagged as a risk, not
  advice.

## What this updates in the wiki

**Closes an explicitly-flagged open gap**, doesn't conflict with
anything — [[geo-content-optimization-tactics]]'s existing "Known
adversarial risk: LLM recommendation manipulation" section, sourced
from [[kumar-lakkaraju-manipulating-llms-2024]], explicitly noted that
paper's attack "requires gradient/white-box access... not
independently retested here on production black-box systems." This
paper is exactly that missing independent black-box-on-production-system
test, for a different (jailbreaking/prompt-injection) attack family,
on a different production system (Perplexity, via Sonar Large Online)
— and finds the vulnerability holds without white-box/gradient access.

- Updated [[geo-content-optimization-tactics]] — added this paper to
  the "Known adversarial risk" section, closing the "not independently
  retested on production systems" caveat with concrete (if narrower,
  single-platform) evidence that black-box transfer to Perplexity
  works via straightforward prompt-injection, no gradient access
  needed.
