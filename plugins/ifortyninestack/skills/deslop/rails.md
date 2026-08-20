# Rails deslop

Keep the response format the app already ships. Put work in the object that owns the invariant.

A controller authorizes, permits params, calls one operation, and renders. Domain rules live on the model or one workflow object. Extract a new object only when it hides a real invariant, transaction, or external dependency. Inline anything that wraps a single persistence call.

Return one kind of result from a method. Handle persistence failure with the bang form or an explicit branch. Treat uniqueness, existence, and "create if missing" as concurrency problems: a validation is not a constraint, and check-then-act is not atomic. Writes that form one business fact belong in one transaction. Side effects that cannot roll back (HTTP, mail, jobs) run after commit.

Rescue only errors this layer can turn into a user or API response. Unexpected errors belong to the reporter. Retry jobs for transient failures. Make irreversible work idempotent.

For every endpoint, follow request to actor, resource scope, authorization, permitted fields, query, and rendered attributes. Bind SQL values. Permit an explicit attribute list. Fail closed when a new action appears.

Count queries, HTTP calls, storage, enqueues, mail, and cache round trips. Load what the template or serializer actually uses. Keep network I/O out of open database transactions.

Use one name for each concept across models, routes, jobs, events, and copy.
