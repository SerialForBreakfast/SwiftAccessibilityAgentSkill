# Gold-task pool

Natively graded developer tasks for **Claude Haiku 5.5 low** (the development target). Each task is a realistic single-file Swift starter, a natural request, and a hidden unit contract. Its known valid alternatives must pass; its plausible mistakes must fail. The pool is the portfolio every candidate is run against. Ranked failure evidence comes from the [failure inventory](../../research/evaluation/failure-inventory/README.md).

```bash
python3 -B evals/pool/pool.py list
python3 -B evals/pool/pool.py export checkout-integrated
python3 -B evals/pool/pool.py qualify --cell ios-uikit
```

`qualify` compiles every variant together with the hidden test, on the booted iOS/tvOS 26.5 unit simulators or the macOS host, and checks each variant's expected status. It never boots or shuts down simulators. Results go to ignored `evals/results/pool/`. `--record` writes `<cell>/scorecard.json` once.

## Cells

`ios-uikit`, `ios-swiftui`, `macos-appkit`, `macos-swiftui`, `tvos-uikit`, `tvos-swiftui`. Deployment target 26.0 everywhere. Folder layout: `evals/pool/<cell>/<task-id>/`.

## Task format

| File | Contents |
|---|---|
| `task.json` | `id` (= folder name), `cell`, `workstream` (W1–W9, see the inventory), `decision` (the developer decision under test, one sentence), `split` (`development` or `transfer`), `evidence` (see below), optional `starterExpect`, `variants` |
| `prompt.md` | The developer's request, in their words. **Doesn't state the rule being tested.** Names the types and members the answer must keep, because the hidden test uses them. |
| `starter.swift` | The complete current file the developer pastes. It compiles. It contains working behavior worth preserving. |
| `reference.swift` | One complete correct answer. |
| `test.swift` | The hidden check: Swift statements that end in `return true` or `return false`. They run inside `@MainActor static func check() -> Bool` after `import <Framework>` and `import Darwin`. |
| `support.swift` | Optional hidden top-level helpers for the test (fakes, recorders). |
| other `.swift` | Variants listed in `task.json` as `{"file", "expect", "why"}` with `expect` one of `pass`, `contract-failure`, `compile-failure`. |

**`evidence.status`:**
- `observed`: a model failure on this decision is recorded. Give `inventoryCase` and a note naming the model and counts.
- `credible`: another model failed, or a package negative fixture shows a plausible mistake, but no Haiku failure is recorded. Give the source (`inventoryCase` or `package` with the fixture name).
- `control`: the decision usually passes. The task guards against regressions.

**Rules every task must satisfy** (`qualify` enforces the first three):
1. The reference and **at least one materially different accepted alternative** pass. If a valid alternative fails, fix the test, never the alternative. The test must accept every correct design, not one implementation.
2. **At least one mutant** fails. Prefer the mechanism models actually produced (from the inventory reasons) and package `NegativeFixtures`. A compile failure counts only when it is the defect itself, as with the observed out-of-scope stack. Mutants must keep the members the test uses; otherwise the oracle fails to compile, which is reported as an infrastructure error.
3. **The untouched starter fails**, unless the task is a no-change control. Then set `"starterExpect": "pass"`, make the starter already correct, and make the mutants plausible unnecessary rewrites that break working behavior.
4. **The test checks observable behavior only:** state, callbacks, configured properties, fonts after a trait change, IDs after reorder. Never the source text. Never rendered pixels, spoken output or UI automation.
5. **Transfer cases** (about a third of each cell) test the same decision as a development case in a different product context and code shape. Don't reuse the incident's wording, identifiers or structure.
6. **Never copy model answers** from private returns into tasks. Write variants yourself; describe observed mechanisms in `why`.

## Known harness facts

- **No `UIApplication` or `NSApplication` runs in a unit process.** `sendActions(for:)` and `NSControl.sendAction` don't deliver. Read the registered target/action (`actions(forTarget:forControlEvent:)`, `target`/`action`) and invoke it directly.
- **Trait changes work without a window.** Set `traitOverrides.preferredContentSizeCategory` on a view or controller, then call `updateTraitsIfNeeded()`. A label with `adjustsFontForContentSizeCategory` follows it, and `registerForTraitChanges` handlers fire. Layout works after giving the root view a frame and calling `layoutIfNeeded()`.
- **SwiftUI accessibility trees can't be inspected.** Type-check the view and test the model, bindings, closures and state it uses.
- **Asynchronous work needs deterministic doubles** that record calls and complete on command, not timers or sleeps. Run continuations synchronously where possible.
- **The unit timeout is 40 s per variant.** The first iOS launch after a boot is slow; qualify again on the warm simulator rather than raising it.
