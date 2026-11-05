# API availability

Reviewed 2026-11-05 (second and third passes). Research only. Evidence: Apple DocC JSON at
`https://developer.apple.com/tutorials/data/documentation/<path>.json`, field
`metadata.platforms` (`introducedAt`, `deprecatedAt`, `beta`, `renamed`). Tier-1, evidence
type **API declaration**. A DocC platform entry records symbol availability. It does not
prove behavior, hardware support or a linked-SDK condition, and a release-note mention is
never used as an introduction date. "?" means the platform is listed with no
`introducedAt`. Unchecked symbols stay **pending**.

The third-pass scan covered 2,518 accessibility-matching symbols across SwiftUI, UIKit,
AppKit, Accessibility, MediaAccessibility and AVKit, plus targeted scans of AVFoundation,
XCUIAutomation, LiveCommunicationKit, Translation and PencilKit (WWDC notes, method note).

## Pass-2 records (preserved)

| ID | Symbol / Apple source | Introduced platforms | Interpretation | Pass-3 record |
| --- | --- | --- | --- | --- |
| API-01 | [accessibilityLinkedGroup(id:in:)](https://developer.apple.com/documentation/swiftui/view/accessibilitylinkedgroup(id:in:)) | iOS/iPadOS/Catalyst/tvOS 14; macOS 11; watchOS 7; visionOS 1 | Existing symbol. CROSS-01 describes new iOS-27 reading behavior, not API introduction. | API-101 (agrees) |
| API-02 | [TabsPickerStyle](https://developer.apple.com/documentation/swiftui/tabspickerstyle) | iOS/iPadOS/Catalyst/macOS/tvOS/visionOS 27 | New symbol; no watchOS entry. | API-117 (agrees) |
| API-03 | [UIAccessibilityCustomAction.editCategory](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/editcategory) | iOS/iPadOS/Catalyst/tvOS 18; visionOS 2 | Predates 27. | API-103 (agrees) |
| API-04 | [NSTextSelectionManager](https://developer.apple.com/documentation/appkit/nstextselectionmanager) | macOS 27 | New AppKit text-interaction abstraction. | API-133 (agrees) |
| API-05 | [NSToolbarItemGroup.role](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup/role-swift.property) | macOS/Catalyst 27; response also lists iOS/iPadOS 13 | Unexpected mobile metadata retained as received. | API-135; see [conflicts.md](conflicts.md) C-12 |

## A. New in the 27 SDKs (introducedAt 27.x)

| ID | Symbol | introducedAt | Accessibility relevance | Source (JSON path) | Cross-ref |
| --- | --- | --- | --- | --- | --- |
| API-116 | `MACaptionAppearanceDomain.videoConferencing` | iOS, macOS, tvOS, visionOS 27.0 (parent domain iOS 7.0) | Caption appearance domain. Empty DocC abstract; link to FaceTime captions is speculative. | [videoconferencing.json](https://developer.apple.com/tutorials/data/documentation/mediaaccessibility/macaptionappearancedomain/videoconferencing.json) | |
| API-117 | SwiftUI `TabsPickerStyle`, `PickerStyle.tabs` | iOS, iPadOS, Catalyst, macOS, tvOS, visionOS 27.0; **no watchOS** | Release notes: VoiceOver reads it as "tabs". | [tabspickerstyle.json](https://developer.apple.com/tutorials/data/documentation/swiftui/tabspickerstyle.json); [tabs.json](https://developer.apple.com/tutorials/data/documentation/swiftui/pickerstyle/tabs.json) | API-02; IOS-323; MAC-309; TV-140; VISION-223/274/310 |
| API-117a | `AVMediaCharacteristic.signLanguageInterpretationForAccessibility` | iOS, macOS, tvOS, visionOS, watchOS **27.1** | Marks a track that "provides a sign language interpretation of the spoken dialog". | [JSON](https://developer.apple.com/tutorials/data/documentation/avfoundation/avmediacharacteristic/signlanguageinterpretationforaccessibility.json) | Note: no OS 27.1 shipped except iOS for iPhone Duo; see [conflicts.md](conflicts.md) C-17 |
| API-117b | AVKit `AVPlaybackUserInterfaceMediaSelectionControllable` `legibleOptions` / `currentLegibleOption` | iOS, iPadOS, Catalyst 27.0 | Abstract mentions closed captions for accessibility and sign-language tracks. `AVPlaybackUserInterfaceContentMetadata.subtitle` is also 27.0 but is metadata. | [protocol](https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-2fftn.json) | |
| API-118 | `AccessibilitySettings.isApplicationAccessibilityEnabled`, `applicationAccessibilityEnabledDidChangeNotification`, `ApplicationAccessibilityEnabledDidChangeMessage` | all seven platforms 27.0 | Reports whether application accessibility is enabled for the process. | [JSON](https://developer.apple.com/tutorials/data/documentation/accessibility/accessibilitysettings/isapplicationaccessibilityenabled.json) | |
| API-119 | `AXSpeechAttributeSSML` | all seven platforms 27.0 | Attributed-string key; empty DocC abstract, semantics unverified. | [JSON](https://developer.apple.com/tutorials/data/documentation/accessibility/axspeechattributessml.json) | |
| API-120 | `AEAssessmentConfiguration.allowsAccessibilityVoiceOver`, `…SpokenContent` | iOS, macOS 27.0 | Exam-mode accessibility availability (WWDC26-230). | [VoiceOver JSON](https://developer.apple.com/tutorials/data/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilityvoiceover.json) | MAC-143; MAC-409; WWDC-123 |
| API-120 | `…SwitchControl`, `…VoiceControl`, `…Zoom`, `…HoverText`, `…LiveSpeech`, `…BackgroundSounds`, `…AlternativeInputMethods`, `…FullKeyboardAccess` | macOS, Catalyst 27.0 only | Same. Setting true does not enable the feature (WWDC26-230 ~4:13). | [SwitchControl JSON](https://developer.apple.com/tutorials/data/documentation/automaticassessmentconfiguration/aeassessmentconfiguration/allowsaccessibilityswitchcontrol.json) | |
| API-121 | SwiftUI `GestureInputKinds` (`.directTouch`, `.indirectTouch`) | all platforms 27.0 | Input-modality, not an accessibility API. | [JSON](https://developer.apple.com/tutorials/data/documentation/swiftui/gestureinputkinds/directtouch.json) | MAC-406 |
| API-122 | `XCUIVoiceOverService`, `XCUIDevice.voiceOverService`, `currentSpeech()`, `XCUIVoiceOverServiceErrorDomain` | iOS, iPadOS, Catalyst, macOS, tvOS, visionOS, watchOS 27.0 (JSON also lists "Xcode 16.3") | UI-test API that drives VoiceOver. | [JSON](https://developer.apple.com/tutorials/data/documentation/xcuiautomation/xcuivoiceoverservice.json) | XCODE-101/102; WWDC-132; [conflicts.md](conflicts.md) C-16 |
| API-123 | PencilKit `PKStrokeRecognizer`, `search(_:fullWordsOnly:caseMatchingOnly:)` | iOS, macOS, visionOS 27.0 | Handwriting recognition that WWDC26-203 links to VoiceOver. | [JSON](https://developer.apple.com/tutorials/data/documentation/pencilkit/pkstrokerecognizer.json) | WWDC-125 |
| API-124 | `View.directTouchSystemGesturesDisabled(_:)`; `NSWindow.disablesDirectTouchSystemGestures`; UIViewController `prefersDirectTouchSystemGesturesDisabled` family | macOS/Catalyst **27.3, `beta: true`** | Mac touch input, not VoiceOver direct touch. Do not conflate with `accessibilityDirectTouch`. | [JSON](https://developer.apple.com/tutorials/data/documentation/swiftui/view/directtouchsystemgesturesdisabled(_:).json) | Beta only |
| API-133 | AppKit `NSTextSelectionManager` | macOS 27.0 | Gesture-based text selection; NSTextView adopts it. | MAC-405 | API-04; MAC-119 |
| API-134 | `NSSegmentedControl.role`, `NSSegmentedControl.Role` (`automatic`, `tabs`, `valueSelection`) | macOS 27.0 | `tabs` role is read by VoiceOver as "tabs" (MAC-118). | [Role JSON page](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/role-swift.enum) | MAC-01; MAC-118 |
| API-135 | `NSToolbarItemGroup.Role` (enum) | iOS, iPadOS, Catalyst, macOS 27.0 | Toolbar group roles. The `role` property page was not re-fetched in pass 3. | MAC-405 | API-05; C-12 |
| API-136 | `NSMenuItem.preferredImageVisibility` | macOS 27.0 | Needed for image-only menu items once the 27 SDK hides images. | MAC-405 | MAC-120/139/140 |
| API-137 | `NSRefreshController`; `NSScrollView.refreshController` | macOS 27.0 | Pull-to-refresh. | MAC-405 | MAC-117 |
| API-138 | `NSScrollView.scrollGestureForRelationships`, `minimumNumberOfTouchesForScrolling` (`maximumNumberOfTouchesForScrolling` per MAC-212) | macOS 27.0 | Release notes call it `scrollGestureForFailureRelationship`. | [JSON page](https://developer.apple.com/documentation/appkit/nsscrollview/scrollgestureforrelationships) | MAC-212; C-02 |
| API-139 | `NSGestureRecognizer.isCancellableByScrollGesture` | macOS 27.0 | Release notes call it `cancellableByScrollGesture`. | [JSON page](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/iscancellablebyscrollgesture) | MAC-208; C-02 |
| API-140 | `NSView.exclusiveGestureBehavior` | macOS 27.0 | Opt-out of exclusive gesture hit-testing. | MAC-405 | MAC-209 |
| API-141 | `NSStatusItem.expandedInterfaceSession` | macOS 27.0 | Keyboard focus for custom status-item windows (WWDC26-289 6:34–8:22). | [JSON page](https://developer.apple.com/documentation/appkit/nsstatusitem/expandedinterfacesession) | MAC-408 |
| API-142 | `NSApplication.PresentationOptions.disableScreenCornerInteractions` | macOS 27.0 | Disables Hot Corners. | MAC-405 | MAC-207 |
| API-143 | SwiftUI `TextInputBorderShape`, `textInputBorderShape(_:)` | all platforms 27.0, including tvOS and watchOS | Text-field border shape; `.squareBorder`/`.roundedBorder` soft-deprecated per release notes. | [JSON](https://developer.apple.com/tutorials/data/documentation/swiftui/view/textinputbordershape%28_%3A%29.json) | MAC-310; TV-141; VISION-310 |
| API-144 | SwiftUI `View.asyncImageURLSession(_:)` | tvOS 27.0, watchOS 27.0 (others not recorded) | Not accessibility. | tvOS/watchOS notes, DocC checks | TV-138 |

## B. Older symbols whose behavior or platform support changed in 27

| ID | Symbol | introducedAt | 27 change and its source | Cross-ref |
| --- | --- | --- | --- | --- |
| API-101 | `View.accessibilityLinkedGroup(id:in:)` | iOS 14.0, macOS 11.0, tvOS 14.0, watchOS 7.0, visionOS 1.0 | Starting in iOS 27 it also links text navigation (WWDC26-219, 7:59–8:06). DocC abstract unchanged. | API-01; CROSS-01; WWDC-107 |
| API-110 | `EnvironmentValues.dynamicTypeSize`, `DynamicTypeSize.isAccessibilitySize` (tvOS 15.0); `UIContentSizeCategory.isAccessibilityCategory` (tvOS 11.0); `adjustsFontForContentSizeCategory` (tvOS 10.0) | as listed | tvOS 27 adds the system Text Size setting, so these existing symbols now respond on tvOS (WWDC26-221). | TV-01; TV-171–179 |
| API-111 | `EnvironmentValues.accessibilityShowBorders` | iOS 14.0, macOS 11.0, tvOS 14.0, watchOS 7.0, visionOS 1.0 | SOTU: macOS 27 "also supports" it (WWDC26-102, 23:25). DocC macOS 11.0 records symbol availability, not functional support. Related: `AccessibilitySettings.showBordersEnabled` 26.1; UIKit `buttonShapesEnabled` deprecated at 26.1. | MAC-04; MAC-325; WWDC-121; C-14 |
| API-132 | CarPlay `CPVoiceControlTemplate` | iOS 12.0 | From iOS 27 available to all CarPlay app categories (WWDC26-212, 7:08). Not the Voice Control assistive feature. | WWDC-124 |
| API-145 | `UIScene.extendStateRestoration()` | iOS 15.0, tvOS 15.0, visionOS 1.0 | Release notes frame extended restoration as behavior "when linked on iOS 27, tvOS 27". DocC date conflicts with that framing. | IOS-02; IOS-358; TV-157; C-04 |
| API-146 | `UIFontMetrics` | tvOS 11.0, watchOS 4.0 | Usable for custom-font scaling under tvOS Larger Text; not named in the WWDC26-221 transcript. | TV-180 |

## C. Older symbols revisited at WWDC26 (not new in 27, no 27 behavior change stated)

| ID | Symbol | introducedAt | Note |
| --- | --- | --- | --- |
| API-102 | `UIAccessibilityTraits.causesPageTurn`; SwiftUI `AccessibilityTraits.causesPageTurn` | UIKit iOS 5.0, watchOS 2.0, visionOS 1.0, tvOS ?; SwiftUI iOS 13.0, macOS 10.15, tvOS 13.0, watchOS 6.0, visionOS 1.0 | WWDC26-219 9:55 demonstrates it; not called new. |
| API-103 | `UIAccessibilityCustomAction.editCategory`, `.category`; SwiftUI `accessibilityActions(category:_:)` / `AccessibilityActionCategory` | iOS 18.0, tvOS 18.0, visionOS 2.0; SwiftUI adds macOS 15.0, watchOS 11.0 | API-03; WWDC26-219 11:46. |
| API-104 | `accessibilityNextTextNavigationElement` / `…Previous…` | iOS 18.0, Catalyst 18.0, visionOS 2.0; no tvOS or watchOS | WWDC26-219 7:00 says iOS 18 introduced them. |
| API-105 | AppKit `accessibilitySharedTextUIElements()` | macOS 10.10 | WWDC26-219 8:27. |
| API-106 | `View.accessibilityDirectTouch(_:options:)`, `.requiresActivation`, `.silentOnTouch` | iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, visionOS 1.0 | WWDC26-220 ~12:52–14:16. |
| API-107 | `accessibilityActivationPoint(_:)` (iOS 14.0); `accessibilityActivationPoint(_:isEnabled:)` (iOS 18.0); `accessibilityAdjustableAction(_:)` (iOS 13.0); `accessibilityAction(named:_:)` (iOS 16.0) | as listed | WWDC26-220. |
| API-108 | `AccessibilityNotification.Announcement` | iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, visionOS 1.0 | No 26.x or 27 children. |
| API-109 | `UITextInteraction` (iOS 13.0), `UITextInputStringTokenizer` (iOS 3.2), `textSelection(_:)` (iOS 15.0/macOS 12.0), `TextEditor` (iOS 14.0/macOS 11.0), `UIAccessibility.Notification.pageScrolled` (iOS 4.2) | as listed | WWDC26-219 text stack. |
| API-147 | `performAccessibilityAudit(for:_:)` (XCUIAutomation) | iOS 17.0, macOS 14.0, watchOS 10.0, tvOS 17.0 | No Xcode 27.x note mentions audit changes (XCODE-103). |
| API-148 | RealityKit `AccessibilityComponent` and members (`label`, `systemActions`, `customRotors`, `AccessibilityEvents`) | iOS 17.0, iPadOS 17.0, Catalyst 17.0, macOS 14.0, tvOS 26.0; **visionOS ? (pending)** | No new spatial-accessibility API found in 27 (VISION-305/306). |
| API-149 | RealityKit `HoverEffectComponent` (visionOS 1.0, iOS 18.0, macOS 15.0); `InputTargetComponent` (visionOS 1.0, iOS 18.0) | as listed | VISION-308. |
| API-150 | SwiftUI on visionOS 1.0: `hoverEffect(_:isEnabled:)`, `hoverEffectDisabled(_:)`, `accessibilityDirectTouch(_:options:)`, `accessibilityRepresentation(representation:)`, `accessibilityAction(_:_:)`, `accessibilityLabel(_:)` | visionOS 1.0 (iOS 13.0–17.0) | VISION-309. |

## D. Added in 26.1–26.4 and showcased at WWDC26 (label "26.x", not "27")

| ID | Symbol | introducedAt | Note |
| --- | --- | --- | --- |
| API-112 | `AVPlayerLayer.setCaptionPreviewProfileID(_:position:text:)`, `stopShowingCaptionPreview()` | iOS, macOS, tvOS, visionOS 26.4 | Session 256 presents them as this year's features (WWDC-120; C-13). |
| API-113 | `AVLegibleMediaOptionsMenuController` family | iOS, macOS, visionOS 26.4; **no tvOS** | |
| API-114 | `AVCaptionRenderer` (iOS 18.0, macOS 12.0, tvOS 26.4, visionOS 26.4); `captionPreview(forProfileID:extendedLanguageTag:renderSize:)` 26.4 on six platforms | as listed | |
| API-115 | `MACaptionAppearanceCopyProfileIDs()`, `MACaptionAppearanceSetActiveProfileID(_:)` (26.0); `AccessibilitySettings.Feature.captionStyles`, `canOpenSettings(for:)` (26.4) | as listed | |
| API-125 | `AccessibilitySettings.isReduceHighlightingEffectsEnabled`, `accessibilityReduceHighlightingEffects`, `accessibilityPrefersCrossFadeTransitions`, `AXOpenSettingsFeatureIsSupported` | 26.4, all platforms | |
| API-126 | `AccessibilitySettings.prefersActionSliderAlternative`, `showBordersEnabled` (+ notifications, C functions) | 26.1, all platforms | |

## E. Deprecations

### DocC `deprecatedAt` 27.0

| ID | Symbol | Introduced | Replacement |
| --- | --- | --- | --- |
| API-117c | `AVAssetWriterInputCaptionAdaptor`, `AVAssetReaderOutputCaptionAdaptor` | iOS 18.0 / macOS 12.0 | "Use AVAssetWriter.inputCaptionReceiver(for:) instead" |
| API-120 (part) | `AEAssessmentConfiguration.allowsAccessibilitySpeech` | iOS 14.0 | granular toggles above |

### DocC `deprecatedAt` 27.3 (no `beta` flag on the platform entries; re-verify at 27.3 GM)

| ID | Symbol | Introduced | Replacement |
| --- | --- | --- | --- |
| API-127 | SwiftUI `ContentSizeCategory` (all cases and `isAccessibilityCategory`) | | `renamed: "DynamicTypeSize"` |
| API-128 | SwiftUI `View.accessibility(label:)`, `(value:)`, `(hint:)`, `(hidden:)`, `(identifier:)`, `(inputLabels:)`, `(addTraits:)`, `(removeTraits:)`, `(sortPriority:)`, `(activationPoint:)` and `ModifiedContent` twins | 13.0 | e.g. `renamed: "accessibilityLabel(_:)"` |

### Deprecations stated only in release notes (DocC `deprecatedAt` pending)

| Release | Item | Claim IDs |
| --- | --- | --- |
| 27.0 | Scene-based life cycle required for apps built with the latest SDK, or they fail to launch | IOS-373; TV-158; VISION-251 |
| 27.0 | `canOpenURL:` deprecated | IOS-374 |
| 27.0 | On Demand Resources / `NSBundleResourceRequest` | IOS-218; TV-112 |
| 27.0 | `FileDocument` (and `ReferenceFileDocument` described as deprecated) | IOS-351; IOS-329 |
| 27.0 | `.squareBorder` / `.roundedBorder` soft-deprecated for `.bordered` | IOS-324; MAC-310; TV-141 |
| 27.0 | `barMinimizeBehavior`, `barMinimizationSafeAreaAdjustment` replaced by `navigationBarMinimization`; `toolbarMinimizeBehavior` replaced by `toolbarMinimizationBehavior` | IOS-364; IOS-331 |
| 27.0 | `PHAssetResource.originalFilename` replaced by nullable `filename` | TV-114 |
| 27.0 | `WKExtension`, `WKExtensionDelegate` (minimum deployment watchOS 9.2 or later) | WATCH-165 |
| 27.0 | `PreviewProvider` and its modifiers | XCODE-109 |
| 27.0 | AirPort Utility | IOS-103; MAC-105 |
| 27.2 | `EnablePasteboardPrivacyDeveloperPreview` default removed | MAC-374 |
| 27.2 | CSS `flow-tolerance` renamed `fit-tolerance` (grid-lanes) | WEB-147 |
| 27.3 beta | `IOUserSCSIParallelInterfaceController::UserGetDataBuffer` | MAC-383 |
| 27.3 beta | Live Caller ID Lookup and NEURLFilter PIR rules; NEURLFilter user tiers; Info.plist URL declaration | IOS-401, IOS-403–405; MAC-386–388 |
| 27.3 beta | Rosetta audio plug-in, print extension and printer-driver notifications (listed under Deprecations) | MAC-389; MAC-390 |

## F. Negative results (scan-backed)

- API-129: no new `AccessibilityTraits` or `UIAccessibilityTraits` in 27 (latest 17.0).
- API-130: no 27.x rotor, custom-content, `NSAccessibility` or `UIAccessibility` symbols in the
  2,518-symbol scan. The only 27.x Accessibility-framework items are API-118 and API-119.
- API-131: no public FaceTime interpreter API. LiveCommunicationKit's 27.2 additions are
  `LiveAssistance` / `LiveAssistanceExtension`; `supportsAudioTranslation` predates 27.
- API-117e: no DocC symbol for subtitle generation (115 AVFoundation paths scanned); consistent
  with WWDC26-256 ("you don't need to implement anything", 3:03).
- No visionOS detection API for Dwell Control, Face Gestures or Look to Drive was found
  (VISION Q3; not an exhaustive search).
- Apple's Accessibility updates page has no 2026 section; SwiftUI, UIKit, AppKit, AVKit and
  AVFoundation updates pages have no 2026 accessibility subsection (MAC-407; WWDC notes).

## Pending symbol checks

`UIMenuElement.preferredImageVisibility` (IPAD-106/MAC-352), `UISceneAccessory.externalNonInteractive`
and `registerSceneAccessory(_:)` (IOS-363), `UINavigationItem.navigationBarMinimization` (IOS-364),
`NSControl` `Events`, `NSView.beginDraggingSession(items:gesture:source:)` (MAC-406),
`NSTextTable` for UIKit clients (IOS-356), `concentricCornerRadii`, `TabRole.prominent`
(listed 27.0 on the SwiftUI updates page), the `NSToolbarItemGroup.role` property page, and a
full `NSAccessibility` diff. See [backlog.md](backlog.md).

## Research inference

Label API-101, API-110, API-111, API-132 and API-145 as "older symbol, behavior changed in
27". Do not emit "new in iOS 27" for `causesPageTurn`, `editCategory`, text-navigation
elements, `accessibilityDirectTouch` or `AccessibilityNotification` merely because WWDC26
demonstrated them. The 27 accessibility API delta is discoverable only from symbol JSON, not
from Apple's curated updates pages.
