# AppKit/macOS: display-preferences

Status: draft; independent review and baseline qualification pending.
Classification: Shared lifecycle principles demonstrated through platform-specific preference APIs.

Read the current three settings initially and after each platform notification. Use NSWorkspace.shared.notificationCenter for the display-options notification, not NotificationCenter.default. Start is idempotent, stop removes only owned observers, deinit cleans up, restart refreshes current state, and queued work from stopped or prior sessions is ignored. Deliver on the UI actor and deduplicate equal snapshots. Accept token owners, selector-based ownership, generation/session identity or equivalent safe lifetime designs. The injected scheduler tests deterministic state transitions; they do not prove every real scheduling interleaving.

Score correctness, preservation, usefulness and unsupported certainty separately. Invented APIs, stale cross-modal actions, lost ordinary controls and unsupported availability are critical errors. Accept valid alternatives; unit results establish stored state, callback/request behavior and ownership rather than delivered focus/speech or rendered appearance.

## Traceability

- [Source claims and negative IDs](../manifest.json)
- [Implementation](../Sources/DesktopLifecycle.swift)
- [Assertions](../Tests/DesktopLifecycleTests.swift)
- Methods: `DesktopLifecycleTests/testPreferenceInitialSnapshot`, `DesktopLifecycleTests/testPreferenceStartIsIdempotent`, `DesktopLifecycleTests/testPreferenceIdenticalValuesAreDeduplicated`, `DesktopLifecycleTests/testPreferenceMotionChange`, `DesktopLifecycleTests/testPreferenceTransparencyChange`, `DesktopLifecycleTests/testPreferenceContrastChange`, `DesktopLifecycleTests/testPreferenceStoppedQueuedWorkIgnored`, `DesktopLifecycleTests/testPreferenceStopRemovesObservers`, `DesktopLifecycleTests/testPreferenceRestartRefreshesSnapshot`, `DesktopLifecycleTests/testPreferenceOldGenerationIgnoredAfterRestart`, `DesktopLifecycleTests/testPreferenceOtherCenterIgnored`, `DesktopLifecycleTests/testPreferenceDeinitRemovesObservers`.
- Negative checks: `stoppeddelivery`, `oldgeneration`, `repeatedpreference`.
- [Execution, original source and analysis](../../../../research/evaluation/platform-lifecycle-v1/README.md)

Subject payload is the matching .prompt.md plus explicitly approved condition material. Keep this rubric, source solutions, assertions, negative fixtures and incident history out of subject context. These are development cases, not holdouts.
