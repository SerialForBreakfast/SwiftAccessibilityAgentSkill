import UIKit
import AVFoundation

/// Shows the episode that is playing. The player is shared with the Up Next queue and
/// with CarPlay, and either of them can switch episodes without going through this screen.
final class NowPlayingViewController: UIViewController {
    typealias MetadataLoader = (AVPlayerItem, @escaping @MainActor (String) -> Void) -> Void

    let player: AVPlayer
    let titleLabel = UILabel()
    let playPauseButton = UIButton(type: .system)
    private(set) var playItem: AVPlayerItem?
    private let loadTitle: MetadataLoader
    private var requestID = 0

    init(player: AVPlayer, loadTitle: @escaping MetadataLoader) {
        self.player = player
        self.loadTitle = loadTitle
        super.init(nibName: nil, bundle: nil)
    }

    required init?(coder: NSCoder) { fatalError("Programmatic only") }

    override func viewDidLoad() {
        super.viewDidLoad()
        titleLabel.font = .preferredFont(forTextStyle: .title2)
        titleLabel.adjustsFontForContentSizeCategory = true
        titleLabel.numberOfLines = 0
        playPauseButton.setTitle("Play", for: .normal)
        playPauseButton.addTarget(self, action: #selector(togglePlayback), for: .primaryActionTriggered)
        let stack = UIStackView(arrangedSubviews: [titleLabel, playPauseButton])
        stack.axis = .vertical
        stack.spacing = 12
        stack.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(stack)
        NSLayoutConstraint.activate([
            stack.leadingAnchor.constraint(equalTo: view.layoutMarginsGuide.leadingAnchor),
            stack.trailingAnchor.constraint(equalTo: view.layoutMarginsGuide.trailingAnchor),
            stack.centerYAnchor.constraint(equalTo: view.centerYAnchor),
        ])
    }

    /// Starts an episode from this screen.
    func play(_ item: AVPlayerItem) {
        loadViewIfNeeded()
        playItem = item
        player.replaceCurrentItem(with: item)
        titleLabel.text = "Loading episode…"
        titleLabel.accessibilityLabel = nil
        requestID += 1
        let request = requestID
        loadTitle(item) { [weak self] title in
            // Apply only the newest lookup, and only while its item is still the one the shared player has.
            guard let self, request == self.requestID, self.player.currentItem === item else { return }
            self.titleLabel.text = title
            self.titleLabel.accessibilityLabel = "Now playing: \(title)"
        }
    }

    @objc func togglePlayback() {
        if player.rate == 0 {
            player.play()
            playPauseButton.setTitle("Pause", for: .normal)
        } else {
            player.pause()
            playPauseButton.setTitle("Play", for: .normal)
        }
    }
}
