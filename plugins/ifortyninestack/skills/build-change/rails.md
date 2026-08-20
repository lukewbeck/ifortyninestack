# Rails and Ruby

- Follow Rails conventions and repository patterns before you add a new object.
- Keep controllers focused on authentication, authorization, parameters, orchestration, and rendering.
- Put domain invariants in models, database constraints, or a clear domain boundary.
- Use a service object for a multi-step workflow that spans models, transactions, jobs, or external systems. Do not use one to move a simple line out of a controller.
- Use one source of truth for feature access and capability checks.
- Use persistence methods whose failure behavior matches the workflow.
- Use `update!` when failure must stop the workflow.
- Use `update_columns` only when bypassing validation, callbacks, and timestamps is required.
- Use strong domain names. Avoid overloaded names that hide meaning.
- Keep methods small and control flow explicit.
- Avoid metaprogramming, broad rescue clauses, hidden callbacks, and surprise side effects.
- Follow Zeitwerk file, directory, and constant naming.
- Inspect Active Record, SQL, Rack, and allocation behavior before changing a hot path.
- Run StandardRB only on touched Ruby files.
