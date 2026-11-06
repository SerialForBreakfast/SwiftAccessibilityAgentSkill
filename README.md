# Swift Accessibility Agent

**Evidence-backed accessibility guidance for Swift developers and AI coding agents.**

This project turns documented Apple-platform behavior, executable examples, and
observed agent mistakes into focused guidance that can be evaluated. The objective
is practical: help agents preserve working accessibility, find real defects, and
make changes that improve the experience of people using Apple-platform software.

**Released skill: `0.2.2`** · [Install or upgrade](INSTALLATION.md) ·
[Latest UIKit evidence](research/evaluation/failure-driven/uikit-closure-v1/RESULTS.md) ·
[Evaluation dashboard](evals/reports/README.md)

## What Makes This Different

Apple documentation is the foundation, not the finished product. We investigate
where coding agents struggle to apply it: overwriting a working control, hiding an
ordinary action behind an accessibility shortcut, retaining stale callbacks, mixing
framework defaults, or confusing metadata with behavior that was never observed.

Each proposed improvement needs a traceable chain:

```text
Documented claim -> executable contract -> observed gap -> reviewed question/rubric
                -> frozen baseline -> candidate guidance -> paired evaluation
```

A passing example establishes a bounded behavior. A better model answer requires
its own evidence. Keeping those conclusions separate is central to this project.

## Capabilities at a Glance

Status reflects the November 6, 2026 checkpoint. **Available guidance, executed
tests, independent review and measured model improvement are separate milestones.**

| Area | Available now | Evidence and next gate |
| --- | --- | --- |
| Apple-platform skill | Source-backed review, implementation and triage guidance for UIKit, SwiftUI, AppKit/macOS, tvOS and visionOS | Released `0.2.2`; new evidence has not been promoted into the frozen skill |
| UIKit companion | Naming, traits, native controls, grouping, actions, reuse, rotors, text scaling, preferences, modal restoration requests, media and form state | 19 packages; 202 distinct positive unit methods passed on the recorded iOS26 anchor; independent campaign review pending |
| Coverage accounting | All 15 UIKit guidelines and 209 inventoried clauses have dispositions | 22 covered, 123 partial, 33 documentation-supported/outside unit scope, 31 SwiftUI-deferred clauses; [inspect the ledger](research/evaluation/failure-driven/uikit-closure-v1/COVERAGE.md) |
| Regression sensitivity | Deliberately broken examples test whether assertions detect the intended defect | 66 negative controls rejected for their specified reasons; not 66 observed model mistakes |
| API/version evidence | SDK declaration context, source hashes, deployment targets and runtime receipts | 202 external member references inventoried; unresolved introduction dates remain explicit |
| Agent evaluation | Frozen inputs, framework-separated questions, controller rubrics, protocol and quality scoring | Existing frontier/local diagnostics inform development; new companion cases await independent review and baseline qualification |
| Progressive disclosure | Focused guidance today; source/test/evidence packages available on demand in this repository | Companion retrieval remains offline/repository-based, not yet integrated into released skill routing or an MCP endpoint |
| Next platform work | Existing SwiftUI and other-platform guidance remains available | New SwiftUI unit-library expansion is deferred; UIKit is the active validation lane |

The [completed campaign](research/evaluation/failure-driven/uikit-closure-v1/RESULTS.md)
ran **104 native checks** with expected outcomes and **246 offline checks** passed.
Compile checks and negative controls overlap; method counts are not independent
behavior counts. This is coverage accounting, not a claim of universal accessibility.

## How We Find and Close Gaps

1. **Start with a claim.** Link Apple documentation or sample code and the relevant SDK declarations. Separate platform behavior from application policy, such as quantity bounds or callback timing.
2. **Make it testable.** Write a focused example and compile/unit assertions. Record exactly what they establish and what remains documentation-supported.
3. **Challenge the assertion.** Introduce a targeted defect where useful. A negative control succeeds only when the intended assertion or diagnostic rejects it.
4. **Preserve difficulties.** Retain first source, diagnostics, environment and repair history. Classify implementation defects, faulty test expectations, harness errors and coverage gaps separately.
5. **Ask a realistic developer question.** Pair the contract with a natural prompt and a separate rubric that accepts valid alternative implementations. Keep solutions, expected routes and incident conclusions out of subject inputs.
6. **Measure the proposed fix.** Compare frozen skill conditions on the same cases. Promote guidance only after review and benchmark-backed acceptance.

For example, checkout preservation tests protect an existing button's identity,
typography and action rather than assuming it needs replacement. Quantity examples
keep ordinary plus/minus controls alongside accessibility adjustment. Motion examples
update final status independently of optional animation. These are concrete contracts,
not instructions to add more accessibility properties indiscriminately.

See the [failure-driven methodology](research/evaluation/failure-driven/PRD.md),
[preserved difficulties](research/evaluation/failure-driven/uikit-closure-v1/DIFFICULTIES.md)
and [independent review packet](research/evaluation/failure-driven/uikit-closure-v1/REVIEW-REQUEST.md).

## Unit-Test Companion: Code When You Need It

