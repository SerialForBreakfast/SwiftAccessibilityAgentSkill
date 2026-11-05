# Accessible Reading Content

Reviewed: 2026-11-04. Evidence: Tier-1 Apple WWDC26 session 219,
Characteristics, Standard views, and Custom text. Status: source-supported candidate update.

Long-form reading needs granular navigation, continuous reading, and text
selection, rather than a single oversized accessibility label. Prefer native
text components where practical. Custom-rendered pages need text semantics;
an image alone cannot supply equivalent navigation and selection.

Keep availability separate from the year a technique was discussed:
- UIKit next/previous accessible text navigation was introduced in iOS 18.
- The session introduces SwiftUI `accessibilityLinkedGroup` for iOS 27.
- AppKit has a related shared-text-elements mechanism; check symbol availability
  before generating deployment-target-specific code.

For iOS 26 support, do not use the iOS 27 SwiftUI modifier unguarded. Consider
native text views or supported UIKit text-navigation integration. Preserve ordinary
reading and control access alongside rotor navigation; familiarity with rotors
varies across users.

Source: [Enhance the accessibility of your reading app](https://developer.apple.com/videos/play/wwdc2026/219/).
