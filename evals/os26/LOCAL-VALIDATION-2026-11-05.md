# Local OS26 validation

Owner assigned fixture implementation and native validation to this Mac. BigDog
confirmed this in `bigdog-swift-sillycon-validation-owner-20261105-r1` (project
cursor1393), superseding its earlier fixture-author/MaxMini proposal. BigDog has
not started overlapping implementation. Local acceptance is stored at cursor1394.
BigDog will independently review locally authored changes; original BigDog-authored
fixtures require separate local source/assertion review, not automatic approval.

## Initial native result

Source: commit `31742c6db9fe5b14871827af9d189061243d5788`.
The only preexisting untracked file was the local coordinator record.

| Configuration | Observed value |
| --- | --- |
| Xcode | 27.0, build27A266a |
| Swift | 6.4, swiftlang-6.4.0.34.1 |
| Compile SDK | iOS Simulator27.0 |
| Declared deployment target | iOS26.0 |
| Actual runtime | iOS26.5, build23F77 |
| Destination | iPhone17 simulator, arm64 |
| Scheme | OS26Fixtures |
| Result | 3 passed, 0 failed, 0 skipped; xcodebuild exit0 |

The installed SDK is27, not26. These are genuine OS26.5 runtime results compiled
with SDK27; they do not establish compilation with SDK26 or behavior on26.0.
tvOS26.5 build23L470 is installed but was not exercised in this run.

Passed tests:

- `UIKitTests/testSettingsCallbacksAndExposedControls`
- `UIKitTests/testReconfigurationWithoutPrepareForReuse`
- `UIKitTests/testCheckoutCallbackAndResizePrerequisites`

The checkout test took about121 seconds; other tests took under a second. Preserve
this timing anomaly when planning bounded mutation runs; do not describe it as a
fast fixture yet. No runtime warning or failure was reported by the xcresult summary.

## Reproduction and retained evidence

From `evals/os26/fixtures`, using a fresh evidence destination:

```sh
xcodebuild test -scheme OS26Fixtures \
  -destination 'platform=iOS Simulator,id=<installed-iOS26-device-id>' \
  -derivedDataPath <private-derived-data> \
  -resultBundlePath <new-private-result>.xcresult \
  -parallel-testing-enabled NO CODE_SIGNING_ALLOWED=NO
```

Actual private run directory: `/private/tmp/swift-os26-native-20261105/`.
Contains `UIKit-initial.log`, `UIKit-initial.xcresult`, `UIKit-summary.json`,
retrieved source pages and build products. Raw logs contain local paths and remain
outside Git. Temporary storage is not an archive; retain a sanitized evidence
bundle before promotion or cleanup. No UI-test target or manual verification ran.

- UIKit test source SHA-256: `70b37699500d8b64e74e640ae4ca88352dc0ca6454be4c815cf3a2cecae6eb3e`.
- Build/test log SHA-256: `2e1b7a3ce72233e56686f856cb30548a6a0e45d84b09e97654740daeb9b22e02`.

## Source-review progress

Retrieved Apple's Markdown documentation on2026-11-05; supporting excerpts were
read, not merely the JavaScript shell pages.

- [prepareForReuse discussion](https://developer.apple.com/documentation/uikit/uitableviewcell/prepareforreuse%28%29): content must be refreshed during configuration, and reconfiguration can bypass reuse preparation. Supports the same-instance A/B assertion. It does not require the reference fix's exact label wording.
- [Font-size adjustment discussion](https://developer.apple.com/documentation/uikit/uicontentsizecategoryadjusting/adjustsfontforcontentsizecategory): automatic updates require suitable preferred/scaled fonts. Supports testing both font configuration and automatic adjustment; does not prove visual fit.

This is partial review, not completed source-review receipts for all six fixtures.

## Remaining promotion work

1. Record executed test IDs and pinned source/fixture identities in gate receipts.
2. Run original UIKit mutations in disposable copies against the same tests; classify
   expected assertion failures separately from build/launch errors.
3. Implement SwiftUI production-path tests and versioned unit-observable mutations
   for GP26-04/05/06, preserving old files and accepted alternative fixes.
4. Run iOS/tvOS unit evidence with bounded process deadlines and nonzero-test checks.
5. Complete independent source/assertion review and BigDog review of new local code.
6. Assemble actual42gate evidence and re-run promotion; currently0/6 gold-ready.

Gemini allocation and execution remain separate. No provider call or download was
performed. No test result establishes spoken output, input delivery or visual layout.
