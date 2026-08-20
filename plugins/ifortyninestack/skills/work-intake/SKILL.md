---
name: work-intake
description: Reads, creates, or updates Linear issues and prepares an execution contract. Use for tickets, ENG or DEV issue IDs, cycle planning, work intake, acceptance criteria, or issue status changes.
---

# Work intake

Use the Linear MCP for all Linear reads and writes. Do not use API keys, direct GraphQL, browser scraping, or application credentials as a fallback.

If Linear is not installed, use GitHub Issues and still apply the required issue content in [linear-protocol.md](linear-protocol.md). Skip cycle-tracking labels on GitHub Issues.

## Read an existing issue

1. Discover the Linear MCP schema.
2. Read the issue, comments, relations, attachments, project, cycle, labels, and linked context that affect the work.
3. Read linked Slack threads, documents, meetings, and pull requests when they contain requirements or decisions.
4. Return an execution brief with the problem, acceptance criteria, constraints, scope, dependencies, customer impact, and deploy constraints.
5. Separate explicit requirements from inference and unresolved questions.

## Create or update an issue

1. Confirm the Linear team. Use the team's ticket prefix. Common prefixes are `ENG` and `DEV`. Do not invent a prefix.
2. Write an action-plus-object title.
3. Include the problem, constraints, acceptance criteria, links, scope, and known test or deploy notes.
4. Use Linear relationships for blockers. Do not hide dependencies in prose.
5. Apply the rules in [linear-protocol.md](linear-protocol.md).
6. Preserve unrelated labels and fields unless the user asks to change them.
7. Read the saved issue after the write and confirm the final state.

## Before implementation

Ordinary implementation work requires a ticket unless the human explicitly approves an exception. Read-only investigation and trivial local commands do not require one.

If an urgent customer-impacting fix has no ticket, state what is missing, keep the work narrow, and record that a ticket or link is still required.

## Authentication failure

If the Linear MCP needs authentication, stop the Linear operation. Ask the user to authenticate the Linear integration in Cursor. Do not use a credentials workaround.
