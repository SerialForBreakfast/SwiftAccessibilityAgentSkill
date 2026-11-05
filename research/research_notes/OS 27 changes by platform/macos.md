# macOS 27 "Golden Gate" release notes: full inventory (27.0, 27.2, and the 27.3 beta), with accessibility flags

Snapshot date: 2026-11-05. Stable releases are 27.0, 27.0.1 and 27.2. The 27.3 beta is kept apart: every row from it is labelled "27.3 beta".
Claim IDs MAC-101 to MAC-396 are release-note entries, one row for each bullet in Apple's order. MAC-397 and above are added claims (dates, WWDC, DocC).
Earlier MAC-0x claims: no earlier macOS notes file was found under `research_notes/` (`grep -rl "MAC-0"` returned nothing), so no MAC-0x to MAC-1xx matches can be confirmed. The report writer should reconcile them by Apple issue number if the earlier notes exist somewhere else.

**Source captures (fetched 2026-11-05 with curl):**

| File | URL | HTTP | Bytes | SHA-256 | Bullets / unique issue numbers |
|---|---|---|---|---|---|
| macOS 27 (27.0) | https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes.md | 200 | 66,704 | 0616186e80cae8071deee10b3010c97b1a07f128b68f340d3497d01f424c118a | 272 / 272 (86 `###` sections) |
| macOS 27.1 (attempted) | https://developer.apple.com/documentation/macos-release-notes/macos-27_1-release-notes.md | 404 (SPA shell served) | 15,639 | c8a4f47291ff4563e78e90f4326f3d457661a44a8041d823b1c21b325eb7c510 | n/a (no page exists) |
| macOS 27.2 | https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes.md | 200 | 2,463 | 1a80a8819f65a464acf484c5f5ef9581630210c70a124d8f57388874e3081a69 | 9 / 9 |
| macOS 27.3 beta | https://developer.apple.com/documentation/macos-release-notes/macos-27_3-release-notes.md | 200 | 6,176 | e1a78c79b5ec0dc5bf9bf5885de779b5c5dec689ed331d5f5f4c44e75046ff10 | 15 / 15 |
| Release-notes index | https://developer.apple.com/tutorials/data/documentation/macos-release-notes.json | 200 | 41,970 | 2d8499c636b28cbebf9535a096e73cc64e857b4a3c5e9d82eb2b3e3ff648a86f | lists only the 27, 27.2 and 27.3 pages for the 27 cycle |

Notes on the page titles: the 27.0 page is titled "macOS 27 Golden Gate Release Notes". It is cumulative across the betas and mentions "Beta 1/2/5" inside some entries. The 27.3 page is titled "macOS 27.3 Golden Gate Beta Release Notes".

## Q1. Every documented entry: section, status, issue number, SDK conditions, workarounds

### Takeaway
Apple's macOS 27 release notes have 296 bullets: 272 in 27.0, 9 in 27.2 and 15 in the 27.3 beta. All are listed below. About 48 are high-priority for accessibility and adjacent interaction (marked ★). They fall into five groups:
- The menu-item-image reduction in AppKit, SwiftUI and UIKit/Catalyst, which depends on the SDK an app links against.
- New semantic "tabs" roles that VoiceOver reads as "tabs": `NSSegmentedControl.Role.tabs`, `NSToolbarItemGroup.role` and `TabsPickerStyle`.
- Keyboard-loop and focus fixes in AppKit and the open/save panels.
- SwiftUI-on-macOS controls that no longer use AppKit controls underneath (`Slider` no longer uses `NSSlider`; bordered `Menu` and `Picker` no longer use `NSPopUpButton`).
- A full redesign of gesture recognizers and text selection in AppKit (`NSTextSelectionManager`, exclusive gestures).

### Cited Findings

#### High-priority accessibility and interaction findings (★ rows, all Tier-1, all from the 27.0 page unless marked)
Base URL for these rows: [macOS 27 Release Notes](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes). The locator is the section plus the Apple issue number.

**VoiceOver and semantic roles**
- MAC-118 (AppKit › New Features, 162577742): `NSToolbarItemGroup.role` and `NSSegmentedControl.role` are new, including a `tabs` role. With that role, controls "are read by VoiceOver as 'tabs' and have a distinct visual appearance." DocC confirms `NSSegmentedControl.Role` has the cases `automatic`, `tabs` and `valueSelection` (macOS 27.0). `NSToolbarItemGroup.Role` is listed for iOS, iPadOS, Mac Catalyst and macOS 27.0. See MAC-405.
- MAC-309 (SwiftUI › New Features, 173211711): `TabsPickerStyle` is new. It works like `.segmented`, "but VoiceOver reads it as 'tabs'", and has a distinct look on macOS. DocC lists it for iOS, iPadOS, Mac Catalyst, macOS, tvOS and visionOS 27.0.
- MAC-307 (SwiftUI, 170678002): in apps built with the latest SDKs, a `TabView` in an inspector now looks the same as one in a sidebar, and both automatically use the `.tabs` picker style.
- MAC-330 (SwiftUI › Resolved, 171831601): on macOS, a `Menu` with a `.plain` or custom button style used the AXDescription (Label) attribute instead of AXTitle. Fixed.
- MAC-325 (SwiftUI › Resolved, 155906280): section backgrounds in the `.grouped` form style did not show a border when the "Show borders" accessibility setting was on. Fixed.

**Keyboard navigation and focus**
- MAC-124 (AppKit › Resolved, 43112307): keyboard focus and tab order in expanded and collapsed open/save panels might not traverse all fields and controls, including the accessory view. Fixed.
- MAC-133 (AppKit › Resolved, 169837566): "When full keyboard navigation is off, the keyboard loop might not traverse the correct fields and controls." Fixed.
- MAC-115 (AppKit › New, 120442314): the Recents list in open and save panels can be reached with Command-Shift-F.
- MAC-116 (AppKit › New, 150791154): the Window › Move & Resize and Window › Full Screen Tile menus now work on open and save panels that are not shown as a sheet.
- MAC-331 (SwiftUI › Resolved, 174278196): buttons with `keyboardShortcut(.defaultAction)` stayed tinted when disabled. Fixed.
- MAC-336 (SwiftUI › Resolved, 178957869): buttons with `.defaultAction` and a `.destructive` role did not look destructive in sheet toolbars. Fixed.
- MAC-209 (NSGestureRecognizer › New, 173551081): the new Info.plist key `NSGestureRecognizerSuppressesMainMenuActions` lets main-menu actions run while gesture recognizers are active. DocC's AppKit updates page describes the same key as controlling "whether gesture recognizers suppress menu keyboard shortcuts". See MAC-406.

**Menus (behavior depends on the linked SDK)**
- MAC-120 (AppKit › New, 170477566): menu bar and context menus show a reduced set of item images. `NSMenu` hides all symbol images by default and honors the xib "macOS 26.0 only" checkbox. This applies to apps linked on macOS 26.0 SDK or later. Images can be controlled with the new `NSMenuItem.preferredImageVisibility`, which DocC lists as macOS 27.0.
- MAC-139 (AppKit › Resolved, 179374305 / FB23070183): this refines MAC-120. For apps linked on the macOS 27 SDK, both symbol and non-symbol images are hidden automatically. On earlier SDKs, non-symbol images stay visible.
- MAC-140 (AppKit › Resolved, 179936632): on SDKs before macOS 27, NSMenu shows the image when the title and attributed title are both empty. On the 27 SDK such images are hidden, so image-only items need `preferredImageVisibility`. **Accessibility risk:** an image-only menu item that loses its image shows no visible content at all.
- MAC-306 (SwiftUI, 170480710): SwiftUI hides menu symbol images in most contexts. Use `.labelStyle(.titleAndIcon)` to force an icon to show.
- MAC-352 (UIKit, 170479084): on iPadOS 27 and macOS 27 (Catalyst), menu elements do not show images by default. `UIMenuElement.preferredImageVisibility` is new.
- MAC-121 (AppKit, 177605020): the NSTextView context menu moves Layout Orientation into the Font submenu. This applies only to apps linked on the macOS 27 SDK.
- MAC-312 (SwiftUI, 175594929): with the 27 SDK, `LabeledContent` inside a `Menu` maps its value to the menu item's subtitle.
- MAC-138 (AppKit › Resolved, 178288949): some NSMenu APIs, such as `highlightedItem`, did not work in context menus. Fixed.
- MAC-333 (SwiftUI › Resolved, 175053352): the "Settings…" item showed no icon. Fixed.
- MAC-334 (SwiftUI › Resolved, 177616606): a crash when a toolbar overflow submenu is an `NSHostingMenu`. Fixed.
- MAC-268 (Siri › Known Issue, 176299524): "Ask Siri" might appear in context menus on macOS even when Siri is disabled. No workaround is listed.

**Toolbars, title bars, windows and sheets**
- MAC-122 (AppKit, 180962967 / FB23481212): for apps linked on macOS 27.0 or later, `NSTitlebarAccessoryViewController` may draw outside its bounds by default (for shadows and interactive glass). It may be clipped during reveal animations.
- MAC-195 (Mac Catalyst › Resolved, 176879915): show/hide sidebar toolbar buttons were missing for some apps. Fixed.
- MAC-193 (Mac Catalyst › New, 69906818): when you switch to a Catalyst app that has no open windows, it no longer creates a new window, matching AppKit apps. It still does when activated from the Dock or Spotlight.
- MAC-328 (SwiftUI › Resolved, 167448274): with 27 SDKs, the `controlSize`, `buttonSizing`, `buttonRepeatBehavior`, `menuIndicatorVisibility` and `ButtonBorderShape` environment values are reset to their defaults in sheets and popovers.
- MAC-369 (Window Management › Resolved, 177660206): a window could be lost when it exited full screen through Mission Control. Fixed.
- MAC-164 (Dock › Resolved, 174992242): the Dock persisted in full screen after entering and exiting Mission Control. Fixed.
- MAC-198 (Media Playback › Resolved, 177984877): in TV, Podcasts and Music, window controls could stop responding after dragging the playhead. Fixed.
- MAC-207 (NSApplication › New, 168692527): the new `.disableScreenCornerInteractions` presentation option disables Hot Corners. DocC lists it as macOS 27.0.

**Text system**
- MAC-119 (AppKit › New, 163365571): `NSTextSelectionManager` provides click, drag, shift-click and double/triple-click selection using gesture recognizers. `NSTextView` now uses it. Subclasses that override `mouseDown:` keep working through a binary-compatible fallback. DocC lists macOS 27.0.
- MAC-127 (AppKit › Resolved, 118196071 / FB13354582): a selectable, non-editable `NSTextField` drew text outside its bounds when truncating. Fixed.
- MAC-135 (AppKit › Resolved, 175095850): an `NSTextField` with `textColor = nil` showed inconsistent colors while editing. Fixed.
- MAC-126 (AppKit › Resolved, 115247760): `NSTextContentManager` subclasses could not be instantiated. Fixed.
- MAC-304 and MAC-323 (SwiftUI, 158160386 and 151015350): selectable `Text` now supports `TextRenderer` (27 SDK).
- MAC-310 (SwiftUI, 173362083): `TextInputBorderShape` and `textInputBorderShape(_:)` are new. `.squareBorder` and `.roundedBorder` are soft-deprecated in favor of `.bordered`. DocC lists 27.0.
- MAC-322 (SwiftUI › Resolved, 86580365): with the macOS 27 SDK, `TextField` honors custom font and color on its prompt.

**SwiftUI controls no longer built on AppKit controls (affects inherited AX behavior)**
- MAC-301 (SwiftUI, 68559433 / FB8657381): bordered `Menu` and `Picker` buttons "no longer use `NSPopUpButton` in their implementation."
- MAC-311 (SwiftUI, 173990195): "On macOS, the `Slider` implementation no longer uses `NSSlider`."
- MAC-308 (SwiftUI, 172689844): disabled `.checkbox` toggles are no longer tinted, so they are easier to tell apart from enabled ones.
- MAC-326 (SwiftUI › Resolved, 158800693): `.glass` and `.glassProminent` buttons showed no hover state outside a toolbar. Fixed.
- MAC-335 (SwiftUI › Resolved, 177790490): dragging a `Slider` in a window that moves when its background is dragged could move the window instead. Fixed.
- MAC-332 (SwiftUI, 174628712): with the macOS 27 SDK, `List` accepts drops the same way iOS does.

**Liquid Glass, contrast and appearance**
- MAC-130 (AppKit › Resolved, 159019809): `NSScrollView` showed the scroll edge effect when no scrollers were visible. Fixed.
- MAC-131 (AppKit › Resolved, 168066807): `NSSegmentedCell` drew at the wrong location under Liquid Glass. Fixed.
- MAC-125 (AppKit › Resolved, 107870015): the Web Safe Colors list drew incorrectly in right-to-left layouts. Fixed.

