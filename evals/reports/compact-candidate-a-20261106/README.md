# Compact skill comparison · 6 November 2026

**144/144 calls completed · 144 source reviews · no retries · raw answers private.**

N = no skill · F = frozen skill + reference · A = compact skill alone · AR = compact skill + the same reference. Each cell covers the same 18 cases, one answer per case.

## At a glance

| Condition | AGY Flash | Haiku |
|---|---:|---:|
| No skill | 13/18 · 48.4k tokens | 15/18 · 41.4k tokens |
| Full skill + reference | 14/18 · 97.7k tokens | 16/18 · 130.5k tokens |
| **Compact alone** | **15/18 · 64.8k tokens** | **17/18 · 72.0k tokens** |
| Compact + reference | 15/18 · 79.8k tokens | 16/18 · 98.5k tokens |

**Read these as core-contract source grades, not flawless answers or native test passes.** One unblinded maintainer-agent reviewed the actual answers against the frozen criteria. No generated answer was compiled or executed.

## Does compacting help?

| Comparison against F | AGY Flash | Haiku |
|---|---:|---:|
| Compact alone | 33.6% fewer tokens; +1 passes | 44.8% fewer tokens; +1 passes |
| Compact + same reference | 18.3% fewer tokens; +1 passes | 24.5% fewer tokens; +0 passes |

A versus F changes both entrypoint length and reference inclusion. **AR versus F is the controlled entrypoint comparison with references held constant:** 18.3% fewer tokens on AGY with one additional pass; 24.5% fewer on Haiku with the same pass total but different cases passing.

**Recommendation: retain the compact candidate for independent confirmation; do not promote it yet.** Compacting reduces measured tokens, but reference effects differ by case and model. A single development sample does not justify model-specific forks or statistical superiority. Preserve the full/reference baseline and investigate the concrete regressions before changing the released skill.

The useful signal is specific: compact Haiku accepts the valid Slider, while full Haiku invents a defect. Compact-only AGY accepts the valid Reduce Motion implementation; both reference-supplied variants invent a transition defect. All eight conditions solve the focus-restoration, popup-state, adjustable-knob and download-state contracts by source review. Checkout remains weak, especially integration of local variables with lifecycle callbacks.

## Where answers passed

| Model / condition | Existing gold code /6 | Exploratory code /6 | Evidence questions /6 |
|---|---:|---:|---:|
| AGY Flash N | 4 | 4 | 5 |
| AGY Flash F | 5 | 4 | 5 |
| AGY Flash A | 5 | 5 | 5 |
| AGY Flash AR | 6 | 4 | 5 |
| Haiku N | 4 | 5 | 6 |
| Haiku F | 5 | 5 | 6 |
| Haiku A | 5 | 6 | 6 |
| Haiku AR | 4 | 6 | 6 |

## Question-by-question

Questions below are short summaries; complete frozen inputs are identified by the [approved batch](../../../research/evaluation/failure-driven/compact-candidate-a/BATCH.json). ✓ = core contract met; ✕ = material gap. Each four-symbol cell is ordered **N / F / A / AR**.

| Question | AGY N/F/A/AR | Haiku N/F/A/AR |
|---|---|---|
| **GP26-01** · How should a settings row expose its switch and help button? | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ |
| **GP26-02** · How do reused labels keep the current name and status? | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ **✕** |
| **GP26-03** · How can checkout handle large text without changing Pay? | ✓ **✕** **✕** ✓ | **✕** **✕** **✕** **✕** |
| **GP26-04** · How can a message be deleted without swiping? | **✕** ✓ ✓ ✓ | **✕** ✓ ✓ ✓ |
| **GP26-05** · How should a tvOS poster expose its title and activation? | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ |
| **GP26-06** · Does this native notifications Toggle need a fix? | **✕** ✓ ✓ ✓ | ✓ ✓ ✓ ✓ |
| **GP26-07** · How do we restore focus to the current row after dismissal? | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ |
| **GP26-08** · How do we contain a popup and restore the prior hidden state? | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ |
| **GP26-09** · How do we make a custom volume knob adjustable? | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ |
| **GP26-10** · How do we announce only the first download outcome? | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ |
| **GP26-11** · Does this already-working native Slider need a fix? | **✕** **✕** **✕** **✕** | **✕** **✕** ✓ ✓ |
| **GP26-12** · Does this Reduce Motion implementation need a fix? | **✕** **✕** ✓ **✕** | ✓ ✓ ✓ ✓ |
| **EV01** · Can a screenshot prove the Pay button works with VoiceOver? | **✕** ✓ **✕** **✕** | ✓ ✓ ✓ ✓ |
| **EV02** · What can a clean accessibility audit actually establish? | ✓ **✕** ✓ ✓ | ✓ ✓ ✓ ✓ |
| **EV03** · Can we verify a claim without the referenced document? | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ |
| **EV04** · What evidence supports a claimed OS behavior change? | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ |
| **EV05** · How should SDK, deployment target and tested runtime be reported? | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ |
| **EV06** · Do compile and direct-callback checks prove real activation? | ✓ ✓ ✓ ✓ | ✓ ✓ ✓ ✓ |

