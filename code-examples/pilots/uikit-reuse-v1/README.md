# UIKit reuse and configuration transitions

Eleven unit tests connect collection reuse, accessible metadata, heading/container
configuration, typography and notification arguments to reviewed public declarations.
The [manifest](manifest.json) pins inputs; [coverage](coverage.json) maps each test
to its source claim. SDK header hashes are in [apple-sdk-sources.json](apple-sdk-sources.json).

## Primary sources and scope

- [prepareForReuse](https://developer.apple.com/documentation/uikit/uicollectionreusableview/prepareforreuse())
  requires calling the superclass and distinguishes reuse from reconfiguration.
  Tests directly invoke the hook and separately configure a cell twice without it.
  Reconfiguration replaces speech-language metadata, name, selected state, value,
  conditional hint and actions. Retained old actions reject a changed identity.
- [UIKit accessibility](https://developer.apple.com/documentation/uikit/uiaccessibility)
  and installed `UIAccessibility.h`/`UIAccessibilityConstants.h` define attributed
  labels, speech-language attributes and traits. Tests observe stored metadata,
  not pronunciation. The cell is a metadata fixture, not a full interactive screen;
  ordinary action-path examples remain in the semantic/dynamic pilots.
- [Containers](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainer)
  support explicit elements and container types. A heading remains separate from
  a nested list; changing heading role preserves unrelated traits. No reading-order
  or rotor-menu behavior is inferred from these configuration assertions.
- [Preferred fonts](https://developer.apple.com/documentation/uikit/uifont/preferredfont(forTextStyle:compatibleWith:))
  accept explicit style and traits. The helper uses the receiving label's traits;
  tests set its public content-size trait override. Three styles and three categories
  exercise reconfiguration, scaling flags and unlimited-line policy, not layout fit.
- [Accessibility notifications](https://developer.apple.com/documentation/uikit/uiaccessibility/notification)
  and `UIAccessibilityConstants.h` define layout/screen-change kinds and optional
  target arguments. An injected recorder checks argument identity, kind, nil target
  and call count. No system notification is sent and no focus movement is asserted.

## Run locally

```sh
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-reuse-v1/manifest.json reuse-unit \
  /private/tmp/uikit-reuse-new IOS26_SIMULATOR_UUID
```

Other checks: `compile-reuse`, `staleselection-negative`, `staleidentity-negative`,
`wrongnotification-negative`. Each mutation runs the same selected positive test.
No UI tests, downloads or model calls are required. Skill integration and anchor
promotion remain separate from this offline example library.
See the [validation report](validation/README.md) for the completed matrix and
preserved typography revisions.
