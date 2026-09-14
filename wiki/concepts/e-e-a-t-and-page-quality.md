---
type: concept
tags: [seo, aeo]
updated: 2026-09-04
---

# E-E-A-T and Page Quality

The framework Google's human search quality raters use to judge content
quality, per [[google-search-quality-evaluator-guidelines-2025-09]].
Not a ranking algorithm itself, but the canonical definition behind
terms ("E-E-A-T," "YMYL," "helpful, people-first content") used
throughout Google's own guidance (e.g.
[[google-ai-optimization-guide]]) and the wider SEO/AEO industry.

## E-E-A-T: Experience, Expertise, Authoritativeness, Trust

**Trust is the most important member of the family** — everything else
exists to support a Trust assessment, not as independent, separately
weighted scores:

- **Trust**: is the page accurate, honest, safe, and reliable? The type
  and amount of Trust needed depends on the page (an online store needs
  secure payment/customer service; a product review should be honest
  rather than solely sales-driven; a YMYL informational page must be
  accurate to prevent harm).
- **Experience**: does the content creator have first-hand or life
  experience with the topic? (A product review from someone who
  actually used the product vs. someone who didn't.)
- **Expertise**: does the content creator have the necessary knowledge
  or skill? (Electrical rewiring advice from an electrician vs. a
  hobbyist.)
- **Authoritativeness**: is the content creator or website a known
  go-to source for the topic? (An official government page is the
  authoritative source for passport renewal.)

The guidelines are blunt about the hierarchy: "a financial scam is
untrustworthy, even if the content creator is a highly experienced and
expert scammer who is considered the go-to on running scams" — E, E, and
A cannot substitute for Trust. Conflicts of interest undermine
trustworthiness even when experience/expertise is genuine (e.g., a
manufacturer's own "review" of its product, or a paid influencer
promotion).

Raters assess E-E-A-T from three angles: what the site/creator says
about itself (About Us pages), what independent others say (reviews,
news, references), and what's directly visible/verifiable on the page
itself.

## YMYL: Your Money or Your Life

Topics where inaccurate or untrustworthy content could significantly
harm a person's health, financial stability, safety, or the welfare of
society. Four categories: **Health or Safety**, **Financial Security**,
**Government, Civics & Society**, and **Other** harm to people/society's
welfare. YMYL-ness is explicitly a spectrum ("clear YMYL," "may be
YMYL," "not or unlikely YMYL"), not a binary flag — e.g., "evacuation
routes for a tsunami" is clear YMYL, "weather forecast" is not, even
though both are "informational" content.

Notably, first-hand experience can satisfy YMYL trust requirements for
some purposes even on serious topics (e.g., a forum thread of people
sharing coping strategies for a cancer diagnosis can be high E-E-A-T),
while other YMYL purposes require actual expert-sourced information
(e.g., specific treatment options and their outcomes). The distinction
is *purpose*: sharing lived experience vs. giving expert advice.

## Page Quality tiers

Five tiers, assessed after an initial harm/deception screening step
(pages with harmful purpose or deceptive intent are automatically rated
Lowest regardless of other qualities):

- **Lowest**: untrustworthy, deceptive, harmful, or spammy — see abuse
  types below.
- **Low**: beneficial purpose but lacking in an important dimension —
  inadequate effort/originality, distracting ads, mildly negative
  reputation, inadequate E-E-A-T for the purpose.
- **Medium**: has a beneficial purpose and achieves it adequately —
  "there is nothing wrong with Medium quality pages... expect to
  encounter many Medium quality pages."
- **High**: beneficial purpose achieved *well* — high-effort MC, positive
  reputation, high E-E-A-T.
- **Highest**: beneficial purpose achieved *very well* — very high
  effort/originality, very positive reputation, very high E-E-A-T.

Page Quality applies regardless of site type (academic, nonprofit,
government sites can still be rated Low; personal social posts can be
rated Highest) and regardless of monetization ("the presence or absence
of Ads alone is not a consideration").

## The three abuse patterns most relevant to AI-era content

All three trigger an automatic **Lowest** rating:

- **Scaled Content Abuse**: "Using automated tools (generative AI or
  otherwise) as a low-effort way to produce many pages that add
  little-to-no value for website visitors as compared to other pages on
  the web" — explicitly including scraping/synonymizing/translating
  content, stitching pages together, or hiding scaled-content patterns
  across multiple sites. Rated Lowest "no matter how it's created," even
  if raters aren't certain generative AI was used — mere strong suspicion
  of scaled content abuse is sufficient. This is the official policy
  reasoning behind [[ai-visibility-correlation-factors]]'s finding that
  content *volume* has almost no correlation with AI-mention visibility:
  it's not merely that volume doesn't help, low-effort scaled volume is
  an explicit penalty target.
- **Site Reputation Abuse**: third-party content hosted on an
  established site mainly to exploit that host's already-earned ranking
  signals (e.g., a medical site hosting unrelated "best casinos" content
  from a third party). Explicitly does *not* include wire
  services/syndicated news, forums/UGC, genuine editorial/opinion
  content, properly-disclosed advertorial content meant to reach
  readers rather than manipulate rankings, or correctly-handled affiliate
  links.
- **Expired Domain Abuse**: buying an expired, previously-trusted domain
  (e.g. a school, charity, or government site) and repurposing it for
  unrelated, often monetized content that exploits the domain's inherited
  trust/reputation.

## See also

- [[how-google-search-works]] — the technical crawl/index/serve pipeline
  a page must pass through before Page Quality/E-E-A-T assessment is even
  relevant; a page that isn't crawled or indexed never gets rated at all.
- [[search-intent-and-needs-met]] — the companion framework for how
  raters judge query intent and result relevance.
- [[generative-engine-optimization]] — E-E-A-T and Page Quality are the
  retrieval-eligibility foundation this concept's Conflicting Evidence
  section refers to.
- [[google-ai-optimization-guide]] — its "helpful, reliable,
  people-first" language is a direct paraphrase of the E-E-A-T/Page
  Quality framework defined here.
- [[ai-visibility-correlation-factors]] — content-volume correlation
  finding, now explained by the Scaled Content Abuse policy above.
- [[traditional-seo-ranking-factors]] — independent empirical
  confirmation of this framework: reviews/star ratings correlate with
  classic SERP rankings, and the study explicitly ties this to E-E-A-T
  Trust and cites the Search Quality Evaluator Guidelines by name.
- [[seo-copywriting]] — the writing-level playbook for producing
  content that clears this quality bar in practice.
- [[content-pruning-playbook]] — the remediation path for content that
  doesn't clear it: improve, consolidate, noindex, or remove.
- [[geo-content-optimization-tactics]] — how the same
  experience/expertise/sourcing signals are applied for generative
  engines.
