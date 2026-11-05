# tvOS 27 and watchOS 27: release-note claim inventory with accessibility deep dive (snapshot 2026-11-05)

Conventions: Evidence tier T1 = Apple (developer docs, Support, Newsroom, WWDC video); T2 = editorial/expert; T3 = forum. Locators: (issue number) for release notes, [mm:ss] for WWDC26 video transcript, section title for Support pages. Status = New Feature (NF), Resolved Issue (RI), Known Issue (KI), Deprecation (DEP). "A11y" marks accessibility- or interaction-relevant entries. API availability is "pending" unless the DocC JSON check below verified it.

Source captures (curl of the `.md` endpoint, 2026-11-05):

| File | URL | HTTP | Bytes | SHA-256 |
|---|---|---|---|---|
| tvOS 27 | https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes.md | 200 | 17814 | ce009decc5f8bbb77078c5f7af19d88b40aee11fdc14e46b753661c5a73b945c |
| tvOS 27.1 | https://developer.apple.com/documentation/tvos-release-notes/tvos-27_1-release-notes.md | 404 (HTML error page) | 15639 | c8a4f47291ff4563e78e90f4326f3d457661a44a8041d823b1c21b325eb7c510 |
| tvOS 27.2 | https://developer.apple.com/documentation/tvos-release-notes/tvos-27_2-release-notes.md | 200 | 1517 | 9a03c402f490b5268ec88a22f0f51a5eb36ded1bba5b4d82445ba93528a04b88 |
| tvOS 27.3 beta | https://developer.apple.com/documentation/tvos-release-notes/tvos-27_3-release-notes.md | 200 | 1385 | 03c90f33be6a25c34a6fb57c0daebf0ea20696ef9528f443acc5e0e4840abe8e |
| watchOS 27 | https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes.md | 200 | 18698 | a3da0d4b4ae9899a49a61e919270bc7bf585e7881a578e1fe22d536f78971aa5 |
| watchOS 27.1 | https://developer.apple.com/documentation/watchos-release-notes/watchos-27_1-release-notes.md | 404 (same error page) | 15639 | c8a4f47291ff4563e78e90f4326f3d457661a44a8041d823b1c21b325eb7c510 |
| watchOS 27.2 | https://developer.apple.com/documentation/watchos-release-notes/watchos-27_2-release-notes.md | 200 | 1544 | 5848f6262abe5089ed3e786acb812377cbc52063bd909c3df4b5c501d1d0af29 |
| watchOS 27.3 beta | https://developer.apple.com/documentation/watchos-release-notes/watchos-27_3-release-notes.md | 200 | 1412 | 90b115bfa891a80175126fb6502ecb7d2e7f8bdcae0a2809d7dde49bac8fc1ea |

