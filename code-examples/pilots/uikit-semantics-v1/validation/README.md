# UIKit semantic validation

Revision2 completed all five native checks on the local Apple worker:

| Check | Result |
| --- | --- |
| Library type-check | Passed |
| Positive unit suite | 23 passed,0 failed,0 skipped |
| Dropped callback | Intended assertion failure |
| Wrong rotor direction | Intended assertion failure |
| Lost unrelated traits | Intended assertion failure |

Each negative executes one focused test from the same test source used in the
positive suite. The three rejection results are separate from the23 positive
passes; they are not additional unique test behaviors.

[Revision2 records](revision-2.json) include manifest/result/log hashes, exact
toolchain/runtime metadata, selected/failed test IDs and sanitized assertion
excerpts. All evidence artifact hashes were checked before export. Full source,
manifest, adapter, command and result snapshots remain private, alongside raw
xcresult bundles. Self-contained ledger copies retain the hashed record artifacts.

Environment: Xcode27.0 build27A266a, Swift6.4, iOS SDK27.0 build24A430,
deployment target26.0, arm64, actual iOS26.5 runtime build23F77. Compile checks
make no runtime claim. Tests exercise UIKit objects and public callbacks, without
UI automation, global preference changes, network assets or model inference.

[Revision1 records](revision-1.json) preserve the initial22-test suite, positive
compile and three intended mutant failures. Its source package is archived at
`../history/revision-1/`. Revision2 adds initial rotor search coverage and optional
current-item handling. The earlier observations are not relabeled as revision2.

Across this expansion and the unchanged first UIKit pilot there are26 distinct
positive unit test methods. This count is not a measure of complete UIKit or
accessibility coverage. The [coverage ledger](../../../UIKIT-COVERAGE.md) identifies
remaining areas and separates framework observations from application policies.

All159 offline repository/harness tests passed, and all210 frozen baseline files
verified unchanged. No annual anchor or runtime skill integration is promoted.
Independent review of the new source bindings, example policies and assertions
remains pending. The dedicated simulator is shut down; no native job remains active.
