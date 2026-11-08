import UIKit

/// Builds receipt rows. The same rows appear in the order screen and in the
/// "Preview text size" sheet, which renders them for the size the customer picks.
final class ReceiptRowStyler {
    let brandFont: UIFont
    let detailColor: UIColor = .secondaryLabel

    init(brandFont: UIFont = UIFont(name: "AvenirNext-Medium", size: 15) ?? .systemFont(ofSize: 15)) {
        self.brandFont = brandFont
    }

    func makeDescriptionLabel(text: String, traits: UITraitCollection) -> UILabel {
        let label = UILabel()
        label.text = text
        label.font = UIFontMetrics(forTextStyle: .body).scaledFont(for: brandFont, compatibleWith: traits)
        label.textColor = detailColor
        label.numberOfLines = 1
        label.adjustsFontSizeToFitWidth = true
        label.minimumScaleFactor = 0.6
        return label
    }
}

final class TextSizePreviewController: UIViewController {
    let styler = ReceiptRowStyler()
    let sizes: [UIContentSizeCategory] = [.small, .large, .extraExtraLarge, .accessibilityLarge, .accessibilityExtraExtraExtraLarge]
    let picker = UISegmentedControl(items: ["XS", "M", "XXL", "AX1", "AX5"])
    private let rows = UIStackView()
    var sampleDescriptions = ["2 × Oat flat white, extra hot, no lid", "Gift wrap with handwritten card"]

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBackground
        picker.selectedSegmentIndex = 1
        picker.addTarget(self, action: #selector(sizeChanged), for: .valueChanged)
        rows.axis = .vertical
        rows.spacing = 8
        let column = UIStackView(arrangedSubviews: [picker, rows])
        column.axis = .vertical
        column.spacing = 16
        column.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(column)
        NSLayoutConstraint.activate([
            column.leadingAnchor.constraint(equalTo: view.layoutMarginsGuide.leadingAnchor),
            column.trailingAnchor.constraint(equalTo: view.layoutMarginsGuide.trailingAnchor),
            column.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 16),
        ])
        rebuildRows()
    }

    @objc func sizeChanged() {
        rebuildRows()
    }

    private func rebuildRows() {
        rows.arrangedSubviews.forEach { $0.removeFromSuperview() }
        let traits = UITraitCollection(preferredContentSizeCategory: sizes[picker.selectedSegmentIndex])
        for text in sampleDescriptions {
            rows.addArrangedSubview(styler.makeDescriptionLabel(text: text, traits: traits))
        }
    }
}
