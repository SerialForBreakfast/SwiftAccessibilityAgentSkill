# Paired UIKit Evidence and Evaluation Tasks

All tasks below are pending unless their completion evidence is explicitly recorded.
Native evidence already exists for some features; that does not complete their paired
evaluation work. This file augments, rather than rewrites, the pinned
[UIKit completion audit](../../../code-examples/UIKIT-COMPLETION-AUDIT.md).

## Work Packages

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
