import UIKit
import AVKit

@MainActor
final class RegionState: UIView {
    let button = UIButton(type: .system)
    let status = UILabel()
    let query = UITextField()
    let backdrop = UIVisualEffectView(effect: UIBlurEffect(style: .regular))
    override init(frame: CGRect) {
        super.init(frame: frame); [backdrop, button, status, query].forEach { addSubview($0) }
        isAccessibilityElement = false; accessibilityLabel = "Downloads"
        accessibilityElements = [query, button, status]
        query.accessibilityLabel = "Search downloads"
        status.textColor = .label; status.numberOfLines = 0; status.lineBreakMode = .byWordWrapping
        status.font = .preferredFont(forTextStyle: .body); status.adjustsFontForContentSizeCategory = true
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    func configure(name: String, selected: Bool, reduceTransparency: Bool) {
        button.setTitle(name, for: .normal); button.accessibilityLabel = name
        status.text = selected ? "Selected" : "Not selected"; button.accessibilityValue = status.text
        if selected { button.accessibilityTraits.insert(.selected) } else { button.accessibilityTraits.remove(.selected) }
        backdrop.isHidden = reduceTransparency
    }
    func search(_ text: String, count: Int) {
        query.text = text; status.text = "\(count) results"; status.accessibilityLabel = status.text
    }
    static func player(_ player: AVPlayer) -> AVPlayerViewController {
        let view = AVPlayerViewController(); view.player = player; view.showsPlaybackControls = true; return view
    }
}

@MainActor
final class ModalFlag {
    let view: UIView
    private var prior: Bool?
    init(_ view: UIView) { self.view = view }
    func begin() { guard prior == nil else { return }; prior = view.accessibilityViewIsModal; view.accessibilityViewIsModal = true }
    func end() { guard let prior else { return }; view.accessibilityViewIsModal = false; self.prior = nil }
}
