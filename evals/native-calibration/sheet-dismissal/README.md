# Who requested restoration?

This development check uses the two closures on the actual SwiftUI modifiers produced by the candidate's SheetOwner. The source is matched byte-for-byte to the first Swift example in the research archive's return card before staging. The modifier passes that same closure to sheet(isPresented:onDismiss:content:). No presentation driver, reflection, or simulated VoiceOver interaction is involved.

| Callback order | Owned request history | Shared-ticket control |
|---|---|---|
| Open A, open B | empty | empty |
| Deliver A late | empty | A requests B's origin |
| Deliver B | B requests B's origin | unchanged: A already consumed B |
| Deliver B again | unchanged | unchanged |

The mutant still deduplicates. A final-count or final-target oracle would accept it; recording the caller and checking each prefix distinguishes it. Three assertion diagnostics in one mutant execution describe one ownership defect, not three defects. Both origins are eligible. This is not a result for fallback, user-perceived focus or SwiftUI's scheduling. The shared-ticket implementation is a deliberate control, not an execution of the historical SheetExample view.

[Unit test](CallbackTests.swift) | [First native receipts](evidence.json) | [Development question](question.md) | [Controller rubric](rubric.md)

The retained first attempts live under `evals/results/persistent-replay/sheet-callback-d0p4j40r`: exact staged sources and checks, build command, environment, stdout/stderr and xcresult per cell. Run `python3 -B evals/native-calibration/sheet-dismissal/verify.py` to verify the first receipts locally. For a separate repetition, stage.py allocates a fresh project-local batch; pass its name to research/evaluation/signal-panel-v4/replay/native.py. Historical results and released guidance are not rewritten.

Authoring request: “Lets test the installed sheet dismissal callbacks: fire A late, then B twice. Verify only B requests focus restoration, exactly once, and the shared-ticket version fails. Preserve first failures. No model runs or released skill changes.” The question is a development draft; no subject answer or judge output exists. Full authoring transport transcript unavailable in this packet.
