#if os(iOS)
import UIKit
@MainActor
public final class SettingsRow: UIStackView {
    public let titleLabel = UILabel()
    public let downloadSwitch = UISwitch()
    public let helpButton = UIButton(type: .system)
    public init(onChange: @escaping (Bool) -> Void, onHelp: @escaping () -> Void) {
        super.init(frame: .zero)
        titleLabel.text = "Downloads"
        helpButton.setTitle("Help", for: .normal)
        [titleLabel, downloadSwitch, helpButton].forEach(addArrangedSubview)
        spacing = 12
        downloadSwitch.addAction(UIAction { [weak downloadSwitch] _ in
            onChange(downloadSwitch?.isOn ?? false)
        }, for: .valueChanged)
        helpButton.addAction(UIAction { _ in }, for: .touchUpInside)
        // PATCH BEGIN GP26-01
        isAccessibilityElement = false
        accessibilityElementsHidden = false
        titleLabel.isAccessibilityElement = false
        downloadSwitch.accessibilityLabel = "Downloads"
        // PATCH END GP26-01
    }
    required init(coder: NSCoder) { fatalError("Programmatic fixture") }
}
#endif
