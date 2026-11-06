# Paired UIKit Evidence and Evaluation Tasks

All tasks below are pending unless their completion evidence is explicitly recorded.
Native evidence already exists for some features; that does not complete their paired
evaluation work. This file augments, rather than rewrites, the pinned
[UIKit completion audit](../../../code-examples/UIKIT-COMPLETION-AUDIT.md).

## Work Packages

The [UIKit coverage-closure campaign](uikit-closure-v1/README.md) now replaces small
delivery tranches for UPAIR-07/08. It accounts for all 209 clauses and 15 rules,
reuses completed packages, and pairs three newly identified behavioral families
with separate draft questions/rubrics. The frozen sequential native campaign
completed 104 checks with expected outcomes: 202 positive methods and 66 intended
negative rejections across 19 packages. Independent review and baseline eligibility
remain pending. Earlier
pending rows below are historical progress notes, not a request to rebuild work.

The [eight-answer UIKit checkout review](checkout-review-20261106/README.md)
records first type-check outcomes and provisional source assessments for existing
GP26-03 outputs. Exact first failures are preserved privately; BigDog adjudication
is requested, not accepted yet. This is FD-04 calibration evidence, not completion
of the unit-test or baseline gates. GP26-04 SwiftUI remains deferred.

The [focused checkout units](checkout-review-20261106/UNIT-REVIEW.md) subsequently
ran eight configuration methods on the four compiling answers: seven passed,
one original-answer typography-preservation test failed. Missing-member answers
were not repaired. This supplements the first compiler record; BigDog has not
yet acknowledged either return packet. No gold prompt or frozen rubric changed.

Subsequent [BigDog adjudication](checkout-review-20261106/ADJUDICATION.md), cursor
1425, accepts the scoped first-compile/unit evidence and closes that dependency.
Earlier pending labels above describe delivery-time status. Full answer correctness,
broader FD-04 calibration and promotion remain separate. R14 is inconclusive;
R16's preservation defect is confirmed; no further builds or repairs are needed
for this bounded eight-answer review.

| ID | Story and owner role | Dependencies | Acceptance criteria |
| --- | --- | --- | --- |
| FD-01 | As a maintainer, I need adjudicated incidents so faulty tests do not become gold answers. Author + independent reviewer | None | Classify all F01-F08 and C01/C02; retain exact archive links/hashes; identify claim and oracle limits; record disputed interpretations. FR-01/02/06 |
| FD-02 | As a developer, I need questions phrased like my actual tasks. Case author + reviewer | FD-01 | Review draft prompts; extract minimum public starter fixtures; assign family/lane; remove answer hints and internal IDs from rendered user text; record source-backed rubric and valid alternatives. FR-03/10 |
| FD-03 | As a worker, I need isolated inputs and reliable result import. Harness owner | FD-02 | Add offline payload builder/import checks in a new overlay; reject missing hashes, condition leakage and hidden solution mounts; preserve unattempted/failed cells; synthetic tests cover unknown telemetry and redaction. FR-04/05/09 |
| FD-04 | As a reviewer, I need grading that accepts correct alternative code. Independent reviewer | FD-02 | Grade a correct example, deliberate defect, plausible alternative and ungradable harness result per pilot family; reconcile differences without weakening contract; freeze rubric revision. FR-02/08 |
| FD-05 | As an owner, I need a bounded zero-spend pilot. Worker + maintainer | FD-03/04 | Confirm model/harness/quota; approve exact four-cell manifest and limits; record first outputs and all failures; do not auto-retry or substitute; sanitized report received. NFR-01/05 |
| FD-06 | As a maintainer, I need a reproducible development baseline. Worker + reviewer | FD-05 | Resolve pilot task/oracle defects in new revisions; freeze overlay; expand approved chunks by coverage, then repetitions; no held-out tuning; distinguish protocol from quality. FR-05/08 |
| FD-07 | As a UIKit author, I need every remaining feature paired with a user challenge. Local author, on resumption | FD-01/02 + owner resume | Complete feature rows below with source/test/prompt/rubric mappings; record native and eval status separately; preserve failures before fixes. FR-01/07/10 |
| FD-08 | As a maintainer, I need measured skill improvements rather than benchmark-specific patches. Skill author + reviewer | Accepted FD-06, relevant FD-07 | Propose smallest generalized reference/instruction change; paired baseline/candidate evaluation; independent held-out families; critical-error and quality gates reviewed before promotion. FR-08, NFR-02/03 |

