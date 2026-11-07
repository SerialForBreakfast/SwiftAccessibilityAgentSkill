# Dev.7 comparison readiness

**Ready for local, source-level comparative scoring; execution held.** One local candidate, one prepared BigDog job. The 24 questions are known development scenarios across 12 families, not a promotion of 24 gold prompts. The six historical gold decisions stand unchanged.

| What's ready | Result |
|---|---|
| Candidate | [Shared entry point](../failure-driven/candidates/0.3.0-dev.7/ENTRYPOINT.md), focused framework notes, and explicit opt-in example lookup. Not the installed skill. |
| Inputs | 48 sealed two-message files: dev.5 and dev.7 for each final question. 21 questions unchanged; three dismissal questions now state the fallback when the opener disappears. Six controls receive no supplied references in either arm. |
| Controller | [Scoring guide](SCORING.md) and [case-by-case crosswalk](controller/scoring.json): all 78 criteria, accepted alternatives, historical transitions, source pins, matching receipts where available, and proposed supplemental evidence distinguished from original bindings. |
| Execution | [Single worker brief](BIGDOG.md), [job list](jobs.json), [integrity seal](seal.json). Not sent. No provider calls, native tests, quota allocation or release changes. |
| Context | Across the same 24 final requests, total message-content bytes: 162,223 vs 123,215; medians: 7,199 vs 5,633 (21.8% smaller). Dev.7 supplied references range from zero to 4,709 bytes. Model tokens, latency and answer quality are unmeasured. |

## What is scored

Prior dev.5 results motivate the [three regression distinctions](DISTINCTIONS.md); they are neither new scores nor a substitute generic arm. Each row of the crosswalk connects the original question, prior outcome, included candidate guidance, answer criteria, and evidence limits. Both new arms are scored against the same final request and revised guide. The comparison measures the combined change to instructions and supplied guidance, not autonomous routing. No examples or incident records enter the default input. The few narrow helper receipts are not an integration test of either answer.

The portable and Mac audits agree on **73 distinct method identities**. The Mac count of 104 checks includes ten checks from two older container/reuse packages outside the portable audit's 94. They are not extra confirmations of the selected criteria. For all 78 criteria, the inherited evidence remains **2 direct, 35 partial, 39 review-only, 2 implementation gaps**. The gaps concern macOS checkout text/layout and preservation of the existing Pay path. Score the proposed design, not tested macOS behavior. The 48 older calibration originals are unavailable locally; bounded R13/R16 checkout observations and documented alternatives support scoring without manufacturing replacement answers.

## Reproduce locally

From the repository root, use Python 3.10+ with normal assertion checking:

```sh
python3 -B research/evaluation/dev7-comparison/build.py
python3 -B research/evaluation/dev7-comparison/checks.py
```

Both commands compare existing files; neither dispatches work, runs native code, or rewrites evidence. The builder checks protected paths against the named Git checkpoint. The offline checks compare subject separation, question equality, real reference contents, routing by explicit platform/framework, disclosure budgets, opt-in media examples and the existing checkout calibration outcomes. The checks do not claim semantic grading, tool isolation or model lift.

**Next decision:** approve or continue holding the single subscription-only paired job under the limits in the worker brief. A critical new loss of an ordinary action or navigation path blocks release regardless of average score.
