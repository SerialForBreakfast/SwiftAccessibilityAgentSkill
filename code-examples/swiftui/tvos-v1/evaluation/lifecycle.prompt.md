Target tvOS26, SwiftUI.

Our SwiftUI details sheet needs a clear entry target and a return target after dismissal. Keep the ordinary Open and Close controls. The originating item may disappear while the sheet is open; use a persistent fallback. Multiple presentation generations and old dismissal callbacks are possible. Resolve the current eligible target at completion and ignore stale or repeated completion. A restoration request may synchronously open another sheet.

Provide complete code and focused compile/unit tests. No UI automation.
