# Issue protocol

Treat the issue as the execution contract. Keep it current when scope or constraints change.

## Required issue content

- Problem.
- Acceptance criteria.
- Constraints.
- Linked customer, Slack, meeting, document, pull request, or prior issue context.
- Scope and out-of-scope boundaries when useful.
- Known test and deploy notes.

## Tracker conventions

Follow the repository and team process for identifiers, labels, estimates, cycles, and status names.

Do not add labels, assignees, cycles, or priority values unless the user asked or the repository workflow requires them. Preserve labels that already exist.

If the workspace uses required tracking labels, keep a valid set. Do not infer Commitment, Origin, Delay Reason, or similar process labels. Ask one focused question when a required value is missing.

## Active issue fields

Before ordinary implementation starts, confirm the fields the team requires for in-progress work. Common examples are assignee, priority, cycle, estimate, and project.

If an issue is still in backlog or triage, do not start ordinary implementation until an authorized human moves it into an active state. Follow repository-specific exceptions for urgent work.

## Status

When the user asks you to keep the ticket in sync:

- Move the issue to the in-progress state when implementation starts.
- Move the issue to the review state when a pull request opens.
- Do not mark the issue done until the change is in production or an authorized human confirms an equivalent final state.

Do not move an issue, assign it, change its cycle, or change its priority unless the user requested that write or the active repository workflow explicitly requires it.
