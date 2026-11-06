import AppKit

@MainActor
final class DesktopOutline: NSObject, NSOutlineViewDataSource {
    struct Item { let id: String; let title: String; var children: [Item] = [] }
    final class Node: NSObject {
        let id: String
        var title: String
        var children: [Node] = []
        init(id: String, title: String) { self.id = id; self.title = title }
    }
    let outline = NSOutlineView()
    private(set) var roots: [Node] = []
    private(set) var nodes: [String: Node] = [:]
    override init() {
        super.init()
        let name = NSTableColumn(identifier: NSUserInterfaceItemIdentifier("name"))
        name.title = "Name"
        let kind = NSTableColumn(identifier: NSUserInterfaceItemIdentifier("kind"))
        kind.title = "Kind"
        outline.addTableColumn(name); outline.addTableColumn(kind)
        outline.outlineTableColumn = name
        outline.allowsEmptySelection = true
        outline.allowsMultipleSelection = false
        outline.setAccessibilityLabel("Library")
        outline.dataSource = self
    }
    var selectedID: String? { (outline.item(atRow: outline.selectedRow) as? Node)?.id }
    @discardableResult
    func apply(_ items: [Item]) -> Bool {
        var ids = Set<String>()
        func unique(_ item: Item) -> Bool {
            guard ids.insert(item.id).inserted else { return false }
            return item.children.allSatisfy(unique)
        }
        guard items.allSatisfy(unique) else { return false }
        let selected = selectedID
        let expanded = Set(nodes.values.filter { outline.isItemExpanded($0) }.map(\.id))
        var next: [String: Node] = [:]
        var ordered: [Node] = []
        func build(_ item: Item) -> Node {
            let node = nodes[item.id] ?? Node(id: item.id, title: item.title)
            node.title = item.title
            next[item.id] = node; ordered.append(node)
            node.children = item.children.map(build)
            return node
        }
        roots = items.map(build); nodes = next
        outline.reloadData()
        for node in ordered where expanded.contains(node.id) && !node.children.isEmpty {
            outline.expandItem(node)
        }
        select(selected)
        return true
    }
    func select(_ id: String?) {
        guard let id, let node = nodes[id] else { outline.deselectAll(nil); return }
        let row = outline.row(forItem: node)
        guard row >= 0 else { outline.deselectAll(nil); return }
        outline.selectRowIndexes(IndexSet(integer: row), byExtendingSelection: false)
    }
    private func current(_ item: Any?) -> Node? {
        guard let node = item as? Node else { return nil }
        return node
    }
    func outlineView(_ outlineView: NSOutlineView, numberOfChildrenOfItem item: Any?) -> Int {
        item == nil ? roots.count : current(item)?.children.count ?? 0
    }
    func outlineView(_ outlineView: NSOutlineView, child index: Int, ofItem item: Any?) -> Any {
        let children = item == nil ? roots : current(item)?.children ?? []
        // AppKit requests an index within the count supplied above.
        precondition(children.indices.contains(index))
        return children[index]
    }
    func outlineView(_ outlineView: NSOutlineView, isItemExpandable item: Any) -> Bool {
        !(current(item)?.children.isEmpty ?? true)
    }
    func outlineView(_ outlineView: NSOutlineView, objectValueFor tableColumn: NSTableColumn?, byItem item: Any?) -> Any? {
        guard let node = current(item) else { return nil }
        switch tableColumn?.identifier.rawValue {
        case "name": return node.title
        case "kind": return node.children.isEmpty ? "Item" : "Group"
        default: return nil
        }
    }
}
