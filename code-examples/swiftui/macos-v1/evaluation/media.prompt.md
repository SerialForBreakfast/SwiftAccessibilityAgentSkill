Target macOS26, SwiftUI.

Our SwiftUI player must keep the supplied AVPlayer and native controls. Build a synthetic, injected caption-options browser with stable IDs and localized names. Distinguish not-yet-loaded options from a successfully empty result. Preserve a selected ID through reordering, clear it when removed, reject unknown selections and duplicate IDs, and ignore old asynchronous option-list replies. Do not change volume or mute while browsing. This component records a preference only; applying AVMediaSelection and rendering captions are outside this task.

Provide complete code and focused compile/unit tests. No UI automation.
