import UIKit

enum SyncResult {
    case synced(itemCount: Int)
    case failed(reason: String)
}

/// Status strip at the top of the Library tab.
final class SyncStatusView: UIView {
    typealias Fetch = (@escaping @MainActor (SyncResult) -> Void) -> Void

    let statusLabel = UILabel()
    let retryButton = UIButton(type: .system)
    private(set) var retryCount = 0
    private let fetch: Fetch
    private var activeToken: NSObject?

    init(fetch: @escaping Fetch) {
        self.fetch = fetch
        super.init(frame: .zero)
        statusLabel.font = .preferredFont(forTextStyle: .subheadline)
        statusLabel.adjustsFontForContentSizeCategory = true
        statusLabel.numberOfLines = 0
        retryButton.setTitle("Retry", for: .normal)
        retryButton.addTarget(self, action: #selector(retry), for: .primaryActionTriggered)
        retryButton.isHidden = true
        let row = UIStackView(arrangedSubviews: [statusLabel, retryButton])
        row.spacing = 8
        row.alignment = .firstBaseline
        row.translatesAutoresizingMaskIntoConstraints = false
        addSubview(row)
        NSLayoutConstraint.activate([
            row.leadingAnchor.constraint(equalTo: layoutMarginsGuide.leadingAnchor),
            row.trailingAnchor.constraint(equalTo: layoutMarginsGuide.trailingAnchor),
            row.topAnchor.constraint(equalTo: layoutMarginsGuide.topAnchor),
            row.bottomAnchor.constraint(equalTo: layoutMarginsGuide.bottomAnchor),
        ])
    }

    required init?(coder: NSCoder) { fatalError("Programmatic only") }

    /// Called on pull-to-refresh, on foregrounding, and from Retry.
    func refresh() {
        let token = NSObject()
        activeToken = token
        statusLabel.text = "Checking for changes…"
        fetch { [weak self, weak token] result in
            guard let self, let token, token === self.activeToken else { return }
            self.activeToken = nil
            self.apply(result)
        }
    }

    private func apply(_ result: SyncResult) {
        let failure: String?
        switch result {
        case .synced(let count):
            statusLabel.text = "Up to date"
            statusLabel.accessibilityLabel = "Up to date, \(count) items"
            failure = nil
        case .failed(let reason):
            statusLabel.text = "Sync failed"
            statusLabel.accessibilityLabel = "Sync failed: \(reason)"
            failure = reason
        }
        statusLabel.accessibilityValue = nil
        retryButton.isHidden = failure == nil
        retryButton.accessibilityHint = failure == nil ? nil : "Tries the sync again."
    }

    @objc func retry() {
        retryCount += 1
        refresh()
    }
}
