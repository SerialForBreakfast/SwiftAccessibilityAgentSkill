# SwiftUI native results

[Validated receipts](results-index.json): 18 unique attempts, 17 expected outcomes and 1 retained unexpected outcomes. 257 unit-method executions include repaired, repeated and deliberate-defect executions; not independent behavioral coverage.

| Lane | Current selected methods | Recorded current checks |
| --- | ---: | --- |
| SwiftUI/macOS | 62 | 9/9 expected |
| SwiftUI/iOS | 62 | 3/3 expected |
| SwiftUI/tvOS | 62 | 3/3 expected |

Seven development families; 62 method definitions run on 3 platforms, not 186 independent behaviors. Nine shared/platform coordinator mutant runs plus the original AppKit target defect form 10 intended rejection receipts. The seven standard mutation patterns run on Mac, with coordinator mutation repeated on iOS and TV; the supplemental original-target control is Mac-only.

## Anchors
- iOS: runtime 26.5 (23F77); SDK 27.0 (24A430), target 26.0
- macOS: runtime 27.0 (26A428); SDK 27.0 (26A425), target 26.0
- tvOS: runtime 26.5 (23L470); SDK 27.0 (24J360), target 26.0

Actual modifier compositions compile; unit packages use Swift tools 6.0 and standalone compile retains adapter default language mode. Neither proves generated SwiftUI semantics, framework callback installation or environment propagation. The coordinator tests directly invoke actual native dispatch and public dismantle, not private SwiftUI introspection.

## First failures
The initial 52-method source set compiled but was not unit-executed. The first complete 61-method Mac suite built and ran, failing old native-target dispatch and immediate weak lifetime. Repair 1 detached the old AppKit target and corrected the oracle's autorelease boundary; the final 62-method suite adds an independent native lifetime control. Exact first source and diagnostics remain recoverable. No second repair was needed for those contracts. Source-audit integration findings are distinct from native failures.

## Scope and acceptance
All 15 rules / 217 requirements are dispositioned; unresolved broad interop and real-media application requirements remain visible. 21 task/rubric pairs are drafts with no independent subject answers. Independent review is pending, not accepted. No model calls or skill promotion follows from green tests.

## Attempt ledger
| Attempt | Status | Observed | Methods executed |
| --- | --- | --- | ---: |
| swiftui-ios-compile-r3 | passed | success | 0 |
| swiftui-ios-interop-r3 | passed | failure | 1 |
| swiftui-ios-positive-r3 | passed | success | 62 |
| swiftui-mac-compile-r3 | passed | success | 0 |
| swiftui-mac-documents-r3 | passed | failure | 1 |
| swiftui-mac-forms-r3 | passed | failure | 1 |
| swiftui-mac-interop-r3 | passed | failure | 1 |
| swiftui-mac-lifecycle-r3 | passed | failure | 1 |
| swiftui-mac-media-r3 | passed | failure | 1 |
| swiftui-mac-positive-r3 | passed | success | 62 |
| swiftui-mac-preferences-r3 | passed | failure | 1 |
| swiftui-mac-semantics-r3 | passed | failure | 1 |
| swiftui-tv-compile-r3 | passed | success | 0 |
| swiftui-tv-interop-r3 | passed | failure | 1 |
| swiftui-tv-positive-r3 | passed | success | 62 |
| swiftui-mac-compile-r1 | passed | success | 0 |
| swiftui-mac-old-target-r1 | passed | failure | 1 |
| swiftui-mac-positive-r2 | failed | failure | 61 |
