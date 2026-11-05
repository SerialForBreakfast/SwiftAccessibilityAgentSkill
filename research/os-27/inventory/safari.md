# Safari and WebKit 27 release-note inventory

Research only. Mechanically transferred from the pass-3 research notes on 2026-11-05 (script `build_inventory.py`, not retyped). Every row is **Tier-1**, evidence type **release note**. Apple text is truncated in the notes (22 words or fewer). Symbol availability for any API named here is pending unless [api-availability.md](../api-availability.md) records DocC metadata. The `Pass-2 ID` column cross-references earlier claim IDs by Apple issue number.

Sources: [Safari 27](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes) (117,412 bytes), [27.1](https://developer.apple.com/documentation/safari-release-notes/safari-27_1-release-notes) (1,870 bytes), [27.2](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes) (5,322 bytes), [27.3 beta](https://developer.apple.com/documentation/safari-release-notes/safari-27_3-release-notes) (64,306 bytes). Full hashes: [sources.md](../sources.md).

**Scope warning.** Unlike the OS inventories, the notes did not extract every Safari entry. They extracted every entry in the Accessibility sections plus accessibility-relevant entries from other sections (CSS focus, forms, HTML focus, media/captions, Web Inspector, WebDriver). WebKit's beta post counts 58 new features, 525 fixes and 4 deprecations for 27.0 alone. A complete Safari inventory is in the [backlog](../backlog.md). Issue numbers are Apple radar IDs, not WebKit Bugzilla IDs.

Rows are split from the notes' bullets at each radar-numbered sentence; grouped bullets keep their claim ID with a part number.

## Stable: Safari 27.0

| Claim ID | Release | Notes heading | Radar(s) | Entry (notes' paraphrase) | Locator | Pass-2 ID |
|---|---|---|---|---|---|---|
| WEB-101 | 27.0 | Safari 27.0: Accessibility > New Features | 166338108 | Added the `ariaNotify` API, described as "allowing web developers to programmatically make screen reader announcements." (166338108) | Source: [Safari 27 RN](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes) § Accessibility/New Features. |  |
| WEB-102 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 46151521 | `speechSynthesis.cancel()` no longer removes utterances queued by later `speak()` calls (46151521). |  |  |
| WEB-103 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 98999595 | SVG `<use>`→`<symbol>` inside `<img>` no longer shows up as unnamed images in VoiceOver's Images rotor (98999595). |  | WEB-02 |
| WEB-104 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 107644248 | Changing the `id` of an element targeted by `aria-owns` now updates the accessibility tree (107644248). |  |  |
| WEB-105 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 114500560 | A `<slot>` referenced by `aria-labelledby` now uses its slotted content for the name and ignores hidden slotted nodes (114500560). |  |  |
| WEB-106 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 127460695 | `<meter>` labels are now consistent between `aria-label` and `title` (127460695). |  |  |
| WEB-107 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 129361833 | `display: contents` elements with shadow-root content are now read when referenced by `aria-labelledby` (129361833). |  |  |
| WEB-108 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 141564913 | `aria-labelledby` now uses the checkbox name, not its value, when the name comes from a `<label>` (141564913). |  |  |
| WEB-109 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 146323788 | The VoiceOver cursor is now positioned correctly for elements focused via canvas `drawFocusIfNeeded()` (146323788). |  |  |
| WEB-110 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 153134654 | Grids whose child rows are in a shadow root now work with VoiceOver (153134654). |  |  |
| WEB-111 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 159304061 | VoiceOver no longer reads text inside images with `role="presentation"` (159304061). |  |  |
| WEB-112 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 159865815 | Content in dynamically expanded `<details>` is now exposed in the accessibility tree (159865815). |  | WEB-02 |
| WEB-113 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 164128676 | `contextmenu` now fires inside iframes when triggered by keyboard or AT, for example VO+Shift+M (164128676). |  |  |
| WEB-114 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 168200460 | Changes to `<input type="button">` inside live regions are now announced (168200460). |  |  |
| WEB-115 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 168458291 | `::first-letter` text is now exposed in the accessibility tree when it stands alone (168458291). |  |  |
| WEB-116 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 168770938 | VoiceOver can now reach `aria-owns`'d rows and cells in grids and tables (168770938). |  |  |
| WEB-117 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 170187464 | VoiceOver next/previous form-control navigation now finds focusable splitters (170187464). |  |  |
| WEB-118 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 172218114 | Color picker inputs can now be activated with VoiceOver's press action (172218114). |  |  |
| WEB-119 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 172559238 | Interactive elements containing an `<svg>` named by a child `<title>` now expose an accessible name (172559238). |  |  |
| WEB-120 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 172851295 | Bounding boxes for MathML table rows and cells are now computed correctly (172851295). |  |  |
| WEB-121 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 172931277 | Comboboxes now forward focus to `aria-activedescendant`, so AT can interact with list items (172931277). |  | WEB-02 |
| WEB-122 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 173228707 | VoiceOver can now navigate to content revealed by `hidden="until-found"` disclosure widgets (173228707). |  |  |
| WEB-123 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 173249317 | `aria-owns` is now respected when computing a name from content (173249317). |  |  |
| WEB-124 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 174349841 | VoiceOver line-by-line reading no longer skips content in read-only documents (174349841). |  |  |
| WEB-125 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 174449524 | `aria-hidden="true"` is now invalidated correctly when focus lands inside the hidden subtree (174449524). |  |  |
| WEB-126 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 176297111 | VoiceOver's "Skip redundant labels" setting is now respected on certain pages (176297111). |  |  |
| WEB-127 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 177167634 | VoiceOver now follows `focus()` calls on newly added elements (177167634). |  |  |
| WEB-128 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 178399441 | Role computation is fixed for elements with prefixes (178399441). |  |  |
| WEB-129 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 179065364 | VoiceOver no longer jumps to the top of the page when the target element immediately becomes accessibility-ignored via JS (179065364). |  |  |
| WEB-130 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 179156593 | Site-specific fix: VoiceOver no longer reports the parks.wa.gov Recent Events table as empty (179156593). |  |  |
| WEB-131 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 179398579 | An `<a>` with a click handler but no `href` is now exposed as a link (179398579). |  |  |
| WEB-132 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 180294912 | VoiceOver now announces the selected state of the day-of-month button in a monthly-notification UI (180294912). |  |  |
| WEB-133 | 27.0 | Safari 27.0: Accessibility > Resolved Issues | 180319221 | `aria-labelledby` no longer goes stale when the referenced element changes its `aria-label` (180319221). |  |  |
| WEB-134 | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 158759228 | CSS: added the `:heading` pseudo-class (158759228) | Locator: § CSS/New Features, .md L80. |  |
| WEB-135 (part 1) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 134337357 | CSS focus fixes: `:focus-visible` no longer matches wrongly after programmatic `focus()` from a click on a button with children (134337357) | Locator: § CSS/Resolved Issues (.md ~L115–259). |  |
| WEB-135 (part 2) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 173145294 | `:active`, `:focus-within` and `:hover` now account for the top layer (173145294) | Locator: § CSS/Resolved Issues (.md ~L115–259). |  |
| WEB-135 (part 3) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 173321368 | The SVG and MathML UA sheets now use `:focus-visible` instead of `:focus` (173321368) | Locator: § CSS/Resolved Issues (.md ~L115–259). |  |
| WEB-135 (part 4) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 177850766 | Programmatic focus after keyboard interaction now matches `:focus-visible` (177850766) | Locator: § CSS/Resolved Issues (.md ~L115–259). |  |
| WEB-135 (part 5) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 173068660 | `outline: auto` now respects zoom (173068660) | Locator: § CSS/Resolved Issues (.md ~L115–259). |  |
| WEB-136 | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 170328089 | Forms: added customizable `<select>` (`appearance: base-select`, `<selectedcontent>`) (170328089) | Locator: § Forms/New Features, .md L350. |  |
| WEB-137 (part 1) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 120676409 | Forms fixes: tab position is kept when a focused button becomes disabled; previously focus jumped to the top of the page (120676409) | Locator: § Forms/Resolved Issues, .md L352–374. |  |
| WEB-137 (part 2) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 4360235 | Keyboard paste now works in numeric-restricted fields (4360235) | Locator: § Forms/Resolved Issues, .md L352–374. |  |
| WEB-137 (part 3) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 147428926 | Range-slider thumbs get a larger touch hit area on iPadOS and visionOS (147428926) | Locator: § Forms/Resolved Issues, .md L352–374. |  |
| WEB-137 (part 4) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 168676757 | `<datalist>` no longer shows white-on-white in dark mode (168676757) | Locator: § Forms/Resolved Issues, .md L352–374. |  |
| WEB-137 (part 5) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 183345556 | Base-select default styles were fixed, including "increased contrast colors" (183345556) | Locator: § Forms/Resolved Issues, .md L352–374. |  |
| WEB-138 (part 1) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 176258900 | HTML: added `tabindex`, `focus()`, `blur()` and `autofocus` on MathML elements (176258900) |  |  |
| WEB-138 (part 2) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 103370883 | Sequential focus navigation now skips elements that don't meet the focusability requirements (103370883) |  |  |
| WEB-138 (part 3) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 171352032, 171358576 | Popover light dismiss now accounts for input buttons and disabled command buttons (171352032, 171358576) |  |  |
| WEB-138 (part 4) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 174734133 | Locator: § HTML, .md L382, L388, L395–396. Also MathML `tabIndex` values fixed (174734133), .md L508. |  |  |
| WEB-139 | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 143751056 | SVG: added `lang` and `xml:lang` support in SVG (143751056) | Locator: § SVG/New Features, .md L758. |  |
| WEB-140 (part 1) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 71042767 | Media, captions and WebVTT: `TextTrackCue.endTime` can now be `Infinity` (71042767) | Locator: § Media (.md L515–586). |  |
| WEB-140 (part 2) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 136809012 | WebVTT no longer displays cues larger than the viewport (136809012) | Locator: § Media (.md L515–586). |  |
| WEB-140 (part 3) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 171699293 | Autoplay waits for default text tracks to load (171699293) | Locator: § Media (.md L515–586). |  |
| WEB-140 (part 4) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 175084171 | NULL is allowed in `VTTCue` text (175084171) | Locator: § Media (.md L515–586). |  |
| WEB-140 (part 5) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 175296476 | WebVTT cue-settings line parsing is fixed (175296476) | Locator: § Media (.md L515–586). |  |
| WEB-140 (part 6) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 175298523 | Subtitles and closed captions now appear in fullscreen video on iOS (175298523) | Locator: § Media (.md L515–586). |  |
| WEB-140 (part 7) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 175357130 | `<audio controls>` hides "Subtitles" when there is no track (175357130) | Locator: § Media (.md L515–586). |  |
| WEB-140 (part 8) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 175550173 | `::cue()` now matches the WebVTT root object (175550173) | Locator: § Media (.md L515–586). |  |
| WEB-141 | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 171840378 | Scrolling: scroll anchoring is enabled (171840378) | Locator: § Scrolling/New Features, .md L841. Per the 27.0 blog, it is controlled by `overflow-anchor` ([WebKit blog 27.0](https://webkit.org/blog/18325/webkit-features-for-safari-27-0/), § Scroll Anchoring). |  |
| WEB-142 (part 1) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 113887185, 171332734 | Web Inspector: added color contrast information in the Color Picker (113887185), including when editing background colors (171332734) | Locator: § Web Inspector, .md L1070, L1073, L1116. |  |
| WEB-142 (part 2) | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 178562336 | The Accessibility sidebar is no longer empty for nodes in cross-origin iframes (178562336) | Locator: § Web Inspector, .md L1070, L1073, L1116. |  |
| WEB-143 | 27.0 | Safari 27.0: accessibility-relevant entries in other sections | 176038457 | WebDriver: added the Safari MCP server so agents can connect to Safari (176038457) | Locator: § WebDriver/New Features, .md L1162. |  |

62 rows.

## Stable: Safari 27.1

| Claim ID | Release | Notes heading | Radar(s) | Entry (notes' paraphrase) | Locator | Pass-2 ID |
|---|---|---|---|---|---|---|
| WEB-144 | 27.1 | Safari 27.1 | 170353889, 170005463, 176426722 | The only sections are PDF and Web API. They cover foldable book-pose PDF (170353889), the Device Posture API (170005463) and the Viewport Segments API (176426722), the last two behind a feature flag. There are no accessibility entries. Available for iOS 27.1 only. |  |  |

1 rows.

## Stable: Safari 27.2

| Claim ID | Release | Notes heading | Radar(s) | Entry (notes' paraphrase) | Locator | Pass-2 ID |
|---|---|---|---|---|---|---|
| WEB-145 | 27.2 | Safari 27.2: Accessibility > Resolved Issues | 186766347 | VoiceOver no longer repeats already-announced text when a page streams content by re-rendering an `aria-live` region instead of appending to it (186766347). |  | WEB-04 |
| WEB-146 | 27.2 | Safari 27.2: Accessibility > Resolved Issues | 187788949 | VoiceOver on iOS now identifies date, time and color inputs as pop-up buttons (187788949). |  | WEB-05 |
| WEB-147 | 27.2 | Safari 27.2: Accessibility > Resolved Issues | 182558329, 187933878, 187617020, 185816680 | Other 27.2 entries relevant to accessibility: Safari no longer takes keyboard focus from other apps when under Safari MCP control (182558329), § Safari MCP. An anchor-positioned element inside a modal `<dialog>` no longer goes offscreen (187933878), § CSS. Base-select gets `::field-content` and alignment and `text-overflow` changes (187617020), § Forms. `flow-tolerance` is renamed `fit-tolerance` for grid-lanes (185816680), § CSS Deprecations. The WebKit 27.2 post ties this property to keyboard focus order (see WEB-162). |  | WEB-06 |

3 rows.

## Beta (not shipped): Safari 27.3 beta

These rows are beta-only. Do not treat them as shipped behavior.

| Claim ID | Release | Notes heading | Radar(s) | Entry (notes' paraphrase) | Locator | Pass-2 ID |
|---|---|---|---|---|---|---|
| WEB-148 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 185108892 | The accessible name of a `display: contents` element no longer includes sibling text (185108892). |  |  |
| WEB-149 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 185422271 | List-marker text is excluded when a name or value is requested without markers (185422271). |  |  |
| WEB-150 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 186015032 | List, table, tree and canvas content is no longer omitted from the name or description when the container is referenced by `aria-labelledby` or `aria-describedby` (186015032). **Conflict:** the WebKit "Features for Safari 27.2" post lists this same radar under 27.2 Accessibility ([WebKit blog 27.2](https://webkit.org/blog/18515/webkit-features-for-safari-27-2/), § Accessibility), while the Apple 27.2 release notes do not. |  | WEB-03 |
| WEB-151 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 186342070 | VoiceOver now speaks `aria-keyshortcuts` `Meta` and `Alt` as Command and Option (186342070). |  |  |
| WEB-152 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 186687365 | The list marker is now present in the accessibility text of list items with block content (186687365). |  |  |
| WEB-153 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 187789276 | VoiceOver on iOS no longer auto-expands `<select>` and date pickers after a swipe from a text field (187789276). |  |  |
| WEB-154 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 188921930 | VoiceOver no longer announces every focused ARIA menu item as "selected" (188921930). |  |  |
| WEB-155 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 188980125 | VoiceOver can now press buttons with `pointer-events: none` (188980125). |  |  |
| WEB-156 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 189417259 | VoiceOver activation now dispatches `click` with a non-zero `detail` plus pointer events, mimicking a mouse click (189417259). |  |  |
| WEB-157 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 189824370 | Text hidden with `clip` plus `overflow: hidden` is no longer exposed in the accessibility tree (189824370). |  |  |
| WEB-158 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 190043178 | VoiceOver can now reach an `<iframe>` nested inside an iframe with `role="none"` or `role="presentation"` (190043178). |  |  |
| WEB-159 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 190150062 | `::marker` `content` is now exposed in the accessibility tree (190150062). |  |  |
| WEB-160 | 27.3 beta | Safari 27.3 beta (BETA): Accessibility > Resolved Issues | 191127608 | VoiceOver on iOS no longer dispatches duplicate `pointerdown` events (191127608). |  |  |
| WEB-161 | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 182180043, 184548373, 184654901 | HTML new features: `headingoffset` and `headingreset` attributes (182180043), `popover=hint` (184548373), and the viewport `interactive-widget` key for on-screen-keyboard behavior (184654901) | § HTML/New Features, .md L262–265. |  |
| WEB-161a (part 1) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 184751412 | Dialog and focus fixes: focus is restored to the correct element when a `<dialog>` closes (184751412) |  |  |
| WEB-161a (part 2) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 185156091 | `show()` now moves focus (185156091) |  |  |
| WEB-161a (part 3) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 185549474 | `close()` no longer restores focus when focus wasn't inside a non-modal dialog (185549474) |  |  |
| WEB-161a (part 4) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 185567540 | `documentElement.focus()` now moves focus to the viewport (185567540) |  |  |
| WEB-161a (part 5) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 100476630 | A color input with `display:none` now opens via its `<label>` (100476630) |  |  |
| WEB-161a (part 6) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 180105698 | § HTML/Resolved Issues, .md L268–278. Web API: close watchers and `closedby` for `dialog` (180105698), § Web API/New Features, .md L559. |  |  |
| WEB-161b (part 1) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 181570771 | CSS: `:focus-visible` is no longer shown after `focus()` inside an already-focused ancestor (181570771) | § CSS (.md L71–117). |  |
| WEB-161b (part 2) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 180547604, 182750380, 184964807 | New features include `outline-offset: inset` (180547604), `content` on `::marker` (182750380) and unprefixed `user-select` (184964807) | § CSS (.md L71–117). |  |
| WEB-161c (part 1) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 189042890 | Forms: a disabled `<option>` can no longer be chosen by access key (189042890) | § Forms/Resolved Issues, .md L239–256. |  |
| WEB-161c (part 2) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 188830823 | Base-select supports press-drag-release picking (188830823) | § Forms/Resolved Issues, .md L239–256. |  |
| WEB-161c (part 3) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 189042427 | `<optgroup>` labels now use only a first-child `<legend>` (189042427) | § Forms/Resolved Issues, .md L239–256. |  |
| WEB-161d (part 1) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 183365541 | Media and captions: added `HTMLMediaElement.removeTextTrack()` (183365541) | § Media, .md L351–364. |  |
| WEB-161d (part 2) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 182001231 | Find-in-text now resolves to the caption cue nearest the playhead (182001231) | § Media, .md L351–364. |  |
| WEB-161d (part 3) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 184039946 | The auto position of WebVTT `start`/`end`-aligned cues is now 50% (184039946) | § Media, .md L351–364. |  |
| WEB-161e (part 1) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | — | Web Inspector (27.3 beta): no accessibility-specific entries in the New Features or Resolved Issues lists (.md L623–660) |  |  |
| WEB-161e (part 2) | 27.3 beta | Safari 27.3 beta (BETA): accessibility-relevant entries in other sections | 158871569 | The entries are network throttling, canvas and WebGPU tools, layout-invalidation events, quirks logging, and a fix for Find in Page in Responsive Design Mode (158871569). |  |  |

30 rows.
