# Linear protocol

This is the shipped Linear taxonomy. Fork the plugin and rename labels, statuses, or ticket prefixes if your team uses different names.

Treat the issue as the execution contract. Keep it current when scope or constraints change.

Use Linear as the issue tracker. Use GitHub Issues only when Linear is not available. GitHub Issues still need the required issue content. Skip cycle-tracking labels on GitHub Issues.

## Ticket prefix

Use the team's existing ticket prefix. Do not invent one.

Common prefixes are `ENG` and `DEV`. Examples in this plugin use `ENG-###`. If the workspace issues are `DEV-###`, use `DEV`.

Keep the prefix in ticket identifiers, branch names, and `Closes` lines.

## Required issue content

- Problem.
- Acceptance criteria.
- Constraints.
- Linked customer, Slack, meeting, document, pull request, or prior issue context.
- Scope and out-of-scope boundaries when useful.
- Known test and deploy notes.

## Cycle tracking

For an issue assigned to a cycle:

- Set exactly one label from `Cycle Tracking - Commitment`.
- Set exactly one label from `Cycle Tracking - Origin`.
- If the issue slipped, set at most one label from `Cycle Tracking - Delay Reason`.
- Keep multicycle work unpointed.

The human chooses Commitment, Origin, and Delay Reason. Do not infer these values. If a required value is not explicit, ask one focused question before the issue write.

Do not add unrelated labels unless the user asks. Preserve labels that already exist.

## Active issue fields

Before an issue moves past Backlog, confirm:

- A specific assignee.
- An explicit priority.
- A cycle when the work belongs to the current cycle.
- An estimate when the issue is expected to finish in one cycle.
- The required cycle tracking labels.
- A project when the work belongs to one.

If an issue is in Backlog, do not start ordinary implementation until an authorized human moves it to Todo. Follow repository-specific exceptions for urgent work.

## Status

- Move the issue to In Progress when implementation starts.
- Move the issue to In Review when a pull request opens.
- Move the issue to In Staging after the change reaches staging.
- Do not move the issue to Done until the change is in production or an authorized human confirms an equivalent final state.

Do not move an issue, assign it, change its cycle, or change its priority unless the user requested that write or the active repository workflow explicitly requires it.
