"""Controller decisions. Only the label and guidance of selected rules enter an archive."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Rule:
    id: str
    label: str
    target: str
    control: str
    neighbor: str
    evidence: str
    distinction: str
    guidance: str


RULES = (
    Rule("restraint", "Reviewing an existing interaction", "GP26-11", "GP26-09", "GP26-12",
         "evals/rc1-failure-replay/RESULTS.md",
         "A native adjustable control already works; a custom knob without an adjustment path needs a change.",
         "Identify the user action that fails before replacing a working control. If none is shown, keep the implementation. A cosmetic change to a native Slider need not replace its binding, range or step. Conversely, a custom control may need an adjustment path. Separate the user's preference for reduced motion from changes to the underlying state transition."),
    Rule("ordinary", "Shortcuts and independently usable controls", "ios-uikit-actions", "GP26-01", "tvos-swiftui-actions",
         "code-examples/platforms/tvos-uikit-v1/manifest.json",
         "An auxiliary shortcut is additive; an exclusively gestural command needs an ordinary alternative.",
         "Trace each ordinary action before adding a shortcut. UIKit: preserve the existing controls and their enabled-state checks when adding a custom action. On Apple TV, keep Select connected to the current item. In SwiftUI, put an alternative on the existing action path rather than firing both handlers. Before proposing a keyboard alternative, check the command API on the actual OS: sharing SwiftUI does not make a Mac command available on other targets. A rotor or shortcut can save steps without becoming the only way to finish the task."),
    Rule("children", "AppKit containers and hosted controls", "macos-appkit-structure", "macos-appkit-no-change", "mixed-macos-owner",
         "code-examples/platforms/macos-structure-v1/manifest.json",
         "A descriptive row may be grouped; two actionable children must still dispatch independently.",
         "On Mac, examine the parent role together with the children it exposes. A descriptive group and an actionable leaf are different designs. Keep independent buttons and their target/action paths intact. At an NSHostingView boundary, identify whether AppKit or SwiftUI creates the interactive child before changing the parent. If the supplied code ends at that boundary, give conditional advice."),
    Rule("refresh", "Reconfiguring a live row or card", "ios-uikit-state", "rc1/switch-preservation", "macos-swiftui-state",
         "code-examples/pilots/uikit-semantics-v1/manifest.json",
         "Clear an absent status previously owned by the card; preserve help or traits owned elsewhere.",
         "Walk through A then B on the same instance, including B with missing optional text. Replace or clear the fields this configuration owns on every update, not only on reuse. A rename-only update leaves unrelated fields alone. A permanently connected action can resolve the current owner at activation; a per-binding callback must not outlive that binding."),
    Rule("dismissal", "Closing a presentation and returning focus", "ios-swiftui-lifecycle", "GP26-07", "tvos-uikit-lifecycle",
         "code-examples/platforms/tvos-lifecycle-v1/manifest.json",
         "A matching completion may request focus; a close request, cancellation or old completion cannot.",
         "Record the opener for this presentation. Requesting dismissal does not finish it. At the owning completion (for example SwiftUI's onDismiss), consume that presentation's pending restoration before calling outward. Ignore superseded callbacks. Resolve the current eligible opener, then a valid fallback; if neither exists, make no request. On tvOS a request is not evidence of delivered focus."),
    Rule("layout", "Updating text in an existing checkout or form", "GP26-03", "rc1/checkout-layout", "macos-swiftui-text",
         "research/evaluation/failure-driven/checkout-contract-v1/manifest.json",
         "A label that wraps inside a fixed-height row is not the same as a row that can grow.",
         "Follow a long localized value through font configuration, line wrapping and the enclosing layout. If a later callback changes the row, show how it reaches the same installed views; a variable local to setup is not available in a separate method. Flexible layouts can remain vertical or adapt. Preserve the original payment control, its appearance and its action."),
    Rule("font", "UIKit font scaling for a supplied or live text setting", "rc1/checkout-font", "GP26-03", "ios-uikit-text",
         "evals/headroom/checkout-font/scorecard.json",
         "Supplied traits differ from the label's live environment; automatic tracking can be right for one and wrong for the other.",
         "Decide whose text-size setting the label must follow. For a caller-selected size, scale the unscaled design font against the supplied traits and preserve that result; automatic tracking of the label's own environment can override it. For live changes, use environment tracking or rescale from the original font on changes. Check the typeface and effective size, not just a tracking flag."),
    Rule("media", "Inspecting media or applying a delayed result", "IOS-MEDIA-OWNERSHIP-R1", "rc1/stale-media-reply", "tvos-uikit-media",
         "code-examples/platforms/ios-closure-v1/manifest.json",
         "Replacing the player item and superseding a request on the same item are different invalidations.",
         "At delivery, compare the requested item with the player's actual current item, not just the last item the view cached. Track request ownership too when a newer request can supersede one on the same item. An inspection reports available options and current selection separately; it does not select a track. Keep an unfinished load, an error and a successful empty result distinguishable."),
    Rule("proof", "Explaining what accessibility evidence establishes", "EV06", "EV01", "macos-appkit-testing",
         "evals/rc1-failure-replay/RESULTS.md",
         "Direct handler invocation proves that handler's effect; exercising target/action also establishes wiring, not input delivery.",
         "Name the path exercised. A direct handler call, a wired control dispatch and a delivered keyboard or assistive action are different observations. Report an audit's checked elements and checks rather than declaring the app accessible. For availability, distinguish an SDK declaration, a deployment target and an executed runtime; identify any missing evidence."),
    Rule("callbacks", "Testing delayed or repeated callbacks", "IOS-MEDIA-OWNERSHIP-R1", "rc1/status-change", "tvos-swiftui-testing",
         "evals/rc1-failure-replay/RESULTS.md",
         "A once-resuming async fake cannot demonstrate a double callback; a duplicate-capable boundary can.",
         "Build the test around the event that can go wrong. Wait for a deterministic registration signal before delivering a delayed response. To test duplicate callback delivery, use a boundary that can deliver twice, not a continuation that may resume only once. Exercise the live owner and assert the effect on the existing control or state; invoking a helper alone establishes less."),
)
