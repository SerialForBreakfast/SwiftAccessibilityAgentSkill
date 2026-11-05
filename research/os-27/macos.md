# macOS 27 changes

Research only; reviewed 2026-11-05. Tier-1 source: [27.0 release notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes), [27.2](https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes), [27.3 beta](https://developer.apple.com/documentation/macos-release-notes/macos-27_3-release-notes). Section names and issue IDs below locate the supporting passage; fingerprints are in [sources](sources.md). Symbol minimum versions remain pending DocC availability extraction unless expressly stated. A release-note appearance alone is not an API introduction date.

| Claim ID | Documented change | Release/type | Supporting section / issue | Research implication (inference) |
| --- | --- | --- | --- | --- |
| MAC-01 | Toolbar groups and segmented controls gain semantic roles including tabs. | 27 feature | AppKit / 162577742 | Compare AppKit roles with SwiftUI tab pickers. |
| MAC-02 | Text-selection interactions gain a gesture-based manager with subclass fallback. | 27 feature | AppKit / 163365571 | Study custom text and input interoperability. |
| MAC-03 | Open/save panel tab order and keyboard loops receive fixes. | 27 resolved | AppKit / 43112307, 169837566 | Preserve issue-specific regression scope. |
| MAC-04 | Grouped forms honor Show borders; menu AXTitle/AXDescription behavior is corrected. | 27 resolved | SwiftUI / 155906280, 171831601 | Build future semantic and contrast cases. |
| MAC-05 | External-display settings restoration is a known issue. | 27.2 known | Display Settings / 188643179 | Keep display setup effects separate from app bugs. |
| MAC-06 | CaptureInputSequenceProvider assertion in Designed-for-iPad targets is fixed. | 27.3 beta resolved | Speech / 187921017 | Check Catalyst versus Designed-for-iPad distinctions. |

## Follow-up

AppKit menu imagery has linked-version nuances (170477566); extract those before proposing code. Follow notification permission issues (187312007) and keyboard navigation across app/system boundaries. SDK validation later can check symbols, not infer user usability.

[Full topic inventory](coverage.md) · [Cross-platform evidence](cross-platform.md) · [Research method](README.md)

## Second-pass constraints

[API-04/05](api-availability.md) records text-selection and toolbar-role availability, including a metadata interpretation issue. [SHIP-02](shipping-constraints.md) establishes the M1-or-later media constraint, and [SHIP-06](shipping-constraints.md) records managed-device accessibility policy.
