# UIKit Coverage-Closure Campaign

Status: author-reviewed coverage ledger; native campaign executed with expected outcomes; independent
review pending. Research only. Released skill and frozen baselines remain unchanged.

## Read First

- [Results](RESULTS.md): 104 native checks, 202 distinct positive methods and 66
  intended negative rejections; zero unexpected native outcomes.
- [Coverage table](COVERAGE.md): all 209 clauses and 15 guideline rules.
- [Machine-readable ledger](clause-ledger.json) and [assertions](assertion-catalog.json):
  exact selected methods, body/file hashes, source claims and matching native evidence.
- [New questions](gap-contracts/evaluation/prompts.json) and
  [separate controller rubrics](gap-contracts/evaluation/RUBRICS.md).
- [Difficulty history](DIFFICULTIES.md) and [one review request](REVIEW-REQUEST.md).
- [Preservation checks](preservation.json): 246 offline checks passed, all 210 frozen
  files and 87 historical pins verified, and durable private archive hashes recorded.
- [Availability matrix](availability-matrix.json), [type inventory](type-declarations.json)
  and [targeted Apple source review](apple-source-review.json).

## Bounded Scope

The starting inventory is 17 pilot packages, 180 selected positive unit methods and
59 negative checks. Checkout preservation adds five methods and two negatives, with
its original oracle failure and correction preserved. This campaign adds three
behavioral families, 17 methods and five mutants. Method counts are not independent
behavior counts. Existing completed behavior is rerun, not counted as new development.

| Workstream | Existing evidence reused | New contract |
| --- | --- | --- |
| Naming, traits, native controls | Contextual names, decorative flags, control state and values | Complete supplied summary metadata is exercised in grouping |
| Containers, actions, reuse | Ordering, ordinary actions, stale callbacks, ownership | Text-only summary reuse |
| Rotors, text, Dynamic Type | Edited Unicode ranges, headings, typography, supplied checkout button | Named adjustable quantity with ordinary plus/minus paths |
| Lifecycle, preferences, presentation | Observer restart/teardown, restoration request arguments | Final status independent of optional animation |
| Media, forms | Audio/text selection, loaded-item metadata, unknown/absent/error distinctions, recovery | Audit and regression; no duplicate implementation added |

The three new families address seven source clauses. Partial dispositions retain
their broader documentation-supported components. The 31 SwiftUI interop clauses
stay deferred. Outside-unit behavior receives a rationale rather than invented unit
coverage. All 15 broad guideline rules remain partially covered; no finite fixture
proves universal meaning, perception, navigation or usability.

## Native Evidence

The base execution plan contains 98 checks over 18 packages. A separate frozen
supplement contains six checks over the new package and started only after the base
campaign completed without an infrastructure stop. Both used the existing selected
iOS26 simulator. Exact SDK/compiler/runtime versions belong to the receipts, not
an assumed version label. SDK27 compilation is not OS27 runtime promotion.

`execution.json` is produced only after all selected receipts exist and validate.
It reports unique selected positive methods, positive unit checks, compile checks,
negative checks and repeated method executions separately. Compile and negative
categories can overlap; do not add them to infer a total. Each negative must fail
for its specified assertion/diagnostic reason, not merely return a nonzero exit.

The completed campaign records 355 method executions including negative reruns;
these are not 355 independent behaviors. The seven identified clause gaps are now
validated within unit scope. Final clause dispositions: 22 covered, 123 partial,
33 documentation-supported/outside unit scope, and 31 SwiftUI deferred. All 202
selected positive methods have matching native evidence.

First-attempt sources, manifests, diagnostics and receipts remain immutable in the
private execution roots. Public rows retain hashes and relative artifact paths.
The checkout revision-1 oracle record remains in its original package. The eight
reviewed model answers are not edited or rerun by this campaign.

## Execution and Resume

Run from the repository root, using a new private absolute directory and an already
installed iOS26 simulator UUID. No installations or model calls are involved.

```sh
node code-examples/tools/campaign.mjs freeze "$BASE" "$IOS26_UUID"
node code-examples/tools/campaign.mjs run "$BASE" "$IOS26_UUID"
node research/evaluation/failure-driven/uikit-closure-v1/prepare-supplement.mjs "$BASE" "$SUPPLEMENT"
node code-examples/tools/campaign.mjs run "$SUPPLEMENT" "$IOS26_UUID"
node research/evaluation/failure-driven/uikit-closure-v1/export-results.mjs "$BASE" "$SUPPLEMENT"
node research/evaluation/failure-driven/uikit-closure-v1/build-ledger.mjs
node research/evaluation/failure-driven/uikit-closure-v1/render-coverage.mjs
```

Resume with the same `run` command. Inputs, snapshots, adapters and environment must
match. Completed receipts are validated and reused, never replaced. An incomplete
attempt directory is retained and stops execution for adjudication. Assertion
failures allow independent checks to continue; infrastructure/unassessed failures
stop native execution. Existing 600-second native and 900-second wrapper timeouts
remain in force. A live lock blocks another runner.

Repair policy: preserve the first attempt, classify the cause, create a new source/
manifest revision and new output directory, and link the parent attempt. At most two
documented repair attempts per contract; unresolved cases remain visible. The runner
does not automatically repair source, reinterpret failures or modify old receipts.
Do not rewrite this first campaign export to incorporate a later repair.

## API Evidence

The combined member matrix inventories 202 external member/override references in
19 production packages. It retains exact header locations/context when the compiler
provides them; 61 entries have directly extracted iOS availability annotations.
The remaining 141 introduction dates stay explicitly unresolved. Absence of an
extracted deprecation annotation is not proof that an API is never deprecated.

The complementary lexical inventory records 43 Apple-prefixed identifiers, with
31 type/protocol declaration locations. Functions, constants, namespace/importer
aliases and other unresolved identifiers remain explicit. These inventories are
bounded by their extraction methods, not a claim to exhaustive SDK coverage.
Enclosing declaration context is retained separately; adjacent annotations are not
silently assigned to members. Swift overlay interpretation remains a review item.

Apple documentation supplies platform guidance. Fixture bounds, callback timing,
wording and transition policy are application requirements. Native tests support
only their asserted behavior on the recorded anchor; no manual or UI gate is added.

## Acceptance Status

- All bounded clauses and rules have explicit author dispositions.
- New families have separate natural prompts, atomic rubrics and accepted alternatives.
- Native validation, independent review and baseline eligibility are distinct statuses.
- Native validation is complete; independent review and baseline eligibility remain pending.
- All new cases are development cases; no fresh holdouts are claimed.
- Skill promotion requires separately approved, benchmark-backed changes.
- Git publication and live model batches remain separately authorized.
