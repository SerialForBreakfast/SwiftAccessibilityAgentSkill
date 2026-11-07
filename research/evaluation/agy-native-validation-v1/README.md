# Preserved AGY answer intake and native validation

Owner request: push the reconciled updates, obtain BigDog's preserved AGY answers,
and prepare local compile/unit validation. Claude stays pending; released skill and
frozen baselines stay unchanged. This is validation of existing answers, not another
model-generation allocation.

## Intake

The published update is `b90bdcd`. Request `swift-agy-native-intake-20261106-r1`
was stored at coordinator cursor1433. Storage is not worker acceptance or artifact
delivery. One read-only polling window allows up to30 minutes after request storage;
its deadline is2026-11-07T00:06:15Z. Private request/response receipts remain outside
Git. Current delivery and validation state is in [status](status.json).

Required scope: the14 original first answers, seven UIKit/iOS questions across
0.3.0-dev.1 and0.3.0-dev.2. [Expected cells](expected-cells.json) pins the public
proposal and exact input identities. No Claude cells, reconstructed answers,
regeneration, fallback or retries belong in this intake.

Before grading or execution:

1. Verify the delivered archive SHA256 against BigDog's reply; safely inspect archive
   entries and size limits before extraction. Reject traversal, links or unexpected
   executables. Never run a worker-supplied script as part of import.
2. Retain immutable originals privately. Check per-file hashes, all14 case/version
   mappings, original output hashes and exact supplied prompt/reference identities.
3. Compare execution-manifest, controller, grading and token-ledger hashes against
   the published summary. Record absent material or sanitized exports explicitly;
   retain separate original/export hashes rather than silently rewriting evidence.
4. Keep subject answers separate from controller rubrics and grading. Public summaries
   alone do not establish successful retrieval or independently validated answer code.

## Local validation sequence

Review every relevant code fence and prose instruction, including explicit
alternatives. Use `evals/runner/reviewed-swift-probes.mjs` only with a reviewed
adaptation plan. It moves imports and supplies declared context; it must not add
missing APIs, properties, state, callbacks or repairs. Preserve first diagnostics.
A valid no-code/no-change answer is not a compile failure.

Compile for UIKit/iOS26 using the recorded local SDK/Swift toolchain. Execute focused
units only for compiling, reviewed answers on the existing iOS26 simulator. Pin exact
source, scaffold, tests, environment and attempts before each run. No UI automation,
network fixtures or mandatory manual verification.

| Case | Intended assertion boundary |
| --- | --- |
| GP26-01 | Existing switch and Help remain independently exposed; parent hiding removed; names and callbacks preserved |
| GP26-02 | Both state transitions update the exposed owner on the same instance without requiring reuse; preserve customer/priority/status |
| GP26-03 | Existing Pay identity, typography and callbacks preserved; integrated scalable/multiline configuration and live updates; no forced vertical/adaptive-axis oracle |
| GP26-07 | Completion precedes restoration request; resolve current stable-ID row or fallback at dismissal, not a stale captured target |
| GP26-08 | Repeated show/close harmless; original background flag preserved; Close action and child semantics retained; modal-only solution accepted |
| GP26-09 | Adjustable value and ordinary drag use actual shared state; +/-5, clamping and exactly-once changed callbacks; no unrelated quantity-button requirement |
| GP26-10 | Active operation ID, bounded progress, first terminal result and stale/duplicate suppression; preserve meaningful terminal state |

Unit seams must not silently repair the answer. If a static notification call or
opaque helper prevents observation without changing subject semantics, record the
observable subset and the unassessable portion. Do not claim delivered focus or speech
from metadata or a recorded notification request. Test-only adaptations need explicit
provenance and separate outcomes from untouched-source compilation.

Accepted alternatives and ungradable boundaries are in the frozen candidate
[controller review](../failure-driven/candidates/CONTROLLER-REVIEW.md). The new
companion tests are useful evidence, not permission to impose their helper names or
extra product requirements on these answers. Exploratory GP26-07..10 remain distinct
from qualified gold cases.

## Reporting

Keep original source grades and new compiler/unit outcomes side by side. Distinguish
subject defects, oracle defects, scaffold errors, missing inputs and infrastructure
failures. Never repair an original answer in place or mark a missing answer passed.
Report every cell, including code-free, compile-failed and not-assessable cells.
No candidate promotion or baseline edits follow automatically from successful tests.

## Delivery outcome

The full30-minute window completed. The final coordinator check still records the
request as stored, provider-delivered:false, work-accepted:false, read-by:empty,
and no new incoming messages. No answer bundle has been received or verified.
Polling has stopped; no background job remains. Compile/unit answer checks are
not run. BigDog must export the preserved bundle against the original request;
no duplicate allocation or model regeneration is needed.

The intake plan and its two offline checks are prepared locally and uncommitted.
The previously reconciled updates are pushed throughb90bdcd. Claude, released
skill0.2.2 and frozen baselines remain unchanged.
