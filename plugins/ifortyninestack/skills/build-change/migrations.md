# Migrations and schema

- Confirm table size and expected write traffic.
- Identify lock risk, deploy order, mixed-version behavior, rollback limits, and backfill duration.
- Use one forward migration path.
- Split schema changes, data backfills, and constraint validation when a single deploy is unsafe.
- Add nullable or unvalidated structures first when the application needs a compatibility window.
- Backfill before you enforce the invariant.
- Validate the constraint after the data satisfies it.
- Use an irreversible migration when rollback cannot truthfully restore the old state.
- Do not add and remove the same structure through corrective migration churn.
- Ensure every schema change has its migration in the same pull request.
- Verify the committed schema version matches the latest migration.
- Do not run destructive development database commands or recreate a database volume as a troubleshooting shortcut.
- State the production execution and recovery plan in the pull request.
