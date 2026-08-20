---
name: verify-change
description: Proves or disproves a concrete behavior claim with fresh evidence. Use for verify, prove it works, before-and-after checks, UI confirmation, performance claims, or release confidence.
---

# Verify a change

Verification tests a falsifiable claim. It does not restate the implementation.

## Method

1. Restate the claim with a condition, observable result, and threshold when one applies.
2. Choose the smallest surface that can disprove the claim.
3. Capture a baseline from the old or failing state when possible.
4. Capture the changed state with the same command, data, environment, and measurement method.
5. Compare the raw artifacts.
6. Check for confounding differences.
7. Return one verdict:
   - `VERIFIED`
   - `NOT VERIFIED`
   - `INCONCLUSIVE`

## Evidence

Use the surface that matches the claim:

- Focused test or reproduction script for code behavior.
- Request and response for an API.
- Browser interaction, screenshot, accessibility snapshot, or trace for a UI.
- Terminal transcript for a CLI.
- Before-and-after timing or profile for performance.
- Job state, retry evidence, and persisted records for background work.
- Migration output and schema inspection for database work.

## Output

State the verdict first. Then state the claim, baseline, changed result, difference, threshold, and any confound.

Do not convert a missing baseline, failed measurement, or wrong test surface into a pass.
