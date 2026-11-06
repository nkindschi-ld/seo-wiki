# Where do inaccurate AI claims come from?

**Author:** Lucas Kopinski (AI Strategist, Profound)
**Publication:** Profound Blog (Research)
**Published:** 2026-08-17
**URL:** https://www.tryprofound.com/blog/where-do-inaccurate-ai-claims-come-from
**Data:** Profound FactCheck, April–August 2026; snapshot as of 2026-08-14

---

## Full text (extracted from HTML via curl, 2026-10-02; nav and footer removed)

Profound recently released FactCheck, the first solution that shows brands what AI is getting wrong about them, where those claims came from, and how to fix them.
This research analyzes over 158,000 claims in FactCheck data to understand what drives inaccuracy across models, sources, and topics.
For the purposes of this research, we categorized inaccurate claims into four categories: brand (your company’s site), competitor (competitor’s site), earned (third-party publications), and social (social media and user-generated content).

### TL;DR
- Inaccurate claims came mostly from competitor and earned media citations.
- Most inaccurate claims were pricing- and billing-related.
- Inaccuracy rates by Answer Engine range from 4.3-6.8%.

### Which sources drive the most inaccurate claims? 

Unsurprisingly, claims citing sources in the competitor and earned buckets had the highest inaccuracy rates. 51% of brands had at least one inaccurate claim citing earned media.
Even brands’ own content can conflict with their records. 54% of brands had at least one inaccurate claim citing their own content, making regular audits of owned media an immediate lever for improving accuracy.

### Earned media inaccuracy is brand specific
Inaccuracies come from a long tail of outdated information. The top 10 domains account for only 13% of earned media inaccuracies, and the top 100 represent only 40% of errors.
That makes errors remarkably difficult to catch manually: they are widespread and vary by brand. For companies with inaccurate earned media coverage, errors typically come from just 4 websites, and they are often unique to a brand.
There’s no one-size-fits-all approach for correcting earned media. Marketers must identify the domains uniquely affecting their brand and focus on outreach.

### The most frequent topic related to inaccurate claims was pricing and billing

Pricing and billing has the highest inaccuracy rate and accounts for the largest share of inaccurate claims. It represents just 12% of evaluated claims but 24% of all inaccurate claims, far more than the next largest source of inaccurate claims, eligibility and terms, at 4%. This may partly be a selection effect: structured information like pricing and billing is more readily evaluated. The fact remains, however, that a large number of these claims are incorrect. One hypothesis is that pricing, offers, and eligibility change frequently and are likely to become outdated.
Some brand sites even have pricing information that conflicts with their records. Among brands with at least ten evaluated pricing claims, pricing is the highest-inaccuracy theme for 66% of them, making it one of the highest-leverage areas for marketers to address.
Earned media is the most important external source of pricing inaccuracy for brands to address because it is both highly associated with errors and influenceable by marketers. Pricing accounts for 35% of all earned media inaccuracies, and the problem appears to be widespread across most publishers. The top ten earned media domains associated with pricing inaccuracies account for only 15% of inaccuracies.
Marketers should therefore keep pricing details current on owned sites and monitor third-party sources for stale information.

### Claude has the second highest inaccuracy rate of all the models

The models that consumers trust are not always the most accurate. In early July, survey results showed that Claude was ranked the highest in trustworthiness when compared with other models. FactCheck data shows an interesting pattern: Claude is more than 1.3 times more inaccurate than ChatGPT.
ChatGPT and Claude also differ in the claims they get wrong. When faced with the same questions, ChatGPT and Claude overlap on only 12.5% of their returned claims, and only 11% of inaccurate claims. Previous research indicates that the two platforms also differ substantially in the sources that they cite.
So what’s the takeaway? Tracking more claims surfaces more domains that may require correction. Marketers must track inaccuracies for different Answer Engines separately, and each will require a model-specific strategy.

### What does this mean for your brand?
- There’s no silver bullet for fixing inaccurate claims. The sources and claims driving inaccuracies will vary by brand and by model. This requires ongoing monitoring.
- For third-party sources, prioritize earned media. Earned media is one of the biggest sources of inaccuracies and is one of the easiest third-party sources for marketers to influence. Identify the pages most associated with inaccuracies and prioritize outreach.
- The lowest-hanging fruit is to keep your information current and consistent. Ensure that pricing and frequently changing details remain consistent and up to date across your owned pages. A brand site is an authoritative source. You don’t want outdated information reinforcing inaccurate answers elsewhere.

### Methodology
- FactCheck claim analysis: We used the most recent claims with a final verdict of accurate or inaccurate. Semantically equivalent claims were grouped into a single canonical claim.
- Claim 1: “The company offers free shipping on orders over $50.”
- Claim 2: “Orders above $50 ship for free.”
- Both claims were then grouped into a canonical claim: “The company offers free shipping on orders over $50.”
- Inaccuracy rate definition: The share of decided claims classified as inaccurate. For example, if a website/source is 5% inaccurate, 5% of evaluated claims citing that site/source are inaccurate.
- Source and website analysis: Cited URLs were standardized to the domain level and classified as brand, competitor, earned, and social. Rankings show the share of those evaluated claims that were inaccurate.
- Topic and model analysis: Claims were grouped into topic families and compared across source types. Model-level results were deduplicated across repeated claims within each model.
Results are observational and are a snapshot of the most recently completed FactCheck run as of August 14, 2026.



## Charts (downloaded to raw/assets/, values transcribed 2026-10-02)

### Inaccuracy rate by source — `raw/assets/tryprofound-inaccurate-claims-by-source.png`
(~76,000 claim-source pairs, all models, Apr–Aug 2026; bands can overlap; excludes PR wire, earned institution, other)
- Competitor 4.68%
- Earned 4.62%
- Social 3.45%
- Brand 2.40%

### Inaccuracy rate by claim topic and source type — `raw/assets/tryprofound-inaccurate-claims-by-topic-and-source.png`
(~13,000 claim-source pairs; 6 theme families and 3 role bands excluded; bars under 100 claims dropped; values read off the chart, approximate)
- Pricing & billing: Competitor ~10.2%, Earned ~12.3%, Brand ~4.8%, Social ~10.4%
- Eligibility & terms: Earned ~8.6%, Brand ~5.2%, Social ~9.3%
- Rewards & loyalty: Earned ~6.5%, Brand ~4.0%, Social ~4.0%
- Fulfilment, returns & warranty: Earned ~4.9%, Brand ~2.5%, Social ~2.2%

### Inaccuracy rate by model provider — `raw/assets/tryprofound-inaccurate-claims-by-model.png`
(~490,000 model-claim evaluations, Apr–Aug 2026; excludes DeepSeek, Grok, Meta AI, Qwen)
- Microsoft Copilot 6.8%
- Claude 5.7%
- Google Gemini 5.5%
- Google AI Mode 5.2%
- Google AI Overviews 5.0%
- ChatGPT 4.3%
- Perplexity 4.3%
