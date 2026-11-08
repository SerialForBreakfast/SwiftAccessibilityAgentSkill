macOS 26, SwiftUI.

Keyboard users tell us that after they close the bookmark editor sheet (Save, Cancel or Escape), focus lands on Add Bookmark instead of the Edit… button they used to open it. Please send focus back to that bookmark's Edit… button.

A couple of things make this awkward. iCloud sync can delete the bookmark while its editor is open; in that case Add Bookmark is the right place to land. And Duplicate in the editor switches the sheet straight to the copy's editor: SwiftUI runs our onDismiss for the original sheet after the copy's editor is already showing. When the copy's editor closes, people should land on the copy's Edit… button.

Keep `BookmarksModel`, `Bookmark`, `EditRequest`, `BookmarkFocus`, `bookmarks`, `editing` (the sheet item), `focus`, `edit(_:)`, `duplicateAndEdit(_:)`, `remove(_:)` and `sheetDismissed()` (the sheet's onDismiss) with their current names and types.