## Error flags, separate from pass counts

| Source-review finding | Answers flagged | Meaning |
|---|---:|---|
| Invented defect on valid Slider / Reduce Motion controls | 9/16 | AGY 7/8; Haiku 2/8. Compact Haiku avoids both; AGY compact alone avoids only the motion false positive. |
| Evidence checklist not fully satisfied | 4/48 | Three incomplete activation-evidence requests; one audit result overstated in release wording. |
| Missing checkout scope / lifecycle integration | 4/8 | All four Haiku variants; exact generated code not compiled here. |
| Unsupported action API recommendation | 2/144 | One primary deletion action-kind error, one optional settings-row activation assignment. Candidate critical-error flags pending independent adjudication; the latter remains a core pass. |

These counts overlap core failures and include one optional-path issue. They are recorded flags, not a calibrated exhaustive critical-error rate. Unsupported runtime guarantees and unnecessary edits are retained as cautions; no fabricated numerical total is assigned to those broader categories.

<details>
<summary>Every failed answer and review cautions</summary>

## Material gaps and review cautions

These are reviewer findings, not compiler diagnostics. Optional bad advice can coexist with a core pass under the predeclared policy. The following table preserves every core failure; it is not an exhaustive count of all unsupported wording.

| Answer | Why it did not meet the core contract |
|---|---|
| EV01-N-agy | Rejects screenshot proof but offers hierarchy alone or interaction recording as interchangeable sufficient artifacts; hierarchy alone does not establish operation. |
| EV01-A-agy | Requests hierarchy/source only and leaves interaction unverified without requesting operation evidence; omits the required minimal evidence for broader claim. |
| EV01-AR-agy | Requests hierarchy and traversal graph, but not activation evidence; incomplete support for works-with-VoiceOver claim. |
| EV02-F-agy | Rejects full conformance, but release note upgrades zero missing-label/low-contrast findings to requirements met; invents primary-element scope. |
| GP26-02-AR-haiku | Primary fix clears nonpriority status instead of exposing current status required by frozen reconfiguration oracle; optional suggestion does not repair primary answer. |
| GP26-03-F-agy | Changes Pay button font despite preservation requirement; live trait update left as assumed instruction instead of integrated implementation. |
| GP26-03-A-agy | Primary remains proportional horizontal layout with no button-width protection; extreme-size reflow left as optional unintegrated callback note. Long-total requirement not concretely resolved. |
| GP26-03-A-haiku | Local updateSummaryAxis function captures local summary but callback calls self.updateSummaryAxis; missing member/scope integration cannot be silently repaired. |
| GP26-03-AR-haiku | Local summary then separate controller override references undeclared member; initial-axis implementation left to reader. Also misstates original stack-height constraint as button-height change. |
| GP26-03-N-haiku | Local summary then separate override references missing member storage; no silent scope repair. Competing required horizontal resistance also needs layout review. |
| GP26-03-F-haiku | Setup statements/local summary mixed with private member and override without explicit member storage/integration. Required initial layout call remains prose; source cannot be silently repaired. |
| GP26-04-N-agy | Primary code uses AccessibilityActionKind.destructive, absent from Apple action-kind reference; confuses ButtonRole with action kind. Combines children while claiming separate discovery. Not native compiled. |
| GP26-04-N-haiku | Primary code adds identical unscoped Delete shortcut to each row; does not bind shortcut to intended focused message. Acknowledges unexpected-focus conflict but leaves it in implementation; targeted activation contract unresolved. |
| GP26-06-N-agy | Recognizes valid native Toggle but primary improved code invents all notifications/updates/alerts/badges semantics without product evidence; no caveat on supplied copy. |
| GP26-11-N-agy | Invents insufficient native Slider speech/value as a concrete defect without evidence; missing explicit accessibilityValue is not a defect. Binding/range/step preserved, but unnecessary repair fails the no-change control. |
| GP26-11-F-agy | Invents insufficient native Slider speech/value as a concrete defect without evidence; missing explicit accessibilityValue is not a defect. Binding/range/step preserved, but unnecessary repair fails the no-change control. |
| GP26-11-A-agy | Invents insufficient native Slider speech/value as a concrete defect without evidence; missing explicit accessibilityValue is not a defect. Binding/range/step preserved, but unnecessary repair fails the no-change control. |
| GP26-11-AR-agy | Invents insufficient native Slider speech/value as a concrete defect without evidence; missing explicit accessibilityValue is not a defect. Binding/range/step preserved, but unnecessary repair fails the no-change control. |
| GP26-11-N-haiku | Treats native Slider value as a concrete missing/unclear accessibility defect without evidence, despite uncertainty caveat. Unchanged native control is valid; binding/range/step preserved. |
| GP26-11-F-haiku | Treats native Slider value as a concrete missing/unclear accessibility defect without evidence, despite uncertainty caveat. Unchanged native control is valid; binding/range/step preserved. |
| GP26-12-F-agy | Invents continuing slide/motion artifacts despite explicit nil-animation and no-ambient-animation assumptions; prescribes unnecessary transition replacement for a valid no-change control. |
| GP26-12-AR-agy | Invents continuing slide/motion artifacts despite explicit nil-animation and no-ambient-animation assumptions; prescribes unnecessary transition replacement for a valid no-change control. |
| GP26-12-N-agy | Invents continuing slide/motion artifacts despite explicit nil-animation and no-ambient-animation assumptions; prescribes unnecessary transition replacement for a valid no-change control. |

