Target tvOS26, SwiftUI.

Our SwiftUI settings area has a Downloads toggle, Help button and volume readout. Keep the ordinary controls and their current callbacks. Updates can change title, priority and status without reconstructing the state object. Make the names and state reflect current data. Add five-point accessible volume adjustment through the same bounded setter as ordinary controls; values range from0 to100 and unchanged or disabled requests must not call back. Preserve a valid native Toggle rather than inventing a missing-value defect.

Provide complete code and focused compile/unit tests. No UI automation.
