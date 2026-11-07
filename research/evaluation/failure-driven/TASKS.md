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

## Versioned comparison tranche — 2026-11-06

**Current status: AGY executed and independently source-graded; Claude deferred.**
The [report](../../../evals/reports/skill-0.3.0-dev.1-vs-0.3.0-dev.2-20261106/README.md)
and [execution status](candidates/PREPARATION-STATUS.md) record the accepted scope.

- Checkout adjudication closed through message 1426. Campaign requests 1427/1428
  were read and acknowledged; campaign independent acceptance remains pending.
- The owner selected semantic versions 0.3.0-dev.1 and 0.3.0-dev.2, default-on
  identity/version and consulted-file reporting, with separate explicit opt-outs.
- All 28 private inputs were frozen. Controller revision 2 independently calibrated
  alternatives with reviewer exposure disclosed. Seven offline executor checks passed.
- Owner approved the proposed comparison, then selected only the 14 AGY calls after
  Claude reported no subscription login. No silent substitution or scope expansion.
- AGY completed 14 calls using 65,400 tokens, with no retries, fallback or billing
  signals. Grades: 0.3.0-dev.1 six contracts met plus one inconclusive checkout;
  0.3.0-dev.2 seven met. No established material gaps or critical flags.
- Total tokens rose 1.00%, median 3.29%; the efficiency screen was not met. Identity
  and ROUTING appeared in all 14 answers; actual retrieval was not measured because
  references were supplied. No new native answer checks were run.
- Rounded remaining quota was five-hour 100%→99%, weekly 66%→66%. AGY's grant is
  exhausted. Claude's 14 cells remain unattempted; no automatic later launch.

This is a bounded development screen, not fresh confirmation or gold promotion.
Wider FD-05/06/08 gates remain open. Released skill 0.2.2, historical evidence and
frozen baselines are unchanged. Initial planning and blocked preflight observations
are preserved in the linked reconciliation/validation records and private receipts.

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

## SwiftUI campaign - owner-authorized resumption

The current owner explicitly authorized the [SwiftUI campaign](../swiftui-campaign-v1/README.md)
on iOS, macOS and tvOS; earlier SwiftUI-deferred notes remain historical. This is
not promotion of the released skill or authorization for new model calls.

- Seven families cover all five planned workstreams, with real modifier compilation
  and narrow Binding/state/policy/native-coordinator units; no tree introspection.
- All 15 guidelines and 217 requirements have explicit dispositions, including
  unresolved broader interop and real media-application requirements.
- Final positive suites select 62 methods per platform. Shared definitions and
  platform executions are reported separately, with exact native receipts.
- Preserve the AppKit old-native-target failure, the autorelease-oracle failure,
  the first sources/diagnostics and their separate repair histories.
- Twenty-one questions/rubrics remain draft development pairs, not gold or holdouts.
- Consolidated independent review is prepared, not sent/accepted. Claude remains
  pending; no paid/model runs, UI tests, mandatory manual gates or Git publication.
- Exact negative-control outcomes and final acceptance are in the campaign report;
  successful units do not establish generated SwiftUI accessibility semantics.

## SwiftUI forwarding continuation

The initial SwiftUI campaign is committed as0177195. The owner requested the next
tranche; [native forwarding](../swiftui-forwarding-v1/README.md) adds41 positive
methods on each existing iOS/macOS/tvOS anchor,5 intended negative executions and9
new draft task/rubric pairs. Preserve three failed builds (test generator, guessed
Swift role member and prematurely used global spelling), the source-audited inactive
UIKit mutant and frozen-plan transition. No failed build is a successful rejection.

The overlay links13 earlier gap rows to new native-subset evidence. The original
217-requirement ledger is not rewritten; none of its broad host requirements is
silently closed. Final metadata/getter/callback scope and residual assertion gaps
remain explicit. Technical review is prepared, not sent or accepted; model runs,
Claude, released skill and frozen baselines are unchanged. New work is uncommitted.

## Candidate0.3.0-dev.3 - research iteration

