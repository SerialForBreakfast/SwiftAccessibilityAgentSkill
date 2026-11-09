# Calibrate native grades before the next comparison

A developer's passing test answers "did this test pass?", not "would it catch the reported defect?" This controller-only overlay preserves the native implementation verdict, submitted-proof execution and adequacy of that proof as separate fields. It never modifies an historical grade, declares a whole-task win or grants credit for a screenshot, inferred VoiceOver behavior or unseen model reasoning.

## Decision rules

1. Bind the contract to the developer's requested observable and original starter. Grade the installed interaction, not a convenient substitute. If the oracle requires an incidental implementation detail, try a materially different correct implementation before counting a failure. Preserve the initial result.
2. When a submitted proof passes on the same defective implementation, record a **missed contract failure**. Name what escaped detection. A runnable proof of a different behavior can still be useful; it does not prove this one.
3. A missing fixture, refusal to fetch remote media, compile-only result or missing binding provides no behavioral verdict. A broken test does not erase a separately observed correct implementation.
4. To establish that a controller probe discriminates, run the **same test** on the reference, an accepted alternative, and the relevant deliberate defect at the same anchor. Require both correct implementations to pass and the defective one to fail at the intended assertion, not while compiling. This qualifies that probe for that distinction, not the submitted proof or every other case in the family.

## Contrasts to check

| Decision | Witness | Counterexample a weak proof misses |
|---|---|---|
| Restoring panel state | Start exposed, replace A with B, finish B and inspect the original background and ordinary controls. Also preserve an initially hidden background. | Stopping while B is open correctly sees suppression in both good and bad implementations. |
| Returning to a sheet origin | Request dismissal, then complete with the origin still eligible; separately remove it to require fallback. | Completing directly without the close path leaves state that production has already cleared. This does not reproduce a private view callback. |
| Retained action | Retain an installed registration across rebinding, send it, then send the current ordinary action and check recipient and count. | Calling a helper with a known old token bypasses a registration that asks for a new token when invoked. |
| Live field edit | Change the actual field after submit, deliver the obsolete reply and observe acceptance and submit eligibility. Also finish a current submission. | Editing only through a helper retires the request even if the native path does not. |
| Responder refusal | Let an attached origin refuse and observe the requested fallback. Contrast with an accepting origin. | Testing only a detached origin never exercises refusal. |
| Player selection (adjacent control) | Choose through the binding with a real local group; read the item's native selection and its unrelated audio selection. | Updating a local ID can succeed even though the native caption remains Off. |

## Results and use

The [calibration report](calibration.json) covers 80 preserved answers and [eight identified false greens](fixtures.json), not eight independent failure families. Six contrasting cells check successful contracts with broken proofs, missing fixtures and insufficient evidence. Nine platform/probe records cover seven distinct probes. Five reuse the pinned earlier native receipts; [four new three-way checks](probes/README.md) qualify live-field edits on two platforms, attached responder ineligibility and surviving sheet origin. The new native controls produced eight correct passes and four intended mutant failures. These results qualify the grader, not a model answer or an installed skill.

On the evidence host, run:

```bash
python3 -B research/evaluation/signal-panel-v3/persistent-replay/report.py --check
python3 -B research/evaluation/signal-panel-v3/evidence.py --check
python3 -B evals/native-calibration/grade.py --check
python3 -B evals/native-calibration/test_grade.py
```

For another independently verified native ledger with the same effective-lane schema, use `grade.py --ledger PATH`. This writes the overlay to stdout. Apply it to matched criteria only; the tool does not infer whether a newly authored oracle is valid. Unknown statuses fail closed. Keep historical source scores, gaps and raw receipts alongside this overlay. All fixtures here are inspected development evidence, not new holdouts.

The [submitted-proof comparison](proof-sensitivity/README.md) tests the other direction: can the original submitted tests, rather than the controller probes, distinguish the correct fixtures from the known defects? These receipts assess proof sensitivity separately from the original implementations.