**Pointer, trackpad and gestures (redesigned in AppKit)**
- MAC-117 (AppKit, 160867808): `NSRefreshController` adds pull-to-refresh, set through `NSScrollView.refreshController`. DocC lists macOS 27.0.
- MAC-208 (NSGestureRecognizer, 165650612): the notes call the property `cancellableByScrollGesture`. **DocC symbol is `isCancellableByScrollGesture`** (macOS 27.0).
- MAC-209 (173551081): only the first hit-tested view hierarchy activates gesture recognizers. Opt out with `NSView.exclusiveGestureBehavior` (DocC: macOS 27.0) or the Info.plist key `NSViewGestureRecognizerIsExclusive`.
- MAC-210 (175705302): stuck gestures are cancelled automatically after user input has ended for a few seconds. The `NSCrashOnStuckGestureTimeout` default helps with debugging.
- MAC-211 (176396492): the `NSGestureRecognizerCrashOnMissingOverrides` diagnostic default is new.
- MAC-212 (NSScrollView, 164924201): the notes name `scrollGestureForFailureRelationship`. **DocC symbol is `scrollGestureForRelationships`**, alongside `minimumNumberOfTouchesForScrolling` and `maximumNumberOfTouchesForScrolling` (macOS 27.0).
- MAC-134 (AppKit, 173975472): `NSClickGestureRecognizer` with a click count above 1 now sends its action before the multi-click timeout. This is behavior-change wording with no "Fixed:" prefix.
- MAC-137 (AppKit › Resolved, 176395420): the base `NSGestureRecognizer.locationInView:` now returns `NSZeroPoint` and logs an error. Subclasses must override it.
- MAC-355 (UIKit › Resolved, 175048540): Catalyst views with both drag and context-menu interactions could not activate both by touch. Fixed.
- MAC-166 (Drag and Drop, 177839494): `draggingFrame` could be wrong. Fixed.
- MAC-218 (Previews, 177754200): the cursor stayed as an open hand after dragging a 3D annotation. Fixed.

**Assessment, accessibility settings and voice**
- MAC-143 (Automatic Assessment Configuration › New, 158132137): finer-grained assessment configuration, with controls for the Dock, Menu Bar and accessibility settings. See MAC-409 for the WWDC session.
- MAC-269 (Siri › Known Issue, 176812955): Siri cannot interact with specific photos by voice, such as "photo one". Workaround: use the photo picker or tap to select. This is a voice-interaction limit, not Voice Control.
- MAC-255 (Siri › Resolved, 177649865): disabling Siri might not have deleted Siri and Dictation history. Fixed.

#### Full entry-by-entry inventory (Tier-1, Apple)
The locator for each row is its Release page plus Section plus Apple issue number. URLs: 27.0 is https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes, 27.2 is https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes, and 27.3 beta is https://developer.apple.com/documentation/macos-release-notes/macos-27_3-release-notes.

How to read the columns:
- **Status:** "New / behavior change" means a New Features entry whose wording says "now", "no longer" or "default". "Resolved (behavior change)" means an entry listed under Resolved Issues that has no "Fixed:" prefix.
- **SDK cond.:** marks text that mentions linking or building with an SDK.
- **Flag:** comes from keyword matching and includes some false positives. The ★ column is the curated priority list above.
- **Workaround:** the quote is cut at 20 words.

