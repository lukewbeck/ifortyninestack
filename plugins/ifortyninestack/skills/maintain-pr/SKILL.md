---
name: maintain-pr
description: Keeps a pull request merge-ready by triaging comments, fixing CI, resolving clear conflicts, and updating delivery notes. Use for PR comments, CI failures, conflicts, get it green, or babysit this PR.
---

# Maintain a pull request

Use `gh` as the source of truth for GitHub pull requests and checks. Do not merge, enable auto-merge, convert a draft to ready, or deploy.

## Establish state

1. Resolve the pull request for the current branch.
2. Read the pull request description, complete diff, commits, reviews, inline comments, discussion, and check set.
3. Read the linked Linear issue and current acceptance criteria.
4. Report the current blockers before you change code.

## Review feedback

Classify each comment:

- Fix. The comment identifies a real issue in scope.
- Dismiss. The comment is incorrect, duplicate, a style preference, or outside the ticket.
- Ask. Product intent or human authority is required.

For a fix, make the smallest responsible change and run the affected checks. For a dismissal, give a concise technical reason. Do not churn code to satisfy automated review.

## CI failures

1. Use `gh pr checks` to identify the failing check.
2. Read the first actionable failure, not only the final exit code.
3. Reproduce it locally when practical.
4. Fix the cause. Do not bypass the check or add a broad workaround.
5. Run the focused local check.
6. Commit and push only when the user requested active PR maintenance.
7. Recheck the full pull request check set.

## Conflicts

1. Preserve local credentials and unrelated work.
2. Understand both sides before resolving.
3. Keep the pull request intent and current base-branch contract.
4. Run focused tests after the resolution.
5. Report any semantic choice made during resolution.

## Complete

Update the pull request description when tests, risks, migrations, jobs, or compatibility notes changed. Name the title and body by what landed. Keep the Linear issue in In Review while the pull request is under review.

Return the pull request link, resolved items, open merge blockers, check status, and remaining risk. If there are no merge blockers, say the pull request is merge-ready. Do not merge it.
