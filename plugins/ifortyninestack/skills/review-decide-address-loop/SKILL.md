---
name: review-decide-address-loop
description: Runs a high-recall pull-request review, human decision gate, selected fixes, validation, and fresh re-review in one Cursor chat. Use only when the user invokes /review-decide-address-loop.
disable-model-invocation: true
---

# Review, decide, and address

Run this workflow yourself in the current chat. Do not launch review, normalization, implementation, or validation subagents.

The goal is a pull request that is ready to merge. High recall belongs in discovery. Code changes require evidence and lead judgment. A human still decides when to merge.

## Invocation

Accept:

- A pull request URL or number.
- `current PR`.
- `human_in_loop: true` or `false`. Default to `true`.
- `review_only: true` to stop after the decision gate.

If the current branch has no pull request, ask for a URL or number.

## Boundaries

- Read `AGENTS.md`, nested instructions, `.cursor/BUGBOT.md`, repository rules, executable configuration, and ticket context.
- Preserve uncommitted work, local credentials, the development database, and persistent volumes.
- Do not merge, convert a draft to ready, enable auto-merge, deploy, use a Heroku remote, force-push, amend, or rewrite published history.
- Do not post agent-generated findings to GitHub.
- Do not reply to or resolve existing GitHub threads without human approval.
- Do not expose secrets, customer data, or sensitive exploit details.

## Review outcomes

Give every unique concern one outcome:

- **Address.** A correctness, security, contract, data, or operational problem that this pull request introduces, worsens, or makes reachable.
- **Polish.** An in-scope change that materially reduces concepts, branching, indirection, duplication, or future change cost.
- **Watchlist.** A plausible but uncertain, pre-existing, broader, or lower-value concern that does not justify code in this pull request.
- **Human decision.** A product, security, data, compatibility, or architecture choice that requires human authority.
- **No code.** Invalid, out of scope, already fixed, or duplicate, with evidence.

Do not require a minimum number of findings. Do not treat a repeated or cheap suggestion as valid by default.

## Retained state

When the repository has an ignored `tmp/` directory, store resumable state at:

```text
tmp/pr-review-loop/pr-<number>/
  state.json
  candidate-ledger.json
  decision-gate.md
  reviewer-guide.md
  final-report.md
```

Otherwise use `/tmp/ifortyninestack/pr-review-loop/<repo>/pr-<number>/`.

Record the pull request number, URL, base SHA, head SHA, current phase, candidates, decisions, commits, verification, replies, and remote mutations. Reconcile the recorded state with GitHub before retrying a mutation.

## Review cycle

### 1. Resolve and freeze the head

Read:

- Pull request title, body, base, head, commits, files, checks, and draft state.
- Inline comments, reviews, top-level discussion, and unresolved threads.
- Linked ticket requirements and relevant source context.
- Applicable repository instructions.
- Recent history and analogous implementations for changed contracts.

Fetch the exact base and head commits. Record the head SHA. If the remote head changes, discard stale decisions and start a new cycle.

### 2. Review for recall

Run these passes sequentially over the complete change:

1. Intent, local correctness, and changed contracts.
2. Auth, tenancy, privacy, data invariants, migrations, jobs, external APIs, and deploy behavior.
3. Blast radius, callers, readers, writers, old clients, queued work, flags, caches, and missing companion changes.
4. Failure, retry, rollback, concurrency, stale-state, loading, empty, error, cancellation, and accessibility behavior.
5. Structural quality, ownership, types, names, cohesion, directness, and code that can be deleted.
6. Tests, observability, reviewability, mixed concerns, mechanical noise, and unnecessary comments or defensive clutter.

For each changed invariant, identify the one or two facts that make the change safe. Trace those facts through source and tests. Run a focused proof when practical.

Record candidates before deciding them. Include:

- Stable fingerprint.
- Path, line, and symbol.
- Root invariant.
- Observation and reachable trigger.
- Potential impact.
- Evidence and counterevidence.
- Uncertainty.
- Possible response.
- Matching external thread, if one exists.

### 3. Normalize

Group candidates when they share the same root invariant and the same implementation decision.

Combine duplicate test requests into one verification plan for the invariant. Keep a source map so every candidate fingerprint appears once.

Run normalization again after disposition. If one change resolves several concerns, implement it once.

### 4. Decide

Use current code, tests, contracts, history, repository guidance, and thread discussion.

For **Address**:

