# Ifortyninestack

Ifortyninestack is a Cursor plugin for Rails and React engineering. It covers work intake, system investigation, planning, implementation, slop cleanup, diagnosis, verification, review, pull requests, CI, incidents, and technical writing.

Repository instructions still control repository-specific commands, architecture, and credentials.

## Use Ifortyninestack

Run the setup check after installation:

```text
/setup-ifortyninestack
```

Start a complete engineering workflow:

```text
/ifortyninestack-mode TICKET-123 implement the accepted ticket
```

You can also invoke a focused skill:

```text
/work-intake TICKET-123
/plan-change TICKET-123
/fix-bug reproduce and fix this regression
/deslop clean agent-generated slop on the current branch
/review-change review the current branch
/review-decide-address-loop review and improve the current PR
/review-inline-comments draft inline comments for PR 123
/address-senior-review address the human review on the current PR
/verify-change prove the UI state survives a reload
/open-pr open a merge-ready pull request
/maintain-pr address the current PR feedback and CI
/operate-environment diagnose the local service failure
/technical-writing edit this design note
```

## Design

Ifortyninestack uses three levels of guidance:

1. A small always-on baseline for engineering, safety, and communication.
2. File-scoped rules for Ruby, Rails, React, Inertia, tests, jobs, and migrations.
3. Task-specific skills that load detailed workflow guidance only when needed.

See [Architecture](docs/architecture.md).

## Local installation

Cursor loads local plugins from `~/.cursor/plugins/local`.

```bash
git clone https://github.com/lukewbeck/ifortyninestack.git
cp -R ifortyninestack/plugins/ifortyninestack ~/.cursor/plugins/local/
```

Run **Developer: Reload Window**. Then confirm that Ifortyninestack appears in **Customize**.

Validate the source checkout:

```bash
python3 scripts/validate_plugin.py
```

## Team installation

1. Host this directory in a GitHub repository.
2. Open **Dashboard**, then **Plugins**.
3. Import the repository into a Cursor team marketplace.
4. Set the installation mode for the intended team group.
5. Enable automatic refresh after the repository and access policy are stable.

Do not store secrets in this repository. If a future MCP server needs a secret, declare only the variable schema in `.cursor-plugin/plugin.json`.

Linear, Slack, and Granola are optional. The plugin uses them when they are installed. GitHub Issues work when Linear is not available.

## Source layout

```text
.cursor-plugin/marketplace.json               Team marketplace manifest
plugins/ifortyninestack/.cursor-plugin/       Plugin manifest
plugins/ifortyninestack/rules/                Persistent and file-scoped guidance
plugins/ifortyninestack/skills/               Task-specific workflows
plugins/ifortyninestack/agents/               Focused review and CI agents
docs/                                         Architecture and sources
scripts/                                      Local validation
```

## Sources

Ifortyninestack uses original engineering guidance and workflow patterns informed by pstack, Cursor Team Kit, Superpowers Rails planning ideas, Google developer documentation guidance, Simplified Technical English, and established Git commit guidance. See [Sources and attribution](docs/sources.md).

## License

MIT. See [LICENSE](LICENSE).
