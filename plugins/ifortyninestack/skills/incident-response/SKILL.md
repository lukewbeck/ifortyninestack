---
name: incident-response
description: Diagnoses customer-impacting production failures and prepares a safe response. Use for incidents, outages, production regressions, data integrity concerns, or urgent customer impact.
---

# Incident response

Protect customers and preserve evidence. Do not deploy, change production configuration, modify data, or contact customers without explicit approval.

## Triage

1. State the user-visible impact, affected tenants, start time, and current state.
2. Identify the source of each fact.
3. Check authentication, tenant boundaries, data integrity, jobs, external dependencies, and recent deploys.
4. Keep unknown values marked as unknown.

## Diagnose

1. Build a timeline from logs, errors, deploys, tickets, Slack, and observability sources.
2. Correlate symptoms with trace IDs, job IDs, record IDs, releases, and code paths.
3. Form competing hypotheses.
4. Use evidence to eliminate hypotheses.
5. Distinguish the trigger, root cause, contributing conditions, and blast radius.

## Response proposal

For each option, state:

- Expected customer effect.
- Data and tenant risk.
- Time to apply.
- Verification method.
- Rollback or recovery path.
- Required human approval.

Prefer a reversible mitigation when it reduces customer harm without hiding evidence. Do not apply a mitigation that can lose data or widen access without approval.

## Follow-up

Prepare:

- A concise status update.
- A root-cause summary with evidence and confidence.
- A focused fix ticket.
- Observability and regression-test gaps.
- A rollback and deploy plan.

Do not call a symptom guard the root-cause fix.
