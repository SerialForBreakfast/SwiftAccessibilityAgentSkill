Target tvOS26, SwiftUI.

Our SwiftUI email form uses an injected main-actor validator taking the current string and a completion. A nil error means success, a nonempty string is a user-facing error, and an empty error is a service failure. Replies may be synchronous, duplicated or out of order. Edits, cancellation and another Save must invalidate obsolete replies. Preserve raw input; Save may reenter validation. Show current errors visibly and keep the existing form controls.

Provide complete code and focused compile/unit tests. No UI automation.
