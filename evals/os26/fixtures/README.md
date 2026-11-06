# OS26 unit fixture preparation: not gold-ready

**6 candidates, 12 single-error variants, 6 focused unit tests.**

Revision `os26-fixtures-unit-2` implements code-contract revision4. Promotion
requires recorded native outcomes and independent source/assertion review. The
manifest records expected outcomes, not results. Read the dated validation reports
in the parent directory for actual execution status.

## Native validation

Run from the repository root using installed Xcode and installed iOS26/tvOS26
Simulator runtimes. No model inference, downloads or UI-test targets are involved.
The Swift package has no external dependencies and declares deployment target26.0.

```sh
# Inspect the 18-job plan without executing anything.
node evals/runner/os26-native.mjs

# Select installed destinations and a NEW private output directory.
xcrun simctl list devices available
node evals/runner/os26-native.mjs --execute \
  /private/tmp/os26-unit-run IOS26_DEVICE_UUID TVOS26_DEVICE_UUID

# Assemble a complete matrix; independent review remains pending.
node evals/runner/os26-native-receipts.mjs /private/tmp/os26-unit-run
node evals/runner/os26.mjs status \
  /private/tmp/os26-unit-run/native-evidence-pending-review.json
```

The runner uses Xcode's package test scheme and its required test host. It does
not require a separately authored app, poster asset or interaction walkthrough.
`Host/FixtureApp.swift` remains an optional demonstration outside the package.

Jobs run serially in a disposable copy. Each candidate runs before its two
mutations, using the same selected test. The runner restores the candidate after
each variant and never mutates this checkout. A job is bounded to ten minutes;
crashes, build errors, timeouts, skipped tests and unclassified failures stop the
run. Expected assertion failures are retained in logs and xcresult bundles;
automatic extended diagnostic collection is disabled to avoid blocking on those
intentional failures. All outputs contain local paths and remain private.

## Evidence scope

Three UIKit tests cover exposed-control configuration, callback independence,
same-instance reuse and font/layout prerequisites. Three SwiftUI tests exercise
the exact production action handlers and binding used by the controls. They check
correct IDs, action counts and state updates. They do not simulate focus, gestures,
VoiceOver or visual layout. Source review checks that the controls remain wired to
the tested production paths. Equivalent implementations remain acceptable; helper
names and reference implementation structure are not answer requirements.

The receipt assembler verifies matrix completeness, variant/log/intent identity
and consistent test selection. It derives Xcode/SDK identity from captured files
and deliberately leaves review gates pending. Independent reviewer approval must
name the exact revision and evidence examined. A passing unit matrix alone does
not promote the prompts or authorize Gemini execution.

See [source/assertion review](../SOURCE-REVIEW-R4.md) and
[acceptance gates](../acceptance.json). The earlier preparation instructions and
interaction checklist are preserved in
[the draft3 archive](../archive/os26-code-contract-3/FIXTURE-PREPARATION.md);
they are historical, not current requirements.

Offline checks:

```sh
node --test evals/runner/os26-fixtures-test.mjs \
  evals/runner/os26-native-receipts-test.mjs evals/runner/os26-test.mjs
```
