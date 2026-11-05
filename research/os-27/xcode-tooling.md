# Xcode 27 accessibility tooling

Third pass, 2026-11-05. Research only. This is a tooling track: it records what Apple's
Xcode notes and sessions say, not a claim that any assistant discovers or uses this corpus.
Releases: Xcode 27 (27A266a, 14 Sep 2026; Swift 6.4, 27 SDKs, macOS Tahoe 26.6 or later),
27.1 (27A9275, 15 Oct), 27.2 (27B52, 29 Oct), **27.3 beta** (27C5020n, 3 Nov). The extracted
entries are in [inventory/xcode.md](inventory/xcode.md); that inventory is not a full Xcode
inventory. [X0] = [Xcode 27 RN](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes).
Column key as on [ios.md](ios.md).

## Automated accessibility testing

| ID | Change | Release / status | Tier | Source and locator | Cross-ref |
| --- | --- | --- | --- | --- | --- |
| XCODE-101 | "XCTest now includes XCUIVoiceOverService, a new UI testing API for verifying VoiceOver behavior in your app"; drives VoiceOver and validates focus, speech and navigation. | 27.0 New Feature | Tier-1, release note | [X0] § Testing, 175858549 | API-122 |
| XCODE-102 | DocC: `XCUIVoiceOverService` lives in XCUIAutomation, 27.0 on all seven platforms; members `enable()`, `disable()`, `isEnabled`, `moveForward()`, `moveBackward()`, `moveIn()`, `moveOut()`, `currentSpeech()`. Empty abstract; the XCTest path returns 404. | 27.0 | Tier-1, API declaration | [XCUIVoiceOverService](https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice) | C-16 |
| XCODE-103 | `performAccessibilityAudit(for:_:)` documented under XCUIAutomation (iOS 17.0, macOS 14.0, watchOS 10.0, tvOS 17.0); no 27.x note mentions audit changes. | unchanged | Tier-1, API declaration | [performAccessibilityAudit](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/performaccessibilityaudit(for:_:)) | API-147 |
| XCODE-104 | Launch-test template running across orientation, localization and appearance (168770106); UI-test crash severity levels (168107814). | 27.0 New Feature | Tier-1, release note | [X0] § Testing | |
| XCODE-120a | UI tests can be written with Swift Testing and `XCUIAutomation` (95593221); `XCUIHinge` for iPhone Duo (187479559). | **27.3 beta** | Tier-1, release note | [Xcode 27.3 beta RN](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_3-release-notes) | |
| WWDC-132 | Lab: "there is a new XC test API so that from a Mac you can test voiceover on your iOS device". | 27.0 | Tier-1, transcript (group lab, informal) | [WWDC26-8005](https://developer.apple.com/videos/play/wwdc2026/8005/) 22:26–22:29 | XCODE-127 |

## Accessibility Inspector, Simulator and Device Hub

| ID | Change | Release / status | Tier | Source and locator |
| --- | --- | --- | --- | --- |
| XCODE-105 | "Fixed: Accessibility Inspector cannot inspect elements in simulators." Simulator runtimes ship a pre-built dyld cache; `simctl`/`devicectl` reboot. | 27.0 Resolved | Tier-1, release note | [X0] § Simulator, 179033881 |
| XCODE-106 | Device Hub fixes: VoiceOver toggle enables VoiceOver on the device (173507341); Text Size no longer disappears at accessibility sizes (175365925); Color Filter works for simulators (178854926); Simulate Hardware Keyboard (178196115). | 27.0 Resolved | Tier-1, release note | [X0] § Device Hub |
| XCODE-107 | Device Hub known issues: physical-device color filter not visible (178121876); Toggle Software Keyboard fails on iOS 27.0 iPad sims (178432770); no keyboard/mouse for pre-iOS 18-era sims (181945323); no two-finger touch. Deprecation: keyboard and pointer input only on macOS 15, iOS 18, tvOS 18, watchOS 11, visionOS 2 or later (160482487). | 27.0 Known Issue / Deprecation | Tier-1, release note | [X0] § Device Hub |
| XCODE-108 | Mac mouse and trackpad gestures drive standard UIKit components (scroll and transform events); network pairing for iOS/iPadOS/watchOS 27. | 27.0 New Feature | Tier-1, release note | [X0] § Device Hub |
| XCODE-119 | VoiceOver, Accessibility Inspector and other tools "cannot convey screen content on an iPhone Duo within Device Hub" (187148389); no text-size customization for iOS 18-or-earlier devices (189261485). | 27.2 Known Issue | Tier-1, release note | [Xcode 27.2 RN](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) § Device Hub |
| XCODE-119a | Sidecar multi-finger forwarding (188634387); slow-motion, shake, fall and memory-pressure simulation; earlier input issues (181945323, 182553164) fixed. | 27.2 | Tier-1, release note | Xcode 27.2 RN § Device Hub |
| XCODE-120b | Option-drag simulates two-finger touch (169537162); input for older sims (190652440); Sidecar limited to two touches (185140491, known). | **27.3 beta** | Tier-1, release note | Xcode 27.3 beta RN § Device Hub |
| XCODE-121 / XCODE-122 | Sessions show testing with increased contrast and larger Dynamic Type (258, 10:36–10:43) and reproducing a user's large-text bug in Device Hub (260, 13:53–15:06). | 27.0 | Tier-1, transcript | [258](https://developer.apple.com/videos/play/wwdc2026/258/); [260](https://developer.apple.com/videos/play/wwdc2026/260/) |

## Previews

| ID | Change | Release / status | Tier | Source and locator |
| --- | --- | --- | --- | --- |
| XCODE-109 | Overrides picker adds Color Scheme Contrast (181612731) and Control Borders (181850835); `#Preview(arguments:)` grids, Resizable Canvas, localization previews; `PreviewProvider` deprecated (144168701). | 27.0 | Tier-1, release note | [X0] § Previews |
| XCODE-110 | Keyboard input delivered to iOS-Simulator previews (177679215); `#Preview` runs on the main actor. | 27.0 Resolved | Tier-1, release note | [X0] § Previews |
| XCODE-118 | Overrides picker adds a Display group (182598534); iOS 27.1 APIs fail for Catalyst (185924957); no Catalyst destination for 27.1 targets (187046347). | 27.1 | Tier-1, release note | [Xcode 27.1 RN](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) |
| XCODE-120c | RenderPreview filenames and metadata include overrides (176531615); GitHub Copilot added. No accessibility-specific entries. | **27.3 beta** | Tier-1, release note | Xcode 27.3 beta RN |

## Coding assistant and agents

| ID | Change | Release / status | Tier | Source and locator |
| --- | --- | --- | --- | --- |
| XCODE-111 | "Xcode now ships with Apple-built specialists for targeted tasks, like localization, UIKit resizing and accessibility." | 27.0 New Feature | Tier-1, release note | [X0] § Coding Intelligence, 178289150 |
| XCODE-112 | Preview Snapshot MCP tool renders variants including "various type size overrides" (172961797); agents boot simulators, synthesize touches, screenshot (175179787). | 27.0 | Tier-1, release note | [X0] § Coding Intelligence |
| XCODE-113 | Agents verify tvOS apps by moving Siri Remote focus (183317784) and watchOS apps through the Digital Crown and buttons (181147968). | 27.0 | Tier-1, release note | [X0] § Coding Intelligence |
| XCODE-114 | Xcode's own prompt-area buttons get more accessible labels (177462284); VoiceOver no longer trapped in the prompt area (177462397). | 27.0 Resolved | Tier-1, release note | [X0] § Coding Intelligence |
| XCODE-115 | Plugins with skills, MCP servers, ACP agents; filesystem-access security layer; additional providers; `xcrun mcp-server` preview. | 27.0 | Tier-1, release note | [X0] § Coding Intelligence |
| XCODE-119c | RenderPreview MCP tool returns and accepts render destinations (186442676); `.rotateDigitalCrown` fixed (188422137). | 27.2 | Tier-1, release note | Xcode 27.2 RN |
| XCODE-120 | The only "audit" in Xcode 27.x notes is the `audit-xcode-security-settings` skill (181104536), not an accessibility audit. | 27.0 | Tier-1, release note | [X0] § Security |
| XCODE-123 / XCODE-124 | SOTU: an "accessibility specialist that knows what makes an interface work for everyone" (~56:21). Demo: an agent adds VoiceOver labels and identifiers (19:56–20:00), then VoiceOver verification (21:13–21:32). | 27.0 | Tier-1, transcript | [102](https://developer.apple.com/videos/play/wwdc2026/102/); [259](https://developer.apple.com/videos/play/wwdc2026/259/) |

## SDK and availability diagnostics

| ID | Change | Release / status | Tier | Source and locator |
| --- | --- | --- | --- | --- |
| XCODE-116 | Swift Compiler section has no availability-checking items (dependency-scanner change 136303612; SE-0508 known issue 180969028). | 27.0 | Tier-1, release note | [X0] § Swift Compiler |
| XCODE-117 | Strings in availability-constrained `#Preview` macros excluded from String Catalogs (176188980). | 27.0 Resolved | Tier-1, release note | [X0] § Localization |
| XCODE-119b | macOS, watchOS, tvOS and visionOS 27.2 SDKs "incorrectly report 27.1 as a valid deployment target"; Catalyst 27.1/27.2 targets may not use new API (187160501); 185924957 persists. | 27.2 Known Issue | Tier-1, release note | Xcode 27.2 RN § SDK, § Mac Catalyst |

## Community evidence

COMM-125 (Tier-3): Accessibility Inspector Element Detection fails only while a SwiftUI
sheet is presented, Xcode 27.1 with an iPadOS 27.0 simulator. See
[community.md](community.md).

## Gaps

No 27.x note on Swift 6.4 `@available`/`#available` diagnostics (Swift.org not checked); no
new Accessibility Inspector features beyond XCODE-105 and XCODE-119; no WWDC26 session names
`XCUIVoiceOverService` or `performAccessibilityAudit`; the `Output` structure of
`XCUIVoiceOverService` is unverified.

## Research inference (not Apple-stated)

- Xcode 27 adds a second automated path: `performAccessibilityAudit` (static checks since
  iOS 17) and `XCUIVoiceOverService` (drives the screen reader). With 27.3 beta both can be
  written in Swift Testing.
- Device Hub is now the surface for toggling VoiceOver, Text Size and Color Filters on
  simulators and devices.
- XCODE-118 and XCODE-119b are the availability issues most likely to affect teams targeting
  27.1 or 27.2. Pass-2 cross-platform toolchain notes on 27.3 remain valid.

[X0]: https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes
