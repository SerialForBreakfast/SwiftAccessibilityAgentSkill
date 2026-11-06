import UIKit

/// Callers supply complete localized names, rather than joining translated fragments.
@MainActor
final class ItemActionCard: UIView {
    let decoration = UILabel()
    let titleLabel = UILabel()
    let openButton = UIButton(type: .system)
    let saveButton = UIButton(type: .system)
    private var openHandler: () -> Void = {}
    private var saveHandler: () -> Void = {}

    override init(frame: CGRect) {
        super.init(frame: frame)
        [decoration, titleLabel, openButton, saveButton].forEach(addSubview)
        openButton.addAction(UIAction { [weak self] _ in self?.openHandler() }, for: .touchUpInside)
        saveButton.addAction(UIAction { [weak self] _ in self?.saveHandler() }, for: .touchUpInside)
    }

    required init?(coder: NSCoder) { fatalError("init(coder:) is not supported") }

    func configure(title: String, openTitle: String, saveTitle: String,
                   openName: String, saveName: String,
                   onOpen: @escaping () -> Void, onSave: @escaping () -> Void) {
        // This example owns these properties; it never collapses its action subtree.
        isAccessibilityElement = false
        accessibilityElementsHidden = false
        decoration.text = "*"
        decoration.isAccessibilityElement = false
        titleLabel.text = title
        titleLabel.isAccessibilityElement = true
        titleLabel.accessibilityLabel = nil
        openButton.isAccessibilityElement = true
        saveButton.isAccessibilityElement = true
        openButton.setTitle(openTitle, for: .normal)
        saveButton.setTitle(saveTitle, for: .normal)
        openButton.accessibilityLabel = openName
        saveButton.accessibilityLabel = saveName
        openHandler = onOpen
        saveHandler = onSave
    }
}
