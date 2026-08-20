# Ifortyninestack architecture

## Goal

Ifortyninestack gives a Rails and React engineer one installable workflow for the software development lifecycle. It ships Linear, Heroku, and conventional-commit opinions. It must improve agent decisions without filling every session with unrelated instructions.

## Layers

### Always-on rules

`engineering-baseline.mdc` defines investigation, scope, simplicity, testing, evidence, the merge-ready quality bar, and merge authority.

`public-trust-and-safety.mdc` defines customer, tenant, data, security, deploy, and human-approval boundaries.

`communication.mdc` defines the default writing style. Titles, commits, comments, and pull request bodies name what landed.

### File-scoped rules

These rules load only when matching files are relevant:

- Ruby and Rails.
- React, TypeScript, and Inertia.
- Tests.
- Background jobs.
- Migrations and schema.

### Skills

`ifortyninestack-mode` routes the request to one phase:

1. `work-intake`
2. `understand-system`
3. `plan-change`
4. `build-change` or `fix-bug`
5. `deslop` when the change needs a cleanup pass on agent-generated code
6. `verify-change`
7. `review-change`
8. `open-pr`
9. `maintain-pr`

`plan-change` writes vertical slices. Each slice is one user-visible capability with its own proof. Intent-level steps are the default. Exact code is reserved for migrations and other fragile operations.

`deslop` cleans generated code in the working tree. `review-change` reports findings. `fix-bug` starts from a reproduction.

`review-decide-address-loop` is a human-gated PR improvement cycle. `review-inline-comments` publishes inline GitHub feedback. `address-senior-review` handles existing human review with separate approval for code, replies, and resolutions.

Environment operations, incident response, technical writing, plain-language rewriting, setup, and learning capture are separate workflows.

### Agents

Review work uses independent lenses:

- Product intent and contracts.
- Production safety.
- Maintainability.

The lead agent validates and combines findings. Review agents do not edit code.

Default `review-change` uses a merge-ready bar. Blocker and Important items must be fixed before merge. Notes are watchlist only. A small valid fix stays Important. Implementation cost is not a reason to demote a finding. Making the change easy for a human to inspect is not the quality bar. A human still decides when to merge.

The CI watcher reports state and the first actionable failure. It does not rerun jobs or change code.

## Source-of-truth order

Use this order when guidance conflicts:

1. Current user instruction.
2. Current repository instructions and executable configuration.
3. Current ticket and linked decisions.
4. Ifortyninestack safety rules.
5. Ifortyninestack task skills and file-scoped rules.

The repository remains the source of truth for runtime versions, commands, exclusions, architecture, and local credentials.

## Boundaries

Cursor integrations provide Linear, Slack, Granola, GitHub, and other source systems. Ifortyninestack does not ship an MCP server. Linear is the assumed issue tracker. Heroku is the assumed deploy platform. Slack and Granola are optional.

Hooks for formatting, command blocking, and external writes stay out of the plugin. They need repository-specific design.

A human decides merge and deploy.
