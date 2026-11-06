# Local comparison: released skill versus compact B

**Compact B used 29.9–34.7% fewer reported tokens. Correctness effects were mixed, including new API and behavior regressions.** Keep it as a research candidate; this local diagnostic does not support promotion or autonomous Swift edits.

Owner requested this local comparison on November 6, 2026. All 36 generations completed on this Mac: three installed Ollama models × six unchanged OS26 developer questions × two entrypoints. No subscription evaluation, downloads, retries or model substitutions ran. Models were unloaded after the batch.

## Paired results

F = current runtime `SKILL.md` plus selected current references. BR = compact-B subject body with the same metadata and reference bytes. Only the entrypoint body changes within each pair.

| Model | Total tokens F → BR | Reduction | Core coverage by source review F → BR | Type-check F → BR |
| --- | ---: | ---: | --- | --- |
| Gemma 4 12B | 22,869 → 15,392 | 32.7% | 3/6 → 3/6 | 6/6 → 3/5; one BR no-code answer |
| Qwen2.5 Coder 14B | 20,390 → 14,292 | 29.9% | 0/6 → 1/6 | 3/6 → 5/6 |
| Qwen3.5 9.7B (`latest`) | 23,301 → 15,207 | 34.7% | 2 met + 1 inconclusive → 1 met, out of six each | 5/6 → 2/5; one BR no-code answer |

These are provisional, unblinded maintainer source assessments against the [recorded checklist](../local-compact-b-20261106-criteria.json), not accuracy percentages or native test passes. A core-met answer can still contain optional bad advice or unsupported claims. The inconclusive cell-ownership case is retained separately, rather than counted as a failure. Compiler denominators exclude answers that correctly preserve the original Toggle without returning code.

Tokens are Ollama-reported input plus output counts, measured within each model. Six answers per condition, one sample per family, temperature 0/seed 42, thinking off, 16,384 context and a 1,024-token output cap. Two Qwen3.5 F answers reached the cap; every other answer stopped normally. Inference took approximately 57.4 minutes in total. Latency includes loading/prefill and was not measured on an isolated host; cache accounting was unavailable.

## Per-question source coverage

Each cell is F / BR. “Met” means the core checklist is covered by source review, with compiler findings incorporated where applicable. “Gap” does not mean every part of an answer is wrong.

| Case | Framework / target | Gemma | Qwen Coder | Qwen3.5 |
| --- | --- | --- | --- | --- |
| GP26-01 · settings controls | UIKit / iOS | gap / gap | gap / gap | gap / gap |
| GP26-02 · cell reconfiguration | UIKit / iOS | met / met | gap / gap | inconclusive / gap |
| GP26-03 · checkout text/layout | UIKit / iOS | gap / gap | gap / gap | gap / gap |
| GP26-04 · visible delete + swipe | SwiftUI / iPadOS | gap / gap | gap / gap | gap / gap |
| GP26-05 · movie activation | SwiftUI / tvOS | met / met | gap / gap | met / gap |
| GP26-06 · native Toggle control | SwiftUI / iOS | met / met | gap / met | met / met |

The UIKit denominator is three families; the SwiftUI denominator is three, including one tvOS family. Do not substitute the repository's new UIKit library results for these generated-answer findings. Full dispositions and cautions are in [source-review.json](source-review.json); exact counts, hashes and compiler errors are in [summary.json](summary.json).

## Findings that matter

- **Container hiding and naming:** Gemma F leaves `accessibilityElementsHidden = true` active. BR clears it, but still omits the switch name. Qwen Coder F names the switch but invents `UIAccessibilityTraits.switch`; BR removes that API error but omits naming. Qwen3.5 F additionally resets switch state as an unsolicited example. Qwen3.5 BR offers an incorrect parent-grouping alternative.
- **Reconfiguration:** Both Gemma variants refresh current customer/priority/status. Qwen Coder F drops priority information; BR relies on `prepareForReuse` while leaving same-instance configuration stale. Qwen3.5 BR assumes an Optional status and fails against the stated String model. Qwen3.5 F changes semantic ownership to the label without establishing that the cell is no longer the exposed owner; this remains inconclusive.
- **Dynamic Type:** No answer fully supplies the recorded live-update contract. Most omit automatic live adjustment. Gemma BR invents `UILabel.adjustsFontForContentSize`; Qwen3.5 BR keeps a fixed 17-point font. Multiline/flexible-layout improvements do not repair those font issues. Proportional horizontal layout is not rejected merely for differing from the reference's vertical layout.
- **Deletion:** Every answer omits the required visible deletion control. Compiler failures include unavailable `.delete` action kinds, invalid action overloads and an invented `AccessibilityAction` constructor. Qwen3.5 F also removes the original swipe handler while claiming to preserve it. No keyboard delivery was tested.
- **tvOS:** Both Gemma answers use native buttons. Qwen Coder BR fixes the action API but leaves remote focus unresolved; F invents SwiftUI `.accessibilityTraits`. Qwen3.5 F's native button and `.borderless` style type-check; BR regresses to a non-focusable container, an invalid closure, and the false idea that `accessibilityIdentifier` supplies a spoken name.
- **Correct-code control:** Compact B improves no-change reasoning. Gemma BR and Qwen3.5 BR correctly preserve the Toggle without code. Qwen Coder BR acknowledges native behavior and suggests an optional override. Qualified optional customization is review burden, whereas Qwen Coder F invents a required missing-value defect.
- **Evidence reporting:** Some answers name unsupplied files, fabricate source URLs, or assert exact speech/keyboard behavior. Repeated identity/routing/footer text is not proof of source use. Compact B intentionally changes those formatting requirements, so legacy protocol compliance is not the source-quality score.

