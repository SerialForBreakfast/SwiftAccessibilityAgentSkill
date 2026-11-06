import UIKit

@MainActor
final class RestoringPanel: UIView {
    enum State: Equatable { case closed, open, closing }
    let heading = UILabel()
    let primary = UIButton(type: .system)
    let close = UIButton(type: .system)
    private(set) var state: State = .closed
    var canDismiss = true
    var onPrimary: () -> Void = {}
    var performDismissal: (@escaping @MainActor () -> Void) -> Void = { completion in completion() }
    var post: (UIAccessibility.Notification, Any?) -> Void = { UIAccessibility.post(notification: $0, argument: $1) }
    weak var returnTarget: UIView?
    private weak var background: UIView?
    private var priorHidden = false
    private var generation = 0

    override init(frame: CGRect) {
        super.init(frame: frame)
        [heading, primary, close].forEach(addSubview)
        isAccessibilityElement = false
        isHidden = true
        accessibilityElementsHidden = true
        primary.addAction(UIAction { [weak self] _ in
            guard let self, self.state == .open, self.primary.isEnabled else { return }
            self.onPrimary()
        }, for: .touchUpInside)
        close.addAction(UIAction { [weak self] _ in _ = self?.dismiss() }, for: .touchUpInside)
    }

    required init?(coder: NSCoder) { fatalError("init(coder:) is not supported") }

    @discardableResult
    func open(background: UIView, target: UIView?, title: String, primaryTitle: String, closeTitle: String) -> Bool {
        // Hide only the separate background subtree, never an ancestor containing the panel.
        guard state == .closed, background !== self,
              !isDescendant(of: background), !background.isDescendant(of: self) else { return false }
        generation += 1
        self.background = background
        priorHidden = background.accessibilityElementsHidden
        returnTarget = target
        background.accessibilityElementsHidden = true
        heading.text = title
        heading.isAccessibilityElement = true
        heading.accessibilityTraits.insert(.header)
        primary.setTitle(primaryTitle, for: .normal)
        close.setTitle(closeTitle, for: .normal)
        primary.isAccessibilityElement = true
        close.isAccessibilityElement = true
        accessibilityElements = [heading, primary, close]
        isHidden = false
        accessibilityElementsHidden = false
        accessibilityViewIsModal = true
        state = .open
        return true
    }

    @discardableResult
    func dismiss() -> Bool {
        guard state == .open, canDismiss else { return false }
        state = .closing
        post(.screenChanged, returnTarget)
        let token = generation
        performDismissal { [weak self] in
            guard let self, self.state == .closing, self.generation == token else { return }
            self.finish(notify: true)
        }
        return true
    }

    private func finish(notify: Bool) {
        let target = returnTarget
        background?.accessibilityElementsHidden = priorHidden
        background = nil
        returnTarget = nil
        state = .closed
        isHidden = true
        accessibilityElementsHidden = true
        accessibilityViewIsModal = false
        onPrimary = {}
        if notify { post(.screenChanged, target) }
    }

    /// Owner calls before discarding the panel, even if dismissal has not completed.
    func tearDown() {
        guard state != .closed else { return }
        generation += 1
        finish(notify: false)
    }

    override func accessibilityPerformEscape() -> Bool { dismiss() }
}
