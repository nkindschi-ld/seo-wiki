# The Rise of the AI Crawler

Authors: Giacomo Zecchini, Alice Alexandra Moore, Malte Ubl, Ryan Siddle
Publish date: 2024-12-17
Source: https://vercel.com/blog/the-rise-of-the-ai-crawler
Retrieved: 2026-07-23

## Key statistics & traffic data (one month, across Vercel's network)

- GPTBot (ChatGPT): 569 million requests
- Claude: 370 million requests
- AppleBot: 314 million requests
- PerplexityBot: 24.4 million requests
- Googlebot (comparison): 4.5 billion requests

Combined AI crawler traffic ≈ 28% of Googlebot's volume — a significant
presence despite much lower absolute numbers.

## Geographic operations

All measured AI crawlers operate from U.S. data centers only: ChatGPT
uses Des Moines and Phoenix; Claude operates from Columbus. This
contrasts with Google's seven-region distribution strategy.

## JavaScript rendering capabilities

None of the major AI crawlers currently render JavaScript, with two
exceptions. ChatGPT fetches JavaScript files in 11.50% of requests and
Claude in 23.84%, but neither executes the code — client-side rendered
content remains inaccessible to these bots. AppleBot and Gemini are the
exceptions, using browser-based rendering comparable to Googlebot.

## Content type preferences

- ChatGPT prioritizes HTML (57.70% of fetches)
- Claude emphasizes images (35.17% of total fetches)
- Both fetch JavaScript as raw text despite not executing it

## Crawling inefficiencies

- ChatGPT hits 404 errors on 34.82% of requests; Claude on 34.16%
- ChatGPT additionally wastes 14.36% of requests following redirects
- Googlebot, by contrast: only 8.22% 404 rate and 1.49% redirect rate

## Recommendations for site owners

**To enable crawling:**
- Implement server-side rendering for critical content
- Reserve client-side rendering for non-essential features
- Maintain updated sitemaps and consistent URL structures

**To prevent crawling:**
- Configure `robots.txt` with appropriate user-agent rules
- Employ firewall/blocking tools (e.g. Vercel's AI Bot rules)