- Require affirmative evidence.
- Name the execution path or violated invariant.
- Propose the smallest responsible fix.
- Define one verification plan.

For **Polish**:

- Keep the work in changed code or necessary companion code.
- State the concrete quality gain.
- Include implementation cost and added change surface.
- Reject changes that only move complexity or express preference.

For **Watchlist**:

- State why code is not justified now.
- State the promotion trigger.
- State the cheapest next proof.

For **Human decision**:

- Ask one exact question.
- Offer only real options.
- Recommend the safest responsible option.

For **No code**:

- Cite the contrary evidence or scope boundary.
- Draft a reply when the concern maps to an existing external thread.

Missing tests alone are not a defect. Tie test work to a changed invariant and a plausible regression that the test uniquely catches.

### 5. Present the decision gate

Present the gate in the current chat. For a large review, also write `decision-gate.md` and link it.

Use these sections:

1. Address before merge.
2. Structural and readability polish.
3. Human decisions.
4. Watchlist.
5. No-code dispositions.
6. Proposed replies to existing threads.

For each Address or Polish item, include evidence, recommendation, affected files, verification, cost, and change surface.

Ask the human to accept, reject, or modify each proposed code change and each proposed GitHub reply. Use a structured question when available.

If `human_in_loop` is `true`, stop before implementation.

If `human_in_loop` is `false`, apply only safe, routine Address items and low-surface Polish items. Stop for architecture, auth, permissions, public APIs, destructive data work, compatibility choices, or repository-defined escalation.

Human acceptance authorizes the selected code edits, logical commits, and push to the existing pull request branch. It does not authorize a merge, deploy, history rewrite, or GitHub reply.

### 6. Implement accepted work

For each coherent accepted group:

1. Confirm the remote head still matches the reviewed SHA.
2. Reconfirm the root cause or quality goal.
3. Implement only the accepted response.
4. Prefer deletion, framework behavior, the standard library, and existing patterns.
5. Add or update the smallest test that proves an Address item.
6. Preserve behavior for Polish and avoid implementation-detail tests.
7. Run focused checks and repository gates.
8. Inspect the group diff against every linked candidate.
9. Create one logical commit and push without force or amend.
10. Record the old head, new head, commit, files, commands, results, and limitations.

Stop on an unsafe partial fix or an unexpected design choice.

### 7. Validate each group

After each implementation:

1. Confirm the remote head and changed files.
2. Check that the selected response was implemented exactly.
3. Re-run the original reproduction or focused proof.
4. Confirm the root concern no longer applies.
5. Confirm scope stayed coherent.
6. Check for new contract breaks, dead code, duplication, or complexity.

If validation fails, correct the same group and validate again. Stop if the same fingerprint returns without progress.

### 8. Handle existing review threads

After validation, show the exact proposed replies in chat.

Post only the replies the human approves. Use concise teammate language and no em dash.

Resolve a thread only when:

- The approved fix is pushed and verified.
- The reply is posted.
- The human approved resolution.

Leave deferred, uncertain, failed, and Watchlist threads unresolved.

### 9. Re-review the latest head

After any code change:

1. Fetch the latest head.
2. Start a new cycle.
3. Repeat every review pass over the complete pull request.
4. Normalize and decide new or changed candidates.
5. Return to the decision gate when new Address, Polish, or Human decision items appear.

Do not declare success from a review performed on an older head.

## Merge-ready gate

Declare `merge-ready` only when:

- One complete fresh cycle on the latest head finds no new Address or Polish items.
- Accepted changes are committed, pushed, and verified.
- Every candidate has one recorded outcome.
- Watchlist items retain evidence and a promotion trigger.
- Approved external-thread actions are complete.
- No unresolved actionable thread remains.
- The final diff is free of unnecessary comments, defensive clutter, loose casts, avoidable nesting, and unrelated changes.
- `reviewer-guide.md` matches the latest head.
- Relevant local checks and required CI pass, or the limitation is explicit.
- The head did not change after the final review.
- The remaining human action is the merge decision, not leftover fixes.

Write `final-report.md` with the head SHA, cycle count, verification, watchlist, thread state, limitations, and human next step.

This verdict increases confidence. It does not prove that the software has no defects. It does not authorize a merge.

## Final response

Return:

- The decision gate or final report path.
- Counts by outcome.
- Current status.
- The smallest human decision or next action.

Do not merge the pull request or convert a draft to ready.
