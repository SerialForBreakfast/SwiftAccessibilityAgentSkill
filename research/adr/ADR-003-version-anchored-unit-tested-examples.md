# ADR-003: Version-Anchored, Unit-Tested Examples

- Status: Proposed for review; design direction agreed, implementation deferred
- Date: 2026-11-05
- Deciders: Project maintainer
- Scope: Research architecture; no runtime skill or evaluation-input changes
- Related: [ADR-001](../../docs/core/adr/ADR-001-robust-evaluation-methodology.md), [ADR-002](../../docs/core/adr/ADR-002-context-budget-and-routing.md), [frontier evaluation strategy](../../evals/TARGET-EVALUATION.md)

## Context

The skill needs precise, source-backed Apple accessibility guidance without imposing
continuous maintenance across every OS version. Documentation, SDK declarations and
observed code behavior can differ. Small SDK or runtime changes may matter even when
release notes omit them. Developers should be able to retrieve a focused example and
rerun its checks in their own environment.

The maintainer commits to one annual refresh cycle. Intermediate releases, beta/RC
experiments and exceptional corrections are opt-in. The intended product remains a
skill for capable frontier Swift coding agents, not a library optimized to compensate
for weak local models.

## Decision

Create an on-demand library of source-backed examples with compile checks and unit
tests. Attach version-specific validation records to documentation claims. Keep the
existing evidence tiers unchanged: there is no Tier 0.

Maintain two rolling major-version anchors: current and previous. Each anchor identifies
one exact tested configuration per covered platform, not a sweep of minor releases.
Older records remain archived. This is a validation policy, not a promise of continuous
support for every version between anchors.

**No UI testing is part of this library.** No UI automation, VoiceOver navigation
automation, screenshot assertions, accessibility UI audits or end-to-end assistive-
technology tests are required or implemented by this decision. Historical ADRs remain
unchanged; their optional UI/runtime lanes are not dependencies of this example library.

## Evidence Relationship

Apple documentation and Apple-authored sample code remain Tier-1 sources within their
stated scope. Project-authored examples and test results are supporting validation
evidence linked to those sources, not a new source tier.

A result records an observation about a particular assertion and configuration:

- Documentation describes the supported contract or version-specific behavior.
- Compile checks establish which declarations and diagnostics the selected toolchain
  produces for a target.
- Unit tests establish the directly asserted behavior of the example in that environment.
- Source/test discrepancies remain explicit records rather than silently replacing
  either source or result.

An untested documented claim remains documented, not automatically speculative. Beta
claims retain their provisional release status. A failed rerun means the validated
expectation did not hold in that environment; it does not alone establish an API change.
Possible causes include example defects, SDK/runtime differences, compiler settings,
configuration and test infrastructure.

## Annual Cadence

For a transition from major version 26 to 27:

1. Close out 26 by validating against the latest available 26.x release selected by
   the maintainer. Record exact SDK, compiler, target and runtime; freeze that snapshot.
2. Collect 27 announcements, documentation and WWDC material separately. Optional
   RC checks may prepare examples and expectations; they do not replace stable anchors.
3. Adopt 27 after the maintainer considers it sufficiently settled. This may be a
   point release, but there is no requirement that every platform ship or use 27.1.
4. Publish 27 as current and the frozen 26 configuration as previous. Archive the
   older major's examples and records without rewriting them.
5. Leave later 26.x and 27.x patches outside the automatic maintenance commitment.
   The maintainer may explicitly opt into an exceptional update with new records.

Platform anchors may use different point versions and toolchains. If a platform cannot
be exercised during the cycle, preserve its last observation and show the validation
gap. Do not invent a passing anchor or silently expand the required matrix.

## Example and Test Design

Each example covers one focused capability or documented claim and includes:

- A stable example ID, platform/framework tags and linked Apple source/claim IDs.
- Minimal readable source, intended use, limitations and required availability guards.
- Focused compile checks and unit tests with explicit expectations.
- A short validated-on note pointing to exact immutable result records.
- Instructions to list or run that example alone using supported command-line tooling.

Examples may instantiate framework objects in a unit-test host to inspect public
configuration or invoke handlers directly. They must not navigate an application,
drive assistive technologies or rely on screenshots. Respect framework threading and
host requirements. Unit tests may check, for example, a configured accessible label,
the names of custom actions, a handler's state transition or an older-OS fallback.
These checks do not establish the full user-facing accessibility experience.

Use real framework declarations for checks about framework behavior. Test doubles may
isolate application-owned dependencies, but cannot prove that Apple's implementation
behaves like the double. Avoid network, account or timing dependencies where possible.
Record required settings rather than claiming universal determinism.

### Compile and Negative Checks

Compile checks are separate from executable unit tests. Capture availability and
deprecation diagnostics, compiler flags and target details. Successful compilation
does not mean an API is not deprecated. Missing SDKs are blocked checks, not evidence
that a symbol was removed.

Use isolated negative fixtures where useful. A compile-failure fixture must fail for
the intended diagnostic; an unrelated syntax error is not success. A behavioral
counterexample must be caught by the specified assertion. Keep these fixtures out of
normal passing example targets and clearly label their purpose.

Commented-out incorrect code may explain a pitfall, but is not executable evidence.
Prefer linking the validated negative fixture rather than maintaining duplicate snippets.

### Version Selection

Select an actual installed SDK, destination/runtime and deployment target. No flag
pretends that the process is running a different OS. Availability guards select real
supported paths; test a fallback explicitly when one is offered. Do not skip a
capability merely because its observed result differs from the expected result.

