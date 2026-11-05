#if os(iOS)
import UIKit
public struct Order {
    public let customer: String
    public let status: String
    public let isPriority: Bool
    public init(customer: String, status: String, isPriority: Bool) {
        self.customer = customer; self.status = status; self.isPriority = isPriority
    }
}
@MainActor
public final class OrderCell: UITableViewCell {
    public let titleLabel = UILabel()
    public override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        contentView.addSubview(titleLabel)
        titleLabel.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            titleLabel.leadingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.leadingAnchor),
            titleLabel.trailingAnchor.constraint(equalTo: contentView.layoutMarginsGuide.trailingAnchor),
            titleLabel.topAnchor.constraint(equalTo: contentView.layoutMarginsGuide.topAnchor),
            titleLabel.bottomAnchor.constraint(equalTo: contentView.layoutMarginsGuide.bottomAnchor)
        ])
    }
    required init?(coder: NSCoder) { fatalError("Programmatic fixture") }
    // PATCH BEGIN GP26-02
    public func configure(_ order: Order) {
        titleLabel.text = order.customer
        isAccessibilityElement = true
        if order.isPriority { accessibilityLabel = "Priority order for \(order.customer)" }
        accessibilityValue = order.status
    }
    // PATCH END GP26-02
}
#endif
