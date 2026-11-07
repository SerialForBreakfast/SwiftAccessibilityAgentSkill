import SwiftUI
import Observation

@MainActor @Observable final class SurfaceStore {
    var snapshot = SurfaceSnapshot()
    var reducedMotion = false
    var reduceTransparency = false
    var events: [String] = []
    var input: Binding<String> { Binding(get: { self.snapshot.title }, set: { self.snapshot.title = $0 }) }
    var opacity: Double { reduceTransparency ? 1 : 0.5 }
    func setSelected(_ selected: Bool, animate: () -> Void) {
        guard snapshot.selected != selected else { return }
        snapshot.selected = selected; events.append(snapshot.value)
        animate()
    }
}
struct ForwardingExample: View {
    @Bindable var store: SurfaceStore
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @Environment(\.accessibilityReduceTransparency) private var reduceTransparency
    let perform: (String, Bool) -> Void
    var body: some View {
        VStack {
            TextField("Report name", text: store.input)
            SurfaceExample(snapshot: store.snapshot, perform: perform)
            Button("Change selection") { store.reducedMotion = reduceMotion; store.setSelected(!store.snapshot.selected, animate: {}) }
        }
        .background(.background.opacity(reduceTransparency ? 1 : 0.5))
    }
}
