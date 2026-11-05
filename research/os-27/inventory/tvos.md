# tvOS 27 release-note inventory

Research only. Mechanically transferred from the pass-3 research notes on 2026-11-05 (script `build_inventory.py`, not retyped). Every row is **Tier-1**, evidence type **release note**. Apple text is truncated in the notes (22 words or fewer). Symbol availability for any API named here is pending unless [api-availability.md](../api-availability.md) records DocC metadata. The `Pass-2 ID` column cross-references earlier claim IDs by Apple issue number.

Sources: [27.0](https://developer.apple.com/documentation/tvos-release-notes/tvos-27-release-notes) (17,814 bytes), [27.2](https://developer.apple.com/documentation/tvos-release-notes/tvos-27_2-release-notes) (1,517 bytes), [27.3 beta](https://developer.apple.com/documentation/tvos-release-notes/tvos-27_3-release-notes) (1,385 bytes). No tvOS 27.1 exists.

The notes recorded these entries as bullets, not a table; this file converts them mechanically. Status codes: NF New Feature, RI Resolved Issue, KI Known Issue, DEP Deprecation. Where the notes grouped several entries under one ID range, the rows are expanded in listing order and marked.

## Stable: 27.0 (62 entries)

| Claim ID | Release | Section | Status | Issue (FB) | SDK-linked | A11y / interaction flag | Entry (notes' paraphrase and quotes) | Transfer note | Pass-2 ID |
|---|---|---|---|---|---|---|---|---|---|
| TV-101 | 27.0 | App Intents | Resolved | 182532125 |  |  | The `notes.appendText` schema "erroneously disappeared from the SDK"; fixed. |  |  |
| TV-102 | 27.0 | Apple TV | Resolved | 177389941 |  | A11y/focus | Fixed: "When launching the Apple TV app, the sidebar focus highlight might briefly appear flat on the right side." This is the only focus-engine entry in the notes. |  | TV-03 |
| TV-103 | 27.0 | AVKit Video Playback | Resolved | 177086166 |  | A11y/captions | Fixed: "When a video is muted or unmuted during playback, subtitles may not be automatically enabled or disabled as expected." The note adds that the subtitles-on-mute logic "has not yet been updated to account for the new system behavior". The wording is ambiguous because it is filed as Fixed (see Inferences). |  |  |
| TV-104 | 27.0 | Background Assets | New Feature | 163944365 |  |  | Localized asset packs, delivered according to the user's preferred languages. |  |  |
| TV-105 | 27.0 | Foundation | Resolved | 161588649 (FB20439045) |  |  | `+[NSURL URLWithString:]` no longer double-encodes `%` in valid percent-escapes. |  |  |
| TV-106 | 27.0 | Game Center | Resolved | 172683368 |  |  | The Access Point completion handler was never invoked; fixed. |  |  |
| TV-107 | 27.0 | HomeKit | New Feature | 178858470 |  |  | With Apple Intelligence in Home, HomeKit Secure Video recordings are processed on-device and through Private Cloud Compute for descriptions and search. |  |  |
| TV-108 | 27.0 | HomeKit | New Feature | 181282161 |  |  | Apple Intelligence for Home "requires an iCloud+ subscription starting at 2TB." |  |  |
| TV-109 | 27.0 | Metal | Resolved | 172520325 |  |  | A clamp-to-edge sampler might return zero; fixed. |  |  |
| TV-110 | 27.0 | Metal | Resolved | 177318505 |  |  | The same clamp-to-zero issue on the Apple 10 GPU family; fixed. |  |  |
| TV-111 | 27.0 | Network Security | New Feature | 176055825 |  |  | Select system processes (MDM, DDM, ADE, profile install, app install, software update) require TLS 1.2 or later with ATS-compliant ciphers and certificates. Reference: support.apple.com/en-us/126655. |  |  |
| TV-112 | 27.0 | On Demand Resources | Deprecation | 170066290 |  |  | ODR and `NSBundleResourceRequest` are deprecated; use Background Assets instead. |  |  |
| TV-113 | 27.0 | PhotoKit | Resolved | 175050631 |  |  | `PHAsset.addedDate` might return nil despite being non-nullable; fixed. |  |  |
| TV-114 | 27.0 | PhotoKit | Deprecation | 175412725 (FB22589474) |  |  | `PHAssetResource.originalFilename` is mis-annotated as non-null; the new nullable `filename` replaces it. |  |  |
| TV-115 | 27.0 | RealityKit | Resolved | 172875414 |  |  | Some MaterialX 1.39 nodes were unsupported; fixed. |  |  |
| TV-116 | 27.0 | RealityKit | Resolved | 177674901 |  |  | `ComputeGraphComponents` in a Reality file didn't render; fixed. |  |  |
| TV-117 | 27.0 | RealityKit | Resolved | 177976245 |  |  | `OpacityComponent` on opaque materials revealed interior surfaces in `RealityRenderer`; fixed. |  |  |
| TV-118 | 27.0 | Security | Resolved | 183456836 |  |  | ACME certificate issuance and Managed Device Attestation enrollments failed; fixed. |  |  |
| TV-119 | 27.0 | ShaderGraph | Resolved | 177976666 |  |  | The `realitykit_hair_surfaceshader` node lacked `DiffuseLightProbeGroupComponent` support; fixed. |  |  |
| TV-120 | 27.0 | Siri | Resolved | 177464215 |  |  | Siri might not resolve entity types that provide only an `EntityStringQuery`; fixed. |  |  |
| TV-121 | 27.0 | StoreKit | New Feature | 156749517 |  |  | Adds `Transaction.OwnershipType.assigned` and `RevocationType.assignmentRevoked` for volume purchases. |  |  |
| TV-122 | 27.0 | StoreKit | New Feature | 160501742 |  |  | `Product.ProductType` APIs for subscription Bundles and Suites, plus `Product.SubscriptionInfo.BundledSubscription`. |  |  |
| TV-123 | 27.0 | StoreKit | New Feature | 167808780 |  |  | `partnerName` and `partnerId` in `Transaction.AdvancedCommerceInfo` and `RenewalInfo.AdvancedCommerceInfo`. |  |  |
| TV-124 | 27.0 | StoreKit | Resolved | 181766819 (FB23646993) |  |  | The `Storefront` API returned wrong metadata in TestFlight; fixed. |  |  |
| TV-125 | 27.0 | StoreKit | Resolved | 181842500 |  |  | Non-subscription purchases via `SKTestSession.buyProduct()` failed, and `billingPlanType(_:)` was ignored; fixed. |  |  |
| TV-126 | 27.0 | StoreKit | Resolved | 183165269 |  |  | "Transactions fail to finish"; fixed. |  |  |
| TV-127 | 27.0 | StoreKit Testing | Resolved | 102093015 (FB11767567) |  |  | The unified receipt wasn't updated after a forced expiration; fixed. |  |  |
| TV-128 | 27.0 | StoreKit Testing | Resolved | 154390284 (FB18403150) |  |  | `disableDialogs` wasn't always respected; fixed. |  |  |
| TV-129 | 27.0 | StoreKit Testing | Resolved | 160698598 (FB20269723) |  |  | Transaction Manager upgrades were missing from `Transaction.updates`; fixed. |  |  |
| TV-130 | 27.0 | StoreKit Testing | Resolved | 162014134 (FB20537538) |  |  | The renewal behavior in `purchaseDate(_:renewalBehavior:)` was ignored; fixed. |  |  |
| TV-131 | 27.0 | StoreKit Testing | Resolved | 174560379 (FB22475017) |  |  | Re-purchasing a refunded non-consumable failed as "already owned"; fixed. |  |  |
| TV-132 | 27.0 | StoreKit Testing | Resolved | 177942756 |  |  | Wrong `pricingTerms.commitmentInfo.price` for a monthly subscription with a 12-month commitment; fixed. |  |  |
| TV-133 | 27.0 | StoreKit Testing | Resolved | 178441109 |  |  | Upgraded subscriptions were immediately marked expired; fixed. |  |  |
| TV-134 | 27.0 | StoreKit Testing | Resolved | 183933307 (FB24137836) |  |  | Intro offer eligibility didn't reset after `clearTransactions()`; fixed. The same entry appears again in the 27.2 notes (TV-163). |  |  |
| TV-135 | 27.0 | StoreKit Testing | Known Issue | 184155259 |  |  | Storefront and locale changes in `SKTestSession` don't propagate through `Storefront.updates`. No workaround given. Fixed in 27.2 (TV-164). |  |  |
| TV-136 | 27.0 | StoreKit Testing | Known Issue | 184255116 |  |  | Failed purchases show error dialogs even when `dialogsDisabled` is true. No workaround given. Fixed in 27.2 (TV-165). |  |  |
| TV-137 | 27.0 | Swift Charts | Resolved | 174168981 | Yes | SDK/deployment condition | with a deployment target below 27.0, conditionals inside a `Chart` produced a `_ConditionalContent` warning and a possible runtime crash; fixed. |  |  |
| TV-138 | 27.0 | SwiftUI | New Feature | 78212597 |  |  | `AsyncImage` HTTP caching, `URLRequest` initializers, and `View.asyncImageURLSession(_:)`. |  |  |
| TV-139 | 27.0 | SwiftUI | New Feature | 105893279 |  |  | A macro-based `@State` (Xcode 27) avoids re-evaluating the initial-value expression. It "back-deploys to iOS 17 aligned OSes". Source breaks: [A declaration initial value combined with init assignment no longer compiles. Workaround: omit the declaration initial value.] [The synthesized private memberwise init is disabled. Workaround: assign members explicitly.] [Generic inference is weaker.] [Composing with other wrappers or macros is unsupported.] |  |  |
| TV-140 | 27.0 | SwiftUI | New Feature | 173211711 |  | A11y/VoiceOver | `TabsPickerStyle` for tab-navigation pickers is "similar to the `.segmented` style, but VoiceOver reads it as 'tabs'". This entry is in tvOS notes but absent from watchOS notes. |  | IOS-01, TV-02, API-02 |
| TV-141 | 27.0 | SwiftUI | New Feature | 173362083 |  |  | `TextInputBorderShape` and `textInputBorderShape(_:)`. `.squareBorder` and `.roundedBorder` are soft-deprecated in favor of `.bordered`. |  |  |
| TV-142 | 27.0 | SwiftUI | New Feature | 175594929 | Yes | SDK-linked | "In apps built with the 27.0 SDKs", `LabeledContent` in a `Menu` maps its value to the menu item subtitle. |  |  |
| TV-143 | 27.0 | SwiftUI | New Feature | 175902616 |  |  | `@Entry` warns about default class instances or closures in the environment. |  |  |
| TV-144 | 27.0 | SwiftUI | New Feature | 177185166 |  |  | `GeometryProxy.concentricCornerRadii` and `concentricCornerRadii(in:)` return `RectangleCornerRadii?`. |  |  |
| TV-145 | 27.0 | SwiftUI | New Feature | 177526032 |  |  | `@ContentBuilder` type-checking performance is improved compared with Beta 1. |  |  |
| TV-146 | 27.0 | SwiftUI | New Feature | 179388848 |  |  | Data-item and error-based `alert` and `confirmationDialog` back-deploy to tvOS 15.0 and watchOS 8.0, among other OSes. |  |  |
| TV-147 | 27.0 | SwiftUI | Resolved | 154080867 |  |  | Using both `.fileExporter` and `.fileMover` broke dialogs; fixed. |  |  |
| TV-148 | 27.0 | SwiftUI | Resolved | 165913417 | Yes | SDK-linked (27.0 SDKs) | `containerRelativeFrame` mis-applied safe-area insets on a ScrollView's non-scrollable axis; fixed. [Relevant to the WWDC26-221 grid technique, which uses `containerRelativeFrame` (see TV-176).] |  |  |
| TV-149 | 27.0 | SwiftUI | Resolved | 167448274 | Yes | SDK-linked | The `controlSize`, `buttonSizing`, `buttonRepeatBehavior`, `menuIndicatorVisibility`, and `ButtonBorderShape` environment values now reset to defaults in sheets and popovers. |  |  |
| TV-150 | 27.0 | SwiftUI | Resolved | 169091260 |  | A11y/interaction | Fixed: "`Menu` labels cannot contain controls, views with gestures, or view representables with gesture recognizers." This entry is tvOS-only (absent from watchOS notes). |  |  |
| TV-151 | 27.0 | SwiftUI | Resolved | 171830912 | Yes | tvOS-specific, SDK-linked, visual/contrast | "Buttons on tvOS no longer automatically use the accent color from an app's asset catalog as a label tint color when building against the tvOS 27 SDK." |  |  |
| TV-152 | 27.0 | SwiftUI | Resolved | 175681345 |  |  | Icon-to-title spacing for a Button in a List Section header or footer; fixed. |  |  |
| TV-153 | 27.0 | SwiftUI | Resolved | 179149051 (FB23015259) |  |  | `@State` with a raw identifier failed to compile; fixed. |  |  |
| TV-154 | 27.0 | System | New Feature | 160612181 |  |  | Swift `stat`, `lstat`, `fstat`, and `fstatat` APIs (`Stat`, `FilePath.stat()`, …), per SYS-0006. |  |  |
| TV-155 | 27.0 | System | Resolved | 177911316 |  |  | Unqualified `stat()` calls in custom extensions conflicted with the new methods (SYS-0008); fixed. |  |  |
| TV-156 | 27.0 | TextKit | New Feature | 159870239 |  |  | `NSTextTable` is available to UIKit clients in OS 27. |  | IOS-06, WATCH-01 |
| TV-157 | 27.0 | UIKit | New Feature | 161843040 | Yes | SDK-linked | "When linked on iOS 27, tvOS 27, …", `UIScene.extendStateRestoration` and `completeStateRestoration` extend restoration across background-to-foreground transitions. |  | IOS-02 |
| TV-158 | 27.0 | UIKit | Deprecation | 141837548 | Yes | SDK-linked, breaking | Apps built with the latest SDK "must adopt the scene-based life cycle or they fail to launch". Migration guide linked. |  |  |
| TV-159 | 27.0 | USDKit | Resolved | 170653056 |  |  | Some USD attribute types couldn't be read or modified; fixed. |  |  |
| TV-160 | 27.0 | USDKit | Resolved | 178071414 |  |  | Array, vector, matrix, and quaternion authoring; fixed. |  |  |
| TV-161 | 27.0 | VideoToolbox | New Feature | 177635243 |  |  | `VTLowLatencySuperResolutionScalerConfiguration` supports a 1.5x scale factor (`+supportedScaleFactorsForFrameWidth:frameHeight:`). |  |  |
| TV-162 | 27.0 | VideoToolbox | New Feature | 179040806 |  |  | `VTLowLatencyFrameInterpolationConfiguration` accepts arbitrary source dimensions up to 1080p. |  |  |

## Stable: 27.2 (4 entries)

| Claim ID | Release | Section | Status | Issue (FB) | SDK-linked | A11y / interaction flag | Entry (notes' paraphrase and quotes) | Transfer note | Pass-2 ID |
|---|---|---|---|---|---|---|---|---|---|
| TV-163 | 27.2 | StoreKit Testing | Resolved | 183933307 (FB24137836) |  |  | Intro offer eligibility reset; listed again after its 27.0 appearance. |  |  |
| TV-164 | 27.2 | StoreKit Testing | Resolved | 184155259 |  |  | Storefront and locale propagation; fixed. This was a 27.0 KI. |  |  |
| TV-165 | 27.2 | StoreKit Testing | Resolved | 184255116 |  |  | Error dialogs despite `dialogsDisabled`; fixed. This was a 27.0 KI. |  |  |
| TV-166 | 27.2 | StoreKit Testing | Known Issue | 186018916 |  |  | An in-app purchase of a bundle-member subscription "incorrectly allows the user to unbundle instead of throwing an error". No workaround given. |  |  |

## Beta (not shipped): 27.3 beta (2 entries)

These rows are beta-only. Do not treat them as shipped behavior.

| Claim ID | Release | Section | Status | Issue (FB) | SDK-linked | A11y / interaction flag | Entry (notes' paraphrase and quotes) | Transfer note | Pass-2 ID |
|---|---|---|---|---|---|---|---|---|---|
| TV-167 | 27.3 beta | StoreKit Testing | Resolved | 186018916 |  |  | The bundle-unbundle issue from 27.2 is fixed. |  |  |
| TV-168 | 27.3 beta | StoreKit Testing | Known Issue | 186670057 (FB24651858) |  |  | On first launch of an app using `SKTestSession`, some StoreKit Test API calls might hang. [**Workaround:** "Set a StoreKit configuration file in your scheme's run options, then rerun the tests."] |  |  |

Totals: 68 entries (27.0: 62; 27.2: 4; 27.3 beta: 2). Expected from the notes: 62 + 4 + 2 = 68.
