# Signal-v6: research candidate for passing the 56-question panel

[Candidate](candidate.zip) `de259a35…`, built by `build.py` from signal-v5 `8ed8f947…`. This is a draft; it has not been measured. Released 0.2.2 and all earlier candidates are unchanged.

| Card | Change | Targets (families that failed primary in every earlier arm, or a confirmed v4 regression) |
|---|---|---|
| Entry | Decide whether a fix is needed before writing one, and change nothing if the code works. Changes fit the supplied files and show their production call site. A four-step proof contract. | 17 verification-only failures; 7/23 v4 proofs that did not compile |
| Return | Removed "consume its return request before calling reentrant code". The presentation carries its owner (`sheet(item:)` or a token captured at open). Eligibility and refusal are separate fallback rules. Apply-and-close is kept. | restore-only-owned-sheet ×3, refusing-focus-target, restore-accessibility-background |
| Media | Distinct load states with retry. Membership validated before writing. Same-item reload, cancellation and replacement retire old setters and completions. Chapter: stay put at the edges, do nothing with no chapters. | stale-off-capture ×2, same-item-new-request, missing-item-vs-no-options, selection-before-validation, chapter-boundary |
| Validation | A retired reply applies no error, and Submit becomes available again | validation-busy-recovery, input-snapshot-after-edit |
| Actions | Reconfigure without re-adding targets. Outline identity, selection by ID and removed handles. | duplicate-dispatch-on-reuse (critical), duplicate-ordinary-command, retired-outline-handle |
| Facts | `NSAccessibilityCustomAction` API, the SwiftUI macOS editable child, keeping a native `Slider`, the selected trait on reconfigure | native-custom-action-api, native-editable-child, preserve-native-slider ×2, selected-trait-vs-selection |

**Unchanged from v5:**
- The examples are byte-identical. The SheetOwner excerpt keeps its qualification: in `evals/native-calibration/sheet-dismissal`, owned passes and shared-ticket fails on iOS, macOS and tvOS.
- Font and the description are also unchanged.

**Size:** entry 2,111 B; total 14,846 B (limits 2,200 / 15,000). The build guards against leaking panel IDs, rubrics or oracles. `screen.py` fails if new card text shares an 8-word run with any panel question, rubric, criterion, calibration note or preserved v4 answer; it passes against 255 texts.

**Offline checks done:**
- `build.py --check`.
- Typecheck of every new API claim on macOS, iOS and tvOS 26: NSAccessibilityCustomAction in both forms, nil help, `editCategory` assignment, `sheet(item:)`.
  - Sources: `evals/results/signal-v6-offline/`.

**Not yet done:** any model measurement. These cards were written from development cases, which are not holdouts, so a panel gain alone does not justify promotion.

## Run 1 (submitted; worker acceptance pending)

**Packet:** [readiness/held.zip](readiness/held.zip), seal `1b865cef…`, rebuilt by `readiness/seal.py --check`.
- **Arms:** unaided, released 0.2.2, signal-v6.
- **Questions:** 56.
- **Trials:** 3, so 504 cells, with counterbalanced arm order.
- **Grading:** one source pass per component, with twins hidden from the grader.
- **Checker:** `readiness/check_return.py` rejects missing cells and component reasons copied across components. It was rehearsed on synthetic returns.
- **Analysis:** `analyze.py` covers trial-majority verdicts, exact sign tests against the release and against unaided, per-arm self-agreement across trials, the exposure split, tokens, critical flags, and the panel gate. A planted synthetic effect is recovered exactly.

**After return:**
- `evals/qualification-56/grade_run.py RETURN SHA` stages every cell with one arm-blind selection rule, and `research/evaluation/signal-panel-v4/replay/native.py` runs the qualified controls.
- **Calibration on the v4 return:**
  - 84/112 staged subjects are byte-identical to the hand-selected ones.
  - In 6 cells the mechanical subject fails to typecheck where the hand choice compiled. Report compiled contract verdicts separately from source grades in every arm. Neither failed extraction nor a narrow unit pass rewrites the source grade.
  - Diff-only answers are ambiguous.
- **Native coverage:** only 45/112 v4 cells reached a compiled contract verdict. Native grading therefore checks roughly 40% of answers; the 47 qualified controls validate the oracles, not answers directly.
- **Collecting results:** `grade_run.py --collect BATCH` writes `native.json` for `analyze.py`.

**Dispatch:** Coordinator receipt 1507, operation `signal-v6-run1-1b865cef-r1`, stored once. This receipt does not establish delivery, worker acceptance or completed sessions.

[Decision log](DECISIONS.md)

**Release comparison:** 56 development questions across three arms and three trials, with subscription quota only. The former v2 packet remains archived; it was not sent. Return one consolidated report. No transfer or release claim from this panel alone.
