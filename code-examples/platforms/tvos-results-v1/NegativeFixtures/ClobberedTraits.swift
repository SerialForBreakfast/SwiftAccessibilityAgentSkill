import UIKit

@MainActor
final class TelevisionResults: UIView {
    struct Item: Equatable { let id: String; let title: String; let actionName: String }
    private(set) var visible: [Item] = []
    private(set) var buttons: [UIButton] = []
    private(set) var selectedID: String?
    private var generation = 0
    @discardableResult
    func apply(_ items: [Item], query: String = "") -> Bool {
        guard Set(items.map(\.id)).count == items.count else { return false }
        generation += 1
        let revision = generation
        visible = items.filter { query.isEmpty || $0.title.localizedCaseInsensitiveContains(query) }
        if !visible.contains(where: { $0.id == selectedID }) { selectedID = nil }
        buttons.forEach { $0.removeFromSuperview() }
        buttons = visible.map { item in
            let button = UIButton(type: .system)
            button.setTitle(item.title, for: .normal)
            button.accessibilityLabel = item.actionName
            button.addAction(UIAction { [weak self, weak button] _ in
                guard let self, let button, self.generation == revision, button.isEnabled else { return }
                self.select(item.id)
            }, for: .primaryActionTriggered)
            addSubview(button)
            return button
        }
        refreshTraits()
        return true
    }
    func select(_ id: String?) {
        selectedID = visible.contains(where: { $0.id == id }) ? id : nil
        refreshTraits()
    }
    private func refreshTraits() {
        for (item, button) in zip(visible, buttons) {
            if item.id == selectedID { button.accessibilityTraits.insert(.selected) }
            else { button.accessibilityTraits = [] }
        }
    }
}

@MainActor
final class TelevisionStatus {
    let label = UILabel()
    private let reduceMotion: () -> Bool
    private let animate: () -> Void
    init(reduceMotion: @escaping () -> Bool = { UIAccessibility.isReduceMotionEnabled },
         animate: @escaping () -> Void) {
        self.reduceMotion = reduceMotion; self.animate = animate
        label.isAccessibilityElement = true
    }
    func update(_ text: String) {
        guard text != label.text else { return }
        // Final content never depends on animation or its completion callback.
        label.text = text
        label.accessibilityLabel = text
        if !reduceMotion() { animate() }
    }
}
