---
type: source
tags: [aeo, seo]
date_published: 2026-07-19
date_ingested: 2026-09-10
origin: raw/studies/ai-assistants-robots-txt-compliance-2026.html
---

# Do Generative AI Assistants Respect robots.txt? Tracing Web Access Beyond Visible Answers

Gabriel Lopez-Fonseca, David Rodriguez, Stefan Bechtold, Jose M. Del
Alamo (Universidad Politécnica de Madrid; ETH Zurich). arXiv:2607.14447,
published 2026-07-19.

## Citation

Gabriel Lopez-Fonseca, David Rodriguez, Stefan Bechtold, Jose M. Del
Alamo, "Do Generative AI Assistants Respect robots.txt? Tracing Web
Access Beyond Visible Answers," arXiv:2607.14447, 2026.

## Key takeaways

- Controlled experiment testing 10 AI assistants with web-search
  capability against dynamically-generated pages containing unique,
  HMAC-validated secret codes, across 4 robots.txt conditions
  (allow-all, disallow-all, assistant-specific allow, assistant-
  specific disallow), 200 trials — server logs distinguish *actual page
  access* from *what the assistant claims/answers*, catching both
  under-compliance and hallucinated answers.
- **Compliance varies substantially by assistant.** Claude and Mistral
  showed the expected allowed/disallowed access pattern (respecting
  robots.txt). DeepSeek, Gemini, Grok, and Qwen accessed
  robots.txt-restricted pages regardless of the disallow rule.
- **Generic user-agents block attribution.** Some assistants exposed
  browser-like user-agent strings (Chrome/Safari) rather than an
  identifiable bot signature, making it impossible for a site owner to
  write assistant-specific robots.txt rules even if they wanted to —
  you can't allow/disallow what you can't identify server-side.
- **Server-side access and the user-visible answer frequently
  diverge.** Copilot accessed all test pages but never returned a
  correct answer (it accessed content it didn't visibly use); ChatGPT
  retrieved nothing in some trials despite the content being fully
  allowed (it answered without accessing). Citation/answer behavior is
  not a reliable proxy for what actually got fetched.
- **Access continues outside the visible interaction.** Follow-up
  monitoring found continued retrieval after the testing window ended
  — Grok alone generated 173+ additional accesses to test pages over
  subsequent weeks, and made 48-52x as many requests to a target page
  per trial as expected, suggesting AI-inference traffic has a
  distinct "hits-the-same-page-repeatedly" load signature, different
  from traditional crawling.
- Authors flag potential EU regulatory exposure: retrieved content
  entering training pipelines without honoring robots.txt/opt-outs
  could implicate the EU Digital Single Market Directive's text-and-
  data-mining exceptions and EU AI Act Article 53 transparency
  obligations.
- Authors' recommendation: don't rely on robots.txt alone for content-
  governance intent at inference time — it's a passive, unenforced
  convention that a meaningful share of assistants ignore. They call
  for automated compliance-auditing frameworks and note interest in
  "cryptographically verifiable web governance protocols" as a
  longer-term alternative to robots.txt's honor-system model.

## What this updated

- New subsection in [[robots-txt-strategy]]: "Empirical AI-assistant
  compliance data," quantifying the wiki's existing "not all crawlers
  respect robots.txt (bad actors, AI crawlers, etc.)" limitation with
  concrete per-assistant evidence.
- Cross-linked from [[robots-txt-audit-checklist]] and the per-LLM
  user-agent table already in [[robots-txt-strategy]].
- No conflicts — this is corroborating empirical evidence for a
  limitation the wiki already stated as a general caveat, now with
  specifics on which assistants comply and which don't.
