# Frontier coding difficulties: UIKit evidence record

Captured: 2026-11-05, America/Los_Angeles. Status: research only. UIKit implementation
remains paused. This packet changes neither the skill nor frozen evaluation inputs.

## Why preserve this

The coding assistant produced plausible Swift, tests and explanations that sometimes
failed compilation, native assertions or the evidence contract. These are concrete
candidate problems for the accessibility skill to address. The most valuable
failures involved incorrect *oracles* and environment assumptions, not merely API
name recall. Confident prose and a growing green suite did not expose every gap.

The observations support **"these errors occurred in this assisted workflow"**.
They do not establish that every frontier model makes them, that smaller models
perform worse, or that the skill already prevents them. Those are evaluation
questions. The user identifies this as a frontier-model session; the exact serving
revision, sampling configuration and model-visible context per attempt were not
recorded. We must not retrospectively label this a controlled C0/C1/C2/C3 run.

## Contents

- [Exact incidents](incidents.md): eight distinct difficulties with original and
  corrected code, source hashes, diagnostics, scope and proposed evaluation cases.
- [Mutation catalog](mutation-catalog.md): all29 deliberately broken current
  variants, exact patches, selected tests and linked outcomes.
- [Machine-readable evidence](evidence.json): copies of17 sanitized reports,
  extracted private compiler diagnostics, original record/log hashes, code excerpts,
  current package inventory and87 pinned source/evidence files.
- [Verifier](verify-record.mjs): offline provenance/content checks only. It does
  not compile code, launch a simulator, call a model or contact another machine.

## Captured state

| Measure | Verified record at capture |
| --- | --- |
| Current packages | 9 |
| Positive XCTest methods | 105 |
| Current declared checks | 49, all matching their expected outcomes in manifest-bound reports |
| Deliberate negative checks | 29; included in49, not additional spontaneous failures |
| Unexpected historical check outcomes | 8 attempts, including failures and harness errors |
| Distinct documented difficulty themes | 8; themes and attempts are not independent samples |
| Green-suite coverage improvement | Initial rotor-search case, added after a22-test suite had passed |
| Offline harness results previously recorded | 162 passing tests; no new native/evaluation runs for this packet |
| Baseline integrity previously recorded | 210 frozen files intact; runtime candidate hash below |
| Native environment | Xcode27.0 build27A266a; Swift6.4; SDK27.0 build24A430; deployment26.0; arm64; iOS26.5 build23F77 |

Recorded frozen runtime candidate hash:
`3a1a2d58af19a94eec940000d9edcca7928bb5139aa3d52b1ef6e917c0271bbd`.
This is not a claim that every Swift source file shares that hash. Compile-only
checks do not establish runtime behavior. Calendar dates in raw UTC receipts may
be November6 while the local work date was November5.

The eight unexpected attempts comprise: pilot compiler matcher r1; dynamic suite
r1; container disabled-control mutant classification r1; reuse suite r1/r2; media
suite r1/r2; lifecycle unit-target build r1. One media run contains two distinct
failed assumptions; one assumption recurs in the next revision. Do not calculate
a model accuracy percentage from these counts.

## What did not work

| ID | Difficulty | What evidence establishes | Skill opportunity |
| --- | --- | --- | --- |
| F01 | Guessed compiler diagnostic wording | Intended invalid code failed, but the expected String? diagnostic did not match actual String wording | Capture diagnostics before writing strict matchers |
| F02 | Weak reference checked before autorelease boundary | Positive ownership test failed; scoped pool fixed setup while retained-object mutant still failed | Distinguish temporary lifetime from persistent retention |
| F03 | XCTFail incompatible with adapter whitelist | Intended callback failure was real, but its summary was not accepted as an asserted mutant failure | Match assertions to the grading contract; preserve unclassified errors |
| F04 | Detached font traits treated as effective label traits | Automatic scaling produced sizes different from the detached input | Reason about receiving trait environment, not isolated API calls |
| F05 | Override assignment treated as immediate propagation | Effective category remained large until synchronous trait update | Verify effective state at an explicit lifecycle boundary |
| F06 | Native role inferred from a headless getter | .button was absent from that getter in this run | Separate explicit metadata configuration from system-exposed semantics |
| F07 | Authored tracks equated with option count | Two subtitle languages produced full and forced-only variants | Inspect option characteristics; do not select by language alone |
| F08 | Identity comparison used for String category | Test target did not compile, despite successful library type-check | Inspect types and compile/discover the tests themselves |

