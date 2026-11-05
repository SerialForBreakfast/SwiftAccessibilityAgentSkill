# Research completion backlog

These are research tasks only. No skill changes or benchmark mutations are authorized.
Updated for the third pass, 2026-11-05. Every item comes from a "Gaps" section of the
pass-3 notes or from the pass-2 backlog.

## Third-pass progress

- Full release-note inventories for every OS platform: iOS/iPadOS 322, macOS 296, visionOS
  168, tvOS 68, watchOS 73 entries ([inventory/](inventory/ios-ipados.md)). Safari and Xcode
  inventories are accessibility-scoped only.
- Release, build and date map with source per value ([releases.md](releases.md)); 27.1 scope
  established.
- API availability expanded to API-101 to API-150, separating new, changed and 26.x symbols
  and listing 27.0 and 27.3 deprecations ([api-availability.md](api-availability.md)).
- Announced-versus-shipped matrix with SHIP-101 to SHIP-116 and PEND-01 to PEND-04
  ([shipping-constraints.md](shipping-constraints.md)).
- WWDC26 session index ([wwdc.md](wwdc.md)), community records COMM-101 to COMM-133
  ([community.md](community.md)), 33 conflicts kept ([conflicts.md](conflicts.md)).

## Release and build reconciliation

| ID | Priority | Gap | Completion evidence |
| --- | --- | --- | --- |
| R-1 | P0 | No Apple-sourced public 27.0 build for iOS/iPadOS (24A435 is Tier-2), macOS or visionOS. Check the macOS Golden Gate 27 security-content page and Apple's OTA records. | Apple page stating each 27.0 build |
| R-2 | P0 | No Apple statement of iOS 27.1 builds or of the two iOS 27.2 builds (24B119, 24B91020). | Apple source or documented "unavailable" |
| R-3 | P1 | Safari 27.1 build not recorded; tvOS 27.0.1 existence unrecorded; watchOS 27.0.1 missing from security extraction; 27.3 beta number unknown. | Index and security-page re-check |
| R-4 | P1 | India-region copy of 149076 reportedly differs from the US copy (unverified); macOS 27.0.1 contents beyond "no published CVE entries" unknown. | Fetched and compared |
| R-5 | P1 | Release notes may be edited after 2026-11-05; hashes pin this snapshot only. Re-fetch after 27.3 GM. | New hashes and a diff |

## API and symbol review

| ID | Priority | Gap | Completion evidence |
| --- | --- | --- | --- |
| A-1 | P0 | Symbol availability pending for every release-note API not in api-availability.md (e.g. `UIMenuElement.preferredImageVisibility`, scene accessories, `navigationBarMinimization`, `NSTextTable` for UIKit, `concentricCornerRadii`, Transaction enum cases, `.bordered` style, `TabRole.prominent`). | DocC `metadata.platforms` per symbol |
| A-2 | P0 | No full `NSAccessibility` symbol diff; `NSToolbarItemGroup.role` property page not re-fetched (C-12); `NSControl` `Events`, `beginDraggingSession(items:gesture:source:)` and `GestureInputKinds` availability for AppKit context pending. | Diff and property-page fetch |
| A-3 | P1 | Empty DocC abstracts: `AXSpeechAttributeSSML`, `MACaptionAppearanceDomain.videoConferencing`, `XCUIVoiceOverService` (and its `Output` type, "Xcode 16.3" anomaly, C-16). | Abstracts or header comments reviewed |
| A-4 | P1 | `AccessibilityComponent` visionOS `introducedAt` missing; no DocC `diffAvailability` retrieved to confirm absence of new 27 accessibility symbols; symbols whose paths lack accessibility keywords may be missed. | API-diff view or broader scan |
| A-5 | P1 | Re-verify the 27.3 deprecations (API-127, API-128) and API-124 beta symbols after 27.3 GM. | Post-GM DocC fetch |
| A-6 | P1 | `UIScene.extendStateRestoration` DocC versus release-note framing (C-04); sign-language characteristic 27.1 on platforms without 27.1 (C-17). | SDK header check |
| A-7 | P2 | Swift 6.4 `@available`/`#available` changes (Swift.org and Swift Evolution not checked). | Swift release notes reviewed |
| A-8 | P2 | No visionOS detection API for Dwell, Face Gestures or Look to Drive was found, but the Accessibility framework DocC was not searched exhaustively. | Exhaustive search |

## Shipping and Support evidence

