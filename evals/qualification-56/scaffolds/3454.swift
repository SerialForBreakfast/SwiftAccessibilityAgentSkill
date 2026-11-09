import UIKit
@MainActor final class CheckoutPanel: UIView {
    let heading = UILabel(), apply = UIButton(type: .system), cancel = UIButton(type: .system)
    var animateDismissal: (@escaping () -> Void) -> Void = { done in done() }
    var requestFocus: (UIView?) -> Void = { _ in }
    override init(frame: CGRect) {
        super.init(frame: frame)
        [heading, apply, cancel].forEach { addSubview($0) }
    }
    required init?(coder: NSCoder) { nil }
}
