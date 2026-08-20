# Testing

Define the smallest check that can fail when the changed behavior is wrong.

- Start with a failing test when the behavior has a cheap, reliable test surface.
- Cover the expected path.
- Cover one meaningful edge case.
- Cover failure behavior when the failure changes persisted state, user feedback, retries, authorization, or data safety.
- Use model or service tests for domain behavior.
- Use request tests for HTTP behavior, auth, authorization, API-key context, JSON contracts, and Inertia props.
- Send the correct Inertia headers and assert the parsed props.
- Use React Testing Library roles and visible text for user behavior.
- Mock external network calls and realtime transports in component tests.
- Reserve system tests for critical end-to-end behavior that lower-level tests cannot prove.
- Use a focused test for a new non-trivial class or module.
- Run repository-specific linters and type checks for touched languages.
- Follow repository exclusions for expensive or unsafe local tests.
- If a check cannot run, record the command, failure, and remaining uncertainty.
