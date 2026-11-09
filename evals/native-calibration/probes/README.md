# Controls for three previously unqualified distinctions

These are controller tests, not new subject answers. An original contract failure paired with a passing submitted proof remains a missed failure. Qualification asks a different question: does this focused controller test accept two correct approaches and distinguish the particular defect at this anchor?

| Case(s) | Positive and alternate approaches | Deliberate defect and observed path |
|---|---|---|
| P-4099aaf89ec377cf (tvOS), P-db6ab4c551e67aca (iOS) | Compare the current snapshot with submitted input, or inspect each captured field against its live native control. | Remove the live-input check. Edit the native field, deliver the old reply, then submit again. The old value must never be accepted; the current one must succeed. |
| P-be25d510c5ffe50f (macOS) | Select the eligible original or fallback using branches, or search ordered candidates for the first eligible button. | Ignore the attached button's responder eligibility. The recorded request goes to the original twice, rather than original then fallback. This does not exercise a window declining an attempted request. |
| P-90629dd9d60ff906 (iOS) | Retain the sheet origin in a session record, or capture it in a resolver. | Look up the origin through cleared presentation state after Close. Contrast a surviving origin with a removed one. This is a coordinator unit, not proof of a SwiftUI dismissal callback or delivered focus. |

The field and button controls derive from the existing platform examples. The sheet is a reduced, newly authored coordinator contract. No preserved answer was patched, newly scored, or substituted with one of these controls.

## Reproduction

From the repository root run `python3 -B evals/native-calibration/probes/run.py` on the recorded Mac and booted simulator anchors. Each invocation creates a fresh private directory under `evals/results/native-calibration/` with the sources, intent, diagnostics, result bundles and receipts. There are no UI or model runs. For the recorded batch, `python3 -B evals/native-calibration/grade.py --check` verifies hashes and method-specific results against the local artifacts, rather than trusting this summary.

The first Mac staging attempt stopped before test discovery because its package did not expose the named scheme. The second manifest explicitly exposed its library product. Both attempts are retained; the first is not a subject defect. The public index records the first log and receipt hashes separately from the qualified attempts.
