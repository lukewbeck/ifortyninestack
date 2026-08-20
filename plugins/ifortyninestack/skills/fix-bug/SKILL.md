---
name: fix-bug
description: Reproduces, diagnoses, fixes, and verifies a Rails or React defect. Use for bugs, regressions, crashes, wrong output, flaky behavior, or customer-reported failures.
---

# Fix a bug

## Reproduce

1. State the observed behavior and the expected behavior.
2. Reproduce the defect on the same surface where it occurs.
3. Capture the smallest reliable failing artifact. Use a test, request, screenshot, trace, log, or script.
4. If the defect does not reproduce, instrument the path or tighten the conditions. Do not implement a speculative fix.

## Diagnose

1. Trace the runtime path and recent changes.
2. List plausible causes.
3. Test the split that removes the most uncertainty.
4. Continue until one mechanism explains the evidence.
5. Separate the confirmed cause from contributing conditions and unrelated findings.

## Fix

1. Add the failing regression test first when practical.
2. Make the smallest change that fixes the confirmed cause.
3. Do not add broad rescues, retries, null guards, or string transforms unless the evidence requires them.
4. Keep unrelated cleanup out of the change.

## Verify

1. Run the original reproduction against the fix.
2. Run the focused regression test and nearby relevant checks.
3. Compare before and after artifacts.
4. Report the defect, cause, fix, evidence, and remaining uncertainty.

A test that exercises a branch is not enough when the defect is visible only in a browser, worker, external integration, or deployed runtime. Verify on the matching surface when it is available.
