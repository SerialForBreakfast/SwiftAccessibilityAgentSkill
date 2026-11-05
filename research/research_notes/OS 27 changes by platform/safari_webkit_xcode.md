# Safari 27.x / WebKit and Xcode 27.x: accessibility changes and accessibility developer tooling (OS 27 cycle)

Snapshot date: 2026-11-05. Betas are kept separate from shipped releases (Safari 27.3 and Xcode 27.3 are betas).

**Evidence tiers used below**
- **T1**: Apple primary documentation (release notes, API reference JSON) or a WebKit team post on webkit.org/blog (Tier-1 for engine behavior).
- **T2**: Apple WWDC26 session video transcript (primary, but spoken and less precise than release notes).
- **T3**: WWDC26 Group Lab Q&A transcript (informal, conversational answers from Apple staff).

**Source snapshot record** (fetched 2026-11-05 with curl from the `.md` endpoints; IDs in parentheses in the notes are Apple radar/issue numbers, not WebKit Bugzilla IDs)

| Source | URL | Bytes | SHA-256 |
|---|---|---|---|
| Safari 27 RN (released Sep 14, 2026, 27.0 / 20625.1.29) | https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes.md | 117412 | 7762b476ff0f2a477ae6f4dd84a60b90955a6b19aee9add1b7aab9cd8f5ea844 |
| Safari 27.1 RN (released Oct 23, 2026; iOS 27.1 only) | https://developer.apple.com/documentation/safari-release-notes/safari-27_1-release-notes.md | 1870 | 4bc3f74bd4304322ec3962d3b713cdf3d663abeb5587f91d6bdfd1a6983021d9 |
| Safari 27.2 RN (released Oct 26, 2026, 20625.2.8) | https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes.md | 5322 | 835edb5f8e916985942eaf05228d6c60539f7e8f5bad35eb5fcbf721c17b07d9 |
| Safari 27.3 **Beta** RN (Nov 3, 2026, 20626.1.12) | https://developer.apple.com/documentation/safari-release-notes/safari-27_3-release-notes.md | 64306 | 9edb941f876ee6c1044ba995fca18da5b76389f42daa057ebc162ebd0a3e59b5 |
| Xcode 27 RN | https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes.md | 67593 | 318463d4d177c63b21d3d101e1b6b0e3d3b0e317d83520162dc645ab3771d8f2 |
| Xcode 27.1 RN | https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes.md | 2210 | 558b04372b51f995348fb966327a40690ad80e29d758b280980a12b77a17afd1 |
| Xcode 27.2 RN | https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes.md | 7778 | dfca14a3f276af6a6380c36bd47ad94e8ffe862bfcf4ca1761c5a4b3a15e1c57 |
| Xcode 27.3 **Beta** RN | https://developer.apple.com/documentation/xcode-release-notes/xcode-27_3-release-notes.md | 3878 | 0e0e89abf984171bf5ea39e42d236f57370ffdc5831badab09b8fde24b05e382 |

Index files used to discover these pages: https://developer.apple.com/tutorials/data/documentation/safari-release-notes.json and https://developer.apple.com/tutorials/data/documentation/xcode-release-notes.json. Each lists exactly four 27.x pages (27, 27_1, 27_2, 27_3), with the release dates and build numbers shown above.

---

## Q1: Which Safari 27.x release notes exist, and what accessibility entries does each contain?

### Takeaway
Four Safari 27.x notes exist: 27.0, 27.1, 27.2 and 27.3 beta. 27.0 adds one accessibility feature, the `ariaNotify` API, and lists 32 Accessibility fixes. 27.1 has no accessibility entries. 27.2 has 2 Accessibility fixes, and the 27.3 beta has 13. Many more accessibility-relevant changes sit in other sections: focus and `:focus-visible`, dialog focus, forms, WebVTT and captions, Web Inspector contrast tools, and the `:heading` and `headingoffset` features. The notes cite Apple radar IDs, not WebKit Bugzilla numbers. I found no reduced-motion entries.

### Cited Findings

**Safari 27.0: Accessibility > New Features** ([Safari 27 RN](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes), § Accessibility, .md L24)
- **WEB-101** [T1] Added the `ariaNotify` API, described as "allowing web developers to programmatically make screen reader announcements." (166338108). Source: [Safari 27 RN](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes) § Accessibility/New Features.

