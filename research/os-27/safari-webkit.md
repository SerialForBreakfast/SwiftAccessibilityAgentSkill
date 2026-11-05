# Safari and WebKit 27

Reviewed 2026-11-05. Tier-1 first-party engine evidence. Browser version and OS
version must be recorded separately, particularly on Macs with Safari updates.

| ID | Documented change | Source and section | Research consequence |
| --- | --- | --- | --- |
| WEB-01 | SVG language attributes support text pronunciation/rendering; MathML gains focus/navigation facilities. | [Safari 27.0](https://webkit.org/blog/18325/webkit-features-for-safari-27-0/), SVG; MathML | Investigate mixed-language reading and keyboard math content. |
| WEB-02 | Fixes cover accessible names, dynamic details, image-rotor entries and grid/combobox navigation. | [Safari 27.0](https://webkit.org/blog/18325/webkit-features-for-safari-27-0/), Accessibility; e.g. 98999595, 159865815, 172931277 | Extract remaining atomic fix records before generalizing to WKWebView. |
| WEB-03 | Accessible names/descriptions include previously omitted list/table/tree/canvas content. | [Safari 27.2](https://webkit.org/blog/18515/webkit-features-for-safari-27-2/), Accessibility / 186015032 | Future label/reference fixture. |
| WEB-04 | Live-region rerendering no longer causes the described repeated VoiceOver text. | [Safari 27.2](https://webkit.org/blog/18515/webkit-features-for-safari-27-2/), Accessibility / 186766347 | Future streaming-status fixture; preserve version scope. |
| WEB-05 | Date/time/color inputs receive corrected popup-button identification on iOS. | [Safari 27.2](https://webkit.org/blog/18515/webkit-features-for-safari-27-2/), Accessibility / 187788949 | Confirm custom control wrappers preserve native semantics. |
| WEB-06 | Safari MCP tab creation/screenshots receive a keyboard-focus fix. | [Safari 27.2](https://webkit.org/blog/18515/webkit-features-for-safari-27-2/), Safari MCP / 182558329 | Tooling evidence, not ordinary web navigation behavior. |

[Apple Safari release index](https://developer.apple.com/documentation/safari-release-notes/)
lists 27.0 (September 14), 27.1 (October 23), 27.2 (October 26) and 27.3 beta
(November 3). Capture exact engine builds and WKWebView host scope before defining
regression expectations. The broader rendering, form and media sections remain in
the research queue; accessibility keywords alone do not cover all user effects.
