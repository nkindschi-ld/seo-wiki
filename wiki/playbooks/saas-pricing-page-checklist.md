---
type: playbook
tags: [seo, aeo]
updated: 2026-11-04
---

# SaaS Pricing Page Checklist

**Why / when to use this:** use this when building, redesigning or
reviewing `/pricing` itself: what goes on the page, how it ranks for
pricing searches, how AI systems can read it, and how to mark it up.
For what AI answers *say* about your pricing and how to fix it off-page,
use [[ai-pricing-visibility-audit]]. The two link to each other: this
page is the on-page half of that audit's "answer stack".

Concepts: [[structured-data-and-ai-search]],
[[search-intent-and-needs-met]] (pricing searches are BoFu intent),
[[ai-shortlist-effect]] (accurate pricing affects selection).

## 1. Page structure

Technotize's four zones ([[technotize-pricing-page-seo-b2b-saas-2026]]),
with the layout detail from [[schematic-saas-pricing-page-examples-2026]]:

1. **Top section:** H1 with product name + "pricing" or "plans"; a
   one-line value statement whose sub-line names the pricing model (free
   plan, per seat, usage-based).
2. **Plans and comparison:** 3–4 plans side by side, one marked
   recommended; monthly/annual toggle with the saving shown in currency;
   key features on the cards and a full comparison table below.
3. **Trust and conversion:** logos, testimonials, compliance badges,
   trial terms, CTAs.
4. **Link hub:** contextual links to comparison and alternatives pages,
   billing docs, feature pages, case studies, calculators.

**Don't over-optimize.** No long-form SEO copy on `/pricing`. Build the
SEO surface around it (comparison, alternatives, category pages, billing
docs). Pricing pages are a weak citation page type on their own
([[ai-pricing-visibility-audit]]).

## 2. Search targeting

Four pricing query types ([[technotize-pricing-page-seo-b2b-saas-2026]]):

- **Branded:** "[product] pricing", "[product] cost". `/pricing` should
  own these.
- **Category:** "[category] pricing". Usually needs a category page or
  comparison content too.
- **Competitor:** "[competitor] pricing alternatives". Needs
  alternatives/comparison pages ([[saas-seo-strategy]]).
- **Tier:** "[product] enterprise pricing". Needs tier detail on the page
  or a supporting FAQ/doc.

**Two-way links:** every comparison page links to `/pricing` after the
comparison and before the CTA; `/pricing` links to the top comparison
pages with contextual anchors ("See how we compare to [Competitor]").
See [[link-and-anchor-text-best-practices]]. One `/pricing` URL per
product line; avoid near-duplicate plan pages
([[keyword-mapping-and-cannibalization]]).

## 3. Content that answers the buyer (and the AI)

These are the details AI engines cite most and invent when missing
([[ai-pricing-visibility-audit]] steps 4–5), and the ones buyers bounce
over ([[storylane-saas-pricing-page-design-2026]]):

- [ ] At least one concrete price or "starts at" figure is visible. If
      enterprise is custom, say what's custom and give a starting signal
      if deal sizes allow. Not every tier "Contact us".
- [ ] **Every usage unit defined in the buyer's words** (what counts as a
      seat, MAU, task, outcome; what isn't charged). Intercom's
      per-outcome definition is the model.
- [ ] **Overage behaviour stated:** what happens past a limit (blocked,
      billed at $X, alert first).
- [ ] Monthly price visible, not only the annual figure behind a toggle.
- [ ] Billing cadence and contract length stated separately in visible
      text. (Schema has no clear property for payment frequency; see §5.)
- [ ] **No misleading starting price:** if a feature typical buyers need
      (SSO, audit logs) sits on a higher tier, show it on the cards.
- [ ] Currency and tax: local currency switch, whether VAT/sales tax is
      included, regional availability of plans or data residency.
- [ ] Pricing FAQ in visible text covering: after the trial, cancel or
      downgrade, hidden fees, tier limits, monthly vs. yearly billing,
      support included. Answers resolve doubts rather than repeat the
      table.
