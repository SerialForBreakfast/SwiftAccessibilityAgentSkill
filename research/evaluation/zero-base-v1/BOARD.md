# Failure-to-rule board

One row per graded case, including passes. Associations are hypotheses, not evidence of challenger lift.
See matrix.json for inputs, rubric locators, source registry and scoped contracts.

| Case | Framework / platform | Observed developer decision | Disposition | Candidate rules |
|---|---|---|---|---|
| GP26-03 | iOS UIKit | Checkout total wraps at large text; Pay appearance preserved | mixed result | font, layout |
| GP26-11 | iOS SwiftUI | Already-correct native Slider needs no change | mixed result | restraint |
| GP26-12 | iOS SwiftUI | Existing reduced-motion transition needs no change | mixed result | restraint |
| rc1/checkout-font | iOS UIKit | Supplied text-size setting owns the label font | mixed result | font |
| IOS-MEDIA-OWNERSHIP-R1 | iOS UIKit | Late media callback after external item replacement | observed failure | callbacks, media |
| ios-swiftui-media | iOS SwiftUI | Metadata states distinct; reject stale completions | mixed result | media |
| ios-uikit-state | iOS UIKit | Repeated updates replace stale status/help; current reply only | observed failure | refresh |
| ios-swiftui-lifecycle | iOS SwiftUI | Restore to the current eligible origin at completion | mixed result | dismissal |
| ios-uikit-text | iOS UIKit | Scalable checkout text with Pay identity preserved | mixed result | font, layout |
| ios-uikit-actions | iOS UIKit | Shortcut added; ordinary Open/Delete stay reachable | mixed result | ordinary |
| tvos-swiftui-testing | tvOS SwiftUI | Map claims to actual assertions; keep first diagnostics | observed failure | callbacks |
| macos-appkit-structure | macOS AppKit | Group descriptions without merging Open and Details | mixed result | children |
| macos-appkit-testing | macOS AppKit | Map claims to actual assertions; keep first diagnostics | mixed result | callbacks, proof |
| macos-swiftui-lifecycle | macOS SwiftUI | Restore to the current eligible origin at completion | observed failure | dismissal |
| mixed-macos-owner | macOS mixed | Condition advice on the owning view/coordinator layer | mixed result | children |
| tvos-uikit-state | tvOS UIKit | Repeated updates replace stale status/help; current reply only | mixed result | refresh |
| GP26-04 | iPadOS SwiftUI | Delete without requiring a swipe | mixed result | ordinary |
| macos-swiftui-state | macOS SwiftUI | Repeated updates replace stale status/help; current reply only | mixed result | refresh |
| tvos-uikit-lifecycle | tvOS UIKit | Restore to the current eligible origin at completion | mixed result | dismissal |
| GP26-06 | iOS SwiftUI | Already-correct Toggle needs no change | mixed result | restraint |
| EV02 | any evidence | 12 clean checks don't justify 'fully accessible' | mixed result | proof |
| EV06 | any evidence | Direct handler test doesn't prove keyboard/VoiceOver activation | mixed result | proof |
| GP26-02 | iOS UIKit | Reused cell shows current customer and status | mixed result | refresh |
| IOS-VALIDATION-OWNERSHIP-R1 | iOS UIKit | Validation result ignores newer submissions | mixed result | refresh |
| macos-swiftui-text | macOS SwiftUI | Scalable checkout text with Pay identity preserved | observed failure | layout |
| ios-uikit-no-change | iOS UIKit | Working standard control needs no replacement | mixed result | restraint |
| macos-appkit-actions | macOS AppKit | Shortcut added; ordinary Open/Delete stay reachable | mixed result | children |
| tvos-swiftui-actions | tvOS SwiftUI | Shortcut added; ordinary Select stays reachable | mixed result | ordinary |
| tvos-uikit-media | tvOS UIKit | Metadata states distinct; reject stale completions | observed failure | media |
| EV01 | any evidence | Screenshot does not prove VoiceOver activation | preserved success | proof |
| EV03 | any evidence | Unavailable docs can't establish exactly-once activation | preserved success | proof |
| EV04 | any evidence | Forum post can't justify removing a payment workaround | preserved success | proof |
| EV05 | any evidence | Simulator 26.5 doesn't establish 26.0 and later | preserved success | proof |
| GP26-01 | iOS UIKit | Settings row: switch and Help stay independently usable | preserved success | ordinary |
| GP26-05 | tvOS SwiftUI | tvOS tile navigation keeps controls | preserved success | ordinary |
| GP26-07 | iOS UIKit | Return focus to the current payment origin | preserved success | dismissal |
| GP26-08 | iOS UIKit | Custom popup contains focus and restores background state | preserved success | dismissal |
| GP26-09 | iOS UIKit | Custom volume knob is adjustable | preserved success | ordinary, restraint |
| GP26-10 | iOS UIKit | Download progress without repeated announcements | preserved success | media |
| ios-missing-reference | iOS any | Don't claim an unread reference's contract | preserved success | proof |
| ios-swiftui-no-change | iOS SwiftUI | Working standard control needs no replacement | preserved success | restraint |
| ios-swiftui-semantics | iOS SwiftUI | Native switch: change only for a demonstrated defect | preserved success | restraint |
| macos-appkit-no-change | macOS AppKit | Working standard control needs no replacement | preserved success | children, restraint |
| rc1/adjustable-volume | iOS SwiftUI | Adjustable volume steps within bounds | preserved success | ordinary |
| rc1/checkout-layout | macOS SwiftUI | Stack checkout at accessibility sizes | preserved success | layout |
| rc1/landmark-identity | macOS SwiftUI | Landmarks keep order and stable IDs | preserved success | children |
| rc1/motion-policy | tvOS SwiftUI | Reduce Motion suppresses only the optional effect | preserved success | restraint |
| rc1/ordinary-buttons | macOS AppKit | Both buttons dispatch to the current owner | preserved success | ordinary |
| rc1/restoration-eligibility | tvOS UIKit | Restore to an eligible enabled opener, else fallback | preserved success | dismissal |
| rc1/row-traits | tvOS UIKit | Selection preserves unrelated traits | preserved success | refresh |
| rc1/stale-media-reply | tvOS SwiftUI | Media reply must match current item and request | preserved success | media |
| rc1/status-change | macOS AppKit | Publish new status before notifying, once per change | preserved success | callbacks, refresh |
| rc1/switch-preservation | iOS UIKit | Rename returns the original switch unchanged | preserved success | ordinary, refresh |
| rc1/toggle-binding | iOS SwiftUI | Guarded toggle binding forwards changed writes once | preserved success | refresh |
| tvos-swiftui-structure | tvOS SwiftUI | Group descriptions without merging Open and Details | preserved success | children |
| tvos-version-boundary | tvOS any | Separate SDK, deployment and runtime evidence | preserved success | proof |
