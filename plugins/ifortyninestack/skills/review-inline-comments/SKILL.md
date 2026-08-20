---
name: review-inline-comments
description: Reviews a pull request and publishes human-approved inline GitHub comments. Use only when the user invokes /review-inline-comments or explicitly asks to leave inline review comments.
disable-model-invocation: true
---

# Review with inline comments

Run the review yourself in the current chat. Do not launch review subagents.

This skill performs an external write. Draft comments first unless the user explicitly asks to publish all validated findings without another approval step.

## Boundaries

- Do not edit application code.
- Do not post discovery notes, uncertain candidates, watchlist items, summaries, or decision gates.
- Do not submit `APPROVE` or `REQUEST_CHANGES`.
- Do not merge, convert a draft to ready, resolve threads, deploy, force-push, or change pull request metadata.
- Do not expose secrets, customer data, or sensitive exploit details.
- Use no em dash in GitHub text.

## Resolve the review head

1. Resolve the pull request URL or number.
2. Read the title, body, ticket, base, head, commits, full diff, checks, and repository instructions.
3. Read existing inline comments and unresolved threads.
4. Fetch and record the exact head SHA.
5. Stop and restart if the head changes before publication.

## Review

Review the complete pull request for:

- Intent and local correctness.
- Contracts, callers, readers, writers, and missing companion changes.
- Auth, authorization, tenancy, privacy, and data invariants.
- Migrations, jobs, retries, partial failures, external APIs, and deploy behavior.
- Loading, empty, error, cancellation, accessibility, and hydration behavior.
- Structure, ownership, naming, cohesion, unnecessary indirection, and code that can be deleted.
- Tests that fail for a plausible regression in a changed invariant.

Record high-recall candidates privately. Normalize candidates by root invariant and implementation decision.

## Select publishable findings

Publish a candidate only when:

- The current pull request introduces, worsens, or exposes it.
- The failure path or concrete quality cost is supported by inspected evidence.
- The requested response is specific and in scope.
- The comment can attach to a changed line that gives the reviewer enough context.
- No existing unresolved thread already represents the concern.

Publish correctness, security, contract, data, and operational findings.

Publish a polish finding only when it removes material complexity that would block merge. Do not publish personal style preferences, speculative refactors, watchlist probes, or missing-test requests without a changed invariant and unique regression.

## Draft each comment

Use one concern per comment:

```text
<Specific observation and trigger>.

<Concrete consequence>.

<Requested change or focused question>.
```

Keep the comment concise and teammate-like. Name the execution path, contract, or invariant. Do not add generic praise, severity theater, or a long review rubric.

For each draft, record:

- Path.
- Diff side.
- Line or range.
- Head SHA.
- Root invariant.
- Evidence.
- Exact comment body.

## Human approval

Show the exact proposed comment set in chat. Include concise evidence and the target line.

Ask the user to approve, reject, or edit each comment. A request to `publish all validated findings` authorizes publication without this pause. It does not authorize other GitHub actions.

## Publish

1. Re-read the remote head.
2. Confirm every target line still exists in the current diff.
3. Remove any comment duplicated by a new external thread.
4. Submit one GitHub review with event `COMMENT` and the approved inline comments.
5. Read the created review and comments to confirm their path, line, body, and head.
6. Record the review URL and comment IDs.

Use `gh api` for the GitHub write. Pass the review as JSON through a file so comment text is not damaged by shell quoting.

If a comment cannot attach to the intended line, stop and report it. Do not convert it to a top-level comment without approval.

## Output

Return:

- Pull request link.
- Reviewed head SHA.
- Published comment links.
- Rejected or withheld count.
- Any limitation.
