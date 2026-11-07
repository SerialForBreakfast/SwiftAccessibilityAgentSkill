# Preserved Difficulties And Evaluation Consequences

These are authoring/tool observations, not controlled comparisons between models.
Known incidents belong in development cases, not new holdouts. Original sources,
diagnostics and run metadata remain recoverable; repairs do not replace them.

## F01: Async Work Inside A Synchronous Assertion Autoclosure

First test source:

```swift
let audio = try XCTUnwrap(try await item.asset.loadMediaSelectionGroup(for: .audible))
let text = try XCTUnwrap(try await item.asset.loadMediaSelectionGroup(for: .legible))
```

Compiler: `'async' call in an autoclosure that does not support concurrency`.
Production source typechecking passed; the XCTest target did not compile and ran
zero tests. Repair 1 awaits each load separately, then unwraps the returned value.
This is a Swift/XCTest diagnostic case, not new accessibility guidance.

The historical adapter reported `Incomplete or inconsistent unit evidence`. That
was safe (no pass credit) but insufficiently specific. Additive adapters classify
the same evidence as `test-source-compilation`, retaining zero credited tests.
The old adapters and original receipt remain unchanged.

## F02: Swift 6 Actor Isolation In Test Helpers

After the first repair, the compiler reported:

```text
sending 'audio' risks causing data races
sending 'text' risks causing data races
sending 'group.some' risks causing data races
```

The fixture callback was async but not explicitly `@MainActor`. The continuation
also transferred an `AVMediaSelectionGroup` as its result. Repair 2 makes the
callback explicitly main-actor-isolated and uses a `Void` continuation as a gate;
the loader returns the group from its actor-isolated closure. No unchecked
Sendable conformance was added to AVFoundation classes. The small test observation
flag is separately lock-protected. Both failed test-source revisions remain intact.

This is another general Swift/concurrency diagnostic case, not proof of an Apple
accessibility defect. There are at most two repairs for this compile contract.

## F03: Additive Adapter Self-Snapshot Omission

The new adapter initially tried to archive `platform-native.mjs` from a frozen
directory containing only the new adapter name. Preflight returned `ENOENT` and
stopped before compilation. The repair names the additive adapter itself; offline
regression checks pin that self-snapshot requirement. This is a harness packaging
failure, not a subject defect or successful negative control.

## F04: Incorrect Nil-Selection Oracle

The first executed positive suite asserted:

```swift
XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in: group))
```

The fixture instead exposed a selected forced English subtitle. The contract is
that a stale choice must not mutate the old item, not that the item starts with nil
selection. The correct oracle captures the initial selection and compares against
it after replacement. The initial code, exact diagnostic and native environment
are retained. This observation does not establish a universal platform default.

## Source-Audit Findings Before Native Execution

- An early cancellation branch called `cancel()` unconditionally when an old task
  finished. That could cancel a newer request. The first authored source is retained;
  ticket-scoped cancellation and a deliberate mutant check the actual contract.
- Calling AVFoundation from a binding setter did not itself invalidate the
  observable selection. An explicit observable revision plus an observation-tracking
  assertion covers store notification, not SwiftUI-rendered picker semantics.
- Prompt assertion partitioning initially overlapped one method between families.
  The current index partitions method IDs exactly once per platform. This is an
  evidence-index defect, not another accessibility behavior.
- Reload originally launched an unstructured task from the button. The final view
  uses a revision-keyed view task instead, and the store rejects an already-cancelled
  task before starting a new load. Source composition is compiled; the unit asserts
  the store guard, not delivery of SwiftUI lifecycle events.
- The first declaration extractor matched a deprecated neighbor's comment about
  the async loader. Its capture is preserved under `history/declarations-001/`.
  The corrected extractor requires an exact selector declaration and keeps its
  annotations. This is a source-indexing error, not evidence of API unavailability.

## Candidate Improvement Backlog

| Finding | Candidate lesson | Required evidence before promotion |
| --- | --- | --- |
| F01/F02 | Await outside synchronous assertion autoclosures; preserve actor isolation in test harnesses | General Swift diagnostic lane, not accessibility answer inflation |
| F03 | Freeze every adapter dependency, including the adapter itself | Offline regression and immutable failure receipt |
| F04 | Preserve native state instead of guessing defaults | Oracle review, native assertion and neutral preservation question |
| Cancellation | Old work cannot own newer state | Positive ownership test and intended cancellation mutant |
| Binding wiring | A native side effect and observable invalidation are separate contracts | Real native selection plus observation assertion |
| Forced tracks | Full-caption policy must distinguish forced-only options | Actual tagged fixture, accepted policy alternatives and source link |

These remain research findings. Released instructions and BigDog's sealed inputs
are unchanged. Successful unit tests do not establish measured model-answer lift.
