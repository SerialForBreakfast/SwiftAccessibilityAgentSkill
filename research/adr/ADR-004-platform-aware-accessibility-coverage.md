# ADR-004: Shared Accessibility Principles, Target-Specific Evidence

- Status: Proposed for maintainer review
- Date: 2026-11-05
- Decider: Project maintainer
- Scope: Next-version architecture and evaluation planning; no runtime changes
- Related: [ADR-003](ADR-003-version-anchored-unit-tested-examples.md), [failure-driven evaluation plan](../evaluation/failure-driven/PRD.md), [example infrastructure](../../code-examples/README.md), [Haiku baseline](../../evals/reports/claude-haiku-20261105/README.md)

## Decision at a glance

**Build a small shared core, route to target-specific guidance, and qualify each
claimed target independently. Design the test infrastructure for multiple targets
now; expand native coverage in bounded tranches rather than waiting for exhaustive
coverage or treating iOS results as universal.**

The agent can be useful before every target is validated. Its recommendations must
identify their applicability and distinguish documented guidance from executed
compile/unit evidence. It must not advertise blanket cross-platform qualification.

## Context

This repository describes SwiftUI, UIKit, tvOS, macOS and visionOS guidance. The
current example library is UIKit-first with an iOS native adapter. Separate OS26
evaluation fixtures include tvOS cases; their evidence does not qualify the example
library on tvOS. A framework name, documentation directory or passing shared-logic
test is not evidence that an application target has been compiled or exercised.

The latest Haiku evaluation found an answer that introduced a wrong-platform API
into an iPadOS deletion solution. It also found unnecessary changes to valid native
controls. The skill improved some scores while increasing measured token use by
2.90 times. These development observations motivate better applicability checks and
selective retrieval; they do not prove that this architecture will improve scores.

“All targets” has two meanings: platform families and the concrete build targets
inside a developer's project. A shared package, application, extension and test host
may have different requirements even when they use the same framework. The agent
must inspect the relevant target context, not infer it from `.swift` or SwiftUI alone.

## Architecture

### 1. Shared core: intent and evidence discipline

Keep broadly applicable principles compact: meaningful names/state/actions,
preservation of valid native behavior, nonexclusive access to primary actions,
state consistency, and honest limits on evidence. Link substantive claims to their
source scope. Shared does not mean every API or interaction is universal.

Pure Swift tests may validate application-owned policy such as clamping, state
transitions, deduplication and selection. They cannot establish framework semantics,
rendered accessibility trees, actual focus movement or assistive-technology delivery.

### 2. Framework and target profiles: concrete implementation

Select the smallest applicable framework/topic guidance and its target-specific
constraints. Framework and platform are separate dimensions. A shared implementation
may be reused, but its public API availability and relevant assertions must be checked
for each selected target. Conditional compilation is not proof that every branch works.

Do not add every platform document to every prompt. Reuse the existing single skill
entry point and on-demand routing. Keep evidence archives and full diagnostics out of
normal context. Missing target information requires a scoped question or an explicitly
conditional answer when it materially affects the recommendation.

### 3. Target inventory: explicit coverage, not implied support

Inventory actual project targets before selecting tests. The following is the proposed
coverage map, not a statement of current native qualification or available hosts:

| Target family or variant | Treatment |
| --- | --- |
| iOS and iPadOS | Continue the UIKit foundation; distinguish selected device idiom, framework and application requirements. Shared SDK evidence does not settle all idiom-specific behavior. |
| tvOS | Early next tranche alongside TTR work; target-specific control/action and availability contracts. No claim of remote or focus traversal from unit checks. |
| macOS | Separate AppKit and SwiftUI coverage where encountered; do not import UIKit assumptions. |
| Mac Catalyst | Distinct target environment when present; do not equate it with native AppKit or an iOS simulator run. |
| visionOS | Explicit profile and gaps; add a bounded native tranche when workload and host capability justify it. |
| watchOS | Inventory when encountered; initially a coverage gap, not an inherited SwiftUI qualification. |
| Packages, extensions and other product targets | Record product type and relevant restrictions within their platform profile; qualify used contracts rather than assuming the app host covers them. |
| Non-Apple targets | Outside this Swift skill's current scope. State the limitation; adding another ecosystem needs a separate scope decision. |

A target without native evidence may still receive source-backed guidance with that
limitation stated. Missing tools are not evidence that a documented API is unsupported.
Do not promise all possible target variants, OS versions or assistive technologies.

## Test architecture

Extend the existing infrastructure rather than replacing the validated iOS adapter.
Separate target-independent planning/result validation from platform host execution.
Add host adapters only for selected, approved workloads; never silently substitute a
nearby simulator, platform or framework to make a check pass.

Each future case/profile must identify:

- Stable semantic family, claim IDs, framework and example/test revision.
- Concrete project target or synthetic fixture target, product type, platform,
  target environment/variant, deployment target and relevant idiom.
- Actual compiler/Xcode, SDK/build, architecture, destination and runtime/build.
- Required capabilities, exact compile/unit checks and predeclared applicability.
- Source and input hashes, adapter revision, assertion scope and known limitations.

Use ADR-003's current/previous annual anchors per covered platform. Do not build the
Cartesian product of every platform, framework, runtime and input modality. A compile
record has no runtime observation; a unit record must name the runtime actually used.

| Check layer | What it can establish | What it cannot establish |
| --- | --- | --- |
| Shared policy unit test | Asserted application-owned state or callback policy | Apple framework behavior or user input delivery |
| Target compile check | Selected source compiles with the actual target settings; expected diagnostics are matched | Runtime behavior or support on all older deployments |
| Native framework unit test | Asserted public configuration, state and direct callback behavior in that host | Spoken output, rendered layout, traversal or end-to-end accessibility |
| Model evaluation | Answer quality against an independently reviewed target-specific contract | Native correctness unless that answer separately passes the relevant native checks |

