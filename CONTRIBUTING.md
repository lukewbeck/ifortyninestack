# Maintain Ifortyninestack

## Put guidance in the correct layer

Use an always-on rule only for a short requirement that applies to almost every task.

Use a file-scoped rule for a language or file type.

Use a skill for a workflow, detailed standard, tool sequence, or output format.

Use an agent for an independent review lens or monitoring task.

Prefer a test, script, lint, type, or runtime check when the requirement can be enforced.

## Write guidance

- State when the guidance applies.
- Use direct instructions.
- Write what to do. Name the current practice.
- Keep one concern in each rule.
- Keep `SKILL.md` under 500 lines.
- Put optional detail in a directly linked reference file.
- Do not copy repository-specific commands into the plugin.
- Do not add a source-system workaround for missing MCP authentication.
- Remove conflicting or obsolete guidance in the same change.

## Validate

Run:

```bash
python3 scripts/validate_plugin.py
```

Then load the plugin from `~/.cursor/plugins/local/ifortyninestack`, reload Cursor, and check **Customize**.

For a changed workflow, run one representative prompt and confirm that the expected skill loads. For a changed review agent, run it against a known diff and inspect false positives as well as missed issues.

## Release

1. Update the semantic version in `plugins/ifortyninestack/.cursor-plugin/plugin.json`.
2. Update documentation for changed behavior.
3. Run the validator.
4. Test the local install.
5. Open a focused pull request.
