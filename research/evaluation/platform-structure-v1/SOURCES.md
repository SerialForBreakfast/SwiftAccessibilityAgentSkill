# Source and API evidence

Reviewed November 6, 2026. The [source index](source-index.json) hashes retrieved
Apple markdown and exact installed SDK27 headers separately for Mac and TV.

| Source | Supporting section | Used for |
| --- | --- | --- |
| [NSOutlineViewDataSource](https://developer.apple.com/documentation/appkit/nsoutlineviewdatasource) | Overview and required programmatic methods | Roots/children, expandability and values per column for conventional data sources |
| Installed NSOutlineView.h | Data-source note, required methods, row/expansion and item-retention declarations | Root represented by nil; do not reload from data-source queries; query item/row identity and expansion |
| Installed NSTableView.h / NSTableColumn.h | Selection, reload and column declarations | Named columns and visible row selection, not spoken relationships |
| [AppKit accessibility help](https://developer.apple.com/documentation/appkit/nsaccessibilityprotocol/setaccessibilityhelp(_:)) | Property setter | Supplemental help text; does not document an automatic validation announcement |
| Installed NSTextField.h / NSControl.h | Editing delegate, actions, enabled state and current value | Ordinary editing/submission wiring without UI automation |
| [UIAccessibilityContainer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainer) | Providing information about accessibility elements | Explicit container elements rather than replacing independent child controls |
| Installed UIAccessibility.h / UIAccessibilityContainer.h | Hint, element and trait properties | Stored hint/heading/selected metadata and configured child order |
| Installed UITextField.h / UIControl.h / UIAction.h | Current text, editingChanged, primary actions and enabled state | Native control state/action contracts |

The attempted UIKit accessibilityHint markdown URL returned HTTP404. The installed
UIAccessibility.h declaration supplies the scoped property evidence; no unavailable
page content was inferred.

## Availability

All selected production sources compile with SDK27 for target26. Runtime receipts
are separate: Mac27 host, TV26.5 simulator. The NSOutlineView convenience child-query
API header explicitly lists macOS10.10, but the sample primarily supplies data-source
callbacks, not that convenience method. UIKit accessibilityElements has an iOS8
annotation in the inspected header; this is not invented tvOS8 availability.
Unannotated earliest introductions remain unspecified. This is a scoped declaration
audit, not a complete member-by-member historical availability matrix.

## Application policy, not an Apple promise

Global Mac tree IDs, section-qualified TV item IDs, duplicate rejection, persistence
across updates, callback generation checks, validation timing and help restoration
are the examples' application policies. APIs provide the underlying tree/control/
metadata mechanisms. Tests assert only these configurations and effects. A pure
validator returns a nonempty localized message or nil; it does not reenter UI code.

Source tiers remain unchanged. Unit results supplement documentation at the exact
recorded anchors; they do not establish rendered layout, input delivery, automatic
speech, directional focus or complete usability.
