import UIKit

final class CheckoutViewController: UIViewController {
    let totalLabel = UILabel()
    let payButton = UIButton(type: .system)
    var formattedTotal = "Total: 1.234.567,89 € inklusive Mehrwertsteuer"
    private(set) var payCount = 0
    private let summary = UIStackView()

    override func viewDidLoad() {
        super.viewDidLoad()
        totalLabel.text = formattedTotal
        totalLabel.font = UIFontMetrics(forTextStyle: .body).scaledFont(for: .systemFont(ofSize: 17))
        totalLabel.adjustsFontForContentSizeCategory = true
        totalLabel.numberOfLines = 0
        totalLabel.adjustsFontSizeToFitWidth = false
        payButton.setTitle("Pay now", for: .normal)
        payButton.addTarget(self, action: #selector(pay), for: .primaryActionTriggered)

        summary.addArrangedSubview(totalLabel)
        summary.addArrangedSubview(payButton)
        summary.spacing = 8
        summary.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(summary)
        NSLayoutConstraint.activate([
            summary.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            summary.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
            summary.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            summary.heightAnchor.constraint(equalToConstant: 44),
        ])
        updateAxis()
        registerForTraitChanges([UITraitPreferredContentSizeCategory.self]) { (self: Self, _: UITraitCollection) in
            self.updateAxis()
        }
    }

    private func updateAxis() {
        let large = traitCollection.preferredContentSizeCategory.isAccessibilityCategory
        summary.axis = large ? .vertical : .horizontal
        summary.alignment = large ? .leading : .center
    }

    @objc func pay() {
        payCount += 1
    }
}
