# AGY expanded baseline — 72 new conversations

**Result: a narrow benefit, not a broad win. The skill preserved the valid Toggle in 3/3 answers versus 0/3 without it, but used 1.97× total tokens across the new campaign.**

C0 = baseline assistant. C2 = frozen skill 0.2.2 plus evaluator-selected reference. Model: `gemini-3.8-flash-low`, low effort. Frozen source: `e493802`.

| Measure | C0 · no skill | C2 · with skill |
|---|---:|---:|
| Existing gold code, three repetitions | 13/18 | 15/18 |
| New exploratory code, three repetitions | 12/18 | 13/18 |
| Evidence questions, all four criteria met | 4/6 | 4/6 |
| New campaign calls completed | 36/36 | 36/36 |
| New campaign total tokens | 98,578 | 194,158 |
| Mean call latency | 7.84 s | 9.11 s |

“Meets” means the primary answer satisfies the frozen source-review criteria. It does **not** mean compiled, fully correct in every optional recommendation, or verified with assistive technology. Incorrect alternatives are retained as flags, not silently repaired. The existing-gold row includes 12 previously collected answers; all other answers are new. The review corpus is 84 answers; the subscription campaign made 72 calls.

## Code results at a glance

Counts show core criteria met out of three responses. Gold fixtures and generated-answer validation are separate. New cases remain exploratory and are not promoted by these scores.

| Case / developer task | C0 | C2 | What the comparison shows |
|---|---:|---:|---|
| GP26-01 · Restore access to settings switch and Help | 3/3 | 3/3 | Both restore access; runtime traversal untested. |
| GP26-02 · Clear stale accessibility data on reused cells | 3/3 | 3/3 | Primary fixes work; some optional reset-only alternatives remain wrong. |
| GP26-03 · Fix large text without changing Pay appearance | 1/3 | 0/3 | C0: shrink-to-fit/scope problems. C2: appearance changes/scope problems. |
| GP26-04 · Expose deletion without requiring swipe | 3/3 | 3/3 | Both preserve ID-based deletion; actual keyboard/VoiceOver use untested. |
| GP26-05 · Preserve tvOS navigation and controls | 3/3 | 3/3 | Both meet core; baseline adds more unrelated UI changes. |
| GP26-06 · Review an already-correct native Toggle | 0/3 | 3/3 | Clear repeatable skill benefit: preserves valid control instead of inventing behavior. |
| GP26-07 · Restore focus after asynchronous dismissal | 3/3 | 3/3 | Both resolve current target after completion; actual focus untested. |
| GP26-08 · Restore popup background accessibility state | 3/3 | 3/3 | Both preserve prior state and repeat-safe lifecycle. |
| GP26-09 · Implement adjustable knob steps and callbacks | 3/3 | 3/3 | Both use real adjustment hooks and suppress unchanged callbacks. |
| GP26-10 · Deduplicate progress completion announcements | 3/3 | 3/3 | Both guard active IDs and terminal callbacks. |
| GP26-11 · Review an already-correct native Slider | 0/3 | 1/3 | Both usually invent a defect; one C2 response offers qualified optional formatting. |
| GP26-12 · Review existing reduced-motion behavior | 0/3 | 0/3 | Both claim a defect without evidence under the supplied transaction assumptions. |

Read the actual prompts and code: [GoldPrompts.md](../../../GoldPrompts.md) and [six exploratory prompts](../../os26/expansion-1/PROMPTS.md). GP26-01–06 are the existing gold lane; GP26-07–12 are exploratory.

## Evidence questions

| Question | C0 | C2 | Review finding |
|---|---:|---:|---|
| Can a screenshot prove the Pay button has a useful accessibility name and works with VoiceOver? | 3/4 | 3/4 | Both reject the claim but offer an evidence alternative insufficient to establish actual operation. |
| Do zero findings from 12 label/contrast checks establish full accessibility? Write a release note. | 3/4 | 2/4 | Both reject full accessibility but invent that remaining testing is “in progress”; C2 also drops the precise count/result. |
| Can unavailable AppControls.md confirm exactly-once accessibility activation? | 4/4 | 4/4 | Both leave the missing-document claim unverified. |
| Should an unverified forum claim justify removing a payment accessibility workaround? | 4/4 | 4/4 | Both request versioned reproduction and supported-configuration regression checks. |
| Does an SDK27 build tested on simulator26.5 verify deployment target26.0 and every later version? | 4/4 | 4/4 | Both reject the inference and provide a runtime-bounded unit-test rewrite. |
| Does compilation plus a direct delete-handler test establish keyboard/VoiceOver discovery and activation? | 4/4 | 4/4 | Both preserve the useful unit result while withholding the interaction claim. |

Checklist passes do not certify every sentence: C0's short SDK rewrite is broader than its detailed alternative; C2's delete answer adds an unsupported absence-of-side-effects assurance. Protocol headers, citations and freshness labels are not verification.

## Usage and execution

72/72 calls completed successfully; no retries, fallback, tools or model judging. Input/output tokens: C0 **82,157 / 16,421**; C2 **172,011 / 22,147**. Total **292,736 tokens**, about **610 seconds** summed call latency. C2 input was 2.09× and output 1.35× C0. These are reported inference tokens, not a conversion to subscription quota or money.

CLI quota display: weekly **66% → 66%**, five-hour **100% → 98%**. The display uses whole percentages, so an exact weekly debit cannot be determined; unchanged display does not mean free usage.

Frozen prompt hashes, all 72 output hashes, all 72 successful receipts and complete review coverage were checked. Full prompts-as-sent, generated replies, receipts and per-answer assessments remain private. Existing reports and the skill are unchanged.

## What to change next

1. **Require a concrete defect before changing code.** Preserve correct native controls and the stated transaction context; optional polish must not be called a fix.
2. **Treat preservation requirements as acceptance checks.** Verify identifiers, callbacks, appearance and scope in every proposed snippet and alternative.
3. **Make reporting evidence-bounded.** Never invent tests “in progress,” infer UI behavior from direct callbacks, or present a reference/freshness banner as proof.
4. **Reduce mandatory prompt and response overhead.** Keep a compact decision policy; retrieve only relevant references. Test that candidate against the frozen baseline, rather than assuming shorter means better.
5. **Qualify generated code on Apple hosts.** Sillycon's separate library progress does not qualify these responses. Freeze an explicit adaptation contract, preserve failed originals, and record compile/unit/UI/assistive evidence separately.

## Limits and next steps

This is one unblinded source review on a small development set, with three samples per code case—not a statistically established improvement. Historical first-round assessments were retained; their missing dimensional scores were not invented. No native generated-answer execution or actual VoiceOver/keyboard qualification is claimed. The new draft cases need independent review and Apple validation. Valid alternative implementations are allowed; optional changes are not automatically failures. C2 references were selected by the evaluator, so this does not test agent retrieval or isolate the effect of the bootstrap from the reference. The progress case used frozen SwiftUI guidance for UIKit code; that mismatch remains a limitation.

**Assistant next:** obtain Sillycon's exact fixture acceptance/evidence, resolve disputed source judgments, then prepare one compact skill candidate and a consolidated comparison plan. No further provider run is authorized by completion of this campaign.

**Owner next:** review the repeated failures and the proposed priorities above. No setup action is needed for this completed run; approve the next skill version and its bounded test campaign when the complete proposal is ready.
