# UPAIR-03 Difficulty Ledger

Local date2026-11-05. Assisted development, not a controlled cross-model run.
Exact serving model revision/context are unavailable. Intentional mutations and
anticipated risks are not spontaneous model failures.

| ID | Difficulty | Treatment and evaluation translation |
| --- | --- | --- |
| K01 | Existing manifest accepts Apple claim URLs, while contrast math is W3C-defined | Keep Apple API claims and supplemental W3C provenance separate; pure math coverage does not pretend to test an Apple contract. No validator or tier changes. |
| K02 | Apple web results expose HTML shells rather than API bodies | Review installed declarations and pin headers. Record web-body access limits; do not infer an API is unsupported. |
| K03 | Raw components may use a different transfer function or space | Use a known linear-sRGB fixture whose expected converted value is independently specified; a separate deliberate wrong-space variant tests sensitivity. |
| K04 | Alpha needs a backdrop/compositing model | Explicitly reject translucent colors in this bounded fixture. The independent rubric also accepts correct explicitly scoped composition; do not train an unnecessary blanket restriction. |
| K05 | Dynamic color correctness can be confused with assumptions about Apple's palette | Test trait propagation with an injected provider separately from the real configured semantic pair. Record real pair ratios by context. |
| K06 | A semantic-pair pass or threshold can be overstated as full accessibility | Scope results to configured opaque colors at the tested environment, not rendered pixels or universal conformance. |
| K07 | An optional process-inspection command returned `operation not permitted: ps` in the sandbox while waiting for native checks | Used the existing execution session and immutable adapter results instead; no permission bypass or test-oracle change. Environment inspection limitation, not a Swift failure. |
| K08 | The partial offline-test command placed `--test-name-pattern` after the test filename; it ran the report test before the native report existed, producing `ENOENT` for `validation/revision-1.json` | Moved the option before the filename. The two intended pre-report checks passed; the complete suite must still run after all native evidence exists. Actual orchestration error, not a native failure or successful negative control. |

K01 is a discovered infrastructure/provenance constraint; K02 is source-access
friction. K03-K06 are addressed design/oracle risks, not observed accidental code
failures. Exact mutant diffs are separate. Any unexpected native failure must retain
its complete input revision, diagnostics and repair history before the next run.

## Exact Offline Invocation Correction

Failed partial-run invocation (two checks passed, the premature report check failed):

```sh
node --test code-examples/tools/contrast-contract.test.mjs --test-name-pattern='contrast coverage|contrast draft'
```

Corrected invocation (two intended checks passed):

```sh
node --test --test-name-pattern='contrast coverage|contrast draft' code-examples/tools/contrast-contract.test.mjs
```

Diagnostic: `ENOENT: no such file or directory` for the not-yet-written
`validation/revision-1.json`. No Swift or assertion code was changed to hide it.

## Native Outcome and Gold Translation

Revision1 compiled, all nine positive unit methods passed, and each of four
deliberate variants failed its intended assertion on the first attempt. There is
no accidental failed Swift snippet to invent. [Exact manufactured diffs](MUTATIONS.md)
and [native diagnostics](validation/revision-1.json) preserve what actually failed.

The separate developer question asks about ordinary UIColor inputs, appearance
changes, transparency and the meaning of a passing check. Its rubric permits valid
alternatives, including properly scoped composition, and distinguishes Apple API
support from W3C arithmetic. The family remains development material, not a fresh
holdout. No cross-model failure or skill improvement has yet been measured.
