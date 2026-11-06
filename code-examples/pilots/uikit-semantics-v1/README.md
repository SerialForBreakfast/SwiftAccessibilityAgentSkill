# UIKit semantic assertions

This expansion contains23 focused UIKit unit tests and three isolated behavioral
mutations. It extends the first pilot without changing its source or results.
SwiftUI work is deferred. No runtime skill integration or annual anchor is promoted.

## Tier1 sources

The [manifest](manifest.json) maps each claim to an Apple URL, supporting section,
review date and availability scope. [Coverage](coverage.json) maps each individual
test to its claim and existing U-series guidelines. Public SDK27 header hashes are
recorded in [apple-sdk-sources.json](apple-sdk-sources.json).

- [UIKit accessibility](https://developer.apple.com/documentation/uikit/accessibility-for-uikit): public semantics, traits, elements, containers and adjustable hooks. Exact property contracts were also read in the installed `UIAccessibility.h`, `UIAccessibilityConstants.h`, `UIAccessibilityContainer.h` and `UIAccessibilityElement.h`.
- [Custom actions](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction): named actions and handlers. Tests invoke the actual stored handler and keep a separate ordinary button callback path.
- [Custom rotors](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor) and [search block](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor/itemsearchblock): search result identity and direction. SDK comments additionally describe initial searches without a current item.
- [Font metrics](https://developer.apple.com/documentation/uikit/uifontmetrics/scaledfont(for:compatiblewith:)): explicit trait-compatible scaling. The capped overload is also declared in the installed `UIFontMetrics.h`.

Apple API support and example policy are distinct. The archive example chooses
once-only execution; the quantity example clamps to0...3; the rotor chooses not to
wrap. Those policies are tested application behavior, not universal Apple rules.

## Cases

- Label, value and hint separation; stale-hint clearing; attributed/plain linkage;
  ordered user-input names.
- Trait composition preserving unrelated traits; stored container order and
  grouping; empty containers; virtual-element metadata and container-relative frame.
- Modal configuration distinct from hiding descendants.
- Adjustable increment/decrement hooks, value synchronization and bounds.
- Named custom action success/failure, exact callback count, ordinary button path
  and weak-owner lifetime.
- Rotor next/previous identity, initial first/last result, boundaries, unknown
  anchor, empty results, retained ordinary elements, headings and weak-owner lifetime.
- Preferred-font response to explicit content-size traits and custom-font scaling
  with a maximum-size constraint.

The unit checks do not measure spoken output, hint usefulness, navigation, rendered
layout or whether a person discovers an action. A direct action callback is not
gesture delivery, and an element list is not observed VoiceOver reading order.

## Run one bounded check

From repository root:

```sh
node code-examples/tools/native.mjs plan \
  code-examples/pilots/uikit-semantics-v1/manifest.json semantics-unit

node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-semantics-v1/manifest.json semantics-unit \
  /private/tmp/uikit-semantics-new IOS26_SIMULATOR_UUID
```

Other check IDs are `compile-semantics`, `droppedaction-negative`,
`wrongrotordirection-negative` and `losttraits-negative`. Each negative runs the
same selected positive test against an isolated single-error variant. Use new
private output directories. Execution uses installed tools only; no UI tests,
simulator downloads or model calls are involved.

Revision1's22-test package is preserved under `history/revision-1/` with its own
manifest. Revision2 adds an explicit initial-current-item test and optional handling
in the search block. It is new evidence, not a rewrite of the earlier run. See
the [validation report](validation/README.md) for actual outcomes and outstanding review requirements.

The broader [UIKit coverage ledger](../../UIKIT-COVERAGE.md) tracks remaining work.
Source review, implementation tests and real-user outcomes remain different kinds
of evidence; test counts do not establish universal accessibility coverage.
