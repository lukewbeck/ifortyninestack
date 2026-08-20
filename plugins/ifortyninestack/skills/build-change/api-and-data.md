# APIs, tenancy, and data

- Preserve shipped JSON, Inertia, public API, metrics, and client contracts unless a breaking change has explicit approval and a migration plan.
- Prefer additive contract changes.
- Validate input and authorize the operation on the server.
- Scope every query to the correct organization, team, user, or tenant.
- Use the API-authenticated user for API-key routes. Do not substitute the session user.
- Enforce important invariants at the model or database boundary.
- Preserve structured data across imports, jobs, models, and responses.
- For bulk work, authorize each item, cap the batch, and return item-level success and failure results.
- Preserve supported singular and plural request forms when compatibility requires them.
- Distinguish invalid input, empty input, duplicate no-op, partial success, and failure.
- Clamp pages and whitelist page sizes when the repository uses paginated APIs.
- Never log secrets, tokens, raw personal data, or customer content.
- Persist the user-facing write before a best-effort notification or webhook.
