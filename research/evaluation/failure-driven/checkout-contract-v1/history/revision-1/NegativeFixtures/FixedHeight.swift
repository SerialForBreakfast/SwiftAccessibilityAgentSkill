import UIKit

@MainActor
public final class CheckoutSummary: UIStackView {
    public let totalLabel = UILabel()
    public let payButton: UIButton

    public init(payButton: UIButton) {
        self.payButton = payButton
        super.init(frame: .zero)
        axis = .vertical
        alignment = .fill
        spacing = 8
        heightAnchor.constraint(equalToConstant: 44).isActive = true
        totalLabel.font = .preferredFont(forTextStyle: .body)
        totalLabel.adjustsFontForContentSizeCategory = true
        totalLabel.numberOfLines = 0
        addArrangedSubview(totalLabel)
        addArrangedSubview(payButton)
    }

    required init(coder: NSCoder) { fatalError("Programmatic example") }

    public func update(total: String) {
        totalLabel.text = total
    }
}
