---
name: technical-writing
description: Writes and reviews engineering prose in a concise Google developer documentation and Simplified Technical English style. Use for READMEs, guides, references, design notes, pull requests, commit messages, comments, or status updates.
---

# Technical writing

Write text that an engineer can understand on the first read.

## Choose the document type

- Tutorial. Teach by completing a concrete task. Give the learner a visible result after each step.
- How-to guide. Give the steps to reach a goal. Assume technical competence.
- Reference. State facts, options, limits, inputs, outputs, and errors. Do not persuade.
- Explanation. Explain a bounded design question, its constraints, and its tradeoffs.

Keep one primary type in each document. Split and link when a file tries to serve incompatible purposes.

## Write the first draft

- Lead with the result or purpose.
- Address the reader as `you` when giving instructions.
- Use active voice and present tense.
- Write instructions as commands.
- Put the condition before the instruction.
- Put the common case before exceptions.
- Use one thought or instruction in each sentence.
- Keep instructions near 20 words and other sentences near 25 words when that improves clarity.
- Use the shortest common word that preserves technical precision.
- Use the exact symbol, command, path, field, and domain name from the system.
- Use one name for each concept.
- Keep `only`, `not`, and other modifiers next to the words they change.
- Replace an ambiguous pronoun with the noun.
- Use periods instead of semicolons or em dashes.

## Edit

Remove:

- Preamble and repeated conclusions.
- Filler such as `in order to`, `it is important to note`, and `please note`.
- Slogans, aphorisms, metaphors, and marketing language.
- Unsupported certainty, praise, and emotional framing.
- `simply`, `easy`, and `quickly` in procedures.
- A comment that only narrates the next line of code.

Keep every warning, condition, risk, and uncertainty that affects a safe decision.

## Engineering artifacts

Name titles, commits, comments, and pull request bodies by what landed. Chat and rejected extras stay in chat.

Keep an absence only when a reviewer needs it to judge safety, compatibility, or a ticket-scope gap. Write that as one short fact.

For a commit:

- Follow the repository commit style.
- If the repository uses conventional commits, use `<type>(<scope>): <short imperative summary>`.
- Keep the subject concise and omit the final period.
- Separate the body with a blank line.
- Wrap the body near 72 characters.
- Explain the problem and reason. Let the diff explain routine mechanics.

For a pull request, use this order:

1. Problem.
2. What changed.
3. How to test.
4. Why it is safe to deploy.

For a paste-ready deliverable, return only the deliverable.