Forwarding evidence committed asa56c9a5. The owner requested further skill iteration;
[dev.3](candidates/0.3.0-dev.3/README.md) is an additive research snapshot, not a
released entrypoint replacement. Existing candidate files and VERSIONS.json hashes
remain unchanged. A local manifest registers exact subject and optional asset hashes.

Shared body3286 bytes versus dev.2's4910 (-33.08%); native-only path4628,
validation-only4511, both5853, excluding task-topic references held constant across
pairs. Byte checks are not provider token or quality results. Six offline checks
pass, including rejecting execution arguments on the new offline planner.

The proposed14-cell matched dev.2/dev.3 comparison is not executable or approved:
exact private wrapper/reference serialization, independent review and fresh provider/
quota allocation remain pending. Existing AGY answers cannot substitute for newly
matched baseline calls. No new models, native-answer tests, Claude activity, messaging,
paid work or skill promotion was performed. Candidate/controller input and grading
records remain separated; previous known failures do not become new holdouts.

## Substantial milestone bundle0.3.0-dev.4

Owner rejected small frontier evaluation increments and requested a large local
iteration. [dev.4](candidates/0.3.0-dev.4/README.md) consolidates eight failure-driven
task notes with explicit metadata routing, opt-in example/contract lookup, real read
traces, byte limits, source-gap handling and a55-input provenance audit.48 routing
rows include3 explicit missing-primary mappings; no irrelevant substitute is used.

54 new offline checks pass; these are not model routing/quality scores. Shared body
3439 bytes; full same-guideline/note static comparison reports median-9.69% bytes,
not token savings. Earlier dev.3 is retained without triggering its unused14-cell
proposal. No evaluation calls, quota allocation, model substitution, Claude activity,
worker message or released skill/baseline change. One future milestone evaluation
requires independent qualification and explicit scope approval, not per-version runs.

## Consolidated candidate 0.3.0-dev.5

- [x] Draft eight topic families across iOS/UIKit, iOS/SwiftUI, macOS/AppKit,
  macOS/SwiftUI, tvOS/UIKit and tvOS/SwiftUI (48 applications).
- [x] Add twelve no-change, ownership, target-scope and evidence-boundary controls.
- [x] Separate subject inputs from alternative-aware controller rubrics; retain
  unrun outputs explicitly and keep known scenarios out of holdouts.
- [x] Strengthen conditional candidate guidance without modifying released files.
- [x] Validate subject hashes, all route pairs, context boundaries and source gaps.
- [ ] Independently review each question/rubric and exact claim/assertion links.
- [ ] Freeze qualified milestone payloads and obtain explicit bounded run approval.
- [ ] Measure paired answer quality and real token use; no benefit claimed yet.

## Local qualification before distillation

- [x] Account for all 60 dev.5 cases and criterion-level pending review.
- [x] Join all 36 manifest-linked cases to existing matching native contract receipts,
  including older package-local UIKit records; preserve first discovery limitation.
- [x] Add adversarial receipt checks for false passes, missing execution, source drift,
  environment mismatches and deliberate-assertion versus infrastructure failures.
- [ ] Review exact assertion bodies and bind each rubric criterion, rather than
  counting lexical test leads or broad package passes as whole-question coverage.
- [ ] Resolve three primary-source mappings and qualify source freshness separately.
- [ ] Freeze representative reviewed cases before approved frontier comparison;
  distill only after trustworthy contract and answer-quality evidence.

See research/evaluation/local-qualification-v1/README.md. No model/native reruns,
released skill edits or frozen baseline mutations in this qualification pass.

## Off-the-shelf offline analysis

- [x] Install isolated pinned Ajv, Markdown and Promptfoo tooling with lifecycle
  scripts disabled; preserve lockfile and keep dependencies out of source tracking.
- [x] Extract pinned SwiftLint locally; compile syntax probe against installed
  Xcode SwiftSyntax/SwiftParser without a new Swift package dependency.
- [x] Validate 15 records, inspect 110 Swift files and replay 26 preserved excerpts
  with deterministic checks, no model generation and network denial.
