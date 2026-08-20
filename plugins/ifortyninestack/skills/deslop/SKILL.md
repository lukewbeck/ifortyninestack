---
name: deslop
description: Removes agent-generated slop from a Rails, React, Inertia, job, or contract change. Use for /deslop, clean this AI code, remove slop, or after an agent implementation that looks ceremonial, unsafe, or over-abstracted.
---

# Deslop a Rails and React change

Clean agent-generated code against the current branch diff. Keep intended behavior unless you fix a clear bug.

This skill edits the working tree. Use `review-change` for findings and `fix-bug` when you start from a reproduction.

Read only the references that match the diff:

- [rails.md](rails.md) for controllers, models, persistence, errors, SQL, jobs, and naming.
- [frontend.md](frontend.md) for React, TypeScript, and Inertia.

## Scope

1. Diff against the correct base branch. Include staged, unstaged, and untracked files when the work is local.
2. Limit edits to files this change introduced or made worse. Do not restyle unrelated code.
3. Prefer deletion and inlining over new wrappers.
4. Do not add a service, helper, or compatibility layer to make slop look organized.

## Order

Do not start by renaming classes or extracting prettier services.

1. Add or keep a characterization test around current externally visible behavior when the cleanup could change a contract.
2. Fix authorization, tenant scoping, unsafe parameters, injection, secrets, and output escaping.
3. Restore data integrity: bang vs non-bang writes, transactions, unique indexes, idempotency.
4. Fix error paths and job retry semantics.
5. Measure and reduce SQL, HTTP, storage, mail, and cache I/O.
6. Remove duplication and dead abstractions.
7. Normalize names and simplify control flow.
8. Delete narrating comments and run formatting last on touched files only.

Stop after each step if the remaining issues are outside this change.

## Guardrails

- Do not change product behavior to match taste.
- If a write path, retry, or render currently fails open, that is a bug. Fix it and say so.
- If two names refer to different domain concepts, do not merge them.
- If a check cannot run, record the command and remaining risk. Do not claim a pass.
- Ask before a breaking contract, auth, tenancy, or public-endpoint change.

## Abstraction test

Ask of every new object in the diff:

What complexity, invariant, or dependency does this object encapsulate?

If the answer is that it calls one Active Record method, one Inertia render, or one fetch, inline it.

## Finish

1. Run the narrowest relevant tests and linters for touched files.
2. Inspect the remaining diff for leftover wrappers, ignored writes, unscoped queries, and wide parameter permits.
3. Summarize in three sentences or fewer: what you removed, which bugs you fixed, and what you did not verify.
