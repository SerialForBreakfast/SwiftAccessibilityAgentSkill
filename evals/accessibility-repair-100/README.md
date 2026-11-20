# Swift accessibility repair corpus

[Browse all 100 questions](INDEX.md) · [Read every prompt with its code on one page](ALL-100.md) · [Controller answer key with XCTest examples](ANSWER-KEY.md)

| Task | Questions | What one successful answer demonstrates |
|---|---:|---|
| Repair an implementation | 80 | Fixes the supplied defect, preserves an ordinary behavior, and proposes a test that distinguishes the two implementations. |
| Repair the proof | 20 | Strengthens a weak XCTest against a working implementation. The new assertion rejects the private defective variant for the intended reason. |
| Total | 100 | 59 iOS, 30 macOS and 11 tvOS questions. |

These are newly worded **development prompts** assembled from the repository's existing positive examples and intentional defects. Some test-repair questions deliberately revisit a behavior from a production-repair question. The full set is visible for author review. It measures neither 100 independent bugs nor transfer to unseen tasks. The platform mix follows the available verifiable fixtures. All 100 have Swift source; the 20 proof tasks also include the weak test and its setup. Each repair task requires a proposed XCTest. The controller key includes a concrete XCTest example per prompt, an implementation to compare against, the registered assertion IDs, and the manifest with source claims.

## Run and grade

1. Before spending quota, qualify the new prompt/test pair on the relevant Apple SDK. For each repair task, run the named original check against the working source and its defective counterpart. For a proof task also confirm the **supplied weak test passes both**. Reject compilation failures, missing fixtures or failed setup as proof that a behavioral defect was detected. Bind test code to the source module named in its original suite. Record the environment, assertion, and any case revision before freezing the subject bytes.
2. For discovery, run one fresh, unaided Gemini Flash Low session per eligible question. Supply exactly one file from `subjects/`. Keep the key, other sessions, the corpus index and the local repository outside the subject environment. The question already contains the code. Pin the same CLI for generation and quota reads; record first answers, errors, effective model, tokens and quota. Authoring the corpus does not allocate a live batch.
3. Grade the original answer without its condition label. Record **behavior**, **preservation**, **integration** and **test sensitivity** separately. A repair passes the proof check when the proposed XCTest passes the repaired implementation and fails on the original defect at the intended assertion. For test repairs, run it on the working implementation and the hidden defective source. Accept alternative implementations and behavioral checks. Treat an unsupported proof or ambiguous requirement as inconclusive. Record unnecessary production changes separately. A configured focus target or notification request proves only the application behavior directly observed.
4. Group confirmed baseline misses by mechanism, and inspect passes for unnecessary rework. Try one small skill change for a recurring failure: e.g., capture the actual installed callback, replace its owner, deliver the old callback, then exercise the current callback. Use a short topic reference when the rule is platform-specific. Freeze the candidate before replay. Include passing controls and compare matched gains, losses, unresolved cases, token cost, and observed skill/reference reads.
5. Report selection explicitly. A replay limited to known failures is diagnostic. For a transfer claim, commission fresh scenarios with distinct fixtures kept out of skill authoring. If reserving a portion of this corpus internally, keep shared production types, helper code and sibling defects together across platforms; do not randomly split individual prompts.

## Verification and regeneration

`python3 -B build.py` rebuilds the subject files, index, combined reader and controller key from the two question lists. It checks the source and XCTest file hashes against their original manifests and binds each case to a named failing check. The generator removes comments explicitly identifying a seeded defect from subject code. The seeded code remains reviewable beside the reference implementation in the controller key. Swift syntax parsing can run on Linux. Apple SDK compilation, the proposed weak-test pass/pass checks, independent calibration and model outcomes for this corpus require separate results.
