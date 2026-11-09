# Dismissal replay and focused-panel distillation

Scope: all 56 signal-v2 panel questions (not a new 384-question run). [Decision board](portfolio.md) joins the frozen criterion proposal to each pair's observed transition and the installed answer's failing dimensions. Keep all nine rescues and four preserved passes as controls; forty persistent failures remain opportunities; three incomplete pairs stay outside lift estimates. No prior question, grade or model output is revised. The board is controller-only.

## Replay

Original held packet: P-34541ce79ee3d519 and P-90629dd9d60ff906. Both are full-implementation questions, with controller rubrics and no mandated interface or assertion IDs. Neither requires the reference implementation's type names. First we staged the exact two Swift fences in each answer in a package named to match its submitted test import. Then we compiled the same implementation bytes with separate probes for observable requirements from the original questions. These probes are adapters for the original behavioral contracts, not the original reference suite or the later v3 mutant tests.

| Answer | Submitted tests | Independent observation |
|---|---|---|
| UIKit panel | 4/4 passed | A closes, B reopens, A finishes late, then B finishes. Background started exposed and finished hidden. Apply was not attached to the panel. Both assertions failed. |
| SwiftUI sheet | 4/4 passed | After an ordinary dismissal with the origin still eligible, the coordinator returned persistentFallback instead of the origin. One assertion failed. |

**Gap:** The SwiftUI view reads the current generation inside its inline no-argument callback. That is source evidence for the stale-owner diagnosis. No public seam exposes that installed callback for deterministic out-of-order delivery. The test of the surviving origin does not execute the installed callback. Do not report that stale delivery as natively reproduced, or credit the alternative v3 modifier as the submitted answer. Neither probe establishes assistive focus delivery. No repairs or retries.

[First results](first-results.json) links each answer, implementation, submitted or controller test and first log by digest. The first private attempt is retained in evals/results/signal-dismissal-replay/tmpp8oicrif with both answers, intents, full logs and result bundles. Xcode 27.0, simulator SDK 27.0, booted iOS 26.5, deployment target 26.0. Run evidence.py --check to verify these specific records; replay.py <booted-iOS-26.5-UDID> creates a separate attempt.

## Distillation

[Candidate](candidate.zip) retains discovery scope, original platform facts and font note, and every tested example byte. Shorten the entry and four on-demand cards. Keep original background and surviving origin distinct from current suppression and presentation state. Address chapter endpoints, outline state, queued-observer witnesses, native slider and reduced-motion restraint without making all examples required reading. Changes are development hypotheses, not measured rescues.

Offline: distill.py --check rebuilds the archive and 56 rows, checks sizes and resolves internal links; test_distillation.py checks retained examples, selected rule contrasts, entry contract and controller-ID isolation. The parent evidence checker verifies prior native example receipts, not behavior of a model prompted with shorter text. It is possible to pass every local check and still regress developer answers.

Next decision: keep the shorter candidate for comparison, not promotion. Use the same questions and grading criteria for any later owner-approved comparison, including previously correct no-change answers. Compare requested verification separately from primary correctness.
