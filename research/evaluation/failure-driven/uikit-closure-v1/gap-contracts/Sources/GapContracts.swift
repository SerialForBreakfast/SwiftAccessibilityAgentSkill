import UIKit

@MainActor
public final class SummaryCard: UIView {
    public let title = UILabel()
    public let subtitle = UILabel()
    public override init(frame: CGRect) {
        super.init(frame: frame)
        addSubview(title)
        addSubview(subtitle)
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    // Caller supplies a complete localized summary, not concatenated translations.
    public func configure(title: String, subtitle: String, spokenSummary: String) {
        self.title.text = title
        self.subtitle.text = subtitle
        isAccessibilityElement = true
        self.title.isAccessibilityElement = false
        self.subtitle.isAccessibilityElement = false
        accessibilityLabel = spokenSummary
        accessibilityValue = nil
        accessibilityTraits.insert(.staticText)
    }
}

@MainActor
public final class QuantityValue: UILabel {
    var increase: () -> Void = {}
    var decrease: () -> Void = {}
    public override func accessibilityIncrement() { increase() }
    public override func accessibilityDecrement() { decrease() }
}

@MainActor
public final class QuantityChoices: UIStackView {
    public let value = QuantityValue()
    public let more = UIButton(type: .system)
    public let less = UIButton(type: .system)
    public private(set) var quantity = 0
    public var enabled = true {
        didSet {
            more.isEnabled = enabled
            less.isEnabled = enabled
            if enabled { value.accessibilityTraits.remove(.notEnabled) }
            else { value.accessibilityTraits.insert(.notEnabled) }
        }
    }
    public var onChange: (Int) -> Void = { _ in }
    public init(name: String) {
        super.init(frame: .zero)
        isAccessibilityElement = false
        value.isAccessibilityElement = true
        value.accessibilityLabel = name
        value.accessibilityTraits = [.adjustable]
        more.setTitle("Increase quantity", for: .normal)
        less.setTitle("Decrease quantity", for: .normal)
        [less, value, more].forEach(addArrangedSubview)
        value.increase = { [weak self] in self?.change(by: 1) }
        value.decrease = { [weak self] in self?.change(by: -1) }
        more.addAction(UIAction { [weak self] _ in self?.change(by: 1) }, for: .primaryActionTriggered)
        less.addAction(UIAction { [weak self] _ in self?.change(by: -1) }, for: .primaryActionTriggered)
        render()
    }
    required init(coder: NSCoder) { fatalError("Programmatic example") }
    private func change(by delta: Int) {
        guard enabled else { return }
        let next = min(3, max(0, quantity + delta))
        guard next != quantity else { return }
        quantity = next
        render()
        onChange(quantity)
    }
    private func render() {
        value.text = String(quantity)
        value.accessibilityValue = String(quantity)
    }
}

@MainActor
public final class MotionStatus: UIView {
    public let label = UILabel()
    private let readReduceMotion: () -> Bool
    public var animate: (TimeInterval) -> Void = { _ in }
    public init(readReduceMotion: @escaping () -> Bool = { UIAccessibility.isReduceMotionEnabled }) {
        self.readReduceMotion = readReduceMotion
        super.init(frame: .zero)
        addSubview(label)
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    public func update(message: String) {
        label.text = message
        label.accessibilityLabel = message
        if !readReduceMotion() { animate(0.25) }
    }
}
