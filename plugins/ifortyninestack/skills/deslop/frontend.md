# React, TypeScript, and Inertia deslop

Keep the first paint equal to the server props. Keep policy and durable writes on the server.

Build small components with explicit props and local state. Use the primitives already in the repository. Inline a helper that only forwards props. Keep types honest. Avoid a new store, context, or package for state one screen already owns.

When a server contract changes, update the producer, the types, the consumer, and the tests together. Client checks can hide a control. They cannot authorize the action.

Show loading, empty, error, and success as they really are. Confirm durable success on the server before you report it. If the page already has the data, use it. Fetch in the smallest place that owns the request.

Treat HTML, redirects, and storage as untrusted when they come from the client or from user content. Identity, tenancy, and role come from the server session or token, not from a field the client posted.

Use the same domain names the server uses.
