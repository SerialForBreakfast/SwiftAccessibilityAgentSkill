import SwiftUI
import Observation

@MainActor @Observable
final class ListeningSettings {
    private(set) var volume: Double = 0.6
    var normalizeLoudness = true
    let range: ClosedRange<Double> = 0...1
    let step: Double = 0.05
    /// Persists the new volume to the listener's profile.
    var save: (Double) -> Void = { _ in }

    var volumeBinding: Binding<Double> {
        Binding(get: { self.volume }, set: { self.setVolume($0) })
    }

    func setVolume(_ requested: Double) {
        let stepped = (requested / step).rounded() * step
        let next = min(range.upperBound, max(range.lowerBound, stepped))
        guard next != volume else { return }
        volume = next
        save(next)
    }

    // Normalized so VoiceOver reads a percentage instead of a bare number.
    var volumeText: String { volume.formatted(.percent.precision(.fractionLength(0))) }
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
                    Slider(value: settings.volumeBinding, in: settings.range, step: settings.step) {
                        Text("Volume")
                    } minimumValueLabel: {
                        Image(systemName: "speaker.fill")
                    } maximumValueLabel: {
                        Image(systemName: "speaker.wave.3.fill")
                    }
                }
                Toggle("Normalize loudness", isOn: $settings.normalizeLoudness)
            }
        }
        .navigationTitle("Listening")
    }
}
