# UIKit Availability Audit: Compile Sweep

UPAIR-07 is in progress. This additive audit preserves historical pilot manifests
and runtime skill inputs. It inventories all sixteen current pilot Sources sets,
then invokes each existing successful compile check at its declared deployment
target26.0. Tests, mutation sources and historical revisions are not the scope of
this sweep. Existing native test evidence remains separately versioned.

[Inventory](inventory.json) pins the manifests and exact source bytes. The only
conditional lines found in these sources are three `#if os(iOS)` wrappers in the
original pilot. No `#available` or `@available` runtime-version branches were found;
there is no reason to invent a fallback solely to add a test. The scan is textual,
not a general Swift parser or proof of all transitive dependencies.

[Compile report](compile-results.json) records actual environments and diagnostics.
A successful type check validates that selected source against the SDK's compiler
availability rules at the declared deployment target. It does not execute code,
qualify other OS targets, prove behavior on26.0, or establish all API contracts.
Warnings are retained rather than silently equated with failure or ignored.

## Remaining Declaration Audit

- Enumerate each selected public API/member and its defining declaration.
- Record applicable platform availability, deprecation and any conditional branch.
- Connect diagnostics to source decisions; preserve historical source when proposing repairs.
- Confirm compiled source coverage and separately account for excluded test/helper APIs.
- Link the final declaration matrix to the source-to-test inventory audit.

The complete declaration audit is still pending; green compilation does not close
UPAIR-07. A [natural developer question](evaluation/prompt.json) and
[independent grading criteria](evaluation/controller.md) are draft development
material. No model run, gold promotion or skill change is authorized by this audit.
