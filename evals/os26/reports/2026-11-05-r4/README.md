# OS26 revision4 native validation

## Result

**6/6 candidates passed; 12/12 intentional mutations failed at the selected unit
assertions. Independent review remains pending; 0/6 cases are gold-ready.**

Executed locally on 2026-11-05. No LLM inference, UI tests or manual device
verification were performed. This is fixture/oracle validation, not a Gemini
baseline and not a measured skill-quality improvement.

| Case | Selected unit test | Candidate | Mutation1 | Mutation2 |
| --- | --- | --- | --- | --- |
| GP26-01 | Settings callbacks/exposed controls | Pass | Hidden descendants rejected | Missing Help callback rejected |
| GP26-02 | Same-instance reconfiguration | Pass | Stale label rejected | Stale status rejected |
| GP26-03 | Checkout callback/font-layout prerequisites | Pass | Fixed height rejected | Scaling disabled rejected |
| GP26-04 | Production message handlers | Pass | Dropped action rejected | Duplicate action rejected |
| GP26-05 | Production movie activation | Pass | Dropped action rejected | Wrong ID rejected |
| GP26-06 | Production Toggle binding | Pass | Constant binding rejected | Inverted write rejected |

Each variant executed exactly one focused XCTest, with zero skipped tests. The
same suite and test selection were used across each candidate/mutation triplet.
An expected assertion failure is a successful mutation check, not a passing test.

## Environment and provenance

- Fixture checkpoint: `b0f4e449d22086fcce87765c154d390507c31b75`.
- Prompt/acceptance revision: `os26-code-contract-4`; fixture revision:
  `os26-fixtures-unit-2`. Six developer question texts remain unchanged.
- Xcode27.0 build27A266a, SDK27.0, deployment target26.0.
- iOS Simulator26.5 build23F77 for cases01-04/06; tvOS Simulator26.5 build23L470
  for case05. These results do not claim execution on26.0 or compilation with SDK26.
- Runner delta from checkpoint: `-collect-test-diagnostics never`, and SIGKILL
  on the ten-minute job timeout. Sources and unit tests were unchanged during
  the successful matrix. The delta is included with this report's commit.
- [Structured results](native-results.json) record exact variant/suite hashes,
  counts, selected IDs, original log hashes and sanitized excerpt hashes.
- Per-variant text files contain only actual test lifecycle/assertion excerpts.
  Local paths, host account details and simulator UUIDs are omitted. Full logs,
  command intents, xcresult bundles and pending-review receipts remain local.
  These public excerpts are not the complete logs or an approval receipt.

## Earlier attempts

Two earlier serial attempts were interrupted while Xcode gathered diagnostics for
an intentional failure. Partial artifacts are retained locally as incomplete or
infrastructure-error attempts. They are not counted as completed matrices or
mutation kills. Disabling extended test diagnostic collection resolved the stall;
the complete third attempt is the sole source of this report's18 outcomes.

## Promotion and remaining work

The receipt assembler verified all18 records and log/intent hashes. The readiness
gate returned only `evidence_pending` and `independent_review_pending`: review
records were intentionally not supplied, and no reviewer identity was invented.

BigDog must review the exact committed fixture/test/runner delta, source and
availability notes, accepted alternative implementations, and these results.
Approval must identify the reviewed revision and scope. In particular, review
control-to-handler wiring rather than treating direct handler calls as simulated
input or focus. Local review of original BigDog fixtures is recorded in
[SOURCE-REVIEW-R4](../../SOURCE-REVIEW-R4.md); it does not independently approve
locally authored revisions.

After that review, record genuine review evidence, rerun the promotion gate and
produce the model-input-only plan. Gemini execution still requires the separately
approved bounded batch and confirmed provider/model/quota details. No paid calls
or model substitution are authorized by this report.

## Checks and limitations

- 107 offline runner tests pass, including10 new receipt-assembly tests.
- 210 frozen baseline files verified; runtime remains0.2.2 with unchanged content
hash `3a1a2d58af19a94eec940000d9edcca7928bb5139aa3d52b1ef6e917c0271bbd`.
- Heldout questions preserved. Earlier research/history remains intact.
- Unit results cover scoped configuration/state/callback assertions. They do not
establish spoken navigation, visual fit, focus restoration or real-user usability.
- Two mutants per case sample defects; they do not establish comprehensive defect
coverage or require generated solutions to copy fixture helper names.

The dedicated validation simulators are shut down. There is no native matrix or
model process left running from this task.
