# What Fable Actually Chooses (Amplifying, Jul 2026)

**Authors:** Edwin Ong & Alex Vikati
**Publisher:** Amplifying / agent-intelligence
**Date:** July 2026
**Prior study:** February 2026 (three-model edition) —
[[amplifying-claude-code-picks-2026]]
**URL:** https://amplifying.ai/research/claude-code-picks-fable/report

## Methodology

- **Sample size:** 810 tool recommendations across 4 greenfield
  repositories; 761 picks successfully extracted (94% extraction rate).
- **Test parameters:** 3 runs per repository, 20 tool categories, 4
  project types (nextjs-saas, react-spa, python-api, node-cli). No
  prompt named a specific tool.
- **Models tested:** Sonnet 4.5, Opus 4.5, Opus 4.6 (all Aug 2025
  training cutoff), Opus 4.8, and Fable 5 (both Jan 2026 cutoff).

## Key findings

- **Custom code adoption roughly doubled across one model generation.**
  21.4% of Fable 5's picks are custom code — the #1 answer overall — up
  from 11% two generations prior. Opus 4.8 (same training cutoff as
  Fable) independently reached 20.5%, suggesting this is a generational
  capability trend, not one model's individual quirk.
- **Category-specific custom-code jumps:** Caching 0%→57%, Observability
  12%→42%, Authentication 52%→64%, Feature Flags 66%→71% (Sonnet 4.5 →
  Fable 5).
- **Near-monopolies persist:** GitHub Actions 100% (55/55 CI/CD picks),
  Stripe 100% (21/21 payments picks).
- **Six categories changed winners** between the Feb 2026 study and this
  one: Caching (Redis 42% → Custom/DIY 57%), Feature Flags (Custom 69%→
  71%, incumbent held), ORM (SQLModel 35% → Drizzle 45%), State
  Management (Zustand → TanStack Query), Real-time (Custom → SSE 40%),
  Background Jobs (BullMQ → ARQ 29%).
- **"Deferred buy" pattern:** 32.5% of custom implementations (53/163
  builds) explicitly named an upgrade vendor in code comments — e.g. a
  hand-rolled cache documenting "swap to Redis once multiple workers
  exist." The model builds DIY now but pre-writes the vendor's on-ramp.
- **Stack-specific defaults:** Next.js SaaS — Vercel deploy 100%, Drizzle
  ORM 93%, Resend email 86%. Python API — pytest 100%, FastAPI 100%, DIY
  SMTP 60%. React SPA — Mantine UI 100%, TanStack Query 67% state, DIY
  localStorage auth 60%.
- **"Known but not chosen" tools, with mention-vs-pick gap:** Redis 21%
  picked / 75% mentioned (named as swap target); Prisma 0% picked / 40%
  mentioned; SendGrid 0% picked / 55% mentioned; **LaunchDarkly 0%
  picked / 38% mentioned** in feature flags.
- **Bundling as distribution:** PostHog reached 27% share in feature
  flags by bundling flags with analytics — beating dedicated competitor
  LaunchDarkly (0% primary picks despite the 38% mention rate above).
- **"Lean wins":** tools that simplify an existing category gained share
  over more full-featured incumbents — Drizzle over Prisma, ARQ over
  Celery, SSE over Socket.io — consistent with a model preference for
  fewer dependencies.
- **Provider vs. technology split:** models distinguish the underlying
  technology (PostgreSQL wins database-technology choice) from the
  hosting provider (Neon/Supabase/RDS appear as deployment-time options,
  not competing "primary picks" against Postgres itself).

## Conclusion (source's framing)

Newer Claude models increasingly build rather than buy, but strategically
name vendors as documented upgrade paths inside the DIY code itself —
creating a "deferred sales" opportunity for infrastructure vendors whose
interfaces are designed to match the shape of the hand-rolled
alternative a model would otherwise write.
