# Version-anchored example infrastructure

Initial offline implementation of [ADR-003](../research/adr/ADR-003-version-anchored-unit-tested-examples.md).
This directory is not integrated with skill routing. No example library or annual
anchor is promoted yet. Existing OS26 evaluation fixtures remain separate and
unchanged while independent review is pending.

## Available now

- Manifest/result contracts with source and evidence hashes, Apple claim links,
  explicit compile/unit lanes, platform/target/runtime checks and scoped negatives.
- Offline plan inspection and append-only private evidence storage.
- Synthetic tests for malformed evidence, path confinement and immutable records.
- An explicit, bounded iOS native adapter and [three-example UIKit pilot](pilots/uikit-v1/README.md).
- A [UIKit semantic expansion](pilots/uikit-semantics-v1/README.md) and
  [UIKit-first coverage ledger](UIKIT-COVERAGE.md). SwiftUI testing is deferred.
- [Dynamic UIKit content and action reuse](pilots/uikit-dynamic-v1/README.md),
  including native UIAction identifier replacement/removal checks.
- [Text-range rotors and metadata](pilots/uikit-text-v1/README.md), including
  real UITextRange selection, native control bounds and broader font metrics.
- [Preferences and non-color cues](pilots/uikit-preferences-v1/README.md), including
  reduced-motion policy, explicit semantic-color resolution and form-state reset.
- [Containers and action hooks](pilots/uikit-containers-v1/README.md), including
  data-table spans/header metadata, activation results and modal overlay teardown.
- [Reuse and configuration transitions](pilots/uikit-reuse-v1/README.md), including
  collection reconfiguration, language metadata, nested sections and trait-aware fonts.
- [UIKit/AVKit media contracts](pilots/uikit-media-v1/README.md), including local
  authored-language options, forced-only variants, selection and control metadata.
- [UIKit lifecycle contracts](pilots/uikit-lifecycle-v1/README.md), including private
  notification-center refresh/ownership and state-dependent presentation/actions.

```sh
node --test code-examples/tools/*.test.mjs
node code-examples/tools/cli.mjs plan /path/to/manifest.json
node code-examples/tools/cli.mjs record /path/to/manifest.json \
  /path/to/result.json /private/tmp/example-ledger
```

Both `cli.mjs` modes report `execution: false`. They do not launch compilers, simulators,
models or commands embedded in a record. `cli.mjs` has no execute mode; there is no MCP endpoint.
No dependencies or downloads are needed beyond Node with its built-in test runner
for these offline modes. The separate `native.mjs execute` entry point requires
reviewed local source, installed Xcode and an actual installed runtime for unit tests.

## Manifest contract, schema1

The executable contract is in [contracts.mjs](tools/contracts.mjs). Fully populated
synthetic examples are built in [its tests](tools/contracts.test.mjs); these are
harness data, not Apple claims or native validation evidence.

| Field | Requirement |
| --- | --- |
| `schema`, `id`, `revision` | Schema1 and stable non-path identifiers |
| `platform`, `deploymentTarget`, `runtimeMajor` | Actual target family, explicit deployment version and selected runtime major |
| `limitations` | Bounded observation scope |
| `claims[]` | Unique ID, statement, Apple HTTPS URL, supporting section, review date and availability description |
| `files[]` | Unique relative path and SHA-256 for each source/test input; paths resolve inside the manifest directory |
| `checks[]` | Unique ID, `compile` or `unit` lane, referenced claim IDs, expected `success` or `failure` |
| `testIds` | Exact unit selection; empty for compile checks |
| `failureIds` | Exact intended failed test IDs or normalized compiler diagnostic IDs; empty for positive checks |
| `skipCondition` | Optional predeclared inapplicability reason; not an escape for unexpected failure |

A native adapter must include all inputs in `files`, capture toolchain identity,
and map compiler diagnostics to reviewed IDs with provenance. The initial iOS
adapter parses actual diagnostic lines and preserves raw output; only the pilot's
specific type-error mapping is currently qualified. A caller-supplied diagnostic
ID alone is not independent proof that the compiler emitted it.

## Result contract, schema1

Results bind the SHA-256 of the exact manifest bytes and one check ID. Required
provenance includes a unique run ID, timestamp, source revision and `maintainer`,
`user-rerun` or `synthetic` origin. Synthetic records never count as Apple evidence.

Executed results include the recorded argv (not executed by this tool), artifact
hashes and toolchain fields: platform, deployment target, Xcode, compiler, SDK
version/build, architecture and destination type. Unit results require an actual
runtime version/build matching the selected major. Compile-only results set both
runtime fields to null. No version flag emulates an OS.

`execution` records exit code, signal, infrastructure error, build outcome, exact
executed/failed test IDs, diagnostic IDs and skipped-test count. A successful unit
check requires a successful build, the exact nonempty test selection, no skips
and no infrastructure failure. Negative checks pass only when the observed failure
IDs exactly match the predefined ones. Unrelated failures and surviving mutations
are retained as failed expectations.

`status` is `passed`, `failed`, `skipped`, `blocked` or `error`. `observed` remains
`success` or `failure` for executed checks, so an expected-negative pass still
discloses the actual failure. Non-assessed outcomes require a reason and
`observed: not-assessed`; they never establish a capability result. Skips require
the predeclared condition. Missing runtimes are blocked, not passes.

## Immutable ledger

`record` validates the manifest and result, creates a fresh run directory, copies
hashed evidence into it and writes `result.json` last. Existing run IDs, including
symlinks, are rejected. Removing the original temporary artifacts does not break
the saved record. Interrupted writes may leave an incomplete directory: preserve
it and use a new run ID rather than overwriting it. Artifacts and ledger roots
should be private; copying is not sanitization.

These checks establish structural integrity and honest outcome classification,
not authenticity of arbitrary external reports. Source/code review and native
adapter qualification remain necessary. Successful tests never refresh a source's
review date or promote an anchor automatically. Annual current/previous anchor
selection and retrieval integration remain separate maintainer decisions.

## Pilot and next gate

The [pilot manifest](pilots/uikit-v1/manifest.json) binds three UIKit examples,
tests and isolated negatives to documented claims. Its native adapter rejects
wrong destinations, incomplete test evidence and unclassified failures. Pilot
execution is distinct from prior evaluation-fixture evidence and does not promote
an anchor. Independent review of this adapter/library remains the next gate.
No UI tests, mandatory manual verification, automatic minor-version matrix or
runtime skill changes are part of this infrastructure.
