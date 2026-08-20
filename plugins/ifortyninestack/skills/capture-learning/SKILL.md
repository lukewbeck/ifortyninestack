---
name: capture-learning
description: Converts a completed task, review, or incident into durable engineering guidance. Use for retrospectives, repeated agent mistakes, workflow improvements, or requests to update rules and skills.
---

# Capture learning

Record only lessons supported by the completed work.

## Find the lesson

1. State what took longer than expected or failed.
2. Identify the missing fact, unsafe default, unclear boundary, or unreliable step.
3. Separate a one-time event from a repeated pattern.
4. Confirm the new guidance would have changed the result.

## Choose the durable form

Use the first form that prevents recurrence:

1. Delete the obsolete path.
2. Fix the API, type, data model, or default.
3. Add a focused test, assertion, lint, or validation script.
4. Update executable configuration.
5. Update repository documentation.
6. Update a task-specific skill.
7. Add an always-on rule only for a short, universal safety requirement.

Do not add a rule when code or automation can enforce the requirement. Do not add a skill for a one-time fact.

## Update guidance

- Keep the instruction specific, testable, and short.
- State when the instruction applies.
- Write what to do. Name the current practice.
- Remove or replace conflicting guidance.
- Add the source task, ticket, incident, or pull request when the reason is not obvious.
- Validate links, paths, frontmatter, and examples.

Report what changed, why this is the correct layer, and how the new guidance can be checked.
