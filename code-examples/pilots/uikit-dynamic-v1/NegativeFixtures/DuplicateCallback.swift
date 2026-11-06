import UIKit

public struct SectionRecord {
    public let id: String
    public let title: String
    public init(id: String, title: String) { self.id = id; self.title = title }
}

@MainActor public final class DynamicSections: UIView {
    public private(set) var labels: [UILabel] = []
    private var byID: [String: UILabel] = [:]
    public override init(frame: CGRect) {
        super.init(frame: frame)
        isAccessibilityElement = false
        accessibilityElements = []
        accessibilityCustomRotors = [UIAccessibilityCustomRotor(name: "Sections") { [weak self] predicate in
            guard let self, !self.labels.isEmpty else { return nil }
            let item: UIAccessibilityCustomRotorItemResult? = predicate.currentItem
            let current = self.labels.firstIndex { $0 === item?.targetElement }
            let index = predicate.searchDirection == .next
                ? current.map { $0 + 1 } ?? 0
                : current.map { $0 - 1 } ?? self.labels.count - 1
            guard self.labels.indices.contains(index) else { return nil }
            return UIAccessibilityCustomRotorItemResult(targetElement: self.labels[index], targetRange: nil)
        }]
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    @discardableResult public func replace(_ records: [SectionRecord]) -> Bool {
        guard Set(records.map(\.id)).count == records.count else { return false }
        var next: [String: UILabel] = [:]
        let ordered = records.map { record in
            let label = byID[record.id] ?? UILabel()
            label.text = record.title
            label.accessibilityLabel = record.title
            label.accessibilityTraits.insert(.header)
            next[record.id] = label
            return label
        }
        labels.forEach { $0.removeFromSuperview() }
        ordered.forEach(addSubview)
        byID = next
        labels = ordered
        accessibilityElements = ordered
        return true
    }
}

public enum MessageOperation: String { case archive, delete }

@MainActor public final class ReusableMessageActions: UIView {
    public let summary = UILabel()
    public let archiveButton = UIButton(type: .system)
    public let deleteButton = UIButton(type: .system)
    private var revision = 0
    private var itemID = ""
    private var active = false
    private let onAction: (String, MessageOperation) -> Void
    public init(onAction: @escaping (String, MessageOperation) -> Void) {
        self.onAction = onAction
        super.init(frame: .zero)
        isAccessibilityElement = false
        [summary, archiveButton, deleteButton].forEach(addSubview)
        for (button, operation) in [(archiveButton, MessageOperation.archive), (deleteButton, .delete)] {
            button.setTitle(operation == .archive ? "Archive" : "Delete", for: .normal)
            button.isEnabled = false
            button.addAction(UIAction { [weak self] _ in
                guard let self else { return }
                _ = self.perform(token: self.revision, id: self.itemID, operation: operation)
            }, for: .touchUpInside)
        }
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    public func configure(id: String, title: String, enabled: Bool) {
        revision += 1
        itemID = id
        active = enabled
        summary.text = title
        summary.accessibilityLabel = title
        archiveButton.isEnabled = enabled
        deleteButton.isEnabled = enabled
        archiveButton.accessibilityLabel = "Archive \(title)"
        deleteButton.accessibilityLabel = "Delete \(title)"
        let token = revision
        summary.accessibilityCustomActions = [.archive, .delete].map { (operation: MessageOperation) in
            UIAccessibilityCustomAction(name: "\(operation == .archive ? "Archive" : "Delete") \(title)") { [weak self] _ in
                self?.perform(token: token, id: id, operation: operation) ?? false
            }
        }
    }
    private func perform(token: Int, id: String, operation: MessageOperation) -> Bool {
        guard token == revision, active else { return false }
        onAction(id, operation)
        onAction(id, operation)
        return true
    }
}
