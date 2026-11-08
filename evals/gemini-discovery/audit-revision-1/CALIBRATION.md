# Flash Low grading calibration

Two reviewers independently examined all 17 exported developer questions with their original Swift source and controller criteria. A third reviewer wrote an acceptable answer fragment and a plausible near miss for each question. Each grader classified every fragment with the author's key and the other grader's judgments withheld. The coordinator joined the grades afterward. These are short, authored calibration examples; agreement on them does not predict agreement on long Gemini answers.

| Offline check | Result |
|---|---:|
| Primary-behavior fragments agreed by both graders and the author | 34/34 |
| Supplemental judgments agreed by both graders | 6/6 |
| Distinct final question digests verified | 17 |
| Existing Swift source blocks preserved byte for byte | 16/16 |
| New Gemini sessions | 0 |

The six supplemental fragments tested an alternative object-identity implementation, a correct diagnosis with a circular test, a valid text-range check, an incorrect fixed-time chapter increment, and two missing-answer scenarios. Both graders marked the missing answers inconclusive and separated the circular test from the correct production diagnosis. The [controller-only record](calibration.json) retains fragments, individual labels, supplemental evidence notes and prompt hashes. Only the question exporter is intended for preparing subject inputs.

## Fixes that affect interpretation

- All 16 code questions now use the same neutral request for a conclusion and a focused check. The former boilerplate already told unaided Gemini to leave working code alone. Original platform/deployment context is restored. The chapter question accepts a behavioral design.
- The modal case requires exactly one restoration to an eligible target after completion. Disabling all callbacks now fails. Close and Escape are each exercised in both permission states from an appropriate fresh panel. The sheet case also requires the newer presentation's valid dismissal to work.
- Direct removal and cross-owner reparenting are distinct. Check selection and the actual callback. Outline checks use populated old and current nodes, including removal before same-ID replacement. Accept equivalent ownership designs.
- Verify names, status, ordinary controls, playback choices and selected traits through their production paths. Require present fixtures for both audio tag classes and compare actual player selection. UI metadata or an empty filtered set cannot establish player state.
- The three text prompts use the same literal hit after an emoji. Grade the native substring returned by the handler and ordinary selection independently. One implementation drops the first letter; two already return the whole word. They are three sessions per arm and one related behavior family.
- Score primary behavior, effects on existing behavior/rework, and the proposed check separately. A proposed check gives source-level evidence only. Missing output is inconclusive. An implemented answer with a vacuous check can meet the primary behavior while missing the evidence requirement.

## Final reviewer check

Both reviewers re-exported all 17 corrected questions and retained their primary grades. Four acceptable fragments illustrate correct behavior but omit part of the requested check. For full evidence credit the final grader also requires these observations:

| Positive fragment | Additional evidence for the final question |
|---|---|
| node-removal | In the same data source, a still-current populated parent has positive child count and returns its expected child. |
| dismiss-owner | After the late A callback leaves B intact, invoke B’s valid callback and observe exactly one B restoration. |
| captured-action | Invoke the current shortcut and both actual ordinary buttons. Each invocation reports its current ID and corresponding operation exactly once. |
| text-range-47 | On “😀 cat!” searching for “cat”, the native range starts at UTF-16 offset 3, ends at 6 and returns “cat”; the text view remains selectable. The original fragment uses another valid literal. |

These additions accompany the original masked fragments so the independent grading record remains reproducible. They do not constitute native run results.

## Estimate for the proposed 68 sessions

Use 17 fresh sessions in each of four conditions on AGY Gemini 3.8 Flash Low: unaided, review sentence only, UIKit text note only, and both. Use identical question bytes, permissions and settings within each quartet. For this content experiment, supply the assigned text directly, including on unrelated tasks, so the treatment is well defined. Keep the common system envelope identical and omit skill-specific branding or route instructions from all four conditions. This estimates content effects; automatic routing and normal installed-skill attribution require a separate comparison. Interleave the four conditions and balance their order across questions. Report the note's three text tasks and 14 off-topic tasks separately. The primary outcome for the text family includes fixing the broken variant while preserving both working ones.

| Empirical projection | Five-hour allowance used | Weekly allowance used |
|---|---:|---:|
| Scale the 375-session continuation by 68/375 | 5.1 points | 1.5 points |
| Scale by the reported tokens of the 17 matched parent questions, repeated across four arms | 7.6 points | 2.2 points |
| Same token projection replacing the single largest parent with the other parents' median | 4.2 points | 1.2 points |

The continuation consumed 28 displayed five-hour and 8 displayed weekly percentage points over 1,683,213 reported tokens. The parent cases total 114,677 tokens per arm (458,708 across four); the captured-action answer alone used 55,475 tokens. With that case at the median the projected total drops to 251,528. These projections use historical rounded account meters; response length, treatment and concurrent account use can change the debit. **Plan for roughly 4–8 five-hour points and 1–3 weekly points**, with 8 and 3 as planning allowances, not hard ceilings. Scope is 68 first answers, subscription only, with no extra probes or paid fallback. No current balance or live run is implied.
