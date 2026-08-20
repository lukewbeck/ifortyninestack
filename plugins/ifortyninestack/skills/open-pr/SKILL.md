---
name: open-pr
description: Creates a branch, commit, and pull request with ticket linkage and delivery notes. Use for branch creation, commits, pull requests, or requests to open a merge-ready pull request.
---

# Open a pull request

Do not merge, enable auto-merge, convert a draft to ready, or deploy unless the user explicitly requests that separate action.

Open a pull request that is merge-ready. State remaining merge blockers instead of leftover review polish. A human still decides when to merge.

## Before a branch switch

1. Read repository and user instructions for local credentials and ignored files.
2. Preserve required local-only credentials.
3. Confirm unrelated work will not be lost or included.

## Branch

- Require a ticket unless the user approves an exception.
- Follow the repository branch-name convention when one exists.
- If the repository has no convention, use `github_username/ticket-id/short-description`.
- Keep the description to about five hyphenated words.

## Commit

1. Inspect status, staged and unstaged diffs, and recent commit style.
2. Stage only files in scope.
3. Follow the repository commit style. If the repository uses conventional commits, use `<type>(<scope>): <short imperative summary>`.
4. Name the subject by the landed change. Keep rejected extras out of the subject.
5. Keep the subject concise and omit the final period.
6. Add a body only when it explains the problem, reason, or non-obvious consequence.
7. Wrap body text at about 72 characters.
8. Add `Closes <ticket-id>` when the commit resolves the issue.
9. Never bypass hooks.

## Pull request

1. Read the full branch diff and all branch commits.
2. Follow the repository pull request template when present.
3. Title the pull request by the landed change.
4. Write the description in this order:
   - Problem.
   - What changed.
   - How to test.
   - Why it is safe to deploy.
5. Describe the shipped outcome. Record an absence only when a reviewer needs it to judge safety, compatibility, or ticket scope. One short fact.
6. Include focused tests, linters, type checks, and their observed results.
7. Include screenshots or a video for user-interface changes.
8. State migration, schema, jobs, external APIs, auth, tenancy, contracts, compatibility, deploy risk, and rollback impact.
9. Link the Linear or GitHub issue.
10. Push the branch and open the pull request.
11. Move the issue to the review state when the user asked to keep the ticket in sync.
12. Read the created pull request and issue to confirm the final state.

If meeting context informed the change, ask whether the user wants a short decision note in the pull request.

State remaining merge blockers. If there are none, say the pull request is merge-ready. Do not merge it.
