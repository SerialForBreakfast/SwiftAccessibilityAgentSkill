# Coverage delta and next queue

This is an additive delta to the [first platform inventory](../platform-expansion-v1/COVERAGE.md).
It does not rewrite historical dispositions or claim guideline-wide completion.

| Existing guideline | Newly asserted subset | Remaining work |
| --- | --- | --- |
| macOS m-002 keyboard focus | Owned key-view cycle, input uniqueness, disabled/hidden exclusion, removed/incoming link cleanup, explicit stop | Modal restoration requests; actual keyboard movement stays outside unit scope |
| macOS m-006 table/outline/list | Row count/value, selection by stable ID across reorder/rename/removal, duplicate rejection, external table selection | Outline relationships, columns/headers and more complex table semantics |
| tvOS t-004 grouping/collections | Rendered button ownership and removal; selection metadata preservation | Broader collection grouping and container semantics |
| tvOS t-006 search/filter | Case-insensitive filtered membership, stable selection, empty results, duplicates, stale/disabled ordinary actions | Search controller lifecycle and focus restoration requests |
| tvOS t-008 motion | Final visible/accessibility content before optional animation; injected preference changes; repeated-message suppression | Preference observer ownership and other final-state transitions |

These are partial, bounded contracts. macOS m-007 modal restoration, m-009 preference
lifecycle, tvOS t-007 media and t-009 contrast remain queued. tvOS27 larger text is
not added to the26 runtime lane. SwiftUI interop/companion expansion remains deferred.

Next coordinated batch: platform-specific modal restoration requests and preference
observer lifecycle, followed by platform-qualified media selection/metadata. Retain
first failures, use unit-only observable state/request seams and pair each family
with a separate subject question and accepted-alternative rubric.
