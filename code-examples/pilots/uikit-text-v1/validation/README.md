# UIKit text and metadata validation

All five native checks completed successfully against their declared expectations:

| Check | Result |
| --- | --- |
| Library type-check | Passed |
| Positive unit suite | 16 passed, 0 failed, 0 skipped |
| Incorrect text-range start | Intended assertion failure |
| Retained obsolete matches | Intended assertion failure |
| Omitted edit category | Intended assertion failure |

[Structured evidence](revision-1.json) includes exact manifest/result/log hashes,
toolchain/runtime identity, selected/failed test IDs and sanitized excerpts. Every
referenced artifact hash was verified before export. Full source/adapter snapshots,
logs, commands and xcresult bundles remain private; validated record artifacts were
also copied into the immutable local ledger.

Environment: Xcode 27.0 build 27A266a, Swift 6.4, iOS SDK 27.0 build 24A430,
deployment target 26.0, arm64, actual iOS 26.5 runtime build 23F77. Compile checks
do not claim runtime execution. No UI automation, downloads or model calls occurred.
The dedicated simulator is shut down and no native job remains active.

These tests observe real UITextRange extraction, action metadata/ownership, control
bounds and font metrics. Literal search/restart behavior is example policy; the
results do not establish spoken navigation, rotor-menu presentation or visual fit.

The library now has 57 distinct positive UIKit test methods across four packages.
All indexed packages have per-test source-claim maps, including the original
three-example pilot. Its added map does not modify or rerun historical evidence.
All 161 offline tests passed; 210 frozen baseline files verified unchanged.

Independent review and anchor promotion remain separate. SwiftUI expansion is
deferred, and the frozen skill and benchmark inputs were not edited.
