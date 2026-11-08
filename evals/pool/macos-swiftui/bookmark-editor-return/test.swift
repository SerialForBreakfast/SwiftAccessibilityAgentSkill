let model = BookmarksModel(bookmarks: [
    Bookmark(id: "a", title: "Apple", url: "https://apple.com"),
    Bookmark(id: "b", title: "Swift", url: "https://swift.org"),
    Bookmark(id: "c", title: "Forums", url: "https://forums.swift.org"),
])
// SwiftUI clears the sheet item binding, then calls onDismiss.
func close() { model.editing = nil; model.sheetDismissed() }

// An ordinary close returns to the opener.
model.edit("b")
guard model.editing?.bookmarkID == "b" else { return false }
close()
guard model.focus == .editButton("b") else { return false }

// The opener is deleted by sync while the editor is open: fall back to Add Bookmark.
model.focus = nil
model.edit("c")
model.remove("c")
close()
guard model.focus == .addButton else { return false }

// Eligibility is decided at completion: a bookmark that survives is still the target.
model.focus = nil
model.edit("a")
model.rename("a", to: "Apple Inc.")
close()
guard model.focus == .editButton("a") else { return false }

// Duplicate swaps the sheet. The original sheet's onDismiss arrives while the copy's editor is up:
// it must not close the copy's editor or move focus behind it.
model.focus = nil
model.edit("a")
model.duplicateAndEdit("a")
guard model.editing?.bookmarkID == "a-copy" else { return false }
model.sheetDismissed()
guard model.editing?.bookmarkID == "a-copy", model.focus == nil else { return false }
close()
guard model.focus == .editButton("a-copy") else { return false }

// Another ordinary round after the swap still works.
model.focus = nil
model.edit("b")
close()
return model.focus == .editButton("b")
