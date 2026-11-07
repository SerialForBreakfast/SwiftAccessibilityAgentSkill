# Native boundaries

Use for representables, rebinding or unfamiliar imported APIs.

- Identify platform and native owner: AppKit/macOS differs from UIKit/iOS/tvOS.
  An identifier is not a spoken name; a SwiftUI modifier is not a native getter.
- Refresh current labels/values/help, including clearing obsolete optional fields.
  Same-instance reconfiguration must work without reuse. Preserve unrelated traits.
- Keep ordinary controls alongside shortcuts/rotors. Bind callbacks to the current
  item/session; reject stale/duplicate completion and account for reentrancy.
- Check actual native dispatch as well as captured closures. On rebind, detach old
  target/action wiring or reject its sender. A new closure created inside an old
  selector does not establish ownership. Show the real update/dismantle integration.
- Verify exact Swift imports and availability, not guessed Objective-C translations.
  The recorded SDK27 member is NSAccessibility.Role.headingRole (declared macOS26);
  check the actual target rather than copying that spelling across SDKs/platforms.

Apple contracts: [representables](https://developer.apple.com/documentation/swiftui/uiviewrepresentable),
[AppKit accessibility](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol).
Session policies follow the task, not a universal Apple rule.
