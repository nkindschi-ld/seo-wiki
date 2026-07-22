# The URL AI Citation Study 2026

Source: https://otterly.ai/blog/url-ai-citations-study/
Author: Rick Tousseyn
Published: May 7, 2026
Categories: AI Search Studies, GEO Experiments

---

## Methodology

- Sample size: 1,028,959 unique URLs generating 1,932,200 citation instances
- Platforms monitored: ChatGPT, Google AI Overviews, Google AI Mode, Perplexity, Gemini, Microsoft Copilot
- Observation period: 24-hour window
- Statistical approach: Pearson correlation coefficient for continuous variables; average citation comparison for categorical attributes

## Key findings

### URL structure correlations (near-zero impact)

All continuous URL attributes showed negligible correlations with citation frequency:
- URL length: r = -0.025
- Domain length: r = -0.007
- Path depth: r = +0.002
- Hyphen count: r = -0.013

Near-zero correlation between URL length and citation count — average cited URLs run 63 characters, yet 40- and 120-character URLs achieve nearly identical citation rates.

### Page type performance (strongest signal)

- Guide pages: 2.7 average citations (42% above baseline of 1.9)
- Blog posts: 2.0 citations (+5%)
- Help pages: 2.0 citations (+5%)
- News: 1.7 citations (-11%)
- Product/Service: 1.6 citations (-16%)
- Pricing pages: 1.5 citations (-21%)

### Query strings impact

- Clean URLs (no query strings): 2.1 average citations
- URLs with query strings: 1.6 average citations
- Effect: 24% reduction in citations

URLs containing digits showed similar patterns (1.6 vs. 2.0 average).

### TLD performance

Most TLDs clustered around 1.5-1.7 citations, except:
- .uk domains: 3.0 average citations (anomaly requiring longer-term validation)
- .com: 1.7 citations (51.3% of sample)
- .org/.io/.ai: 1.7 citations each

### Citation distribution

- Median citations: 1 per URL
- Average citations: 1.9 per URL
- Maximum: 965 citations (single URL)
- Concentration: 15.8% of URLs generated 50% of all citations; 20% generated 54%
- Distribution pattern: power-law/long-tail structure

### Non-predictive elements

These common SEO tactics showed no observable citation lift:
- Year inclusion in URLs
- Question patterns (how-to, what-is)
- Comparison patterns (vs., best-, top-)
- Homepage status

## Primary conclusions

URL structure basics alone do not predict citation frequency in AI Search. Traditional SEO conventions around URL optimization transfer minimally to AI citation contexts. Reference-style content pages (guides, blogs, help documentation) consistently outperform transactional pages, and clean canonical URLs substantially outpace parameter-laden alternatives by approximately 25%.

The heavy concentration of citations among a minority of URLs suggests that structural URL improvements yield limited returns compared to content quality investments.
