import UIKit

@MainActor
final class TelevisionShelves: UIView {
    struct Item { let id: String; let title: String }
    struct Section { let id: String; let title: String; let items: [Item] }
    struct Key: Hashable { let section: String; let item: String }
    final class Shelf: UIView {
        let heading = UILabel()
        var buttons: [UIButton] = []
    }
    private(set) var shelves: [Shelf] = []
    private(set) var keys: [Key] = []
    private(set) var selected: Key?
    private var generation = 0
    var onChoose: (Key) -> Void = { _ in }
    @discardableResult
    func apply(_ sections: [Section]) -> Bool {
        guard Set(sections.map(\.id)).count == sections.count,
              sections.allSatisfy({ Set($0.items.map(\.id)).count == $0.items.count }) else { return false }
        generation += 1
        let revision = generation
        let nextKeys = sections.flatMap { section in section.items.map { Key(section: section.id, item: $0.id) } }
        if !nextKeys.contains(where: { $0 == selected }) { selected = nil }
        shelves.forEach { $0.removeFromSuperview() }
        isAccessibilityElement = false
        shelves = sections.map { section in
            let shelf = Shelf()
            shelf.isAccessibilityElement = false
            shelf.heading.text = section.title
            shelf.heading.isAccessibilityElement = true
            shelf.heading.accessibilityTraits.insert(.header)
            shelf.addSubview(shelf.heading)
            shelf.buttons = section.items.map { item in
                let key = Key(section: section.id, item: item.id)
                let button = UIButton(type: .system)
                button.setTitle(item.title, for: .normal)
                button.accessibilityLabel = item.title
                button.addAction(UIAction { [weak self, weak button] _ in
                    guard let self, let button, self.generation == revision,
                          button.isEnabled else { return }
                    self.select(key); self.onChoose(key)
                }, for: .primaryActionTriggered)
                shelf.addSubview(button)
                return button
            }
            shelf.accessibilityElements = [shelf.heading] + shelf.buttons
            addSubview(shelf)
            return shelf
        }
        keys = nextKeys
        accessibilityElements = shelves
        refreshSelection()
        return true
    }
    func select(_ key: Key?) {
        selected = key.flatMap { keys.contains($0) ? $0 : nil }
        refreshSelection()
    }
    private func refreshSelection() {
        for (key, button) in zip(keys, shelves.flatMap(\.buttons)) {
            if key == selected { button.accessibilityTraits.insert(.selected) }
            else { button.accessibilityTraits.remove(.selected) }
        }
    }
}
