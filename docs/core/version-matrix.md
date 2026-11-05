# Accessibility Version Matrix (Issues and Guidance)

Last updated: 2026-11-04
Purpose: provide quick version-specific status across known issue classes.

## Known Issue Matrix

| Issue ID | Platforms | introduced_in | affected_range | fixed_in | status | confidence | Primary Evidence |
|---|---|---|---|---|---|---|---|
| AX-BUG-001 | iOS, iPadOS | iOS 26 (reported) | iOS 26 incl. 26.2 reported; 26.5/27 beta reports differ | unknown | needs_revalidation | medium | APPLE-FORUMS-THREAD-814208 |
| AX-BUG-002 | iOS, iPadOS | unknown | configuration-dependent | n/a (setting-driven) | configuration_dependent | high | APPLE-FORUMS-THREAD-804448, APPLE-VOICEOVER-RECOGNITION-SUPPORT |
| AX-BUG-003 | iOS, iPadOS | unknown | OS unspecified; 2024/2025 reports | unknown | needs_revalidation | medium | APPLE-FORUMS-THREAD-750508 |
| AX-BUG-004 | iOS, iPadOS | iOS 16 (reported) | iOS 16; current/minor versions unspecified | unknown | needs_revalidation | medium | APPLE-FORUMS-THREAD-725486 |
| AX-BUG-005 | iOS (historical report) | unknown | 2018/2020 report; current versions unspecified | unknown | needs_revalidation | medium | APPLE-FORUMS-THREAD-100449 |
| AX-BUG-006 | All | n/a | all supported lines | n/a | open | high | APPLE-AX-INSPECTOR, APPLE-AX-TESTING |
| AX-BUG-007 | iOS, iPadOS, macOS | release-cycle dependent | major/minor release dependent | release-note dependent | open | medium | APPLE-IOS18-RELEASE-NOTES, APPLE-MACOS15-RELEASE-NOTES |
| AX-BUG-008 | iOS, macOS | release-cycle dependent | browser/OS dependent | release-note dependent | open | medium | APPLE-SAFARI18-RELEASE-NOTES |

## Usage Notes

- Treat `unknown` values as active research gaps.
- Do not claim issue resolved without source-backed evidence.
- Revalidate `needs_revalidation` entries each major release cycle.

## Reading Availability Boundary

`accessibilityLinkedGroup` exists from iOS 14/macOS 11. WWDC26 describes continuous text navigation behavior on iOS 27. Distinguish the modifier's availability from the behavior described in a newer OS; see [reading guidance](reading-content.md).