- [ ] Links to billing docs that cover the edge cases (Supabase links
      features to docs; Plaid's billing docs out-cite its pricing page).
- [ ] Visible "last updated" date; upcoming price changes shown ahead.

## 4. Crawlability

- [ ] **All prices are in the initial HTML.** No JS-only tables, no
      prices only behind tabs, sliders or calculators, no iframes. Test
      with `curl` or JS disabled ([[ai-pricing-visibility-audit]] step
      3, [[technical-seo-audit-checklist]]).
- [ ] `/pricing` and billing docs not blocked in robots.txt
      ([[robots-txt-audit-checklist]]).
- [ ] Mobile: comparison table collapses usably; toggles and tier
      selectors work by keyboard and screen reader (WCAG 2.2).

## 5. Structured data

**Set expectations:** markup on a pricing page is a consistency and
eligibility layer, not an AI-citation lever, and a price that exists
only in JSON-LD isn't reliably read by AI systems
([[structured-data-and-ai-search]]). Do §3 and §4 first.

Type choice ([[coreaex-saas-pricing-schema-2026]]):

- `SoftwareApplication` (a `CreativeWork`, not a `Product`) for a
  software product; `Product` is defensible too since its definition
  covers services. Pick one, use it consistently across the site, and
  give it a stable `@id`.
- **One `Offer` per plan** (name, URL, `price`, `priceCurrency`) rather
  than one `AggregateOffer` low/high range, so each plan's terms survive.
- Per-seat or usage rates: `priceSpecification` →
  `UnitPriceSpecification` with `unitText` / `referenceQuantity`
  ([[storylane-saas-pricing-page-design-2026]]).
- `billingDuration` = how long the price applies (the term), **not** the
  payment cadence. It and `billingStart`/`priceType` are "new" in
  Schema.org v30.0, and Google doesn't document consuming them.
- **Enterprise / custom tier: an Offer with no `price`**, and the
  custom terms in `description`. Never a placeholder 0.
- **Software App rich result needs `aggregateRating` or `review`.** If
  your ratings live on G2 and not on the page, you aren't eligible.
  Accept it; don't mark up third-party ratings you don't display or
  write your own reviews.
- `FAQPage` only as a word-for-word mirror of a visible pricing FAQ. No
  rich result for SaaS sites (Google, 2023). Update it whenever billing,
  cancellation or unit answers change.
- `BreadcrumbList` and a page-specific `WebPage` are low-risk additions.

Minimal pattern (illustrative):

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "@id": "https://example.com/#software",
  "name": "ExampleApp",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Web",
  "offers": [
    { "@type": "Offer", "name": "Free", "price": "0", "priceCurrency": "USD",
      "url": "https://example.com/pricing#free" },
    { "@type": "Offer", "name": "Pro", "priceCurrency": "USD",
      "url": "https://example.com/pricing#pro",
      "priceSpecification": { "@type": "UnitPriceSpecification",
        "price": "12", "priceCurrency": "USD",
        "unitText": "per seat per month" } },
    { "@type": "Offer", "name": "Enterprise",
      "url": "https://example.com/pricing#enterprise",
      "description": "Custom pricing; annual contract." }
  ]
}
```

Keeping it true:

- [ ] Visible prices and markup generated from **one pricing source**
      (CMS field or pricing config), so a price change updates both.
- [ ] Four separate checks after every pricing release: markup parses
      (Schema Markup Validator); meets the feature's requirements (Rich
      Results Test); the rendered page contains it; values match the
      visible page.
- [ ] Resolve any on-page price contradiction **before** marking anything
      up. Markup can't fix two visible prices disagreeing.

## 6. Measurement

- Organic: GSC clicks/impressions on the four query types; branded
  pricing rank.
- Conversion: pricing-page conversion by source; set your own baseline
  (published pricing-page benchmarks rarely show sources, per
  [[storylane-saas-pricing-page-design-2026]]).
- AI: the baseline in [[ai-pricing-visibility-audit]] step 1, checking
  **fact accuracy**, not just citation.
- Know the GSC limits: rich-result reports show validity, not
  appearance; the Generative AI report is AIO + AI Mode impressions only
  ([[coreaex-saas-pricing-schema-2026]]).

## Worked example: launchdarkly.com/pricing (query, 2026-10-27)

From a wiki query logged 2026-10-27, checked against the live page. The
page emitted no JSON-LD at all. The recommendation:

- a page-specific `WebPage` and `BreadcrumbList`;
- the shared `#software` `SoftwareApplication` with `offers`:
  - Developer at $0;
  - Foundation as `UnitPriceSpecification`s (per service connection,
    per 1K client-side MAU, per 1K AI runs);
  - Enterprise as a priceless "custom pricing" Offer;
- `FAQPage` only once pricing FAQs are on the page;
- no `aggregateRating`/`review`, since the ratings are third-party G2.
  So no Software App rich result, and the Offer markup is a
  comprehension aid only.

A $8.33-vs-$10 MAU contradiction on the page had to be fixed before any
price went into markup. CoreAEX's evidence (visible text wins every
conflict; JSON-LD-only prices aren't read) supports fixing visible copy
first.

## Related

- [[ai-pricing-visibility-audit]] — the off-page / AI-answer half.
- [[structured-data-and-ai-search]] — evidence behind §5.
- [[saas-seo-strategy]] — BoFu page types, alternatives pages.
- [[technical-seo-audit-checklist]] — JS rendering and crawler checks.
- [[ai-shortlist-effect]] — why pricing accuracy changes selection.