**Safari 27.0: Accessibility > Resolved Issues** (all from [Safari 27 RN](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes) § Accessibility/Resolved Issues, .md L26–59; T1)
- **WEB-102** `speechSynthesis.cancel()` no longer removes utterances queued by later `speak()` calls (46151521).
- **WEB-103** SVG `<use>`→`<symbol>` inside `<img>` no longer shows up as unnamed images in VoiceOver's Images rotor (98999595).
- **WEB-104** Changing the `id` of an element targeted by `aria-owns` now updates the accessibility tree (107644248).
- **WEB-105** A `<slot>` referenced by `aria-labelledby` now uses its slotted content for the name and ignores hidden slotted nodes (114500560).
- **WEB-106** `<meter>` labels are now consistent between `aria-label` and `title` (127460695).
- **WEB-107** `display: contents` elements with shadow-root content are now read when referenced by `aria-labelledby` (129361833).
- **WEB-108** `aria-labelledby` now uses the checkbox name, not its value, when the name comes from a `<label>` (141564913).
- **WEB-109** The VoiceOver cursor is now positioned correctly for elements focused via canvas `drawFocusIfNeeded()` (146323788).
- **WEB-110** Grids whose child rows are in a shadow root now work with VoiceOver (153134654).
- **WEB-111** VoiceOver no longer reads text inside images with `role="presentation"` (159304061).
- **WEB-112** Content in dynamically expanded `<details>` is now exposed in the accessibility tree (159865815).
- **WEB-113** `contextmenu` now fires inside iframes when triggered by keyboard or AT, for example VO+Shift+M (164128676).
- **WEB-114** Changes to `<input type="button">` inside live regions are now announced (168200460).
- **WEB-115** `::first-letter` text is now exposed in the accessibility tree when it stands alone (168458291).
- **WEB-116** VoiceOver can now reach `aria-owns`'d rows and cells in grids and tables (168770938).
- **WEB-117** VoiceOver next/previous form-control navigation now finds focusable splitters (170187464).
- **WEB-118** Color picker inputs can now be activated with VoiceOver's press action (172218114).
- **WEB-119** Interactive elements containing an `<svg>` named by a child `<title>` now expose an accessible name (172559238).
- **WEB-120** Bounding boxes for MathML table rows and cells are now computed correctly (172851295).
- **WEB-121** Comboboxes now forward focus to `aria-activedescendant`, so AT can interact with list items (172931277).
- **WEB-122** VoiceOver can now navigate to content revealed by `hidden="until-found"` disclosure widgets (173228707).
- **WEB-123** `aria-owns` is now respected when computing a name from content (173249317).
- **WEB-124** VoiceOver line-by-line reading no longer skips content in read-only documents (174349841).
- **WEB-125** `aria-hidden="true"` is now invalidated correctly when focus lands inside the hidden subtree (174449524).
- **WEB-126** VoiceOver's "Skip redundant labels" setting is now respected on certain pages (176297111).
- **WEB-127** VoiceOver now follows `focus()` calls on newly added elements (177167634).
- **WEB-128** Role computation is fixed for elements with prefixes (178399441).
- **WEB-129** VoiceOver no longer jumps to the top of the page when the target element immediately becomes accessibility-ignored via JS (179065364).
- **WEB-130** Site-specific fix: VoiceOver no longer reports the parks.wa.gov Recent Events table as empty (179156593).
- **WEB-131** An `<a>` with a click handler but no `href` is now exposed as a link (179398579).
- **WEB-132** VoiceOver now announces the selected state of the day-of-month button in a monthly-notification UI (180294912).
- **WEB-133** `aria-labelledby` no longer goes stale when the referenced element changes its `aria-label` (180319221).