- [x] Add adversarial adapter regression tests and preserve integration failures.
- [ ] Use syntax observations to propose exact assertion-to-criterion bindings;
  do not equate syntax counts or excerpt equality with answer-quality improvement.

See research/evaluation/local-analysis-tools-v1/README.md. Full historical answers
remain unavailable in the public summary; no reconstructed outputs were graded.

## Deferred Claude completion and Sillycon delivery — 2026-11-06

Executed after explicit owner authorization:14 Claude Haiku calls,87,619 tokens,
no retries/fallback/billing signals. Both0.3.0-dev.1 and dev.2 meet six contracts,
with checkout layout inconclusive; no established critical flags. Dev.2 total tokens
+1.02%, median+3.34%; no efficiency or promotion claim. Independent grading used a
fresh context and neutral/version-redacted answers. Both models' original28 cells
are now executed, with separate token/cache conventions and source-only grades.

Sillycon request1433 was actually read/acknowledged. Existing14 AGY first answers
and exact relevant input/controller/grade records were delivered on the private share,
SHA256 a9c28497ae64e46917ea703cccb996adfd1734aca55154e73d5261b2b0f19f14,
142,782 bytes,101 members; readback verified. Coordinator acceptance/delivery notices
1434/1435 sent once; peer verification/native completion not yet confirmed. No raw
answers/account records are public. No remote native execution or new AGY calls.
See candidates/SILLYCON-AGY-DELIVERY-20261106.md and the new Claude report.

## Assertion-level binding continuation

- [x] Commit and push the local-analysis checkpoint, preserving upstream Claude
  completion findings and leaving unrelated private/AGY working files out.
- [x] Extend SwiftSyntax observations with owner/method identity, exact UTF-8 source
  ranges, assertion expressions and conditional-compilation ancestry.
- [x] Account for 198 criteria across all 60 draft cases in an additive overlay:
  81 criteria / 35 cases have narrow links to 143 methods and 317 assertion sites.
- [x] Verify exact historical unit receipts for every selected method, and link 30
  methods to matching same-manifest negative controls. No new native execution.
- [x] Preserve scope-control selection failure and test repaired unsupported axes.
- [ ] Independently review semantic applicability, residual gaps and alternatives;
  source/answer-only criteria and whole-criterion gold acceptance remain separate.

See research/evaluation/assertion-bindings-v1/README.md. New bindings do not alter
candidate subject/rubric bytes, released skill files or frozen baselines.

## Consolidated operational rubric gap closure

- [x] Publish assertion-binding checkpoint b9c0a14; unrelated coordinator/AGY files
  remain outside Git publication.
- [x] Define pass, gap and insufficient-evidence decisions for all 198 criteria,
  including the 117 without unit-subset bindings. This closes grading definitions,
  not missing behavioral evidence or independent gold qualification.
- [x] Correct accepted alternatives for all 12 controls without editing frozen
  subject/original controller bytes; separate no-change from ownership clarification.
- [x] Add three existing checkout revision-2 method/receipt links for native iOS text
  and Pay preservation, retaining the original oracle failure and other target bounds.
- [x] Add exact local source/policy anchors and a review-record consistency validator
  rejecting stale hashes, fabricated excerpts, incomplete criteria and fixture-pass
  substitution for answer grading. No semantic auto-grading or independent acceptance.
- [ ] Independently review the operational packet and source applicability; resolve
  three primary-source mappings before API-specific qualification.
- [ ] Freeze the approved representative selection before any separate model-run
  request. No model calls, spend, new native execution or release promotion here.

See research/evaluation/rubric-closure-v1/README.md. Earlier bindings, candidate
snapshots, released skill, native receipts and frozen baselines remain unchanged.

## Research-backed skill-lift tranche

- [x] Reinterpret preserved comparisons as separate gain/regression/preservation/
  persistent-failure/inconclusive outcomes without rewriting historical grades.
