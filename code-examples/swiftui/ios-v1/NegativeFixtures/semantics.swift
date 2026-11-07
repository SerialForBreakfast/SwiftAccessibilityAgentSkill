import SwiftUI
import Observation

@MainActor @Observable
final class SettingsState {
    var title = "Downloads"
    private(set) var enabled = false
    private(set) var amount = 50
    private(set) var status = ""
    private(set) var priority = false
    var disabled = false
    var changed: (Bool) -> Void = { _ in }
    var amountChanged: (Int) -> Void = { _ in }
    var help: () -> Void = {}
    var toggle: Binding<Bool> {
        Binding(get: { self.enabled }, set: { value in
            guard !self.disabled else { return }
            self.enabled = value; self.changed(value)
        })
    }
    var value: String { enabled ? "On" : "Off" }
    var name: String { priority ? "\(title), Priority" : title }
    var hint: String { disabled ? "Unavailable while saving" : "" }
    func configure(title: String, status: String, priority: Bool) {
        self.title = title; self.status = status; self.priority = priority
    }
    func openHelp() { guard !disabled else { return }; help() }
    func setAmount(_ requested: Int) {
        guard !disabled else { return }
        let next = min(100, max(0, requested))
        guard next != amount else { return }
        amount = next; amountChanged(next)
    }
    func adjust(_ direction: AccessibilityAdjustmentDirection) {
        switch direction {
        case .increment: setAmount(amount + 5)
        case .decrement: setAmount(amount - 5)
        @unknown default: break
        }
    }
}

struct SettingsExample: View {
    @Bindable var state: SettingsState
    var body: some View {
        HStack {
            Image(decorative: "download-decoration")
            Toggle(state.name, isOn: state.toggle)
            if !state.status.isEmpty { Text(state.status) }
            Button("Help for \(state.title)", action: state.openHelp)
                .accessibilityHint(state.hint)
        }
        .disabled(state.disabled)
        .accessibilityElement(children: .contain)
    }
}

struct AdjustableExample: View {
    @Bindable var state: SettingsState
    var body: some View {
        VStack {
            Text("\(state.amount) percent")
            HStack {
                Button("Decrease volume") { state.adjust(.decrement) }
                Button("Increase volume") { state.adjust(.increment) }
            }
        }
        .accessibilityElement(children: .contain)
        .accessibilityLabel("Volume")
        .accessibilityValue("\(state.amount) percent")
        .accessibilityAdjustableAction(state.adjust)
        .disabled(state.disabled)
    }
}

struct RepresentationExample: View {
    @Bindable var state: SettingsState
    var body: some View {
        Button { state.toggle.wrappedValue.toggle() } label: {
            HStack {
                Circle().fill(state.enabled ? Color.green : Color.gray)
                Text(state.value)
            }
        }
            .accessibilityRepresentation {
                Toggle("Notifications", isOn: state.toggle)
            }
    }
}
