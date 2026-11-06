# Container and action-hook validation

Revision2 completed all five checks against their declared expectations:

| Check | Result |
| --- | --- |
| Library type-check | Passed |
| Positive unit suite | 13 passed, 0 failed, 0 skipped |
| Incorrect spanning-cell lookup | Intended assertion failure |
| Retained modal flag after dismissal | Intended assertion failure |
| Ignored disabled-activation guard | Intended assertion failure |

[Revision2 evidence](revision-2.json) includes verified manifest/artifact hashes,
toolchain/runtime identity, exact selected/failed tests and sanitized excerpts.
[Revision1 evidence](revision-1.json) preserves the initial successful positive
suite and the rejected `XCTFail` representation. See [history](../history/README.md)
for the test-only revision; production code and adapter safeguards did not change.
Both complete raw evidence sets are retained in separate private immutable ledgers.

Environment: Xcode27.0 build27A266a, Swift6.4, SDK27.0 build24A430,
deployment26.0, arm64, iOS26.5 build23F77. Compile-only results do not imply
runtime execution. The dedicated simulator is shut down.

This adds13 unique positive methods, bringing the library to78 across six packages.
All161 offline harness tests pass; all210 frozen baseline files remain intact.
No UI automation, model calls, downloads, paid runs or runtime skill edits occurred.

Evidence covers configured data-table metadata and direct action hooks, not screen
geometry, spoken navigation or gesture delivery. Independent review and annual
anchor promotion remain separate requirements.
