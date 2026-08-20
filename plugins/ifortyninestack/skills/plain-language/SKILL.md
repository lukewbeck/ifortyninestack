---
name: plain-language
description: Rewrites the previous assistant response in simpler language without changing facts. Use for /plain-language, explain that simply, too dense, or when the user did not understand the prior response.
disable-model-invocation: true
---

# Plain language

Rewrite the most recent assistant response.

1. Do not answer a new question.
2. Do not use tools or add information.
3. Preserve every path, command, filename, number, URL, name, decision, warning, and uncertainty.
4. Replace jargon when a common word has the same meaning.
5. Define any technical term that must remain.
6. Remove preamble, repeated points, and unnecessary structure.
7. Use short paragraphs and a list only when the content is a real sequence or set.
8. Keep enough detail to prevent misunderstanding.

If there is no prior assistant response, state that there is nothing to rewrite.
