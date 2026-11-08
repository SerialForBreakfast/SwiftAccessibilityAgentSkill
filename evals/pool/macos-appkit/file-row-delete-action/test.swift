_ = NSApplication.shared
var opened: [String] = [], deleted: [String] = []
let row = FileRowView(frame: NSRect(x: 0, y: 0, width: 480, height: 28))
let budget = FileItem(id: "a", name: "Budget.numbers", modified: "Today", isLocked: false)
let notes = FileItem(id: "b", name: "Notes.txt", modified: "Yesterday", isLocked: false)
let contract = FileItem(id: "c", name: "Contract.pdf", modified: "Monday", isLocked: true)
func show(_ file: FileItem) {
    row.configure(with: file, onOpen: { opened.append($0.id) }, onDelete: { deleted.append($0.id) })
}
func deleteActions() -> [NSAccessibilityCustomAction] {
    (row.accessibilityCustomActions() ?? []).filter { $0.name.localizedCaseInsensitiveContains("delete") }
}

show(budget)
guard let earlier = deleteActions().first else { return false }
show(notes)

// The row offers exactly one Delete action, and it deletes the file the row shows now, once.
guard deleteActions().count == 1, fire(deleteActions()[0]), deleted == ["b"] else { return false }
// An action object kept from before the row was reused never deletes the previous file.
deleted = []
_ = fire(earlier)
guard !deleted.contains("a"), deleted.count <= 1 else { return false }

// The ordinary buttons stay reachable and still act once on the current file.
for button in [row.openButton, row.deleteButton] {
    guard reachable(button, from: row), button.isEnabled else { return false }
}
guard row.openButton.accessibilityLabel() == "Open Notes.txt",
      row.deleteButton.accessibilityLabel() == "Delete Notes.txt" else { return false }
opened = []; deleted = []
guard press(row.openButton), opened == ["b"], deleted.isEmpty else { return false }
guard press(row.deleteButton), deleted == ["b"], opened == ["b"] else { return false }

// A locked file can't be deleted through the shortcut either; Open still works.
show(contract)
opened = []; deleted = []
guard deleteActions().count <= 1, !row.deleteButton.isEnabled else { return false }
for action in deleteActions() { _ = fire(action) }
_ = fire(earlier)
_ = press(row.deleteButton)
guard deleted.isEmpty, press(row.openButton), opened == ["c"], reachable(row.openButton, from: row) else { return false }

// Unlocked again after reuse: the shortcut works for the new file.
show(budget)
deleted = []
guard deleteActions().count == 1, fire(deleteActions()[0]), deleted == ["a"] else { return false }
return true