Work-in-progress limit: at most two new semantic families in the pilot. Harness and
general-Swift cases remain diagnostic lanes. Use named owner acknowledgment, not an
assumed assignment, before scheduling work. There is no estimated completion date.

## Backfill Existing Evidence

| Family | Evidence / draft prompt IDs | Required completion |
| --- | --- | --- |
| Typography environment | F04/F05, FD-P03 | One family with configuration and propagation variants; exact effective-state oracle, no rendered-layout claims |
| Media choice | F07, FD-P05 | Synthetic minimum fixture; full/forced distinction; no-track/unknown handling; source-backed accepted alternatives |
| Ownership | F02, FD-P02 | Positive and retained-target negative control; defensible lifetime boundary |
| Native-role interpretation | F06, FD-P04 | Scoped interpretation rubric; explicit metadata versus observed native behavior |
| Initial rotor navigation | C01, FD-P07 | Initial/forward/backward/boundary behavior, ordinary access retained; no claim of spoken navigation |
| Diagnostic matcher | F01, FD-P01 | Compiler diagnostic fixture and adapter expectations in a separate harness lane |
| Failure classification | F03, FD-P08 | Assertion versus infrastructure-error fixture; no false passing mutant |
| Swift value comparison | F08, FD-P06 | Minimal compiler task; general-Swift control, not accessibility-specific improvement |
| Acceptance mismatch | C02 | Controller-only evidence-review task before any gold promotion; trace criterion to actual assertions |

## Remaining UIKit Feature Pairs

The new [checkout preservation contract](checkout-contract-v1/README.md) extends
UPAIR-02 with explicitly supplied existing-button wiring, repeated updates and
configuration preservation. It is a new authored example, not a repair of the
eight reviewed answers. The first failed configuration oracle is preserved;
production source remains unchanged after the oracle revision. Two separate draft
questions cover implementation and oracle diagnosis. See its validation record
for native outcomes; independent prompt/oracle review and model execution remain
pending. No frozen gold prompt, score report or runtime skill changed.

UPAIR-06C now has [speed-control evidence](../../../code-examples/pilots/uikit-speed-v1/README.md):
eight positive methods and three intended mutant rejections, with a separate draft
question/rubric. It addresses the identified configuration/direct-action gap;
independent review and broader media coverage acceptance remain pending.

UPAIR-08 now has an [exact clause inventory and first media review](../../../code-examples/audits/requirements-v1/README.md).
All15 guideline sources are pinned;209 selected clauses are inventoried, not counted
as passing tests. Media review identifies UPAIR-06C speed-control semantics as an
open unit contract. Remaining clause reviews and independent acceptance are pending.

UPAIR-07 now has a [sixteen-pilot compile sweep](../../../code-examples/audits/availability-v1/README.md)
with source/manifest hashes, recorded diagnostics and a separate draft prompt/rubric.
All selected source sets compile at deployment26.0; the full public-member
declaration matrix is still required before closing the availability audit.

See [current status](CURRENT-STATUS.md) for the verified six-tranche rollup,
changes since the last pushed commit and sequenced acceptance gates.

UPAIR-01 now has [native evidence and a draft paired case](../../../code-examples/pilots/uikit-naming-v1/README.md):
eight positive methods and three intended mutant rejections. Independent case review
and model execution remain pending.

