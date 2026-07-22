---
type: source
tags: [seo, aeo]
date_published: 2024-04-11
date_ingested: 2026-07-22
origin: raw/studies/kumar-lakkaraju-manipulating-llms-2024.pdf
---

# Manipulating Large Language Models to Increase Product Visibility (Kumar & Lakkaraju, Harvard, 2024)

**Citation:** Kumar, Aounon; Lakkaraju, Himabindu. "Manipulating Large
Language Models to Increase Product Visibility." Harvard University.
arXiv:2404.07981v2 [cs.IR], 2024-04-11 (v2: 2024-09-02).
https://github.com/aounon/llm-rank-optimizer

## What this source is

A **black-hat** adversarial-attack paper (explicitly disclaimed by the
authors as "conducted in the spirit of scientific inquiry," not a
recommended tactic) — already referenced secondhand elsewhere in this
wiki via [[ahrefs-llm-optimization]] and cited in
[[c-seo-bench-2025]]'s related-work section as one of the black-hat
C-SEO papers that benchmark scopes out. This is the primary source.

## Method: Strategic Text Sequence (STS)

A vendor embeds an optimized adversarial token sequence (the STS) into
their product's information page. The STS is optimized using the
**Greedy Coordinate Gradient (GCG)** algorithm — the same
jailbreak-attack algorithm used to bypass LLM safety guardrails,
repurposed here for a benign-in-intent but manipulative objective:
minimizing the cross-entropy loss between the LLM's output and the
string "1. [Target Product Name]." GCG iteratively replaces STS tokens
with high-gradient candidates. The STS can optionally be optimized
against **randomized product-list orderings** to make it robust to
however the retrieval step happens to order candidates in the prompt.

**Experimental setup**: a catalog of 10 fictitious coffee machines
(JSON-line format: Name, Description, Price, Capacity, Rating, Ideal
For) fed to **Llama-2** (open-source; the authors note, citing prior
GCG work, that such sequences have been shown to transfer to black-box
models like GPT-4, but this paper's own experiments test Llama-2 only)
alongside a user query requesting affordable coffee machine
recommendations.

## Key findings

- **ColdBrew Master** ($199, high-priced, almost never recommended
  without intervention): after 2000 GCG iterations, the STS took it
  from **not appearing in recommendations at all to the top
  recommendation within ~100 iterations**, and it stayed the top
  recommendation for the remainder of the run.
  - With a **fixed product order** in the prompt, evaluated across 200
    independent trials with randomized order at *evaluation* time: the
    STS gave a rank **advantage in ~40%** of trials, **no
    change in ~60%**, and a **disadvantage in a tiny fraction**.
  - When the STS itself was **optimized against randomized product
    order** (not just evaluated under it), the advantage rate jumped to
    **~95%**, with disadvantage reduced to negligible — order-robust
    optimization meaningfully improves real-world reliability of the
    attack.
- **QuickBrew Express** ($89, more affordable, usually ranks 2nd
  without intervention): after 2000 GCG iterations, becomes the
  consistent top recommendation (with an initial dip in rank during
  early iterations before recovering).
  - With a **fixed-order-optimized** STS evaluated under randomized
    order: advantage (~15%) and disadvantage (~15%) were roughly
    equal, **"neutralizing its overall benefit"** — a fixed-order STS
    does not reliably help a product that's already ranking well when
    order varies.
  - When optimized against randomized order: advantage rose to **~48%**
    with disadvantage minimized — order-robust optimization was
    necessary to get a real net benefit for this already-competitive
    product, more so than for the near-invisible ColdBrew Master.
- **Order-robustness is the single most important lever tested**:
  across both products, an STS optimized against a fixed prompt order
  performs far worse under real-world (randomized) retrieval ordering
  than one explicitly optimized to be robust to that randomization —
  the single biggest determinant of whether the attack transfers from
  lab conditions to a realistic deployment.

## Correction to a wiki citation — the "34% to 59.4%" figure is not in this paper

[[ahrefs-llm-optimization]] (and this wiki's [[geo-content-optimization-tactics]],
which cited it secondhand) states this paper found a "preference-
manipulation prompt injection" that "raised a fake product's
recommendation rate from 34% to 59.4%, a 2.5x selection increase."
**This specific figure does not appear anywhere in the primary paper.**
The paper reports rank-*advantage* percentages from randomized-order
trials (e.g., ~40% → ~95% advantage rate for ColdBrew Master, fixed vs.
order-robust STS) and qualitative rank-distribution plots (before/after
STS, 200 trials, ColdBrew Master going from "almost never recommended"
to "top recommendation in most evaluations"), but no "34%"/"59.4%"
recommendation-rate statistic. This looks like either a misattribution
in Ahrefs' article (possibly conflating this paper with a different,
unidentified study) or a garbled restatement of the ~40%-advantage
figure — either way, **the specific numbers in the wiki's existing
adversarial-risk note should be corrected to the verified primary-source
figures above** rather than repeated. See the Conflicting Evidence
(citation-accuracy) note on [[geo-content-optimization-tactics]].

## Relationship to existing wiki claims

- **Cited in [[c-seo-bench-2025]]'s related work** as one of several
  black-hat C-SEO papers (alongside Nestaas et al. 2025, Pfrommer et al.
  2024, Tang et al. 2025) that operate on a different threat model than
  that benchmark's white-hat scope — small, fictitious-catalog datasets
  (10 products here) rather than C-SEO Bench's 16.3k-document
  multi-domain design, and adversarial optimization rather than
  legitimate content editing.
- **Corrects, not conflicts with**, the qualitative existence of the
  risk described in [[ahrefs-llm-optimization]] and
  [[geo-content-optimization-tactics]]'s "Known adversarial risk"
  section — the *existence* of this vulnerability is real and confirmed
  by this primary source; only the specific "34%→59.4%" numbers cited
  secondhand are unverified/likely inaccurate.
- **Requires white-box or transfer access**: GCG is a gradient-based
  attack, requiring either direct model access (as used here, on
  Llama-2) or reliance on adversarial-sequence transferability to
  black-box models (asserted by prior work, not independently retested
  by this paper on GPT-4/production systems) — a meaningfully higher
  bar than the prompt-injection-via-plain-text techniques described in
  other adversarial C-SEO literature.

## Caveats (stated or implied by the authors)

- Tests a **fictitious** product catalog (10 coffee machines) and a
  single query type (affordable coffee machine recommendations) —
  small-scale relative to later benchmarks like [[c-seo-bench-2025]].
- Tested on **Llama-2 only**; transferability to production black-box
  systems (GPT-4, Gemini, commercial RAG search) is asserted from prior
  GCG literature, not directly demonstrated in this paper's own
  experiments.
- The authors explicitly frame this as demonstrating a **vulnerability**
  to motivate defenses, not as a usable technique, and note "more
  research is needed to uncover other vulnerabilities" and that
  "safeguards must be established."

## See also

- [[ahrefs-llm-optimization]] — the secondhand citation of this paper
  that contains the unverified "34%→59.4%" figure corrected above.
- [[geo-content-optimization-tactics]] — the "Known adversarial risk"
  section updated with the verified primary-source figures.
- [[c-seo-bench-2025]] — cites this paper in its related-work
  discussion of black-hat C-SEO as a category distinct from its own
  white-hat benchmark scope.
- [[bardas-white-hat-seo-llm-2025]] — a white-hat competitive-search
  paper from the same broader research area (LLM-driven document/
  product ranking manipulation), using legitimate editing rather than
  adversarial token optimization.
