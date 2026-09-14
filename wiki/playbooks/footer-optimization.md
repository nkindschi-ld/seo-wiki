---
type: playbook
tags: [seo]
updated: 2026-09-06
---

# Footer Optimization

Why/when to use this: the footer is a sitewide template surface that
most organizations don't defend politically, making it unusually cheap
to change. Work on it when you're polishing the **"last 20%"** of a site
whose fundamentals are already solid, when you're diagnosing **crawl
rate or crawl depth** problems, or when analytics show a meaningful
share of users scrolling to the bottom of your pages
([[growth-memo-show-me-your-footer]]). Do **not** treat it as a primary
growth lever — see "Expected impact" below.

Based on [[growth-memo-show-me-your-footer]],
[[seoptimer-website-footer-seo]] and
[[heydaymarketing-footer-optimization]]. Complements
[[link-and-anchor-text-best-practices]] (which owns internal-link
mechanics generally) and [[technical-seo-audit-checklist]] (navigation).

## Expected impact — set this expectation first

Kevin Indig's framing is the honest one: **low impact, but not no
impact.** Footer links will not double organic traffic. The case for
doing the work is that it is cheap, low-risk, improves UX, and is
politically easy to ship — "less about the *why?* and more about the
*why not?*"

The plausible mechanism is **crawl, not ranking weight**: a page linked
from every page (including the homepage) gets crawled more often, and
more-frequently-crawled pages tend to coincide with better-ranking pages
(see [[how-google-search-works]]). At G2, footer optimization "boosted
our crawl rate, and our ranks climbed over time" — but the incremental
organic traffic was never isolated, and Indig says so. Treat that as
directional, not measured.

Two supporting facts worth having in the room when you pitch this:

- **Google says it doesn't discount footer links.** John Mueller (2023):
  "It's not the case that we would say, Oh, like links in a footer have
  less weight… we essentially just see them as links on a page." This is
  in tension with the older reasonable-surfer model — see "Conflicting
  Evidence."
- **Users do reach footers** (Nielsen Norman Group). Scrolling to the
  bottom signals *interest*, so the footer is a high-intent, low-
  aggression placement surface rather than dead space.

## 1. Claim ownership of the footer

Organizational step, and the one that actually unblocks the rest. SEO
teams should explicitly own the footer template. It is also the standard
workaround when design/product blocks changes to the **top navigation** —
the footer gives you a sitewide link surface you can actually ship
changes to.

## 2. Choose a layout

- **Fat footer** — the default for content-rich or large sites.
- **Double footer** — two stacked bands (e.g. a wide link grid plus a
  legal/utility strip).
- **Slim + fat combination** — a compact bar above the main footer for
  high-priority items.
- **Dropdowns / accordions** — when you must compress a long link list,
  particularly on mobile.
- **Headings for every column** — non-negotiable for scannability.
- **Contextual footers** — vary the footer by site section. Atlassian
  runs a different footer on its Agile microsite than on the main site.

## 3. Decide what to link

The single most common footer mistake is a footer containing **only
utility links**. Spend the surface deliberately:

- Important pages **not already linked in the top nav** (avoid
  duplicating top-nav links — you're wasting the slot).
- Moneymaker blog articles and guides.
- Sub-categories.
- Tools, calculators, templates.
- Comparison / "alternatives" pages (several of the best-in-class
  examples do this — see [[saas-seo-strategy]]).
- Sibling brands within the organization.
- An **HTML sitemap**.
- Utility links: contact, about, terms of service, privacy policy.
- **"Secondary tasks"** (NN/g's term): careers, investor relations,
  product documentation, media kits / PR, newsletter signup, social
  profiles. Consider limiting social links to the homepage rather than
  sitewide.

Anchor text: descriptive and specific, never "click here" / "read more"
— same rules as [[link-and-anchor-text-best-practices]].

## 4. Structure it visually

- Divide into **at least three sections** (e.g. company / services /
  contact) — the sectioning itself communicates site structure.
- **"New" / "Popular" labels** on individual links.
- **Icons** to make long lists parseable.
- **Testimonials, awards, trust badges.**
- Consistent **brand treatment**: site theme colors, logo, same font
  family. Use type-size contrast for hierarchy (larger CTA, smaller
  copyright).

## 5. One CTA, and make it generic

Because the footer renders on every page, a page-specific CTA (a product
demo link) will be wrong on most of them. Pick **one** generic CTA —
newsletter signup is the canonical choice — make it visually prominent,
and let users complete it **in the footer itself** (an inline form, not
a link to a form).

## 6. Must-have elements

- **Copyright notice** — generate the year in code so it never goes
  stale.
- **Contact information** — address, phone, email; optionally an inline
  contact form. Track phone-click events; that's a measurable footer
  signal.
- **Legal** — privacy policy, terms of service, disclaimers.
- **Trust/commerce signals** — SSL/security badge, accepted payment
  methods for ecommerce, and industry credentials where they're real
  (BBB accreditation, Google/GSA certifications). Overlaps with the
  Trust leg of [[e-e-a-t-and-page-quality]].
- **Back-to-top button** on long-form pages.

## 7. Local SEO in the footer

For businesses with physical locations:

- Full **NAP** (name, address, phone) consistent with your other
  listings.
- Map embed and a link to the **Google Business Profile**.
- **But**: above roughly three locations, link to a dedicated locations
  page instead of listing every address in the footer. A footer listing
  10 office addresses is the canonical bad example.

## 8. Schema markup

The footer already contains the data that `Organization` /
`LocalBusiness` structured data wants — so mark it up: contact
information, business hours, and social profiles as `sameAs`. See
[[entity-based-seo-implementation]] for the entity/`sameAs` rationale.

## 9. Mobile

Test the **collapsed/stacked** footer on real devices, not just a
resized desktop viewport. Footers are one of the main reasons mobile
navigation works at all — reaching the top nav from the bottom of a long
page is a long scroll — so a footer that breaks on mobile costs more
than it does on desktop. Watch for fixed elements (live chat widgets,
cookie bars, back-to-top buttons) colliding with footer controls.

## 10. Maintain it

The footer is sitewide, so a broken link there is broken everywhere. On
a recurring cadence:

- Crawl for 404s among footer links.
- Refresh contact details, hours, and the CTA offer.
- Add links for new important sections; remove links to pruned pages
  (see [[content-pruning-playbook]]).
- Re-check that footer links still aren't duplicating the top nav after
  navigation changes.

## Anti-patterns

- **Utility-links-only footers** — the most common failure.
- **Duplicating the top navigation** — spends a sitewide slot on pages
  that already have one.
- **Hidden text or hidden links** — a spam technique with real penalty
  risk, not a clever trick.
- **Keyword-stuffing the footer.** [[heydaymarketing-footer-optimization]]
  explicitly advises seeding commercial keywords ("SEO company," "SEO
  agency") into footer copy while, two sentences earlier, warning
  against stuffing. That advice is **deliberately not carried into this
  playbook.** Descriptive anchor text on genuinely useful links is the
  legitimate version of the same idea.
- **Listing every location** rather than linking a locations page.
- **Two or more competing CTAs** in a sitewide footer.

## Conflicting Evidence

- **Claim**: how many links a footer should carry.
  - Supported by (more is fine): [[growth-memo-show-me-your-footer]]
    (2023-07-31) — "good footers are fat but not obese… there is no
    downside to feeding your footer to a certain limit," provided
    PageRank and **CheiRank** stay roughly in balance. Argues that
    "large footers are bad UX" is an unproven assertion and that rigid
    organization, not link scarcity, prevents overwhelm.
  - Contradicted by: [[seoptimer-website-footer-seo]] (2019-10-01) —
    "simplicity is the best way forward," include only primary links;
    and [[heydaymarketing-footer-optimization]] (2024-05-23) —
    "overloading with links can dilute link equity."
  - **Current best guess**: lean Indig, consistent with the wiki's
    existing resolution on internal link counts in
    [[link-and-anchor-text-best-practices]] (defer to Google's "no
    magical ideal number"). Neither opposing source offers data, and the
    equity-dilution argument they use is the same simplified
    PageRank-dilution reasoning the wiki already declined to adopt as a
    numeric rule. The real constraint is **organization and scannability
    rather than count** — a well-sectioned 60-link footer beats an
    unstructured 20-link one. Unresolved to the extent that no source
    provides a measured UX or ranking outcome either way.

- The footer/boilerplate **link-weight** conflict (Mueller's "we don't
  differentiate" vs. the reasonable-surfer placement hierarchy) is
  recorded on [[link-and-anchor-text-best-practices]], which owns the
  placement guidance.

## See also

- [[link-and-anchor-text-best-practices]] — internal-link mechanics,
  anchor text rules, and the reasonable-surfer placement conflict.
- [[technical-seo-audit-checklist]] — navigation and crawlability
  auditing this playbook feeds into.
- [[how-google-search-works]] — the crawl-frequency mechanism behind the
  claimed benefit.
- [[xml-sitemap-optimization-checklist]] — the machine-readable
  counterpart to the HTML sitemap link in the footer.
- [[saas-seo-strategy]] — mega-menu/architecture guidance and the
  comparison-page patterns several exemplar footers link to.
- [[entity-based-seo-implementation]] — `Organization`/`sameAs` schema
  for the footer's contact and social data.
