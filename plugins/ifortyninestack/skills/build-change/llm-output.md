# LLM output behavior

If the defect is wording, capitalization, spelling, tone, format, or a missing field, fix the source prompt or schema first.

Check, in order:

1. Prompt templates and system instructions.
2. Structured output schemas.
3. Parser schemas and format examples.
4. Representative examples and evaluation cases.

Do not add Ruby or TypeScript string transforms to repair model prose. Post-processing hides the source defect and creates another contract.

Use parsing code only for a real wire format, structured data parsing, security sanitization, or another hard boundary.

Add one focused evaluation or test that demonstrates the expected output and a meaningful failure case.