| ID | Release | Section | Status | Apple issue (FB) | Apple text (≤22 words, verbatim prefix) | SDK cond. | Workaround | A11y/interaction flag (heuristic) | Tier | Priority |
|---|---|---|---|---|---|---|---|---|---|---|
| MAC-101 | 27.0 | General | Resolved | 179068335 | “Fixed: If you installed Xcode 27 beta on macOS Tahoe 26.5.1 and earlier, macOS virtual machine installation will fail due to a …” |  | — | — | T1 |  |
| MAC-102 | 27.0 | Accessory Access | Resolved | 176815987 | “Fixed: Accessory Access does not work inside App Sandbox.” |  | — | — | T1 |  |
| MAC-103 | 27.0 | Accessory Access | Resolved | 177390971 | “Fixed: The Accessory Access framework is not supported within a macOS virtual machine.” |  | — | — | T1 |  |
| MAC-104 | 27.0 | AirPods Max 2 | Resolved | 178280323 | “Fixed: You cannot update AirPods Max 2 firmware beta in iOS 27 Beta 1 and macOS 27 Beta 1. AirPods Max 2 …” |  | — | — | T1 |  |
| MAC-105 | 27.0 | AirPort Utility | Deprecation | 158248382 | “AirPort Utility is no longer included with new clean installations of macOS. However, if you update macOS when AirPort Utility is already …” |  | — | — | T1 |  |
| MAC-106 | 27.0 | APFS | Resolved | 182156751 | “Fixed: High-RAM Macs running macOS 27 Golden Gate Beta might erroneously report filesystem metadata corruption that doesn’t actually exist when running First …” |  | — | — | T1 |  |
| MAC-107 | 27.0 | App Intents | New / behavior change | 173431080 | “You can now pass a name parameter of type `AttributedString` to the `notes.createNote` and `notes.updateNote` schemas.” |  | — | — | T1 |  |
| MAC-108 | 27.0 | App Intents | Resolved | 175534195 | “Fixed: Default values from schemas might not be applied for parameters that are of “Set” type.” |  | — | — | T1 |  |
| MAC-109 | 27.0 | App Intents | Resolved | 181212609 FB23526663 | “Fixed: Requests that should result in an app’s `reminders.updateReminder`-conforming intent to be called might fail with “<App> cannot be used for this …” |  | — | — | T1 |  |
| MAC-110 | 27.0 | App Intents | Resolved | 181763422 | “Fixed: AppEntity instances have a cumulative size limit of 10MB, including all child properties and their values. Your app might crash if …” |  | — | — | T1 |  |
| MAC-111 | 27.0 | App Intents | Resolved | 182532125 | “Fixed: The notes.appendText schema erroneously disappeared from the SDK.” | SDK-linked | — | — | T1 |  |
| MAC-112 | 27.0 | App Intents | Known Issue | 177198033 | “If you adopt the Audio App Schema domain, you might have trouble playing your content using Siri.” |  | Adopt an IntentValueQuery that takes the AudioSearch input, or index your entities in Spotlight. | — | T1 |  |
| MAC-113 | 27.0 | App Intents | Known Issue | 181800016 FB23652582 | “Existing entities that conformed to @AppEntity(schema: .photos.asset) in prior releases might no longer compile in the 27 SDKs because new properties were …” | SDK-linked | To continue conforming to the schema, adopt the additional properties and move the code behind an availability check. | — | T1 |  |
| MAC-114 | 27.0 | App Intents | Deprecation | 176751155 | “The `calendar.deleteEvents` schema has been renamed to `calendar.deleteEvent`.” |  | — | — | T1 |  |
| MAC-115 | 27.0 | AppKit | New | 120442314 | “The Recents list in the open and save panels can be accessed with the keyboard shortcut cmd-shift-f.” |  | — | Keyboard/focus; Windows/sheets/panels | T1 | ★ |
| MAC-116 | 27.0 | AppKit | New | 150791154 | “Window > Move & Resize and Window > Full Screen Tile menus can be used to move, resize, open and save panels …” |  | — | Menus; Windows/sheets/panels | T1 | ★ |
| MAC-117 | 27.0 | AppKit | New | 160867808 | “In macOS 27.0, AppKit adds `NSRefreshController`, providing pull-to-refresh functionality for `NSScrollView`. You can set it with `NSScrollView.refreshController`, configure a target or action …” |  | — | Pointer/trackpad/gesture | T1 |  |
| MAC-118 | 27.0 | AppKit | New | 162577742 | “`NSToolbarItemGroup` adds the `role` property and the `NSToolbarItemGroupRole` enum, allowing toolbar item groups to be tagged with a semantic role. `NSSegmentedControl` similarly …” |  | — | VoiceOver/AX; Toolbar; Glass/contrast/material | T1 | ★ |
| MAC-119 | 27.0 | AppKit | New / behavior change | 163365571 | “`NSTextSelectionManager` provides common text selection interactions (click, drag, shift-click, double/triple-click word/line/paragraph selection) to a `NSView` with a set of `NSGestureRecognizers` rather than …” |  | — | Text system; Pointer/trackpad/gesture | T1 | ★ |
| MAC-120 | 27.0 | AppKit | New / behavior change | 170477566 | “In macOS 27.0, menu bar and context menus present a reduced set of menu item images, similar to the behavior prior to …” | SDK-linked | — | Menus | T1 | ★ |
| MAC-121 | 27.0 | AppKit | New / behavior change | 177605020 | “NSTextView’s `menuForEvent:` now returns a context menu in which the Layout Orientation menu item, and its submenu, are located inside the Font …” | SDK-linked | — | Menus; Text system | T1 | ★ |
| MAC-122 | 27.0 | AppKit | New / behavior change | 180962967 FB23481212 | “When an app is linked on macOS 27.0 or later, `NSTitlebarAccessoryViewController` is now allowed to draw outside its bounds by default, supporting …” | SDK-linked | — | Toolbar; Glass/contrast/material | T1 | ★ |
| MAC-123 | 27.0 | AppKit | Resolved | 6938919 | “Fixed: In apps built with the macOS 27.0 SDK, setting `allowedContentTypes` and `treatsFilePackagesAsDirectories` on `NSOpenPane` updates `canChooseFiles` and `canChooseDirectories` based on whether …” | SDK-linked | — | Windows/sheets/panels | T1 |  |
| MAC-124 | 27.0 | AppKit | Resolved | 43112307 | “Fixed: Keyboard focus and tab order in expanded and collapsed open/save panels might not traverse all fields and controls — including the …” |  | — | Keyboard/focus; Windows/sheets/panels | T1 | ★ |
| MAC-125 | 27.0 | AppKit | Resolved | 107870015 | “Fixed: The Web Safe Colors list displays incorrectly in right-to-left layout.” |  | — | Glass/contrast/material | T1 |  |
| MAC-126 | 27.0 | AppKit | Resolved | 115247760 FB13146578 | “Fixed: Subclasses of `NSTextContentManager` cannot be instantiated due to internal class-cluster initialization assumptions, preventing apps from defining custom content managers.” |  | — | Text system | T1 |  |
| MAC-127 | 27.0 | AppKit | Resolved | 118196071 FB13354582 | “Fixed: An `NSTextField` configured as selectable but not editable draws its text outside the field’s bounds when text truncation is enabled.” |  | — | Text system | T1 | ★ |
| MAC-128 | 27.0 | AppKit | Resolved | 132024038 | “Fixed: `NSAlert` buttons erroneously allow `bezelColor` customization.” |  | — | Windows/sheets/panels | T1 |  |
| MAC-129 | 27.0 | AppKit | Resolved | 140307283 | “Fixed: When an allowed file type has multiple valid extensions — for example, `.htm` and `.html` — `NSSavePanel` appends additional file extensions …” |  | — | Windows/sheets/panels | T1 |  |
| MAC-130 | 27.0 | AppKit | Resolved | 159019809 FB19853927 | “Fixed: `NSScrollView` displays the system scroll edge effect when the scroll view has no visible scrollers.” |  | — | Pointer/trackpad/gesture; Glass/contrast/material | T1 | ★ |
| MAC-131 | 27.0 | AppKit | Resolved | 168066807 FB21616308 | “Fixed: An `NSSegmentedCell` draws incorrectly under the Liquid Glass appearance, with the control rendering at the wrong location.” |  | — | Glass/contrast/material | T1 | ★ |
| MAC-132 | 27.0 | AppKit | Resolved | 169126818 FB21791717 | “Fixed: A subclass of `NSSegmentedCell` that overrides label drawing does not take charge of drawing labels, with the system drawing the default …” |  | — | AppKit (adjacent) | T1 |  |
| MAC-133 | 27.0 | AppKit | Resolved | 169837566 | “Fixed: When full keyboard navigation is off, the keyboard loop might not traverse the correct fields and controls.” |  | — | Keyboard/focus | T1 | ★ |
| MAC-134 | 27.0 | AppKit | Resolved (behavior change) | 173975472 | “`NSClickGestureRecognizers` with a click count greater than 1 will send an action before their multi-click timeout has elapsed.” |  | — | Pointer/trackpad/gesture | T1 | ★ |
| MAC-135 | 27.0 | AppKit | Resolved | 175095850 FB22546245 | “Fixed: An `NSTextField` whose `textColor` is set to `nil` displays inconsistent text colors while in editing mode.” |  | — | Text system | T1 |  |
| MAC-136 | 27.0 | AppKit | Resolved | 176048351 | “Fixed: `-[NSFilePromiseReceiver receivePromisedFilesAtDestination:options:operationQueue:reader:]` asserts that it is called during `-prepareForDragOperation:`, `-performDragOperation:`, or `-concludeDragOperation:`. If `receivePromisedFilesAtDestination:...` is called at other times, your application …” |  | — | Pointer/trackpad/gesture | T1 |  |
| MAC-137 | 27.0 | AppKit | Resolved | 176395420 | “Fixed: The base `NSGestureRecognizer` implementation of `locationInView:` previously returned the current mouse location converted into the view’s coordinate system, which is incorrect …” |  | — | Pointer/trackpad/gesture | T1 | ★ |
| MAC-138 | 27.0 | AppKit | Resolved | 178288949 | “Fixed: Some NSMenu APIs, such as `highlightedItem`, will not work in context menus.” |  | — | Menus | T1 | ★ |
| MAC-139 | 27.0 | AppKit | Resolved | 179374305 FB23070183 | “Fixed: For applications linked on the macOS 27 SDK, both symbol and non-symbol menu item images are now automatically hidden. For applications …” | SDK-linked | — | Menus | T1 | ★ |
| MAC-140 | 27.0 | AppKit | Resolved | 179936632 | “Fixed: For applications linked on SDKs prior to macOS 27, NSMenu now automatically shows menu item images if the menu item title …” | SDK-linked | — | Menus | T1 | ★ |
| MAC-141 | 27.0 | Apple Intelligence Report | Resolved | 176056930 | “Fixed: When you view Apple Intelligence Report entries for Home Intelligence, some data that was sent to Private Cloud Compute won’t appear …” |  | — | — | T1 |  |
| MAC-142 | 27.0 | Apple Unified Logging System | New | 160567675 | “Unified Logging System archives generated on 27.0 releases cannot be read on macOS 26.1 or earlier due to an updated archive format. …” |  | — | — | T1 |  |
| MAC-143 | 27.0 | Automatic Assessment Configuration | New / behavior change | 158132137 | “You can now use a more flexible and granular Automatic Assessment Configuration in macOS 27, giving you greater control over your testing …” |  | — | VoiceOver/AX; Menus; Assessment/a11y settings | T1 | ★ |
| MAC-144 | 27.0 | AVFAudio | Resolved | 163978549 | “Fixed: AudioDSP might crash when audio device properties change.” |  | — | — | T1 |  |
| MAC-145 | 27.0 | Background Assets | New | 163944365 | “You can reduce your app’s storage usage with localized asset packs. The system delivers the appropriately localized asset packs based on the …” |  | — | — | T1 |  |
| MAC-146 | 27.0 | Communication Safety | Resolved | 183962032 | “Fixed: Sensitive QRCode detected as non-sensitive, preventing 3rd party developers from testing API functionality.” |  | — | — | T1 |  |
| MAC-147 | 27.0 | Core AI | New / behavior change | 174796039 | “iOS 27 includes Neural Engine improvements for Apple Intelligence capable devices. The system now restricts background access to the Neural Engine, similar …” |  | — | — | T1 |  |
| MAC-148 | 27.0 | Core AI | New | 179282606 | “Access to the Neural engine when your app is in the background requires the new entitlement: “com.apple.developer.background-tasks.continued-processing.inference”.” |  | — | — | T1 |  |
| MAC-149 | 27.0 | Core AI | Resolved | 169746264 | “Fixed: `AIModelCache` entries might not honor the cache policy you provide, causing re-specialization to occur more often than expected.” |  | — | — | T1 |  |
| MAC-150 | 27.0 | Core AI | Resolved | 175789258 | “Fixed: When inference runs on the GPU, `InferenceFunction.encode` blocks until all compute is complete instead of returning as soon as encoding is …” |  | — | — | T1 |  |
| MAC-151 | 27.0 | Core AI | Resolved | 176210080 | “Fixed: Certain weight and activation configurations may not run on the Neural Engine, such as FP8-quantized weights and activations, palettized weights with …” |  | — | — | T1 |  |
| MAC-152 | 27.0 | Core AI | Resolved | 176807213 | “Fixed: When you run `InferenceFunction.run` on functions with both state arguments and outputs with dynamic shapes, the framework might be unable to …” |  | — | — | T1 |  |
| MAC-153 | 27.0 | Core AI | Resolved | 177008303 | “Fixed: On-device specialization fails when loading an `.aimodel` converted with `coreai-torch` v0.4.0.” |  | — | — | T1 |  |
| MAC-154 | 27.0 | Core AI | Resolved | 177354777 | “Fixed: Inference might fail or crash for models with control flow over dynamic-shape tensors (for example, linear-attention LLMs such as Qwen3.5/3.6).” |  | — | — | T1 |  |
| MAC-155 | 27.0 | Core AI | Resolved | 177729331 | “Fixed: Ahead-of-time (AOT) compilation might fail unexpectedly for certain models.” |  | — | — | T1 |  |
| MAC-156 | 27.0 | Core AI | Resolved | 177991751 | “Fixed: When Metal API Validation is enabled, CoreAI models might fail to execute.” |  | — | — | T1 |  |
| MAC-157 | 27.0 | Core AI | Resolved | 178056451 | “Fixed: Models with custom Metal kernels will fail to load.” |  | — | — | T1 |  |
| MAC-158 | 27.0 | Core AI | Resolved | 179732320 | “Fixed: App-group support might not work as expected on certain model types.” |  | — | — | T1 |  |
| MAC-159 | 27.0 | Core AI | Resolved | 181264112 | “Fixed: On-device specialization might fail when loading an `.aimodelc` compiled ahead of time using Xcode 27 Beta 2 or earlier.” |  | — | — | T1 |  |
| MAC-160 | 27.0 | Core Spotlight | Known Issue | 183770678 | “Creating a SpotlightSearchTool without a configuration and using it with a LanguageModelSession backed by the on-device system language model fails with an …” |  | Configure the tool with a focused guide, which uses a compact schema sized for the on-device model: ``` let configuration … | Windows/sheets/panels | T1 |  |
| MAC-161 | 27.0 | CoreStorage | Deprecation | 175892420 | “Encrypted HFS+ (CoreStorage) is deprecated and will not be supported in a future version of macOS. If you use Encrypted HFS+ backups …” |  | — | — | T1 |  |
| MAC-162 | 27.0 | Deprecation Information | New / behavior change | 169548657 | “Intel-based applications that will no longer run in macOS 28.0 now display a treatment in Get Info.” |  | — | — | T1 |  |
| MAC-163 | 27.0 | Disk Images | New | 177868758 | “The new DiskImageKit framework provides Swift APIs for creating and managing standalone and stacked disk images in the Apple Sparse Image Format …” |  | — | — | T1 |  |
| MAC-164 | 27.0 | Dock | Resolved | 174992242 | “Fixed: While using an app in full screen, the Dock might persist when entering and exiting Mission Control.” |  | — | Windows/sheets/panels | T1 |  |
| MAC-165 | 27.0 | Dock | Resolved | 179502922 | “Fixed: The Dock might incorrectly indicate that some applications (such as Device Hub) are running in the background when they are not.” |  | — | — | T1 |  |
| MAC-166 | 27.0 | Drag and Drop | Resolved | 177839494 | “Fixed: When you call `enumerateDraggingItemsWithOptions:...` during `draggingSession:willBeginAtPoint:`, the returned `NSDraggingItem` might have an incorrect `draggingFrame` value.” |  | — | Pointer/trackpad/gesture | T1 |  |
| MAC-167 | 27.0 | DVDPlayback | Deprecation | 179136240 | “The `DVDPlayback ` framework has been removed from the macOS 27 Golden Gate SDK and apps cannot build against it. The framework …” | SDK-linked | — | — | T1 |  |
| MAC-168 | 27.0 | EcosystemUI | New / behavior change | 175697313 | “Settings > General now lists Intel-based apps that will be incompatible with macOS 28.0. The list also identifies unused Intel-based software discovered …” |  | — | — | T1 |  |
| MAC-169 | 27.0 | EcosystemUI | Resolved | 175781938 | “Fixed: The Intel-based apps view might unexpectedly display “Additional components” when the primary app is not native.” |  | — | — | T1 |  |
| MAC-170 | 27.0 | EcosystemUI | Resolved | 177192993 | “Fixed: Intel-based apps might appear erroneously in the unsupported apps list with the entry “Steam Game”. Games should not appear in this …” |  | — | — | T1 |  |
| MAC-171 | 27.0 | Finder | Resolved | 178093786 | “Fixed: Suggested names for a file or folder might be more generic than its contents. For example, a folder containing only bird …” |  | — | — | T1 |  |
| MAC-172 | 27.0 | First-Party App Search | Resolved | 178186226 | “Fixed: Search assets might download slowly for languages and regions other than English and the United States, causing degraded search experiences for …” |  | — | — | T1 |  |
| MAC-173 | 27.0 | Foundation | Resolved | 161588649 FB20439045 | “Fixed: `+[NSURL URLWithString:]` no longer double-encodes the `%` of valid percent-escape sequences when encoding other invalid characters.” |  | — | — | T1 |  |
| MAC-174 | 27.0 | Foundation Models | Resolved | 177748926 | “Fixed: When using the on-device Apple Foundation Model for both tool calling and guided generation, some prompts might cause the model to …” |  | — | — | T1 |  |
| MAC-175 | 27.0 | Foundation Models | Resolved | 177899620 | “Fixed: `@Generable` on an `enum` produces a deprecation warning about `GenerationError` that cannot be silenced.” |  | — | — | T1 |  |
| MAC-176 | 27.0 | Foundation Models | Resolved | 177901494 | “Fixed: Truncating transcript history in the `onPrompt` modifier might cause an unexpected runtime error.” |  | — | — | T1 |  |
| MAC-177 | 27.0 | Foundation Models | Resolved | 177902488 | “Fixed: `onPrompt` might not be called when applied to a `Profile` without instructions.” |  | — | — | T1 |  |
| MAC-178 | 27.0 | Foundation Models | Resolved | 178181782 | “Fixed: `PrivateCloudComputeLanguageModel` always uses greedy decoding.” |  | — | — | T1 |  |
| MAC-179 | 27.0 | Game Center | Resolved | 172683368 | “Fixed: When you trigger the Access Point, its completion handler is never invoked.” |  | — | — | T1 |  |
| MAC-180 | 27.0 | Game Controller | New / behavior change | 168071382 | “The PlayStation® Access™ controller is now supported on macOS, iPadOS, and iOS. You can create custom input profiles in game controller settings …” |  | — | — | T1 |  |
| MAC-181 | 27.0 | Game Controller | Resolved | 163514369 FB20846101 | “Fixed: Modifications to the game controller lightbar (`GCController.light`) may persist after your application no longer has focus.” |  | — | Keyboard/focus | T1 |  |
| MAC-182 | 27.0 | Game Controller | Resolved | 176985783 FB22770585 | “Fixed: `+[GCController supportsHIDDevice:]` might return an incorrect result when queried with a recently connected HID device.” |  | — | — | T1 |  |
| MAC-183 | 27.0 | Gaming | New | 166398727 | “A new command line tool lets you enable support for legacy Intel-based games during beta releases. To enable it, run the following …” |  | — | — | T1 |  |
| MAC-184 | 27.0 | Gatekeeper | New / behavior change | 123097648 FB13625586 | “The spctl command line tool now supports a –purge command which will clean up Gatekeeper database entries for apps and executables which …” |  | — | — | T1 |  |
| MAC-185 | 27.0 | Gaussian Splats | Resolved | 183538823 | “Fixed: When 3DGS content rendered by a GaussianSplatComponent is moved offscreen and then returns to the visible area, some splats might be …” |  | — | — | T1 |  |
| MAC-186 | 27.0 | Hardware Security | New | 152103975 | “arm64e.x1 introduces additional hardware security and performance instructions, including CPA2 for stronger MIE protection. Devices with support for arm64e.x1 include iPhone models …” |  | — | — | T1 |  |
| MAC-187 | 27.0 | HomeKit | New | 178858470 | “When Apple Intelligence in the Home app is enabled, your HomeKit Secure Video recordings are processed on-device and through Private Cloud Compute …” |  | — | — | T1 |  |
| MAC-188 | 27.0 | HomeKit | New | 181282161 | “Apple Intelligence for Home requires an iCloud+ subscription starting at 2TB.” |  | — | — | T1 |  |
| MAC-189 | 27.0 | Image Playground | Resolved | 174413381 | “Fixed: When you try to generate an image using ChatGPT in the Messages extension on macOS, the image fails to generate.” |  | — | — | T1 |  |
| MAC-190 | 27.0 | Image Playground | Resolved | 178256174 | “Fixed: In the Image Playground photo picker, the All and Suggested tabs are missing, which might limit the number of photos available …” |  | — | SwiftUI-macOS | T1 |  |
| MAC-191 | 27.0 | Install macOS Golden Gate | Resolved | 79372256 | “Fixed: macOS cannot be installed to an external storage device connected to the DFU port.” |  | — | — | T1 |  |
| MAC-192 | 27.0 | Launch Daemons and Agents | Resolved | 166415497 | “Fixed: `launchd` no longer supports loading `launchd` property list files with the quarantine extended attribute.” |  | — | — | T1 |  |
| MAC-193 | 27.0 | Mac Catalyst | New / behavior change | 69906818 | “Catalyst apps now behave like AppKit apps when you switch to them with no open windows - they won’t automatically create new …” |  | — | Windows/sheets/panels; Catalyst | T1 | ★ |
| MAC-194 | 27.0 | Mac Catalyst | Resolved | 57819435 | “Fixed: Mac-Idiom Catalyst apps could not use `UIStepper`.” |  | — | Catalyst | T1 |  |
| MAC-195 | 27.0 | Mac Catalyst | Resolved | 176879915 | “Fixed: For some apps, the show/hide sidebar toolbar buttons are missing.” |  | — | Toolbar | T1 | ★ |
| MAC-196 | 27.0 | Mail | Resolved | 177768221 | “Fixed: Smart Mailboxes might not update while you’re using Mail.” |  | — | — | T1 |  |
| MAC-197 | 27.0 | Mail Banners | Resolved | 173869986 | “Fixed: Mail banners for early flights will show the flight status as delayed.” |  | — | — | T1 |  |
| MAC-198 | 27.0 | Media Playback | Resolved | 177984877 | “Fixed: In apps like TV, Podcasts, and Music, the window controls may become unresponsive after dragging the playhead to adjust the playback …” |  | — | Windows/sheets/panels; Pointer/trackpad/gesture; Media/captions | T1 | ★ |
| MAC-199 | 27.0 | Messages | Resolved | 177657977 | “Fixed: GIFs and pasted images might render as the incorrect size.” |  | — | — | T1 |  |
| MAC-200 | 27.0 | Messages | Resolved | 180859837 | “Fixed: HDR screenshots might appear garbled when sent in Messages.” |  | — | — | T1 |  |
| MAC-201 | 27.0 | Metal | Resolved | 172520325 | “Fixed: When you use a sampler to read from a texture with clamp-to-edge addressing mode, the result might be clamped to zero.” |  | — | — | T1 |  |
| MAC-202 | 27.0 | Metal | Resolved | 177318505 | “Fixed: On devices in the Apple 10 GPU family, using a sampler to read from a texture with clamp-to-edge addressing mode might …” |  | — | — | T1 |  |
| MAC-203 | 27.0 | Music | Resolved | 177480780 | “Fixed: Music Visualizer shows a black screen in both full screen and window mode.” |  | — | Windows/sheets/panels; Media/captions | T1 |  |
| MAC-204 | 27.0 | Network Security | New / behavior change | 176055825 | “Starting in 27.0 operating systems, select system processes now enforce stricter network security (TLS) requirements. These new requirements might cause connections to …” |  | — | — | T1 |  |
| MAC-205 | 27.0 | News | Resolved | 177972625 | “Fixed: The News app crashes on launch when configuration profiles are installed.” |  | — | — | T1 |  |
| MAC-206 | 27.0 | Notification Center | Resolved | 181736751 | “Fixed: You might be unable to dismiss certain notifications.” |  | — | — | T1 |  |
| MAC-207 | 27.0 | NSApplication | New / behavior change | 168692527 | “`NSApplication.presentationOptions` now includes the `.disableScreenCornerInteractions` option, which you can use to disable Hot Corners.” |  | — | AppKit (adjacent) | T1 | ★ |
| MAC-208 | 27.0 | NSGestureRecognizer | New | 165650612 | “A new `cancellableByScrollGesture` property on `NSGestureRecognizer` allows gesture recognizers to be automatically cancelled when the enclosing scroll view is panned.” |  | — | Pointer/trackpad/gesture | T1 | ★ |
| MAC-209 | 27.0 | NSGestureRecognizer | New | 173551081 | “Only the initial hit-tested view hierarchy will activate gesture recognizers until all gestures terminate. A new `exclusiveGestureBehavior` property on `NSView` allows you …” |  | — | Menus; Pointer/trackpad/gesture | T1 | ★ |
| MAC-210 | 27.0 | NSGestureRecognizer | New / behavior change | 175705302 | “To prevent exclusive gestures from making apps unresponsive, stuck gestures are automatically cancelled after user input has ended for a few seconds. …” |  | — | Pointer/trackpad/gesture | T1 | ★ |
| MAC-211 | 27.0 | NSGestureRecognizer | New / behavior change | 176396492 | “A new diagnostic user default `NSGestureRecognizerCrashOnMissingOverrides` is provided to help developers find `NSGestureRecognizer` subclasses that are missing required overrides to ensure that …” |  | — | Windows/sheets/panels; Pointer/trackpad/gesture | T1 | ★ |
| MAC-212 | 27.0 | NSScrollView | New | 164924201 | “New properties on `NSScrollView` allow you to constrain the number of touches needed to scroll. The new `scrollGestureForFailureRelationship` property allows you to …” |  | — | Pointer/trackpad/gesture | T1 | ★ |
| MAC-213 | 27.0 | PhotoKit | Resolved | 175050631 | “Fixed: The `addedDate` property on `PHAsset` might return `nil` even though it’s marked as non-nullable.” |  | — | — | T1 |  |
| MAC-214 | 27.0 | PhotoKit | Deprecation | 175412725 FB22589474 | “The `originalFilename` property on `PHAssetResource` is incorrectly marked as non-nullable, which misrepresents the property value; a new, nullable `filename` property is available …” |  | — | — | T1 |  |
| MAC-215 | 27.0 | Photos Edit | Resolved | 178183850 | “Fixed: A thin white line might be visible in photos that have had Spatial Reframing applied.” |  | — | — | T1 |  |
| MAC-216 | 27.0 | Previews | New | 176839273 | “Preview and Quick Look have added support for RealityKit as the scene renderer for USD and other 3D scenes that were previously …” |  | — | — | T1 |  |
| MAC-217 | 27.0 | Previews | Resolved | 177483209 | “Fixed: After you load certain 3D models, materials for most other 3D models might not appear properly and display an error pattern …” |  | — | — | T1 |  |
| MAC-218 | 27.0 | Previews | Resolved | 177754200 | “Fixed: When you drag an annotation in a 3D document, such as a USD file, and release the mouse button, the cursor …” |  | — | Pointer/trackpad/gesture | T1 |  |
| MAC-219 | 27.0 | Privacy & Security Settings | Known Issue | 184660124 | “In the Files & Folders pane, a process without a bundle ID cannot be granted access to specific app data containers or …” |  | Consider if the access is necessary. If required, grant Full Disk Access to the process for the duration of the … | — | T1 |  |
| MAC-220 | 27.0 | RealityKit | New | 178061856 | “The Gaussian Splat Component API in RealityKit will be available in an upcoming release.” |  | — | — | T1 |  |
| MAC-221 | 27.0 | RealityKit | Resolved | 172875414 | “Fixed: Some MaterialX 1.39 nodes are not supported.” |  | — | — | T1 |  |
| MAC-222 | 27.0 | RealityKit | Resolved | 177674901 | “Fixed: `ComputeGraphComponents` stored in a Reality file do not render when loaded.” |  | — | — | T1 |  |
| MAC-223 | 27.0 | RealityKit | Resolved | 177976245 | “Fixed: When `OpacityComponent` is applied to an entity with opaque materials, `RealityRenderer` renders the opaque materials with transparency, revealing interior surfaces. Only …” |  | — | — | T1 |  |
| MAC-224 | 27.0 | RealityKit | Resolved | 178092354 | “Fixed: An App might crash if the `SurroundingsLight` component is added to more than 8 light entities.” |  | — | — | T1 |  |
| MAC-225 | 27.0 | Reminders | Known Issue | 180040003 | “After you tap “Add to Reminders” in Messages, the “New Reminder” interface presents the reminder with an empty title field.” |  | Tap “Add to Reminders” in the “New Reminder” interface to create the reminder, then edit the title in the Reminders … | — | T1 |  |
| MAC-226 | 27.0 | Rosetta | New | 168097174 | “On launch, Applications previously set to “Open using Rosetta” by a user will have the application launch natively. Any compatibility issues requiring …” |  | — | — | T1 |  |
| MAC-227 | 27.0 | Rosetta | Deprecation | 163213094 | “If Rosetta was previously installed, it is not automatically restored after upgrading to macOS 27.0.” |  | — | — | T1 |  |
| MAC-228 | 27.0 | Rosetta | Deprecation | 171187112 | “Installer packages which specify no `hostArchitecture` will now default to arm64. Ensure any pre and post install scripts behave as intended under …” |  | — | — | T1 |  |
| MAC-229 | 27.0 | Rosetta | Deprecation | 176042635 | “Intel-based plugins and loaders may not appear in Settings or trigger notifications of their incompatibility. All Intel-based software will no longer be …” |  | — | SwiftUI-macOS | T1 |  |
| MAC-230 | 27.0 | Safari | Resolved | 177470803 | “Fixed: Selecting “Rename” or “Edit Address…” from the context menu in the sidebar has no effect.” |  | — | Menus | T1 |  |
| MAC-231 | 27.0 | Safari | Resolved | 178099724 | “Fixed: Safari Intelligence features might appear as available before assets are fully downloaded. If you use the feature before assets are available, …” |  | — | — | T1 |  |
| MAC-232 | 27.0 | Safari | Known Issue | 183044008 | “When developing Safari Extensions, unsigned extensions might not appear until rebuilt when using the “Allow Unsigned Extensions” checkbox.” |  | Ensure “Allow Unsigned Extensions” is checked and rebuild the extension project. | — | T1 |  |
| MAC-233 | 27.0 | Safari Extensions | Resolved | 179293939 | “Fixed: Turning on or off Safari extensions created via the “Describe an Extension” feature might not take effect until Safari is relaunched.” |  | — | — | T1 |  |
| MAC-234 | 27.0 | Security | Resolved | 183456836 | “Fixed: Obtaining new certificates via ACME fails. New MDM enrollments using Managed Device Attestation fail.” |  | — | — | T1 |  |
| MAC-235 | 27.0 | Setup Assistant | Resolved | 175787760 | “Fixed: Setup Assistant might remain on screen after you configure a new user account.” |  | — | — | T1 |  |
| MAC-236 | 27.0 | ShaderGraph | Resolved | 177976666 | “Fixed: The `realitykit_hair_surfaceshader` node does not support `DiffuseLightProbeGroupComponent`. Materials built with this node might not respond to diffuse light probe group lighting.” |  | — | — | T1 |  |
| MAC-237 | 27.0 | Shortcuts | Resolved | 180337087 | “Fixed: Battery Level and Charger automations might not work on macOS.” |  | — | — | T1 |  |
| MAC-238 | 27.0 | Shortcuts | Resolved | 181071784 | “Fixed: The Use Model action might fail to run when using the On-Device option for some output types.” |  | — | — | T1 |  |
| MAC-239 | 27.0 | Shortcuts | Known Issue | 166068090 | “If an app intent uses Duration or `LPLinkMetadata`, creating a shortcut with that intent and then attempting to edit it with “Describe …” |  | If the model discards the action, press “Undo” to recover the unsupported intent. | — | T1 |  |
| MAC-240 | 27.0 | Shortcuts | Known Issue | 168315587 | “When an app intent defines a `UnionValue` parameter with two number-related types (for example, both Int and Double), the number option appears …” |  | Define only one number-related type in the `UnionValue` parameter (for example, use only Int or only Double, not both). | Menus; SwiftUI-macOS | T1 |  |
| MAC-241 | 27.0 | Siri | Resolved | 172713904 | “Fixed: Siri cannot find albums in Photos on macOS.” |  | — | — | T1 |  |
| MAC-242 | 27.0 | Siri | Resolved | 174911042 | “Fixed: When you ask Siri to start navigation using AMap, Tencent Maps, or Baidu Maps on Mac, navigation might not start.” |  | — | — | T1 |  |
| MAC-243 | 27.0 | Siri | Resolved | 175230813 | “Fixed: Siri ignores custom values for navigation preferences, transport, and incident types in apps that use `maps.startNavigation` or `maps.reportIncident` intent schemas.” |  | — | — | T1 |  |
| MAC-244 | 27.0 | Siri | Resolved | 175380461 | “Fixed: When location data is unavailable or only coarse-accuracy location data is available, Maps searches initiated through Siri might return empty or …” |  | — | — | T1 |  |
| MAC-245 | 27.0 | Siri | Resolved | 175884006 | “Fixed: When you turn off Siri, some photo-related questions might return web search results instead of prompting you to share the photo …” |  | — | — | T1 |  |
| MAC-246 | 27.0 | Siri | Resolved | 176400964 | “Fixed: When you ask Siri to work with reminder lists, you might need to use the exact list name. Siri might not …” |  | — | — | T1 |  |
| MAC-247 | 27.0 | Siri | Resolved | 176844035 | “Fixed: App Intents with `@UnionValue` types that accept a `PlaceDescriptorEntity` and a `String` always receive `String` values instead of `PlaceDescriptorEntity` entities.” |  | — | — | T1 |  |
| MAC-248 | 27.0 | Siri | Resolved | 177190637 | “Fixed: Starting a call with Siri might fail with an error in apps that adopt CallKit and the `phone.startCall` AppSchema.” |  | — | — | T1 |  |
| MAC-249 | 27.0 | Siri | Resolved | 177356158 | “Fixed: When you ask Siri to send a message to a contact that doesn’t exist on your device, Siri might draft a …” |  | — | — | T1 |  |
| MAC-250 | 27.0 | Siri | Resolved | 177416168 | “Fixed: You might not see names and images of email senders in the Siri email list UI.” |  | — | — | T1 |  |
| MAC-251 | 27.0 | Siri | Resolved | 177464215 | “Fixed: Siri might not resolve some entity types when your app has provided only an `EntityStringQuery` for the entity type.” |  | — | — | T1 |  |
| MAC-252 | 27.0 | Siri | Resolved | 177476889 | “Fixed: Siri functionality during software updates is limited, including calls to emergency services.” |  | — | — | T1 |  |
| MAC-253 | 27.0 | Siri | Resolved | 177545828 | “Fixed: Asking Siri to call short phone numbers, such as “Call 17”, might fail.” |  | — | — | T1 |  |
| MAC-254 | 27.0 | Siri | Resolved | 177634308 | “Fixed: Cannot click on Notes in Siri responses on MacOS.” |  | — | — | T1 |  |
| MAC-255 | 27.0 | Siri | Resolved | 177649865 | “Fixed: Disabling Siri might not delete your Siri and Dictation interaction history from your device.” |  | — | Voice/Siri | T1 |  |
| MAC-256 | 27.0 | Siri | Resolved | 177679168 | “Fixed: Siri might not find app-specific contacts that are only indexed in Spotlight and do not appear in the Contacts app.” |  | — | — | T1 |  |
| MAC-257 | 27.0 | Siri | Resolved | 177722240 | “Fixed: Siri cannot create a recurring reminder or update an existing reminder to be reoccurring.” |  | — | — | T1 |  |
| MAC-258 | 27.0 | Siri | Resolved | 177755742 | “Fixed: When you use ChatGPT with Apple Intelligence, some responses used in follow-up queries or when you resume a chat might be …” |  | — | — | T1 |  |
| MAC-259 | 27.0 | Siri | Resolved | 177762533 | “Fixed: When you ask Siri to find, search, or read reminders, Siri might list or read the reminders instead of showing a …” |  | — | — | T1 |  |
| MAC-260 | 27.0 | Siri | Resolved | 177992979 | “Fixed: Siri might run the incorrect `OpenIntent` or `system.open` intent when multiple intents targeting different entity types are available in your app.” |  | — | — | T1 |  |
| MAC-261 | 27.0 | Siri | Resolved | 178025056 | “Fixed: When you tap the Send button in the Siri message confirmation flow, the message might fail to send.” |  | — | — | T1 |  |
| MAC-262 | 27.0 | Siri | Resolved | 178379209 | “Fixed: When asking Siri to call, message, or email a contact, Siri might fail to resolve the correct person — particularly when …” |  | — | — | T1 |  |
| MAC-263 | 27.0 | Siri | Resolved | 178384054 | “Fixed: Businesses with overnight hours might display as “Closed till [next day]” even during open hours.” |  | — | — | T1 |  |
| MAC-264 | 27.0 | Siri | Resolved | 178489724 | “Fixed: Siri might not respond to your voice correctly.” |  | — | — | T1 |  |
| MAC-265 | 27.0 | Siri | Resolved | 178560562 | “Fixed: In the Siri app, conversations might be deleted a few minutes after receiving streaming responses.” |  | — | — | T1 |  |
| MAC-266 | 27.0 | Siri | Resolved (behavior change) | 182145010 | “As of beta 5, Siri AI conversation history no longer syncs to devices running a prior beta. iCloud sync works between devices …” |  | — | — | T1 |  |
| MAC-267 | 27.0 | Siri | Known Issue | 171728298 | “After Siri returns photo search results and you select photos, Siri might not detect which photos are selected on screen. Commands like …” |  | Open Photos, select the photos you want to act on, then perform the action using Siri — for example, “Send … | — | T1 |  |
| MAC-268 | 27.0 | Siri | Known Issue | 176299524 | ““Ask Siri” might appear in context menus on macOS even when Siri is disabled in System Settings or the system is in …” |  | — | Menus | T1 |  |
| MAC-269 | 27.0 | Siri | Known Issue | 176812955 | “Siri doesn’t support voice commands to interact with specific photos. For example, you can’t refer to photos by number, such as “photo …” |  | Use the photo picker to select the photo you want, or tap to select photos directly. | Voice/Siri | T1 |  |
| MAC-270 | 27.0 | Siri | Known Issue | 177116121 | “When you ask Siri for Maps information, the response snippets might appear incomplete or display formatting issues.” |  | Ask Siri to repeat the information, or open Maps directly for complete details. | — | T1 |  |
| MAC-271 | 27.0 | Siri | Known Issue | 177376984 | “When you ask Siri to add photos to an album, the confirmation prompt and spoken response might report or display more photos …” |  | Add photos to the album manually in the Photos app: tap Select, tap the photos you want to add, tap … | — | T1 |  |
| MAC-272 | 27.0 | Siri | Known Issue | 177984074 | “Non-SF Symbol custom images for entities might not appear in Siri results for third-party apps.” |  | — | — | T1 |  |
| MAC-273 | 27.0 | Software Update | Resolved | 174428921 | “Fixed: Background Security Improvements cannot be installed when your startup disk is an external storage device.” |  | — | — | T1 |  |
| MAC-274 | 27.0 | Software Update | Resolved | 178942816 | “Fixed: Devices configured with Reduced Security mode might fail to install macOS 27 beta 1. Devices in this mode might also be …” |  | — | — | T1 |  |
| MAC-275 | 27.0 | Spatial Preview | Resolved | 156180612 | “Fixed: When Device Discovery UI is invoked via the Spatial Preview API, it might show nearby Apple Vision Pro devices running an …” |  | — | — | T1 |  |
| MAC-276 | 27.0 | Spatial Preview | Resolved | 174366004 | “Fixed: Some large 3D models with poor mesh connectivity of approximately 750,000 to 3.75 million triangles might not appear when previewing on …” |  | — | — | T1 |  |
| MAC-277 | 27.0 | Spatial Preview | Resolved | 178168374 | “Fixed: When spatial previewing USDZ assets larger than 75MB in Preview or using the Spatial Preview API, edits made on Mac or …” |  | — | — | T1 |  |
| MAC-278 | 27.0 | Startup Disk | Known Issue | 166640903 | “When a Mac is running macOS 11.0, you might not be able to select the boot volume of macOS 27.0 or later …” |  | Shut down your Mac, press and hold the power button until “Loading startup options” appears, then select the boot volume … | — | T1 |  |
| MAC-279 | 27.0 | StoreKit | New / behavior change | 141012819 | “Offer code redemption APIs now return a `VerificationResult` when redemption completes. If a redemption succeeds, your app receives a `VerificationResult` that contains …” |  | — | — | T1 |  |
| MAC-280 | 27.0 | StoreKit | New / behavior change | 156749517 | “StoreKit now includes the `Transaction.OwnershipType.assigned` and `Transaction.RevocationType.assignmentRevoked` enum values to support volume purchases. `Transaction` query methods now additionally return transactions assigned to …” |  | — | — | T1 |  |
| MAC-281 | 27.0 | StoreKit | New | 160501742 | “New `Product.ProductType` APIs represent subscription Bundles and subscription Suites. New APIs in `Product.SubscriptionInfo.BundledSubscription` let you fetch merchandising data about subscriptions contained in …” |  | — | — | T1 |  |
| MAC-282 | 27.0 | StoreKit | New | 167808780 | “`partnerName` and `partnerId` properties for Advanced Commerce API are available in [`Transaction.AdvancedCommerceInfo`](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct) and [`RenewalInfo.AdvancedCommerceInfo`](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct).” |  | — | — | T1 |  |
| MAC-283 | 27.0 | StoreKit | Resolved | 180072209 | “Fixed: The transaction refund request sheet fails to display on macOS.” |  | — | Windows/sheets/panels | T1 |  |
| MAC-284 | 27.0 | StoreKit | Resolved | 181766819 FB23646993 | “Fixed: `Storefront` API might return incorrect metadata when running in the TestFlight environment.” |  | — | — | T1 |  |
| MAC-285 | 27.0 | StoreKit | Resolved | 181842500 | “Fixed: Purchases of non-subscription In-App Purchases made using the SKTestSession.buyProduct() method might fail with an invalid product error. The billingPlanType(_:) PurchaseOption isn’t …” |  | — | — | T1 |  |
| MAC-286 | 27.0 | StoreKit | Resolved | 183165269 | “Fixed: Transactions fail to finish.” |  | — | — | T1 |  |
| MAC-287 | 27.0 | StoreKit Testing in Xcode | Resolved | 102093015 FB11767567 | “Fixed: The unified app receipt is not updated after forcing a subscription expiration with `SKTestSession`.” |  | — | — | T1 |  |
| MAC-288 | 27.0 | StoreKit Testing in Xcode | Resolved | 154390284 FB18403150 | “Fixed: The `SKTestSession` `disableDialogs` setting is not always respected for all system dialogs.” |  | — | Windows/sheets/panels | T1 |  |
| MAC-289 | 27.0 | StoreKit Testing in Xcode | Resolved | 160698598 FB20269723 | “Fixed: Subscription upgrades performed with the Xcode Transaction Manager are not reported in `Transaction.updates`.” |  | — | — | T1 |  |
| MAC-290 | 27.0 | StoreKit Testing in Xcode | Resolved | 162014134 FB20537538 | “Fixed: The renewal behavior preference is not respected when using the `purchaseDate(_:renewalBehavior:)` purchase option to make purchases using `SKTestSession`.” |  | — | — | T1 |  |
| MAC-291 | 27.0 | StoreKit Testing in Xcode | Resolved | 173406202 | “Fixed: Calls to `Transaction.requestRefund()` fail in StoreKit Testing in Xcode and `AppStore.presentOfferCodeRedeemSheet(from:options:)` targets the sandbox environment instead of StoreKit Testing.” |  | — | Windows/sheets/panels | T1 |  |
| MAC-292 | 27.0 | StoreKit Testing in Xcode | Resolved | 174560379 FB22475017 | “Fixed: Re-purchasing a previously refunded non-consumable fails with an already owned error when using StoreKit Testing in Xcode.” |  | — | — | T1 |  |
| MAC-293 | 27.0 | StoreKit Testing in Xcode | Resolved | 177942756 | “Fixed: Using `pricingTerms.commitmentInfo.price` in StoreKit Testing in Xcode returns an incorrect price for monthly subscriptions with a 12-month commitment.” |  | — | — | T1 |  |
| MAC-294 | 27.0 | StoreKit Testing in Xcode | Resolved | 178441109 | “Fixed: Transactions for upgraded subscriptions are immediately marked as expired when using StoreKit Testing in Xcode.” |  | — | — | T1 |  |
| MAC-295 | 27.0 | StoreKit Testing in Xcode | Resolved | 178555835 | “Fixed: Purchases and fetching the unified app receipt sometimes fails with an unknown error when using StoreKit Testing in Xcode.” |  | — | — | T1 |  |
| MAC-296 | 27.0 | StoreKit Testing in Xcode | Resolved | 183933307 FB24137836 | “Fixed: Intro offer eligibility does not reset immediately after calling `SKTestSession.clearTransactions()`.” |  | — | — | T1 |  |
| MAC-297 | 27.0 | StoreKit Testing in Xcode | Known Issue | 184155259 | “Changing the storefront or locale using `SKTestSession` doesn’t propagate through `Storefront.updates`.” |  | — | — | T1 |  |
| MAC-298 | 27.0 | StoreKit Testing in Xcode | Known Issue | 184255116 | “Failed purchases using `SKTestSession` might display error dialogs even when `dialogsDisabled` is set to true.” |  | — | Windows/sheets/panels | T1 |  |
| MAC-299 | 27.0 | Swift Charts | Resolved | 174168981 | “Fixed: When your project has a minimum deployment target lower than 27.0, using conditionals inside a `Chart` closure produces the warning “Conformance …” |  | — | — | T1 |  |
| MAC-300 | 27.0 | SwiftData | Resolved | 178113288 | “Fixed: You might experience a deadlock for @Query when saving a ModelContext on a background actor while scheduling new async tasks for …” |  | — | — | T1 |  |
| MAC-301 | 27.0 | SwiftUI | New / behavior change | 68559433 FB8657381 | “Bordered `Menu` and `Picker` buttons now support better label customization and no longer use `NSPopUpButton` in their implementation.” |  | — | Menus; SwiftUI-macOS | T1 | ★ |
| MAC-302 | 27.0 | SwiftUI | New / behavior change | 78212597 | “`AsyncImage` now automatically caches downloaded images using HTTP caching protocols, allowing servers to control caching behavior via standard headers. You can customize …” |  | — | SwiftUI-macOS | T1 |  |
| MAC-303 | 27.0 | SwiftUI | New / behavior change | 105893279 | “A `@State` declared with an expression as its initial value used to evaluate the expression each time the view struct re-instantiates. In …” |  | — | SwiftUI-macOS | T1 |  |
| MAC-304 | 27.0 | SwiftUI | New / behavior change | 158160386 FB19589465 | “In apps built with the iOS 27.0 and macOS 27.0 SDKs, selectable `Text` views now support `TextRenderer`.” | SDK-linked | — | Text system; SwiftUI-macOS | T1 | ★ |
| MAC-305 | 27.0 | SwiftUI | New | 158441552 | “In apps built with the 27.0 SDKs, the new `ReadableDocument` and `WritableDocument` protocols support asynchronous reading and writing, progress reporting, and direct …” | SDK-linked | — | SwiftUI-macOS | T1 |  |
| MAC-306 | 27.0 | SwiftUI | New / behavior change | 170480710 | “The menu bar on iPadOS 27.0 and macOS 27.0, as well as context menus on macOS 27.0, present a reduced set of …” |  | — | Menus; SwiftUI-macOS | T1 | ★ |
| MAC-307 | 27.0 | SwiftUI | New / behavior change | 170678002 | “In apps built with the latest SDKs, the appearance of `TabViews` in inspectors now matches their appearance in sidebars, and in both …” | SDK-linked | — | SwiftUI-macOS; Glass/contrast/material | T1 | ★ |
| MAC-308 | 27.0 | SwiftUI | New / behavior change | 172689844 | “Disabled Toggles using the `.checkbox` style are no longer tinted in macOS, so you can more easily distinguish them from their enabled …” |  | — | SwiftUI-macOS; Glass/contrast/material | T1 | ★ |
| MAC-309 | 27.0 | SwiftUI | New / behavior change | 173211711 | “The `TabsPickerStyle` style is now available for pickers that represent tab-based navigation and content selection. This style is similar to the `.segmented` …” |  | — | VoiceOver/AX; SwiftUI-macOS; Glass/contrast/material | T1 | ★ |
| MAC-310 | 27.0 | SwiftUI | New / behavior change | 173362083 | “You can now use the `TextInputBorderShape` type to customize the border shape of text input controls like `TextField` with the `textInputBorderShape(_:)` view …” |  | — | Text system; SwiftUI-macOS | T1 | ★ |
| MAC-311 | 27.0 | SwiftUI | New / behavior change | 173990195 | “On macOS, the `Slider` implementation no longer uses `NSSlider`.” |  | — | SwiftUI-macOS | T1 | ★ |
| MAC-312 | 27.0 | SwiftUI | New | 175594929 | “In apps built with the 27.0 SDKs, a `LabeledContent` view used inside a `Menu` maps its value to the platform menu item’s …” | SDK-linked | — | Menus; SwiftUI-macOS; Media/captions | T1 | ★ |
| MAC-313 | 27.0 | SwiftUI | New / behavior change | 175902616 | “The @Entry macro now warns of potential issues if you store default class instances or closures in the environment. The SwiftUI Specialist …” |  | — | SwiftUI-macOS | T1 |  |
| MAC-314 | 27.0 | SwiftUI | New / behavior change | 177185166 | “You can now access `concentricCornerRadii` and `concentricCornerRadii(in:)` on `GeometryProxy`. These APIs return the corner radii that are concentric with the view’s container …” |  | — | SwiftUI-macOS | T1 |  |
| MAC-315 | 27.0 | SwiftUI | New / behavior change | 177458781 | “You can now use the `Document` protocol for representing documents in `DocumentGroup`. This protocol combines `ReadableDocument` and `WritableDocument` for common read-and-write cases. …” |  | — | SwiftUI-macOS | T1 |  |
| MAC-316 | 27.0 | SwiftUI | New | 177526032 | “`@ContentBuilder` type checking performance is further improved for valid code compared to Beta 1.” |  | — | SwiftUI-macOS | T1 |  |
| MAC-317 | 27.0 | SwiftUI | New / behavior change | 179388848 | “The new data item or error object based `alert` and `confirmationDialog` modifiers can now be used by projects targeting iOS 15.0, macOS …” |  | — | Windows/sheets/panels; SwiftUI-macOS | T1 |  |
| MAC-318 | 27.0 | SwiftUI | New / behavior change | 180300890 | “In macOS apps built with the macOS 27 SDK, the action retrieved from the `\.newDocument` environment value accepts an in-memory `ReadableDocument` produced …” | SDK-linked | — | Windows/sheets/panels; SwiftUI-macOS | T1 |  |
| MAC-319 | 27.0 | SwiftUI | New | 180301165 | “A new `fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)` modifier exports a collection of values that conform to `WritableDocument` whose `Writer.Destination` is `URL`. The system presents a single …” |  | — | Windows/sheets/panels; SwiftUI-macOS | T1 |  |
| MAC-320 | 27.0 | SwiftUI | New / behavior change | 180301399 | “The `makeFileWrapper` closure of `FileWrapperDocumentWriter` now receives a second argument, `previous: FileWrapper?`, holding the `FileWrapper` from the document’s most recent read or …” |  | — | SwiftUI-macOS | T1 |  |
| MAC-321 | 27.0 | SwiftUI | New / behavior change | 180301692 | “`DocumentReader.Source` and `DocumentWriter.Destination` now default to `URL`. Conforming types that read from or write to a file URL no longer need to …” |  | — | SwiftUI-macOS | T1 |  |
| MAC-322 | 27.0 | SwiftUI | Resolved (behavior change) | 86580365 | “In apps built with the macOS 27.0 SDK, `TextField` respects custom font and color styling applied to its prompt. Apply styling to …” | SDK-linked | — | Text system; SwiftUI-macOS | T1 | ★ |
| MAC-323 | 27.0 | SwiftUI | Resolved | 151015350 | “Fixed: A custom `TextRenderer` applied via `.textRenderer(_:)` now takes effect on a `Text` view that also has `.textSelection(.enabled)` applied. Previously, the custom …” |  | — | Text system; SwiftUI-macOS | T1 | ★ |
| MAC-324 | 27.0 | SwiftUI | Resolved | 154080867 | “Fixed: When you apply both `.fileExporter(_:...)` and `.fileMover(_:...)` modifiers to a view, some dialogs might not present correctly.” |  | — | Windows/sheets/panels; SwiftUI-macOS | T1 |  |
| MAC-325 | 27.0 | SwiftUI | Resolved | 155906280 | “Fixed: Section backgrounds in the `.grouped` form style don’t display a border when the “Show borders” accessibility setting is turned on.” |  | — | VoiceOver/AX; SwiftUI-macOS | T1 | ★ |
| MAC-326 | 27.0 | SwiftUI | Resolved | 158800693 | “Fixed: In macOS, buttons using the `.glass` and `.glassProminent` styles don’t display a hover state when used outside of a toolbar.” |  | — | Toolbar; SwiftUI-macOS; Pointer/trackpad/gesture; Glass/contrast/material | T1 | ★ |
| MAC-327 | 27.0 | SwiftUI | Resolved | 165913417 | “Fixed: In apps built with the 27.0 SDKs, `containerRelativeFrame(_:alignment:)` incorrectly accounts for safe-area insets on a `ScrollView`’s non-scrollable axis, causing the calculated …” | SDK-linked | — | SwiftUI-macOS; Pointer/trackpad/gesture | T1 |  |
| MAC-328 | 27.0 | SwiftUI | Resolved | 167448274 | “Fixed: Certain control-related view modifiers unexpectedly affect sheet and popover content. In apps built with the 27.0 SDKs, the `controlSize`, `buttonSizing`, `buttonRepeatBehavior`, …” | SDK-linked | — | Menus; Windows/sheets/panels; SwiftUI-macOS | T1 |  |
| MAC-329 | 27.0 | SwiftUI | Resolved | 171755081 | “Fixed: Dual-axis scroll views align to `.center` instead of the `.topLeading` unit point, which disagrees with documentation. Additionally, specifying `.defaultScrollAnchor(_:)` on dual-axis …” |  | — | SwiftUI-macOS; Pointer/trackpad/gesture | T1 |  |
| MAC-330 | 27.0 | SwiftUI | Resolved | 171831601 | “Fixed: On macOS, a Menu composed with a `.plain` or custom button style uses the AXDescription (Label) attribute instead of the AXTitle …” |  | — | VoiceOver/AX; Menus; SwiftUI-macOS | T1 | ★ |
| MAC-331 | 27.0 | SwiftUI | Resolved | 174278196 | “Fixed: Buttons with `keyboardShortcut(.defaultAction)` remain tinted when disabled.” |  | — | Keyboard/focus; SwiftUI-macOS; Glass/contrast/material | T1 | ★ |
| MAC-332 | 27.0 | SwiftUI | Resolved (behavior change) | 174628712 | “In macOS apps built with the macOS 27 SDK, `List` accepts drops in two cases that previously didn’t work: drags with compatible …” | SDK-linked | — | SwiftUI-macOS; Pointer/trackpad/gesture | T1 |  |
| MAC-333 | 27.0 | SwiftUI | Resolved | 175053352 | “Fixed: The “Settings…” menu item does not display an icon.” |  | — | Menus; SwiftUI-macOS | T1 | ★ |
| MAC-334 | 27.0 | SwiftUI | Resolved | 177616606 | “Fixed: An app might crash if a submenu within the toolbar overflow menu is an `NSHostingMenu` and a user tries to open …” |  | — | Menus; Toolbar; SwiftUI-macOS | T1 |  |
| MAC-335 | 27.0 | SwiftUI | Resolved | 177790490 | “Fixed: In some system video players, when you attempt to drag a `Slider` within a window that is configured to be movable …” |  | — | Windows/sheets/panels; SwiftUI-macOS; Pointer/trackpad/gesture; Media/captions | T1 | ★ |
| MAC-336 | 27.0 | SwiftUI | Resolved | 178957869 | “Fixed: Buttons with `keyboardShortcut(.defaultAction)` and a `.destructive` role don’t appear as a destructive button in sheet toolbars.” |  | — | Keyboard/focus; Toolbar; Windows/sheets/panels; SwiftUI-macOS | T1 | ★ |
| MAC-337 | 27.0 | SwiftUI | Resolved | 179149051 FB23015259 | “Fixed: `@State` variable named using a raw identifier fails to compile.” |  | — | SwiftUI-macOS | T1 |  |
| MAC-338 | 27.0 | SwiftUI | Resolved (behavior change) | 180302015 | “The `read(from:progress:)` and `write(content:to:previous:progress:)` requirements of `DocumentReader` and `DocumentWriter` are declared with `@concurrent` instead of `nonisolated`. With approachable-concurrency defaults that infer `MainActor` …” |  | — | SwiftUI-macOS | T1 |  |
| MAC-339 | 27.0 | SwiftUI | Resolved (behavior change) | 180302065 | “The `makeDocument:` and `makeReadableDocument:` closures passed to `DocumentGroup` initializers are now `@MainActor`-isolated. SwiftUI invokes these factories on the main actor when constructing …” |  | — | SwiftUI-macOS | T1 |  |
| MAC-340 | 27.0 | SwiftUI | Resolved (behavior change) | 180302075 | “`URLDocumentConfiguration` is a `@MainActor`-isolated `@Observable` reference type and no longer conforms to `Sendable`. Code that captured a configuration in a `Sendable` closure …” |  | — | SwiftUI-macOS | T1 |  |
| MAC-341 | 27.0 | SwiftUI | Known Issue | 158441261 | “Progress reported in `DocumentReader.read(from:progress:)` and `DocumentWriter.write(snapshot:to:previous:progress:)` might not be presented.” |  | — | SwiftUI-macOS | T1 |  |
| MAC-342 | 27.0 | SwiftUI | Deprecation | 178776840 | “The `FileDocument` protocol is deprecated. Use `ReadableDocument` for read-only documents or `Document` for documents that support reading and writing.” |  | — | SwiftUI-macOS | T1 |  |
| MAC-343 | 27.0 | System | New / behavior change | 160612181 | “System now provides Swift APIs for the C `stat`, `lstat`, `fstat`, and `fstatat` system calls. This includes a new `Stat` type with …” |  | — | — | T1 |  |
| MAC-344 | 27.0 | System | Resolved | 177911316 | “Fixed: Custom `FilePath` or `FileDescriptor` extensions that make unqualified calls to `stat()` or `stat(_)` (without the `Darwin.` qualification) might conflict with the …” |  | — | — | T1 |  |
| MAC-345 | 27.0 | System Integrity Protection | New / behavior change | 161835690 | “Accessing files in other developer teams’ app data containers and app group containers no longer prompts the user for authorization; such accesses …” |  | — | — | T1 |  |
| MAC-346 | 27.0 | System Integrity Protection | New / behavior change | 178668601 | “XProtect may now restrict access to app data that is commonly targeted by malicious software. Accessing files created by other developer teams’ …” |  | — | — | T1 |  |
| MAC-347 | 27.0 | TCC | Deprecation | 90775556 | “Apps can no longer access the local TCC database directly.” |  | — | — | T1 |  |
| MAC-348 | 27.0 | Terminal | Resolved | 179656565 | “Fixed: Terminal might hang when you click Terminate in the “Do you want to terminate running process…” dialog, but recovers after a …” |  | — | Windows/sheets/panels | T1 |  |
| MAC-349 | 27.0 | Thunderbolt | Resolved | 176292156 | “Fixed: When connecting to two identical displays (same model and serial number), the first display will work as expected whereas the second …” |  | — | — | T1 |  |
| MAC-350 | 27.0 | UIKit | New | 161843040 | “When linked on iOS 27, tvOS 27, macCatalyst 27, or visionOS 27 SDKs, you can use `UIScene.extendStateRestoration` and `UIScene.completeStateRestoration` to extend state …” | SDK-linked | — | Catalyst | T1 |  |
| MAC-351 | 27.0 | UIKit | New | 168884200 | “On iOS 27.0 and iPadOS 27.0, Siri can load resources from drag interactions installed in your app’s interface. For example, when Apple …” |  | — | Menus; Pointer/trackpad/gesture | T1 |  |
| MAC-352 | 27.0 | UIKit | New / behavior change | 170479084 | “On iPadOS 27.0 and macOS 27.0, the menu bar and context menus present a reduced set of menu item images and do …” |  | — | Menus | T1 | ★ |
| MAC-353 | 27.0 | UIKit | Resolved | 170008344 | “Fixed: The `UISceneClosureConfirmation` API does not present a confirmation dialog.” |  | — | Windows/sheets/panels | T1 |  |
| MAC-354 | 27.0 | UIKit | Resolved | 173271862 | “Fixed: The `UIMenuLeaf` protocol is missing the subtitle property introduced in iOS 16.0.” |  | — | Menus; Media/captions | T1 |  |
| MAC-355 | 27.0 | UIKit | Resolved | 175048540 | “Fixed: Catalyst views that have both `UIDragInteraction` and `UIContextMenuInteraction` do not allow you to activate both interactions with touch.” |  | — | Menus; Catalyst; Pointer/trackpad/gesture | T1 | ★ |
| MAC-356 | 27.0 | UIKit | Deprecation | 141837548 | “Apps built with the latest SDK must adopt the scene-based life cycle or they fail to launch. For migration guidance, see [Transitioning …” | SDK-linked | — | — | T1 |  |
| MAC-357 | 27.0 | USDKit | Resolved | 170653056 | “Fixed: Some types of USD attributes cannot be read or modified.” |  | — | — | T1 |  |
| MAC-358 | 27.0 | USDKit | Resolved | 178071414 | “Fixed: Array, vector, matrix, and quaternion types cannot be authored using USDKit.” | SDK-linked | — | — | T1 |  |
| MAC-359 | 27.0 | USDKit | Deprecation | 177417812 | “Meshes compressed using the USDKit export API or `usdcrush tool` in Beta 1 cannot be decoded by Beta 2, and meshes from …” | SDK-linked | — | — | T1 |  |
| MAC-360 | 27.0 | VideoToolbox | New / behavior change | 177635243 | “`VTLowLatencySuperResolutionScalerConfiguration` now supports a 1.5x scale factor. Call `+supportedScaleFactorsForFrameWidth:frameHeight:` to discover the scale factors available for your source dimensions.” |  | — | — | T1 |  |
| MAC-361 | 27.0 | VideoToolbox | New / behavior change | 179040806 | “`VTLowLatencyFrameInterpolationConfiguration` now supports arbitrary source dimensions up to 1080p.” |  | — | — | T1 |  |
| MAC-362 | 27.0 | Virtualization | New / behavior change | 64203273 FB7731708 | “The vmnet port forwarding APIs now support port forwarding when communicating over loopback.” |  | — | — | T1 |  |
| MAC-363 | 27.0 | Virtualization | Resolved | 174267926 | “Fixed: Saving a virtual machine state with one or more USB devices passed through to a virtual machine may fail.” |  | — | — | T1 |  |
| MAC-364 | 27.0 | Virtualization | Resolved | 174794802 | “Fixed: If an App uses `AccessoryAccess` framework within a Virtualization framework to launch a virtual machine, and if you assign both the …” |  | — | Keyboard/focus | T1 |  |
| MAC-365 | 27.0 | Virtualization | Resolved | 177528319 | “Fixed: A virtual machine might crash during restore if a USB mass storage device was hot-plugged before the virtual machine was saved …” |  | — | — | T1 |  |
| MAC-366 | 27.0 | Virtualization | Resolved | 177662539 | “Fixed: `AAUSBAccessoryManager registerListener:withMatchingCriteria:completionHandler:` does not work with a non-empty matching criteria array.” |  | — | — | T1 |  |
| MAC-367 | 27.0 | Weather Highlights | Deprecation | 164408676 | “Weather Highlights is currently only available in US English.” |  | — | — | T1 |  |
| MAC-368 | 27.0 | Wi-Fi Settings | Resolved | 183437912 | “Fixed: Apple menu > System Settings… > Wi-Fi > Details… button does nothing.” |  | — | Menus | T1 |  |
| MAC-369 | 27.0 | Window Management | Resolved | 177660206 | “Fixed: When you exit a window from fullscreen mode using Mission Control, the window might be lost.” |  | — | Windows/sheets/panels | T1 | ★ |
| MAC-370 | 27.0 | Writing Tools | Resolved | 174926739 | “Fixed: Writing Tools on macOS might stop working after you use Describe Your Change.” |  | — | — | T1 |  |
| MAC-371 | 27.0 | xnu | Resolved | 134346968 | “Fixed: Launch binaries larger than 2GiB might fail.” |  | — | — | T1 |  |
| MAC-372 | 27.0 | XQuartz | Resolved | 180761569 | “Fixed: Clicking on X11 windows while XQuartz is in the background does not activate the XQuartz application.” |  | — | Windows/sheets/panels | T1 |  |
| MAC-373 | 27.2 | General | Resolved | 186939138 | “Fixed: Xcode might crash when using code completion on macOS 27.2 beta.” |  | — | — | T1 |  |
| MAC-374 | 27.2 | AppKit | Deprecation | 186955507 | “The `EnablePasteboardPrivacyDeveloperPreview` user default has been removed.” |  | — | AppKit (adjacent) | T1 |  |
| MAC-375 | 27.2 | Display Settings | Known Issue | 188643179 | “When an external display is connected, display settings might not be restored correctly, and the display arrangement might change.” |  | — | — | T1 |  |
| MAC-376 | 27.2 | Notifications | Known Issue | 187312007 | “Mac computers with a clean install of this build might not prompt you to allow notifications for some apps, such as Calendar, …” |  | Go to System Settings > Notifications to manually turn on notifications for the affected apps. | — | T1 |  |
| MAC-377 | 27.2 | Shortcuts | Known Issue | 187499433 | “Describe a Shortcut might fail with the error “Something went wrong. Try again later.”” |  | — | — | T1 |  |
| MAC-378 | 27.2 | StoreKit Testing in Xcode | Resolved | 183933307 FB24137836 | “Fixed: Intro offer eligibility does not reset immediately after calling `SKTestSession.clearTransactions()`.” |  | — | — | T1 |  |
| MAC-379 | 27.2 | StoreKit Testing in Xcode | Resolved | 184155259 | “Fixed: Changing the storefront or locale using `SKTestSession` doesn’t propagate through `Storefront.updates`.” |  | — | — | T1 |  |
| MAC-380 | 27.2 | StoreKit Testing in Xcode | Resolved | 184255116 | “Fixed: Failed purchases using `SKTestSession` might display error dialogs even when `dialogsDisabled` is set to `true`.” |  | — | Windows/sheets/panels | T1 |  |
| MAC-381 | 27.2 | StoreKit Testing in Xcode | Known Issue | 186018916 | “Making a purchase in-app for a subscription that is a member of a subscription bundle incorrectly allows the user to unbundle instead …” |  | — | — | T1 |  |
| MAC-382 | 27.3 beta | DriverKit | New | 190089334 | “DriverKit 27.3 adds `IOUserSCSIParallelInterfaceController::UserCopyDataBuffer`, which supersedes the deprecated `UserGetDataBuffer` and has the same API interface. `UserCopyDataBuffer` returns the buffer at +1, so …” |  | — | — | T1 |  |
| MAC-383 | 27.3 beta | DriverKit | Deprecation | 184905119 FB24326124 | “`IOUserSCSIParallelInterfaceController::UserGetDataBuffer` is deprecated in DriverKit 27.3 because it leaks memory. Use `UserCopyDataBuffer` instead. `UserCopyDataBuffer` returns the buffer at +1, so you must …” |  | — | — | T1 |  |
| MAC-384 | 27.3 beta | mBoot | Resolved | 182898702 FB23916610 | “Fixed: Only a single core is available when you boot Linux or other third-party operating systems from a custom raw boot object …” |  | — | — | T1 |  |
| MAC-385 | 27.3 beta | NEURLFilter | New / behavior change | 187726173 | “The system now keeps a set of unused evaluation keys uploaded to your NEURLFilter PIR service, and when it runs out of …” |  | — | — | T1 |  |
| MAC-386 | 27.3 beta | NEURLFilter | Deprecation | 191651440 | “NEURLFilter no longer supports user tiers. The system no longer calls your service’s `/token-key-for-user-token` endpoint and instead uses the first valid public …” |  | — | — | T1 |  |
| MAC-387 | 27.3 beta | NEURLFilter | Deprecation | 191651462 | “NEURLFilter now limits a service’s PIR configuration to at most 65,536 shards and requires the shard count to be a power of …” |  | — | — | T1 |  |
| MAC-388 | 27.3 beta | NEURLFilter | Deprecation | 191651632 | “Your NEURLFilter service URL and Privacy Pass issuer URL must now be declared statically in your app’s Info.plist, and providing them only …” |  | — | — | T1 |  |
| MAC-389 | 27.3 beta | Rosetta | Deprecation | 180686443 | “macOS now notifies users when an audio plug-in or print dialog extension that requires Rosetta is used, and lists these plug-ins in …” |  | — | Windows/sheets/panels | T1 |  |
| MAC-390 | 27.3 beta | Rosetta | Deprecation | 188594616 | “macOS now notifies you when you print using a printer driver that requires Rosetta but is not yet updated for Apple silicon. …” |  | — | — | T1 |  |
| MAC-391 | 27.3 beta | SCSIControllerDriverKit | New / behavior change | 182426393 FB23797269 | “SCSIControllerDriverKit now supports software controllers. A software controller declares itself by setting `kIOPropertySoftwareIOKey` (an `OSBoolean`, from `<IOKit/storage/IOStorageControllerCharacteristics.h>`) through `UserSetHBAProperties()`. The system honors …” |  | — | — | T1 |  |
| MAC-392 | 27.3 beta | Siri | Known Issue | 191273925 | “On macOS, Siri cannot find app entities donated to Spotlight by third-party apps unless those entities conform to a schema.” |  | — | — | T1 |  |
| MAC-393 | 27.3 beta | Speech | Resolved | 187921017 FB24862729 | “Fixed: An assertion failure occurs when you use `CaptureInputSequenceProvider` in a “Mac (Designed for iPad)” target.” |  | — | — | T1 |  |
| MAC-394 | 27.3 beta | StoreKit | New | 164581840 | “Multiseat subscriptions let a customer purchase multiple seats for an auto-renewable subscription and invite others to join it. Check whether a subscription …” |  | — | — | T1 |  |
| MAC-395 | 27.3 beta | StoreKit Testing in Xcode | Resolved | 186018916 | “Fixed: Making an in-app purchase for a subscription that is a member of a subscription bundle incorrectly allows the user to unbundle …” |  | — | — | T1 |  |
| MAC-396 | 27.3 beta | StoreKit Testing in Xcode | Known Issue | 186670057 FB24651858 | “When you launch an app that uses `SKTestSession` for the first time, some StoreKit Test API calls might hang.” |  | Set a StoreKit configuration file in your scheme’s run options, then rerun the tests. | — | T1 |  |


### Inferences
- The menu-image change is the release's most likely source of accessibility regressions. On the 27 SDK, image-only `NSMenuItem`s are hidden automatically (MAC-140). An item with no title and no image may leave VoiceOver users with an empty or unlabeled item unless it has an accessibility label. This needs testing; Apple does not say how VoiceOver handles it.
- SwiftUI `Slider` and bordered `Menu`/`Picker` no longer use `NSSlider`/`NSPopUpButton` (MAC-301, MAC-311). Their AX roles, actions and keyboard handling are no longer inherited from AppKit and should be re-audited with VoiceOver, Full Keyboard Access and Voice Control. This is an inference; the notes say nothing about the AX impact.
- `NSTextView`'s move to gesture-recognizer-based selection (MAC-119) and exclusive gesture hit-testing (MAC-209) can change how custom NSTextView subclasses and hit-testing interact with assistive pointer input, such as Voice Control clicks and Dwell. That is worth regression testing.
- `NSClickGestureRecognizer` timing (MAC-134) is worded as a behavior change, not a fix, even though it sits under Resolved Issues.

### Gaps
- Apple's notes do not say whether `NSToolbarItemGroup.Role` changes VoiceOver output in toolbars. The VoiceOver "tabs" wording in MAC-118 is attached to the segmented-control `tabs` role.
- There are no release-note entries about VoiceOver, Voice Control, Zoom, Full Keyboard Access, captions, Increase Contrast or Reduce Transparency as features. Those consumer accessibility features are not in the developer release notes.

## Q2. What did 27.1 change?

### Takeaway
No macOS 27.1 release-notes page and no macOS 27.1 public release could be found on Apple's own sources. The macOS sequence is 27.0, then 27.0.1, then 27.2. The "27.1" items Apple did publish are Xcode 27.1 and a device-specific iOS 27.1. The Apple Support page "What's new in the updates for macOS Golden Gate 27" could not be found.

### Cited Findings
- MAC-397 (T1): the release-notes index JSON lists only `macos-27-release-notes`, `macos-27_2-release-notes` and `macos-27_3-release-notes` for the 27 cycle. Requesting `macos-27_1-release-notes.md` returns HTTP 404. — [macOS release-notes index](https://developer.apple.com/tutorials/data/documentation/macos-release-notes.json); [404 URL](https://developer.apple.com/documentation/macos-release-notes/macos-27_1-release-notes.md)
- MAC-398 (T1): Apple's security-releases table lists macOS Golden Gate 27 (14 Sep 2026), 27.0.1 (28 Sep 2026, "This update has no published CVE entries.") and 27.2 (26 Oct 2026). It has no macOS 27.1. The only "27.1" entry is "iOS 27.1", for iPhone Duo, on 23 Oct 2026. — [Apple security releases](https://support.apple.com/en-us/100100)
- MAC-399 (T1): the Developer Releases feed lists "Xcode 27.1 beta (27A9269)" on September 18, 2026 and "Xcode 27.1 (27A9275)" on October 15, 2026. It has no macOS 27.1 entry. — [Apple Developer Releases](https://developer.apple.com/news/releases/)
- MAC-400 (T1): Apple Support page 122868 is "What's new in the updates for macOS Tahoe 26" (26.7.2: "This update provides security fixes for your Mac."). It is not the Golden Gate page. — [support.apple.com/en-us/122868](https://support.apple.com/en-us/122868)
- MAC-401 (T2): an editorial source says 27.2 expanded Siri AI to French, Japanese, Korean, Portuguese and Spanish. This comes from search-result summaries and the article was not opened, so treat it as unverified. — [MacTrast, "Apple Releases macOS Golden Gate 27.2 to the Public"](https://www.mactrast.com/?p=173725)

### Inferences
- Apple seems to have skipped a macOS 27.1 version: it went 27.0.1 to 27.2, while iOS 27.1 was limited to one device. This is inferred from the release tables having no 27.1 entry. Apple does not state it.

### Gaps
- The Apple Support URL for "What's new in the updates for macOS Golden Gate 27" was not found. A web search turned up only editorial results. Without it, the 27.0.1 and 27.2 user-facing changes, including any accessibility fixes, are not documented here.
- The 27.0.1 release has no developer release notes. Its contents are unknown beyond "no published CVE entries".

## Q3. Exact release dates and builds

### Takeaway
macOS 27.0 shipped 14 Sep 2026. The build was not found on Apple's releases page. 27.0.1 (26A434) shipped 28 Sep 2026, 27.2 (26B123) shipped 26 Oct 2026, and the 27.3 beta (26C5035r) came out 3 Nov 2026.

### Cited Findings
- MAC-402 (T1), stable releases:
  - "macOS 27.0.1 (26A434)", September 28, 2026.
  - "macOS 27.2 (26B123)", October 26, 2026.
  - Xcode 27 (27A266a), September 14, 2026.
  - Xcode 27.2 (27B52), October 29, 2026.

  — [Apple Developer Releases](https://developer.apple.com/news/releases/)
- MAC-403 (T1), beta (kept separate): "macOS 27.3 beta (26C5035r)", November 3, 2026, alongside Xcode 27.3 beta (27C5020n). — [Apple Developer Releases](https://developer.apple.com/news/releases/)
- MAC-404 (T1): macOS Golden Gate 27 was released 14 Sep 2026. Supported Macs per the table: MacBook Neo (2026), and Apple-silicon MacBook Air, MacBook Pro, iMac, Mac mini, Mac Studio and Mac Pro. — [Apple security releases](https://support.apple.com/en-us/100100)
- (T2) Eclectic Light reports macOS Golden Gate was released on 2026-09-14. This matches MAC-404. — [Eclectic Light Co.](https://eclecticlight.co/2026/09/14/apple-has-released-macos-golden-gate-and-security-updates-to-tahoe-26-7-sequoia-15-8/)

### Inferences
- The macOS 27 build prefix is "26", as in 26A434, 26B123 and 26C5035r. That follows Darwin's major-version numbering, and Darwin 27.0.0 on this machine is consistent with it. Copy builds exactly as Apple shows them; do not "correct" them to 27x.

### Gaps
- No macOS 27.0 (GM) build number appears in the Developer Releases list. The 14 Sep entries show only tvOS, watchOS and Xcode. Check it against Apple's security-content page for "macOS Golden Gate 27", which was not opened.

## Q4. Which 27.0 known issues were resolved later (matched by issue number)?

### Takeaway
I matched issue numbers across the three captured pages programmatically. Two 27.0 known issues were resolved in 27.2: 184155259 and 184255116, both in StoreKit Testing. One 27.2 known issue was resolved in the 27.3 beta: 186018916. No accessibility or AppKit/SwiftUI known issue appears again as resolved.

### Cited Findings
- MAC-297 to MAC-379 (T1): 184155259, "Changing the storefront or locale using `SKTestSession` doesn't propagate through `Storefront.updates`." It is a Known Issue in 27.0 and Resolved in 27.2. — [27.0](https://developer.apple.com/documentation/macos-release-notes/macos-27-release-notes) StoreKit Testing in Xcode › Known Issues; [27.2](https://developer.apple.com/documentation/macos-release-notes/macos-27_2-release-notes) StoreKit Testing in Xcode › Resolved
- MAC-298 to MAC-380 (T1): 184255116, failed `SKTestSession` purchases show error dialogs even when `dialogsDisabled` is true. It is a Known Issue in 27.0 and Resolved in 27.2. Same sources.
- MAC-296 and MAC-378 (T1): 183933307, intro offer eligibility does not reset after `clearTransactions()`. It is already listed as Resolved in 27.0 and is repeated as Resolved in 27.2. Both pages carry FB24137836.
- MAC-381 to MAC-395 (T1, beta): 186018916, a purchase of a subscription-bundle member allows unbundling. It is a Known Issue in 27.2 and Resolved in the 27.3 beta. — [27.3 beta](https://developer.apple.com/documentation/macos-release-notes/macos-27_3-release-notes) StoreKit Testing › Resolved
- Still-open 27.0 known issues with no later resolution: 177198033, 181800016, 183770678, 184660124, 180040003, 183044008, 166068090, 168315587, 171728298, 176299524, 176812955, 177116121, 177376984, 177984074, 166640903 and 158441261 (SwiftUI document progress).

### Inferences
- The 27.0 page is a cumulative beta log. Many beta-era known issues were turned into "Fixed:" items before release, so you cannot reconstruct which issues were open in beta N from the final page.

### Gaps
- New 27.2 known issues that are not yet resolved: 188643179 (display arrangement), 187312007 (notification prompts, workaround available) and 187499433 (Describe a Shortcut). The 27.3 beta page does not address them.

## Q5. AppKit and SwiftUI-for-Mac accessibility API additions in WWDC26 sessions

### Takeaway
WWDC26 has no "What's new in AppKit" session. The macOS AppKit session is **"Modernize your AppKit app" (session 289)**. It covers keyboard navigation (key view loop, status-item keyboard navigation and the new `NSStatusItem` expanded-interface-session API), `NSTextSelectionManager`, and Liquid Glass changes in macOS 27. It does not cover new NSAccessibility protocol APIs. Apple's DocC "Accessibility updates" page has no June 2026 section.

### Cited Findings
- MAC-405 (T1, DocC; all fetched 2026-11-05), with `introducedAt` values from the `platforms` metadata:
  - `NSRefreshController` macOS 27.0
  - `NSTextSelectionManager` 27.0
  - `NSSegmentedControl.role` and `NSSegmentedControl.Role` 27.0 (cases automatic, tabs, valueSelection)
  - `NSToolbarItemGroup.Role` iOS, iPadOS, Mac Catalyst and macOS 27.0
  - `NSMenuItem.preferredImageVisibility` 27.0
  - `NSScrollView.refreshController` 27.0
  - `NSScrollView.scrollGestureForRelationships` 27.0
  - `NSScrollView.minimumNumberOfTouchesForScrolling` 27.0
  - `NSGestureRecognizer.isCancellableByScrollGesture` 27.0
  - `NSView.exclusiveGestureBehavior` 27.0
  - `NSStatusItem.expandedInterfaceSession` 27.0
  - `NSApplication.PresentationOptions.disableScreenCornerInteractions` 27.0
  - SwiftUI `TabsPickerStyle` 27.0 (iOS, iPadOS, Catalyst, macOS, tvOS, visionOS)
  - SwiftUI `TextInputBorderShape` 27.0 (all platforms including watchOS)

  — e.g. [NSSegmentedControl.Role](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/role-swift.enum), [NSGestureRecognizer.isCancellableByScrollGesture](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/iscancellablebyscrollgesture), [NSScrollView.scrollGestureForRelationships](https://developer.apple.com/documentation/appkit/nsscrollview/scrollgestureforrelationships), [NSStatusItem.expandedInterfaceSession](https://developer.apple.com/documentation/appkit/nsstatusitem/expandedinterfacesession), [TabsPickerStyle](https://developer.apple.com/documentation/swiftui/tabspickerstyle)
- MAC-406 (T1): the June 2026 section of the AppKit updates page lists these:
  - the new `Events` type on `NSControl`, which works like UIControl events
  - `NSView.beginDraggingSession(items:gesture:source:)`
  - gesture recognizers for Sidecar iPad touch (TN3212)
  - `NSRefreshController`
  - SwiftUI `GestureInputKinds`
  - the Info.plist keys `NSViewGestureRecognizerIsExclusive`, `NSIsTouchNative` and `NSGestureRecognizerSuppressesMainMenuActions`

  Symbol availability for `Events`, `beginDraggingSession(items:gesture:source:)` and `GestureInputKinds` is **pending**; their DocC pages were not checked. — [AppKit updates](https://developer.apple.com/documentation/updates/appkit)
- MAC-407 (T1): the Accessibility updates page's newest section is "June 2025". It has no June 2026 entries. — [Accessibility updates](https://developer.apple.com/documentation/updates/accessibility)
- MAC-408 (T1), WWDC26 session 289 "Modernize your AppKit app" — [video page](https://developer.apple.com/videos/play/wwdc2026/289/):
  - 3:52–4:13: "use NSTextSelectionManager. It's a new API in macOS 27".
  - 5:51–6:29: keyboard navigation "to enable speed and accessibility". Enable `.autorecalculatesKeyViewLoop`, or else "you are in charge of creating and maintaining the key view loop."
  - 6:34–8:22: keyboard navigation reaches the menu bar and status items. An `NSStatusItem` button with a target and action fires on Return. Custom status-item windows should use the expanded interface session API (`statusItem didBegin ExpandedInterfaceSession` / `DidEnd`, `.cancel`) "so that keyboard focus can behave correctly."
  - 14:31–14:56: the automatic `NSScrollEdgeEffectStyle` resolves to a hard edge behind free-floating text. Sidebar selection uses semibold text. Bordered toolbar items over the sidebar adopt Liquid Glass.
  - 15:01–15:24: a new glass "bounce on click" effect, for use with controls only.
- MAC-409 (T1): WWDC26 session 230 "What's new in assessment on macOS", 3:00–3:30. It covers "managing the availability of accessibility features" during exams. By default the Menu Bar and Dock are hidden, but enabled accessibility features stay available (the sentence is cut at 3:30). — [video page](https://developer.apple.com/videos/play/wwdc2026/230/)
- MAC-410 (T1): WWDC26 session 269 "What's new in SwiftUI":
  - 2:35–2:47: on macOS, Liquid Glass custom elements can be marked "interactive" and are tuned for the mouse pointer.
  - 3:32–3:46: Mac menu bars "now have a minimal set of icons by default". Use `labelStyle(.titleAndIcon)` to show an icon.
  - 3:24: `appearsActive` can be used to reduce opacity in inactive windows.

  — [video page](https://developer.apple.com/videos/play/wwdc2026/269/)
- MAC-411 (T1): other WWDC26 sessions that touch Mac accessibility include:
  - 220 "Refine accessibility for custom controls" (`.adjustable` trait at 5:37, `accessibilityAdjustableAction` at 5:47, custom actions at 9:53). Not macOS-specific in what I reviewed.
  - 219 "Enhance the accessibility of your reading app".
  - 370 "Elevate your app's text experience with TextKit" (covers NSTextView alongside UITextView and TextEditor).
  - 272 "Use SwiftUI with AppKit and UIKit" (menu bar extra in an AppKit app at 11:42; keyboard shortcut in an NSMenu at 9:29–10:05).
  - 8005 "Accessibility Technologies Group Lab".

  — [WWDC26 video index](https://developer.apple.com/videos/wwdc2026/)

### Inferences
- In macOS 27, most accessibility-relevant API work is semantic (the `tabs` roles) or about input (gestures, text selection, status-item keyboard focus). There are no new `NSAccessibility` protocol members. This is inferred from the AppKit and Accessibility updates pages and the session transcripts, not from a full diff of the NSAccessibility symbols.
- The names in the release notes do not match DocC for two APIs (`cancellableByScrollGesture` vs `isCancellableByScrollGesture`; `scrollGestureForFailureRelationship` vs `scrollGestureForRelationships`). Use the DocC names in any guidance.

### Gaps
- No full NSAccessibility symbol diff was done. Whether any `NSAccessibility*` symbol has `introducedAt` 27.0 is **pending**.
- `NSToolbarItemGroup.role` (property) and `NSSegmentedControl.role` (property) were confirmed via `role-swift.property` / `role-swift.enum`. `NSToolbarItemGroup.role-swift.property` itself was not fetched, so its availability is pending.
- Transcripts for sessions 219, 370 and 8005 were not reviewed fully for macOS-specific accessibility API claims.
