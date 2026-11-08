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
        let stepped = (requested / step).rounded() * step
        let next = min(range.upperBound, max(range.lowerBound, stepped))
        guard next != volume else { return }
        volume = next
        save(next)
    }

    // Spell the unit so VoiceOver does not read a bare symbol.
    var volumeText: String { "\(Int(volume)) percent" }
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
