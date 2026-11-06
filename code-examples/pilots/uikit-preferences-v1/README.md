# UIKit preferences and non-color state cues

Eight unit tests cover reduced-motion policy, semantic color resolution and form
error/reset configuration. The [manifest](manifest.json) pins source files and
Apple claim locators; [coverage](coverage.json) maps every positive assertion.

## Source support

- [Reduce Motion](https://developer.apple.com/documentation/uikit/uiaccessibility/isreducemotionenabled)
  supplies the read-only preference. Zero versus 0.25 seconds is example policy.
  Tests exercise both policy branches and the live preference reader without
  modifying device settings or asserting an animation was displayed.
- [Color resolution](https://developer.apple.com/documentation/uikit/uicolor/resolvedcolor(with:))
  supports resolving dynamic colors with explicit traits. The example retains
  semantic label/background colors and re-resolves a concrete layer border.
  Tests cover light/dark and normal/high contrast configuration, not a measured
  rendered contrast ratio or automatic trait-change delivery.
- [UIKit accessibility](https://developer.apple.com/documentation/uikit/accessibility-for-uikit)
  supports element labels/hints. Visible error text and corresponding accessible
  naming remain present independently of color preferences. Error replacement
  and recovery reset the hint and enabled state. Message wording is app policy.

Installed SDK header hashes are recorded in [apple-sdk-sources.json](apple-sdk-sources.json).
The fixture is a configuration example, not a complete laid-out form.

## Run locally

```sh
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-preferences-v1/manifest.json preferences-unit \
  /private/tmp/uikit-preferences-new IOS26_SIMULATOR_UUID
```

Use a fresh output directory. Other checks are `compile-preferences`,
`ignoredmotion-negative` and `stalehint-negative`. The negatives retain motion
when reduction is requested and retain an obsolete form hint, respectively.
They run the same selected tests against isolated source replacements.

Unit tests only; runtime skill integration and anchor promotion remain separate.
Completed native results are in the [validation report](validation/README.md).
