Target tvOS26, SwiftUI.

Our SwiftUI article list has stable string IDs, titles and a flag identifying important articles. Keep visible Open and Delete operations on each row, and add shortcut navigation to important articles without requiring it for ordinary use. Updates may rename, reorder or remove articles. Reject duplicate IDs atomically; preserve surviving selection. Old captured actions must not apply to a rebound revision, and deleted selections must clear.

Provide complete code and focused compile/unit tests. No UI automation.