UPAIR-02 now has [long-text/selection evidence and a draft paired case](../../../code-examples/pilots/uikit-choice-v1/README.md):
nine positive methods and four intended mutant rejections. Its native contracts
passed; independent case review and model evaluation remain pending.

UPAIR-03 now has [configured-color evidence and a draft paired case](../../../code-examples/pilots/uikit-contrast-v1/README.md):
nine positive methods, four intended mutant rejections, and separately sourced W3C
numerical oracles. Native validation is complete; independent review and model
evaluation remain pending.

UPAIR-04 now has [modal lifecycle evidence and a draft paired case](../../../code-examples/pilots/uikit-modal-v1/README.md):
thirteen positive methods and five intended mutant rejections. A new retained-removal
test first failed against unchanged source; that revision and the repair are preserved.
Native validation is complete; independent case review/model evaluation remain pending.
UPAIR-05 now has [edited-rotor evidence and a draft paired case](../../../code-examples/pilots/uikit-edited-rotor-v1/README.md):
twelve positive methods and five intended mutant rejections, including Unicode,
overlap policy and stale callbacks. Native validation is complete; independent
review/model evaluation remain pending.

UPAIR-06A adds [media time/buffering contracts](../../../code-examples/pilots/uikit-media-inspection-v1/README.md)
and a separate draft prompt/rubric. Nine positive methods, one compile check and
three intended mutant rejections passed on iOS26.5. Independent review/model
evaluation remain pending. UPAIR-06B adds
[actual tagged metadata and loaded-asset extraction](../../../code-examples/pilots/uikit-media-metadata-v1/README.md),
with seven positive methods, matched tagged/untagged fixtures and a separate draft
prompt/rubric. Its revisioned validation records distinguish first-attempt warning
from repair and deliberate negatives. Independent review of both media packets
remains pending; UPAIR-07 and UPAIR-08 remain pending.
See [incoming Haiku analysis](HAIKU-INPUT-ANALYSIS.md) for evidence limits and
future no-change, availability and efficiency cases; frozen inputs stay unchanged.

Each row requires a source claim, exact test IDs, recorded environment/result, natural
prompt, atomic rubric, accepted alternatives and a link to baseline eligibility.
The questions below are authoring seeds, not frozen gold cases.

| Pair | Native contract | Developer question seed / evaluation criterion |
| --- | --- | --- |
| UPAIR-01 Decorative/sibling semantics | Explicit decorative flags and distinct control names | "My cards repeat the same buttons. How do I make them distinguishable without reading decoration?" Preserve independent controls; do not infer native defaults from a headless getter. |
| UPAIR-02 Long text/non-color selection | Flexible text configuration and explicit selected/text/symbol state under effective traits | "Long translated names and selected rows become hard to understand at large text sizes." Correct configuration without claiming rendered clipping was unit-tested. |
| UPAIR-03 Contrast | Independently checked formula, color-space conversion and trait-resolved configured colors | "Our semantic colors change in dark mode. Can we check our chosen color pairs?" Numeric configured-color evidence, not screenshot or universal contrast guarantees. |
| UPAIR-04 Modal/restoration | Modal content flags, dismissal and captured restoration target across reopen | "Closing this panel should return attention to its original button." Preserve ordinary dismissal and lifecycle state; argument assertions do not prove focus delivery. |
| UPAIR-05 Edited rotors | Range updates, overlap policy, Unicode and boundaries after edits | "Jumping between highlighted passages breaks after editing the text." Correct ranges and navigation boundaries; ordinary reading remains available. |
| UPAIR-06 Media inspection | Description metadata, stream kind, seekability, buffering/rate/options with unavailable inputs | "I need useful player diagnostics without reading all those details to the user." Keep diagnostics separate from spoken labels; distinguish unknown, indefinite and absent. |
| UPAIR-07 Availability | Actual public declarations and applicable guards at deployment26 | "Can this code run on our older supported iOS version?" Distinguish SDK declaration from runtime/deployment; no invented fallback branches. |
| UPAIR-08 Inventory closure | All15 guideline code contracts mapped to assertions or explicit out-of-scope status | Reviewer audits omissions; do not turn broad inventory closure into one oversized subject question. |

