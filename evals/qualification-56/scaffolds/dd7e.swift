import AppKit
struct LibraryEntry {
    let id: String
    var name: String
    var kind: String
    var children: [LibraryEntry]
}
@MainActor final class LibraryOutline {
    let outline = NSOutlineView()
    init() {
        for name in ["Name", "Kind"] {
            let column = NSTableColumn(identifier: .init(name))
            column.title = name
            outline.addTableColumn(column)
        }
        outline.outlineTableColumn = outline.tableColumns.first
    }
}
