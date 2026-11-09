import UIKit
@MainActor final class InvoiceCard: UIView {
    let star = UIImageView(), title = UILabel()
    let open = UIButton(type: .system), save = UIButton(type: .system)
    override init(frame: CGRect) {
        super.init(frame: frame)
        [star, title, open, save].forEach { addSubview($0) }
    }
    required init?(coder: NSCoder) { nil }
}