The release-notes index JSON files (https://developer.apple.com/tutorials/data/documentation/tvos-release-notes.json and .../watchos-release-notes.json) list only the 27, 27_2 and 27_3 pages for each platform. Neither lists a 27_1 page.

## For each release-note entry: section, status, Apple issue number, SDK-linked conditions, workaround

### Takeaway
The tvOS 27.0 notes have 62 entries and the watchOS 27.0 notes have 67. The 27.2 notes have 4 entries per platform and the 27.3 beta notes have 2, all of them StoreKit Testing. No 27.1 notes exist for either platform. Only a few entries matter for accessibility: tvOS focus highlight (177389941), tvOS AVKit subtitles-on-mute (177086166), tvOS TabsPickerStyle VoiceOver "tabs" (173211711), tvOS button tint (171830912), watchOS Digital Crown TabView selection (163517317), watchOS complications (177840928, 113202790), Smart Stack (178464737), Status Bar Always On (178633015), and heart-rate notifications (162788761).

### Cited Findings

#### tvOS 27.0 — https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes (all T1)
- TV-101 · App Intents · RI · (182532125): The `notes.appendText` schema "erroneously disappeared from the SDK"; fixed.
- TV-102 · Apple TV · RI · (177389941) · **A11y/focus**: Fixed: "When launching the Apple TV app, the sidebar focus highlight might briefly appear flat on the right side." This is the only focus-engine entry in the notes.
- TV-103 · AVKit Video Playback · RI · (177086166) · **A11y/captions**: Fixed: "When a video is muted or unmuted during playback, subtitles may not be automatically enabled or disabled as expected." The note adds that the subtitles-on-mute logic "has not yet been updated to account for the new system behavior". The wording is ambiguous because it is filed as Fixed (see Inferences).
- TV-104 · Background Assets · NF · (163944365): Localized asset packs, delivered according to the user's preferred languages.
- TV-105 · Foundation · RI · (161588649)(FB20439045): `+[NSURL URLWithString:]` no longer double-encodes `%` in valid percent-escapes.
- TV-106 · Game Center · RI · (172683368): The Access Point completion handler was never invoked; fixed.
- TV-107 · HomeKit · NF · (178858470): With Apple Intelligence in Home, HomeKit Secure Video recordings are processed on-device and through Private Cloud Compute for descriptions and search.
- TV-108 · HomeKit · NF · (181282161): Apple Intelligence for Home "requires an iCloud+ subscription starting at 2TB."
- TV-109 · Metal · RI · (172520325): A clamp-to-edge sampler might return zero; fixed.
- TV-110 · Metal · RI · (177318505): The same clamp-to-zero issue on the Apple 10 GPU family; fixed.
- TV-111 · Network Security · NF · (176055825): Select system processes (MDM, DDM, ADE, profile install, app install, software update) require TLS 1.2 or later with ATS-compliant ciphers and certificates. Reference: support.apple.com/en-us/126655.
- TV-112 · On Demand Resources · DEP · (170066290): ODR and `NSBundleResourceRequest` are deprecated; use Background Assets instead.
- TV-113 · PhotoKit · RI · (175050631): `PHAsset.addedDate` might return nil despite being non-nullable; fixed.
- TV-114 · PhotoKit · DEP · (175412725)(FB22589474): `PHAssetResource.originalFilename` is mis-annotated as non-null; the new nullable `filename` replaces it.
- TV-115 · RealityKit · RI · (172875414): Some MaterialX 1.39 nodes were unsupported; fixed.
- TV-116 · RealityKit · RI · (177674901): `ComputeGraphComponents` in a Reality file didn't render; fixed.
- TV-117 · RealityKit · RI · (177976245): `OpacityComponent` on opaque materials revealed interior surfaces in `RealityRenderer`; fixed.
- TV-118 · Security · RI · (183456836): ACME certificate issuance and Managed Device Attestation enrollments failed; fixed.
- TV-119 · ShaderGraph · RI · (177976666): The `realitykit_hair_surfaceshader` node lacked `DiffuseLightProbeGroupComponent` support; fixed.
- TV-120 · Siri · RI · (177464215): Siri might not resolve entity types that provide only an `EntityStringQuery`; fixed.
- TV-121 · StoreKit · NF · (156749517): Adds `Transaction.OwnershipType.assigned` and `RevocationType.assignmentRevoked` for volume purchases.
- TV-122 · StoreKit · NF · (160501742): `Product.ProductType` APIs for subscription Bundles and Suites, plus `Product.SubscriptionInfo.BundledSubscription`.
- TV-123 · StoreKit · NF · (167808780): `partnerName` and `partnerId` in `Transaction.AdvancedCommerceInfo` and `RenewalInfo.AdvancedCommerceInfo`.
- TV-124 · StoreKit · RI · (181766819)(FB23646993): The `Storefront` API returned wrong metadata in TestFlight; fixed.
- TV-125 · StoreKit · RI · (181842500): Non-subscription purchases via `SKTestSession.buyProduct()` failed, and `billingPlanType(_:)` was ignored; fixed.
- TV-126 · StoreKit · RI · (183165269): "Transactions fail to finish"; fixed.
- TV-127 · StoreKit Testing · RI · (102093015)(FB11767567): The unified receipt wasn't updated after a forced expiration; fixed.
- TV-128 · StoreKit Testing · RI · (154390284)(FB18403150): `disableDialogs` wasn't always respected; fixed.
- TV-129 · StoreKit Testing · RI · (160698598)(FB20269723): Transaction Manager upgrades were missing from `Transaction.updates`; fixed.
- TV-130 · StoreKit Testing · RI · (162014134)(FB20537538): The renewal behavior in `purchaseDate(_:renewalBehavior:)` was ignored; fixed.
- TV-131 · StoreKit Testing · RI · (174560379)(FB22475017): Re-purchasing a refunded non-consumable failed as "already owned"; fixed.
- TV-132 · StoreKit Testing · RI · (177942756): Wrong `pricingTerms.commitmentInfo.price` for a monthly subscription with a 12-month commitment; fixed.
- TV-133 · StoreKit Testing · RI · (178441109): Upgraded subscriptions were immediately marked expired; fixed.
- TV-134 · StoreKit Testing · RI · (183933307)(FB24137836): Intro offer eligibility didn't reset after `clearTransactions()`; fixed. The same entry appears again in the 27.2 notes (TV-163).
- TV-135 · StoreKit Testing · KI · (184155259): Storefront and locale changes in `SKTestSession` don't propagate through `Storefront.updates`. No workaround given. Fixed in 27.2 (TV-164).
- TV-136 · StoreKit Testing · KI · (184255116): Failed purchases show error dialogs even when `dialogsDisabled` is true. No workaround given. Fixed in 27.2 (TV-165).
- TV-137 · Swift Charts · RI · (174168981) · SDK/deployment condition: with a deployment target below 27.0, conditionals inside a `Chart` produced a `_ConditionalContent` warning and a possible runtime crash; fixed.
- TV-138 · SwiftUI · NF · (78212597): `AsyncImage` HTTP caching, `URLRequest` initializers, and `View.asyncImageURLSession(_:)`.
- TV-139 · SwiftUI · NF · (105893279): A macro-based `@State` (Xcode 27) avoids re-evaluating the initial-value expression. It "back-deploys to iOS 17 aligned OSes". Source breaks:
  - A declaration initial value combined with init assignment no longer compiles. Workaround: omit the declaration initial value.
  - The synthesized private memberwise init is disabled. Workaround: assign members explicitly.
  - Generic inference is weaker.
  - Composing with other wrappers or macros is unsupported.
- TV-140 · SwiftUI · NF · (173211711) · **A11y/VoiceOver**: `TabsPickerStyle` for tab-navigation pickers is "similar to the `.segmented` style, but VoiceOver reads it as 'tabs'". This entry is in tvOS notes but absent from watchOS notes.
- TV-141 · SwiftUI · NF · (173362083): `TextInputBorderShape` and `textInputBorderShape(_:)`. `.squareBorder` and `.roundedBorder` are soft-deprecated in favor of `.bordered`.
- TV-142 · SwiftUI · NF · (175594929) · SDK-linked: "In apps built with the 27.0 SDKs", `LabeledContent` in a `Menu` maps its value to the menu item subtitle.
- TV-143 · SwiftUI · NF · (175902616): `@Entry` warns about default class instances or closures in the environment.
- TV-144 · SwiftUI · NF · (177185166): `GeometryProxy.concentricCornerRadii` and `concentricCornerRadii(in:)` return `RectangleCornerRadii?`.
- TV-145 · SwiftUI · NF · (177526032): `@ContentBuilder` type-checking performance is improved compared with Beta 1.
- TV-146 · SwiftUI · NF · (179388848): Data-item and error-based `alert` and `confirmationDialog` back-deploy to tvOS 15.0 and watchOS 8.0, among other OSes.
- TV-147 · SwiftUI · RI · (154080867): Using both `.fileExporter` and `.fileMover` broke dialogs; fixed.
- TV-148 · SwiftUI · RI · (165913417) · SDK-linked (27.0 SDKs): `containerRelativeFrame` mis-applied safe-area insets on a ScrollView's non-scrollable axis; fixed.
  - Relevant to the WWDC26-221 grid technique, which uses `containerRelativeFrame` (see TV-176).
- TV-149 · SwiftUI · RI · (167448274) · SDK-linked: The `controlSize`, `buttonSizing`, `buttonRepeatBehavior`, `menuIndicatorVisibility`, and `ButtonBorderShape` environment values now reset to defaults in sheets and popovers.
- TV-150 · SwiftUI · RI · (169091260) · **A11y/interaction**: Fixed: "`Menu` labels cannot contain controls, views with gestures, or view representables with gesture recognizers." This entry is tvOS-only (absent from watchOS notes).
- TV-151 · SwiftUI · RI · (171830912) · **tvOS-specific, SDK-linked, visual/contrast**: "Buttons on tvOS no longer automatically use the accent color from an app's asset catalog as a label tint color when building against the tvOS 27 SDK."
- TV-152 · SwiftUI · RI · (175681345): Icon-to-title spacing for a Button in a List Section header or footer; fixed.
- TV-153 · SwiftUI · RI · (179149051)(FB23015259): `@State` with a raw identifier failed to compile; fixed.
- TV-154 · System · NF · (160612181): Swift `stat`, `lstat`, `fstat`, and `fstatat` APIs (`Stat`, `FilePath.stat()`, …), per SYS-0006.
- TV-155 · System · RI · (177911316): Unqualified `stat()` calls in custom extensions conflicted with the new methods (SYS-0008); fixed.
- TV-156 · TextKit · NF · (159870239): `NSTextTable` is available to UIKit clients in OS 27.
- TV-157 · UIKit · NF · (161843040) · SDK-linked: "When linked on iOS 27, tvOS 27, …", `UIScene.extendStateRestoration` and `completeStateRestoration` extend restoration across background-to-foreground transitions.
- TV-158 · UIKit · DEP · (141837548) · SDK-linked, breaking: Apps built with the latest SDK "must adopt the scene-based life cycle or they fail to launch". Migration guide linked.
- TV-159 · USDKit · RI · (170653056): Some USD attribute types couldn't be read or modified; fixed.
- TV-160 · USDKit · RI · (178071414): Array, vector, matrix, and quaternion authoring; fixed.
- TV-161 · VideoToolbox · NF · (177635243): `VTLowLatencySuperResolutionScalerConfiguration` supports a 1.5x scale factor (`+supportedScaleFactorsForFrameWidth:frameHeight:`).
- TV-162 · VideoToolbox · NF · (179040806): `VTLowLatencyFrameInterpolationConfiguration` accepts arbitrary source dimensions up to 1080p.

#### tvOS 27.2 — https://developer.apple.com/documentation/tvos-release-notes/tvos-27_2-release-notes (T1)
- TV-163 · StoreKit Testing · RI · (183933307)(FB24137836): Intro offer eligibility reset; listed again after its 27.0 appearance.
- TV-164 · StoreKit Testing · RI · (184155259): Storefront and locale propagation; fixed. This was a 27.0 KI.
- TV-165 · StoreKit Testing · RI · (184255116): Error dialogs despite `dialogsDisabled`; fixed. This was a 27.0 KI.
- TV-166 · StoreKit Testing · KI · (186018916): An in-app purchase of a bundle-member subscription "incorrectly allows the user to unbundle instead of throwing an error". No workaround given.
- No accessibility, AVKit, focus or UI entries in tvOS 27.2.

#### tvOS 27.3 beta (kept separate) — https://developer.apple.com/documentation/tvos-release-notes/tvos-27_3-release-notes (T1)
- TV-167 · StoreKit Testing · RI · (186018916): The bundle-unbundle issue from 27.2 is fixed.
- TV-168 · StoreKit Testing · KI · (186670057)(FB24651858): On first launch of an app using `SKTestSession`, some StoreKit Test API calls might hang.
  - **Workaround:** "Set a StoreKit configuration file in your scheme's run options, then rerun the tests."
- No accessibility entries in 27.3 beta.

#### watchOS 27.0 — https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes (all T1)
- WATCH-101 · App Intents · RI · (181763422): AppEntity instances have a cumulative 10MB limit including child properties; the app might crash past it, and the exception is logged.
- WATCH-102 · App Intents · RI · (182532125): The `notes.appendText` schema disappeared from the SDK; fixed.
- WATCH-103 · AV Conference Telephony · RI · (178187431): Outgoing FaceTime Audio from family-setup watches to iOS 27 beta devices might fail; fixed.
- WATCH-104 · Cellular · RI · (180062521): Verizon calls and Text-to-911 might fail after updating to or clean-installing watchOS 27.0 beta 2; fixed.
- WATCH-105 · Communication Safety · RI · (183962032): A sensitive QR code was detected as non-sensitive; fixed.
- WATCH-106 · Complications · RI · (177840928) · **A11y-adjacent/complications**: "Some complications might be missing in the Watch app's Face Gallery"; fixed.
- WATCH-107 · Foundation · RI · (161588649)(FB20439045): NSURL percent-escape double-encoding; fixed.
- WATCH-108 · Foundation Models · RI · (177684296): Private Cloud Compute didn't work in simulators; fixed.
- WATCH-109 · Foundation Models · RI · (177901494): Truncating transcript history in `onPrompt` caused a runtime error; fixed.
- WATCH-110 · Foundation Models · RI · (177902488): `onPrompt` wasn't called on a `Profile` without instructions; fixed.
- WATCH-111 · Foundation Models · RI · (178181782): `PrivateCloudComputeLanguageModel` always used greedy decoding; fixed.
- WATCH-112 · Foundation Models · RI · (178244470): `@Generable` on an enum failed to compile for watchOS; fixed.
- WATCH-113 · Foundation Models · RI · (179949809): The framework couldn't be imported for watchOS in Xcode 27 beta 2; fixed.
- WATCH-114 · Hardware Security · NF · (152103975) · **hardware-gated**: arm64e.x1 and CPA2 (stronger MIE protection). Supported on "Apple Watch models with S11 or later chips", plus A20 Pro iPhone and M6 Mac. Enabled via the Xcode enhanced security pane and a build setting.
- WATCH-115 · Health · listed under RI, but phrased as behavior, not "Fixed" · (162788761) · **A11y-adjacent/notifications**: While a third-party heart rate monitor is active, the watch "pauses background heart rate measurements and heart rate notifications" (irregular rhythm, high, low).
- WATCH-116 · HealthKit · NF · (135746152): Heart rate and cycling power zones.
- WATCH-117 · HealthKit · RI · (171273931)(FB22066297): A null unit converted incorrectly to count and percent; fixed.
- WATCH-118 · Network Security · NF · (176055825): The same stricter TLS for system processes as TV-111.
- WATCH-119 · Security · RI · (183456836): ACME and MDA failures; fixed.
- WATCH-120 · Siri · RI · (177464215): `EntityStringQuery`-only entity resolution; fixed.
- WATCH-121 · Siri · RI · (180303086): Siri AI couldn't complete some actions for English users outside the US; fixed.
- WATCH-122 · Siri · RI, phrased as a status statement · (182145010): "As of beta 5, Siri AI conversation history no longer syncs to devices running a prior beta." No conversations are lost.
- WATCH-123 · Siri · KI · (180434572): Siri may appear to be listening when it is not, after long silence with the UI on screen. No workaround.
- WATCH-124 · Siri · KI · (183040889): Siri AI conversations might not sync to the watch ("No iCloud is configured").
  - **Workaround:** on the watch, Settings > Apple Account triggers a refresh.
- WATCH-125 · Siri · KI · (183958361): Watches updated from an earlier beta might not sync Siri history; they usually self-recover.
  - **Workaround:** Settings > Apple Account on the watch.
- WATCH-126 · Sleep Focus · RI · (179960164): Sleep Focus didn't auto-toggle after reboot or update until unlock; fixed.
- WATCH-127 · Smart Stack · RI · (178464737) · **A11y-adjacent/widgets**: Tapping the Now Playing "Suggestions" widget didn't start playback; fixed.
- WATCH-128 · Status Bar · RI · (178633015): In Always On, the status-bar time may not update; fixed.
- WATCH-129–131 · StoreKit · NF · (156749517), (160501742), (167808780): Same as TV-121–123.
- WATCH-132–134 · StoreKit · RI · (181766819)(FB23646993), (181842500), (183165269): Same as TV-124–126.
- WATCH-135–143 · StoreKit Testing · RI: (102093015), (154390284), (160698598), (162014134), (174560379), (177942756), (178441109), (183933307), same as tvOS; plus **watchOS-only (178760994)**: "Purchases made with the original StoreKit API fail with an unknown error on watchOS"; fixed.
- WATCH-144–145 · StoreKit Testing · KI · (184155259), (184255116): Same as TV-135–136; both fixed in watchOS 27.2.
- WATCH-146 · Swift Charts · RI · (174168981): Same as TV-137.
- WATCH-147–154 · SwiftUI · NF: (78212597) AsyncImage; (105893279) `@State` macro; (173362083) TextInputBorderShape; (175594929) LabeledContent in Menu; (175902616) @Entry warnings; (177185166) concentricCornerRadii; (177526032) @ContentBuilder performance; (179388848) alert/confirmationDialog back-deploy to watchOS 8.0. **TabsPickerStyle (173211711) is NOT in the watchOS notes.**
- WATCH-155 · SwiftUI · RI · (154080867): fileExporter plus fileMover; fixed.
- WATCH-156 · SwiftUI · RI · (163517317) · **A11y/Digital Crown, SDK-linked, watchOS-only**: Fixed: "In apps built with the watchOS 27.0 SDK, `TabView.selection` updates only after the user has scrolled or rotated the Digital Crown past the 50% threshold…" Selection now updates as soon as the offset begins to change.
- WATCH-157 · SwiftUI · RI · (165913417): containerRelativeFrame safe-area insets; fixed.
- WATCH-158 · SwiftUI · RI · (167448274): Control environment values reset in sheets and popovers.
- WATCH-159 · SwiftUI · RI · (175681345): List section header button spacing; fixed.
- WATCH-160 · SwiftUI · RI · (179149051)(FB23015259): Raw-identifier `@State`; fixed.
- WATCH-161 · System · NF · (160612181): Swift stat APIs.
- WATCH-162 · System · RI · (177911316): stat() name conflicts; fixed.
- WATCH-163 · TextKit · NF · (159870239): `NSTextTable` available to "UIKit clients". This text is copied verbatim into the watchOS notes even though watchOS apps don't use UIKit directly (see Inferences).
- WATCH-164 · Watch Connectivity · RI · (113202790)(FB12819178) · **complications**: `WCSession.transferCurrentComplicationUserInfo` didn't work with WidgetKit complications; fixed.
- WATCH-165 · WatchKit · DEP · (70031637): `WKExtension` and `WKExtensionDelegate` are deprecated for a minimum deployment target of watchOS 9.2 or later.
- WATCH-166 · Workout · RI · (176497682): Mirrored Playback on iPhone didn't start; fixed.
- WATCH-167 · Workout · RI · (181296052) · **audio feedback**: In standalone mode with Siri AI on iPhone, Workout Alerts and Workout Buddy might fail to deliver audio announcements; fixed.
- The watchOS notes have no UIKit, AVKit, Metal, RealityKit, VideoToolbox, Background Assets, ODR, PhotoKit, HomeKit or Game Center sections.

#### watchOS 27.2 — https://developer.apple.com/documentation/watchos-release-notes/watchos-27_2-release-notes (T1)
- WATCH-168–170 · StoreKit Testing · RI · (183933307)(FB24137836), (184155259), (184255116): Identical to TV-163–165.
- WATCH-171 · StoreKit Testing · KI · (186018916): Bundle-member subscription unbundling. No workaround.

#### watchOS 27.3 beta (kept separate) — https://developer.apple.com/documentation/watchos-release-notes/watchos-27_3-release-notes (T1)
- WATCH-172 · StoreKit Testing · RI · (186018916): Fixed.
- WATCH-173 · StoreKit Testing · KI · (186670057)(FB24651858): First-launch `SKTestSession` hang.
  - **Workaround:** set a StoreKit configuration file in the scheme's run options.

#### DocC JSON availability checks (T1, https://developer.apple.com/tutorials/data/documentation/<path>.json, fetched 2026-11-05)
- `swiftui/tabspickerstyle`: iOS, iPadOS, Mac Catalyst, macOS, tvOS and visionOS 27.0. **No watchOS entry**, consistent with TV-140 being absent from the watchOS notes. Verified.
- `swiftui/view/asyncimageurlsession(_:)`: tvOS 27.0, watchOS 27.0, among others. Verified.
- `swiftui/textinputbordershape`: tvOS 27.0, watchOS 27.0. Verified.
- `uikit/uiscene/extendstaterestoration()`: DocC lists **tvOS 15.0** (iOS 15.0, visionOS 1.0), not 27.0. The release note (161843040) frames the behavior as linked on 27 SDKs, so this is a conflict.
- `uikit/uifontmetrics`: tvOS 11.0, watchOS 4.0. Long-standing, so it is usable for tvOS Larger Text today. Verified.
- All other APIs named above: **pending** (not checked).

### Inferences
- The tvOS and watchOS 27.0 notes are largely cross-platform boilerplate (StoreKit, SwiftUI, System, TextKit, Security, Network Security). Platform-specific substance is concentrated in:
  - tvOS: Apple TV focus, AVKit subtitles, VideoToolbox, tvOS button tint, Menu labels.
  - watchOS: Digital Crown TabView, complications, Smart Stack, Health, Siri AI, Workout, cellular.
- TV-103 reads like a known issue that was relabeled "Fixed" without its text being rewritten. Treat the subtitles-on-mute behavior on tvOS 27 as unverified and test it.
- 183933307 appears as Resolved in both 27.0 and 27.2, which looks like a carry-over duplicate.
- WATCH-163 (NSTextTable for "UIKit clients") is probably irrelevant to third-party watchOS apps.
- Shared-framework entries that actually apply:
  - tvOS: TabsPickerStyle, the tvOS button tint change, Menu label content, `UIScene` state restoration, and the scene-life-cycle mandate.
  - watchOS: the Digital Crown TabView fix, the WidgetKit complication transfer, and `WKExtension` deprecation.
  - Both: AsyncImage, the `@State` macro, TextInputBorderShape, LabeledContent in Menu, concentricCornerRadii, the alert/confirmationDialog back-deploy, the containerRelativeFrame fix, and the sheet environment reset.

### Gaps
- No release notes exist for 27.1 on either platform (404, and absent from the index JSON). I can't tell whether Apple skipped 27.1 or published no developer notes for it; see the next section.
- Exact "Beta N" provenance of each 27.0 entry isn't shown on the consolidated page.

## tvOS Larger Text: what shipped, sizes, automatic versus adoption, APIs, hardware limits; WWDC26 session and Support guide

### Takeaway
tvOS 27 adds a system Text Size slider at Settings > Accessibility > Display > Text Size. Its sizes run from "Large" (the default) up to "Accessibility XXXL". Standard UIKit and SwiftUI components (labels, buttons, navigation and tab bars) scale automatically. Custom UI must adopt text styles: `.font(.caption)` in SwiftUI, and `preferredFont(forTextStyle:)` plus `adjustsFontForContentSizeCategory` in UIKit. Layouts must also adapt, using `dynamicTypeSize.isAccessibilitySize` or `preferredContentSizeCategory.isAccessibilityCategory`. The authoritative session is WWDC26-221, "Prepare your tvOS apps for Dynamic Type". Hardware is bounded by tvOS 27 itself, which runs on Apple TV 4K (2nd generation) and later.

### Cited Findings
- TV-169 (T1): The May 2026 accessibility preview says "Larger Text support is coming to tvOS, so viewers who have low vision can increase onscreen text size to be easier to read." Locator: tvOS paragraph and image captions of a Prehistoric Planet menu at standard and larger size. — [Apple Newsroom, May 2026](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/)
- TV-170 (T1): The same release says generated subtitles "appear automatically for uncaptioned videos on iPhone, iPad, Mac, Apple TV, and Apple Vision Pro". They are produced by on-device speech recognition, and their appearance can be customized in the playback menu or in Settings. Locator: subtitles paragraph, footnote 4. — [Apple Newsroom, May 2026](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/)
- TV-171 (T1): WWDC26-221 [0:12]–[0:20]: "Large Text support is now available, bringing system-wide text scaling to every app on the platform." — [WWDC26 session 221](https://developer.apple.com/videos/play/wwdc2026/221/)
- TV-172 (T1): WWDC26-221 [0:40]–[0:43] and [9:46]: developers can indicate Larger Text support in "Accessibility Nutrition Labels for tvOS in the App Store". — [WWDC26-221](https://developer.apple.com/videos/play/wwdc2026/221/)
- TV-173 (T1): WWDC26-221 [1:21]–[1:30]: "Dynamic Type works the same way on tvOS." UIKit and SwiftUI adapt text sizes automatically. — [WWDC26-221](https://developer.apple.com/videos/play/wwdc2026/221/)
- TV-174 (T1): WWDC26-221, sizes and path:
  - [1:38]–[1:41]: Settings > Accessibility > Display > Text Size.
  - [1:47]–[1:49]: sizes run "starting at Large all the way up to Accessibility XXXL".
  - So the only change is upward from the default. The session does not mention xSmall, Small or Medium.
  - [WWDC26-221](https://developer.apple.com/videos/play/wwdc2026/221/)
- TV-175 (T1): WWDC26-221, automatic versus custom:
  - [2:31]–[2:37]: "Standard UIKit and SwiftUI components like Labels, Buttons and Navigation tabBars handle this automatically."
  - [2:40]–[2:43]: "your job is just to identify and update any custom elements".
  - [WWDC26-221](https://developer.apple.com/videos/play/wwdc2026/221/)
- TV-176 (T1): WWDC26-221, issues and fixes:
  - [2:54]–[3:15]: avoid fixed font sizes and hard-coded sizes or constraints, which cause truncation and clipping.
  - [4:56]–[5:00] and code at 4:58: replace a fixed size with the semantic style `.caption`.
  - [5:17]–[5:24] and code at 5:10: replace `.frame(width: 300)` with `.frame(maxWidth: .infinity)`.
  - [WWDC26-221](https://developer.apple.com/videos/play/wwdc2026/221/)
- TV-177 (T1): WWDC26-221 [5:55]–[6:08], code at 5:55, UIKit: replace `UIFont.boldSystemFont(ofSize: 28)` with `UIFont.preferredFont(forTextStyle: .headline)` and set `adjustsFontForContentSizeCategory = true`. — [WWDC26-221](https://developer.apple.com/videos/play/wwdc2026/221/)
- TV-178 (T1): WWDC26-221, media grids:
  - [6:25]–[7:21] and code at 7:09: a poster `LazyHStack` reads `@Environment(\.dynamicTypeSize)` and calls `containerRelativeFrame(.horizontal, count: dynamicTypeSize.isAccessibilitySize ? 4 : 6, spacing: 40)`.
  - [7:26]: "consider a custom marquee strategy" for longer titles.
  - [WWDC26-221](https://developer.apple.com/videos/play/wwdc2026/221/)
- TV-179 (T1): WWDC26-221, cards:
  - [8:03]–[8:27] and code at 8:07: SwiftUI `AnyLayout` switches between `VStackLayout` and `HStackLayout` on `isAccessibilitySize`.
  - [8:33]–[8:49] and code at 8:31: UIKit flips `UIStackView.axis` on `traitCollection.preferredContentSizeCategory.isAccessibilityCategory`, with `registerForTraitChanges([UITraitPreferredContentSizeCategory.self], action:)`.
  - [WWDC26-221](https://developer.apple.com/videos/play/wwdc2026/221/)
- TV-180 (T1): Session metadata: chapters at 0:01 Introduction, 2:46 Identify common issues, and 6:13 Adapt your layout. Listed resources are "Applying custom fonts to text" and "Scaling fonts automatically"; the related video is WWDC24 "Get started with Dynamic Type". `UIFontMetrics` is not named in the transcript; custom-font scaling is covered only through the "Applying custom fonts to text" resource link. — [WWDC26-221](https://developer.apple.com/videos/play/wwdc2026/221/)
- TV-181 (T1): The Apple TV 4K User Guide page "Display bold text or change the text size" gives the path Settings > Accessibility > Display, with Bold Text and Text Size. It says "Apps that support Dynamic Type automatically adjust to the Text Size setting." It also says "Not all features… on all Apple TV hardware models." — [Apple Support: Display bold text or change the text size on Apple TV 4K](https://support.apple.com/guide/tv/display-bold-text-or-change-the-text-size-atvb0222141c/tvos)
- TV-182 (T1): "What's new in tvOS 27" says: "You can now adjust the text size across all apps that support Dynamic Text on Apple TV 4K". "Dynamic Text" is Apple's own wording there. The page also lists the redesigned Podcasts app (video podcasts, sidebar) and Music app (sidebar, transitions, 24-bit/192 kHz lossless). — [Apple Support: What's new in tvOS 27](https://support.apple.com/guide/tv/whats-new-in-tvos-27-atvb457e13ae/27/tvos/27)
- TV-183 (T1): Hardware: Apple's security releases page lists tvOS 27 for "Apple TV 4K (2nd generation and later)". tvOS 26.x was listed for Apple TV HD and all Apple TV 4K models. — [Apple security releases](https://support.apple.com/en-us/100100)
- TV-184 (T1): Separate, pre-existing tvOS text aids remain in the guide:
  - Hover Text (atvb8f832e2e)
  - Zoom
  - Change subtitle settings (atvb7d97de8b)
  - Closed captions/SDH (atvb1d61ca06)
  - Adjust VoiceOver settings (atvbbcb628a8)
  - [Apple TV 4K User Guide TOC](https://support.apple.com/guide/tv/welcome/tvos)
- TV-185 (T2): Editorial coverage notes that some major streaming apps don't use Apple's own UI frameworks, so they may not respond to Larger Text. — [TechRadar](https://www.techradar.com/televisions/streaming-devices/apple-is-introducing-useful-accessibility-features-in-tvos-27-for-apple-tv-4k-that-will-appeal-to-everyone-including-larger-text-and-auto-generated-subtitles-but-some-major-streaming-apps-dont-use-apples-own-app-tech-that-enables-them); [MacRumors preview, 2026-05-20](https://macrumors.com/2026/05/20/apple-previews-new-tvos-27-feature/); [9to5Mac](https://9to5mac.com/2026/05/20/tvos-27-will-give-apple-tv-4k-a-useful-new-display-setting/)
- TV-186 (T2): AppleVis reports that tvOS 27 shipped on 2026-09-14 with larger accessibility text sizes. The page body could not be fetched (HTTP 403); this comes from a search snippet only. — [AppleVis: Apple Releases tvOS 27](https://applevis.com/blog/apple-releases-tvos-27)

### Inferences
- There is a wording conflict:
  - The session says "every app on the platform" [0:18].
  - The Support guide says only apps that support Dynamic Type adjust.
  - The session's own content shows custom or hard-coded UI won't scale.
  - Treat Larger Text as system-wide for the system UI and for standard components, and as adoption-dependent for custom text.
- Because sizes start at Large (the tvOS default), the effective range is Large through AX5 (Accessibility XXXL). Layout testing should focus on `isAccessibilitySize`.
- TV-151 (the button tint change) and TV-148 (the containerRelativeFrame fix) interact with Larger Text grid layouts and focus visuals in 27-SDK builds.

### Gaps
- No Apple source names a tvOS hardware restriction specific to Larger Text beyond tvOS 27's own Apple TV 4K (2nd generation and later) floor. "Not all… hardware models" is generic boilerplate.
- No Apple statement says whether AVKit's `AVPlayerViewController` transport and info panels scale with Text Size, or whether caption size is tied to it. Generated-subtitle API surface: none found (pending).
- No WWDC26 tvOS focus-engine or Siri Remote input changes were found. No tvOS VoiceOver changes were found in Apple sources.
- `UIFontMetrics` is not discussed in the session. Its tvOS availability (11.0) is verified only through DocC.

## watchOS 27: new accessibility features, gesture changes, hardware and model restrictions

### Takeaway
Apple documents two watchOS 27 interaction and accessibility changes:
- **Sound Recognition directly on Apple Watch:** continuous listening, Apple Watch Series 12 and Apple Watch Ultra 4 only, set up from iPhone at Accessibility > Sound & Name Recognition.
- **A new single tap gesture:** selects a widget in the Smart Stack, alongside the existing double tap.

watchOS 27 itself requires Series 9 or later (Ultra 2, SE 3), and Siri AI has the same model floor. I found no Apple source describing new watchOS 27 VoiceOver, AssistiveTouch, text-size or haptics features. Wrist flick and Cover to Mute are documented as current gestures, not new ones. AppleVis (T2) reports a new VoiceOver "Tap to Wake" toggle.

### Cited Findings
- WATCH-174 (T1): "What's new in watchOS 27" says Series 12 and Ultra 4 "can continuously listen for certain sounds—such as a doorbell, siren, or crying baby—and notify you". Locator: "Sound Recognition in Accessibility" bullet. — [Apple Support: What's new in watchOS 27](https://support.apple.com/guide/watch/whats-new-apdb93ea3872/watchos)
- WATCH-175 (T1): "Recognize sounds using Apple Watch":
  - Note: "Sound recognition is available on Apple Watch Series 12 and Apple Watch Ultra 4."
  - Setup on iPhone: Settings > Accessibility > Sound & Name Recognition > Sound Recognition, then choose Sounds.
  - Turn off: "Detect using Apple Watch".
  - Safety caveat: not for high-risk or emergency situations.
  - [Apple Support: Use Sound Recognition](https://support.apple.com/guide/watch/use-sound-recognition-ay39m4y6riek/watchos)
- WATCH-176 (T1): New gesture: "When you're viewing widgets in the Smart Stack, perform the single tap gesture to select a widget." Locator: "Open Smart Stack widgets with a single tap" bullet. — [What's new in watchOS 27](https://support.apple.com/guide/watch/whats-new-apdb93ea3872/watchos)
- WATCH-177 (T1): "Use tap gestures": single tap is "Tap your index finger and thumb together"; double tap is the same, twice.
  - Double tap is unsupported when:
    - Low Power Mode is on
    - Sleep Focus is active
    - the wrist is down
    - the watch is locked
    - "Accessibility features that use hand gestures are turned on"
    - the watch is set up for a family member
  - New settings: Playback (Play/Pause or Skip), "Ignore Tap Gestures" while using Apple Vision Pro, and Off.
  - [Apple Support: Use tap gestures](https://support.apple.com/guide/watch/use-tap-gestures-apdabb7b275c/watchos)
- WATCH-178 (T1): Wrist flick: "quickly turn your wrist over and back to dismiss anything". Cover to Mute requires resting a palm on the display for at least 3 seconds, and "A haptic tap confirms" the mute. Both are on by default; toggle them in Settings > Gestures. Not marked new in watchOS 27. — [Apple Support: Use gestures for notifications and alerts](https://support.apple.com/guide/watch/use-gestures-for-notifications-and-alerts-apd8bcbaa778/watchos)
- WATCH-179 (T1): Text size: Control Center offers a text-size control adjusted with the Digital Crown. Settings > Accessibility lists On/Off Labels, Reduce Transparency, Increase Contrast, Show Borders, Color Filters, Minimum Brightness, Text Size and Bold Text. Restart is needed for bold and grayscale. Nothing is marked new. — [Apple Support: Adjust text and display settings](https://support.apple.com/guide/watch/adjust-text-and-display-settings-apd766b7bd85/watchos)
- WATCH-180 (T1): The Apple Watch User Guide (watchOS 27) accessibility TOC lists:
  - VoiceOver (setup, basics, braille display, Bluetooth keyboard)
  - Apple Watch Mirroring, Control nearby devices
  - AssistiveTouch, Adjust motor skills settings, Automatically open the focused app
  - RTT, Live Listen, Sound Recognition
  - Type to speak, Tell time with haptic feedback
  - [Apple Watch User Guide TOC](https://support.apple.com/guide/watch/whats-new-apdb93ea3872/watchos)
- WATCH-181 (T1): Other watchOS 27 items with interaction relevance:
  - Dynamic app grid: Siri-suggested apps, with the Siri app always in the center.
  - Siri Modular face.
  - Steps complication (Series 12 and Ultra 4).
  - Shazam in the Smart Stack (Series 12 and Ultra 4).
  - Find My consolidation.
  - Workout Buddy works without iPhone.
  - [What's new in watchOS 27](https://support.apple.com/guide/watch/whats-new-apdb93ea3872/watchos)
- WATCH-182 (T1): Siri AI (beta) model floor: "Apple Watch Series 9 and later, Apple Watch Ultra 2 and later, and Apple Watch SE 3". It requires an Apple Intelligence iPhone (15 Pro or later), is not initially in the EU, and is not for users under 13. — [What's new in watchOS 27](https://support.apple.com/guide/watch/whats-new-apdb93ea3872/watchos)
- WATCH-183 (T1): The security releases page lists watchOS 27 and 27.2 for "Apple Watch Series 9 and later". watchOS 26.x was listed for Series 6 and later. — [Apple security releases](https://support.apple.com/en-us/100100)
- WATCH-184 (T1): The May 2026 accessibility release mentions Name Recognition across more than 50 languages, with no platform list in the captured paragraph. My extraction of that page found no watchOS-specific features. — [Apple Newsroom, May 2026](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/)
- WATCH-185 (T1): WWDC26 has no dedicated watchOS accessibility session in search results. The closest are the watchOS Group Lab (8014) and the Accessibility Technologies Group Lab (8005). The WWDC26 watchOS guide notes that SwiftUI reordering comes to watchOS. — [watchOS Group Lab](https://developer.apple.com/videos/play/wwdc2026/8014/); [Accessibility Technologies Group Lab](https://developer.apple.com/videos/play/wwdc2026/8005/); [WWDC26 watchOS guide](https://developer.apple.com/wwdc26/guides/watchos/)
- WATCH-186 (T2): AppleVis "watchOS 27: A Summary of VoiceOver Features, Issues, and Improvements" reports a new "Tap to Wake" toggle in VoiceOver settings and limited beta testing. Search snippet only; HTTP 403 on fetch. — [AppleVis](https://applevis.com/comment/215526)
- WATCH-187 (T2): Model lists in editorial coverage conflict. Tom's Guide lists six models (Series 9, 10, 11, Ultra 2, Ultra 3, SE 3); Geeky Gadgets says "Series 9, SE (2nd generation)". The Apple T1 floor is Series 9 and later, Ultra 2 and later, and SE 3 (WATCH-182 and WATCH-183). — [Tom's Guide](https://tomsguide.com/wellness/smartwatches/watchos-27-all-the-new-features-coming-to-apple-watch-later-this-year); [Geeky Gadgets](https://www.geeky-gadgets.com/apple-watch-watchos-27-guide/)

### Inferences
- Sound Recognition "on Apple Watch" is gated to the new S11-generation hardware (Series 12 and Ultra 4), not to all watchOS 27 watches. Older watches presumably keep iPhone-side Sound Recognition.
- The single-tap gesture requires double-tap-capable hardware (Series 9 and later, Ultra 2 and later), but Apple's page doesn't state a model list. Test apps for Smart Stack widget selection by single tap.
- The developer-relevant interaction fixes are WATCH-156 (Digital Crown TabView selection, 27 SDK) and WATCH-164 (complication transfer).

### Gaps
- No Apple source on watchOS 27 changes to VoiceOver, AssistiveTouch, haptics, notifications or Digital Crown accessibility (beyond WATCH-156).
- Single-tap hardware list: not stated by Apple.
- No Apple confirmation of AppleVis's "Tap to Wake".

## 27.1 changes, release dates and builds

### Takeaway
There was no tvOS 27.1 or watchOS 27.1. Releases went from 27.0 (14 Sep 2026) to 27.2 (26 Oct 2026). watchOS also had 27.0.1 (28 Sep). The 27.3 betas arrived on 3 Nov 2026.

### Cited Findings
- REL-1 (T1): Developer Releases RSS:
  - tvOS 27.0 (24J361) and watchOS 27.0 (24R364): 2026-09-14
  - watchOS 27.0.1 (24R365): 2026-09-28
  - tvOS 27.2 beta 3 (24K5103f): 2026-10-05
  - tvOS 27.2 (24K122) and watchOS 27.2 (24S118): 2026-10-26
  - tvOS 27.3 beta (24K5286g) and watchOS 27.3 beta (24S5284h): 2026-11-03
  - watchOS 27.0 beta 1 was 24R5289n (2026-06-08)
  - [Apple Developer Releases RSS](https://developer.apple.com/news/releases/rss/releases.rss); e.g. [tvOS 27.2](https://developer.apple.com/news/releases/?id=10262026e), [watchOS 27.2](https://developer.apple.com/news/releases/?id=10262026g), [watchOS 27.0.1](https://developer.apple.com/news/releases/?id=09282026e), [watchOS 27.0 beta](https://developer.apple.com/news/releases/?id=06082026g)
- REL-2 (T1): The security releases page lists tvOS 27 and watchOS 27 (14 Sep 2026) and tvOS 27.2 and watchOS 27.2 (26 Oct 2026). It has no 27.1 entries. My extraction did not surface a watchOS 27.0.1 row. — [Apple security releases](https://support.apple.com/en-us/100100)
- REL-3 (T1): The 27_1 release-notes URLs return 404, and the index JSON lists no 27.1 page (see the capture table).

### Inferences
- The "27.1" in the brief has no artifact for these two platforms. The 27.2 content (StoreKit Testing only) is the first point release.

### Gaps
- Why the version skipped from 27.0 to 27.2 is undocumented. The watchOS 27.0.1 content and security notes were not found.

## Shared-framework (SwiftUI/UIKit) changes that actually apply on tvOS or watchOS

### Takeaway
Applicability is established by each platform's notes listing the entry, plus DocC where verified.
- **tvOS only:** TabsPickerStyle (VoiceOver "tabs"), the button tint change, Menu labels with controls, the `UIScene` state restoration APIs, and the mandatory scene life cycle.
- **watchOS only:** the Digital Crown `TabView` fix, the `WKExtension` deprecation, and the `WCSession` complication fix.
- **Both:** the remaining SwiftUI entries.

### Cited Findings
- tvOS-only shared-framework entries: TV-140 (173211711), TV-150 (169091260), TV-151 (171830912), TV-157 (161843040), TV-158 (141837548). — [tvOS 27 RN](https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes)
- watchOS-only: WATCH-156 (163517317), WATCH-164 (113202790), WATCH-165 (70031637), and the original StoreKit API fix (178760994). — [watchOS 27 RN](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes)
- Both platforms: (78212597), (105893279), (173362083), (175594929), (175902616), (177185166), (177526032), (179388848), (154080867), (165913417), (167448274), (175681345), (179149051), (159870239). — both RN URLs above
- DocC: TabsPickerStyle has no watchOS availability. AsyncImage URLSession and TextInputBorderShape are available on tvOS and watchOS 27.0. — [DocC JSON](https://developer.apple.com/tutorials/data/documentation/swiftui/tabspickerstyle.json)

### Inferences
- The tvOS 27 SDK scene-life-cycle mandate (141837548) is the highest-impact UIKit change for tvOS apps.
- 171830912 changes the tint and contrast of tvOS button labels, so re-check focus-state contrast.

### Gaps
- DocC availability of most other symbols (concentricCornerRadii, the Transaction enum cases, `.bordered` text field style) is pending.