Additional cautions retained in private review records: AGY’s no-skill settings-row answer included an invalid optional activation assignment despite a valid primary fix; some answers offered unnecessary UI/manual testing, overpromised actual focus/speech, or changed copy and layout beyond the request. These do not disappear because the core task passed. The deletion action-kind finding is checked against [Apple’s AccessibilityActionKind reference](https://developer.apple.com/documentation/swiftui/accessibilityactionkind); it is not a native compiler result.

Borderline findings needing second review include the screenshot evidence request, horizontal checkout alternative and per-row Delete keyboard shortcut. Do not silently repair missing storage/lifecycle integration when grading checkout answers. Keep optional suggestions separate from the primary implementation.

</details>

<details>
<summary>Exact token counts, cache accounting and latency</summary>

## Measured tokens and time

| Model / condition | Input incl. cache | Output incl. thinking | Total | Thinking subset | Median seconds |
|---|---:|---:|---:|---:|---:|
| AGY Flash N | 40,463 | 7,926 | 48,389 | 0 | 8.81 |
| AGY Flash F | 87,520 | 10,148 | 97,668 | 0 | 10.04 |
| AGY Flash A | 56,069 | 8,755 | 64,824 | 0 | 9.62 |
| AGY Flash AR | 70,693 | 9,062 | 79,755 | 0 | 8.90 |
| Haiku N | 16,862 | 24,508 | 41,370 | 12,286 | 7.58 |
| Haiku F | 91,326 | 39,177 | 130,503 | 23,262 | 10.97 |
| Haiku A | 42,620 | 29,415 | 72,035 | 15,608 | 9.80 |
| Haiku AR | 66,864 | 31,617 | 98,481 | 16,982 | 8.83 |

**Batch total: 633,025 reported tokens.** No API-dollar estimate is treated as subscription spend. Thinking tokens are already included in output and are not added twice.

Claude input totals include uncached input + cache creation + cache reads; AGY input is its reported input total. Both routes reported zero cache reads in this run. Claude cache creation remains input usage, not a cache hit discount. Provider tokenization, hidden wrappers and accounting differ: compare conditions within a model, not raw cross-provider totals as a model-efficiency ranking.

| Model | Uncached reported input | Cache creation | Cache reads |
|---|---:|---:|---:|
| AGY Flash | 254,745 | not separately reported | 0 |
| Haiku | 144 | 217,528 | 0 |

Output target was 1,024 tokens, **not a hard cap**; receipts above that target are included. Owner accepted unavailable hard token caps. The measured stop threshold was 2 million total tokens before another dispatch; the batch remained below it. Prompt-byte ceiling 20 KiB, per-call deadline 120 seconds, captured-output bound 1 MiB.

</details>

## Formatting protocol, separately measured

Full-skill answers emitted the exact skill/version identity in 18/18 answers per model. Literal routing/footer markers appeared in 17/18 AGY answers and 15/18 Haiku answers. This is a text-presence check, not validated routing or source access. All compact answers omitted the legacy identity/routing/footer markers as intended by the candidate. Removing that protocol is still a proposed contract change, not an automatically accepted release improvement.

## Quota snapshots

Claude used: **session 0% → 2%; weekly 14% → 14%**, at whole-percent precision. Before values came from the owner display; after values were read directly through the documented interactive CLI `/usage`, after its refresh. Usage credits showed OFF. The quota check reported zero model input/output tokens and zero API duration. These are account-wide snapshots, not an exact isolated batch debit. The displayed session bucket is not relabeled as a documented five-hour bucket. The old $1.92 CLI session display is not this batch’s cost.

**AGY weekly remaining: 66% → 66%; five-hour remaining: 100% → 98% (2 percentage points consumed on the display).** Both snapshots came from the documented CLI usage command, without inference. Whole-percent account snapshots are coarse and may include concurrent use; they are not exact per-batch billing or token rates.

## Scope and reproducibility

- Exactly 18 fixed development cases × 4 conditions × 2 models = 144. No warmups, repairs, model judges, new holdouts or automatic retries.
- Models: AGY `gemini-3.8-flash-low` and Claude `claude-haiku-5-5`, low effort, documented subscription CLI routes; no API-key fallback. Claude returned the pinned model in every receipt; AGY was pinned in the invocation and availability check, without a separate returned model identity.
- Candidate and batch published at `d93efa9`; frozen comparison selection reviewed against `f0bfc51`. Report prepared after preserving new upstream media work at `6cdaa0b`; that new work was not injected into these frozen cases.
- All 144 prompt hashes, unique job identities, successful receipts, token sums and reviewed answer hashes checked. Same user task across conditions; N/F historical payloads preserved; A/AR change only the entrypoint body and retain frozen metadata.
- F and AR use the same manually selected reference. Reference retrieval and installed-agent routing were not tested. The historical cross-framework progress reference remains disclosed.
- No native execution of generated answers. Existing fixture checks do not transfer to generated code. Exploratory cases remain exploratory; no platform-wide qualification.
- One source reviewer, unblinded; independent calibration and disputed-case adjudication remain pending. One sample per case; no confidence or significance claim. No weighted calibrated quality score is invented.
- Raw prompts, answers, receipts and account configuration remain private. Only aggregate metrics and reviewer summaries are published. Prior reports and released skill files remain unchanged.

## Next steps

1. Independently review the disputed answers and compile exact checkout/deletion outputs against the intended targets without silent repair; keep first attempts intact.
2. Use the results to propose minimal entrypoint/reference changes: protect existing behavior, accept valid no-change answers, require integrated code, and distinguish configured state from actual interaction.
3. Freeze the next candidate and a fresh confirmation set before requesting a separate bounded run. Do not optimize against the same development answers repeatedly.
4. Retain a compact shared core and on-demand target guidance; these two model samples do not justify separate model-specific skill variants.

**Owner next:** review the tradeoffs; no manual quota reading is needed. **Assistant next:** prepare the independent-review packet and concrete revision proposal; no further model runs or released-skill changes without approval.
