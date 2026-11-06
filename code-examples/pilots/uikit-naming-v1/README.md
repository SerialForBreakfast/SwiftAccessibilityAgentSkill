# Decorative Content and Independent Named Controls

UPAIR-01 implementation candidate, not a promoted skill example or gold case.
Eight positive unit tests and three intentional negative variants exercise explicit
configuration, caller-supplied localized names, reconfiguration and ordinary action
dispatch. [Manifest](manifest.json), [coverage](coverage.json) and
[source provenance](apple-sdk-sources.json) pin the inputs and reviewed declarations.

Apple's installed `UIAccessibility.h` comments support explicit element exposure,
localized accessibility labels and the descendant-hidden flag. `UIControl.h`
supplies action registration/dispatch declarations. Complete item-specific names and
reconfiguration are this example's application contract, not a universal requirement
that every repeated label be globally unique. The example accepts localized strings
from its caller; it does not claim to implement a localization pipeline.

The source creates a property/configuration fixture, not a laid-out production card.
The tests do not assert speech, navigation, Voice Control matching, rendering or
native default button traits. Direct control-event dispatch verifies ordinary
handler wiring; it does not establish actual accessibility activation delivery.

## Reproduction

```sh
node code-examples/tools/native.mjs plan \
  code-examples/pilots/uikit-naming-v1/manifest.json naming-unit
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-naming-v1/manifest.json naming-unit \
  /private/tmp/uikit-naming-new IOS26_SIMULATOR_UUID
```

Other check IDs: `compile-naming`, `exposeddecoration-negative`,
`hiddencontrols-negative`, `stalenames-negative`. Each execution uses a new output
directory and preserves raw private artifacts. No dependencies or UI tests are added.

See [development difficulties](DIFFICULTIES.md) and the separate
[controller case](evaluation/controller.md). The [subject question](evaluation/prompt.json)
is draft development material, not a frozen baseline addition. Do not provide this
README, the tests, mutations or controller rubric to the evaluated model.
