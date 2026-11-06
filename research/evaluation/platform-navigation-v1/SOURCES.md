# Source-backed contracts

Reviewed November 6, 2026. Apple documentation markdown and SDK header fingerprints
are recorded in [source-index.json](source-index.json). Source tiers are unchanged.

| Apple source | Inspected contract | Application policy exercised |
| --- | --- | --- |
| [NSTableView.selectRowIndexes](https://developer.apple.com/documentation/appkit/nstableview/selectrowindexes(_:byextendingselection:)), Parameters / Discussion | Sets indexed selection and optionally extends it; installed NSTableView.h also documents reload/data source and empty-selection configuration | Reconcile identity across reorder/rename, reject duplicates atomically, clear missing IDs |
| [NSView.nextKeyView](https://developer.apple.com/documentation/appkit/nsview/nextkeyview), Discussion | Assignable next key-view reference, nil when absent; this is not a guarantee of first-responder delivery | Own a filtered cycle, clear excluded and removed links, explicit stop |
| [UIControl.sendActions](https://developer.apple.com/documentation/uikit/uicontrol/sendactions(for:)), Discussion | Dispatch registered actions for specified control events | Ordinary primary actions select by ID; stale/disabled callbacks do not change new results |
| [UIAccessibility.isReduceMotionEnabled](https://developer.apple.com/documentation/uikit/uiaccessibility/isreducemotionenabled) | Reads whether Reduce Motion is enabled | Commit final text independently of animation, inject current settings, suppress unchanged messages |

SDK declarations inspected: NSTableView.h (selection/data source), NSView.h
(nextKeyView), UIControl.h (primary-action registration/dispatch), UIAccessibility.h
(reduce motion). Unannotated platform introduction dates remain unresolved rather
than inferred from iOS annotations. This is scoped availability evidence; a complete
member-by-member declaration audit remains a promotion task.

Both packages target26.0 using installed SDK27. Mac execution uses the real27 host;
tvOS uses the existing26.5 simulator. None of these observations establish every
intermediate version, real assistive-tool interaction or Mac26 runtime behavior.
