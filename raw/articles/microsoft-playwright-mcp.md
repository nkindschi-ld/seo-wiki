# microsoft/playwright-mcp (GitHub repo README)

Owner: Microsoft
Source: https://github.com/microsoft/playwright-mcp
Status: living open-source project
Captured: 2026-08-06 (WebFetch extraction of README)

---

## What it is

A Model Context Protocol (MCP) server that enables LLMs / AI agents to
automate web browser interactions. Designed for agentic workflows, not
just traditional test automation.

## Core innovation: accessibility trees over screenshots

Key claims (verbatim):
- "Uses Playwright's accessibility tree, not pixel-based input"
- "No vision models needed, operates purely on structured data"

Rather than requiring vision models to interpret screenshots, Playwright
MCP gives agents structured **accessibility snapshots** — hierarchical
representations of page content and interactive elements — enabling
deterministic navigation/interaction without visual processing. Agents
perceive pages through element roles, accessible names, and interactive
state, not visual renderings.

## Problem it solves

- Reduces token consumption vs screenshot-based approaches.
- Eliminates need for multimodal vision capabilities.
- Deterministic, unambiguous element targeting.
- Enables "exploratory automation, self-healing tests, or long-running
  autonomous workflows."

## Tool exposure

Exposes 60+ tools: core automation (click/type/navigate/form-fill),
network mocking, storage management (cookies/localStorage/sessionStorage),
tab management, DevTools capabilities (tracing/video/highlighting), and
optional coordinate-based (pixel) actions as a fallback vision capability.

## Technical details

Maintains persistent browser state; configurable with authentication,
device emulation, and custom init scripts.

---

## Notable for the wiki

Concrete, production tooling embodying the thesis that AI agents read the
**accessibility tree**, not pixels — the mechanism behind the
optimize-your-accessibility-tree SEO guidance and OpenAI's ChatGPT Atlas
ARIA behavior. A page whose interactive elements are missing roles/
accessible names is effectively invisible/inoperable to an accessibility-
snapshot-based agent, regardless of how it looks.
