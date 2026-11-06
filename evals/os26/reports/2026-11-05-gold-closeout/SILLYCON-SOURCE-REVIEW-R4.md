# Source and assertion review: unit fixture revision 2

Reviewed locally on2026-11-05. Original fixtures authored by BigDog; local reviewer
is the SwiftAccessibility agent on Sillycon. New SwiftUI test seams, mutations,
tests and runner are locally authored and require BigDog's independent review.
This document is not that independent approval.

| Case | Source/section | Scoped conclusion and valid alternatives |
| --- | --- | --- |
| 01 | SDK27 UIKit `UIAccessibility.h`, accessibilityElementsHidden declaration/comment (iOS5+) | Hiding a container's descendants is inconsistent with exposing independent controls. Unit flags/callbacks are observable; other groupings are valid if functions remain available. Spoken order is not asserted. |
| 02 | [Apple prepareForReuse Discussion](https://developer.apple.com/documentation/uikit/uitableviewcell/prepareforreuse%28%29), retrieved2026-11-05 | Configuration must refresh content; reconfiguration can bypass reuse preparation. Same-instance transitions are appropriate. An answer need not use the reference label's exact wording. |
| 03 | [Apple automatic font updates Discussion](https://developer.apple.com/documentation/uikit/uicontentsizecategoryadjusting/adjustsfontforcontentsizecategory), retrieved2026-11-05 | Preferred/scaled fonts plus automatic adjustment support updates. Unit prerequisites do not prove visual fit. Other flexible layouts remain acceptable. |
| 04/05 | [Apple Button Overview](https://developer.apple.com/documentation/swiftui/button), retrieved2026-11-05; availability metadata includes iOS/tvOS13+ | Buttons associate labels and action closures. Direct production-handler tests check callback identity/count, not event delivery. The old focus-reset mutation is outside this unit endpoint. |
| 06 | [Apple Toggle Overview](https://developer.apple.com/documentation/swiftui/toggle) and [Binding Overview](https://developer.apple.com/documentation/swiftui/binding), retrieved2026-11-05; iOS/tvOS13+ | Toggle accepts a Boolean binding; Binding connects to externally owned state. Testing the exact binding returned to Toggle is preferable to testing a disconnected copy. Native unchanged control is valid. |

The original visibility documentation URL returned404; the public installed SDK
declaration supplies the bounded symbol/contract evidence instead. The SDK is27,
not26. Public source files and test execution support claims for the recorded
toolchain/runtime; no earliest behavioral-change date is inferred.

## Mutation specification frozen before native runs

| Case | Unit assertion | Mutation1 | Mutation2 |
| --- | --- | --- | --- |
| 01 | UIKitTests/testSettingsCallbacksAndExposedControls | Hidden descendants | Missing Help callback |
| 02 | UIKitTests/testReconfigurationWithoutPrepareForReuse | Stale label | Stale status |
| 03 | UIKitTests/testCheckoutCallbackAndResizePrerequisites | Fixed height | Automatic scaling disabled |
| 04 | SwiftUIContractTests/testMessageActions | Dropped deletion | Duplicate deletion |
| 05 | SwiftUIContractTests/testMovieActivation | Dropped activation | Wrong movie |
| 06 | SwiftUIContractTests/testNotificationBinding | Constant binding | Inverted write |

The runner records exact variant/suite hashes and selected tests before each call.
Same test selection is used for candidate and both mutations. One expected XCTest
assertion failure with the matching case is required; infrastructure failures stop
the run. Original draft3 sources/variants remain archived. Assertions validate this
reference implementation, not a requirement for generated answers to use these exact
helper names or this code structure. Equivalent answers require reviewed adaptation
to the fixture, not rejection for failing to match internal helper names.

## Independent review request

BigDog should verify public-control wiring still uses these tested functions/binding,
absence of duplicate test-only logic, expected-mutation classification, runner
isolation, valid alternate solutions and evidence limitations. Approval must cite
the exact source revision/hash, not merely agree with this summary. Until then,
source-review and oracle promotion remain pending despite any native passes.
