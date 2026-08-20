---
name: review-change
description: Reviews a diff or pull request for product intent, production safety, maintainability, and test evidence. Use for code review, PR review, risk review, or pre-merge review.
---

# Review a change

The default deliverable is findings. Do not edit code unless the user also asks for fixes. Use `deslop` when the user wants a cleanup pass on agent-generated code rather than a review report.

The bar is a pull request that is ready to merge. Do not optimize for making the change easier for a human to inspect. Optimize for a change a human can merge. Code is cheap. A small, valid fix is still a fix. A human still decides when to merge.

Use `review-decide-address-loop` when the user wants an exhaustive review, a human decision gate, selected fixes, validation, and fresh re-review. Use `review-inline-comments` only when the user explicitly wants GitHub comments.

## Establish scope

1. Read the user request, ticket, pull request description, and acceptance criteria.
2. Inspect the complete change set against the correct base branch.
3. Include staged, unstaged, and untracked changes when reviewing local work.
4. Read the changed files and enough surrounding code to validate each concern.
5. State the intended behavior in one paragraph.

## Run focused reviews

For a substantial change, launch these agents in parallel:

- `ifortyninestack-product-contract-reviewer`
- `ifortyninestack-production-safety-reviewer`
- `ifortyninestack-maintainability-reviewer`

Give each agent the same intent, diff scope, relevant file paths, and ticket constraints. Do not assign the same broad review prompt to all three. Each agent owns its documented lens.

## Lead judgment

Validate every proposed finding against the code and intent. Deduplicate related findings. Reject formatting taste, hypothetical problems without a reachable path, and suggestions outside this change.

Do not reject a validated finding because the edit is small. Implementation cost is not a reason to demote severity.

Use these severities:

- Blocker. The change can cause incorrect behavior, data loss, security exposure, cross-tenant access, or unsafe deployment.
- Important. The pull request is not ready to merge until this is fixed. Include likely defects, contract breaks, operability gaps, missing tests for a changed invariant, and in-scope quality problems that would block merge: narrating comments, dead paths, one-caller wrappers, duplicated decisions, logic in the wrong layer, avoidable branching, incomplete loading, empty, error, or accessibility behavior for a surface this change introduced. Include a title or description that teaches a stranger a rejected extra from the conversation.
- Note. Watchlist only. The concern is uncertain, pre-existing, or outside this change. A Note is not a work queue. Do not use Note because a fix looks small.

Do not downgrade a validated maintainability or product-contract finding to Note because it is not a production incident. Formatting taste means indent, quote style, or a rename with no meaning change. It does not mean comments, extra abstraction, duplication, ownership, or incomplete UX.

For each finding, include the path and line, the failure scenario or quality cost, why this blocks merge, and the smallest responsible fix.

## Complete the review

Report findings first, in this order:

1. Fix before merge. All Blocker and Important items. If this section is not empty, say the pull request is not merge-ready.
2. Watchlist. Notes only.

Then report:

- Acceptance-criteria coverage.
- Tests and verification inspected or run.
- Migration and schema impact.
- Job and external API impact.
- Deploy, rollback, and compatibility risk.
- Dismissed reviewer suggestions when the reason helps.

If there are no Blocker or Important findings, say the pull request is merge-ready within the limits of the review. This verdict does not authorize a merge.
