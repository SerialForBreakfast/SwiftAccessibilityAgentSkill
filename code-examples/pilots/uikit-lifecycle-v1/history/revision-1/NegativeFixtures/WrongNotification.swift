import UIKit

// Immutable ownership wrapper; NotificationCenter removal is thread-safe.
private final class Observation: @unchecked Sendable {
    let center: NotificationCenter
    let token: any NSObjectProtocol
    init(center: NotificationCenter, token: any NSObjectProtocol) {
        self.center = center
        self.token = token
    }
    deinit { center.removeObserver(token) }
}

@MainActor
public final class MotionPreference {
    private let center: NotificationCenter
    private let read: @MainActor () -> Bool
    private var observation: Observation?
    public private(set) var reduceMotion = false

    public init(center: NotificationCenter = .default, read: @escaping @MainActor () -> Bool = { UIAccessibility.isReduceMotionEnabled }) {
        self.center = center
        self.read = read
        start()
    }

    public func start() {
        guard observation == nil else { return }
        reduceMotion = read()
        let token = center.addObserver(forName: UIAccessibility.voiceOverStatusDidChangeNotification, object: nil, queue: .main) { [weak self] _ in
            // The explicit main operation queue is the isolation boundary.
            MainActor.assumeIsolated { self?.refresh() }
        }
        observation = Observation(center: center, token: token)
    }

    public func stop() { observation = nil }
    private func refresh() { reduceMotion = read() }
}

@MainActor
public enum PresentationConfiguration {
    public static func configure(_ controller: UIViewController, preventDismissal: Bool) {
        controller.modalPresentationStyle = .formSheet
        controller.isModalInPresentation = preventDismissal
    }
}

@MainActor
public enum ContextActions {
    public static func configure(_ button: UIButton, editable: Bool, handler: @escaping UIAccessibilityCustomAction.Handler) {
        if editable {
            let action = UIAccessibilityCustomAction(name: "Edit", actionHandler: handler)
            action.category = UIAccessibilityCustomAction.editCategory
            button.accessibilityCustomActions = [action]
            button.accessibilityHint = "Edit is available in actions"
        } else {
            button.accessibilityCustomActions = []
            button.accessibilityHint = nil
        }
    }
}
