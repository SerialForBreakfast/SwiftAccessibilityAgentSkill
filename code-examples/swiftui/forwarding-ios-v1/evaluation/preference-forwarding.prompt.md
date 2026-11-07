Target iOS26, SwiftUI with UIKit.

Build SwiftUI state feeding that native report card through one snapshot. Editing its name must preserve selection. Selection changes update current visible/value state before an optional animation callback; unchanged requests should not notify or animate. Reduced motion must still apply the final state, with no animation. Reentrant callbacks may change selection again. Reduced transparency chooses an opaque background policy and can return to normal later.

Provide complete code and focused unit tests; no UI automation.