The companion provides focused Swift examples, their tests, source claims and
version-specific results as one inspectable package. Developers can read the code,
adapt it, or rerun a selected contract against an installed SDK/runtime.

| Retrieve | Purpose |
| --- | --- |
| Guideline | Understand the relevant accessibility principle without loading the full corpus |
| Example source | See a concrete implementation for the task |
| Manifest and tests | Inspect the precise contract, input hashes and intended negative controls |
| Validation record | See which toolchain, deployment target and runtime actually produced the result |
| Difficulty history | Investigate a discrepancy without losing the first failure |

This is progressive disclosure: small, relevant guidance first; executable detail
when requested. The incident archive and entire example library do not belong in
every model prompt. **The companion is available in the repository; connecting it
to installed skill routing is a separately gated update.**

The latest UIKit campaign used **SDK 27.0, deployment target 26.0, and iOS 26.5
(23F77)**. Compilation and runtime evidence are recorded separately. SDK27 use does
not mean an OS27 runtime baseline has been established.

The maintenance design uses annual current/previous major-version anchors, exact
tested configurations, archived history and opt-in interim updates. It does not
promise every minor release. A different rerun result identifies a discrepancy to
investigate, not automatic proof that Apple changed an API.

The companion uses **compile checks and unit tests only**, with no UI-test or mandatory
manual-verification gate. Its results describe directly asserted configuration,
state and callbacks, not delivered VoiceOver navigation or universal user usability.

[Companion tooling](code-examples/README.md) ·
[Version-anchor design](research/adr/ADR-003-version-anchored-unit-tested-examples.md) ·
[Campaign reproduction instructions](research/evaluation/failure-driven/uikit-closure-v1/README.md#execution-and-resume)

## Evaluating Agent Improvement

The evaluation harness uses promptfoo and repository tooling to separate instruction
effects, reference usefulness and actual retrieval behavior:

| Condition | What it measures |
| --- | --- |
| C0: generic Swift assistant | Unaided answer quality |
| C1: skill instructions, references unavailable | Instruction effects and honest handling of missing evidence |
| C2: instructions plus selected references | Guidance usefulness under controlled reference injection |
| C3: instrumented reference lookup | Actual selection, loading and installed-workflow behavior |

These are evaluation conditions, not a claim that every model has completed every
lane. Correctness and task success are scored separately from identity, routing and
disclosure. C0 is not penalized for lacking skill branding. Naming a reference is
not proof that it was read; retrieval claims require traces.

We track unsupported claims, API-availability errors, preservation of existing
behavior, input/output tokens, reference bytes, tool calls, latency and available
cost data. Paired comparisons use the same scenarios and report uncertainty. Known
incidents stay development cases rather than becoming artificial fresh holdouts.

**Frontier Swift coding agents are the primary target.** Small local models provide
diagnostic data, not the optimization target. Existing model pilots are useful
observations; the new UIKit campaign is not itself a measured improvement in model
performance. Subject runs require explicit scope/quota approval and zero incremental
spend under the current project policy.

[Evaluation guide](evals/README.md) · [Framework-separated prompts](evals/FRAMEWORK-INDEX.md) ·
[Gold prompts](GoldPrompts.md) · [Frontier target strategy](evals/TARGET-EVALUATION.md)

## Using the Skill

After [installation](INSTALLATION.md), ask a normal development question:

> Review this UITableView cell's accessibility. Preserve its existing buttons and actions.

> Our custom quantity control needs to work with ordinary buttons and accessibility adjustment.

> After editing this UITextView, jumping between highlighted passages lands in the wrong place.

The released [skill contract](SKILL.md) selects relevant guidance rather than loading
the whole repository. It requests a first-response identity, concise `ROUTING:` for
guidance actually consulted, and source/assumption disclosure. Detailed research and
the companion remain readable references for humans as well as agents.

The released contract still contains earlier verification-planning language. The
unit-only companion and promotion process described here are the current development
methodology; updating the installed contract awaits benchmark-backed promotion.

## Evidence and Project Map

Apple documentation, declarations and Apple-authored examples provide Tier-1 platform
evidence. Tier-2 implementation commentary and Tier-3 discovery/user-experience
research help identify practical concerns. Project-authored test results supplement
those sources with version-scoped observations; they do not create a new source tier.

| Location | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) and [references/](references/) | Released instructions and progressively loaded guidance |
| [INSTALLATION.md](INSTALLATION.md) | Prerequisites, project-local installation, upgrades and Xcode compatibility |
| [code-examples/](code-examples/) | On-demand example infrastructure and existing UIKit pilots |
| [UIKit campaign](research/evaluation/failure-driven/uikit-closure-v1/README.md) | Current coverage ledger, new contracts, receipts and review status |
| [evals/](evals/) | Frozen inputs, runners, grading and model comparison reports |
| [Research](research/) | Source audits, design decisions and unpromoted investigations |
| [Source registry](references/core/sources/registry.md) | Source tiers and provenance |
| [Contributor instructions](AGENTS.md) | Evidence preservation, test-to-prompt workflow and safety boundaries |

## License

MIT.
