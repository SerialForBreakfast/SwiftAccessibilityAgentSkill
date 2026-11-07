# Source and version scope

Primary contracts are public SwiftUI UIViewRepresentable/NSViewRepresentable update,
coordinator and dismantle APIs; UIKit UIAccessibility properties/custom actions;
AppKit NSAccessibility role/value/help/children/custom-action properties; and public
SwiftUI Binding/accessibility preference APIs. Application selection ordering and
revision invalidation are explicit component policies, not claims Apple mandates them.

- [UIViewRepresentable](https://developer.apple.com/documentation/swiftui/uiviewrepresentable)
- [NSViewRepresentable](https://developer.apple.com/documentation/swiftui/nsviewrepresentable)
- [UIKit accessibility](https://developer.apple.com/documentation/uikit/accessibility-for-uikit)
- [NSAccessibilityProtocol](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol)
- [Reduce Motion environment](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducemotion)

The selected SDK27 AppKit NSAccessibilityConstants.h declares NSAccessibilityHeadingRole
with macOS26 availability. The compiler explicitly renamed the global Swift spelling
to NSAccessibility.Role.headingRole. A separate Swift6/target26 declaration probe
succeeded before the final API repair. Native host27 getter evidence is not a claim
of actual Mac26 execution. Do not guess imported member names from Objective-C
constants or transfer UIKit traits to AppKit/SwiftUI.

UIKit font and multiline configuration is directly inspected, not rendered text
scaling. TV26 configuration is not the newer system Larger Text preference. Public
native getter and dispatch tests do not inspect automatic hosting propagation,
SwiftUI generated accessibility semantics, focus delivery, speech or visual contrast.
