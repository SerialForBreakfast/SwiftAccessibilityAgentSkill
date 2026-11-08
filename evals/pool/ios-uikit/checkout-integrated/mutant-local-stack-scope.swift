import UIKit

final class CheckoutViewController: UIViewController {
    let totalLabel = UILabel()
    let payButton = UIButton(type: .system)
    var formattedTotal = "Total: 1.234.567,89 € inklusive Mehrwertsteuer"
    private(set) var payCount = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        totalLabel.text = formattedTotal
        totalLabel.font = UIFontMetrics(forTextStyle: .body).scaledFont(for: .systemFont(ofSize: 17))
        totalLabel.adjustsFontForContentSizeCategory = true
        totalLabel.numberOfLines = 0
        payButton.setTitle("Pay now", for: .normal)
        payButton.addTarget(self, action: #selector(pay), for: .primaryActionTriggered)

        let summary = UIStackView(arrangedSubviews: [totalLabel, payButton])
        summary.axis = traitCollection.preferredContentSizeCategory.isAccessibilityCategory ? .vertical : .horizontal
        summary.distribution = .fill
        summary.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(summary)
        NSLayoutConstraint.activate([
            summary.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            summary.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
            summary.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
        ])
    }

    override func traitCollectionDidChange(_ previous: UITraitCollection?) {
        super.traitCollectionDidChange(previous)
        summary.axis = traitCollection.preferredContentSizeCategory.isAccessibilityCategory ? .vertical : .horizontal
    }

    @objc func pay() {
        payCount += 1
    }
}
