---
name: address-senior-review
description: Reviews and addresses existing human feedback from senior reviewers on a pull request. Use when the user invokes /address-senior-review or asks to handle senior review comments with human approval for code changes, replies, and resolutions.
disable-model-invocation: true
---

# Address senior review

Run this workflow yourself in the current chat. Do not launch review or implementation subagents.

This skill addresses existing human review. It does not run a new broad review and does not treat automated comments as senior feedback.

## Resolve the review state

1. Resolve the pull request URL, number, or current branch.
2. Read the pull request intent, linked ticket, full current diff, checks, repository instructions, and exact head SHA.
3. Read every human review, inline comment, top-level comment, reply, and unresolved thread.
4. Identify the senior-review threads the user wants addressed.
5. Keep automated comments separate unless the user includes them.
6. Stop and refresh if the remote head changes.

## Understand each thread

For every selected thread:

1. Restate the reviewer request.
2. Trace the relevant execution path, contract, tests, and repository convention.
3. Read the full thread for later clarifications.
4. Determine whether the current head already changed the concern.
5. Link duplicate threads that require the same implementation decision.

Do not assume that senior feedback is correct. Treat it as high-signal input that still requires technical validation.

## Decide the response

Give each thread one proposed outcome:

- **Fix.** The concern is valid and in scope.
- **Clarify.** The code is correct, but the reviewer lacks context that the pull request or code should make clearer.
- **Reply with evidence.** The concern does not apply to the current implementation.
- **Already fixed.** The current head resolves the concern.
- **Duplicate.** Another thread or accepted fix owns the same root issue.
- **Human decision.** The response requires a product, security, data, compatibility, or architecture choice.
- **Defer.** The concern is valid but outside the pull request, with a concrete follow-up path.

For a proposed fix, state:

- The root invariant or quality goal.
- The smallest coherent code change.
- A focused verification plan.
- Files and contracts affected.
- Review surface and risk.
- A draft reply.

For a no-code response, cite the current code, test, contract, or scope evidence and draft the exact reply.

## Human decision gate

Present the proposed outcomes and exact reply drafts in chat.

Ask the user to approve, reject, or modify:

- Each code change.
- Each no-code reply.
- Each thread resolution.
- Each defer or follow-up action.

Use a structured question when available. Do not edit code or write to GitHub before approval.

Approval of a fix authorizes that code change, one logical commit, and a normal push to the existing pull request branch. It does not authorize a reply, resolution, merge, deploy, amend, or force-push.

## Implement approved fixes

For each coherent fix group:

1. Confirm the remote head matches the reviewed SHA.
2. Implement only the approved response.
3. Prefer deletion, framework conventions, the standard library, and existing repository patterns.
4. Add or update the smallest test that proves the reviewer concern when behavior changes.
5. Run focused checks and required repository gates.
6. Inspect the diff against every linked thread.
7. Create one logical commit and push without force or amend.
8. Record the new head, commit, changed files, commands, results, and limitations.

Preserve uncommitted work, local credentials, development data, and persistent volumes.

## Validate

After each fix group:

1. Confirm the remote head and changed files.
2. Re-read the original threads.
3. Verify that the root concern is resolved.
4. Confirm that tests or reproduction cover the original failure.
5. Check for contract breaks, scope growth, dead code, duplication, or new complexity.

If validation fails, do not reply or resolve. Correct the fix or return to the human decision gate.

## Reply and resolve

Show the final exact reply for each thread after validation.

Post only replies the user approves. Use concise teammate language and no em dash.

Resolve a thread only when:

- The approved code is pushed and verified, or the approved no-code disposition is supported by current evidence.
- The approved reply is posted.
- The user approved resolution.

Leave deferred, ambiguous, failed, or disputed threads unresolved.

## Finish

Re-read the current head, unresolved human threads, and required checks.

Return:

- Pull request link and head SHA.
- Fixed, replied, resolved, deferred, and open counts.
- Commits and verification results.
- Remaining merge blockers and human decisions.

If there are no remaining merge blockers, say the pull request is merge-ready. Do not merge the pull request or convert a draft to ready.
