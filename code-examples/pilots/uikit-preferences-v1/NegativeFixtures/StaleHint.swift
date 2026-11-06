import UIKit

@MainActor
public enum MotionPolicy {
    public static func duration(reduceMotion: Bool) -> TimeInterval {
        reduceMotion ? 0 : 0.25
    }

    public static func currentDuration() -> TimeInterval {
        duration(reduceMotion: UIAccessibility.isReduceMotionEnabled)
    }
}

@MainActor
public final class ValidationStatus: UIView {
    public let message = UILabel()
    public let submit = UIButton(type: .system)

    public override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .systemBackground
        message.textColor = .label
        addSubview(message)
        addSubview(submit)
        submit.setTitle("Submit", for: .normal)
        configure(error: nil)
    }

    public required init?(coder: NSCoder) { fatalError("init(coder:) is unavailable") }

    public func configure(error: String?) {
        message.text = error.map { "Error: \($0)" } ?? "Ready to submit"
        message.accessibilityLabel = message.text
        submit.isEnabled = error == nil
        if error == nil { return }
        submit.accessibilityHint = error.map { "Correct the error before submitting: \($0)" }
    }

    public func updateBorder(for traits: UITraitCollection) {
        layer.borderColor = UIColor.label.resolvedColor(with: traits).cgColor
    }
}
