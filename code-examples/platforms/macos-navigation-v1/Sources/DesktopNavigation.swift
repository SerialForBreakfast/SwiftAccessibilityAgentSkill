import AppKit

@MainActor
final class DesktopResults: NSObject, NSTableViewDataSource {
    struct Item: Equatable { let id: String; let title: String }
    let table = NSTableView()
    private(set) var items: [Item] = []
    override init() {
        super.init()
        table.addTableColumn(NSTableColumn(identifier: NSUserInterfaceItemIdentifier("title")))
        table.allowsEmptySelection = true
        table.allowsMultipleSelection = false
        table.dataSource = self
    }
    var selectedID: String? {
        items.indices.contains(table.selectedRow) ? items[table.selectedRow].id : nil
    }
    @discardableResult
    func apply(_ next: [Item]) -> Bool {
        guard Set(next.map(\.id)).count == next.count else { return false }
        let previous = selectedID
        items = next
        table.reloadData()
        select(previous)
        return true
    }
    func select(_ id: String?) {
        guard let id, let index = items.firstIndex(where: { $0.id == id }) else {
            table.deselectAll(nil); return
        }
        table.selectRowIndexes(IndexSet(integer: index), byExtendingSelection: false)
    }
    func numberOfRows(in tableView: NSTableView) -> Int { items.count }
    func tableView(_ tableView: NSTableView, objectValueFor tableColumn: NSTableColumn?, row: Int) -> Any? {
        items.indices.contains(row) ? items[row].title : nil
    }
}

@MainActor
final class DesktopKeyOrder {
    private var configured: [NSButton] = []
    // This configures links only; AppKit still decides actual keyboard navigation.
    func apply(_ buttons: [NSButton]) {
        configured.forEach { $0.nextKeyView = nil }
        var seen = Set<ObjectIdentifier>()
        configured = buttons.filter { seen.insert(ObjectIdentifier($0)).inserted }
        configured.forEach { $0.nextKeyView = nil }
        let eligible = configured.filter { $0.isEnabled && !$0.isHidden }
        for (index, button) in eligible.enumerated() {
            button.nextKeyView = eligible[(index + 1) % eligible.count]
        }
    }
    func stop() { configured.forEach { $0.nextKeyView = nil }; configured = [] }
}
