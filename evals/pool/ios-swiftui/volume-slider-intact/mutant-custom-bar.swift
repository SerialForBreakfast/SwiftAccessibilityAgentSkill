import SwiftUI
import Observation

@MainActor @Observable
final class ListeningSettings {
    private(set) var volume: Double = 60
    var normalizeLoudness = true
    let range: ClosedRange<Double> = 0...100
    let step: Double = 5
    /// Persists the new volume to the listener's profile.
    var save: (Double) -> Void = { _ in }

    var volumeBinding: Binding<Double> {
        Binding(get: { self.volume }, set: { self.setVolume($0) })
    }

    func setVolume(_ requested: Double) {
        volume = min(range.upperBound, max(range.lowerBound, requested))
        save(volume)
    }

    func adjust(_ direction: AccessibilityAdjustmentDirection) {
        switch direction {
        case .increment: setVolume(volume + 1)
        case .decrement: setVolume(volume - 1)
        @unknown default: break
        }
    }

    var volumeText: String { "\(Int(volume))%" }
}

struct ListeningSettingsView: View {
    @Bindable var settings: ListeningSettings

    var body: some View {
        Form {
            Section("Playback") {
                VStack(alignment: .leading, spacing: 8) {
                    HStack {
                        Text("Volume")
                        Spacer()
                        Text(settings.volumeText)
                            .monospacedDigit()
                            .foregroundStyle(.secondary)
                    }
                    GeometryReader { proxy in
                        Capsule()
                            .fill(.quaternary)
                            .overlay(alignment: .leading) {
                                Capsule().fill(.tint)
                                    .frame(width: proxy.size.width * settings.volume / 100)
                            }
                            .gesture(DragGesture(minimumDistance: 0).onChanged { value in
                                settings.setVolume(value.location.x / proxy.size.width * 100)
                            })
                    }
                    .frame(height: 8)
                    .accessibilityElement()
                    .accessibilityLabel("Volume")
                    .accessibilityValue(settings.volumeText)
                    .accessibilityAdjustableAction { settings.adjust($0) }
                }
                Toggle("Normalize loudness", isOn: $settings.normalizeLoudness)
            }
        }
        .navigationTitle("Listening")
    }
}
