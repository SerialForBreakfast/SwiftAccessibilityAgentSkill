import UIKit
import AVKit
import AVFoundation

@MainActor
public enum MediaConfiguration {
    public static func controller(player: AVPlayer) -> AVPlayerViewController {
        let controller = AVPlayerViewController()
        controller.player = player
        controller.showsPlaybackControls = true
        controller.requiresLinearPlayback = false
        return controller
    }

    public static func configure(_ button: UIButton, playing: Bool) {
        button.accessibilityTraits.insert(.button)
        button.setTitle(playing ? "Pause" : "Play", for: .normal)
        button.accessibilityLabel = playing ? "Pause" : "Play"
        button.accessibilityValue = playing ? "Playing" : "Paused"
    }

    public static func configureTimeline(_ slider: UISlider, elapsed: Double, duration: Double?) {
        slider.accessibilityLabel = "Playback position"
        guard let duration, duration.isFinite, duration > 0, duration < Double(Int.max), elapsed.isFinite else {
            slider.isEnabled = false
            slider.minimumValue = 0
            slider.maximumValue = 1
            slider.value = 0
            slider.accessibilityValue = "Position unavailable"
            return
        }
        let value = min(max(elapsed, 0), duration)
        slider.isEnabled = true
        slider.minimumValue = 0
        slider.maximumValue = 1
        slider.value = Float(value / duration)
        slider.accessibilityValue = "\(Int(value.rounded())) of \(Int(duration.rounded())) seconds"
    }

    @discardableResult
    public static func select(language: String, in group: AVMediaSelectionGroup, item: AVPlayerItem) -> Bool {
        guard let option = group.options.first(where: {
            $0.locale?.languageCode == language && $0.hasMediaCharacteristic(.containsOnlyForcedSubtitles)
        }) else { return false }
        item.select(option, in: group)
        return true
    }

    public static func selectedLanguage(in group: AVMediaSelectionGroup, item: AVPlayerItem) -> String? {
        item.currentMediaSelection.selectedMediaOption(in: group)?.locale?.languageCode
    }
}
