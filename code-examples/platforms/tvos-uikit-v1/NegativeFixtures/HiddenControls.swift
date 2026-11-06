import UIKit

@MainActor
final class TelevisionActions: UIView {
    let title = UILabel()
    let play = UIButton(type: .system)
    let details = UIButton(type: .system)
    private var generation = 0
    private var onPlay: () -> Void = {}
    private var onDetails: () -> Void = {}

    init() {
        super.init(frame: .zero)
        [title, play, details].forEach { addSubview($0) }
        play.addAction(UIAction { [weak self] _ in
            guard let self, self.play.isEnabled else { return }; self.onPlay()
        }, for: .primaryActionTriggered)
        details.addAction(UIAction { [weak self] _ in
            guard let self, self.details.isEnabled else { return }; self.onDetails()
        }, for: .primaryActionTriggered)
    }
    required init?(coder: NSCoder) { fatalError("Programmatic example") }
    func configure(title text: String, playName: String, detailsName: String,
                   onPlay: @escaping () -> Void, onDetails: @escaping () -> Void) {
        generation += 1
        let revision = generation
        self.onPlay = onPlay; self.onDetails = onDetails
        title.text = text
        play.setTitle(playName, for: .normal); details.setTitle(detailsName, for: .normal)
        isAccessibilityElement = false; accessibilityElementsHidden = true
        title.isAccessibilityElement = true
        play.isAccessibilityElement = true; details.isAccessibilityElement = true
        play.accessibilityLabel = playName; details.accessibilityLabel = detailsName
        play.accessibilityValue = nil; details.accessibilityValue = nil
        play.accessibilityCustomActions = [UIAccessibilityCustomAction(name: detailsName) { [weak self] _ in
            guard let self, self.generation == revision, self.details.isEnabled else { return false }
            self.onDetails(); return true
        }]
    }
    func setSelected(_ selected: Bool) {
        if selected { play.accessibilityTraits.insert(.selected) }
        else { play.accessibilityTraits.remove(.selected) }
    }
    override var preferredFocusEnvironments: [UIFocusEnvironment] {
        [play, details].filter { $0.superview === self && $0.isEnabled && !$0.isHidden && $0.alpha > 0 }
    }
}
