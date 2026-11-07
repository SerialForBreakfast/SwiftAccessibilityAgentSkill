Target iOS26, SwiftUI with UIKit interop.

Our SwiftUI native-button wrapper receives a title, enabled state and callback that can change on every update. Keep the same native button when appropriate, refresh its explicit name and enabled state, and replace rather than accumulate handlers. A coordinator may be rebound to a different button. Old native controls and captured actions must never invoke the new item handler. Dismantling must stop dispatch and retained callbacks must not retain the coordinator or view.

Provide complete code and focused compile/unit tests. No UI automation.
