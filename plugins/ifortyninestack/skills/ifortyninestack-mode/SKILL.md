---
name: ifortyninestack-mode
description: Runs Rails and React engineering work from ticket intake through a merge-ready pull request. Use for /ifortyninestack-mode or when the user asks for the full Ifortyninestack workflow.
disable-model-invocation: true
mode: true
icon: layers
color: blue
reminder: Apply the matching Ifortyninestack phase until the user opts out.
---

# Ifortyninestack mode

Use the smallest workflow that reaches the requested outcome. Do not run later delivery phases unless the user asked for them or the current task clearly includes them.

## Start

1. Read the repository instructions and executable configuration.
2. Classify the request as intake, investigation, planning, implementation, diagnosis, review, verification, delivery, maintenance, incident response, or documentation.
3. For a non-trivial task, create a short task list with a concrete completion check.
4. Use the matching skill.

## Route the work

- New or updated Linear issue: `work-intake`.
- System walkthrough, placement question, or design history: `understand-system`.
- Design or implementation plan: `plan-change`.
- Feature or behavior change: `build-change`.
- Agent-generated slop, ceremonial wrappers, or unsafe generated Rails/Inertia: `deslop`.
- Defect or regression: `fix-bug`.
- Evidence that a claim is true: `verify-change`.
- Local or branch review: `review-change`.
- Exhaustive PR review, human decisions, selected fixes, and fresh re-review: `review-decide-address-loop`.
- Human-approved inline GitHub review comments: `review-inline-comments`.
- Existing human feedback from senior reviewers: `address-senior-review`.
- Commit, branch, or pull request: `open-pr`.
- Pull request comments, conflicts, or CI: `maintain-pr`.
- Local services, runtime health, or deploy preparation: `operate-environment`.
- Production incident or customer-impacting failure: `incident-response`.
- README, design note, pull request text, commit text, or other engineering prose: `technical-writing`.
- Durable lesson from completed work: `capture-learning`.
- Dense prior answer that needs simpler wording: `plain-language`.

## Working rules

- Ground decisions in the ticket, code, tests, configuration, runtime evidence, and linked source systems.
- Name the data shape and server-client contracts before changing code that crosses boundaries.
- Parallelize independent reads, reviews, and disjoint edits. Serialize shared writes.
- Use separate reviewers for product behavior, production safety, and maintainability on substantial changes.
- Keep the main thread focused on decisions and results. Send broad exploration to subagents.
- Ask only for choices that require human authority. Do not ask the user to answer facts that local evidence can resolve.
- Stop before destructive data work, breaking changes, risky security changes, deploys, Heroku writes, force pushes, or merges.

## Completion

Before you say that work is complete:

1. Compare the result with the acceptance criteria.
2. Run the narrowest reliable checks.
3. Inspect the diff and test output.
4. State migration, job, deploy, operational, and compatibility impact.
5. State any unverified behavior or remaining risk.
6. If the task includes a pull request, state remaining merge blockers. Do not call leftover fixes review polish. The remaining human action should be the merge decision.

Never merge code. A human makes the merge decision.
