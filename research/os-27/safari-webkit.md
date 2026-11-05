# Safari and WebKit 27

Third pass, 2026-11-05. Research only. Apple Safari release notes and WebKit team posts are
Tier-1 for engine behavior. Issue numbers are Apple radar IDs, not WebKit Bugzilla IDs.
Record the browser version and OS version separately. The accessibility-relevant entries are
listed one per radar in [inventory/safari.md](inventory/safari.md); that inventory is not a
full Safari inventory.

Releases: 27.0 (14 Sep 2026, 20625.1.29), 27.1 (23 Oct, iOS 27.1 only, no accessibility
entries), 27.2 (26 Oct, 20625.2.8), **27.3 beta** (3 Nov, 20626.1.12). Accessibility-section
counts: 27.0 one new feature and 32 fixes; 27.1 none; 27.2 two; 27.3 beta 13.
[R0] = [Safari 27 RN](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes);
[R2] = [Safari 27.2 RN](https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes);
[R3] = [Safari 27.3 beta RN](https://developer.apple.com/documentation/safari-release-notes/safari-27_3-release-notes).

## Pass-2 records (preserved, cross-referenced)

| ID | Pass-3 records |
| --- | --- |
| WEB-01 (SVG language; MathML focus) | WEB-139; WEB-138; WEB-163 |
| WEB-02 (names, details, image rotor, grid/combobox) | WEB-103; WEB-112; WEB-121 and WEB-102–133 |
| WEB-03 (list/table/tree/canvas name content, 186015032) | WEB-150; C-03 |
| WEB-04 (live-region repeat, 186766347) | WEB-145 |
| WEB-05 (date/time/color popup buttons, 187788949) | WEB-146 |
| WEB-06 (Safari MCP keyboard focus, 182558329) | WEB-147 |

## Screen-reader announcements and speech

| ID | Change | Release / status | Tier | Source and locator |
| --- | --- | --- | --- | --- |
| WEB-101 | `ariaNotify` API added, "allowing web developers to programmatically make screen reader announcements". Absent from the WebKit 27.0 post (C-15). | 27.0 New Feature | Tier-1, release note | [R0] § Accessibility › New Features, 166338108 |
| WEB-145 | VoiceOver no longer repeats announced text when a page re-renders an `aria-live` region instead of appending. | 27.2 Resolved | Tier-1, release note | [R2] § Accessibility, 186766347 |
| WEB-114 | Changes to `<input type="button">` inside live regions are announced. | 27.0 Resolved | Tier-1, release note | [R0] § Accessibility, 168200460 |
| WEB-102 | `speechSynthesis.cancel()` no longer removes utterances queued by later `speak()` calls. | 27.0 Resolved | Tier-1, release note | [R0] § Accessibility, 46151521 |
| WEB-151 | VoiceOver speaks `aria-keyshortcuts` Meta and Alt as Command and Option. | **27.3 beta** | Tier-1, release note | [R3] § Accessibility, 186342070 |
| WEB-154 | VoiceOver no longer announces every focused ARIA menu item as "selected". | **27.3 beta** | Tier-1, release note | [R3] § Accessibility, 188921930 |

## Accessible name and tree computation

| ID | Change | Release / status | Tier | Source and locator |
| --- | --- | --- | --- | --- |
| WEB-104, 105, 107, 108, 119, 123, 133 | `aria-owns` id changes update the tree; slotted content names `aria-labelledby` slots; `display: contents` shadow content read; checkbox name not value; `<svg><title>` names interactive elements; `aria-owns` respected in name-from-content; `aria-labelledby` no longer stale. | 27.0 Resolved | Tier-1, release note | [R0] § Accessibility (107644248, 114500560, 129361833, 141564913, 172559238, 173249317, 180319221) |
| WEB-106, 111, 115, 125, 128, 131 | `<meter>` label consistency; `role="presentation"` image text not read; standalone `::first-letter` exposed; `aria-hidden` invalidated when focus lands inside; prefixed role computation; `<a>` with click handler but no `href` exposed as link. | 27.0 Resolved | Tier-1, release note | [R0] § Accessibility (127460695, 159304061, 168458291, 174449524, 178399441, 179398579) |
| WEB-112 | Dynamically expanded `<details>` content exposed. | 27.0 Resolved | Tier-1, release note | [R0] § Accessibility, 159865815 |
| WEB-148, 149, 152, 157, 159 | `display: contents` names exclude sibling text; list-marker text excluded when requested; marker present for block-content list items; `clip` + `overflow: hidden` text no longer exposed; `::marker` content exposed. | **27.3 beta** | Tier-1, release note | [R3] § Accessibility (185108892, 185422271, 186687365, 189824370, 190150062) |
| WEB-150 | List, table, tree and canvas content no longer omitted from names or descriptions via `aria-labelledby`/`aria-describedby`. WebKit lists it under 27.2. | **27.3 beta** (Apple RN) | Tier-1, release note + WebKit post | [R3] § Accessibility, 186015032; C-03 |

## VoiceOver navigation and activation

| ID | Change | Release / status | Tier | Source and locator |
| --- | --- | --- | --- | --- |
| WEB-103 | SVG `<use>`→`<symbol>` in `<img>` no longer appears as unnamed images in the Images rotor. | 27.0 Resolved | Tier-1, release note | [R0] § Accessibility, 98999595 |
| WEB-109, 110, 116, 117, 118, 122, 124, 126, 127, 129, 130, 132 | Canvas `drawFocusIfNeeded` cursor; shadow-root grid rows; `aria-owns` rows and cells; focusable splitters in form-control navigation; color-picker press action; `hidden="until-found"` content; line-by-line in read-only documents; Skip redundant labels; following `focus()` on new elements; no jump to top on newly ignored targets; a site-specific table fix; day-of-month selected state. | 27.0 Resolved | Tier-1, release note | [R0] § Accessibility (146323788, 153134654, 168770938, 170187464, 172218114, 173228707, 174349841, 176297111, 177167634, 179065364, 179156593, 180294912) |
| WEB-113 | `contextmenu` fires in iframes when triggered by keyboard or AT (VO+Shift+M). | 27.0 Resolved | Tier-1, release note | [R0] § Accessibility, 164128676 |
| WEB-121 | Comboboxes forward focus to `aria-activedescendant`. | 27.0 Resolved | Tier-1, release note | [R0] § Accessibility, 172931277 |
| WEB-146 | VoiceOver on iOS identifies date, time and color inputs as pop-up buttons. | 27.2 Resolved | Tier-1, release note | [R2] § Accessibility, 187788949 |
| WEB-153, 155, 158 | iOS VoiceOver no longer auto-expands `<select>` and date pickers after swiping from a text field; can press `pointer-events: none` buttons; can reach iframes nested in `role="none"` iframes. | **27.3 beta** | Tier-1, release note | [R3] § Accessibility (187789276, 188980125, 190043178) |
| WEB-156 / WEB-160 | VoiceOver activation dispatches `click` with non-zero `detail` plus pointer events; iOS no longer dispatches duplicate `pointerdown`. | **27.3 beta** | Tier-1, release note | [R3] § Accessibility (189417259, 191127608) |

## Focus, keyboard, dialogs and forms

| ID | Change | Release / status | Tier | Source and locator |
| --- | --- | --- | --- | --- |
| WEB-135 | `:focus-visible` fixes after programmatic focus; top-layer `:active`/`:focus-within`/`:hover`; SVG/MathML UA sheets use `:focus-visible`; `outline: auto` respects zoom. | 27.0 Resolved | Tier-1, release note | [R0] § CSS (134337357, 173145294, 173321368, 177850766, 173068660) |
| WEB-134 | `:heading` pseudo-class. | 27.0 New Feature | Tier-1, release note | [R0] § CSS, 158759228 |
| WEB-136 / WEB-137 | Customizable `<select>`; tab position kept when a focused button becomes disabled; keyboard paste in numeric fields; larger range-slider hit area on iPadOS and visionOS; datalist dark-mode contrast; base-select increased-contrast colors. | 27.0 | Tier-1, release note | [R0] § Forms (170328089, 120676409, 4360235, 147428926, 168676757, 183345556) |
| WEB-138 | MathML `tabindex`, `focus()`, `blur()`, `autofocus`; sequential focus skips non-focusable elements; popover light-dismiss fixes; MathML `tabIndex` values. | 27.0 | Tier-1, release note | [R0] § HTML (176258900, 103370883, 171352032, 171358576, 174734133) |
| WEB-147 | Safari no longer takes keyboard focus from other apps under Safari MCP control; anchor-positioned element in modal dialog stays onscreen; base-select `::field-content`; `flow-tolerance` renamed `fit-tolerance`. | 27.2 | Tier-1, release note | [R2] (182558329, 187933878, 187617020, 185816680) |
| WEB-161 / 161a / 161b / 161c | `headingoffset`/`headingreset`, `popover=hint`, viewport `interactive-widget`; dialog focus restoration and `show()` focus; `documentElement.focus()`; close watchers and `closedby`; `:focus-visible` inside focused ancestor; `outline-offset: inset`; disabled options not selectable by access key; optgroup legend. | **27.3 beta** | Tier-1, release note | [R3] § HTML, CSS, Forms, Web API |

## Media, captions and language

| ID | Change | Release / status | Tier | Source and locator |
| --- | --- | --- | --- | --- |
| WEB-139 | SVG `lang` and `xml:lang`; WebKit says this ensures correct accessibility announcements. | 27.0 New Feature | Tier-1, release note + WebKit post | [R0] § SVG, 143751056; WEB-163 |
| WEB-140 | WebVTT and caption fixes, including subtitles and closed captions in fullscreen video on iOS (175298523) and autoplay waiting for default text tracks (171699293). | 27.0 | Tier-1, release note | [R0] § Media |
| WEB-161d | `removeTextTrack()`; find-in-text resolves to the cue nearest the playhead; WebVTT start/end cue auto position 50%. | **27.3 beta** | Tier-1, release note | [R3] § Media (183365541, 182001231, 184039946) |
| WEB-141 | Scroll anchoring enabled, controlled by `overflow-anchor`. | 27.0 New Feature | Tier-1, release note + WebKit post | [R0] § Scrolling, 171840378 |

## Developer tooling

| ID | Change | Release / status | Tier | Source and locator |
| --- | --- | --- | --- | --- |
| WEB-142 | Web Inspector Color Picker shows contrast information, including for backgrounds; Accessibility sidebar works for cross-origin iframe nodes. | 27.0 | Tier-1, release note | [R0] § Web Inspector (113887185, 171332734, 178562336) |
| WEB-143 / WEB-165 | Safari MCP server lets agents connect to Safari; WebKit says agents can test for missing labels, improper ARIA and poor contrast. | 27.0 | Tier-1, release note + WebKit post | [R0] § WebDriver, 176038457; [WebKit 27.0](https://webkit.org/blog/18325/webkit-features-for-safari-27-0/) § Safari MCP; [Safari MCP intro](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/) |
| WEB-161e | No accessibility-specific Web Inspector entries in 27.3 beta. | **27.3 beta** | Tier-1, release note | [R3] § Web Inspector |

## WebKit team posts and WWDC

| ID | Claim | Tier | Source |
| --- | --- | --- | --- |
| WEB-162 | 27.2 post: "20 bug fixes across accessibility, media, CSS, and more"; grid-lanes tolerance aids focus order for sighted keyboard users; lists 186015032, 186766347, 187788949. | Tier-1, WebKit post | [WebKit 27.2](https://webkit.org/blog/18515/webkit-features-for-safari-27-2/) |
| WEB-163 / WEB-164 | 27.0 post mirrors the Accessibility fixes, covers Color Picker contrast, SVG language and MathML focus; does not mention `ariaNotify`. | Tier-1, WebKit post | [WebKit 27.0](https://webkit.org/blog/18325/webkit-features-for-safari-27-0/) |
| WEB-166 / WEB-167 | WWDC26 beta post: 58 new features, 525 fixes, 4 deprecations; customizable select keeps keyboard and screen-reader support. Golden rule: "always provide text content or accessible text attributes for your option elements". | Tier-1, WebKit post | [WWDC26 beta post](https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/); [Golden rule](https://webkit.org/blog/18117/the-golden-rule-of-customizable-select/) |
| WEB-168 | Adaptive Dark Mode targets WCAG 4.5:1 text contrast and inspects SVG icons and bitmaps. | Tier-1, WebKit post | [Adaptive Dark Mode](https://webkit.org/blog/18541/introducing-adaptive-dark-mode/) |
| WEB-169 / WEB-170 | Grid Lanes drift from source order is "an important consideration for accessibility"; the 27.1 post has no accessibility content. | Tier-1, WebKit post | [Sessions roundup](https://webkit.org/blog/17974/web-technology-sessions-at-wwdc26/); [WebKit 27.1](https://webkit.org/blog/18486/webkit-features-for-safari-27-1/) |
| WEB-171 / WEB-172 | WWDC26-204: accessibility a quality focus (~4:35); customizable select gets "great accessibility automatically" (~10:19). Session 315 covers the select element. | Tier-1, transcript | [204](https://developer.apple.com/videos/play/wwdc2026/204/); [315](https://developer.apple.com/videos/play/wwdc2026/315/) |

## Negative findings

No `prefers-reduced-motion` or "reduce motion" entries in any Safari 27.x notes; no ARIA 1.3
attribute or new-role entries; no WebKit post dedicated to `ariaNotify`; no Bugzilla mapping.
visionOS WebKit `<model>` fixes are in [visionos.md](visionos.md) (VISION-257–259).

## Community evidence

COMM-124 (VoiceOver cursor not following Shift+Tab on macOS 27.0.1 in Safari and other
browsers) and COMM-123 (fractions skipped, including in WKWebView) are Tier-3 on
[community.md](community.md).

## Research inference (not Apple-stated)

- Safari 27 accessibility work centers on name computation, VoiceOver navigation and native
  semantics in customizable select, not new ARIA features.
- WEB-156 and WEB-160 change the events pages see on VoiceOver activation; sites detecting
  assistive technology through `event.detail === 0` would behave differently once 27.3 ships.
- The ship version of 186015032 stays uncertain until Safari 27.3 final notes (C-03).

[R0]: https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes
[R2]: https://developer.apple.com/documentation/safari-release-notes/safari-27_2-release-notes
[R3]: https://developer.apple.com/documentation/safari-release-notes/safari-27_3-release-notes
