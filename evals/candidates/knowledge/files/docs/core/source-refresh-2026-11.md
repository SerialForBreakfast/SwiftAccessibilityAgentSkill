# Source Refresh Ledger: November 2026

Review date: 2026-11-04. Candidate: 0.2.3-candidate.1. Released version remains 0.2.2.
This is a claim-level evidence packet, not a blanket certification of the source registry.
Historical discovery documents remain available. Runtime agents should load this ledger
only for release/version questions or research maintenance.

## Reviewed Changes

| Claim / source | Supporting section | Availability / status | Affected guidance | Evaluation |
| --- | --- | --- | --- | --- |
| [tvOS Larger Text](https://developer.apple.com/videos/play/wwdc2026/221/) | Overview; layout adaptation | tvOS 27 system feature; individual API availability still matters | `tvos/guidelines/t-011-larger-text.md` | D39, tvOS 26/27 |
| [Reading navigation](https://developer.apple.com/videos/play/wwdc2026/219/) | Standard views; Custom text | UIKit text-navigation connections: iOS 18; SwiftUI linking: iOS 27 | `core/reading-content.md` | D38, H19 |
| [Generated subtitles](https://developer.apple.com/videos/play/wwdc2026/256/) | Availability and support; Presenting subtitles; Style preview | OS 27; device/language/platform capabilities vary | `core/media-updates.md` | D40, H20 |
| [Custom controls](https://developer.apple.com/videos/play/wwdc2026/220/) | Guiding principles; Complex controls | Design principles; verify each symbol separately | Existing custom-control and action guidelines; scoped refinement pending | D08, H07 |
| [Release channels](https://developer.apple.com/news/releases/) | October 26 and November 3 entries | 27.2 stable and 27.3 beta listed for scoped OS platforms; previous major lane: 26 | Evaluation OS labels; historical watchlist framing | Stable paired contexts; H18 beta |

The four session transcripts were read directly. Session year does not establish the
minimum deployment target of every API discussed. Source support is sufficient for
platform guidance; optional app tests evaluate an implementation, not Apple's authority.

## Audit Coverage and Remaining Research

`evals/evidence/registry-audit.json` inventories the pre-existing registry URLs and
prior review dates. Its pending entries retain their original status; this refresh
has not revalidated them. The new source entries below are tracked separately.

| Priority | Work item | Evidence needed before promotion |
| --- | --- | --- |
| P0 | Revalidate existing known OS issues and fixed-version claims | Exact Apple issue/release-note section and affected build range |
| P0 | Resolve historical TextKit, TabsPickerStyle, and scene-lifecycle claims | Current symbol availability and applicable release-note text |
| P0 | Revalidate Xcode plugin/MCP/Preview claims | Current Xcode documentation and release-note section |
| P1 | Expand custom-control guidance from reviewed session | API-level availability for code examples; actions/feedback regression cases |
| P1 | Check nutrition-label platform scope | App Store Connect feature definitions and release coverage |
| P1 | Review remaining WWDC watchlist features | Primary documentation for each claim, rather than announcement extrapolation |
| P1 | Refresh Tier-2 examples and accessibility-user scenarios | Specific dated article/report and affected task, device, settings |

The iOS/iPadOS 27 and Xcode 27 release-note pages returned JavaScript shells; their
linked Markdown content could not be retrieved by the available web tool. Those
claims remain pending, rather than receiving a new verification date.

## User Outcomes and Secondary Sources

The [AppleVis bug tracker](https://www.applevis.com/bugs) provides discovery signals
for VoiceOver, braille and low-vision problems. Translate reports into task-centered
candidate cases, preserve their OS/device/settings context, and distinguish reports
from documented platform contracts. Reports are not population-wide usability evidence.

Retain separate ordinary navigation and rotor/action paths so familiarity does not
become a prerequisite to completing the task. Expand research with consented,
compensated participant work when measuring actual usability; it is not a prerequisite
to accepting Apple API documentation.

## Update Protocol

For every subsequent source change, record source URL and section, review date,
authority tier, platform, minimum API availability, SDK requirement if applicable,
release channel/build, affected references, affected scenario IDs, and disposition.
Use `unknown` for unverified availability rather than inferring it from publication year.
Maintain this audit trail outside the always-loaded skill instructions.
