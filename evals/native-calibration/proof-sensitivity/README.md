# Can the submitted test detect the defect?

This board covers **both arms of the four cases matched to the last three qualified distinctions**, not the entire 80-answer replay. The field distinction has an iOS and a tvOS case. No answer was rewritten and no new model answer was requested.

The independent controller test already distinguished reference, alternative and mutant. Here the variable is the **test**: replace the controller assertion with the preserved submitted XCTest files. Keep each qualified subject byte-identical and name the library module to match the submission's import. A proof that passes all three implementations misses that specific defect; this does not mean its assertions have no value.

| Case | What the proof exercises | Distinction left untested |
|---|---|---|
| P-4099aaf89ec377cf, tvOS, both arms | Submit, edit through the helper, deliver the old reply. | The helper cancels the request. Directly changing the field leaves the old reply live until checked. |
| P-db6ab4c551e67aca, iOS, skill | Submit Alice, edit through the helper, reject the old reply, then successfully submit Bob. | The successful second submission is useful evidence but does not exercise a direct native edit. The unaided arm has no submitted executable proof. |
| P-be25d510c5ffe50f, macOS, unaided | Remove the origin, then test fallback; separately remove both buttons. | Removal and attached responder ineligibility are different inputs. The skill arm has no submitted executable proof. |
| P-90629dd9d60ff906, iOS, both arms | The submissions depend on `PresentationCoordinator` and `FocusTargetCoordinator`. | The qualified reduced fixture exposes `Sheet`. No adapters were added. These two results are binding gaps, not executions. The skill answer's prior original-contract failure after Close remains on record. |

See [the execution board](evidence.json) for each method's outcome, the original answer and proof hashes, and each qualified subject and log hash. Proof files are unchanged **from original replay staging**: that staging supplied imports around the returned Swift fences. Original fence hashes are recorded separately. Full answer text, source snapshots, native logs, result bundles and receipts stay in private results. The board does not replace the frozen grades.

Verify on the evidence host with `python3 -B evals/native-calibration/proof-sensitivity/verify.py`. To create a separate first-attempt batch, use `python3 -B evals/native-calibration/proof-sensitivity/replay.py` with the recorded simulators booted. The runner does not retry or overwrite previous attempts. A failure on a correct control, compile error or ambiguous test outcome requires review, not automatic credit for detecting a mutant.
