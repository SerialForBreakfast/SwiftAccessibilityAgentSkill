# Reuse and configuration validation

Revision3 completed all five checks against their declared expectations:

| Check | Result |
| --- | --- |
| Library type-check | Passed |
| Positive unit suite | 11 passed, 0 failed, 0 skipped |
| Retained selected state | Intended assertion failure |
| Retained obsolete action identity | Intended assertion failure |
| Incorrect notification kind | Intended assertion failure |

[Revision3](revision-3.json) contains verified manifest/artifact hashes, environment,
selected tests and sanitized assertion excerpts. [Revision1](revision-1.json) and
[revision2](revision-2.json) preserve their10-pass/1-fail observations and mark their
unattempted negatives explicitly. All executed records and artifacts were copied
to separate private immutable ledgers.

The [history](../history/README.md) explains both typography setup failures. The
final helper uses the receiving label's traits. Tests assign a public override and
synchronously propagate it before inspecting category, font metrics and style.
All nine style/category combinations remain asserted; failures were not converted
to accepted defaults. No device preference was changed.

Environment: Xcode27.0 build27A266a, Swift6.4, SDK27.0 build24A430,
deployment26.0, arm64, iOS26.5 build23F77. The dedicated simulator is shut down.
Compilation alone carries no runtime claim.

The library now contains89 distinct positive methods across seven packages.
All161 offline harness tests pass; all210 frozen baseline files remain intact.
These counts do not establish complete UIKit coverage. Remaining work is tracked
in the [coverage ledger](../../../UIKIT-COVERAGE.md).

No UI automation, system accessibility notifications, model calls, downloads or
paid runs occurred. Frozen skill/runtime instructions were not edited. Independent
review and annual anchor promotion remain separate.
