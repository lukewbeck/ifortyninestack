---
name: build-change
description: Implements a feature, behavior change, or refactor across a Rails and React stack. Use for Rails, React, Inertia, APIs, jobs, migrations, imports, bulk actions, or LLM prompt behavior.
---

# Build a change

## Before editing

1. Read the ticket, repository instructions, affected code, tests, and configuration.
2. Confirm the acceptance criteria and completion evidence.
3. Name the data shape, owner, invariants, authorization boundary, and external contracts.
4. Read only the applicable reference:
   - [rails.md](rails.md)
   - [frontend.md](frontend.md)
   - [api-and-data.md](api-and-data.md)
   - [jobs.md](jobs.md)
   - [migrations.md](migrations.md)
   - [testing.md](testing.md)
   - [llm-output.md](llm-output.md)
5. Check whether deletion, a framework feature, or an installed dependency avoids new code.

## Implement

1. Add or update the smallest test that defines the behavior when a focused test is practical.
2. Make the smallest coherent production change.
3. Keep policy and invariants on the server.
4. Update every side of a changed contract in the same change set.
5. Parallelize only independent work with disjoint writes.
6. Do not add compatibility code unless a shipped caller requires it.
7. Restart services that you started when the changed code or configuration requires a reload.

## Verify

1. Run the narrowest relevant tests and linters.
2. Verify user-facing behavior on the matching surface when practical.
3. Inspect the full diff for unrelated churn, stale code, secrets, and missing contract updates.
4. Compare the result with each acceptance criterion.
5. State migrations, jobs, operations, deploy risk, rollback, and compatibility impact.
6. Do not leave known merge blockers for a later review pass.

If evidence shows that the design is wrong, stop adding exceptions. Return to the data shape and ownership decision.

If the remaining diff is ceremonial wrappers, ignored writes, unscoped finds, or narrating comments, use `deslop` as a separate pass.