## Compiler evidence

All relevant Swift fences and prose were reviewed. Thirty-four answers contained code; two explicitly supplied alternatives were compiled separately, producing 36 type-check probes. Ten code-bearing answers failed, and two valid no-code no-change answers were marked `not_applicable`. No infrastructure failure occurred in this compiler batch.

The [reviewed-probe runner](../../runner/reviewed-swift-probes.mjs) records exact fences, answer/source hashes, explicit scaffold, commands and diagnostics privately. Scaffold supplies imports and declarations already given by the prompt; imports can move to file scope. It adds no missing live-update setting, native button, swipe handler, state repair or callback wiring. Full declarations and body fragments use reviewed containing context; alternatives are not concatenated into duplicate declarations. Compilation remains a bounded snippet check, rather than proof that a drop-in application patch works.

Environment: Xcode 27.0 (27A266a), Apple Swift 6.4, Swift language mode 6; iOS Simulator SDK 27.0 (24A430) and tvOS Simulator SDK 27.0 (24J360), targeting arm64 OS 26.0 simulators. No generated answer was executed in a simulator or unit test. There is no generated-answer evidence for rendered layout, actual input delivery, VoiceOver speech/traversal or remote focus.

## Provenance and comparison limits

Input checkpoint: `a95464ccd2fbc639164bb8f373c5e1a2594e1002`. Catalog: `os26-code-contract-4-closeout-1`; the six user question strings are unchanged. All model digests, quantizations, instruction/reference/payload/answer hashes and token counts are retained. Conditions alternate which entrypoint runs first across cases; sessions are fresh and tool-free, with one model loaded at a time.

The supplied references match the previous local diagnostic's topic selection, using current runtime bytes held identical across each new pair. Some guidance, particularly tvOS, is UIKit-oriented despite SwiftUI subject code. This tests those supplied contexts; it cannot establish the best reference choice or autonomous retrieval. No proposed reference edits from candidate B's controller notes were applied.

The older 900-token local results and frontier compact-A report use different wrappers, reference snapshots, entrypoints or grading procedures. They are context, not matched controls for this run. These six known development families cannot establish general model rankings, statistical superiority or release noninferiority. B remains a draft with separate independent adjudication and transparency-contract work pending.

The executing inference-controller snapshot is preserved with its exact hash. An offline-plan stdout-flush bug was corrected while the batch ran; that branch does not execute during inference, and the live generation path and frozen payloads were unchanged. The original first outcomes remain intact.

While this batch ran, `origin/main` advanced to `f92c52f`, adding AppKit/tvOS companion evidence. Those new cases and native results are outside this pinned comparison; they were not silently added to the corpus.

## Reproduction and retained evidence

Print the bounded local plan or run a separately authorized repeat into a new private directory:

```sh
node evals/runner/local-os26-comparison.mjs
node evals/runner/local-os26-comparison.mjs --execute /private/tmp/<new-run-directory>
node --test evals/runner/local-os26-comparison-test.mjs evals/runner/reviewed-swift-probes-test.mjs
```

The default command makes no inference call. Execution allows 36 generations, 180 seconds per request, a one-hour dispatch deadline, no application retries or fallbacks, and serial local Ollama access. Tags must already be installed; their digests are checked before and after generation. Changed pinned inputs stop the batch. A future run uses then-current source bytes and needs its own recorded version; it is not automatically a replay of this frozen payload set.

Private raw responses, frozen payloads, exact model metadata, executing controller, reviewed adaptation plans and compiler evidence are retained under ignored `evals/results/local-compact-b-20261106-r1/`. Public files contain sanitized summaries and hashes. Seven new offline runner/probe tests and 28 existing OS26 contract/integrity tests passed. Runtime skill files, frozen baselines and prior reports were preserved.

Capture limits: the private bundle retains expanded subject messages, supplied references, settings, original response JSON and analysis artifacts. Exact HTTP request bytes, server-internal rendered context, and full provider requests for maintainer authoring/judging were not exported and remain unavailable in this bundle. The visible chat is not represented as a complete provider-context transcript. The source review records its criteria and findings, with no independent judge-model invocation or repair attempt.

Use these local models for diagnostic failure discovery with compiler and source review. Continue independent candidate review and qualified-model testing before considering any runtime skill replacement.
