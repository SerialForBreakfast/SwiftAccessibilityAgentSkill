# U-015 Media: First Clause Review

Author review, not independent acceptance. Exact clause text and source hashes are
in inventory.json. Native media reports use SDK27/deployment26 and runtime26.5;
they do not establish every supported OS version or actual playback accessibility.

| Clause | Disposition | Assertion scope / remaining work |
| --- | --- | --- |
| L23 controls | Scoped unit evidence | MediaUIKitTests/testPlayPauseControlMetadataTransitions and testTimelineValueAndBounds assert play/pause/timeline metadata. UPAIR-06C now adds PlaybackSpeedTests/testOrdinaryButtonsHaveDistinctNamesAndInitialSelection and testOrdinaryPrimaryActionUpdatesStateBeforeCallback. These assert configuration and direct dispatch, not speech or playback. |
| L24 state/time | Scoped unit evidence | The same two tests assert configured state and timing values. They do not establish spoken output or a rendered control. |
| L25 captions | Scoped unit evidence | MediaUIKitTests/testSubtitleOptionsExposeBothAuthoredLanguages and testSubtitleSelectionAndOffState inspect actual local options and selection. Authored caption quality remains content evidence, not unit evidence. |
| L26 inspection | Scoped unit evidence | MediaInspectionTests/testWaitingStatusDoesNotBecomePlayingFromRate and range/duration/buffer tests preserve input distinctions; MediaMetadataTests/testInspectionPreservesChosenAudioAndSubtitleOff reads actual options. Stream kind is supplied knowledge, never inferred from duration. |
| L27 ordinary actions | Partial | Native player controls are explicitly retained by MediaUIKitTests/testNativeControllerPreservesControlsAndAutomaticSelection. PlaybackSpeedTests/testEverySupportedChoiceHasAnOrdinaryAction now exercises registered primary actions. Native gesture/keyboard delivery is not established. |
| L31 interop labels | Deferred scope | Mixed AVKit/SwiftUI integration is outside this UIKit-first tranche. UIKit metadata is not cross-framework proof. |
| L32 shared owner | Deferred scope | Current metadata loader is item-scoped, not an integration coordinator. Host/embedded-player ownership needs a separately scoped interop example. |
| L33 overlays | Outside current unit evidence | No rendered overlay/hit-testing assertion. Control-retention flags do not establish unobstructed navigation. This adds no UI/manual gate. |
| L39 discoverability | Partial/outside unit evidence | Labels can be inspected in code; actual discoverability is not proved by configured metadata. |
| L40 updates | Scoped unit evidence | Play/pause and timeline reconfiguration assert new values and unavailable reset. No playback or spoken update assertion. |
| L41 caption reachability | Outside current unit evidence | Native selection tests establish selectable options/current state, not user input reachability. |
| L42 snapshot | Scoped unit evidence | Nine MediaInspectionTests methods plus seven MediaMetadataTests methods cover the selected value and local-asset fields. No atomic snapshot or live network state claim. |
| L46 announcements | Outside agreed unit scope | Speech and navigation are documentation-supported behavior, not assertions from these examples. No UI tests or mandatory manual verification added. |
| L47 input operation | Outside agreed unit scope | Direct selection is tested; operation through assistive input is not. |
| L51 optional UI hook | Translate code contract only | State and selection transitions have unit evidence. Do not implement the optional XCUITest hook for this project. |
| L52 inspection fields | Scoped unit evidence | Value-layer and local extraction assertions establish captured fields; they do not prove no speech ever occurs. |
| L56 named controls | Scoped unit evidence | Play/pause/timeline label/value methods above cover explicit configuration, not full UI behavior. |
| L57 gesture hiding | Partial | Native controls are retained. UPAIR-06C preserves ordinary buttons and tests their registered actions. |

## Evidence Locations

- `code-examples/pilots/uikit-media-v1/Tests/MediaUIKitTests.swift` and its revision3 validation.
- `code-examples/pilots/uikit-media-inspection-v1/Tests/MediaInspectionTests.swift` and revision1 validation.
- `code-examples/pilots/uikit-media-metadata-v1/Tests/MediaMetadataTests.swift` and revision2 validation.

## New Pair To Build

Proposed UPAIR-06C developer question: "Our player has normal and faster playback
speeds. How should I expose the current speed and let people change it without
depending on a special gesture? Keep the ordinary controls and show focused unit tests."

Controller criteria: explicit current state, accepted rate choices, ordinary action
and any optional accessibility action share semantics, selection updates consistently,
invalid input preserves a defined safe state, and tests do not claim actual playback
or speech. Accept valid alternative controls; do not mandate one widget or an exact
spoken string. This is an authoring seed, not a frozen or executed model case.

## Speed Gap Follow-Up

The seed above is now implemented as [UPAIR-06C](../../pilots/uikit-speed-v1/README.md)
with a separate subject prompt and controller rubric. Native evidence covers explicit
state and direct control-event dispatch; independent review and gold promotion remain
pending. Other clause dispositions and interop deferrals remain unchanged.
