# How to Write Great agents.md Files: Analysis of 2,500+ Repositories

**Author:** Matt Nigh (@mattnigh)
**Published:** November 19, 2025 (Updated November 25, 2025)
**Platform:** GitHub Blog
**Category:** AI & ML / GitHub Copilot
**URL:** https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/

---

## Overview

This article synthesizes findings from analyzing over 2,500 `agents.md` files across public repositories to identify patterns that distinguish successful custom AI agents from ineffective ones. The core insight: successful agent definitions combine specific personas, exact executable commands, concrete code examples, and clear operational boundaries.

---

## Key Statistics & Findings

- **2,500+ repositories** analyzed to identify patterns in agent file usage
- **Clear divide observed** between vague agents that fail and specialist agents that succeed
- **Six core areas** identified as essential for top-tier agent performance

---

## What Makes Effective agents.md Files

### The Core Problem
Most agent files fail because they're insufficiently specific. Generic statements like "helpful coding assistant" lack the precision needed for effective AI guidance.

### Five Distinguishing Characteristics

1. **Commands positioned prominently**: Include specific, executable commands with flags and options (e.g., `npm test`, `pytest -v`), not just tool names

2. **Code examples over descriptions**: Single real code snippet demonstrating style proves more effective than lengthy explanations

3. **Explicit boundaries**: Clearly state what agents should never modify—secrets, vendor directories, production configurations, or specific folders. "Never commit secrets" emerged as the most commonly beneficial constraint.

4. **Specific technology descriptions**: Rather than stating "React project," specify "React 18 with TypeScript, Vite, and Tailwind CSS" including versions and key dependencies

5. **Coverage of six essential areas**:
   - Commands
   - Testing practices
   - Project structure
   - Code style
   - Git workflow
   - Operational boundaries

---

## Real Example: docs-agent

The article provides a template demonstrating how effective agents combine:
- Clear role definition and required skills
- Executable build and validation commands
- Specific tech stack and file locations
- Real code examples
- Three-tier boundary system (always do/ask first/never do)

---

## Six Recommended Agent Types

### 1. @docs-agent
Converts code into API documentation and tutorials. Command examples: `npm run docs:build`, `markdownlint docs/`. Boundary: writes only to `docs/`, never touches `src/`.

### 2. @test-agent
Writes unit and integration tests. Critical boundary: can write tests but "never remove failing tests unless authorized by user."

### 3. @lint-agent
Enforces code style and formatting safely. Commands: `npm run lint --fix`, `prettier --write`. Low-risk since linters are inherently safe.

### 4. @api-agent
Builds API endpoints using specified frameworks. Can modify routes but should ask before schema changes.

### 5. @dev-deploy-agent
Handles local/development builds and deployments. Tightly constrained: "only deploy to dev, require user approval for anything with risk."

### 6. Additional Consideration
The article doesn't mandate these six as exhaustive; organizations should identify their own specialized needs.

---

## Implementation Strategy

### Starting Simple
Rather than comprehensive initial planning, the recommended approach:
- Pick one specific task
- Define three essentials: agent name, description, persona
- Test and iterate

The article notes: "The best agent files grow through iteration, not upfront planning."

### Using Copilot for Generation
Users can prompt GitHub Copilot to generate initial `agents.md` files by specifying requirements like testing focus, directory restrictions, and modification boundaries.

---

## Starter Template Structure

The article provides a minimal template including:
- YAML frontmatter (name, description)
- Persona section with specialization and output focus
- Project knowledge (tech stack, file structure)
- Tools/commands section
- Standards and code style examples
- Three-tier boundary framework

---

## Common Mistakes Avoided by Successful Files

Implied from the analysis:
- Vague role descriptions without specific expertise areas
- Missing executable commands
- Absent or unclear file/directory restrictions
- No code style examples
- Unstructured or missing boundaries
- Generic technology descriptions

---

## Key Takeaway

Effective `agents.md` files function as detailed operating manuals combining "a specific persona and clear instructions." Success requires executable commands, concrete examples, explicit boundaries, and tech stack specificity rather than upfront comprehensive planning.
