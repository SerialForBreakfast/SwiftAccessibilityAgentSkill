import UIKit

@MainActor
public final class SavedItemCell: UICollectionViewCell {
    public let titleLabel = UILabel()
    private var generation = 0
    public var onRemove: ((String) -> Void)?

    public override init(frame: CGRect) {
        super.init(frame: frame)
        contentView.addSubview(titleLabel)
        isAccessibilityElement = true
        titleLabel.isAccessibilityElement = false
    }

    public required init?(coder: NSCoder) { fatalError("Programmatic example") }

    public func configure(id: String, title: String, saved: Bool, removable: Bool, language: String) {
        generation += 1
        let token = generation
        titleLabel.text = title
        accessibilityAttributedLabel = NSAttributedString(string: title, attributes: [.accessibilitySpeechLanguage: language])
        accessibilityValue = saved ? "Saved" : "Not saved"
        if saved { accessibilityTraits.insert(.selected) }
        else { accessibilityTraits.remove(.selected) }
        accessibilityHint = removable ? "Remove is available in actions" : nil
        accessibilityCustomActions = removable ? [UIAccessibilityCustomAction(name: "Remove") { [weak self] _ in
            guard let self, self.generation == token, let remove = self.onRemove else { return false }
            remove(id)
            return true
        }] : []
    }

    public override func prepareForReuse() {
        super.prepareForReuse()
        generation += 1
        titleLabel.text = nil
        accessibilityAttributedLabel = nil
        accessibilityValue = nil
        accessibilityHint = nil
        accessibilityCustomActions = []
        accessibilityTraits.remove(.selected)
        onRemove = nil
    }
}

@MainActor
public enum ReusableTypography {
    public static func configure(_ label: UILabel, style: UIFont.TextStyle) {
        label.font = .preferredFont(forTextStyle: style, compatibleWith: label.traitCollection)
        label.adjustsFontForContentSizeCategory = true
        label.numberOfLines = 0
    }
}

@MainActor
public enum SectionConfiguration {
    public static func configure(_ header: UILabel, title: String, isHeading: Bool) {
        header.text = title
        header.accessibilityLabel = title
        header.isAccessibilityElement = true
        if isHeading { header.accessibilityTraits.insert(.header) }
        else { header.accessibilityTraits.remove(.header) }
    }

    public static func nested(header: UILabel, rows: [UIView]) -> UIView {
        let list = UIView()
        list.isAccessibilityElement = false
        list.accessibilityContainerType = .list
        rows.forEach(list.addSubview)
        list.accessibilityElements = rows
        let section = UIView()
        section.isAccessibilityElement = false
        section.accessibilityContainerType = .semanticGroup
        section.addSubview(header)
        section.addSubview(list)
        section.accessibilityElements = [header, list]
        return section
    }
}

@MainActor
public struct AccessibilityUpdate {
    public let notification: UIAccessibility.Notification
    public let target: UIView?

    public static func layout(target: UIView?) -> Self {
        Self(notification: .screenChanged, target: target)
    }

    public static func screen(target: UIView?) -> Self {
        Self(notification: .screenChanged, target: target)
    }

    public func deliver(using post: (UIAccessibility.Notification, Any?) -> Void) {
        post(notification, target)
    }
}
