---
name: plan-change
description: Produces an implementation-ready design for non-trivial Rails and React work. Use for plans, design choices, migrations, jobs, API changes, security-sensitive work, or changes that cross Rails and React.
---

# Plan a change

A plan must let another engineer implement the change without guessing.

Slice vertically. Each task is one user-visible capability cut through every layer it needs, with its own proof.

## Ground the plan

1. Read the ticket and acceptance criteria.
2. Read repository instructions, relevant code, tests, configuration, and history.
3. Check linked meeting, Slack, document, and customer context when it can change the design.
4. State the current behavior and the required outcome.
5. Name the data shape, invariants, tenant boundary, authorization model, and shipped contracts.

## Evaluate the design

1. Confirm that a change is required.
2. Check the standard library, Rails, the platform, and installed dependencies.
3. Identify the smallest coherent design that fits existing ownership.
4. Compare alternatives only when they have a material tradeoff.
5. Cut unrequested features.
6. Ask the human before a non-obvious architecture, security, data, or compatibility decision.

If the work covers independent subsystems, write separate plans. Each plan must produce working, testable software.

## Write vertical slices

A slice is shippable on its own, testable on its own, and described as something a person can do.

Fold a migration, model, component, or serializer into the first slice that uses it. If shared groundwork cannot fold, make the thinnest increment that still has a test.

For each slice, name the capability, the files it touches, the auth and error behavior, contract impact, and the check that proves it. Add job, migration, and UI notes only when that slice changes those surfaces.

Write intent-level steps. Include exact code only for migrations, destructive data work, or non-obvious configuration.

Load matching `build-change` references by name. Leave their content in those files.

## End with delivery risk

State schema, jobs, operations, deploy, observability, rollback, customer and tenant risk, and open decisions.

Include follow-up work only when the current change knowingly creates it.
