---
name: setup-ifortyninestack
description: Checks that Ifortyninestack is installed and that repository instructions, GitHub, and optional tracker or chat integrations are available. Use for /setup-ifortyninestack, installation checks, or onboarding.
disable-model-invocation: true
---

# Set up Ifortyninestack

Run a read-only setup check.

1. Confirm that the `ifortyninestack` plugin manifest loads.
2. List the installed Ifortyninestack rules, skills, and agents.
3. Read the current repository instructions, such as `AGENTS.md`.
4. Confirm that the repository tools and documented test commands exist.
5. Check GitHub CLI authentication without changing configuration.
6. Discover Linear, Slack, Granola, GitHub, and other relevant MCP servers when they are installed.
7. Report which integrations are available, need authentication, or are not installed. Missing optional integrations are not blockers.
8. Run `python3 scripts/validate_plugin.py` from the plugin repository when the source checkout is available.

Do not authenticate an integration, edit user settings, create a ticket, post a message, or change repository configuration during setup.

Return:

- Plugin status.
- Repository instruction status.
- GitHub status.
- Integration status.
- Validation result.
- Exact actions the user must take for any blocker.
