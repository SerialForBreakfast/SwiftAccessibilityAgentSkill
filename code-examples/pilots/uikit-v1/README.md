# UIKit pilot: actions, cell state and text configuration

Candidate example library, not a promoted annual anchor. The compact
[index](../../index.json) connects three examples to this pilot manifest. Neither
the index nor code is loaded by the installed skill.

## Lineage and scope

Sources and UIKit assertions derive from `evals/os26/fixtures` at
`b0f4e449d22086fcce87765c154d390507c31b75`. The test module is renamed for this
separate package. Those original fixtures, their historical results, the frozen
skill and baseline snapshots remain untouched. New pilot results are separate
observations, not relabeled evaluation receipts.

| Example | Source | Unit assertion | Isolated counterexample |
| --- | --- | --- | --- |
| Independent row actions | [SettingsRow.swift](Sources/SettingsRow.swift) | Public exposure flags and independent switch/Help callbacks | Hidden descendants |
| Cell reconfiguration | [OrderCell.swift](Sources/OrderCell.swift) | Same instance updates customer, priority label and status | Stale status |
| Text configuration | [CheckoutSummary.swift](Sources/CheckoutSummary.swift) | Font adjustment, multiline configuration, no fixed height, payment title/callback | Font adjustment disabled |

Source support comes from the dated [OS26 source review](../../../evals/os26/SOURCE-REVIEW-R4.md)
and installed UIKit declarations. The manifest records Apple URLs, sections and
bounded availability descriptions. These are iOS26-targeted examples, not claims
that their APIs were introduced in26. Native results do not refresh documentation
review dates. Independent review of the new library adapter remains separate.

Direct callback/configuration assertions do not simulate input, speech, focus,
visual reflow or payment styling. No UI tests or mandatory manual checks are used.

## Native checks

From the repository root, inspect a single check without execution:

```sh
node code-examples/tools/native.mjs plan \
  code-examples/pilots/uikit-v1/manifest.json row-actions-unit
```

Execute only reviewed local source with installed Xcode and, for unit checks, an
installed iOS26 Simulator. Select an actual destination; no OS-emulation flag is
offered. Use a new private output directory for each check:

```sh
node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-v1/manifest.json compile-pilot \
  /private/tmp/uikit-compile-new

node code-examples/tools/native.mjs execute \
  code-examples/pilots/uikit-v1/manifest.json row-actions-unit \
  /private/tmp/uikit-row-new IOS26_SIMULATOR_UUID
```

Eight checks are registered: positive library type-check, one compiler-negative,
three positive unit checks and three behavioral negatives. Run serially. The
adapter generates a dependency-free library/unit-test package from pinned inputs;
it does not execute a supplied Package.swift or manifest shell commands.

Toolchain, command intent, manifest, source/test and adapter snapshots, raw logs and
results are written privately. Unit execution also retains an xcresult bundle.
Compiler/subtool invocations are bounded to two minutes and Xcode jobs to ten.
Extended diagnostic gathering is disabled for intentional assertion failures.
Timeouts, wrong destinations, zero/skipped tests and unclassified failures cannot
qualify as a passing observation. Non-passing results return a nonzero CLI status.
SDK and runtime come from installed tooling; no downloads or model calls occur.

Use the offline `cli.mjs record` command to copy a validated result and its hashed
artifacts into a private ledger. Raw xcresult bundles remain in the original run
directory; exported structured summaries/logs are hashed evidence artifacts.

## Diagnostic revision history

Manifest revision1 expected the compiler to report an Int-to-String? assignment
error. SDK27 actually reported Int-to-String. That first negative run remains a
failed diagnostic match. [The original manifest](history/manifest-revision-1.json)
is preserved as a historical specification; its file paths resolve from the pilot
root, not from the history directory.

Revision2 changes only the expected diagnostic text to the observed compiler
wording. The bad assignment remains invalid; neither its source nor the assertion
was repaired to make it compile. The revision2 runs are new evidence and do not
rewrite the first attempt. This tests compiler diagnostic normalization, not the
date an API became available or its runtime accessibility behavior.
