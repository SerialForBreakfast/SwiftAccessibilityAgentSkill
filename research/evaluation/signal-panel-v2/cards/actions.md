Start with the framework that owns the interactive child. An AppKit row can expose independently actionable children. In a SwiftUI representable, remove redundant wrapper semantics without suppressing the native editable field or replacing its editing behavior.

For UIKit cells, handle configuration twice on the same instance: collection-view reconfiguration can skip prepareForReuse(). Keep one stable ordinary button target or replace its owned registration. A UIControl action and a UIAccessibilityCustomAction are separate activation paths; keeping a shortcut current should not remove the ordinary action.

For a retained action, distinguish its intended owner when installed from the current one when invoked. Reading the latest ID twice cannot detect a stale callback. Reparenting is not the same as detachment. If a check is requested, invoke the old action after reconfiguration and the installed current controls; observe the item and number of deliveries.

[Apple: reconfiguring existing cells](https://developer.apple.com/documentation/uikit/uicollectionview/reconfigureitems%28at%3A%29)