Positive examples and deliberately defective variants should exercise the same
contract. Reject wrong-target APIs, missing applicable availability handling, lost
actions and unintended valid-control changes where the reviewed oracle can establish
them. A negative compile fixture passes only for its intended diagnostic. An unrelated
failure, zero discovered tests or an unbuilt conditional branch is not a pass.

Preserve `passed`, `failed`, `skipped`, `blocked` and `error`. Use skipped only for
predeclared inapplicability; missing SDKs/runtimes are blocked. Display planned but
unexecuted coverage explicitly as not run. Do not count blocked or not-run cells as
successful, or collapse them into the model's accuracy denominator.

Future schema changes must be versioned. Preserve existing manifests/results and
frozen evaluation hashes; any read adapter must retain their original scope rather
than backfilling unrecorded platform evidence. Add synthetic contract tests for target
mismatch, missing prerequisites, result binding and old-record compatibility before
qualifying a new native adapter.

## Evaluation and reporting

Create neutral developer prompts with actual code and explicit target settings where
needed. Pair a reusable semantic family with target-specific starter code, accepted
alternatives and grading criteria. A platform port is a separate case revision, not
an extra independent family for inflating sample size.

Include both defective and already-correct examples. Include wrong-platform API
recommendations, mixed-target projects and insufficient-context cases. Gold readiness
requires reviewed sources, an audited oracle and the relevant compile/unit evidence;
it does not follow from copying an iOS prompt into another platform folder.

Freeze prompts and baselines separately from candidate guidance. Keep related ports
and known incidents in the development family; hold out genuinely unseen families
before tuning. Compare baseline and candidate on identical target/condition cells.

Report by platform/framework and semantic family: source-backed correctness, critical
errors, unjustified changes, native-check status, input/output/cache tokens and latency.
Show one-line coverage rows such as **target · cases reviewed · compile/unit result ·
model score · tokens · remaining gap**. Do not publish an overall average that hides
a missing platform or regression. Measure routing overhead and wrong-profile retrieval
as well as answer quality. Current C2 injection results do not qualify autonomous routing.

## Phased implementation and acceptance

1. **Inventory and contracts.** Enumerate encountered targets and existing evidence;
   distinguish library, model-fixture and generated-answer validation. Specify the
   versioned target/profile extension and offline mismatch tests. Done when no selected
   target is inferred from a framework name and gaps are visible.
2. **Shared core plus existing UIKit evidence.** Audit shared claims and no-change
   rules against the measured failures. Preserve OS26 baselines. Done when a compact
   candidate and paired evaluation plan exist; runtime promotion remains separate.
3. **Prove portability on tvOS.** Add one bounded semantic family with real tvOS
   source, positive/negative checks and an independent developer prompt. Reuse the
   iOS family where appropriate without claiming identical API behavior. Done when
   actual target-bound compile/unit receipts and independent oracle review exist.
4. **Expand by encountered workload.** Prioritize macOS/AppKit and cross-platform
   SwiftUI, then Catalyst, visionOS, watchOS or product variants as actual demand and
   available hosts justify. Review the chosen tranche before execution. No platform
   must finish its entire catalog before another useful target can be addressed.
5. **Candidate promotion.** Run an approved paired comparison with platform-level
   regression review and the existing evaluation gates. Publish only the scope actually
   supported; retain coverage gaps and historical records. Rollback is to the frozen
   released skill, not deletion of unfavorable evidence.

This ADR writes no implementation task into an active execution queue. Ownership,
capacity and a bounded native/model run plan must be agreed when each tranche starts.
No new inference, installs, native runs or worker messages are performed by this ADR.

## Alternatives and consequences

- **Shared accessibility only:** economical, but insufficient for executable API
  advice. Adopt it as the foundation, not the complete qualification strategy.
- **Finish iOS, generalize later:** preserves short-term speed but risks an iOS-shaped
  runner and misleading cross-target claims. Keep UIKit first while making contracts
  target-aware now and proving one second-platform path early.
- **Qualify every target before usefulness:** comprehensive in theory, but delays
  improvements and creates an unbounded matrix. Reject as a release prerequisite.
- **One independent skill per platform:** duplicates principles and increases drift.
  Prefer one entry point with selectively loaded profiles and independent evidence.

Costs include platform hosts, source review, adapter qualification and separate case
oracles. Shared policy tests and metadata reduce duplication; they do not remove the
need for platform evidence. The payoff is a useful agent with explicit coverage rather
than a broad promise supported by only one platform's tests.

## Relationship to existing decisions

This proposal extends ADR-003's target accounting and rollout; it does not change its
source tiers, annual cadence, immutable evidence or compile/unit-only scope. UIKit-first
means implementation order, not permanent iOS-only architecture. Historical architecture
documents discuss broader user-facing verification; those checks are not introduced as
mandatory gates here. Unit-test limitations remain explicit rather than being solved
by silently adding UI tests or manual accessibility requirements.

On acceptance, update the development instructions and implementation plan to reflect
the selected tranches. Runtime manifests, released skill files, frozen prompts and
historical reports stay unchanged until separately reviewed, benchmark-backed promotion.

## Prepared evaluation companion

The [compact candidate offline review](../evaluation/failure-driven/compact-candidate-a/REVIEW.md)
prepares a fixed development comparison. It does not qualify additional platforms or
authorize runs. Newly published contrast, modal and edited-rotor tranches remain
separate development evidence pending independent case review.