The maintained matrix covers the chosen anchors only. Developers may run identical
checks on their own intermediate versions; the project need not locate the earliest
change or maintain a historical binary-search service.

## Proposed Repository Structure

The following is a design, not an existing implementation:

```text
code-examples/
  index.json
  examples/<example-id>/
    README.md
    Sources/
    Tests/
    NegativeFixtures/       # when justified
  validation/
    anchors.json
    runs/<run-id>/
      manifest.json
      results.json
      diagnostics/
  archives/<anchor-id>/
```

Keep source and result revisions immutable once published, identified by hashes and
Git revisions. Archives may reference immutable source snapshots rather than copy
every file. A changed assertion or example gets a new revision; it is not a rerun of
the same test. Human-readable snippets should come from the tested source to prevent
documentation/code drift.

Package/project layout and test framework remain implementation choices. Pure Swift
fixtures may use Swift package tooling; platform frameworks may require an Xcode test
host and suitable runtime. The command-line interface must expose actual requirements
and selected test IDs. No installs, simulator downloads or test execution are implied
by requesting an example.

## Validation Ledger

Record at least:

| Field | Purpose |
| --- | --- |
| Example/test ID and revision; source hash | Identify the exact artifact and assertion |
| Source URL, locator and documentation review date | Trace the supported claim |
| Anchor ID and run timestamp | Distinguish maintained anchors from personal reruns |
| Xcode/compiler and SDK versions/builds | Identify compilation environment |
| Platform, architecture and deployment target | Describe the built target |
| Actual runtime version/build and destination type | Describe execution, or mark compile-only |
| Command, flags and relevant prerequisites | Make the check reproducible without exposing secrets |
| Expected outcome, actual outcome and diagnostics | Explain what was checked and observed |
| Provenance and limitations | Distinguish maintainer validation from user-submitted runs |

Outcomes:

- **Passed:** the named assertion held, or a negative fixture produced its expected failure.
- **Failed:** the assertion did not hold; preserve the result for investigation.
- **Skipped:** an explicitly declared capability branch does not apply here.
- **Blocked:** missing tooling, runtime or prerequisites prevented the check.
- **Error:** the harness failed; no capability conclusion follows.

Keep compile and unit-test outcomes separate. Unavailable telemetry is marked
unavailable, not inferred. A successful run does not automatically refresh the review
date of its Apple source. User reruns append evidence and never overwrite the anchor.

## On-Demand Retrieval

Normal skill use should not load example source, tests, negative fixtures or run logs.
After integration is approved, a compact index can identify relevant examples by
platform, topic and task. Retrieve code only when example code or verification is
requested, using the smallest applicable source and validation summary.

A future CLI option or MCP tool can expose this selection. Exact names and transport
are deferred; this ADR does not claim either interface exists. Retrieval and execution
are separate operations. Retrieved code is not authorization to run it.

Evidence disclosure should distinguish documentation consulted, example retrieved and
test actually executed. A historical passing result must never be narrated as a test
the agent just ran.

## Evaluation and Rollout

1. Keep this decision and current OS research outside runtime references.
2. Establish the agreed reproducible agent baselines before skill integration.
3. Build a bounded pilot: independent row actions, a named custom action and text-size
   configuration/layout-policy logic. Choose only assertions observable through compile
   checks or unit tests; no visual-reflow or focus-navigation claim follows from them.
4. Freeze example revisions and anchor records. Optional TDD starts with source-backed
   expectations; record failures honestly instead of forcing an artificial red phase.
5. Evaluate the optional retrieval path against the baseline, measuring frontier-agent
   answer quality, source honesty and context cost. Keep example answers separate from
   heldout evaluation keys; record example-library hashes in any evaluated candidate.
6. Promote only after evaluation and maintainer review. Enable annual refresh, not
   automatic minor-version updates or background campaigns.

## Consequences and Alternatives

Benefits: useful runnable examples, explicit version evidence, low-context retrieval,
repeatable developer checks, preserved history and a bounded maintenance commitment.

Costs: test-host/toolchain setup, maintaining assertions and source links, limited
platform capacity, and the risk that users overgeneralize a small passing test.
Explicit scope, frozen records and small examples mitigate these costs without
pretending to eliminate them.

Alternatives considered:

- Playgrounds alone: useful exploration, but weaker repeatable assertions; not the
  primary artifact.
- Untested snippets or commented-out failures alone: easy to publish, prone to drift.
- UI/accessibility automation: outside the maintainer-approved scope.
- Every minor version or a full SDK/runtime cross-product: exceeds maintenance capacity.
- Tier 0: rejected; tests support source claims without changing the evidence hierarchy.
- Eagerly loading examples: wastes context; on-demand retrieval is preferred.

## Acceptance Criteria for Future Implementation

- Examples link claims and Apple sources and expose a focused rerunnable command.
- Only compile checks and unit tests are implemented; no UI-test dependency exists.
- Current and previous anchors record exact tested environments; older evidence remains accessible.
- Failure, skip, block and harness error cannot be reported as a passing validation.
- Negative cases identify their intended failure and remain separate from ordinary examples.
- Normal skill requests load no example payload by default.
- Runtime integration is benchmarked separately and does not mutate frozen baselines.
- Annual maintenance is the default; interim work requires maintainer opt-in.

## Implementation Status

ADR draft only. No example library, runner, CLI flag or MCP tool is created here.
No tests or model evaluations have been executed as evidence for proposed examples.
No skill files, source tiers, benchmark fixtures or historical validation records change.