- [x] Keep local-model cohorts diagnostic, frontier cohorts separate, compiler
  outcomes distinct and AGY inconclusive-to-pass out of fail-to-pass gain counts.
- [x] Add strict matched-input identities, family-clustered quality uncertainty,
  critical-error and two-point non-inferiority gates. Numeric flags do not authorize
  runs, publication or promotion; independent/held-out/platform review remains open.
- [x] Report measured/missing token telemetry separately. Focused input savings do
  not establish broader efficiency when total tokens are unavailable or worsen.
- [x] Separate instrumented reads, offline metadata lookup, supplied content and
  routing-only assertions; do not infer semantic use from a read or file name.
- [x] Add 24 realistic draft activation inputs (12 relevant, eight near misses,
  four ambiguous) with labels outside subjects; no holdout/gold promotion or runs.
- [x] Measure current candidate context bytes against dev.2 using the same guideline:
  median -4.89% on 45 mapped rows, three source gaps, no provider-token estimate.
- [ ] Independently review/freeze the representative scenario selection and same
  rubric before one separately approved bounded frontier milestone. Distill after
  useful outcomes, not after a higher structural check count.

See research/evaluation/skill-lift-v1/README.md. No skill edits, baseline changes,
model calls, new native runs, installations, worker messages or spend.

## Controlled milestone preparation

- [x] Commit the operational-rubric/skill-lift checkpoint locally as fd31933;
  no push requested in this continuation.
- [x] Propose one 24-case/48-cell paired package: three domain applications in each
  of six platform/framework lanes, all eight topics, plus six controls. Twelve
  related families, not 48 independent questions. Approved calls remain zero.
- [x] Preserve equal task bytes and shared host boundaries, keep rubrics/grades out
  of subject payloads, distinguish C0, C2 supplied-reference domain tasks and C1
  reference-free controls. No C3/installed-discovery or released-version claim.
- [x] Account for all 60 original drafts: 24 selected, four quarantined, 32 deferred
  development cases. Existing held-outs remain untouched.
- [x] Quarantine ambiguous tvOS UIKit switch premise against the actual public SDK
  declaration; retain original prompt/hash, source evidence and a separate unselected
  UIButton-based repair draft. Do not score the bad premise as a model failure.
- [x] Seal payload hashes and add drift, overwrite, isolation and authorization
  preflight checks. No provider/client/execute path exists in the offline package.
- [ ] Independent review, source applicability, actual isolated harness and exact
  model/provider plus bounded quota/output/total-token/time authorization remain
  prerequisites for a separately approved live milestone.

See research/evaluation/milestone-package-v1/README.md. No model calls, new native
example execution, spend, released-skill edits or frozen-baseline changes.

## Local adversarial milestone pre-review

- [x] Audit all 24 selected scenarios and supplied references as author work, without
  claiming independent review or invoking another model.
- [x] Record two required reference repairs (manual-gate conflict and wrong-topic
  list/form guidance), six platform-metadata warnings and two OS27 context flags.
- [x] Prepare two separate reference-only payload proposals; preserve original
  candidate body, paired request, all sealed v1 files and prior grades.
- [x] Link existing target compile receipts/declaration leads for all six scope
  warnings, explicitly without treating metadata mismatch as API unavailability.
- [x] Preserve original/guarded deterministic counterexamples for malformed nested
  preflight data and explicitly unverified model identity. Add forward-use guards;
  historical modules/results remain unchanged.
- [x] Add an author-readiness gate that distinguishes passing integrity from pending
  source review. Its nonzero result is expected while eight findings remain open.
- [ ] Incorporate reviewed reference corrections in a new package revision; qualify
  remaining target-specific source claims, then independent review before live quota.

See research/evaluation/milestone-audit-v1/README.md. No model runs, spend, new native
example execution, installs, worker messages or released-skill/baseline changes.

## V2 context package and platform applicability