**Safari 27.0: accessibility-relevant entries in other sections** ([Safari 27 RN](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes); T1)
- **WEB-134** CSS: added the `:heading` pseudo-class (158759228). Locator: § CSS/New Features, .md L80.
- **WEB-135** CSS focus fixes: `:focus-visible` no longer matches wrongly after programmatic `focus()` from a click on a button with children (134337357). `:active`, `:focus-within` and `:hover` now account for the top layer (173145294). The SVG and MathML UA sheets now use `:focus-visible` instead of `:focus` (173321368). Programmatic focus after keyboard interaction now matches `:focus-visible` (177850766). `outline: auto` now respects zoom (173068660). Locator: § CSS/Resolved Issues (.md ~L115–259).
- **WEB-136** Forms: added customizable `<select>` (`appearance: base-select`, `<selectedcontent>`) (170328089). Locator: § Forms/New Features, .md L350.
- **WEB-137** Forms fixes: tab position is kept when a focused button becomes disabled; previously focus jumped to the top of the page (120676409). Keyboard paste now works in numeric-restricted fields (4360235). Range-slider thumbs get a larger touch hit area on iPadOS and visionOS (147428926). `<datalist>` no longer shows white-on-white in dark mode (168676757). Base-select default styles were fixed, including "increased contrast colors" (183345556). Locator: § Forms/Resolved Issues, .md L352–374.
- **WEB-138** HTML: added `tabindex`, `focus()`, `blur()` and `autofocus` on MathML elements (176258900). Sequential focus navigation now skips elements that don't meet the focusability requirements (103370883). Popover light dismiss now accounts for input buttons and disabled command buttons (171352032, 171358576). Locator: § HTML, .md L382, L388, L395–396. Also MathML `tabIndex` values fixed (174734133), .md L508.
- **WEB-139** SVG: added `lang` and `xml:lang` support in SVG (143751056). Locator: § SVG/New Features, .md L758.
- **WEB-140** Media, captions and WebVTT: `TextTrackCue.endTime` can now be `Infinity` (71042767). WebVTT no longer displays cues larger than the viewport (136809012). Autoplay waits for default text tracks to load (171699293). NULL is allowed in `VTTCue` text (175084171). WebVTT cue-settings line parsing is fixed (175296476). Subtitles and closed captions now appear in fullscreen video on iOS (175298523). `<audio controls>` hides "Subtitles" when there is no track (175357130). `::cue()` now matches the WebVTT root object (175550173). Locator: § Media (.md L515–586).
- **WEB-141** Scrolling: scroll anchoring is enabled (171840378). Locator: § Scrolling/New Features, .md L841. Per the 27.0 blog, it is controlled by `overflow-anchor` ([WebKit blog 27.0](https://webkit.org/blog/18325/webkit-features-for-safari-27-0/), § Scroll Anchoring).
- **WEB-142** Web Inspector: added color contrast information in the Color Picker (113887185), including when editing background colors (171332734). The Accessibility sidebar is no longer empty for nodes in cross-origin iframes (178562336). Locator: § Web Inspector, .md L1070, L1073, L1116.
- **WEB-143** WebDriver: added the Safari MCP server so agents can connect to Safari (176038457). Locator: § WebDriver/New Features, .md L1162.

**Safari 27.1** ([Safari 27.1 RN](https://developer.apple.com/documentation/safari-release-notes/safari-27_1-release-notes); T1)
- **WEB-144** The only sections are PDF and Web API. They cover foldable book-pose PDF (170353889), the Device Posture API (170005463) and the Viewport Segments API (176426722), the last two behind a feature flag. There are no accessibility entries. Available for iOS 27.1 only.

**Safari 27.2: Accessibility > Resolved Issues** ([Safari 27.2 RN](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes) § Accessibility, .md L20–25; T1)
- **WEB-145** VoiceOver no longer repeats already-announced text when a page streams content by re-rendering an `aria-live` region instead of appending to it (186766347).
- **WEB-146** VoiceOver on iOS now identifies date, time and color inputs as pop-up buttons (187788949).
- **WEB-147** Other 27.2 entries relevant to accessibility: Safari no longer takes keyboard focus from other apps when under Safari MCP control (182558329), § Safari MCP. An anchor-positioned element inside a modal `<dialog>` no longer goes offscreen (187933878), § CSS. Base-select gets `::field-content` and alignment and `text-overflow` changes (187617020), § Forms. `flow-tolerance` is renamed `fit-tolerance` for grid-lanes (185816680), § CSS Deprecations. The WebKit 27.2 post ties this property to keyboard focus order (see WEB-162).

**Safari 27.3 beta (BETA): Accessibility > Resolved Issues** ([Safari 27.3 Beta RN](https://developer.apple.com/documentation/safari-release-notes/safari-27_3-release-notes) § Accessibility, .md L20–36; T1)
- **WEB-148** The accessible name of a `display: contents` element no longer includes sibling text (185108892).
- **WEB-149** List-marker text is excluded when a name or value is requested without markers (185422271).
- **WEB-150** List, table, tree and canvas content is no longer omitted from the name or description when the container is referenced by `aria-labelledby` or `aria-describedby` (186015032). **Conflict:** the WebKit "Features for Safari 27.2" post lists this same radar under 27.2 Accessibility ([WebKit blog 27.2](https://webkit.org/blog/18515/webkit-features-for-safari-27-2/), § Accessibility), while the Apple 27.2 release notes do not.
- **WEB-151** VoiceOver now speaks `aria-keyshortcuts` `Meta` and `Alt` as Command and Option (186342070).
- **WEB-152** The list marker is now present in the accessibility text of list items with block content (186687365).
- **WEB-153** VoiceOver on iOS no longer auto-expands `<select>` and date pickers after a swipe from a text field (187789276).
- **WEB-154** VoiceOver no longer announces every focused ARIA menu item as "selected" (188921930).
- **WEB-155** VoiceOver can now press buttons with `pointer-events: none` (188980125).
- **WEB-156** VoiceOver activation now dispatches `click` with a non-zero `detail` plus pointer events, mimicking a mouse click (189417259).
- **WEB-157** Text hidden with `clip` plus `overflow: hidden` is no longer exposed in the accessibility tree (189824370).
- **WEB-158** VoiceOver can now reach an `<iframe>` nested inside an iframe with `role="none"` or `role="presentation"` (190043178).
- **WEB-159** `::marker` `content` is now exposed in the accessibility tree (190150062).
- **WEB-160** VoiceOver on iOS no longer dispatches duplicate `pointerdown` events (191127608).

**Safari 27.3 beta (BETA): accessibility-relevant entries in other sections** ([Safari 27.3 Beta RN](https://developer.apple.com/documentation/safari-release-notes/safari-27_3-release-notes); T1)
- **WEB-161** HTML new features: `headingoffset` and `headingreset` attributes (182180043), `popover=hint` (184548373), and the viewport `interactive-widget` key for on-screen-keyboard behavior (184654901). § HTML/New Features, .md L262–265.
- **WEB-161a** Dialog and focus fixes: focus is restored to the correct element when a `<dialog>` closes (184751412). `show()` now moves focus (185156091). `close()` no longer restores focus when focus wasn't inside a non-modal dialog (185549474). `documentElement.focus()` now moves focus to the viewport (185567540). A color input with `display:none` now opens via its `<label>` (100476630). § HTML/Resolved Issues, .md L268–278. Web API: close watchers and `closedby` for `dialog` (180105698), § Web API/New Features, .md L559.
- **WEB-161b** CSS: `:focus-visible` is no longer shown after `focus()` inside an already-focused ancestor (181570771). New features include `outline-offset: inset` (180547604), `content` on `::marker` (182750380) and unprefixed `user-select` (184964807). § CSS (.md L71–117).
- **WEB-161c** Forms: a disabled `<option>` can no longer be chosen by access key (189042890). Base-select supports press-drag-release picking (188830823). `<optgroup>` labels now use only a first-child `<legend>` (189042427). § Forms/Resolved Issues, .md L239–256.
- **WEB-161d** Media and captions: added `HTMLMediaElement.removeTextTrack()` (183365541). Find-in-text now resolves to the caption cue nearest the playhead (182001231). The auto position of WebVTT `start`/`end`-aligned cues is now 50% (184039946). § Media, .md L351–364.
- **WEB-161e** Web Inspector (27.3 beta): no accessibility-specific entries in the New Features or Resolved Issues lists (.md L623–660). The entries are network throttling, canvas and WebGPU tools, layout-invalidation events, quirks logging, and a fix for Find in Page in Responsive Design Mode (158871569).

**Reduced motion**
- A keyword scan of all four Safari 27.x notes for `prefers-reduced-motion` and "reduce motion" found no entries. The only `prefers-*` items are `prefers-color-scheme` iframe and SVG fixes in 27.0 (142072593, 172229372, 176413340). Source: [Safari 27 RN](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes) § CSS/Rendering/SVG. T1, negative finding.

### Inferences
- Safari 27.0 is a large accessibility-quality release: 32 fixes in the Accessibility section alone, plus focus and dialog fixes elsewhere. Most target accessible-name computation (`aria-labelledby`/`aria-owns`/shadow DOM/`display: contents`) and VoiceOver navigation. The 27.3 beta continues the same themes: name computation, list markers, and VoiceOver event synthesis.
- WEB-156 and WEB-160 (27.3 beta) change the events web content sees on VoiceOver activation. Sites that detect AT through `event.detail === 0` would behave differently. This is unverified until 27.3 ships.
- The 186015032 placement conflict (WEB-150) suggests either the blog post or the release notes is wrong about which version shipped the fix. Treat its ship version as uncertain until Safari 27.3 final notes exist.

### Gaps
- **WebKit Bugzilla numbers:** neither the Apple release notes nor the WebKit "Features for Safari 27.x" posts give bugs.webkit.org IDs. All IDs are Apple radar numbers. The feeds contain only a generic link to https://bugs.webkit.org/. Mapping radars to Bugzilla would need per-commit searches in the WebKit repo, which were not done here.
- No Safari 27.x note mentions ARIA 1.3 attribute additions, new ARIA roles, or reduced-motion behavior beyond what is listed.
- No Web Inspector "accessibility audit" feature changes were found in 27.x notes beyond WEB-142.

---

## Q2: What did the WebKit blog publish about Safari 27 features and accessibility?

### Takeaway
WebKit published a WWDC26 beta announcement, a sessions roundup, "Features for Safari 27.0/27.1/27.2" posts, a Customizable Select accessibility post ("golden rule"), a Safari MCP introduction that includes accessibility checking, and "Introducing Adaptive Dark Mode", which discusses WCAG contrast. The 27.0 feature post repeats the 32 accessibility fixes but does not mention `ariaNotify`. No "Features for Safari 27.3" post exists yet, because 27.3 is in beta.

### Cited Findings
- **WEB-162** [T1] The WebKit 27.2 post summarizes the release as "20 bug fixes across accessibility, media, CSS, and more". It frames grid-lanes tolerance as aiding focus order for "sighted keyboard users, who watch focus move from item to item." Its Accessibility list includes 186015032, 186766347 and 187788949. Source: [WebKit Features for Safari 27.2](https://webkit.org/blog/18515/webkit-features-for-safari-27-2/) (Oct 26, 2026), intro and § Accessibility.
- **WEB-163** [T1] The WebKit 27.0 post (Sep 17, 2026) has an Accessibility resolved-issues list mirroring the release notes, and a Web Inspector section on inline Color Picker contrast information. It also says SVG `lang`/`xml:lang` ensures correct "accessibility announcements", and that MathML focus support "supports interactive educational content and accessibility." Source: [WebKit Features for Safari 27.0](https://webkit.org/blog/18325/webkit-features-for-safari-27-0/), § Web Inspector, § SVG, § MathML, § Accessibility.
- **WEB-164** [T1] The 27.0 post does not mention `ariaNotify` (zero matches in the post text). The release notes list it as the sole Accessibility new feature (WEB-101). Sources: [WebKit 27.0 post](https://webkit.org/blog/18325/webkit-features-for-safari-27-0/), full-text search; [Safari 27 RN](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes) § Accessibility/New Features.
- **WEB-165** [T1] Safari MCP: the 27.0 post lists among agent capabilities "test for accessibility issues like missing labels, improper ARIA attributes, and poor contrast". The setup command is `claude mcp add safari-mcp -- "/usr/bin/safaridriver" --mcp`. Sources: [WebKit 27.0 post](https://webkit.org/blog/18325/webkit-features-for-safari-27-0/), § Safari MCP; [Introducing the Safari MCP server for web developers](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/) (Jul 1, 2026), "Check for accessibility" paragraph.
- **WEB-166** [T1] The WWDC26 beta post (Jun 8, 2026) counts "58 new features, 525 fixes and 4 deprecations". It says customizable `<select>` keeps "keyboard navigation, screen reader support, form submission, validation". Source: [News from WWDC26: WebKit in Safari 27 beta](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/), intro and § Customizable Select.
- **WEB-167** [T1] "The golden rule of Customizable Select" (Jun 15, 2026) gives one rule: "always provide text content or accessible text attributes for your option elements." It explains the screen reader and braille consequences of icon-only options and recommends visually-hidden text or `alt`/`aria-label`. Source: [The golden rule of Customizable Select](https://webkit.org/blog/18117/the-golden-rule-of-customizable-select/), intro and § Better accessibility.
- **WEB-168** [T1] "Introducing Adaptive Dark Mode" (Nov 3, 2026) says the transform aims for "sufficient contrast as defined by the WCAG 4.5:1 contrast ratio" for text, inspects SVG icons, and analyzes bitmaps. Source: [Introducing Adaptive Dark Mode](https://webkit.org/blog/18541/introducing-adaptive-dark-mode/), color-matrix paragraph.
- **WEB-169** [T1] The WWDC26 sessions roundup notes that Grid Lanes `flow-tolerance` controls drift from source order, "an important consideration for accessibility". Source: [Web Technology Sessions at WWDC26](https://webkit.org/blog/17974/web-technology-sessions-at-wwdc26/), § Grid Lanes.
- **WEB-170** [T1] The 27.1 post covers iPhone Duo and foldable viewport and posture. It has no accessibility content (keyword scan). Source: [WebKit Features for Safari 27.1](https://webkit.org/blog/18486/webkit-features-for-safari-27-1/).

### Inferences
- The WebKit team's public framing of Safari 27 accessibility centers on quality fixes and on keeping native semantics in customizable `<select>`, not on new ARIA features. `ariaNotify` is documented only in Apple's release notes.

### Gaps
- No webkit.org post dedicated to `ariaNotify` or to Safari 27 accessibility in general was found in the feed pages scanned (pages 1–2, back to Feb 2026).
- Safari Technology Preview posts (252–256) were not mined for accessibility entries, since they are pre-release and outside the 27.x scope.

---

## Q3: What do the Xcode 27.0–27.3 release notes say about accessibility tooling, audits, Accessibility Inspector, simulator, previews, availability, Device Hub and the coding assistant?

### Takeaway
Xcode 27.0 adds **XCUIVoiceOverService**, a UI-testing API that drives VoiceOver and checks focus and speech. It also adds an Apple-built **accessibility specialist** for agents, Contrast and Control Borders preview overrides, and Preview Snapshot type-size variants. It fixes "Accessibility Inspector cannot inspect elements in simulators" and Device Hub's VoiceOver, Text Size and Color Filter controls. 27.1 adds a Display preview override. 27.2 documents a known issue: VoiceOver and Accessibility Inspector cannot convey iPhone Duo content in Device Hub. 27.3 beta adds Swift Testing UI tests with XCUIAutomation. No 27.x note mentions `performAccessibilityAudit` or Swift 6.4 availability-checking changes.

### Cited Findings

**Xcode 27.0** ([Xcode 27 RN](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes); T1). Overview: it includes Swift 6.4 and the 27 SDKs and requires macOS Tahoe 26.6 or later (.md L18–20).
- **XCODE-101** Testing: "XCTest now includes XCUIVoiceOverService, a new UI testing API for verifying VoiceOver behavior in your app." It drives VoiceOver and validates focus, spoken output and navigation (175858549). § Testing/New Features, .md L1090.
- **XCODE-102** [T1] API reference: `XCUIVoiceOverService` lives in the XCUIAutomation framework, available iOS/iPadOS/Mac Catalyst/macOS/tvOS/visionOS/watchOS 27.0. Members include `enable()`, `disable()`, `isEnabled`, `moveForward()`, `moveBackward()`, `moveIn()`, `moveOut()`, `currentSpeech()`, plus `Output` and `Error` types. Source: [XCUIVoiceOverService doc](https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice) (JSON: https://developer.apple.com/tutorials/data/documentation/xcuiautomation/xcuivoiceoverservice.json, `metadata.platforms`, `topicSections`). The equivalent `/documentation/xctest/xcuivoiceoverservice` path returned 404.
- **XCODE-103** [T1] `performAccessibilityAudit(for:_:)` is now documented under XCUIAutomation (iOS 17.0, macOS 14.0, watchOS 10.0, tvOS 17.0). No Xcode 27.x release note mentions audit changes. Sources: [performAccessibilityAudit doc](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/performaccessibilityaudit(for:_:)) (JSON `metadata.platforms`); keyword search "audit" across all four Xcode 27.x notes finds only the security skill (XCODE-120).
- **XCODE-104** Testing: a launch-test file template that opts into `runsForEachTargetApplicationUIConfiguration` runs across orientation, localization and appearance combinations (168770106). Test Plans gain UI-test crash severity levels (168107814). XCTest/Swift Testing cross-framework assertion warnings (170335449). § Testing/New Features, .md L1076–1089.
- **XCODE-105** Simulator: "Fixed: Accessibility Inspector cannot inspect elements in simulators." (179033881) (FB22976268). § Simulator/Resolved Issues, .md L899. Simulator runtimes now ship a pre-built dyld cache. `simctl` and `devicectl` gain a reboot command (§ Simulator/New Features, .md L884–886).
- **XCODE-106** Device Hub resolved issues: the VoiceOver toggle in the appearance settings inspector now enables VoiceOver on the device (173507341). "Text Size" no longer disappears when an Accessibility larger text size is in use (175365925). The Color Filter option now works for simulators (178854926). Simulate Hardware Keyboard is fixed (178196115). § Device Hub/Resolved Issues, .md L315–329.
- **XCODE-107** Device Hub known issues (27.0): a color filter set on a physical device is not visible in Device Hub (178121876). Toggle Software Keyboard doesn't work on iOS 27.0 iPad sims (178432770). Keyboard and mouse input isn't accepted for pre-iOS 18, tvOS 18, watchOS 11 and visionOS 2 sims (181945323). Two-finger touch isn't supported. Parallel-testing simulators may not be visible. § Device Hub/Known Issues, .md L369–416. Deprecation: keyboard and pointer input only on macOS 15, iOS 18, tvOS 18, watchOS 11 and visionOS 2 or later (160482487), .md L420.
- **XCODE-108** Device Hub new features: Mac mouse and trackpad gestures now drive standard UIKit components, emitting `UIEvent.EventType.scroll`/`.transform` (§ Device Hub/New Features, .md L300). Network pairing for iOS/iPadOS/watchOS 27 devices (.md L302–306).
- **XCODE-109** Previews: the canvas overrides picker adds a **Color Scheme Contrast** group (standard or increased contrast) (181612731) and a **Control Borders** group (shown or hidden) (181850835). Also new: `#Preview(arguments:)` grids (167544057), a Resizable Canvas (171013421) and localization previews (181040291). § Previews/New Features, .md L759–776. `PreviewProvider` and its modifiers are deprecated (144168701), .md L819.
- **XCODE-110** Previews fix: keyboard input is now delivered to iOS-Simulator previews (177679215). `#Preview` code now runs on the main actor. § Previews/Resolved Issues, .md L788–792.
- **XCODE-111** Coding Intelligence: "Xcode now ships with Apple-built specialists for targeted tasks, like localization, UIKit resizing and accessibility." (178289150). § Coding Intelligence/New Features, .md L172.
- **XCODE-112** Coding Intelligence: the Preview Snapshot MCP tool renders variants such as light/dark, orientation and "various type size overrides" (172961797), and returns the simulator platform, device and OS (177076406). Agents can boot simulators, install and launch apps, synthesize touches and screenshot (175179787). § Coding Intelligence, .md L156–166.
- **XCODE-113** Coding Intelligence: agents can verify tvOS apps by moving focus with the Siri Remote (183317784) and verify watchOS apps through the Digital Crown and buttons (181147968). .md L210, L222.
- **XCODE-114** Coding Intelligence, accessibility fixes in Xcode's own UI: prompt-area buttons have "more accessible labels and descriptions" (177462284), and VoiceOver no longer gets trapped in the Coding Assistant prompt area (177462397). § Coding Intelligence/Resolved Issues, .md L227–229.
- **XCODE-115** Coding Intelligence (other): plugins with skills, MCP servers and ACP agents. Agent Client Protocol support. A filesystem-access security layer. Gemini and Antigravity providers. A beta-5 preview of `xcrun mcp-server`, which works without an open workspace. § Coding Intelligence, .md L150–222.
- **XCODE-116** Swift: the Swift Compiler section has one new feature, dependency-scanner optimization requiring unique Clang module names (136303612), and one known issue, an SE-0508 source break for `init` accessors (180969028). It contains **no availability-checking items**. § Swift Compiler, .md L943–981.
- **XCODE-117** Localization: strings inside availability-constrained `#Preview` macros are now excluded from String Catalogs (176188980) (FB22696182). § Localization/Resolved Issues, .md L697.

**Xcode 27.1** ([Xcode 27.1 RN](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes); T1)
- **XCODE-118** Previews: the overrides picker adds a **Display** group for a device's alternative display (182598534). Known issues: iOS 27.1-specific APIs fail to compile for Mac Catalyst (185924957), and iOS 27.1 targets show no Catalyst run destination (187046347). The workaround is `#if !targetEnvironment(macCatalyst)` or a Catalyst 27.0 minimum. iPhone Duo Simulator known issues (187708500, 187708663, 187708767, 190155353). There are no accessibility entries. Locators: .md L28–54.

**Xcode 27.2** ([Xcode 27.2 RN](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes); T1)
- **XCODE-119** Device Hub known issue: VoiceOver, the Accessibility Inspector and other accessibility tools "cannot convey screen content on an iPhone Duo within Device Hub" (187148389). Device Hub can't customize text size for iOS 18-or-earlier devices (189261485) (FB25077755). § Device Hub/Known Issues, .md L76–78.
- **XCODE-119a** Device Hub new and fixed: Sidecar touch forwarding for multi-finger gestures (188634387). A bundle including Slow Motion Animation, Shake, Fall and Memory Pressure simulation (simulators only) (.md L30). Input for iOS 17 sims (187484157). Modifier keys reach the right device (177181719). The pre-iOS 18 input issue (181945323) and the hardware-keyboard lingering issue (182553164) are fixed. § Device Hub, .md L28–65.
- **XCODE-119b** SDK and availability known issue: the macOS, watchOS, tvOS and visionOS 27.2 SDKs "incorrectly report 27.1 as a valid deployment target". Catalyst builds targeting 27.1 or 27.2 may be unable to use new API (187160501). The Catalyst iOS 27.1 API compile issue (185924957) persists. § SDK/Known Issues, .md L143; § Mac Catalyst, .md L105.
- **XCODE-119c** Other: the RenderPreview MCP tool returns and accepts render destinations (186442676). The JSON `.xcproj` project format arrives. XCTest UI Automation `.rotateDigitalCrown` is fixed (188422137). .md L129, L136, L168.

**Xcode 27.3 beta (BETA)** ([Xcode 27.3 Beta RN](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_3-release-notes); T1)
- **XCODE-120a** Swift Testing: "Xcode now supports writing UI tests with Swift Testing and `XCUIAutomation`." (95593221). .md L95. UI Automation adds `XCUIHinge` for the iPhone Duo hinge angle (187479559), .md L102.
- **XCODE-120b** Device Hub: option-drag simulates two-finger touch on iPhone and iPad (169537162). Input accepted for sims older than iOS 18 etc. (190652440). Drag-and-drop install, open and save (179246120). Known issue: Sidecar is limited to two touches (185140491). .md L35–49.
- **XCODE-120c** Previews: RenderPreview snapshot filenames and metadata include applied overrides (176531615). Interactive delayed macOS snapshots (181244878). Plus several fixes (.md L58–81). Coding assistant: GitHub Copilot added (185837709), .md L28. No accessibility-specific entries.

**Security skill (naming collision with "audit")**
- **XCODE-120** The only "audit" in Xcode 27.x notes is the "audit-xcode-security-settings" Code Intelligence skill (181104536). It is not an accessibility audit. Source: [Xcode 27 RN](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes) § Security/New Features, .md L877. T1.

### Inferences
- In Xcode 27, accessibility testing gains a second automated path. `performAccessibilityAudit` (unchanged since iOS 17) does static checks, and the new `XCUIVoiceOverService` drives the screen reader itself. With 27.3 beta, both can be written in Swift Testing.
- Accessibility Inspector was effectively broken for simulators at some point in the 27 cycle (XCODE-105 is listed as fixed in the 27.0 notes). Device Hub is now the surface for toggling VoiceOver, Text Size and Color Filters on sims and devices (XCODE-106).
- XCODE-119b and XCODE-118 are the SDK-availability diagnostics issues most likely to hit teams targeting 27.1 or 27.2.

### Gaps
- **Swift 6.4 availability checking:** no Xcode 27.x release note describes changes to `@available` or `#available` diagnostics. Swift.org and Swift Evolution were not checked within this research budget, so treat this as open.
- **Accessibility Inspector new features:** the Xcode 27.x notes contain only the simulator-inspection fix (XCODE-105) and the iPhone Duo known issue (XCODE-119). I found no notes on new Inspector features.
- **"Simulator accessibility settings":** beyond the Device Hub VoiceOver, Text Size and Color Filter items, no release notes describe new simulator accessibility settings.
- XCUIVoiceOverService has an empty abstract in the doc JSON. Behavior details such as the `Output` structure were not verified.

---

## Q4: Any WWDC26 sessions on accessibility testing or tooling? (URLs and timestamps)

### Takeaway
I found no WWDC26 session dedicated to accessibility testing APIs. A transcript scan of all 138 WWDC26 session pages found no mention of `XCUIVoiceOverService` or `performAccessibilityAudit`. Accessibility tooling appears in four kinds of sessions: two accessibility design sessions (219, 220), Xcode and Device Hub sessions showing accessibility-settings testing (258, 260), agent sessions showing the accessibility specialist (102, 259), and the Accessibility Technologies Group Lab (8005), where Apple staff discuss XCUITest and the new VoiceOver testing API.

### Cited Findings
- **XCODE-121** [T2] "What's new in Xcode 27" (28:00), Device Hub chapter at 9:37. At 10:36–10:43: "It's important to test an app with different accessibility settings. For example, I can increase contrast, choose a larger dynamic type size". Source: https://developer.apple.com/videos/play/wwdc2026/258/ (transcript 10:36).
- **XCODE-122** [T2] "Get the most out of Device Hub" (17:09). Chapters: Configure 6:04, Reproducing a bug 8:08, devicectl 15:52. It shows configuring text size and "accessibility settings that could affect the UI" (13:53) and reproducing a user's large-text bug (14:39–15:06). Source: https://developer.apple.com/videos/play/wwdc2026/260/.
- **XCODE-123** [T2] Platforms State of the Union, ~56:21: Xcode 27 ships specialists, including "An accessibility specialist that knows what makes an interface work for everyone." Source: https://developer.apple.com/videos/play/wwdc2026/102/ (also the ASL version, /112/, same timestamp).
- **XCODE-124** [T2] "Xcode, agents, and you" (24:03), Orchestrate chapter at 18:25. At 19:56–20:00 a second agent conversation is asked "to add VoiceOver labels and accessibility identifiers to all interactive elements". VoiceOver verification follows at 21:13–21:32. Source: https://developer.apple.com/videos/play/wwdc2026/259/.
- **XCODE-125** [T2] "Enhance the accessibility of your reading app" (20:00). Chapters: Characteristics 1:26, Standard views 3:45, Custom text 14:05. It covers UITextInput adoption for VoiceOver and Speak Screen and a custom edit-rotor action (11:46). At 19:23 it advises: "Audit your app with VoiceOver on, trying out the read all gesture". Source: https://developer.apple.com/videos/play/wwdc2026/219/.
- **XCODE-126** [T2] "Refine accessibility for custom controls" (16:25). Chapters: Guiding principles 1:02, Complex controls 8:41. It covers adjustable traits (5:40), the passthrough gesture (6:38), and direct touch, with VoiceOver silent (14:13). At 15:43 it recommends manual testing: "Turn on VoiceOver, open your app". Source: https://developer.apple.com/videos/play/wwdc2026/220/.
- **XCODE-127** [T3] Accessibility Technologies Group Lab (60:41). At ~5:02 a question covers using Accessibility Inspector to audit elements and Device Hub for screen sizes. At ~36:38, stable accessibility identifiers for UI tests and Inspector. At ~52:26–53:30, automated testing: staff say XCUITest relies on the accessibility hierarchy, and acknowledge new VoiceOver testing API exists without naming it. Source: https://developer.apple.com/videos/play/wwdc2026/8005/.
- **WEB-171** [T2] "What's new in WebKit for Safari 27" (16:32). Chapter "A year of quality improvements" at 1:07 lists Accessibility as a focus area (~4:35). Chapter "Customizable Select" at 10:06 says select gets "great accessibility automatically" (~10:19). Source: https://developer.apple.com/videos/play/wwdc2026/204/.
- **WEB-172** [T2] The Customizable Select session ("Rediscover the HTML Select Element") is at https://developer.apple.com/videos/play/wwdc2026/315/, linked from the [WWDC26 beta post](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/) § Customizable Select. Its transcript was not scanned beyond the all-session keyword search.
- Related labs (not mined): Safari and Web Technologies Group Lab https://developer.apple.com/videos/play/wwdc2026/8015/ and Xcode Tips and Tricks Group Lab https://developer.apple.com/videos/play/wwdc2026/8013/. Session index: https://developer.apple.com/videos/wwdc2026/. [T2]

### Inferences
- XCUIVoiceOverService (XCODE-101) shipped without a dedicated WWDC26 session, at least none whose transcript names it. Developers would rely on the API reference and release notes.

### Gaps
- Timestamps come from on-page transcript `data-start` values and are approximate to the sentence. Some sessions may have code samples or resources tabs that mention the APIs even where the transcript does not. Those were not checked.
- No WWDC26 session on Safari Web Inspector accessibility tooling or `ariaNotify` was found.
