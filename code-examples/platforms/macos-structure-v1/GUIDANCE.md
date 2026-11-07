# AppKit structure and validation companion

Candidate repository guidance, not an installed skill update. The manifest and
run receipts separate deployment target, SDK and actual host runtime.

Form examples retain typed input and the ordinary Save button. A pure injected
validator supplies localized nonempty errors or nil. Show errors visibly; transient
accessibility help supplements them and clears on native editing notification.
Restore the original optional help, preserve control identities, and guard against
disabled or reentrant submission. These assertions do not prove spoken errors.

For conventional NSOutlineView data sources, implement child count, child identity,
expandability and per-column values. Use stable item objects where state must
survive updates; validate IDs before mutating a tree. Restore expanded items and
visible selection by identity, not stale row indices. Do not reload from data-source
query methods. Named columns and query results do not prove spoken relationships.

Load DesktopForm or DesktopOutline source only for that task; tests on demand.
These examples do not configure a complete production window or its visual layout.

Sources: [outline data source](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource),
[accessibility help](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/setaccessibilityhelp(_:)).