- [x] Commit prior milestone/audit checkpoint locally as 760554c; no push requested.
- [x] Apply both exact reference corrections in a separate sealed v2, preserving v1.
- [x] Resolve all six inherited platform-scope questions: five target-specific public
  SDK cards plus the project-only testing context. Preserve enclosing @available
  annotations, distinguish module migration dates, and link existing target26 compile
  receipts without claiming runtime propagation, generated semantics or delivery.
- [x] Keep all generic arms, requests, candidate body and rubric identities unchanged;
  seven candidate cells change with explicit C2-sdk-scoped / C2-project-policy-only
  profiles. No instruction/reference attribution or C3 discovery claim is inferred.
- [x] Verify original package/source pins, sealed rebuilds, byte ceilings, malformed
  preflight inputs and zero live authorization. No models, new native runs or spend.
- [ ] Independent review of v2 evidence limits and alternatives, clean-harness
  attestation, exact provider identity and bounded quota approval before live work.

See research/evaluation/milestone-package-v2/README.md. Runtime skill, frozen
baselines, original guides/candidates, native evidence and quarantines are unchanged.

## SwiftUI Reconciliation And Real Media Selection

- [x] Preserve upstream checkpoint `8e51ee9` and pin2,267 tracked inputs, including
  released skill, frozen baselines, previous native evidence and sealed BigDog v2.
- [x] Reconcile217 requirements/15 rules with actual existing assertion/receipt
  bindings and the13-row forwarding overlay; retain explicit scope for all28
  previously unresolved rows. No whole-clause coverage inferred from compilation.
- [x] Add actual AVFoundation item/group selection, SwiftUI binding and observation
  invalidation, async/current-item ownership and scoped retry composition.
- [x] Validate36 positive methods per platform on macOS27/iOS26.5/tvOS26.5,
  deployment26/SDK27; four distinct intended mutants reject on the shared host lane.
- [x] Preserve25 native attempts and first source/diagnostics before two test-compile
  repairs, one harness snapshot repair and the separate preservation-oracle repair.
  Add forward-use error classification; historical adapters/results stay unchanged.
- [x] Pair three behavioral families with nine complete draft developer questions,
  separate alternative-aware rubrics and actual assertion bindings. Four general
  Swift/harness/oracle diagnostic questions remain separate, draft/not-run.
- [x] Preserve actual source selectors and SDK hashes; do not confuse a deprecated
  neighboring declaration or comment with the async loader's availability.
- [x] Keep progressive disclosure bounded: guidance first, source/contracts and
  complete fixture on demand, no controller or incident context by default.
- [x] Pass1,301 offline checks, baseline210-file verification and historical87-pin
  verification. Zero model calls, additional spend, UI tests or mandatory manual gates.
- [ ] Supplemental live stream-state observation: item rebinding and deterministic
  observer teardown remain a named testable implementation remainder (G-015-L32).
- [ ] Independent source/oracle/prompt review and accepted findings for a later
  candidate. No released-skill promotion or BigDog sealed-input changes implied.

See [consolidated report](../swiftui-closure-v1/RESULTS.md) and
[review packet](../swiftui-closure-v1/REVIEW-REQUEST.md). Prepared, not dispatched;
Git publication remains separately authorized.

## Separate-Context SwiftUI Review And Candidate Dev.6

- [x] Retain original and follow-up reviewer output separately from author
  adjudication. One review agent, two source-only turns; no human/model-lift claim.
- [x] Reproduce three failing assertions against unchanged prior source: stale Off
  after reload, stale Off after replacement, and a filtered native choice labeled Off.
- [x] Validate corrective media-v2 with44 methods/platform, three target compiles
  and two new intended mutants; keep all native attempts and earlier batch immutable.
- [x] Narrow cancellation to cooperative return checks versus immediate explicit
  owner invalidation; state external reload ownership and include store task identity.
- [x] Create nine revised complete media-only question/rubric pairs. Remove worked
  form/generation scaffolding, ask for tests, separate correctness/evidence grades,
  exclude implementation-only notification/key/timing diagnostics from grading.
- [x] Distill accepted lessons into research-only0.3.0-dev.6. Concern notes and target
  SDK excerpts first; source/complete runnable units only on request. Other routes
  inherit pinned dev.5 limits; no silent requalification of unrelated source gaps.
