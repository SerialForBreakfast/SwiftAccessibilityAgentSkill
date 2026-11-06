# Difficulty and Failure Ledger

## First Native Failure: Configuration Oracle

Revision 1 built and executed five methods: four passed; only
`testPreservesConfiguredButtonAndDisabledState` failed. Exact failing test and
all manifest-bound source files are preserved in `history/revision-1/`. The
failed assertion was:

```swift
XCTAssertEqual(button.configuration, configuration)
```

The diagnostic compared a returned configuration with a resolved background color
against the original input configuration without that resolved background color.
The component source does not assign or update the button configuration. Classify
this as an overbroad test oracle, not evidence of an accessibility implementation
failure. The exact private first log is retained and hashed in validation.json;
public excerpts redact addresses and private paths.

Revision 2 leaves the component unchanged and asserts the explicitly supplied
title, subtitle, button size, corner style, base background color and disabled
state. It makes no promise that all computed configuration internals remain equal.
It does not establish every UIButton style or OS version behaves identically.

This difficulty has its own independent developer question,
`evaluation/oracle-prompt.json`, and controller criteria in the rubric. It remains
a development oracle-diagnostic case, not a new held-out model failure.

## Design Decisions Before Execution

- **Coverage gap:** the original eight model answers lacked supplied payment wiring.
  This new fixture explicitly provides a preexisting action; do not confuse its
  direct-dispatch evidence with validation of those original answers.
- **Oracle risk:** requiring a trait observer would reject an acceptable permanently
  vertical layout. The prompt permits vertical layout and the rubric accepts
  alternatives. Tests measure the stated contract, not one preferred pattern.
- **Oracle risk:** a custom font fixture alone misses configured UIButton state.
  Separate tests cover an explicitly configured button and a disabled control.
- **Evidence boundary:** direct `sendActions` checks callback routing, not actual
  touch, keyboard or VoiceOver input. Font metadata is not rendered readability.

## Predeclared Deliberate Mutants

These are authored oracle controls, not model errors or accidental first failures.
Full source is retained under `NegativeFixtures/`; no failed source is overwritten.

`ChangedFont.swift` inserts after spacing configuration:

```swift
payButton.titleLabel?.font = .preferredFont(forTextStyle: .headline)
```

Expected rejection: `testPreservesExistingButtonIdentityTypographyAndTitle`.

`FixedHeight.swift` inserts at the same location:

```swift
heightAnchor.constraint(equalToConstant: 44).isActive = true
```

Expected rejection: `testFlexibleTextConfigurationAndNoFixedEnclosingHeight`.

Each negative runs the same five-method suite as the positive fixture. Native
processes, source snapshots, commands and complete first diagnostics are retained
in separate private output directories. Outcomes are recorded in validation.json;
an infrastructure failure never counts as a rejected mutant.

## Evaluation Pair

Family `UIKIT-CHECKOUT-PRESERVATION-D1` is a development question informed by known
incidents, not a fresh holdout. Rubric checks preserved ordinary behavior, complete
ownership, repeat-update idempotence and honest unit-test scope. Cross-model testing
is pending; no model or harness ranking follows from this authoring session.
