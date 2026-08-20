---
name: operate-environment
description: Starts, restarts, and diagnoses Rails and React development services and prepares safe production operations. Use for local setup, service health, Docker, Redis, database authentication, Heroku diagnosis, deploy readiness, or runtime configuration.
---

# Operate the environment

Read the repository instructions and executable configuration before you run service commands. Repository-specific commands, ports, process order, and exclusions take precedence.

Assume Heroku for staging and production unless the repository documents a different platform.

## Local services

1. Inspect existing terminals and running processes before you start a duplicate service.
2. Start dependencies in the documented order.
3. Start the application with the documented environment variables and command.
4. Confirm health through the documented local endpoint or process check.
5. If you started a service, restart it when changed code, configuration, templates, dependencies, or environment variables require a reload.
6. Report the exact process or health check that failed.

## Preserve local state

- Treat development database volumes and local data as persistent.
- Do not drop the development database, delete a database volume, run a volume prune, or recreate storage to fix authentication or migrations.
- Repair database credentials in place with the repository procedure.
- Preserve local credential files before a branch switch. Restore them after the switch.
- Never commit a key file or print a secret.

## Production-adjacent operations

Read-only diagnosis can inspect logs, configuration names, release state, and health.

Get explicit approval for the exact app and action before:

- A Heroku push or deploy.
- A config variable change.
- A dyno scale change.
- An addon or pipeline change.
- App or review-app creation.
- A deploy from code that is not merged to the approved base branch.

If a deploy or boot fails, stop after diagnosis. Report the failing step, evidence, customer risk, rollback state, and the ticket or pull request needed for the fix. Do not commit a workaround and redeploy without new approval.

## Output

State the environment, commands run, observed health, changed state, remaining risk, and any action that still needs human approval.
