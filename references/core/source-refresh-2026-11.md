# Source Refresh Ledger: November 2026

Review date: 2026-11-04. Candidate: 0.2.3-candidate.1. Released identity: 0.2.2.

## Audit Outcome

All 63 source entries have an explicit disposition in
[the source audit](../../evals/evidence/registry-audit.json). It records requested and
retrieval URLs, response status, content fingerprints and scoped review notes.
The audit distinguishes 35 scoped reviews, five reviewed reports, 11 discovery
resources, six historical references, five access-limited sources and one replaced URL.
A successful HTTP response alone is not a content review.

Apple DocC JSON made the previously inaccessible release-note sections reviewable.
Forum HTML fetched directly sometimes returned the same generic page; the five
original threads were instead reviewed through their browser text views. Their
transport fingerprints are not mislabeled as fingerprints of the reviewed thread.
Blocked or empty community responses are retained as research pointers. Platform
rules use reviewed Tier-1 sources, and older release notes retain their historical scope.

## Claim-to-Guidance Map

| Claim | Reviewed evidence | Disposition / affected guidance | Cases |
| --- | --- | --- | --- |
| tvOS Larger Text | WWDC26/221: overview and layout adaptation | T-011: system feature on tvOS 27; flexible type/layout | D39 |
| Reading | WWDC26/219 and APPLE-LINKED-GROUP metadata/discussion | Symbol exists on iOS 14/macOS 11; distinguish iOS 27 continuous-reading behavior from API introduction | D38, H19 |
| Generated subtitles | WWDC26/256: authoring, availability, selection and style preview | core/media-updates.md and media guideline cross-links; retain authored tracks | D18, D40, H20 |
| Custom controls | WWDC26/220; adjustable/direct-touch symbol metadata | U-008/G-008: adjustable actions, meaningful feedback, optional precision gestures | D08, H07 |
| Categorized actions | APPLE-CATEGORIZED-ACTIONS declaration/metadata | iOS/tvOS 18, macOS 15, visionOS 2; distinguish category availability from newer behavior | Future reading/action cases |
| TextKit | OS 26: 152045248/155893102; OS 27: 159870239 | Separate paragraph/SDK directionality from UIKit text-table support | Availability candidate lane |
| Navigation semantics | OS 27 SwiftUI: 173211711/170480710 | Tabs versus value selection; meaningful menu labels | Navigation candidate lane |
| Scene restoration | OS 27 UIKit: 161843040/141837548 | SDK-linked lifecycle/restoration requirements; not a direct VoiceOver focus API | D06, H01 reasoning |
| Xcode integrations | Xcode 27 Coding Intelligence; Xcode 26.6 snapshot/ACP sections | Host capabilities documented; native skill discovery remains a separate integration check | Host adapter smoke |
| Tool defects | Xcode 27 Device Hub and Coding Intelligence resolved sections | Correct historical limitation status; retain issue IDs | Tool-evidence candidate lane |
| Nutrition labels | ASC overview, common tasks and management sections | core/accessibility-nutrition-labels.md; device-specific support claims | Future support-claim cases |
| Lazy-stack hang | Forum 814208: DTS and subsequent replies | Narrow AX-BUG-001; fix state-allocation race before broad workaround; no universal fixed release | D34 |
| Recognition speech | Forum 804448 and Apple recognition support | AX-BUG-002: preserve user settings and correct image semantics | Future recognition case |
| Link/reorder/container reports | Forums 750508/725486/100449 | Preserve report dates and unspecified versions; remove inferred minor/OS ranges and tvOS extrapolation | D34, regression triage |
| Other announced features | Apple Newsroom 2026 announcement and footnotes | Keep AI descriptions, alternate input and communication topics as discovery; API-specific guidance requires its own source | Research candidate lane |

## Source Corrections

- Replace the 404 SwiftUI accessibility hub URL with the reviewed View accessibility page.
- Point the AppKit protocol source at NSAccessibilityProtocol, not the NSAccessibility
  namespace. Keep stable citation identifiers so existing guidance remains traceable.
- Record the linked-group symbol-versus-behavior distinction in the reading guide,
  version matrix and development rubric before model testing.
- Historical forum posts establish symptoms, not current affected/fixed OS ranges.

## Evaluation Readiness

The refreshed normative documentation is ready for the first source-backed evaluation
pass. The 60-family suite remains candidate coverage until grading calibration.
Specific TextKit, navigation, support-claim and tool-integration additions are tracked
as future candidate coverage rather than silently claimed to be tested by the suite.
No model-quality, runtime-conformance or token-efficiency improvement is asserted.

BigDog deployment details, independent grading calibration and live runs are the next
steps. Preserve the immutable baseline and earlier knowledge-only overlay. The latter
captures an earlier candidate, including its pre-audit reading assumption; use the
current skill hash to identify this refreshed candidate and compare it explicitly.

## Maintenance and User Outcomes

Review the small claim/doc/test set affected by a source change. Record URL, section,
review date, platform, minimum symbol availability, SDK requirement, release/build,
applicable behavior, affected guidance and scenario IDs. Keep discovery resources
outside the always-loaded path.

Use AppleVis and practitioner reports to discover task-level pain points, preserving
OS/device/settings context. Native and ordinary navigation remain usable alongside
rotor shortcuts, accommodating different tool familiarity. App-level research and
runtime checks assess usability; Apple documentation supports platform guidance
without requiring manual device evidence to accept it.
