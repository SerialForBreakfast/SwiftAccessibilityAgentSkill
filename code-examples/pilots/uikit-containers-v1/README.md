# UIKit containers and action hooks

Thirteen unit tests exercise data-table metadata, virtual elements, activation
results and modal overlay teardown. The [manifest](manifest.json) binds every
check to source claims and hashed inputs; [coverage](coverage.json) maps each test.

## Primary sources

- [Data-table containers](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatable)
  and [cell ranges](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatablecell)
  provide dimensions, coordinate lookup, spans and optional headers. Apple requires
  the data-table protocol when using the
  [dataTable container type](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainertype/datatable).
  The installed `UIAccessibilityContainer.h` supplies the exact declarations.
- [Activation](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityactivate())
  reports whether the operation succeeded. The example propagates its callback
  result and rejects disabled activation as an explicit app policy.
- [Escape](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityperformescape())
  reports whether dismissal succeeded. The panel exposes an ordinary Close button
  and an escape override using the same guarded dismissal function.

Reviewed SDK header hashes are in [apple-sdk-sources.json](apple-sdk-sources.json).
The Apple web documentation and installed public header declarations were reviewed
on 2026-11-05. API availability is recorded separately from the tested runtime.

## Scope

The virtual grid is a metadata fixture, not a complete drawing view. It intentionally
does not assign rendered frames. Sparse cells, insertion order, bounds validation
and overlap rejection are example policies. Tests inspect every coordinate in a
spanning cell, invalid/overflow-sized ranges, header identity, and removal from
both lookup paths. These assertions do not establish VoiceOver reading order.

The panel is an in-view overlay, not a presented view controller. Tests call escape
directly and explicitly dispatch the Close button event. Rejection preserves state;
success clears modal flags and hides the overlay; reopening restores configuration.
No accessibility notifications or system gestures are sent.

## Bounded execution

```sh
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-containers-v1/manifest.json containers-unit \
  /private/tmp/uikit-containers-new IOS26_SIMULATOR_UUID
```

Other checks: `compile-containers`, `wrongspan-negative`, `stalemodal-negative`,
`ignoredenabled-negative`. The negatives break span lookup, modal-state cleanup,
and the enabled-state guard. Each uses the same selected positive test.

Unit tests only. The examples remain outside installed skill routing and frozen
baseline inputs; independent review and anchor promotion remain separate.
See the [validation report](validation/README.md) for both preserved revisions.
