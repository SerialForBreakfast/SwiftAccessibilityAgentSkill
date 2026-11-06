# Long Text and Non-Color Choice State

UPAIR-02 implementation candidate; not a promoted skill example or gold case.
Nine unit tests cover long localized text, effective Dynamic Type configuration,
selection metadata, non-color cues, same-instance reconfiguration and self-sizing
constraint configuration. Four deliberate defects test oracle sensitivity.

Inputs are pinned by [manifest.json](manifest.json). The [coverage map](coverage.json)
links each test to a claim and draft evaluation family. Installed Apple SDK header
hashes and web-access limitations are in [source provenance](apple-sdk-sources.json).

## Source and Application Contract

- [UILabel numberOfLines](https://developer.apple.com/documentation/uikit/uilabel/numberoflines)
  and the installed header support the unlimited-line setting. This alone does not
  establish that text fits a particular rendered frame.
- [Preferred fonts](https://developer.apple.com/documentation/uikit/uifont/preferredfont(forTextStyle:compatibleWith:))
  use a supplied trait environment. `UIContentSizeCategoryAdjusting.h` documents the
  relationship between supported scaled fonts and automatic content-size adjustment.
- [Selected trait](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/selected)
  describes selected state. Text and checkmark cues, trait preservation and resetting
  owned state are application policies, not claims that Apple requires this exact design.
- [Automatic dimension](https://developer.apple.com/documentation/uikit/uitableview/automaticdimension)
  and table sizing declarations support the selected sizing configuration. Tests
  inspect a vertical constraint chain without rendering or claiming a measured height.

The cell accepts already localized strings and a chosen state from its controller.
The controller owns selection input and persistence. This fixture does not implement
table selection interaction, accessibility activation, focus or spoken output.
The cell intentionally exposes one item with no independent nested actions; this
differs from the previous two-button card, whose controls must remain independent.

## Reproduce

```sh
node code-examples/tools/native.mjs plan \
  code-examples/pilots/uikit-choice-v1/manifest.json choice-unit
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-choice-v1/manifest.json choice-unit \
  /private/tmp/uikit-choice-new IOS26_SIMULATOR_UUID
```

Other check IDs: `compile-choice`, `singleline-negative`, `fixedfont-negative`,
`staleselection-negative`, `clobberedtraits-negative`. Each native execution needs
a fresh private output directory. No UI tests, model runs or dependencies are added.

Review [difficulties](DIFFICULTIES.md), [deliberate mutation diffs](MUTATIONS.md), and
[native validation](validation/README.md) before interpreting the evidence.
The [subject prompt](evaluation/prompt.json) and [controller rubric](evaluation/controller.md)
are separate drafts. Do not give the evaluated model this README, the rubric,
solution, tests, mutations or incident narrative. Independent case review is pending.
