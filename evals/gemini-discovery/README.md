# Gemini discovery: 384 developer questions, two matched arms

**Prepared, not executed.** The first measurement is how many distinct accessibility decisions Gemini Flash gets wrong **without an installed skill**. The second is how many of those decisions the *already frozen* zero-base challenger rescues without breaking behavior that worked. The target of 50 is a product milestone, not an assumed failure count, a run cap, or a reason to stop at the fiftieth failure.

| Platform | Native | SwiftUI | Shared / mixed | Total |
|---|---:|---:|---:|---:|
| iOS | 111 UIKit | 34 | 1 | 146 |
| macOS | 80 AppKit | 52 | 1 | 133 |
| tvOS | 75 UIKit | 29 | 1 | 105 |

**One full pass:** 384 independent first sessions for unaided discovery. **Paired comparison:** another 384 on identical common questions, including unaided successes, or **768 sessions** total at one observation per condition. Do not interpret 768 sessions as 768 distinct capabilities. No quota reserved; no new model observations. The question texts total 880,158 UTF-8 bytes per arm before wrappers, references or outputs. Bytes are not tokens or a quota estimate.

## What's in the portfolio

| Lane | Questions | What the answer must demonstrate |
|---|---:|---|
| Targeted code repair | 161 | Fix a concrete defect in supplied Swift without sacrificing adjacent behavior. Each has a pinned source fixture, claim and named failing unit assertion. |
| Preservation | 59 | Review working code under the same kind of request. A justified no-change answer is valid. Equivalent implementations are acceptable. |
| Full implementation | 92 | Implement a real developer workflow using the original package question and its separate rubric. These are development rubrics, not 92 independently promoted golds. |
| Historical development | 47 | Retest graded decisions from earlier research using clean question-only inputs, never treating earlier results as matched answers. |
| Integrated native contracts | 7 | Complete existing starter files from the recovered qualified development pool. Quarantined and transfer-reserved tasks excluded. |
| New platform workflows | 18 | Make design decisions about editable hosted controls, independent selection vs focus, input names, ordinary rotor navigation, text reflow, focus recovery and more. Each has a specific criterion and linked guideline. |

These cases use the existing [failure inventory](../../research/evaluation/failure-inventory/README.md), [neutral question exports](../../research/evaluation/zero-base-v1/README.md), [package examples](../../code-examples/) and [qualification ledger](../../research/evaluation/zero-base-v1/pool-receipts.json). The code-repair cases are deliberately diagnostic: the user supplies a suspected symptom, implementation and preservation requirement, not the hidden unit test. They are not independent field prevalence estimates. The original authored prompts add less directed requests. Mutants show what the **grader** is designed to catch; they do not count as model failures. Known-source fixtures are development material, not fresh transfer. Referenced tests are scoped witnesses, not proof of rendered UI, delivered focus, speech, or every possible alternative.

## How many distinct problems?

There are **98 registered primary decision keys** across repair/workflow cases (60 represented on iOS, 49 on macOS, 40 on tvOS; overlaps intentional). Several examples can probe one key. For example, a macOS and a tvOS report that buffered media was seekable both probe `range-kind`; two misses count once. A label using the wrong supplied design font is different from a label refusing multiline layout. The code and assertions make that distinction auditable. Preservation variants provide regression checks, not new evidence of an unaided defect just because the reviewer suggested another style.

The other implementation and historical cases are not forced into one narrow criterion. Record their distinct findings, evidence and affected users separately. Adjudicate novel mechanisms against the registered keys while still blind to challenger results. Keep that exploratory count separate; do not count an overlapping prompt or second rubric bullet as another preregistered rescue. If discovery finds only 30 distinct failures, report 30. Missing or noncomparable answers stay visible. If 50 failures emerge but only 12 are rescued, report 12, not 50.

## Use and verification

- [Single worker handoff and return contract](HANDOFF.md): dormant until explicit approval. Only one question is visible to the subject; controller material is never supplied. Grade source contracts in masked order; separate invocation, coding quality and infrastructure.
- [Controller registry](controller.json): per-case platform, lane, decision, source path, criteria/assertions or original rubric. [Subjects](subjects.jsonl) contains only opaque IDs and exact question text. [Excluded inputs](excluded.json) lists exact duplicates, missing/risk cases and reserved material.
- [Seal](seal.json): hashes, grading dependencies, exact candidate hash and deterministic interleaved order. If a prerequisite or scope changes, prepare a separately identified packet; never blend unmatched arms.

From the repo root:
```sh
python3 -B evals/gemini-discovery/build.py --check
python3 -B evals/gemini-discovery/verify.py
python3 -B evals/gemini-discovery/export.py CASE_ID
python3 -B evals/gemini-discovery/score.py evals/results/gemini-discovery/grades.json
```

The last two commands take an actual cell ID or future private grading ledger; no real ledger exists for this run yet. The scorer reports unaided primary failures even before a challenger answer exists; **only** completed matched pairs can rescue a decision. A packet-neutral model/effort and identical harness settings across both arms are required. Keep diagnostic, native and source-only evidence distinguishable. Local verification exercises synthetic grades, not provider connectivity, an independent rubric audit or new native executions.

**Next owner decision:** how much subscription capacity to allocate and how to handle interruptions. The strongest test of real-world applicability after discovery is a separate, fresh family-level transfer evaluation; do not tune the frozen challenger between the two arms.
