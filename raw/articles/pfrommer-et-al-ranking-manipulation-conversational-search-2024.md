# Ranking Manipulation for Conversational Search Engines

Authors: Samuel Pfrommer, Yatong Bai, Tanmay Gautam, Somayeh Sojoudi
(UC Berkeley, EECS)
Venue: EMNLP 2024 (Proceedings of the 2024 Conference on Empirical
Methods in Natural Language Processing, pages 9523–9552)
Publish date: 2024-11-12 (conference dates Nov 12-16, 2024)
Source: https://aclanthology.org/2024.emnlp-main.534.pdf
Retrieved: 2026-07-23

## Abstract (paraphrased)

Conversational search engines load retrieved website text into an
LLM's context for summarization. The paper formalizes conversational
search ranking as an adversarial problem, introduces a real-world
consumer-product-website dataset, and analyzes how different LLMs
weight product name, document content, and context position absent
any attack. It then presents a tree-of-attacks-based jailbreaking
technique that reliably promotes low-ranked products, and shows these
attacks transfer effectively to a production conversational search
engine, perplexity.ai.

## Methodology

- Dataset: real-world consumer product websites, grouped into product
  categories, each with a designated lowest-ranked ("promoted") product
  to attack.
- Attack technique: built on Tree of Attacks with Pruning (TAP), a
  jailbreaking method — adapted here to optimize for ranking-score gain
  of the promoted product rather than harmful-content jailbreak
  success. Attacks were crafted white-box (assuming ability to inject
  text into the LLM's retrieved-document context) against GPT-3.5
  Turbo, GPT-4 Turbo, Llama 3 70B, and Mixtral 8x22.

## Baseline (non-adversarial) ranking findings

Different LLMs vary significantly in how they weight product
name/brand, document content, and context (position-in-context)
signals when ranking un-manipulated products. GPT-4 Turbo and Llama 3
70B lean heavily on product name/brand; GPT-4 Turbo and Mixtral were
comparatively less swayed by document content alone. Mixtral 8x22
showed the strongest sensitivity to context position specifically.

## Adversarial attack effectiveness (Table 1: mean ranking-score gain)

Reported as mean absolute ranking-score gain / mean gain as a
percentage of the maximum possible gap-to-top-rank:

- GPT-3.5 Turbo: 3.38 / 57.53%
- GPT-4 Turbo: 5.00 / 82.94%
- Llama 3 70B: 6.02 / 95.74%
- Mixtral 8x22: 4.13 / 76.23%
- Sonar Large Online (Perplexity's model): 2.89 / 54.23%

Even models minimally swayed by ordinary document content (GPT-4
Turbo, Mixtral) remained susceptible to adversarial injections — the
paper attributes this to instruction-tuned models treating perceived
instructions anywhere in context as commands, not just in the
designated user-query field.

## Black-box transfer to perplexity.ai

Because full API access to perplexity.ai's search tool wasn't
available, the authors used Sonar Large Online (Perplexity's
online-enabled model) as a surrogate: they hosted adversarially
manipulated webpages on their own server (random-string URLs, to avoid
biasing ranking via the URL itself) and had Sonar Large Online scrape
and evaluate the links directly, rather than pasting page text into
the prompt. Attacks originally crafted against GPT-4 Turbo were
transferred as-is (interspersed 15 times through the page's HTML text
elements) and still substantially raised the promoted product's
ranking on this closed-source, production RAG system (~2.89 mean
position gain, 54.23% of the maximum possible gap) — despite the
attack having no white-box access to Perplexity's actual ranking
pipeline. The paper notes anecdotally (not rigorously quantified) that
the full perplexity.ai product exhibits similar vulnerability. It also
notes that visible injected text could be hidden via conventional
(black-hat) SEO techniques (e.g., off-screen or under-element
positioning) — mentioned as a risk, not a recommendation.

## Conclusion / stated significance

Frames this as an open robustness problem for conversational search
given the financial incentive website owners have to boost ranking —
the same underlying incentive structure that legitimate GEO/AEO
tactics operate within, but via adversarial rather than content-quality
means.
