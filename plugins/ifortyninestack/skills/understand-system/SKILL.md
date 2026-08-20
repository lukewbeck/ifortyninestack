---
name: understand-system
description: Explains how code works, where behavior belongs, and why a design exists. Use for code walkthroughs, architecture questions, ownership questions, design history, regressions, or meeting-informed decisions.
---

# Understand the system

Answer from evidence. Do not infer intent from code structure alone.

## How the system works

1. Identify the entry point, data shape, and requested outcome.
2. Trace the runtime path from input to output or trigger to effect.
3. Read the callers, callees, types, persistence, configuration, tests, and external boundaries on that path.
4. For a broad subsystem, split exploration by independent concerns and run the searches in parallel.
5. Explain the key components, flow, ownership, contracts, and non-obvious behavior.

## Why the system has this shape

1. Anchor the question to files, symbols, lines, commits, and pull requests.
2. Inspect source history and review discussion.
3. Discover relevant MCP sources. Search Linear, Slack, Granola, long-form documents, observability, and error tracking when available and relevant.
4. Treat meeting notes and chat as evidence, not as a replacement for the code that shipped.
5. Report direct evidence, reasonable inference, competing explanations, and gaps separately.

## Output

Use only the sections that help:

- Outcome.
- Runtime flow.
- Ownership and file map.
- Contracts and invariants.
- Design rationale.
- Risks or gotchas.
- Evidence and confidence.

Use exact file paths, symbols, ticket IDs, commit hashes, pull request links, and source links. Never invent a citation.
