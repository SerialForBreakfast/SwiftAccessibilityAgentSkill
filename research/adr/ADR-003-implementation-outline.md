# ADR-003 implementation outline

Status: initial offline contracts implemented; native library pilot and skill
integration remain separate. See [infrastructure](../../code-examples/README.md).
Implements [ADR-003](ADR-003-version-anchored-unit-tested-examples.md), retaining
its existing source tiers, annual cadence and two version anchors.

## Goals and sequence

First establish the OS26 agent baseline. In parallel, resolve test architecture on
paper and inventory an approved Apple worker. Then build a small compile/unit pilot,
freeze its evidence and evaluate optional code retrieval before skill integration.
No UI tests, accessibility UI audits, screenshots or required manual device checks.
No claim that a unit test proves spoken output, focus traversal or universal usability.

Maintain current and previous major anchors at selected exact versions. Annual
refresh closes out the previous major, validates the chosen new stable and archives
older records. RC and interim fixes are opt-in. User reruns append records without
changing historical anchor evidence or requiring us to maintain every point version.

## Minimal architecture

1. **Claim catalog:** stable ID, Apple URL/section/review date, bounded documented
   claim, availability declaration, example/test IDs and observation limits.
2. **Tested source:** small examples using public APIs. Prefer direct public-object
   configuration and real callbacks over mocks that merely prove our assumptions.
   Pure policy logic is useful but must not stand in for framework integration.
3. **Compile lane:** SDK declarations, platform/target availability and diagnostics.
   Negative fixtures require the intended diagnostic, not any failed build.
4. **Unit lane:** independently asserted state/configuration/action behavior.
   Use a platform test host only where necessary; a host is not a UI-test target.
   Reuse XCTest initially where existing fixtures make that practical; framework
   choice does not justify rewriting fixtures before the pilot.
5. **Runner:** offline plan/requirements inspection, explicit execution on an
   approved actual SDK/runtime, and immutable result export. Never emulate another
   OS with a version flag. Missing runtime blocks execution rather than passing.
6. **Ledger:** hashes, source revision, command/flags, compiler/SDK/runtime builds,
   deployment target, expected/observed result and diagnostics. Passed, failed,
   skipped, blocked and harness-error are distinct. Preserve original records.
7. **On-demand index:** compact topic/platform/example lookup. Return tested source
   and a small validation summary only when requested. Retrieval does not authorize
   execution; exact MCP/CLI integration is deferred until benchmark acceptance.

## Bounded first pilot

Start with public UIKit row configuration and independently wired actions, reused
cell state and text-scaling configuration. Use the new OS26 fixtures as candidate
inputs, not established gold oracles. Add a named custom-action example after its
signature and target are reviewed. Keep SwiftUI callback logic explicitly separate
from claims about rendered controls and input delivery.

For each example: review the claim, compile the known-good source, run focused unit
assertions, then run isolated mutations against the identical assertions. A failure
means the assertion differs in that environment; investigate code, SDK, runtime and
setup before calling it an Apple API change. Do not alter assertions merely to turn
an unexpected failure green. Source discrepancies get linked records.

## Implementation tasks

- [x] Agree code-contract evaluation endpoint and resolve existing manual/UI gates.
- [x] Confirm this Mac as Apple worker; existing fixture runs used SDK27 with
  iOS/tvOS26.5. Further native library execution remains separately bounded.
- [x] Specify initial manifest/results contracts and synthetic runner tests, including path
  confinement, immutable outputs, malformed evidence and diagnostic matching.
- [x] Qualify the initial iOS type-error diagnostic mapping against actual compiler
  output; preserve the initial mismatch and version the expectation. Other compiler
  diagnostic families remain outside the qualified pilot.
- [x] Create reproducible host/package commands without UI-test targets; prove that
  a wrong platform or zero discovered tests cannot produce a successful claim.
- [x] Execute the bounded three-example pilot: eight compile/unit checks matched
  expectations; see code-examples/pilots/uikit-v1/validation/README.md.
- [ ] Independently review the new adapter, example claim bindings and assertions;
  existing OS26 fixture review does not automatically approve this pilot.
- [x] Prepare sanitized results and an index pointing to actual tested sources.
- [ ] Publish the reviewed checkpoint; no skill integration or anchor promotion yet.
- [ ] After agent baselines, evaluate optional retrieval quality and token costs.
- [ ] Add the next annual anchor only when the maintainer selects it; retain archives.

No always-on CI, simulator downloads, per-minor OS matrix or new service is necessary
for this design. Native execution scheduling and quota remain separate owner choices.
