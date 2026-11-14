# Callback, live-edit and dismissal qualification

This is an offline development audit, not a skill comparison. The [answer board](board.csv) joins 15 behavioral errors and three additional proof defects from the [350 source grades](../grade350/grades.csv). The immediate-post proof is already one of the 15. The [native receipts](evidence.json) identify source and test bytes, native environment, test events, diagnostics and the first log digest. Raw model text and build artifacts stay private.

## Results

| Outcome | Count |
|---|---:|
| Unique frozen answer records | 18 |
| Distinct behavioral disciplines / platform-specific checks | 4 / 6 |
| Working / alternative / intended mutant outcomes for the six checks | 6 passed / 6 passed / 6 caught |
| Production replays: full blocks / no-change starters / replacement fragments | 4 / 2 / 3 |
| Production replays reaching the behavioral failure | 9 of 9 |
| Complete submitted proof functions / native proof executions | 2 / 6 |

The other nine answer records are not nine additional native failures. They include design/triage, proof proposals and a standalone proof. The two source-level direct-edit proofs call the cancelling helper; the sheet proof supplies the old ticket to the helper itself. The evidence does not establish delivered focus, actual speech, or any skill lift.

Both submitted dismissal tests rejected **both** valid implementations. Q-c13f93 passed the eager-post mutant; Q-015170 rejected even that mutant because it also expected early background exposure. Neither qualifies as a grader. The hosted sheet answer recorded **late-A:open** and no first-B request. On both iOS and tvOS the original no-change validator left the obsolete error on the edited name field. On tvOS the old UIAction set selection to x even when the current button was reused. On macOS both replayed document adapters removed the replacement article.

## What the six contracts measure

| Contract | Decisive observation | Valid alternative |
|---|---|---|
| macOS document | Retained Delete cannot remove a replacement with the same ID; current ordinary selection and current Delete each dispatch once. | Registration lease identity instead of revision number. |
| tvOS shelf | Retain the installed UIAction itself. After a same-ID reconfiguration it cannot select; current primary activation can. | Membership of the original **button instance**, not just the item ID. |
| iOS and tvOS live edit (two native anchors) | Change the actual field without edit(), deliver stale error, check text, errors, requested focus and busy state. During B, repeat A then deliver B. | Compare captured field values to live fields individually rather than comparing snapshot dictionaries. |
| macOS sheet | Call A's installed dismissal after B opens, then B twice; record caller and target after each. | Distinct per-presentation session object rather than a UUID. |
| iOS panel | Refused dismissal leaves panel open; accepted escape or ordinary Close does not post until completion; teardown invalidates pending work. A successful restoration can synchronously reopen the panel without being overwritten. | Per-opening session object rather than an incrementing generation. |

On tvOS selection is an observable state, not a count of handler dispatches; the shelf starter exposes no separate shortcut. On macOS the working DocumentExample uses the tested closure factory for its ordinary and supplementary Delete. One submitted view calls domain methods directly: its *submitted adapter* is executable, but its replay is not an inspection of registrations inside that SwiftUI list. The hosted sheet substitutes a registration recorder in-process; it does not drive the OS presentation UI. UIKit's original panel exposes a refusal and teardown, not a cancellation callback that reverses an interactive animation. We do not claim such cancellation was exercised.

## Replay rules

A no-change recommendation binds to the exact supplied starter. Full production fences and unambiguous replacement fragments bind without editing their bytes; the surrounding source and test adapters are recorded separately. Source judgments stay distinct from native outcomes. Two complete submitted XCTest functions bind unchanged inside a test class. Three other proofs specify expected results in prose: two use edit() (which cancels the pending validation itself); one passes the known A ticket directly into a state helper. None exercises the failure in the question. No converted prose assertion is attributed to the model.

## Reproduce

Run from the repository root on a host with the existing native unit simulators:

```sh
python3 -B evals/discovery-500/grade350/verify.py "$PRIVATE_RETURN"
python3 -B evals/discovery-500/callback-batch/run.py "$PRIVATE_RETURN"
python3 -B evals/discovery-500/callback-batch/run.py "$PRIVATE_RETURN" --patches
python3 -B evals/discovery-500/callback-batch/repair.py "$MAIN_BATCH"
python3 -B evals/discovery-500/callback-batch/report.py "$MAIN_BATCH" "$PATCH_BATCH"
```

Each execution makes a new private directory; never overwrite a first attempt. The last command verifies the recorded runs; a new run has different log hashes and must be versioned as new evidence. The first staging mistake omitted the package's library product and Xcode could not discover the scheme. Its original manifests, native logs and available result bundles remain under `evals/results/callbacks18-vqp4g1yq/`. It had no subject verdict. The corrected primary batch is `evals/results/callbacks18-vchehwm0/`.

Controller authoring record: owner requested implementation of the 18-answer qualification plan in this conversation. Inputs are the frozen grade350 IDs/answer hashes, original subject ZIP, the private BigDog 1562 return, checked-in native sources and original modifier/host hooks. Generated controller checks and run stages are in this directory. No model judge, additional subject answer, or exact export of this authoring conversation exists in the packet. Findings and process lessons are separate from subject inputs.

Patch runs: `evals/results/callbacks18-yxh8ljji/`. The iOS full panel answer changed the callback signature from () to (Bool); the original controller did not compile against it. The isolated hook repair supplied false for cancellation and true for completion, without changing either submitted production file. Both the first diagnostic and the repaired execution remain in the receipts.
