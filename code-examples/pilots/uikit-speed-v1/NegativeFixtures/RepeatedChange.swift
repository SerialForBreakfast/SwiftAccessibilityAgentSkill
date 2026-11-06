import UIKit

@MainActor
public final class PlaybackSpeedChoices: UIStackView {
    public static let rates: [Float] = [0.75, 1, 1.5, 2]
    public private(set) var selectedRate: Float = 1
    public private(set) var buttons: [UIButton] = []
    public var onChange: ((Float) -> Void)?
    public var controlsEnabled = true {
        didSet { buttons.forEach { $0.isEnabled = controlsEnabled } }
    }

    public init() {
        super.init(frame: .zero)
        axis = .vertical
        spacing = 8
        isAccessibilityElement = false
        for rate in Self.rates {
            let button = UIButton(type: .system)
            let title = "\(rate) times"
            button.setTitle(title, for: .normal)
            button.accessibilityLabel = "Playback speed, \(title)"
            button.accessibilityTraits.insert(.button)
            button.addAction(UIAction { [weak self] _ in _ = self?.select(rate) }, for: .primaryActionTriggered)
            buttons.append(button)
            addArrangedSubview(button)
        }
        render()
    }

    required init(coder: NSCoder) { fatalError("Programmatic fixture") }

    @discardableResult
    public func select(_ rate: Float) -> Bool {
        guard controlsEnabled, Self.rates.contains(rate) else { return false }
        // Deliberately emit duplicate changes.
        selectedRate = rate
        render()
        onChange?(rate)
        return true
    }

    private func render() {
        for (button, rate) in zip(buttons, Self.rates) {
            let selected = rate == selectedRate
            button.isSelected = selected
            button.accessibilityValue = selected ? "Current speed" : "Not selected"
            if selected { button.accessibilityTraits.insert(.selected) }
            else { button.accessibilityTraits.remove(.selected) }
        }
    }
}