- [x] Pass1,332 offline checks; verify baseline210 files, historical87 pins, prior
  closure738 pins and inherited/sealed141 pins. No released-skill/baseline edits.
- [ ] Publish consolidated checkpoint when authorized; let BigDog complete its
  unchanged comparison before selecting a later candidate comparison with explicit
  quota limits. No new frontier benchmark or provider run authorized by this work.

See [review results](../swiftui-review-v1/RESULTS.md) and
[candidate dev.6](candidates/0.3.0-dev.6/README.md). Live stream observer lifecycle
remains outside this extension and explicitly unresolved; no UI/manual gate added.

## Gemini Exact-Message Transport And Approval Preparation

- [x] Materialize the reviewed composite controller separately:78 criteria,3 action
  overrides,24 source bindings and5 OR-01 controller-only provenance corrections.
  Preserve all48 original payload bytes and previous experiment identities.
- [x] Export exact messages-only subject files under opaque names, with operator
  metadata/controller files separate. Folder layout is not runtime isolation.
- [x] Add35 offline fixture checks for role/content preservation, hidden context,
  tool/controller/session leakage, model substitution, malformed evidence and quota
  thresholds/resets/unknown data. Schema consistency never enables live execution.
- [x] Capture local AGY help only: stream-JSON documents one turn per line; no
  undocumented system/tools flags or agent-mode isolation guarantees are inferred.
- [x] Reobserve all6 installed SDK declarations/hashes without native builds; this
  does not complete independent source authentication or all domain qualification.
- [x] Draft one named48-first-attempt subscription-only proposal,5/1/1 proposed
  percentage-point thresholds, zero retries/probes/fallbacks and explicit unsupported
  hard provider token/internal-request caps. No debit forecast or allocation claimed.
- [x] Keep96 exemplar slots/312 judgments visibly not-authored/not-graded. Conceptual
  examples and serializer tests do not complete FD-04 calibration.
- [ ] BigDog returns actual supported AGY1.5.3 transport/isolation proof, or one
  concrete blocked-capability report. Handoff prepared, not sent or accepted.
- [ ] Complete source/oracle and executed exemplar calibration, then request fresh
  owner approval for the exact model, observed quota allowances and supported limits.

See [preflight packet](../gemini-preflight-v1/README.md). All1,373 current offline
checks pass, plus25 historical module checks (overlapping, not independent cases).
No new subject/provider calls, native runs, worker messages or Git publication.

## Owner-authorized Gemini controlled-context comparison — 2026-11-07

- [x] Execute all 48 sealed v2 first attempts under the owner’s continuation approval, with no retry, repair, fallback or extra probe.
- [x] Reconcile 48 independent source-calibration fixtures before grading; grade all 48 answers with arm mappings withheld and retain integration uncertainty separately from narrow frozen criteria.
- [x] Verify input/receipt/grade hashes, 22 harness tests, 210 baseline files and sealed package integrity; close the 48-reservation grant.
- [x] Reconcile remote ff846ac after generation, preserving its separate SwiftUI evidence/dev.6 and this unchanged dev.5 cohort.
- [ ] Review source regressions/persistent gaps against dev.6 before preparing a future candidate comparison; no release or gold acceptance.

[Results](../gemini-controlled-run-20261107/README.md): candidate meets 13/24, generic 9/24; six gains, three regressions, six preserved successes, five persistent gaps and four inconclusive pairs. Displayed Argon weekly usage 0% to 17% is rounded account-wide telemetry. All 24 candidate answers announce dev.5; references were supplied inline, with no native discovery/read claim. No native tests of these generated answers ran; the earlier 12-session diagnostic remains held.

Publication reconciliation: the preflight section above is the earlier local
preparation snapshot, not a request to repeat the separately authorized completed
run. Current follow-up is one retrospective transport qualification report from
existing artifacts only. All further evaluations, probes and grading batches stay
held; preserve both records and sealed subject/controller bytes.