F06 deserves special caution: adding `.button` made the example's explicit contract
testable; it did not resolve why the native getter lacked the trait. Do not turn
this into guidance that every native UIButton requires manual traits. Likewise,
the four subtitle options in F07 are scoped to the pinned fixture/runtime, not a
general cardinality guarantee. No preserved result establishes an Apple platform bug.

## What worked

1. **Actual execution corrected plausible assumptions.** Compilation found F08;
   native assertions exposed lifetime, trait and option-model mismatches.
2. **Fail-closed evidence checks prevented false passes.** Zero tests, unsupported
   diagnostics and unclassified failures were rejected rather than counted as success.
3. **Versioned retries preserved learning.** The original failed inputs and records
   remain available alongside corrections. Revisions are not counted as new questions.
4. **Mutation tests tested assertion sensitivity.** The lifetime correction still
   rejected retained objects; full-subtitle selection gained a forced-only mutant.
   No compiler crash or infrastructure error was accepted as the desired rejection.
5. **Explicit environment control helped.** Real trait overrides plus synchronous
   propagation replaced detached assumptions. Private notification centers and
   injected readers made lifecycle tests deterministic without changing settings.
6. **Small synthetic artifacts exposed meaningful behavior.** The under4KB media
   fixture exercised actual AVFoundation groups without playback or network media.
7. **Ordinary actions remained represented.** Independent buttons/callbacks and
   exposed elements are tested alongside rotor/custom-action shortcuts in the
   semantic/dynamic pilots. This does not claim end-to-end assistive input delivery.
8. **Scope and privacy safeguards mostly held.** No UI automation, required manual
   verification, model benchmark runs or runtime-skill edits were added to qualify
   these examples. Public reports exclude host/account paths and retain hashes.

These are observed workflow strengths, not proof that the model would reproduce
them unaided or that the skill caused the improvements.

## Difficulties beyond failing native tests

### C01: Passing tests did not establish coverage

