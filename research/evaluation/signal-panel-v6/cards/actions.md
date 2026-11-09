Start with the layer that owns the control. Keep independently operable children; an AppKit row role need not replace them. Removing duplicate wrapper semantics should leave the native editor available for editing.

Reconfigure the same instance: UIKit can skip prepareForReuse(). Replace owned names, values and callbacks on each configure; do not add another target or handler to a control that already has one, or an ordinary press fires twice. Keep ordinary buttons connected. A retained shortcut must own its registration and remain permitted; a disabled action rejects dispatch. Checking the latest ID, or taking a new ticket when invoked, cannot identify an obsolete registration.

Capture the installed action before rebinding. Invoke it afterward, then dispatch the current ordinary controls and shortcut; inspect the recipient and delivery count. Calling the handler factory again tests a different action. For closure-backed actions UIKit uses actionHandler?(action), AppKit handler?(). A press return value alone does not establish dispatch, nor dispatch attachment.

After outline reload, keep node identity stable across rename and reorder, restore selection by ID rather than row number, keep surviving expansion, and clear selection when the node is no longer visible. A removed node's handle must stop serving data. Keep model state such as Saved distinct from a collection's transient selection. Changing native selection must not rewrite independent saved wording.

[Apple: reconfiguring cells](https://developer.apple.com/documentation/uikit/uicollectionview/reconfigureitems%28at%3A%29) | [Implementation excerpts](examples/actions.md)
