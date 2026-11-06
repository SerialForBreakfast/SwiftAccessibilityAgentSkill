# Version-anchored example infrastructure

Initial offline implementation of [ADR-003](../research/adr/ADR-003-version-anchored-unit-tested-examples.md).
This directory is not integrated with skill routing. No example library or annual
anchor is promoted yet. Existing OS26 evaluation fixtures remain separate and
unchanged by this library. The separate OS26 gold fixtures now have a
[reviewed closeout](../evals/os26/reports/2026-11-05-gold-closeout/REVIEW.md);
that approval does not promote these library examples.

## Available now

[Mac navigation and Apple TV results](../research/evaluation/platform-navigation-v1/README.md)
adds 34 positive methods across table selection, key-view ownership, filtered result
actions and motion-independent status. Four question/rubric pairs are draft; the
native batch is executed. Prior example packages and results remain unchanged.

[AppKit and tvOS expansion](../research/evaluation/platform-expansion-v1/README.md)
adds separate platform packages, a native adapter and opt-in retrieval candidate.
These live under `platforms/`, outside the frozen iOS pilot/campaign selection.
The Mac host anchor is27; tvOS uses the existing26.5 simulator. This does not imply
Mac26 runtime coverage or promote OS27 skill guidance. SwiftUI expansion stays deferred.

[Ordinary playback-speed choices](pilots/uikit-speed-v1/README.md) supplies the
speed-control gap identified by the media clause audit: eight positive unit methods,
three rejected mutants, ordinary button events and explicit selected-state metadata.
Its independent question/rubric remains draft; no playback or speech is claimed.

[Clause-level requirements audit](audits/requirements-v1/README.md) preserves209
selected clauses across all15 UIKit guidelines. Its first media review identified
the speed-control contract now addressed by UPAIR-06C; diagnostic playback-rate
tests were not relabeled as control tests. The remaining clause reviews and full API matrix are still in progress.

[Availability compile sweep](audits/availability-v1/README.md) pins all seventeen
current pilot source sets and their successful deployment26.0 type checks.
Historical media deprecation warnings remain recorded; the complete declaration
matrix and final inventory audit are still pending. Its prompt/rubric is a draft.

[Audio-description metadata and loaded assets](pilots/uikit-media-metadata-v1/README.md)
adds actual tagged/untagged MOV extraction, selected-option observation, duration
and missing/error-state tests. The matched synthetic fixture establishes metadata
recognition, not narration quality. Its draft prompt/rubric remains independent of
the implementation; first-attempt deprecation evidence and repair are preserved.

[Media inspection: time and buffering](pilots/uikit-media-inspection-v1/README.md)
adds a separate UPAIR-06A example and draft prompt/rubric. It distinguishes
duration states, discontinuous seekable/loaded ranges and independent playback
flags. The separate metadata packet above supplies local loaded-asset evidence;
neither packet tests live playback or assistive-technology interaction.

[Edited documents and rotor ranges](pilots/uikit-edited-rotor-v1/README.md) adds
UTF16/whole-grapheme matching, explicit overlap policy, revision-safe callbacks
and ordinary text-access checks. Its prompt and rubric remain separate drafts;
the native report records what was executed without changing frozen skill inputs.

[Modal contents and restoration requests](pilots/uikit-modal-v1/README.md) adds
completion ordering, exact prior-state restoration and stale-callback controls.
Its history preserves a real retained-but-removed target regression discovered
after a green suite, alongside the repair and a separate developer question/rubric.

[Configured color contrast](pilots/uikit-contrast-v1/README.md) adds a bounded
opaque-color calculator with explicit trait resolution, color-space conversion,
separate W3C numerical provenance and a draft independent question/rubric. Its
validation packet records native outcomes; it remains outside skill routing and
frozen model-evaluation inputs.

Completed native tranche: [long text and non-color choice state](pilots/uikit-choice-v1/README.md),
with nine unit contracts, four deliberate defects and a separately pinned developer
prompt/controller rubric. It supplements the historical index without changing the
skill or frozen evaluation inputs. Native results are recorded in its validation
packet; independent gold review and model evaluation remain separate gates.

New paired tranche: [decorative content and independent named controls](pilots/uikit-naming-v1/README.md),
with a separate draft developer prompt/rubric and difficulty ledger. It is linked
here rather than altering the index pinned by the historical evidence packet.
It remains outside runtime skill routing and frozen model-evaluation inputs.

### Latest validation and next gate

The media metadata subtranche passed one compile check and seven positive unit
tests on iOS26.5, and rejected three deliberate defects at their intended assertions.
[Native evidence](pilots/uikit-media-metadata-v1/validation/README.md),
[difficulty ledger](pilots/uikit-media-metadata-v1/DIFFICULTIES.md), and
[exact mutation diffs](pilots/uikit-media-metadata-v1/MUTATIONS.md) preserve the results.
The first-attempt locale deprecation warning and revision2 repair are retained.
Actual local tagged-asset extraction is now covered; narration quality and live
playback are not inferred from those unit assertions.

The [draft developer question](pilots/uikit-media-metadata-v1/evaluation/prompt.json) and
[controller rubric](pilots/uikit-media-metadata-v1/evaluation/controller.md) need independent
review before gold promotion. Keep the controller material out of model inputs.
Model execution and skill improvement claims remain separate, uncompleted gates.
The combined offline library/evaluation suite currently passes 201 tests, including
media inspection, edited rotors, contrast and modal history/evidence-contract checks; this count
does not include native XCTest methods or imply additional gold readiness.
See [current successes, change inventory and next steps](../research/evaluation/failure-driven/CURRENT-STATUS.md)
for the seven-packet rollup and the uncommitted checkpoint since `6cdaa0b`.

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
