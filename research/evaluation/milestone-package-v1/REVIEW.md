# Milestone selection review

Proposed only. Exact payloads are sealed; every selected question still needs independent
review and source applicability checks. Original questions/rubrics remain unchanged.

| Case | Platform/framework | Related family | Candidate context | Input bytes generic/candidate |
| --- | --- | --- | --- | ---: |
| ios-uikit-actions | iOS/UIKit | topic/actions | C2 | 1086 / 7955 |
| ios-uikit-state | iOS/UIKit | topic/state | C2 | 1180 / 8232 |
| ios-uikit-text | iOS/UIKit | topic/text | C2 | 1124 / 8316 |
| ios-swiftui-semantics | iOS/SwiftUI | topic/semantics | C2 | 1112 / 8456 |
| ios-swiftui-lifecycle | iOS/SwiftUI | topic/lifecycle | C2 | 1131 / 8592 |
| ios-swiftui-media | iOS/SwiftUI | topic/media | C2 | 1132 / 9516 |
| macos-appkit-actions | macOS/AppKit | topic/actions | C2 | 1089 / 8623 |
| macos-appkit-structure | macOS/AppKit | topic/structure | C2 | 1119 / 8287 |
| macos-appkit-testing | macOS/AppKit | topic/testing | C2 | 1129 / 9017 |
| macos-swiftui-state | macOS/SwiftUI | topic/state | C2 | 1184 / 8497 |
| macos-swiftui-text | macOS/SwiftUI | topic/text | C2 | 1128 / 8484 |
| macos-swiftui-lifecycle | macOS/SwiftUI | topic/lifecycle | C2 | 1133 / 8594 |
| tvos-uikit-state | tvOS/UIKit | topic/state | C2 | 1182 / 8563 |
| tvos-uikit-media | tvOS/UIKit | topic/media | C2 | 1132 / 9848 |
| tvos-uikit-lifecycle | tvOS/UIKit | topic/lifecycle | C2 | 1131 / 8975 |
| tvos-swiftui-actions | tvOS/SwiftUI | topic/actions | C2 | 1090 / 8128 |
| tvos-swiftui-structure | tvOS/SwiftUI | topic/structure | C2 | 1120 / 8625 |
| tvos-swiftui-testing | tvOS/SwiftUI | topic/testing | C2 | 1130 / 8628 |
| ios-uikit-no-change | iOS/UIKit | control/preservation | C1 | 645 / 4210 |
| ios-swiftui-no-change | iOS/SwiftUI | control/preservation | C1 | 639 / 4204 |
| macos-appkit-no-change | macOS/AppKit | control/preservation | C1 | 619 / 4184 |
| mixed-macos-owner | macOS/mixed | control/ownership | C1 | 664 / 4229 |
| ios-missing-reference | iOS/UIKit | control/unavailable-reference | C1 | 657 / 4222 |
| tvos-version-boundary | tvOS/UIKit | control/version-boundary | C1 | 665 / 4230 |

## Quarantined

- macos-appkit-text: Primary-source mapping unresolved.
- macos-appkit-media: Primary-source mapping unresolved.
- tvos-uikit-text: Primary-source mapping unresolved.
- tvos-uikit-semantics: Standard-switch premise needs clarification: installed UIKit SDK declares UISwitch unavailable on tvOS.

## Deferred development

- ios-swiftui-state
- ios-swiftui-actions
- ios-swiftui-structure
- ios-swiftui-text
- ios-swiftui-testing
- macos-swiftui-semantics
- macos-swiftui-actions
- macos-swiftui-structure
- macos-swiftui-media
- macos-swiftui-testing
- tvos-swiftui-semantics
- tvos-swiftui-state
- tvos-swiftui-text
- tvos-swiftui-lifecycle
- tvos-swiftui-media
- ios-uikit-semantics
- ios-uikit-structure
- ios-uikit-lifecycle
- ios-uikit-media
- ios-uikit-testing
- tvos-uikit-actions
- tvos-uikit-structure
- tvos-uikit-testing
- macos-appkit-semantics
- macos-appkit-state
- macos-appkit-lifecycle
- tvos-uikit-no-change
- mixed-ios-owner
- mixed-tvos-owner
- watchos-scope
- visionos-scope
- macos-version-boundary

No model has answered these package cells. No call allocation is approved. Only the
message payload should reach a clean subject context, never this review packet.
