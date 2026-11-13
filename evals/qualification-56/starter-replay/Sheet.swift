import SwiftUI

@MainActor @Observable final class PresentationState {
    var eligible: Set<String> = []
    var request: (String) -> Void = { _ in }
    private(set) var showing = false
    private(set) var focus: String?
    let fallback = "open"
    private var serial = 0
    private var origin = ""
    private(set) var installed: OwnedSheet?
    @ObservationIgnored private lazy var owner = SheetOwner { [weak self] origin in
        guard let self else { return }
        finish(origin)
    }
    private func finish(_ origin: String) {
        showing = false
        let destination = eligible.contains(origin) ? origin : fallback
        focus = destination
        request(destination)
    }
    @discardableResult func begin(from origin: String) -> Int {
        serial += 1
        self.origin = origin
        showing = true
        focus = "close"
        installed = owner.presentation(origin: origin, showing: .constant(true))
        return serial
    }
    // Direct helper calls are not delivery of the installed modifier callback.
    func dismissed(_ ticket: Int) {
        guard showing, ticket == serial else { return }
        finish(origin)
    }
    func cancel(_ ticket: Int) { dismissed(ticket) }
}
struct SheetExample: View {
    @Bindable var state: PresentationState
    var body: some View {
        let open = Button("Open") { state.begin(from: "open") }
        if let installed = state.installed { open.modifier(installed) } else { open }
    }
}
