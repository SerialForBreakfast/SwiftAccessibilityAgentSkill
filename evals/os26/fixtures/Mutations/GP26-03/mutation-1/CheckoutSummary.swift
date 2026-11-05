#if os(iOS)
import UIKit
@MainActor
public final class CheckoutSummary: UIStackView {
    public let totalLabel = UILabel()
    public let payButton = UIButton(type: .system)
    public init(formattedTotal: String, onPay: @escaping () -> Void) {
        super.init(frame: .zero)
        totalLabel.text = formattedTotal
        payButton.setTitle("Pay now", for: .normal)
        payButton.addAction(UIAction { _ in onPay() }, for: .touchUpInside)
        [totalLabel, payButton].forEach(addArrangedSubview)
        // PATCH BEGIN GP26-03
        totalLabel.font = .preferredFont(forTextStyle: .body)
        totalLabel.adjustsFontForContentSizeCategory = true
        totalLabel.numberOfLines = 0
        axis = .vertical
        distribution = .fill
        alignment = .fill
        spacing = 12
        heightAnchor.constraint(equalToConstant: 44).isActive = true
        // PATCH END GP26-03
    }
    required init(coder: NSCoder) { fatalError("Programmatic fixture") }
}
#endif
