# Structure/form development observations

## What worked

The initial positive native suites passed on both selected anchors. Conventional
NSOutlineView data-source queries, expansion and selected-item restoration were
asserted without driving a window. TV tests asserted real UIView hierarchy,
accessibilityElements arrays and ordinary UIControl actions without focus-engine
simulation. Form editing entry points exercised native delegate/action wiring.
See results for final negative outcomes; no independent subject model was run.

## S01: Historical inventory checker assumed the repo stopped growing

Classification: maintainer harness scope, identified by inspection before running
the expanded full suite. The earlier media integrity test compared its nineteen
indexed questions to every platform question in the repository. Adding four cases
requires a new union check rather than changing those nineteen prompt records.

- [Exact original checker](incidents/media-integrity-original.mjs.txt)
- [Additive amendment record and original hash](inventory-amendment.json)

The earlier checker now tests its declared packages; this batch's integrity check
accounts for the union of all 23 platform cases. Neither an observed model failure
nor a native API defect is claimed. Native evidence indices and original prompt
bytes remain unchanged. The existing Gemini plan still has nine cases.

## S02: Platform facts and application identity differ

Mac outline items use globally unique IDs and retained node identity. TV shelf
items use section-qualified IDs; the same item ID in different shelves is valid.
Blindly copying one platform's uniqueness rule would reject valid input or select
the wrong item. This was a design distinction, not an observed first-run failure.
The two independent questions state their data contracts explicitly.

Generation and hierarchy guards test different risks. The retained TV button is
reattached in the generation test so the hierarchy guard cannot accidentally hide
a broken generation guard. A separate detached-current-button test isolates
ownership. This avoids the ineffective-mutant problem recorded in lifecycle work.

## Native diagnostic observations

Mac logs include AppIntents metadata-extraction and autoShortcut service connection
messages. The adapter recorded a successful build, exact non-skipped test selection
and matching runtime. These messages are preserved in raw evidence, not relabeled
as assertion failures or automatically repaired by changing test expectations.
No assertion repair was needed in the positive first attempts.

## Intentional negative controls

Each platform deliberately bypasses invalid-input rejection, error clearing and
reentrant-save protection. Mac also challenges duplicate validation, node identity,
stale child access and selection restoration. TV challenges duplicate sections,
container independence, generation and current hierarchy ownership. These are
purposeful mutants, not spontaneous model errors or an inferred model ranking.

## Limits that remain explicit

Form validation logic is injected, not a production email validator. Empty error
messages and validator side effects are outside the declared caller contract.
Examples do not provide full layout/localization integration. TV uses custom UIView
shelves, not UICollectionView reuse/data-source qualification. Stored metadata,
outline row state and invoked actions do not establish actual spoken navigation.
The hint-page URL returned404; inspected SDK declarations supply scoped evidence.

The TV test compiler also reports WeakMutability for the weak observation variable
in the owner-lifetime assertion. The weak reference test passes; the exact source
and warning remain in the native record rather than changing hashed inputs for a
nonsemantic warning. This is not an API availability/deprecation finding.
