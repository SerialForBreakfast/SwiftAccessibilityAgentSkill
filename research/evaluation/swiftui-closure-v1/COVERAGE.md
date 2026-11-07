# Coverage Dispositions

The original 217-clause ledger and 15 rules remain immutable. This overlay accounts
for each clause, links prior passing assertions to receipt hashes, and distinguishes
the bounded native-forwarding subset from framework-generated behavior.

| Disposition | Requirements | Meaning |
| --- | ---: | --- |
| Compile-checkable | 80 | Existing target compositions; not whole-prose runtime proof |
| Documentation-supported outside unit scope | 114 | Generated semantics, rendering, traversal, speech or delivered focus |
| Partially covered native subset | 13 | Explicit native metadata/action/configuration already tested |
| Directly unit-testable application subset | 8 | Original named application assertions, not an entire accessibility promise |
| Partially covered with testable remainder | 1 | G-015-L32: media choices have ownership; broader live-stream observer lifecycle remains open |
| Deferred version-specific | 1 | OS27 generated-subtitle/style/device behavior is not promoted by OS26-targeted tests |

These categories are accounting dispositions, not a percentage of universal
accessibility correctness. All 28 previously unresolved clauses now have explicit
reasons. Reclassifying a clause as outside unit scope does not validate it by test,
nor require a human/UI-testing gate. The source documentation supports that scope.

## Implementation Queue

The actionable gap selected for this batch is real media selection and its SwiftUI
binding/async ownership. Existing semantics, documents, preferences, lifecycle,
forms and native-forwarding packages already exercise their named state/configuration
contracts; they were not rebuilt solely because an older ledger said unresolved.

One remaining implementation contract stays visible: a supplemental live stream-state
observer with item rebinding and deterministic teardown. Existing native inspection
snapshots are useful evidence, but neither those snapshots nor this new options
store prove that observer lifecycle. It is not relabeled as documentation-only.

Broad mixed-host semantics and rendered results remain outside the unit-only lane.
OS27 generated subtitles remain a version-specific research item. No historical
rule is silently declared completely proven, and no new holdouts are claimed.

See [full ledger](coverage-ledger.json), [source declarations](declarations.json)
and [paired cases](prompt-records.json). Exact SDK annotations, deployment targets
and recorded runtime anchors are separate evidence dimensions. A nearby header
comment is not an API introduction annotation.
