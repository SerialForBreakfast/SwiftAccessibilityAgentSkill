# Local OS26 model and code-gate results

Date: 2026-11-05  
Repository commit: `b0f4e449d22086fcce87765c154d390507c31b75`  
Scope: diagnostic local testing of the six `os26-code-contract-4` prompts.

This report is not a gold-promotion receipt, a release gate, or a formal model-quality score. The prompts are development cases, the native run is partial, and semantic judgments are descriptive manual review.

## Local model batch

The six exact user prompts from `GoldPrompts.md` were sent serially through Ollama with the current `SKILL.md` and the routed topic references supplied in the system context.

Settings: 16,384 context, 900 output-token cap, temperature 0, seed 42, thinking disabled, no provider calls, no downloads.

| Model | Completed | Truncated | Avg. time | Routed references | Protocol observations |
| --- | ---: | ---: | ---: | ---: | --- |
| `qwen2.5-coder:14b` | 6/6 | 0 | 71.0 s | 6/6 | Routing 2/6; identity/footer 0/6 |
| `gemma4:12b` | 6/6 | 0 | 96.3 s | 6/6 | Identity/footer 6/6; routing-first 0/6 |
| `qwen3.5:latest` | 6/6 | 1 | 54.1 s | 6/6 | Routing 6/6; footer 5/6; identity 0/6 |

Protocol observations are not quality scores. Gemma was the most consistent at following the skill's trust-footer behavior, while Qwen3.5 was the most consistent at placing the routing line first.

## Compile/API gate

`evals/runner/local-os26-code-gate.mjs` extracts the first Swift code block from each answer and type-checks it against the installed Xcode 27 simulator SDKs while targeting iOS 26.0 or tvOS 26.0. It also records high-value static hazards. The gate does not prove runtime behavior, VoiceOver traversal, keyboard delivery, remote focus, or rendered layout.

| Model | Extracted blocks | Type-checked | Main compiler/API findings |
| --- | ---: | ---: | --- |
| `qwen2.5-coder:14b` | 6/6 | 4/6 | `.accessibilityAction(.delete)` is unavailable on iOS; `.accessibilityTraits(.button)` is not a SwiftUI modifier |
| `gemma4:12b` | 6/6 | 5/6 | GP26-04 uses an invalid `accessibilityAction` call signature |
| `qwen3.5:latest` | 5/6 | 3/5 | GP26-04 and GP26-05 use invalid string/action overloads; GP26-06 emitted no Swift block |

The compiler gate confirms that fluent answers can contain non-compiling Swift even when the surrounding explanation is plausible.

## Semantic review findings

- GP26-01: Gemma and Qwen14 correctly remove container-level grouping. Qwen3.5 reintroduces `accessibilityElementsHidden = true`, which hides descendants and conflicts with its own fix.
- GP26-02: Gemma correctly resets the label and status on every configuration. Qwen14 resets the state but drops the priority distinction. Qwen3.5 incorrectly treats the status as inappropriate cell content and fails to update the cell's exposed semantics.
- GP26-03: Gemma provides the strongest fix: preferred Dynamic Type font, multiline label, `.fill`, and no fixed height. Qwen14 adds an undefined `view` reference in a supposedly drop-in snippet. Qwen3.5 keeps a fixed font and incorrectly claims that `systemFont(ofSize:)` automatically follows Dynamic Type.
- GP26-04: None of the three answers fully satisfies the requirement as written. Qwen14 at least adds a visible `Button`, but its delete accessibility action is unavailable on iOS. Gemma and Qwen3.5 expose only an accessibility action and do not provide the requested visible keyboard-focusable control.
- GP26-05: Gemma is the only answer that uses a native `Button` for tvOS remote focus and activation. Qwen14 and Qwen3.5 retain gesture activation; Qwen14 also emits an invalid modifier.
- GP26-06: Qwen3.5 correctly recognizes that the native `Toggle` needs no change. Gemma and Qwen14 add unnecessary explicit accessibility values to a control that already exposes its state.

Current recommendation: use Gemma for review drafts only, with mandatory compile/API validation and human semantic review. Do not permit any of these local models to apply Swift accessibility edits autonomously.

## Native fixture validation

The repository's offline contract suite passed 28/28 tests, and `node evals/runner/check.mjs` passed. The native runner used iOS 26.5 and tvOS 26.5 simulators with Xcode 27 / SDK 27, targeting OS 26 deployment.

The run stopped after GP26-02 mutation-2:

| Case | Observed |
| --- | --- |
| GP26-01 candidate | pass |
| GP26-01 mutation-1 | expected assertion failure |
| GP26-01 mutation-2 | expected assertion failure |
| GP26-02 candidate | pass |
| GP26-02 mutation-1 | expected assertion failure |
| GP26-02 mutation-2 | test emitted the expected stale-status failures, but `xcodebuild` hung while finalizing the result bundle; classified as infrastructure error |

The native run therefore does not establish any of the six cases as gold-ready. It also does not assess VoiceOver speech/traversal, Full Keyboard Access delivery, tvOS remote focus, or rendered layout.

## Reproduction

Run the offline checks:

```sh
node --test evals/runner/os26-test.mjs evals/runner/os26-fixtures-test.mjs
node evals/runner/check.mjs
```

Run the compile/API gate against private Ollama records:

```sh
node evals/runner/local-os26-code-gate.mjs \
  --records /private/tmp/<local-os26-run>/records.jsonl \
  --records /private/tmp/<qwen35-run>/records.jsonl \
  --out /private/tmp/local-os26-code-gate.json
```

The raw model records, generated probe sources, compiler diagnostics, and native xcresults remain outside Git because they contain machine-specific paths and are diagnostic evidence only.
