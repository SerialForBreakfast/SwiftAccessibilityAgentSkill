# watchOS 27 release-note inventory

Research only. Mechanically transferred from the pass-3 research notes on 2026-11-05 (script `build_inventory.py`, not retyped). Every row is **Tier-1**, evidence type **release note**. Apple text is truncated in the notes (22 words or fewer). Symbol availability for any API named here is pending unless [api-availability.md](../api-availability.md) records DocC metadata. The `Pass-2 ID` column cross-references earlier claim IDs by Apple issue number.

Sources: [27.0](https://developer.apple.com/documentation/watchos-release-notes/watchos-27-release-notes) (18,698 bytes), [27.2](https://developer.apple.com/documentation/watchos-release-notes/watchos-27_2-release-notes) (1,544 bytes), [27.3 beta](https://developer.apple.com/documentation/watchos-release-notes/watchos-27_3-release-notes) (1,412 bytes). No watchOS 27.1 exists.

The notes recorded these entries as bullets, not a table; this file converts them mechanically. Status codes: NF New Feature, RI Resolved Issue, KI Known Issue, DEP Deprecation. Where the notes grouped several entries under one ID range, the rows are expanded in listing order and marked.

## Stable: 27.0 (67 entries)

| Claim ID | Release | Section | Status | Issue (FB) | SDK-linked | A11y / interaction flag | Entry (notes' paraphrase and quotes) | Transfer note | Pass-2 ID |
|---|---|---|---|---|---|---|---|---|---|
| WATCH-101 | 27.0 | App Intents | Resolved | 181763422 |  |  | AppEntity instances have a cumulative 10MB limit including child properties; the app might crash past it, and the exception is logged. |  |  |
| WATCH-102 | 27.0 | App Intents | Resolved | 182532125 |  |  | The `notes.appendText` schema disappeared from the SDK; fixed. |  |  |
| WATCH-103 | 27.0 | AV Conference Telephony | Resolved | 178187431 |  |  | Outgoing FaceTime Audio from family-setup watches to iOS 27 beta devices might fail; fixed. |  |  |
| WATCH-104 | 27.0 | Cellular | Resolved | 180062521 |  |  | Verizon calls and Text-to-911 might fail after updating to or clean-installing watchOS 27.0 beta 2; fixed. |  |  |
| WATCH-105 | 27.0 | Communication Safety | Resolved | 183962032 |  |  | A sensitive QR code was detected as non-sensitive; fixed. |  |  |
| WATCH-106 | 27.0 | Complications | Resolved | 177840928 |  | A11y-adjacent/complications | "Some complications might be missing in the Watch app's Face Gallery"; fixed. |  |  |
| WATCH-107 | 27.0 | Foundation | Resolved | 161588649 (FB20439045) |  |  | NSURL percent-escape double-encoding; fixed. |  |  |
| WATCH-108 | 27.0 | Foundation Models | Resolved | 177684296 |  |  | Private Cloud Compute didn't work in simulators; fixed. |  |  |
| WATCH-109 | 27.0 | Foundation Models | Resolved | 177901494 |  |  | Truncating transcript history in `onPrompt` caused a runtime error; fixed. |  |  |
| WATCH-110 | 27.0 | Foundation Models | Resolved | 177902488 |  |  | `onPrompt` wasn't called on a `Profile` without instructions; fixed. |  |  |
| WATCH-111 | 27.0 | Foundation Models | Resolved | 178181782 |  |  | `PrivateCloudComputeLanguageModel` always used greedy decoding; fixed. |  |  |
| WATCH-112 | 27.0 | Foundation Models | Resolved | 178244470 |  |  | `@Generable` on an enum failed to compile for watchOS; fixed. |  |  |
| WATCH-113 | 27.0 | Foundation Models | Resolved | 179949809 |  |  | The framework couldn't be imported for watchOS in Xcode 27 beta 2; fixed. |  |  |
| WATCH-114 | 27.0 | Hardware Security | New Feature | 152103975 |  | hardware-gated | arm64e.x1 and CPA2 (stronger MIE protection). Supported on "Apple Watch models with S11 or later chips", plus A20 Pro iPhone and M6 Mac. Enabled via the Xcode enhanced security pane and a build setting. |  |  |
| WATCH-115 | 27.0 | Health | listed under RI, but phrased as behavior, not "Fixed" | 162788761 |  | A11y-adjacent/notifications | While a third-party heart rate monitor is active, the watch "pauses background heart rate measurements and heart rate notifications" (irregular rhythm, high, low). |  |  |
| WATCH-116 | 27.0 | HealthKit | New Feature | 135746152 |  |  | Heart rate and cycling power zones. |  |  |
| WATCH-117 | 27.0 | HealthKit | Resolved | 171273931 (FB22066297) |  |  | A null unit converted incorrectly to count and percent; fixed. |  |  |
| WATCH-118 | 27.0 | Network Security | New Feature | 176055825 |  |  | The same stricter TLS for system processes as TV-111. |  |  |
| WATCH-119 | 27.0 | Security | Resolved | 183456836 |  |  | ACME and MDA failures; fixed. |  |  |
| WATCH-120 | 27.0 | Siri | Resolved | 177464215 |  |  | `EntityStringQuery`-only entity resolution; fixed. |  |  |
| WATCH-121 | 27.0 | Siri | Resolved | 180303086 |  |  | Siri AI couldn't complete some actions for English users outside the US; fixed. |  |  |
| WATCH-122 | 27.0 | Siri | RI, phrased as a status statement | 182145010 |  |  | "As of beta 5, Siri AI conversation history no longer syncs to devices running a prior beta." No conversations are lost. |  |  |
| WATCH-123 | 27.0 | Siri | Known Issue | 180434572 |  |  | Siri may appear to be listening when it is not, after long silence with the UI on screen. No workaround. |  |  |
| WATCH-124 | 27.0 | Siri | Known Issue | 183040889 |  |  | Siri AI conversations might not sync to the watch ("No iCloud is configured"). [**Workaround:** on the watch, Settings > Apple Account triggers a refresh.] |  |  |
| WATCH-125 | 27.0 | Siri | Known Issue | 183958361 |  |  | Watches updated from an earlier beta might not sync Siri history; they usually self-recover. [**Workaround:** Settings > Apple Account on the watch.] |  |  |
| WATCH-126 | 27.0 | Sleep Focus | Resolved | 179960164 |  |  | Sleep Focus didn't auto-toggle after reboot or update until unlock; fixed. |  |  |
| WATCH-127 | 27.0 | Smart Stack | Resolved | 178464737 |  | A11y-adjacent/widgets | Tapping the Now Playing "Suggestions" widget didn't start playback; fixed. |  |  |
| WATCH-128 | 27.0 | Status Bar | Resolved | 178633015 |  |  | In Always On, the status-bar time may not update; fixed. |  |  |
| WATCH-129 | 27.0 | StoreKit | New Feature | 156749517 |  |  | Adds `Transaction.OwnershipType.assigned` and `RevocationType.assignmentRevoked` for volume purchases. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-129–131; ID assigned by listing order |  |
| WATCH-130 | 27.0 | StoreKit | New Feature | 160501742 |  |  | `Product.ProductType` APIs for subscription Bundles and Suites, plus `Product.SubscriptionInfo.BundledSubscription`. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-129–131; ID assigned by listing order |  |
| WATCH-131 | 27.0 | StoreKit | New Feature | 167808780 |  |  | Notes label: Same as TV-121–123.. `partnerName` and `partnerId` in `Transaction.AdvancedCommerceInfo` and `RenewalInfo.AdvancedCommerceInfo`. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-129–131; ID assigned by listing order |  |
| WATCH-132 | 27.0 | StoreKit | Resolved | 181766819 (FB23646993) |  |  | The `Storefront` API returned wrong metadata in TestFlight; fixed. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-132–134; ID assigned by listing order |  |
| WATCH-133 | 27.0 | StoreKit | Resolved | 181842500 |  |  | Non-subscription purchases via `SKTestSession.buyProduct()` failed, and `billingPlanType(_:)` was ignored; fixed. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-132–134; ID assigned by listing order |  |
| WATCH-134 | 27.0 | StoreKit | Resolved | 183165269 |  |  | Notes label: Same as TV-124–126.. "Transactions fail to finish"; fixed. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-132–134; ID assigned by listing order |  |
| WATCH-135 | 27.0 | StoreKit Testing | Resolved | 102093015 |  |  | The unified receipt wasn't updated after a forced expiration; fixed. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-135–143; ID assigned by listing order |  |
| WATCH-136 | 27.0 | StoreKit Testing | Resolved | 154390284 |  |  | `disableDialogs` wasn't always respected; fixed. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-135–143; ID assigned by listing order |  |
| WATCH-137 | 27.0 | StoreKit Testing | Resolved | 160698598 |  |  | Transaction Manager upgrades were missing from `Transaction.updates`; fixed. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-135–143; ID assigned by listing order |  |
| WATCH-138 | 27.0 | StoreKit Testing | Resolved | 162014134 |  |  | The renewal behavior in `purchaseDate(_:renewalBehavior:)` was ignored; fixed. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-135–143; ID assigned by listing order |  |
| WATCH-139 | 27.0 | StoreKit Testing | Resolved | 174560379 |  |  | Re-purchasing a refunded non-consumable failed as "already owned"; fixed. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-135–143; ID assigned by listing order |  |
| WATCH-140 | 27.0 | StoreKit Testing | Resolved | 177942756 |  |  | Wrong `pricingTerms.commitmentInfo.price` for a monthly subscription with a 12-month commitment; fixed. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-135–143; ID assigned by listing order |  |
| WATCH-141 | 27.0 | StoreKit Testing | Resolved | 178441109 |  |  | Upgraded subscriptions were immediately marked expired; fixed. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-135–143; ID assigned by listing order |  |
| WATCH-142 | 27.0 | StoreKit Testing | Resolved | 183933307 |  |  | Intro offer eligibility didn't reset after `clearTransactions()`; fixed. The same entry appears again in the 27.2 notes (TV-163). *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-135–143; ID assigned by listing order |  |
| WATCH-143 | 27.0 | StoreKit Testing | Resolved | 178760994 |  |  | "Purchases made with the original StoreKit API fail with an unknown error on watchOS" | grouped in notes as WATCH-135–143; ID assigned by listing order |  |
| WATCH-144 | 27.0 | StoreKit Testing | Known Issue | 184155259 |  |  | Storefront and locale changes in `SKTestSession` don't propagate through `Storefront.updates`. No workaround given. Fixed in 27.2 (TV-164). *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-144–145; ID assigned by listing order |  |
| WATCH-145 | 27.0 | StoreKit Testing | Known Issue | 184255116 |  |  | Notes label: Same as TV-135–136. Failed purchases show error dialogs even when `dialogsDisabled` is true. No workaround given. Fixed in 27.2 (TV-165). *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-144–145; ID assigned by listing order |  |
| WATCH-146 | 27.0 | Swift Charts | Resolved | 174168981 |  |  | Same as TV-137. |  |  |
| WATCH-147 | 27.0 | SwiftUI | New Feature | 78212597 |  |  | Notes label: AsyncImage. `AsyncImage` HTTP caching, `URLRequest` initializers, and `View.asyncImageURLSession(_:)`. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-147–154; ID assigned by listing order |  |
| WATCH-148 | 27.0 | SwiftUI | New Feature | 105893279 |  |  | Notes label: `@State` macro. A macro-based `@State` (Xcode 27) avoids re-evaluating the initial-value expression. It "back-deploys to iOS 17 aligned OSes". Source breaks: [A declaration initial value combined with init assignment no longer compiles. Workaround: omit the declaration initial value.] [The synthesized private memberwise init is disabled. Workaround: assign members explicitly.] [Generic inference is weaker.] [Composing with other wrappers or macros is unsupported.] *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-147–154; ID assigned by listing order |  |
| WATCH-149 | 27.0 | SwiftUI | New Feature | 173362083 |  |  | Notes label: TextInputBorderShape. `TextInputBorderShape` and `textInputBorderShape(_:)`. `.squareBorder` and `.roundedBorder` are soft-deprecated in favor of `.bordered`. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-147–154; ID assigned by listing order |  |
| WATCH-150 | 27.0 | SwiftUI | New Feature | 175594929 | Yes |  | Notes label: LabeledContent in Menu. "In apps built with the 27.0 SDKs", `LabeledContent` in a `Menu` maps its value to the menu item subtitle. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-147–154; ID assigned by listing order |  |
| WATCH-151 | 27.0 | SwiftUI | New Feature | 175902616 |  |  | Notes label: @Entry warnings. `@Entry` warns about default class instances or closures in the environment. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-147–154; ID assigned by listing order |  |
| WATCH-152 | 27.0 | SwiftUI | New Feature | 177185166 |  |  | Notes label: concentricCornerRadii. `GeometryProxy.concentricCornerRadii` and `concentricCornerRadii(in:)` return `RectangleCornerRadii?`. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-147–154; ID assigned by listing order |  |
| WATCH-153 | 27.0 | SwiftUI | New Feature | 177526032 |  |  | Notes label: @ContentBuilder performance. `@ContentBuilder` type-checking performance is improved compared with Beta 1. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-147–154; ID assigned by listing order |  |
| WATCH-154 | 27.0 | SwiftUI | New Feature | 179388848 |  |  | Notes label: alert/confirmationDialog back-deploy to watchOS 8.0. Data-item and error-based `alert` and `confirmationDialog` back-deploy to tvOS 15.0 and watchOS 8.0, among other OSes. *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-147–154; ID assigned by listing order |  |
| WATCH-155 | 27.0 | SwiftUI | Resolved | 154080867 |  |  | fileExporter plus fileMover; fixed. |  |  |
| WATCH-156 | 27.0 | SwiftUI | Resolved | 163517317 | Yes | A11y/Digital Crown, SDK-linked, watchOS-only | Fixed: "In apps built with the watchOS 27.0 SDK, `TabView.selection` updates only after the user has scrolled or rotated the Digital Crown past the 50% threshold…" Selection now updates as soon as the offset begins to change. |  |  |
| WATCH-157 | 27.0 | SwiftUI | Resolved | 165913417 |  |  | containerRelativeFrame safe-area insets; fixed. |  |  |
| WATCH-158 | 27.0 | SwiftUI | Resolved | 167448274 |  |  | Control environment values reset in sheets and popovers. |  |  |
| WATCH-159 | 27.0 | SwiftUI | Resolved | 175681345 |  |  | List section header button spacing; fixed. |  |  |
| WATCH-160 | 27.0 | SwiftUI | Resolved | 179149051 (FB23015259) |  |  | Raw-identifier `@State`; fixed. |  |  |
| WATCH-161 | 27.0 | System | New Feature | 160612181 |  |  | Swift stat APIs. |  |  |
| WATCH-162 | 27.0 | System | Resolved | 177911316 |  |  | stat() name conflicts; fixed. |  |  |
| WATCH-163 | 27.0 | TextKit | New Feature | 159870239 |  |  | `NSTextTable` available to "UIKit clients". This text is copied verbatim into the watchOS notes even though watchOS apps don't use UIKit directly (see Inferences). |  | IOS-06, WATCH-01 |
| WATCH-164 | 27.0 | Watch Connectivity | Resolved | 113202790 (FB12819178) |  | complications | `WCSession.transferCurrentComplicationUserInfo` didn't work with WidgetKit complications; fixed. |  |  |
| WATCH-165 | 27.0 | WatchKit | Deprecation | 70031637 |  |  | `WKExtension` and `WKExtensionDelegate` are deprecated for a minimum deployment target of watchOS 9.2 or later. |  |  |
| WATCH-166 | 27.0 | Workout | Resolved | 176497682 |  |  | Mirrored Playback on iPhone didn't start; fixed. |  |  |
| WATCH-167 | 27.0 | Workout | Resolved | 181296052 |  | audio feedback | In standalone mode with Siri AI on iPhone, Workout Alerts and Workout Buddy might fail to deliver audio announcements; fixed. |  |  |

## Stable: 27.2 (4 entries)

| Claim ID | Release | Section | Status | Issue (FB) | SDK-linked | A11y / interaction flag | Entry (notes' paraphrase and quotes) | Transfer note | Pass-2 ID |
|---|---|---|---|---|---|---|---|---|---|
| WATCH-168 | 27.2 | StoreKit Testing | Resolved | 183933307 (FB24137836) |  |  | Intro offer eligibility didn't reset after `clearTransactions()`; fixed. The same entry appears again in the 27.2 notes (TV-163). *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-168–170; ID assigned by listing order |  |
| WATCH-169 | 27.2 | StoreKit Testing | Resolved | 184155259 |  |  | Storefront and locale changes in `SKTestSession` don't propagate through `Storefront.updates`. No workaround given. Fixed in 27.2 (TV-164). *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-168–170; ID assigned by listing order |  |
| WATCH-170 | 27.2 | StoreKit Testing | Resolved | 184255116 |  |  | Notes label: Identical to TV-163–165.. Failed purchases show error dialogs even when `dialogsDisabled` is true. No workaround given. Fixed in 27.2 (TV-165). *(text taken from the matching single entry with the same issue number)* | grouped in notes as WATCH-168–170; ID assigned by listing order |  |
| WATCH-171 | 27.2 | StoreKit Testing | Known Issue | 186018916 |  |  | Bundle-member subscription unbundling. No workaround. |  |  |

## Beta (not shipped): 27.3 beta (2 entries)

These rows are beta-only. Do not treat them as shipped behavior.

| Claim ID | Release | Section | Status | Issue (FB) | SDK-linked | A11y / interaction flag | Entry (notes' paraphrase and quotes) | Transfer note | Pass-2 ID |
|---|---|---|---|---|---|---|---|---|---|
| WATCH-172 | 27.3 beta | StoreKit Testing | Resolved | 186018916 |  |  | Fixed. |  |  |
| WATCH-173 | 27.3 beta | StoreKit Testing | Known Issue | 186670057 (FB24651858) |  |  | First-launch `SKTestSession` hang. [**Workaround:** set a StoreKit configuration file in the scheme's run options.] |  |  |

Totals: 73 entries (27.0: 67; 27.2: 4; 27.3 beta: 2). Expected from the notes: 67 + 4 + 2 = 73.