## Definition of Done for Each Pair

- Claim, minimal example, assertion, fixture hash and exact tested configuration are linked.
- Native outcome and expected negative-control outcome are independently interpretable.
- Prompt has neutral-language review and no controller-answer leakage.
- Rubric scores observable task success, accepts valid alternatives and names critical errors.
- Baseline status is explicit: draft, reviewed, frozen, authorized, run or graded.
- Any proposed skill fix links to this evidence and awaits paired evaluation.

This definition does not require UI tests, manual device verification or a model run
to preserve a draft. It does require the relevant execution evidence before claiming
an evaluated improvement.

## Platform companion expansion (2026-11-06)

Owner authorized AppKit/macOS and UIKit/tvOS next; SwiftUI companion expansion stays
explicitly deferred. This extends the unit-library scope, not the frozen skill or
baseline. See [platform batch](../platform-expansion-v1/README.md).

- Platform adapter: separate from pinned iOS adapter; verify actual host/simulator,
  immutable inputs, complete test selection and exact expected failures.
- Initial families: Mac actions/reuse and notification requests; TV actions/reuse,
  preferred focus candidates and selected-trait preservation.
- Preserve first Mac preflight/oracle failures and TV visible-title coverage gap.
- Pair all five families with draft subject questions and separate rubrics.
- Candidate routing: explicit platform/framework, one/two guidelines by default,
  source and contracts opt-in, actual read-byte/hash traces. No runtime promotion.
- Remaining gates: full member availability audit, independent rubric/oracle review,
  approved frontier baselines and measured candidate comparison. Native test success
  does not mark those gates complete. No review submission or acceptance implied.

## Complete prompt/input/output records (owner requirement, 2026-11-06)

Contract: [prompt records](../prompt-records-v1/README.md).

- [x] Define complete capture for authoring, subjects, repairs, reviewers and judges.
- [x] Index the nine platform draft questions with exact text/hashes and explicit not-run outputs.
- [ ] Inventory all earlier UIKit/OS26/scenario/worker prompts and map every actual attempt.
- [ ] Link complete captured requests, attachments, tool exchanges, original answers and analysis.
- [ ] Recover available authoring/reviewer transcripts through approved exports; label gaps instead of reconstructing them.
- [ ] Audit runner/worker exports against this contract before claiming capture completeness.
- [ ] Independently review isolation, artifact hashes, accepted alternatives and analysis.

Acceptance: every used prompt is accounted for; each executed attempt has complete
captured inputs/outputs and separate analysis, or explicit field-level gaps. Drafts
remain not-run. First failures, repairs and judge inputs remain recoverable. No
controller answer material enters subject context; no frozen fixtures are rewritten.

## Mac navigation / Apple TV results closeout (2026-11-06)

- Executed: 34 new positive methods, eight mutants and one original-defect regression;
  all 13 current checks have matching receipts. See [report](../platform-navigation-v1/RESULTS.md).
- Preserved: first key-view ownership failure, unchanged failing assertion, exact
  sources/diagnostics, and both repeated-animation executions. No count inflation.
- Paired: four independent subject questions and separate accepted-alternative
  rubrics, all draft. No subject-model runs or independent review claimed.
- Corrected: historical Finder metadata pin through an [additive amendment](../platform-expansion-v1-amendment/README.md);
  original index/collector/receipts remain unchanged; original verifier archived.
- Captured: 25 local project sessions and 5,644 available input/output/context records
  privately, with hashes and [capture analysis](../prompt-records-v1/CAPTURE-ANALYSIS.md).
  Full provider context, attachments and remote-worker exports remain explicit gaps.
