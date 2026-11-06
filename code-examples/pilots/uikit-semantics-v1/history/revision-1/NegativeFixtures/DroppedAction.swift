import UIKit

@MainActor public enum SemanticConfiguration {
    public static func configure(_ button: UIButton, selected: Bool, hint: String?) {
        button.accessibilityLabel = "Bookmark"
        button.accessibilityHint = hint
        button.accessibilityValue = selected ? "Saved" : "Not saved"
        if selected { button.accessibilityTraits.insert(.selected) }
        else { button.accessibilityTraits.remove(.selected) }
    }

    public static func container(children: [UIView]) -> UIView {
        let view = UIView()
        children.forEach(view.addSubview)
        view.isAccessibilityElement = false
        view.accessibilityElementsHidden = false
        view.shouldGroupAccessibilityChildren = true
        view.accessibilityElements = children
        return view
    }
}

@MainActor public final class AdjustableQuantity: UIView {
    public private(set) var quantity = 0
    public override init(frame: CGRect) {
        super.init(frame: frame)
        isAccessibilityElement = true
        accessibilityLabel = "Quantity"
        accessibilityTraits.insert(.adjustable)
        updateValue()
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    public override func accessibilityIncrement() { quantity = min(3, quantity + 1); updateValue() }
    public override func accessibilityDecrement() { quantity = max(0, quantity - 1); updateValue() }
    private func updateValue() { accessibilityValue = String(quantity) }
}

@MainActor public final class ArchiveControl: UIView {
    public let button = UIButton(type: .system)
    public private(set) var archived = false
    private let onArchive: () -> Void
    public init(onArchive: @escaping () -> Void) {
        self.onArchive = onArchive
        super.init(frame: .zero)
        isAccessibilityElement = false
        button.setTitle("Archive", for: .normal)
        button.accessibilityLabel = "Archive message"
        addSubview(button)
        button.addAction(UIAction { [weak self] _ in _ = self?.performArchive() }, for: .touchUpInside)
        button.accessibilityCustomActions = [UIAccessibilityCustomAction(name: "Archive message") { [weak self] _ in
            self?.performArchive() ?? false
        }]
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    private func performArchive() -> Bool {
        guard !archived else { return false }
        archived = true
        // Intentional defect: callback omitted.
        return true
    }
}

@MainActor public final class SectionRotor: UIView {
    public let sections: [UILabel]
    public init(names: [String]) {
        sections = names.map { name in
            let label = UILabel()
            label.text = name
            label.accessibilityLabel = name
            label.accessibilityTraits.insert(.header)
            return label
        }
        super.init(frame: .zero)
        sections.forEach(addSubview)
        isAccessibilityElement = false
        accessibilityElements = sections
        accessibilityCustomRotors = [UIAccessibilityCustomRotor(name: "Sections") { [weak self] predicate in
            guard let self, !self.sections.isEmpty else { return nil }
            let current = self.sections.firstIndex { $0 === predicate.currentItem.targetElement }
            let index: Int
            if predicate.searchDirection == .next { index = current.map { $0 + 1 } ?? 0 }
            else { index = current.map { $0 - 1 } ?? self.sections.count - 1 }
            guard self.sections.indices.contains(index) else { return nil }
            return UIAccessibilityCustomRotorItemResult(targetElement: self.sections[index], targetRange: nil)
        }]
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
}
