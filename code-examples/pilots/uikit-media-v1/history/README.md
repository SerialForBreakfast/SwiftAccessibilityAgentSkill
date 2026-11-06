# Media pilot observations

Revision1 compiled, then passed6 of8 unit tests. The headless native UIButton
trait getter did not include `.button`, and the two-subtitle fixture exposed four
legible options. These were initially unsupported test assumptions, not established
Apple API defects. All negative checks were left unattempted.

Revision2 explicitly inserts the button trait as example configuration. Its
diagnostic unit run passed7 of8 tests and retained the expected-count failure while
recording each actual option. It observed:

| Name | Language | Forced-only | Type |
| --- | --- | --- | --- |
| English | en | false | sbtl |
| English Forced | en | true | sbtl |
| Spanish | es | false | sbtl |
| Spanish Forced | es | true | sbtl |

Apple defines
[containsOnlyForcedSubtitles](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/containsonlyforcedsubtitles)
as a characteristic inferred from the track format. Counting every option as a
separate authored-language track was incorrect. Revision3 checks two full and two
forced-only options for this exact fixture/runtime and verifies both language sets.
It also requires full-language selection to exclude forced-only variants, with a
new isolated mutant that intentionally selects the wrong variant.

The four-option observation is a version-scoped fixture result, not a promise that
every two-track asset returns four options. Nor does the headless getter observation
establish how a displayed native button is exposed to assistive technology.

Original inputs remain in [revision-1](revision-1/) and [revision-2](revision-2/).
Revision2 was a diagnostic unit run; no separate compile or negative checks were
scheduled for it. Its unit target did compile successfully before executing tests.
