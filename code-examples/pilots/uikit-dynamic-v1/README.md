# Dynamic UIKit content and action reuse

This batch adds15 UIKit unit tests. It keeps earlier pilot packages and evidence
unchanged. The [manifest](manifest.json) pins source/test/mutation inputs, while
[coverage.json](coverage.json) maps every test to a claim and guideline IDs.

## Source contracts versus example policies

- Apple's [custom rotor](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotor)
  exposes a search callback returning item results. This example adds stable-ID
  updates, identity-preserving reorder, retitling, empty-content handling and a
  boundary restart when the current element was removed. Duplicate-ID rejection
  and restart behavior are application policies, not mandatory UIKit behavior.
- Apple's [custom action](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction)
  has a named Bool handler. The example adds generation-token checks so retained
  actions cannot target a recycled view. Archive and Delete have independent custom
  handlers and ordinary button paths. Disabled-state guards are application logic;
  direct `sendActions` calls do not simulate touch filtering.
- Apple's [UIControl](https://developer.apple.com/documentation/uikit/uicontrol)
  declares enabled/selected defaults and synthesized state. Installed `UIControl.h`
  documents replacement by UIAction identifier and selective removal. Three tests
  exercise those actual framework contracts rather than a mock control.

Public SDK27 headers and availability declarations were read locally; their hashes
are recorded in [apple-sdk-sources.json](apple-sdk-sources.json). API and runtime
scope remain distinct. The callbacks used here are supported below the pilot's
iOS26 deployment target; this does not make them new OS26 features.

## Focused checks

```sh
node code-examples/tools/native.mjs plan \
  code-examples/pilots/uikit-dynamic-v1/manifest.json dynamic-unit

node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-dynamic-v1/manifest.json dynamic-unit \
  /private/tmp/uikit-dynamic-new IOS26_SIMULATOR_UUID
```

`compile-dynamic` type-checks the library. Four separate negative checks run the
same selected assertions against single-error variants:

| Check | Defect | Assertion |
| --- | --- | --- |
| `staleaction-negative` | Removed revision-token guard | A retained old action must reject after reconfiguration |
| `duplicatecallback-negative` | Invoke the callback twice | Independent actions emit exactly the requested events |
| `missingelements-negative` | Clear the ordinary element list | Reordering preserves the stored accessibility element sequence |
| `retainedremoved-negative` | Keep deleted entries in the ID index | Removed elements can be released after replacement |

Each execution uses a fresh private output directory and real installed tools.
No UI tests, device-setting changes, downloaded assets, SwiftUI work or model calls
are involved. Results belong to this pilot, not the frozen baseline or an annual
anchor. Read the [validation report](validation/README.md) before treating any check as executed evidence.

## Test revision history

Revision1's first positive suite passed14 tests and failed the removed-element
lifetime assertion. Its package and results are preserved, not relabeled. The
initial test checked release before draining temporary Objective-C references.
Revision2 keeps the example and mutants unchanged, but places insertion/removal
inside an explicit autorelease pool before checking persistent ownership. The
retained-index mutation remains subject to the same strict release assertion.
See [validation](validation/README.md) for actual outcomes; this is a test-lifetime
investigation, not evidence that Apple's API changed.

Stored order and handler invocation do not establish assistive-technology traversal,
keyboard delivery or discoverability. Remaining work is tracked in the
[UIKit-first ledger](../../UIKIT-COVERAGE.md).
