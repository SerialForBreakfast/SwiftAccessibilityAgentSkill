# Current release decision

**0.2.2 is released. 0.3.0-rc.1 is the one installable candidate.** SwiftUI development is open on iOS, macOS and tvOS. iPadOS-specific expansion, watchOS and visionOS are deferred. Existing historical material stays in place.

| Question | Current evidence |
|---|---|
| Can a user install the RC without switching the default release? | Yes: [archive and local install instructions](evals/rc1/README.md). Project-local copy installed with the existing skills CLI; compared to all archive files. No model session used. |
| Can we grade code without an LLM reviewer? | [Twelve bounded development tasks](evals/rc1/RUBRIC.md) check executable Swift contracts across six cells. The [fixture scorecard](evals/rc1/scorecard.json) separates compilation from the expected runtime verdict. One qualified target per task is not a platform support matrix. |
| Does the installed RC activate or improve answers? | [Measured on Haiku 5.5 low; partial](evals/rc1-comparison/RESULT.md). Quality is unchanged: 12/12 automatic pairs both pass, but these 12 tasks have no headroom. Automatic invocation is 1/12 for each version; explicit invocation is 3/3 for both, and only rc.1 then reads its references. The sealed run stopped at 9/36; the complete cohort used rewritten prompts. No unaided arm. Native grading on this Mac (reviewed local lane): 33/36 pass. checkout-font fails 3/3 for both versions, because the auto-adjust flag overrides the supplied size; the source review had missed it. |

**Preserved-answer check:** the [original local checkout harness](research/evaluation/checkout-local-replay/README.md) reproduced all eight first type-check outcomes and all eight unit-method outcomes, without changing any answer. This is not qualification for arbitrary new submissions.

**Delivery path rehearsed offline (November 7):** `python3 -B evals/protocol/rehearse.py` passes on the preserved returns. It covers the attempt ledger (which enforces the owner's chosen budget and stopping policy), the answer contract, the native reproduction (33/3), the linked verifier and the decision-first report. Two checkout-font contracts are [qualified](evals/headroom/checkout-font/README.md).

**Next decision (owner):** which run option, budget and stopping policy, if any; zero extra spend stands until changed. rc.1 is not promoted. Offline next steps are in [ROADMAP-0.3.md](ROADMAP-0.3.md): draft the rc.2 text-size card against both checkout-font contracts, write transfer cases, and prepare option B + D (60 sessions) for review without dispatching it.