| ID | Priority | Gap | Completion evidence |
| --- | --- | --- | --- |
| S-1 | P0 | Verify every summarizing-fetch quote (SHIP-101–116) against live pages. | Direct fetch with hash |
| S-2 | P0 | iPadOS and macOS shipping evidence for VoiceOver descriptions, Magnifier, Voice Control natural language and Accessibility Reader. | Version-27 user-guide pages |
| S-3 | P0 | Generated subtitles: re-fetch the iPhone guide for locale (C-10); find tvOS and visionOS shipping evidence (PEND-04); iPad and Apple TV hardware/language tables. | Support pages |
| S-4 | P1 | PEND-01 to PEND-03: check version-27 guide pages for Touch Accommodations, Hearing Devices and Game Controllers. | Guide pages or confirmed absence |
| S-5 | P1 | Vehicle Motion Cues and Face Gestures first version (C-24); Pointer Control finger/wrist and Live Recognition "Ask" newness on visionOS. | Dated Apple source |
| S-6 | P1 | FaceTime interpreter user-guide procedure and any developer API or entitlement (C-23). | Guide page; DocC |
| S-7 | P1 | Look to Drive "Instructions for Use" document not fetched. | Fetched and reviewed |
| S-8 | P1 | Enterprise "What's new" pages for iOS 27 and visionOS 27; full Accessibility payload section of the deployment guide; watchOS feature-availability table reconciliation (WATCH-04). | Pages reviewed |
| S-9 | P2 | No "About tvOS 27 Updates" or separate iPadOS updates page found; WWDC June 2026 platform press releases not retrieved. | Located or confirmed absent |
| S-10 | P2 | Braille Access, Live Listen, Live Captions, Personal Voice, Vocal Shortcuts, Eye Tracking, Music Haptics and Accessibility Nutrition Labels changes in 27 not searched. | Searched |
| S-11 | P2 | HomePod/audioOS and CarPlay dependencies (pass-2 item). | Dedicated sources |

## Platform-specific research

| ID | Priority | Gap | Completion evidence |
| --- | --- | --- | --- |
| P-1 | P0 | tvOS: whether `AVPlayerViewController` panels and caption size follow Text Size; subtitles-on-mute behavior (C-05); Larger Text hardware limit beyond the tvOS 27 floor. | Apple statement or test |
| P-2 | P0 | watchOS: VoiceOver, AssistiveTouch, haptics, notifications and Digital Crown accessibility changes; single-tap model list; AppleVis "Tap to Wake". | Apple source |
| P-3 | P1 | iOS: Tier-1 status after 27.0 of Dictation Voice Editing (173448573), Siri truncation (181266301), photo voice commands (171728298, 176812955), Writing Tools (177097101). | Later notes or Feedback status |
| P-4 | P1 | Zero `UIView` margins: runtime versus SDK gating and iPad scope (C-08). | Apple clarification or test |
| P-5 | P1 | Beta provenance of each 27.0 entry is not shown on the consolidated pages. | Archived beta notes |
| P-6 | P2 | HIG 2026-updated pages (Tab bars, Gestures, Pointing devices, Designing for iPhone Duo) not read for embedded accessibility notes. | Pages read |

## Safari and Xcode

| ID | Priority | Gap | Completion evidence |
| --- | --- | --- | --- |
| T-1 | P1 | Complete Safari 27.x and Xcode 27.x inventories (all entries, not the accessibility subset). | Row-per-entry tables |
| T-2 | P1 | Map Apple radars to WebKit Bugzilla IDs via WebKit commits. | Mapping table |
| T-3 | P1 | Confirm 186015032 ship version when Safari 27.3 final notes publish (C-03). | Final notes |
| T-4 | P2 | Safari Technology Preview posts 252–256 not mined; 8015 and 8013 labs not reviewed. | Reviewed |

## WWDC

| ID | Priority | Gap | Completion evidence |
| --- | --- | --- | --- |
| W-1 | P1 | Transcripts not reviewed: 370, 282, 283, 284, 286, 320, 338, 393, 8013, 8014, 8015; ASL duplicates 111 and 112; remaining 60% of 8005; code samples and resources tabs not checked. | Reviewed with timestamps |
| W-2 | P2 | Confirm the "earlier session" in 8005 (58:39) is WWDC23 10034. | Transcript or resource link |

## Community evidence

| ID | Priority | Gap | Completion evidence |
| --- | --- | --- | --- |
| M-1 | P1 | AppleVis editorial or bug-tracker data for 27.0.1, 27.1 and 27.2 (403 on fixed pages); persistence of COMM-108–112 after 27.2. | Retrieved reports |
| M-2 | P1 | No macOS, watchOS, tvOS or visionOS AppleVis coverage; no low-vision, Voice Control or Switch Control reports; no Deque, TPGi or Level Access posts. | Targeted discovery |
| M-3 | P2 | Apple's 27.2 notes were not re-fetched in the community pass to check VoiceOver fixes (they were fetched in the iOS pass; none listed). | Cross-check recorded |

## Promotion gate (unchanged)

Research stays isolated until the agreed benchmark baselines exist. Then choose a small
source-backed candidate change, identify affected development cases, evaluate
frontier-agent quality and efficiency, and review regressions before touching released
skill guidance. Documentation evidence does not require mandatory manual verification; user
studies and runtime tests answer separate implementation and outcome questions.
