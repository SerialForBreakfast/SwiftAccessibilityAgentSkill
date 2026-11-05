# Xcode 27 release-note inventory

Research only. Mechanically transferred from the pass-3 research notes on 2026-11-05 (script `build_inventory.py`, not retyped). Every row is **Tier-1**, evidence type **release note**. Apple text is truncated in the notes (22 words or fewer). Symbol availability for any API named here is pending unless [api-availability.md](../api-availability.md) records DocC metadata. The `Pass-2 ID` column cross-references earlier claim IDs by Apple issue number.

Sources: [Xcode 27](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) (67,593 bytes), [27.1](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) (2,210 bytes), [27.2](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) (7,778 bytes), [27.3 beta](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_3-release-notes) (3,878 bytes). Full hashes: [sources.md](../sources.md).

**Scope warning.** The notes extracted accessibility tooling, testing, previews, Simulator, Device Hub, coding-assistant and availability entries, not every Xcode entry. A complete Xcode inventory is in the [backlog](../backlog.md). XCODE-102 and XCODE-103 are DocC API-reference records, not release-note entries; they are kept here because the notes number them in the same sequence. WWDC claims XCODE-121 to XCODE-127 are in [wwdc.md](../wwdc.md) and [xcode-tooling.md](../xcode-tooling.md).

## Stable: Xcode 27.0

