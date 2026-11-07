# V2 source/applicability review

Author-scoped resolution, not independent acceptance or a model-quality result. All
24 requests, candidate system messages and generic baselines retain their v1 bytes.

| Case | V2 resolution | Supported scope |
| --- | --- | --- |
| macos-swiftui-state | replace-ios-only-guide-with-target-sdk-card | Declared API availability and recorded composition compilation only |
| macos-swiftui-text | replace-ios-only-guide-with-target-sdk-card | Declared API availability and recorded composition compilation only |
| macos-swiftui-lifecycle | replace-ios-only-guide-with-target-sdk-card | Declared API availability and recorded composition compilation only |
| tvos-swiftui-actions | replace-ios-only-guide-with-target-sdk-card | Declared API availability and recorded composition compilation only |
| tvos-swiftui-structure | replace-ios-only-guide-with-target-sdk-card | Declared API availability and recorded composition compilation only |
| macos-appkit-testing | remove-mandatory-manual-workflow-from-unit-only-context | Project compile/unit evidence policy, not Apple interaction-validation requirements |
| tvos-swiftui-testing | replace-wrong-topic-ios-guide-with-project-testing-note | Project compile/unit evidence policy, not Apple interaction-validation requirements |

## Changed candidate contexts

| Case | Context profile | V1 input bytes | V2 input bytes |
| --- | --- | ---: | ---: |
| macos-appkit-testing | C2-project-policy-only | 9017 | 5925 |
| macos-swiftui-state | C2-sdk-scoped | 8497 | 6903 |
| macos-swiftui-text | C2-sdk-scoped | 8484 | 7860 |
| macos-swiftui-lifecycle | C2-sdk-scoped | 8594 | 6982 |
| tvos-swiftui-actions | C2-sdk-scoped | 8128 | 7090 |
| tvos-swiftui-structure | C2-sdk-scoped | 8625 | 6884 |
| tvos-swiftui-testing | C2-project-policy-only | 8628 | 5926 |

Five target-specific SDK cards replace iOS-only guidance. The tvOS testing scope
warning is resolved by using the already reviewed project-policy note instead of
an unrelated iOS lists/forms guide. The macOS testing reference removes the manual-
verification mandate. None of these changes claims actual interaction validation.

Two preexisting OS27 media addenda remain explicitly flagged for version-aware
interpretation, not assumed deployment26 functionality. The four quarantines and
32 deferred cases remain unchanged. No model call or promotion is authorized.
