Keep separately usable native children. Remove redundant wrapper semantics without hiding a live editor's subtree. An AppKit row role can coexist with independently actionable children.

Reconfigure the same instance: UIKit reconfiguration can skip prepareForReuse(). Keep ordinary registrations current without removing working buttons. A retained shortcut must still own its registration and be permitted now; checking the latest ID twice or minting a ticket at invocation accepts stale callbacks. Reparenting alone is not retirement.

Retain the installed shortcut before rebinding A to B. Exercise both ordinary buttons and current and retired shortcuts; check recipient and delivery count. For closure-backed actions use UIKit actionHandler?(action) or AppKit handler?(). Direct dispatch alone does not establish attachment.

[Apple: reconfiguring cells](https://developer.apple.com/documentation/uikit/uicollectionview/reconfigureitems%28at%3A%29) · [Implementation excerpts](examples/actions.md)

After reloading a native outline, stable node identity alone does not preserve visible selection or expansion. Where requested, restore surviving IDs and reject retired handles. In a collection, updating an accessibility trait is distinct from changing the collection's own selection.
