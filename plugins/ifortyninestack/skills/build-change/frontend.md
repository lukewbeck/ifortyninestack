# React, TypeScript, and Inertia

- Build small components with explicit props and local state.
- Use shared primitives and current repository patterns before you add a component family or state layer.
- Do not add a frontend dependency unless the existing stack cannot solve the problem.
- Keep imports at module scope.
- Parse untrusted data at the boundary.
- Make invalid states difficult to represent.
- Use exhaustive `switch` handling for unions and enums.
- Keep permissions, feature access, policy, and configurable domain lists on the server.
- Update Rails props, TypeScript types, React consumers, and tests together.
- Keep the first client render equal to the server render.
- Provide clear loading, success, empty, and error states for important asynchronous work.
- Fire completion telemetry only after confirmed success.
- Do not present durable state before the server confirms it.
- Use accessible names, roles, focus behavior, and keyboard interaction.
- Scope CSS to the component or an explicit opt-in boundary.
- Check for avoidable request waterfalls, rerenders, and bundle growth.