| Claim ID | Release | Notes heading | Radar(s) | Entry (notes' paraphrase) | Locator | Evidence type |
|---|---|---|---|---|---|---|
| XCODE-101 | 27.0 | Xcode 27.0 | 175858549 | Testing: "XCTest now includes XCUIVoiceOverService, a new UI testing API for verifying VoiceOver behavior in your app." It drives VoiceOver and validates focus, spoken output and navigation (175858549) | § Testing/New Features, .md L1090. | release note |
| XCODE-102 | 27.0 | Xcode 27.0 | — | API reference: `XCUIVoiceOverService` lives in the XCUIAutomation framework, available iOS/iPadOS/Mac Catalyst/macOS/tvOS/visionOS/watchOS 27.0. Members include `enable()`, `disable()`, `isEnabled`, `moveForward()`, `moveBackward()`, `moveIn()`, `moveOut()`, `currentSpeech()`, plus `Output` and `Error` types. Source: [XCUIVoiceOverService doc](https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice) (JSON: https://developer.apple.com/tutorials/data/documentation/xcuiautomation/xcuivoiceoverservice.json, `metadata.platforms`, `topicSections`). The equivalent `/documentation/xctest/xcuivoiceoverservice` path returned 404. |  | API declaration (DocC) |
| XCODE-103 | 27.0 | Xcode 27.0 | — | `performAccessibilityAudit(for:_:)` is now documented under XCUIAutomation (iOS 17.0, macOS 14.0, watchOS 10.0, tvOS 17.0). No Xcode 27.x release note mentions audit changes. Sources: [performAccessibilityAudit doc](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/performaccessibilityaudit(for:_:)) (JSON `metadata.platforms`); keyword search "audit" across all four Xcode 27.x notes finds only the security skill (XCODE-120). |  | API declaration (DocC) |
| XCODE-104 (part 1) | 27.0 | Xcode 27.0 | 168770106 | Testing: a launch-test file template that opts into `runsForEachTargetApplicationUIConfiguration` runs across orientation, localization and appearance combinations (168770106) | § Testing/New Features, .md L1076–1089. | release note |
| XCODE-104 (part 2) | 27.0 | Xcode 27.0 | 168107814 | Test Plans gain UI-test crash severity levels (168107814) | § Testing/New Features, .md L1076–1089. | release note |
| XCODE-104 (part 3) | 27.0 | Xcode 27.0 | 170335449 | XCTest/Swift Testing cross-framework assertion warnings (170335449) | § Testing/New Features, .md L1076–1089. | release note |
| XCODE-105 | 27.0 | Xcode 27.0 | 179033881 | Simulator: "Fixed: Accessibility Inspector cannot inspect elements in simulators." (179033881) (FB22976268) | § Simulator/Resolved Issues, .md L899. Simulator runtimes now ship a pre-built dyld cache. `simctl` and `devicectl` gain a reboot command (§ Simulator/New Features, .md L884–886). | release note |
| XCODE-106 (part 1) | 27.0 | Xcode 27.0 | 173507341 | Device Hub resolved issues: the VoiceOver toggle in the appearance settings inspector now enables VoiceOver on the device (173507341) | § Device Hub/Resolved Issues, .md L315–329. | release note |
| XCODE-106 (part 2) | 27.0 | Xcode 27.0 | 175365925 | "Text Size" no longer disappears when an Accessibility larger text size is in use (175365925) | § Device Hub/Resolved Issues, .md L315–329. | release note |
| XCODE-106 (part 3) | 27.0 | Xcode 27.0 | 178854926 | The Color Filter option now works for simulators (178854926) | § Device Hub/Resolved Issues, .md L315–329. | release note |
| XCODE-106 (part 4) | 27.0 | Xcode 27.0 | 178196115 | Simulate Hardware Keyboard is fixed (178196115) | § Device Hub/Resolved Issues, .md L315–329. | release note |
| XCODE-107 (part 1) | 27.0 | Xcode 27.0 | 178121876 | Device Hub known issues (27.0): a color filter set on a physical device is not visible in Device Hub (178121876) |  | release note |
| XCODE-107 (part 2) | 27.0 | Xcode 27.0 | 178432770 | Toggle Software Keyboard doesn't work on iOS 27.0 iPad sims (178432770) |  | release note |
| XCODE-107 (part 3) | 27.0 | Xcode 27.0 | 181945323 | Keyboard and mouse input isn't accepted for pre-iOS 18, tvOS 18, watchOS 11 and visionOS 2 sims (181945323) |  | release note |
| XCODE-107 (part 4) | 27.0 | Xcode 27.0 | 160482487 | Two-finger touch isn't supported. Parallel-testing simulators may not be visible. § Device Hub/Known Issues, .md L369–416. Deprecation: keyboard and pointer input only on macOS 15, iOS 18, tvOS 18, watchOS 11 and visionOS 2 or later (160482487), .md L420. |  | release note |
| XCODE-108 | 27.0 | Xcode 27.0 | — | Device Hub new features: Mac mouse and trackpad gestures now drive standard UIKit components, emitting `UIEvent.EventType.scroll`/`.transform` (§ Device Hub/New Features, .md L300). Network pairing for iOS/iPadOS/watchOS 27 devices (.md L302–306). |  | release note |
| XCODE-109 (part 1) | 27.0 | Xcode 27.0 | 181612731, 181850835 | Previews: the canvas overrides picker adds a **Color Scheme Contrast** group (standard or increased contrast) (181612731) and a **Control Borders** group (shown or hidden) (181850835) |  | release note |
| XCODE-109 (part 2) | 27.0 | Xcode 27.0 | 167544057, 171013421, 181040291 | Also new: `#Preview(arguments:)` grids (167544057), a Resizable Canvas (171013421) and localization previews (181040291) |  | release note |
| XCODE-109 (part 3) | 27.0 | Xcode 27.0 | 144168701 | § Previews/New Features, .md L759–776. `PreviewProvider` and its modifiers are deprecated (144168701), .md L819. |  | release note |
| XCODE-110 | 27.0 | Xcode 27.0 | 177679215 | Previews fix: keyboard input is now delivered to iOS-Simulator previews (177679215). `#Preview` code now runs on the main actor. § Previews/Resolved Issues, .md L788–792. |  | release note |
| XCODE-111 | 27.0 | Xcode 27.0 | 178289150 | Coding Intelligence: "Xcode now ships with Apple-built specialists for targeted tasks, like localization, UIKit resizing and accessibility." (178289150) | § Coding Intelligence/New Features, .md L172. | release note |
| XCODE-112 (part 1) | 27.0 | Xcode 27.0 | 172961797, 177076406 | Coding Intelligence: the Preview Snapshot MCP tool renders variants such as light/dark, orientation and "various type size overrides" (172961797), and returns the simulator platform, device and OS (177076406) | § Coding Intelligence, .md L156–166. | release note |
| XCODE-112 (part 2) | 27.0 | Xcode 27.0 | 175179787 | Agents can boot simulators, install and launch apps, synthesize touches and screenshot (175179787) | § Coding Intelligence, .md L156–166. | release note |
| XCODE-113 | 27.0 | Xcode 27.0 | 183317784, 181147968 | Coding Intelligence: agents can verify tvOS apps by moving focus with the Siri Remote (183317784) and verify watchOS apps through the Digital Crown and buttons (181147968). .md L210, L222. |  | release note |
| XCODE-114 | 27.0 | Xcode 27.0 | 177462284, 177462397 | Coding Intelligence, accessibility fixes in Xcode's own UI: prompt-area buttons have "more accessible labels and descriptions" (177462284), and VoiceOver no longer gets trapped in the Coding Assistant prompt area (177462397) | § Coding Intelligence/Resolved Issues, .md L227–229. | release note |
| XCODE-115 | 27.0 | Xcode 27.0 | — | Coding Intelligence (other): plugins with skills, MCP servers and ACP agents. Agent Client Protocol support. A filesystem-access security layer. Gemini and Antigravity providers. A beta-5 preview of `xcrun mcp-server`, which works without an open workspace. § Coding Intelligence, .md L150–222. |  | release note |
| XCODE-116 | 27.0 | Xcode 27.0 | 136303612, 180969028 | Swift: the Swift Compiler section has one new feature, dependency-scanner optimization requiring unique Clang module names (136303612), and one known issue, an SE-0508 source break for `init` accessors (180969028). It contains **no availability-checking items**. § Swift Compiler, .md L943–981. |  | release note |
| XCODE-117 | 27.0 | Xcode 27.0 | 176188980 | Localization: strings inside availability-constrained `#Preview` macros are now excluded from String Catalogs (176188980) (FB22696182) | § Localization/Resolved Issues, .md L697. | release note |
| XCODE-120 | 27.0 | Security skill (naming collision with "audit") | 181104536 | The only "audit" in Xcode 27.x notes is the "audit-xcode-security-settings" Code Intelligence skill (181104536). It is not an accessibility audit. Source: [Xcode 27 RN](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) § Security/New Features, .md L877. T1. |  | release note |

29 rows.

## Stable: Xcode 27.1

| Claim ID | Release | Notes heading | Radar(s) | Entry (notes' paraphrase) | Locator | Evidence type |
|---|---|---|---|---|---|---|
| XCODE-118 (part 1) | 27.1 | Xcode 27.1 | 182598534 | Previews: the overrides picker adds a **Display** group for a device's alternative display (182598534) |  | release note |
| XCODE-118 (part 2) | 27.1 | Xcode 27.1 | 185924957, 187046347 | Known issues: iOS 27.1-specific APIs fail to compile for Mac Catalyst (185924957), and iOS 27.1 targets show no Catalyst run destination (187046347) |  | release note |
| XCODE-118 (part 3) | 27.1 | Xcode 27.1 | 187708500, 187708663, 187708767, 190155353 | The workaround is `#if !targetEnvironment(macCatalyst)` or a Catalyst 27.0 minimum. iPhone Duo Simulator known issues (187708500, 187708663, 187708767, 190155353). There are no accessibility entries. Locators: .md L28–54. |  | release note |

3 rows.

## Stable: Xcode 27.2

| Claim ID | Release | Notes heading | Radar(s) | Entry (notes' paraphrase) | Locator | Evidence type |
|---|---|---|---|---|---|---|
| XCODE-119 (part 1) | 27.2 | Xcode 27.2 | 187148389 | Device Hub known issue: VoiceOver, the Accessibility Inspector and other accessibility tools "cannot convey screen content on an iPhone Duo within Device Hub" (187148389) | § Device Hub/Known Issues, .md L76–78. | release note |
| XCODE-119 (part 2) | 27.2 | Xcode 27.2 | 189261485 | Device Hub can't customize text size for iOS 18-or-earlier devices (189261485) (FB25077755) | § Device Hub/Known Issues, .md L76–78. | release note |
| XCODE-119a (part 1) | 27.2 | Xcode 27.2 | 188634387 | Device Hub new and fixed: Sidecar touch forwarding for multi-finger gestures (188634387). A bundle including Slow Motion Animation, Shake, Fall and Memory Pressure simulation (simulators only) (.md L30) |  | release note |
| XCODE-119a (part 2) | 27.2 | Xcode 27.2 | 187484157 | Input for iOS 17 sims (187484157) |  | release note |
| XCODE-119a (part 3) | 27.2 | Xcode 27.2 | 177181719 | Modifier keys reach the right device (177181719) |  | release note |
| XCODE-119a (part 4) | 27.2 | Xcode 27.2 | 181945323, 182553164 | The pre-iOS 18 input issue (181945323) and the hardware-keyboard lingering issue (182553164) are fixed. § Device Hub, .md L28–65. |  | release note |
| XCODE-119b (part 1) | 27.2 | Xcode 27.2 | 187160501 | SDK and availability known issue: the macOS, watchOS, tvOS and visionOS 27.2 SDKs "incorrectly report 27.1 as a valid deployment target". Catalyst builds targeting 27.1 or 27.2 may be unable to use new API (187160501) |  | release note |
| XCODE-119b (part 2) | 27.2 | Xcode 27.2 | 185924957 | The Catalyst iOS 27.1 API compile issue (185924957) persists. § SDK/Known Issues, .md L143; § Mac Catalyst, .md L105. |  | release note |
| XCODE-119c (part 1) | 27.2 | Xcode 27.2 | 186442676 | Other: the RenderPreview MCP tool returns and accepts render destinations (186442676) |  | release note |
| XCODE-119c (part 2) | 27.2 | Xcode 27.2 | 188422137 | The JSON `.xcproj` project format arrives. XCTest UI Automation `.rotateDigitalCrown` is fixed (188422137). .md L129, L136, L168. |  | release note |

10 rows.

## Beta (not shipped): Xcode 27.3 beta

These rows are beta-only. Do not treat them as shipped behavior.

| Claim ID | Release | Notes heading | Radar(s) | Entry (notes' paraphrase) | Locator | Evidence type |
|---|---|---|---|---|---|---|
| XCODE-120a (part 1) | 27.3 beta | Xcode 27.3 beta (BETA) | 95593221 | Swift Testing: "Xcode now supports writing UI tests with Swift Testing and `XCUIAutomation`." (95593221) |  | release note |
| XCODE-120a (part 2) | 27.3 beta | Xcode 27.3 beta (BETA) | 187479559 | .md L95. UI Automation adds `XCUIHinge` for the iPhone Duo hinge angle (187479559), .md L102. |  | release note |
| XCODE-120b (part 1) | 27.3 beta | Xcode 27.3 beta (BETA) | 169537162 | Device Hub: option-drag simulates two-finger touch on iPhone and iPad (169537162) |  | release note |
| XCODE-120b (part 2) | 27.3 beta | Xcode 27.3 beta (BETA) | 190652440 | Input accepted for sims older than iOS 18 etc. (190652440) |  | release note |
| XCODE-120b (part 3) | 27.3 beta | Xcode 27.3 beta (BETA) | 179246120 | Drag-and-drop install, open and save (179246120) |  | release note |
| XCODE-120b (part 4) | 27.3 beta | Xcode 27.3 beta (BETA) | 185140491 | Known issue: Sidecar is limited to two touches (185140491). .md L35–49. |  | release note |
| XCODE-120c (part 1) | 27.3 beta | Xcode 27.3 beta (BETA) | 176531615 | Previews: RenderPreview snapshot filenames and metadata include applied overrides (176531615) |  | release note |
| XCODE-120c (part 2) | 27.3 beta | Xcode 27.3 beta (BETA) | 181244878 | Interactive delayed macOS snapshots (181244878). Plus several fixes (.md L58–81) |  | release note |
| XCODE-120c (part 3) | 27.3 beta | Xcode 27.3 beta (BETA) | 185837709 | Coding assistant: GitHub Copilot added (185837709), .md L28. No accessibility-specific entries. |  | release note |

9 rows.
