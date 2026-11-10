# Discovery-v2: next paired pass (held)

Start with [the 384-parent board](board.json), [native results](../native-results.json), [the worker brief](HANDOFF.md) and [the seal receipt](receipt.json). This is a research overlay on 5ab5a92. Install the candidate ZIP only in an isolated candidate session. Nothing here updates the released skill.

## Decision board

The platform [iOS](shards/ios.json), [macOS](shards/macos.json) and [tvOS](shards/tvos.json) decision shards follow the existing [suggestion schema](../schema.md). They are the decisions used for this sealed pass, not edits to parallel reviewers' working shards. Join them by original ID to [the evidence index](../items.json) for blind findings, paired fixtures and follow-up outcomes. Private first-answer records remain under the ignored results directory. This is a reproducible controller synthesis of existing reviews, not 384 new independent grades. A single pass isn't proof of low headroom, and a flagged failure isn't proof the skill can fix it.

| Original disposition | Parents | What goes to the next session |
|---|---:|---|
| Keep as control | 188 | Original question and full inputs |
| Grade components | 74 | Original bytes; apply revised scoring equally to both arms |
| Neutral matching questions | 100 | Same scenario for both code variants |
| Clarify policy or calibrated contract | 19 | Specific developer request and original starter |
| Split incompatible contracts | 3 | Two requests each; 6 questions, not 6 independent original incidents |

The prior missing answer remains excluded from historical transitions. Its question is retained for the fresh matched comparison. Of 31 inconclusive baseline records, 30 were source judgments and one was an attempt error. Neither these nor 90 whole-answer failures can be counted as 50 distinct confirmed defects.

## What changes a developer decision

| Skill decision | Observation or counterexample | What would count as improvement |
|---|---|---|
| Trace before rewriting; preserve ordinary controls | 27 of 59 working/defective pairs passed only on the defective version. The review sentence helped selected status but lost a primary pass on reparenting. | Both distinct implementations get the appropriate answer; rework drops without losing behavior on the defective member. |
| Check the actual returned value or installed handler when asked | Only 8 of 68 follow-up answers satisfied focused verification. The text note gained no whole pass; some tests constructed their own range. | A changed production result makes the proposed check fail. Do not require tests for explanation-only requests. |
| Trace ownership to the actual control or presentation | Audit Q14 and the stale-action controls; dismissal A after B is different from a duplicate completion for A. | The old path is inert and the current ordinary path still works. |
| Distinguish current media selection from picker contents | Full-captions primary behavior improved with the review sentence, but all arms missed the complete request. | Opening leaves actual selection intact; an explicit change acts on the intended group and item. |
| Keep supplied size settings distinct from a live environment | The unchanged receipt-font answer failed the matched native contract. Checkout passed its own contract. | Preserve a caller-selected preview size without outlawing automatic adjustment for a live label. |

Platform specifics load on demand. The evidence does not support adding a default UIKit offsets note, claiming a particular focus utterance, or shipping more advice simply because it is available. Actual deployment-target verification remains separate from host SDK compilation.

## Offline evidence and reproduction

The native receipt records Xcode 27.0, macOS 27.0, simulator runtime 26.5 and deployment target 26.0. All 47 maintained variants across the seven integration tasks matched their expected statuses. Of three unchanged first answers executed, checkout and file-row passed; receipt-font failed. Four stayed held by the reviewed-local gate. None of these outcomes measures discovery-v2 lift. For explanatory grading, reuse the 17 calibrated cases, 34 primary fragments and the supplemental borderline/missing-answer examples; their agreement does not validate every revised rubric.

Run from the repository root, with the original private returns and native receipt present:

```sh
python3 -B research/evaluation/prompt-improvements-v1/build.py --check
python3 -B research/evaluation/prompt-improvements-v1/next-pass/check.py
```

The check reconstructs artifacts in memory, checks each eligible first-answer digest, compares every starter code block and both openings of every matched fixture, verifies schema and answer overlap, and reads back both archives. The handoff archive contains the final subjects and grading sources but no private first answers. A future run needs separate owner approval; all 387 questions are development material. Untouched transfer families and attribution to individual instructions are separate experiments.
