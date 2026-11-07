# Native forms and collection structure

November 6, 2026. A coordinated AppKit/macOS and UIKit/tvOS companion batch.
[Results](RESULTS.md) distinguish executed code contracts from draft evaluation
pairs. Released skill files and frozen baselines are unchanged; SwiftUI is deferred.

| Family | Mac implementation | Apple TV implementation |
| --- | --- | --- |
| Form recovery | NSTextField, ordinary NSButton action, visible error and help restoration via editing delegate | UITextField, ordinary primary action, visible error and hint restoration via editingChanged |
| Collection structure | NSOutlineView hierarchy, named columns, stable item identity, expansion and visible selection | Shelf headings and independent buttons, explicit child ordering, section-qualified selection and callback ownership |

These are configuration/state/action examples, not complete visual layouts.
Validation is injected and pure; localized errors are supplied by the application.
No UI automation, mandatory manual verification, new model calls or spend.

- [Source evidence](SOURCES.md)
- [Results and exact environments](RESULTS.md)
- [Difficulties, limits and preservation](DIFFICULTIES.md)
- [Four exact draft questions and controller rubrics](prompt-records.json)
- [Remaining parity work](COVERAGE.md)
- [Authoring capture boundaries](AUTHORING.md)
- [Independent review packet](REVIEW-REQUEST.md)

## Progressive disclosure

```sh
node code-examples/tools/structure-retrieval.mjs macOS AppKit outline-structure
node code-examples/tools/structure-retrieval.mjs tvOS UIKit form-recovery example
node code-examples/tools/structure-retrieval.mjs tvOS UIKit shelf-structure contract
```

A short platform summary loads by default. Only the selected family source is
added for `example`; manifest/tests for `contract`. Prior routes delegate unchanged.
Wrong frameworks do not receive fallback examples. Read traces report paths,
hashes and bytes; token telemetry is unavailable. No controller rubrics, incidents
or entire library load into normal context. Installed skill routing is unchanged.

## Reproduce

```sh
node code-examples/tools/platform-native.mjs plan code-examples/platforms/macos-structure-v1/manifest.json positive
node code-examples/tools/platform-native.mjs execute code-examples/platforms/macos-structure-v1/manifest.json positive /private/tmp/new-mac-structure-attempt
```

TV uses its own manifest and a matching installed simulator UUID as final argument.
Use a new private output directory for each attempt. Native adapter timeouts and
strict test-ID/expected-failure matching remain in force. Raw evidence belongs in
private archives; public indices contain hashes and sanitized diagnostics.
