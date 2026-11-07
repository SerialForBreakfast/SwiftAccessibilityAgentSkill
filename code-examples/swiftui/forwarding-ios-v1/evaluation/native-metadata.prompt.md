Target iOS26, SwiftUI with UIKit.

The application supplies native card layout; preserve it. This task covers semantic/action configuration, not screen layout. Build a SwiftUI wrapper around a native report card with an independent heading, Open button, Details button and status readout. Its snapshot has id/title/status(optional)/hint(optional)/selected/enabled/landmark fields. On every update, preserve controls and show current contextual names, a non-color selected/not-selected readout, value and optional help; clear obsolete values/help when absent. Preserve unrelated native trait bits and ordered children. Use platform-appropriate scalable text configuration without claiming TV27 Larger Text on TV26.

Provide complete code and focused unit tests; no UI automation.
