# Offline analysis tools

Pinned local tools check record structure, Swift syntax, selected lint rules,
Markdown structure and exact replay of preserved excerpts. No model calls or LLM
judges. No new native unit runs, accessibility-tree assertions or UI automation.

## Setup

From the repository root:

```sh
npm ci --ignore-scripts --no-audit --no-fund --prefix tools/local-analysis
```

Dependencies are isolated in this directory. Dependency lifecycle scripts are not
needed for the offline path and remain disabled. SwiftLint 0.65.1 is extracted from
its Homebrew bottle into `.cache/swiftlint/0.65.1/bin/swiftlint`, not installed globally.
Build `SyntaxProbe.swift` with the selected Xcode's SwiftSyntax/SwiftParser host
libraries; these modules must match the selected toolchain. See `setup-native.sh`.

## Run

```sh
npm --prefix tools/local-analysis test
npm --prefix tools/local-analysis run check
```

Results go to a new ignored `results/<attempt>/report.json` on each run; completed
reports are never overwritten. The command prints the report path. Reports include
source hashes. Historical records and candidates are read-only inputs.

Ajv validates draft controller, evidence-ledger and selected example manifest shapes.
SwiftSyntax reports actual function declarations, direct XCTest assertion calls and
accessibility-named call expressions. It does not perform typechecking, resolve call
graphs, count Swift Testing macros or prove an assertion's semantic relevance.
SwiftLint uses only four selected rules; findings are triage, not automatic failures
or permission to rewrite historical examples. Markdown findings are similarly advisory.

Promptfoo uses a captured-string provider, deterministic equality assertions and
network-denial guards. It replays 26 preserved development excerpts for infrastructure
validation, not semantic grading. Public historical answer summaries contain hashes,
not original answer text: those whole answers remain unavailable for replay here.
Never substitute snippets for full answers or count preservation as answer correctness.

A real archived answer can be passed to `replay(records)` with its exact output and
an explicitly reviewed equality, contains, not-contains or JSON expectation. Do not add LLM assertions, network
providers or executable code extracted from answers. Compile/unit evidence requires
the separate bounded native adapter and must not be inferred from lint results.
