import UIKit

final class CheckoutViewController: UIViewController {
    let totalLabel = UILabel()
    let payButton = UIButton(type: .system)
    var formattedTotal = "Total: 1.234.567,89 € inklusive Mehrwertsteuer"
    private(set) var payCount = 0

    override func viewDidLoad() {
        super.viewDidLoad()
        totalLabel.text = formattedTotal
        totalLabel.font = .systemFont(ofSize: 17)
        totalLabel.numberOfLines = 1
        totalLabel.adjustsFontSizeToFitWidth = true
        totalLabel.minimumScaleFactor = 0.5
        payButton.setTitle("Pay now", for: .normal)
        payButton.addTarget(self, action: #selector(pay), for: .primaryActionTriggered)

        let summary = UIStackView(arrangedSubviews: [totalLabel, payButton])
        summary.axis = .horizontal
        summary.distribution = .fillEqually
        summary.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(summary)
        NSLayoutConstraint.activate([
            summary.leadingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leadingAnchor),
            summary.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
            summary.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            summary.heightAnchor.constraint(equalToConstant: 44),
        ])
    }

    @objc func pay() {
        payCount += 1
    }
}
