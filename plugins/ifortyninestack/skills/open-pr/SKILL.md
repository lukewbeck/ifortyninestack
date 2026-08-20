---
name: open-pr
description: Creates a branch, commit, and pull request with Linear linkage and delivery notes. Use for branch creation, commits, pull requests, or requests to open a merge-ready pull request.
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
- Use `github_username/<prefix>-####/short-description`.
- `<prefix>` is the ticket prefix in lowercase. Use `eng` for `ENG-123`. Use `dev` for `DEV-123`. Do not invent a prefix.
- Use lowercase in the prefix and keep the ticket number in the middle segment.
- Keep the description to about five hyphenated words.

## Commit

1. Inspect status, staged and unstaged diffs, and recent commit style.
2. Stage only files in scope.
3. Use `<type>(<scope>): <short imperative summary>`.
4. Name the subject by the landed change. Keep rejected extras out of the subject.
5. Keep the subject concise and omit the final period.
6. Add a body only when it explains the problem, reason, or non-obvious consequence.
7. Wrap body text at about 72 characters.
8. Add `Closes ENG-###` or `Closes DEV-###` when the commit resolves the issue. Match the ticket prefix.
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
9. Link the Linear issue.
10. Push the branch and open the pull request.
11. Move the Linear issue to In Review.
12. Read the created pull request and issue to confirm the final state.

If meeting context informed the change, ask whether the user wants a short decision note in the pull request.

State remaining merge blockers. If there are none, say the pull request is merge-ready. Do not merge it.