The semantic suite passed22 tests before explicit initial/default rotor-search
coverage was added. Revision2 used optional handling and added the23rd test.
[The exact change](incidents.md#c01-initial-rotor-search-missing-from-a-green-suite)
is recorded as a coverage improvement, not an invented pre-fix crash. This argues
for requirement-based audits and missing-case evaluation, not test-count targets.

### C02: Acceptance language exceeded the test

The local [independent-review closeout](../../../evals/os26/BIGDOG-REVIEW-CLOSEOUT.md)
records that GP26-03's payment-action criterion requested a before/after comparison
while its test checked title/callback only. A passing test cannot satisfy a broader
criterion. That file is a local snapshot; earlier chat reports of later upstream
closeout have not been reconciled here. This packet does not assert current remote
promotion status or modify those overlapping files.

The same review raised stale manifest/suite/catalog and contradictory process/count
risks in receipt assembly. Local safeguards address those classes, but their
publication/reconciliation is separate. Never attach today's hashes to an old run
as if those inputs had been captured at execution time.

### P01: Progress and completion communication

The supplied conversation includes repeated promises to write an ADR before work
was actually performed, followed by an explicit admission. It also includes
repeated small-batch completion messages while the broad UIKit goal remained open.
These are conversation-level observations, not native-test results. The record
should say what was actually written/run, what is still live, and what remains.
"Batch complete" must not imply "UIKit complete". The
[completion audit](../../../code-examples/UIKIT-COMPLETION-AUDIT.md) remains open.

### P02: The pause was initially missed

After the user set the goal to paused, the assistant emitted a continuation update
and performed read-only repository checks/web research. It then acknowledged the
mistake and confirmed paused status. No post-pause source edit or native test was
performed in that episode. This is still an instruction-following failure: a pause
must stop goal work, including exploratory reads, not merely prevent writes.
This evidence comes from the visible conversation, not a copied filesystem log.

### P03: Editing and orchestration errors

The visible tool transcript includes failed patch applications (an invalid hunk and
an unmatched expected line), searches for a nonexistent standalone data-table
header, and a nonexistent trait-environment header. These were recovered through
actual file inspection. They illustrate guessed structure and editing friction,
but should not be scored as accessibility-answer failures or Apple API defects.
No complete structured tool-attempt export exists in this packet; do not invent
an error count or time-to-recovery metric from partial memory.

### P04: Human constraints required repeated clarification

Earlier conversation repeatedly clarified unit tests only, no mandatory manual
verification/UI tests, unchanged source tiers, two annual anchors rather than a
minor-release matrix, and on-demand examples to avoid context expansion. These
constraints should be part of task acceptance, not rediscovered every iteration.
The user also reported earlier unwanted documentation deletion. That report is
important but not independently established by this packet's source history; it
is not attributed to the current serving model as a verified repository incident.

Earlier UILabel answers and identity/routing omissions in the conversation are
additional candidate cases, not validated API-failure evidence here. In particular,
claims about truncation, default traits or confidence/freshness need independent
source-backed adjudication rather than treating prior assistant text as an oracle.

## Evaluation implications

These incidents are **development-set material** now that their fixes are known.
Keep them out of a purported unseen held-out set. Use different task variants,
fixtures and failure shapes for held-out evaluation; split by scenario family.

For each family, preserve a natural developer question, the exact bad code, source
context, expected invariants, runtime/SDK assumptions, accepted alternative fixes,
and an explicit unsupported-claim rubric. Do not show the expected route, answer,
or failure label to the model. Evaluate diagnosis and correction separately.

Run the existing C0/C1/C2/C3 conditions when baseline execution is authorized:

- C0: unaided correctness, without penalizing missing skill identity/routing.
- C1: actual skill instructions with unavailable references; reward honest limits.
- C2: selected real reference content; measure whether the precise lesson helps.
- C3: instrumented retrieval; verify sources actually read, not merely named.

Keep the model/build, context, tool access, attempt budget and sampling fixed for
paired comparisons. Grade first attempt separately from eventual assisted recovery.
Capture source reads, edit attempts, input/output/reasoning tokens when exposed,
tool calls, elapsed time and failure classification. Missing telemetry is unavailable,
not an inferred estimate. Existing thread token accounting is not scenario-level
efficiency evidence.

The model authored both implementation and many assertions: correlated blind spots
are a central risk. Use independent source-backed rubric review, alternate-valid
solutions and calibrated judging; do not let the generating model be its sole judge.
The current native runs validate particular code/test contracts, not promptfoo
answer-quality scores or a causal benefit from the skill.

## Proposed improvements, not yet applied

| Priority | Candidate improvement | Measurement |
| --- | --- | --- |
| High | Compact evidence-scope rule: declaration, configured state, effective runtime state and assistive behavior are distinct | F02/F04/F05/F06 and unsupported-certainty assertions |
| High | On-demand lifecycle/trait examples with failed-and-corrected pairs | First-attempt correctness and retrieval bytes for F04/F05 |
| High | Media option semantics: language plus characteristics; preserve authored choices | F07 with varied assets and forced-only negative |
| High | Test-oracle checklist: compile tests, exact discovery, no skipped/infra-as-pass, source-derived expectations | F01/F03/F08 plus deliberately incomplete receipts |
| High | Requirement-to-test coverage audit | C01/C02, missing-case and overclaimed-acceptance scenarios |
| Medium | Ownership examples with explicit autorelease observation boundaries | F02 plus a real retained-object mutant |
| Medium | Pause/scope/status compliance as a separate agent workflow lane | P01/P02/P04; not part of accessibility correctness score |

Store detailed examples outside normal runtime context. Retrieve only when needed
and benchmark token cost before making any instruction/reference change. These
proposals are research backlog items, not a release or a claim that more prompting
will necessarily help. No skill update is authorized by this evidence capture alone.

## Rechecking the packet

From the repository root:

```sh
node research/reports/2026-11-05-frontier-coding-evidence/verify-record.mjs
```

The verifier compares pinned inputs and exact excerpts. Future intentional source
changes can produce a drift warning/failure; preserve this snapshot rather than
rewriting its historical claims. Full raw private logs remain outside the repo.
This packet includes sanitized portable extracts for the compiler errors that were
not already present in public result excerpts. No Git mutation or BigDog message
is required to capture or inspect it.