- Remaining: case-by-case transcript mapping/grading, full availability audit,
  independent review, approved frontier baselines; modal/preference/media contracts
  continue in the next coordinated batch. SwiftUI and runtime skill changes deferred.

## Mac / Apple TV lifecycle parity (2026-11-06)

- Executed: 57 new positive methods, ten deliberate mutant rejections and one
  preserved original Mac implementation regression; 15 current checks have
  matching receipts. Nineteen attempts retain the first green versions.
- Paired: four new independent developer questions and controller rubrics, exact
  inputs/hashes, not-run answer fields and explicit authoring capture limitations.
- Preserved: source-audit eligibility gap and pre-execution negative-control defect,
  classified separately from independent model failures.
- Candidate routing: additive lifecycle layer; guidelines by default, source/tests
  only on request. Historical routers and released skill remain unchanged.
- Pending: independent review of these four pairs. Packet is prepared, not sent;
  the existing nine-case BigDog/Gemini scope remains unchanged.
- Next: platform-qualified media selection and loaded metadata, followed by forms
  and richer collections; SwiftUI stays deferred. See
  [parity matrix](../platform-lifecycle-v1/COVERAGE.md) and
  [results](../platform-lifecycle-v1/RESULTS.md).

## Platform media qualification (2026-11-06)

- Added: shared AVFoundation metadata, explicit selection and diagnostic snapshot
  families on Mac and TV, separately qualified; exact execution receipts are in
  [media results](../platform-media-v1/RESULTS.md).
- Paired: six draft platform questions/rubrics, separate input/output/analysis
  records, and opt-in platform-qualified source retrieval. No model runs.
- Preserved: first Mac failing audio-group permission oracle and original code;
  corrected using native permission plus a separately asserted policy seam.
  Local prompt-generator parse error is a tooling issue, not skill guidance.
- Pending: independent review of six media pairs, four lifecycle pairs and the
  existing nine-case queue as distinct scopes. No automatic expansion of Gemini.
- Next: native forms/recovery and richer collection relationships. Shared media
  evidence does not finish AppKit/UIKit UI coverage; SwiftUI remains deferred.

## Native forms and structure (2026-11-06)

- Executed positive suites: 28 AppKit/macOS and 29 UIKit/tvOS methods. Exact
  native negative outcomes are recorded in [results](../platform-structure-v1/RESULTS.md).
- Paired: four new draft questions/rubrics for platform form recovery, Mac outline
  structure and TV shelf structure; exact input hashes and explicit not-run outputs.
- Source-backed policy distinctions: globally unique Mac tree IDs versus
  section-qualified TV item IDs, and independent generation/hierarchy guards.
- Preserved historical prompt inventory checker before scoping it to its declared
  packages; new union check covers all23 platform prompts. No old prompt bytes changed.
- Pending: independent review and later authorized baseline scope. The original
  nine-case BigDog/Gemini plan remains unchanged; no live model runs or UI tests.
- Next: multi-field/async validation ownership, native text/rotor audit, deeper
  collection reuse and media-item replacement. SwiftUI remains deferred.

## Consolidated native campaign

The [cross-platform closure ledger](../cross-platform-closure-v1/README.md) replaces
further small-tranche requests for this native pass. It adds async ownership,
platform text/rotors, native state, row/keyboard entry points and transition recovery,
with thirteen separate development questions/rubrics. It preserves the first failures
and all previous iOS/source inventories. SwiftUI and installed skill promotion stay
separate. The corpus now has507 explicitly dispositioned clauses across36 guidelines;
this is accounting, not a claim of100% behavioral coverage.

Independent agent review should adjudicate one consolidated packet. The maintainer
is not a mandatory manual-test gate. Model runs still require an approved bounded
quota/scope, and these questions do not alter frozen gold prompts or create holdouts.
