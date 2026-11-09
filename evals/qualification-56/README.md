# Offline qualification: 56 developer questions

**Keep 0.2.2 released.** The grading packet is ready for use as a development instrument, not as an automatic pass/fail judge of entire answers. [Before-and-after skill scores](CHART.md) · [Offline replay by question](REPLAY.md) · [Machine-readable evidence](board.json) · [Frozen questions and rubric](../../research/evaluation/signal-panel-v4/README.md).

## What was qualified

- **49 runnable starters.** 44 preserve the frozen question's Swift fence; five greenfield requests now have minimal starter interfaces. All 49 compiled and linked as separate SwiftPM modules in three platform suites. Seven questions ask for a design or explanation. Two additional questions include runnable code but ask whether an already working SwiftUI control needs any change; their decision is graded by source. Starter linkage is not a behavior assertion.
- **47 native decision controls.** 32 new three-implementation probes bind 40 questions; seven other questions reuse seven prior, platform-specific qualified probes. Each uses the same assertion for the reference, alternative and defect. For the new probes the verifier requires one XCTest verdict per method, two passes, a deliberate failure at the named witness and a completed host. An assertion failure intentionally makes the aggregate XCTest command exit 65. Working/defective twins and repeat executions do not increase the count of independent probes.
- **Nine source contrasts.** [Controller-only calibration](source-calibration.tsv) contains a reference answer, a different acceptable answer, a plausible defective answer and its rejection reason per question. This is author adjudication, not a keyword grader or an independent review. It covers distinctions like a chapter boundary versus episode duration and a single editable search field versus a single static label.
- **112 original first answers.** 46 existing replay cells were verified rather than rerun; the remaining 66 cells were processed offline. The board verifies every question and full answer against the sealed archives. It records the source selection (unchanged starter, verbatim fence, declaration splice, or unresolved), both first lane receipts, and the original six source grades. Submitted proof and independent contract are different lanes. Ambiguous/incomplete patches are not completed by the grader. New scaffolds are never retroactively substituted into this replay.

The board accounts for every question, **not every assertion a reviewer might make about it**. Use the frozen case-specific rubric and verification scope alongside the calibrated distinction. For example, the attached-ineligible responder probe does not prove the separate eligible-but-refused request path. The surviving-origin probe does not exercise a view's installed dismissal callback. Use the [installed-callback replay](../native-calibration/sheet-dismissal/answers/README.md) for that distinction. A request to restore focus does not demonstrate delivered focus; neither a build nor state assertions establish layout or spoken output. No blanket demand for executable proof on design or no-change questions.

## How to interpret a grade

1. Grade the developer's requested behavior, independent ordinary actions, integration, unnecessary changes and requested verification separately. Accept any alternative satisfying the observable contract, not only the two calibration implementations. A mutant that breaks one dimension need not fail the others.
2. Check the model's unchanged code against the question it actually saw. A fixture can lack a dependency, an assertion can assume one implementation's private member, and optional sample code can fail to build without refuting an otherwise correct explanation. Mark these distinctions explicitly. Never award execution credit to a source-only answer.
3. Record the first receipt before consulting [follow-up integrations](../../research/evaluation/signal-panel-v4/replay/README.md). For example, the iOS wrapper v2 original test could not compile against the selected host. The later integrated host exposed the stale callback; the first error remains a host mismatch, not that behavioral finding.
4. On native-field validation, both preserved iOS answers passed their own checks but failed the unchanged field-mutation contract: one stale error was applied instead of zero. This is a concrete verification gap. On the Mac sheet, an answer's proof failed on an unknown testing attribute in the first host; that is not evidence about which sheet requested focus.
5. Keep a non-executable explanation eligible for a good source grade. Conversely, 37 compile-only first contract outcomes do not count as successful behavior replays. Original grades and original subject bytes remain unchanged.

## Reproduce offline

From the repository root on the evidence host:

```sh
python3 -B evals/native-calibration/grade.py --check
python3 -B research/evaluation/signal-panel-v4/replay/report.py --check
python3 -B research/evaluation/signal-panel-v4/results/analyze.py --check
python3 -B evals/qualification-56/report.py --check
```

These checks use the private original return and the first attempt directories under `evals/results/`. The board and chart can be read without them. To export **one developer starter only**, run:

```sh
python3 -B evals/qualification-56/starters.py --case P-35ee522327907bd8
```

Change into the printed folder under `evals/results/qualification-56/`. It contains the question, package, source and a linkage test, not the rubric. Run `xcodebuild test -scheme Starters -destination 'platform=iOS Simulator,name=SwiftAccessibility-OS26-Unit-iOS' -derivedDataPath dd` for that iOS example; use the corresponding tvOS simulator or native macOS destination for other starters. Providing a new scaffold changes future subject inputs: use it identically in both arms.

For a fresh repeat, `starters.py` without arguments runs all linkage suites. Run `run_controls.py` first without arguments, then with `--more`, then with `--last` for the three sets of native decision probes. All allocate new private batch paths; `--platform tvOS` (or iOS/macOS) narrows the target. The two initial iOS controller processes produced method results but did not close their host receipts during diagnostic collection. Their original logs are retained; only completed reruns with diagnostics collection disabled count. These were harness incidents, not model defects. The existing anchors are Xcode 27.0 build 27A266a / SDK 27.0, deployment 26.0, iOS and tvOS 26.5 simulators and macOS 27.0.

To reproduce the **additional** preserved-answer cells, run `replay.py` and pass its printed batch name to `research/evaluation/signal-panel-v4/replay/native.py`. Do not point repetitions at the first batch. The private return retains the original requests, answers, traces and grades; this packet publishes hashes and controller analysis, not private transcripts.

## Release decision

The [matched model comparison](../../research/evaluation/signal-panel-v4/results/README.md) tested signal-v2 and signal-v4, **not** released 0.2.2 and not the new signal-v5 archive. V4 improved primary behavior from 28/56 to 35/56 but tied on whole answers (14/56 each), regressed on ordinary preservation (45 to 42), and used 56.8% more reported tokens. Its ordinary Play loss is a blocker even if an aggregate increases. The [v5 candidate](../../research/evaluation/signal-panel-v5/README.md) addresses real decision errors, but no paired v5 answers exist in this return.

**Next decision:** use the qualified packet for an owner-authorized release-versus-challenger comparison, with identical final starter bytes and tool access in both arms. Predeclare ordinary Play and installed dismissal ownership as blocking regressions; grade whole-task outcomes separately from proof quality and tokens. Neither this offline work nor a correct example predicts how often v5 will produce the correct answer.

Authoring request: “Lets qualify the full 56-question grading packet offline in one tranche. Add runnable starters for code tasks, replay preserved answers unchanged, and verify each rubric accepts valid alternatives and rejects mutants. No model runs or released skill changes.  Lets also make a good at a glance chart of the state.  Should we promote the new version compared with the last release?” Authoring transcript beyond captured material unavailable; no new subject or judge session.
