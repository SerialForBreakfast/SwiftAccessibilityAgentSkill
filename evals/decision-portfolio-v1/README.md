# Failure-to-success development portfolio

**36 frozen questions, not 36 measured improvements.** Six directly target rc.2's three corrections. Thirty more revise developer questions whose unaided Gemini first answers failed the original whole-task rubric. These cover 30 named decision targets, not 30 proven independent defects: a proof failure is not necessarily an accessibility failure, and related media/ownership cases form clusters. All are development material, not independent holdouts or independently approved gold.

| Platform | Direct repair/control | Broader revisions | Total |
|---|---:|---:|---:|
| iOS | 4 | 14 | 18 |
| macOS | 2 | 7 | 9 |
| tvOS | 0 | 9 | 9 |

### Direct, within-question contrasts

| Decision | Repair input | Working control | What can distinguish them |
|---|---|---|---|
| Mac recipient search | Hides the hosted search field. | Hides only adjacent decorative art. | Trace the modifier to its owner. The field's properties can be correct in both versions; public properties alone don't prove VoiceOver stops. |
| iOS rehearsal cue pad | Play is installed only as an accessibility action. | Single tap plays on the same surface. | Preserve drag-to-seek and chapter adjustment on both. Calling a playback handler directly does not prove it is registered for taps. |
| iOS audio inventory | The submitted test compares a non-Equatable result with XCTAssertEqual. | The same test matches the enum case. | Production inspection is identical. Check the two results and compile the test separately; changing the payload is unnecessary. |

Both members of each direct pair use identical developer wording and differ in precisely one file. **For working controls, leaving a correct implementation intact earns full credit.** The three direct questions were newly authored; their underlying decisions were already examined, so this is not a blind transfer set.

### Broader improvement backlog

[Thirty revised requests, decision criteria, alternatives and counterexamples](authoring/revisions.tsv) span six platform/framework combinations. Examples: a Pay button kept intact at large text sizes; a responder moved between Mac windows; a retained tvOS preference delivery that deduplication might mask; selection that remains unlisted rather than becoming Off; and an old validation reply that releases its own busy state. Start from the recorded *reason* for failure, not just its headline grade. The [controller board](controller/board.json) records historical rationale, available blind review, original source and assertions. These are independent grading inputs, never additional context for the subject.

### How to use the freeze

Give the subject only one ZIP from [subjects](subjects/). The subject-facing ID is derived from the package bytes. The direct packages include SwiftPM source and tests; broader ZIPs contain the full developer request and supplied source where applicable, not 30 newly qualified native oracles. Original inputs and scores stay unchanged. For source-free development requests the original requirements are retained below the revised opening. The inspector lane concerns an AVFoundation API used by iOS developers, not a UIKit rendering contract.

[Grade decision, preservation, source build, test build and proof separately](GRADING.md). Use identical ZIPs within matched comparisons; measure failures rescued *and* new losses. Analyze every development target, but add a skill instruction only for a repeatable developer decision, not to compensate for a bad question or a missing fixture. Separate development targets from whatever run budget the owner later approves. No baseline, evaluation run or handoff is authorized by preparation.

Reproduce the frozen bytes and validate the inventory with `python3 -B evals/decision-portfolio-v1/build.py --check`. For Apple-silicon SDK checks of the six direct packages (three pairs), run `python3 -B evals/decision-portfolio-v1/check_direct.py`. Logs are private under `evals/results/rc2-direct-*/`. The [manifest](freeze.json) pins the controller board, subject archives and grading guide.

Evidence strength for the broader revisions: all 30 have a recorded original failing whole-answer grade and answer hash; eight also have a failing blind whole-answer review. Nineteen have no named assertion in the historical item record. Do not treat those as native-qualified cases. Highest-value offline follow-up: map those 19 to a suitable discriminating unit, a calibrated source-only rubric, or an explicit coverage gap before a live comparison.

[Direct compiler receipts](controller/direct-compile.json): production compiled for all six; tests typechecked for all three working controls and for the two deliberately broken interaction cases. Only the broken inspector test failed, on its Equatable requirement. These are compiler results, not model grades, UI observations or executed test suites.
