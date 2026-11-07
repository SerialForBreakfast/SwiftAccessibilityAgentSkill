# Source and availability evidence

Apple source tiers remain unchanged. The existing15 guideline files are frozen by
hash in inventory.json; their historical verification dates are not reset merely
because they exist locally. The current campaign adds targeted API review and
version-qualified compiler/unit observations, not blanket freshness certification.

| Apple primary source | Scope used here |
| --- | --- |
| [SwiftUI accessibility modifiers](https://developer.apple.com/documentation/swiftui/view-accessibility) | Label/value/hint, children policies, hidden content, actions, representation and focus APIs |
| [Custom rotor entries](https://developer.apple.com/documentation/swiftui/view/accessibilityrotor(_:entries:entrylabel:)-2jbai) | Entry data composition; unit-tested stable-ID policy does not prove actual rotor navigation |
| [ScaledMetric](https://developer.apple.com/documentation/swiftui/scaledmetric) | Numeric layout metric linked to text style; no direct wrapper-value test outside an installed environment |
| [AccessibilityFocusState](https://developer.apple.com/documentation/swiftui/accessibilityfocusstate) | Public focus binding; state/request observations are distinct from delivered focus |
| [UIViewRepresentable](https://developer.apple.com/documentation/swiftui/uiviewrepresentable) and [NSViewRepresentable](https://developer.apple.com/documentation/swiftui/nsviewrepresentable) | Correct platform coordinator/update/dismantle signatures; direct coordinator calls do not establish automatic hosting propagation |
| [VideoPlayer](https://developer.apple.com/documentation/avkit/videoplayer) | Preserve native player composition; synthetic options do not apply real AVMediaSelection |
| [Binding](https://developer.apple.com/documentation/swiftui/binding) | Actual get/set binding consumed by the example and exercised by units |

Apple modifier, rotor and ScaledMetric documentation was consulted during this
campaign. Other links identify the source contracts; not every page was re-audited
in full. Targeted installed SDK 27 interface excerpts and file hashes are recorded
in [declarations](api-declarations.json). Read declaration annotations and enclosing
types together; missing annotations are not guessed from compiler success.

## Platform boundaries

- iOS and Mac use the relevant text-size environment and ScaledMetric composition.
- TV 26 uses semantic text configuration without the TV 27 Larger Text preference.
- UIKit and AppKit representable branches compile separately. Native button defaults
  are not generalized into SwiftUI generated-role claims.
- Compile checks use the existing adapter's default language mode; package unit builds
  use Swift tools 6.0. Swift compiler 6.4 is recorded separately from language mode.
- macOS 27 host evidence does not establish macOS 26 runtime behavior. Existing iOS 26.5
  and TV 26.5 simulator anchors are selected explicitly, without installing runtimes.

Generation tokens, latency or quality cannot be inferred from unit evidence.
Stable-ID invalidation, field validation conventions, step sizes and first-completion
ownership are explicit application policies, not requirements attributed to Apple.
