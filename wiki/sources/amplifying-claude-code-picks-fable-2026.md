---
type: source
tags: [aeo]
date_published: 2026-07
date_ingested: 2026-07-22
origin: raw/studies/amplifying-claude-code-picks-fable-2026.md
---

# What Fable Actually Chooses (Amplifying, Jul 2026)

**Citation:** Ong, Edwin and Vikati, Alex. "What Fable Actually
Chooses." Amplifying (agent-intelligence). July 2026.
https://amplifying.ai/research/claude-code-picks-fable/report

## Key takeaways

- Follow-up to [[amplifying-claude-code-picks-2026]] (Feb 2026),
  extending the same 20-category tool-pick methodology to two newer
  models: Opus 4.8 and **Fable 5** (both Jan 2026 training cutoff), vs.
  the earlier Sonnet 4.5/Opus 4.5/Opus 4.6 generation (Aug 2025 cutoff).
  810 tool recommendations, 761 extracted (94%), 4 repo types, 3 runs
  each.
- **Custom/DIY code adoption nearly doubled generation-over-generation**:
  11% (prior study) → 21.4% of Fable 5's picks, with Opus 4.8
  independently landing at 20.5% — read as a generational-capability
  trend, not single-model variance. Sharpest category jumps: Caching
  0%→57%, Observability 12%→42%.
- **"Deferred buy" pattern (new finding):** 32.5% of custom
  implementations explicitly name an upgrade vendor in code comments
  (e.g. a hand-rolled cache documenting "swap to Redis once multiple
  workers exist"). The model builds DIY now but writes the vendor's
  on-ramp into the code itself.
- **Near-monopolies hold**: GitHub Actions and Stripe both still at
  100% pick share in their categories.
- **6 of 20 category winners changed** since the Feb 2026 study
  (Caching, ORM, State Management, Real-time, Background Jobs; Feature
  Flags custom-share rose but didn't change winner) — the fastest
  category churn observed across the wiki's coding-agent-tool-selection
  sources so far.
- **Bundling as a distribution strategy**: PostHog reached 27% share in
  Feature Flags by bundling flags with analytics, beating dedicated
  competitor **LaunchDarkly (0% primary picks, 38% mention rate)** —
  directly relevant to this wiki's operator's own product category.
- **"Lean wins"**: simpler/fewer-dependency tools gained share over
  more full-featured incumbents (Drizzle > Prisma, ARQ > Celery, SSE >
  Socket.io), consistent with a fewer-dependencies model preference.
- **Provider vs. technology split (new framing)**: models separate the
  underlying technology pick (PostgreSQL wins "database") from the
  hosting-provider decision (Neon/Supabase/RDS appear only as
  deployment-time options, not competitors to Postgres itself).

## What this updated in the wiki

- Extended [[ai-coding-agent-tool-selection]] with the generational
  custom-code-adoption trend, the "deferred buy" mechanism, and the
  provider-vs-technology distinction.
- Extended [[optimizing-for-coding-agent-recommendations]] with a
  "deferred buy" tactic (design your interface to match the shape of the
  DIY code a model would otherwise write, so a code comment already
  names you as the upgrade path) and a bundling-as-distribution note.
- No conflicts — reinforces and sharpens the existing build-over-buy and
  recency-gradient findings from [[amplifying-claude-code-picks-2026]]
  and [[amplifying-codex-vs-claude-code-picks-2026]] with a newer model
  generation; the LaunchDarkly/PostHog data point is a specific instance
  of the existing "known but unpicked" pattern already documented on
  [[ai-coding-agent-tool-selection]] (Redux/MongoDB/Prisma), not a new
  mechanism.
