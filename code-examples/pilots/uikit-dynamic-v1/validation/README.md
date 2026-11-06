# Dynamic UIKit validation

Revision2 completed six native checks:

| Check | Result |
| --- | --- |
| Type-check | Passed |
| Positive unit suite | 15 passed,0 failed,0 skipped |
| Stale retained action | Intended assertion failure |
| Duplicate callback | Intended assertion failure |
| Missing ordinary elements | Intended assertion failure |
| Retained removed element | Intended assertion failure |

[Revision2 evidence](revision-2.json) records exact manifest/log/result hashes,
toolchain and runtime details, test selections and sanitized assertion excerpts.
Object memory addresses are removed from excerpts; original logs remain private.
All hashed native artifacts were checked before export. Ledger copies preserve
record artifacts separately from the original raw xcresult bundles.

[Revision1 evidence](revision-1.json) preserves the first attempt: type-check
passed;14 unit tests passed and the removed-element lifetime test failed. The
runner stopped, leaving all four mutations unattempted. Source and tests from
that attempt are archived under `../history/revision-1/`.

Revision2 adds an autorelease-pool boundary to the lifetime test. Example and
mutation source bytes are unchanged. The positive ownership check then passes,
while the retained-index mutation fails under the identical revised assertion.
This supports distinguishing transient ownership from the deliberate persistent
reference in this example; it does not establish an Apple framework defect or
identify an OS behavior change.

Environment: Xcode27.0 build27A266a, Swift6.4, SDK27.0 build24A430,
deployment26.0, arm64, actual iOS26.5 runtime build23F77. The compile lane does
not claim runtime execution. No UI tests, model calls or downloads occurred.
The dedicated simulator is shut down and no native job remains active.

The three library batches now contain41 distinct positive UIKit test methods.
This is a behavior inventory, not a completeness percentage. All160 offline tests
passed and210 frozen baseline files verified unchanged. New source bindings and
example policies await independent review; no annual anchor or skill integration
is promoted by this report.
