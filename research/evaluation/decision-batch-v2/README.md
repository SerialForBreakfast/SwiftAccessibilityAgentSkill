# Decision batch v2: eight regressions, six repair areas

Research candidate only. The installed default is 0.2.2. Decision batch v1 was measured against it on 62 development questions; v2 has **no model answers**. The changes below repair guidance, not historical scores. Do not add eight passes to v1's 27/62.

| Returned case suffix/prefix | Why v1 lost whole-task credit | New decision and distinguishing control |
|---|---|---|
| 20d89c (tvOS) | Attachment displaced the enabled guard. | Check registration ownership AND permission. Invoke the retained action directly while attached but disabled; then re-enable and use normal activation. A removed-ID check alone is vacuous. |
| f32498 (Mac) | An old Delete could remove today's equal-looking document. | Replace with the exact same value and ID. Deliver old Delete, then current Select and Delete; distinguish registration lifetimes, not value equality. |
| 5e4a6e (Mac) | Typing established editability but could not distinguish the two proposed causes. | Change only redundant sibling semantics, then independently isolate the surrounding container's synthesized element. Report attribution conditionally when the hierarchy is absent. |
| cc39f5 (Mac) | Hiding the representable could hide the editor itself. | Scope exclusion to the decorative sibling or remove the redundant ancestor configuration. The editor, insertion, selection and ordinary Clear path remain requirements. |
| 03bf42 (iOS) | Grapheme counts changed an otherwise correct native text range. | For the supplied NSString search use its UTF-16 start and exclusive end in the same live UITextView. Query the returned substring after an emoji and combining prefix. |
| 1c8e58 (Mac) | Ignoring the row lost the requested semantics while child Open still worked. | Assert element exposure as well as selected role data and the native child; dispatch Open on that child. Do not generalize a leaf/container rule from UIKit. |
| 222d72 (Mac) | The proposed mock or getter could not show what the real player item selected. | Supply a bundled movie; load the legible group from that item and read its current selection. Test forced-first order explicitly, not merely the existence of a forced track. |
| 3d41fd (Mac) | The answer used the wrong audio characteristic. | Inspect .describesVideoForAccessibility on each audible option. Compare the Spanish tagged option with its ordinary counterpart in an untagged control; no selection mutation is necessary. |

[Full case IDs and frozen answer hashes](regressions.json) bind these rows to the source-graded losses in receipt 1591. [Rule changes](fixes.tsv) contain the exact replacements. Only the four relevant topic cards change; the entry changes version only. The native-slider, live-field, visible-title and dismissal-completion rules are byte-preserved. This protects their guidance, not a future answer's score. The two silent media fixtures are bundled on demand, not injected into every prompt.

## Evidence boundaries

- Shelf and Delete units drive the real installed UIAction or application closure. The Delete unit does not inspect a generated SwiftUI view tree.
- The native search check uses the existing representable's field factory and verifies editable configuration, label and text updates. It does not observe accessibility focus stops, determine which modifier an unknown app uses, simulate user typing or verify a Clear button. Those two answers retain source-review criteria. Do not grade either solely on a passing field test.
- AppKit row checks establish exposed configuration and independent ordinary action dispatch, not delivered VoiceOver navigation.
- The existing player selection and metadata units use a real AVPlayerItem. The order probe uses actual options and group, **but orders the chooser inputs itself**. It does not establish that the native option order changed or that the app picker invoked the probe. Historical negative receipts for forced-only selection and all-audio-described are in the [platform media results](../platform-media-v1/results-index.json).
- No native test establishes the effect of new instructions on model output. All eight questions are known development cases.

## Reproduce offline

From this directory run `python3 -B build.py --check` and `python3 -B -m unittest test_candidate`. To repeat the selected native contracts, run `python3 -B native.py` on the configured Mac; it creates a fresh ignored results directory, preserves first commands, sources, diagnostics and XCTest bundles, and reports each negative control separately. For the independent option-order probe, compile MediaProbe.swift with `xcrun swiftc -parse-as-library` and run the executable with the extracted positive.mov as its sole argument. No model provider, remote asset or additional dependency is used.

Author request: "Lets fix all eight regressions across the six areas in one offline batch. Start with the lost tvOS enabled check, stale Delete and Mac search field. Preserve the four wins, verify against native contracts, and leave 0.2.2 unchanged. No model runs." Original frozen inputs and answers remain in the private 1574 return. The graded supplement and original answer hashes identify the judgments used here. New authored outputs are fixes.tsv, the candidate package and the unit sources; this report is separate analysis. No new subject responses or independent reviewer grades exist.

## Preservation checks

The offline package verifier also rechecks the frozen slider starter's compile receipt, the earlier working/alternative/defect results for live field changes and dismissal timing, and the positive and missing-title tvOS records. These were not fresh executions. An unchanged rule can still perform differently when another card changes.

**Next decision:** use this candidate for a paired comparison only after authorization. Prioritize new counterexamples to the six repair areas alongside the four measured wins, report ordinary actions separately, and do not treat a repeat of the eight known questions as evidence of transfer.

**First execution:** [Native receipts](native-receipts.json) record nine passing working methods (tvOS 1, Mac 7, iOS 1), plus two intentional mutant executions that failed at their intended assertions. No skipped or unresolved selected methods. The [separate option-order result](media-order-result.txt) records the fixture's actual order and the independently controlled comparison. Original source snapshots, first logs and XCTest bundles remain under the private results directory printed by the runner.
