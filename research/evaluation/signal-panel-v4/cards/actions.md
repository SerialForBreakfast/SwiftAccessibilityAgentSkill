Start with the layer that owns the control. Keep independently operable children; an AppKit row role need not replace them. Removing duplicate wrapper semantics should leave the native editor available for editing.

Reconfigure the same instance: UIKit can skip prepareForReuse(). Keep ordinary buttons connected. A retained shortcut must own its registration and remain permitted. Checking the latest ID twice or acquiring a new ticket when invoked cannot identify an obsolete registration. Moving a live control is not itself retirement.

Capture the installed action before rebinding. Invoke it afterward, then dispatch the current ordinary controls and shortcut; inspect the recipient and delivery count. Calling the handler factory again tests a different action. For closure-backed actions UIKit uses actionHandler?(action), AppKit handler?(). A press return value alone does not establish dispatch, nor dispatch attachment.

After outline reload, distinguish node identity from surviving expansion and selection; retire removed handles. For a collection, selected accessibility traits do not themselves change collection selection.

[Apple: reconfiguring cells](https://developer.apple.com/documentation/uikit/uicollectionview/reconfigureitems%28at%3A%29) | [Implementation excerpts](examples/actions.md)
