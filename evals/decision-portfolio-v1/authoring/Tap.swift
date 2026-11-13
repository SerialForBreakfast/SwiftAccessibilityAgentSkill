import SwiftUI

@MainActor final class Transport: ObservableObject {
    @Published private(set) var playing = false
    @Published private(set) var cue = 0
    func activate() { playing.toggle() }
    func step(_ direction: AccessibilityAdjustmentDirection) {
        switch direction {
        case .increment: cue = min(3, cue + 1)
        case .decrement: cue = max(0, cue - 1)
        @unknown default: break
        }
    }
}

struct CuePad: View {
    @ObservedObject var transport: Transport
    let seek: (CGFloat) -> Void
    var body: some View {
        Text("Cue \(transport.cue + 1)")
            .contentShape(Rectangle())
            .onTapGesture { transport.activate() }
            .simultaneousGesture(DragGesture(minimumDistance: 12).onChanged { seek($0.location.x) })
            .accessibilityAdjustableAction(transport.step)
    }
}
