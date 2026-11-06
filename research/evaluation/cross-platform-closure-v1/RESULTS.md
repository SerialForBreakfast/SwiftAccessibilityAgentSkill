# Native campaign results

Generated from [verified result index](results-index.json). 35 immutable attempts: 33 expected outcomes, 2 preserved unexpected failures. 161 unit-method executions include deliberate mutants and repeated/repaired assertions; they are not unique behaviors.

| Package | Revision | Selected positive methods | Negative controls | Recorded checks |
| --- | ---: | ---: | ---: | --- |
| ios-closure-v1 | 1 | 21 | 4 | 6/6 expected |
| macos-closure-v1 | 2 | 43 | 8 | 10/10 expected |
| tvos-closure-v1 | 1 | 43 | 8 | 10/10 expected |
| macos-closure-details-v1 | 1 | 7 | 2 | 4/4 expected |
| tvos-state-recovery-v1 | 2 | 12 | 1 | 3/3 expected |

23 current deliberate negative controls are distinct from accidental implementation defects. A negative-control pass means the intended assertion rejected the mutant.

## Runtime anchors

- macOS: runtime 27.0 (26A428); SDK 27.0 (26A425), deployment 26.0
- iOS: runtime 26.5 (23F77); SDK 27.0 (24A430), deployment 26.0
- tvOS: runtime 26.5 (23L470); SDK 27.0 (24J360), deployment 26.0

Exact compiler/Xcode fields and test identifiers are in the receipt index. Mac27 host execution is not Mac26 runtime evidence. TV26.5 does not establish TV27 Larger Text behavior.

## Interpretation

The initial Mac compile failure preserves incorrect Swift import names and an isolation warning. The TV cross-family recovery test preserves a genuine stale-label defect that isolated methods missed. Repaired sources and assertions are new revisions/packages, not rewritten history.

The recovered TV state package supersedes the original TV state example for retrieval. Its12 positive methods include10 requalified earlier contracts and2 new transition assertions. Do not add all12 to the previous totals as novel behavior. Native methods cover application/configuration contracts; no delivered speech, actual focus traversal or universal accessibility claim follows.

## Existing corpus

Earlier iOS and Mac/TV sources/receipts are retained and integrity-checked, not described as newly rerun. Current active companion method counts exclude superseded TV state copies: iOS223; macOS169; tvOS166. These counts include shared algorithms run on distinct platforms and are not independent behavioral coverage.

## Evaluation

Thirteen new platform-specific question/rubric pairs cover shared ownership principles, native text rotors, state, row semantics, keyboard entry points and transition recovery. Questions are development drafts. Outputs remain not-run; independent review and baseline eligibility are pending. No model calls, spend, UI tests or required manual verification.

## Attempt ledger

| Attempt | Outcome | Observation | Selected methods |
| --- | --- | --- | ---: |
| closure-detail-compile-r1 | passed | success | 0 |
| closure-detail-keyboard-disabled-r1 | passed | failure | 1 |
| closure-detail-positive-r1 | passed | success | 7 |
| closure-detail-row-selected-r1 | passed | failure | 1 |
| closure-ios-compile-r1 | passed | success | 0 |
| closure-ios-media-duplicate-r1 | passed | failure | 1 |
| closure-ios-media-identity-r1 | passed | failure | 1 |
| closure-ios-positive-r1 | passed | success | 21 |
| closure-ios-validation-generation-r1 | passed | failure | 1 |
| closure-ios-validation-snapshot-r1 | passed | failure | 1 |
| closure-mac-compile-r1 | failed | failure | 0 |
| closure-mac-compile-r2 | passed | success | 0 |
| closure-mac-media-duplicate-r2 | passed | failure | 1 |
| closure-mac-media-identity-r2 | passed | failure | 1 |
| closure-mac-modal-restore-r2 | passed | failure | 1 |
| closure-mac-positive-r2 | passed | success | 43 |
| closure-mac-state-text-r2 | passed | failure | 1 |
| closure-mac-text-boundary-r2 | passed | failure | 1 |
| closure-mac-text-stale-r2 | passed | failure | 1 |
| closure-mac-validation-generation-r2 | passed | failure | 1 |
| closure-mac-validation-snapshot-r2 | passed | failure | 1 |
| closure-recovery-compile-r2 | passed | success | 0 |
| closure-recovery-positive-r1 | failed | failure | 12 |
| closure-recovery-positive-r2 | passed | success | 12 |
| closure-recovery-stale-status-r2 | passed | failure | 1 |
| closure-tv-compile-r1 | passed | success | 0 |
| closure-tv-media-duplicate-r1 | passed | failure | 1 |
| closure-tv-media-identity-r1 | passed | failure | 1 |
| closure-tv-modal-restore-r1 | passed | failure | 1 |
| closure-tv-positive-r1 | passed | success | 43 |
| closure-tv-state-text-r1 | passed | failure | 1 |
| closure-tv-text-boundary-r1 | passed | failure | 1 |
| closure-tv-text-stale-r1 | passed | failure | 1 |
| closure-tv-validation-generation-r1 | passed | failure | 1 |
| closure-tv-validation-snapshot-r1 | passed | failure | 1 |
