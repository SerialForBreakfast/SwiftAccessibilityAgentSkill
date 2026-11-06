# Modal Native Evidence

## Preserved History

[Revision1](revision-1.json): eleven positive methods and four intended mutant
rejections passed. That suite did not exercise a removed view retained elsewhere.

[Revision2](revision-2.json): same source, expanded twelve-method suite. Exactly
`testRetainedButRemovedTargetPostsNil` failed after compilation succeeded. The
notification argument still contained the removed UIButton. This is an observed
implementation defect exposed by a new test, not a manufactured mutation or an
infrastructure error. Exact sources/tests/manifests are under `history/`.

[Revision3](revision-3.json): repaired current-subtree validation and a check for
previously hidden backgrounds. Thirteen positive methods and five intended negative
controls bind to the current manifest. The DetachedTarget variant reproduces the
original implementation byte-for-byte as a current regression control.

All seven revision3 checks met expectations: compile success, thirteen positive
methods passed, and all five intended negative checks failed exactly their selected
test identities. Revision2's observed failure remains preserved, not relabeled as
an expected mutation or replaced by the repaired result.

## Evidence Scope

Xcode27.0 build27A266a, Swift6.4, SDK27.0 build24A430, arm64, deployment26.0,
actual iOS26.5 build23F77 for unit runs. Compile records have no runtime. Local
work date is November5,2026; raw UTC dates are November6.

Tests capture configured metadata, direct ordinary actions, direct escape handling
and injected asynchronous completion/notification callbacks. They do not present
UI, synthesize gestures, deliver VoiceOver focus or establish rendered behavior.
The owner still supplies real dismissal integration and explicit teardown.

Original private logs and xcresult artifacts remain immutable. Public excerpts
remove private-path aliases and object addresses while retaining exact assertion
identities and record/log hashes. Independent prompt/oracle review and model runs
are separate pending gates; no runtime skill or frozen baseline is modified.

Offline verification: `node --test code-examples/tools/modal-contract.test.mjs`.
