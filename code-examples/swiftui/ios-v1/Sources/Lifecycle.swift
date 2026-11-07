import SwiftUI
import Observation

@MainActor @Observable
final class PresentationState {
    private(set) var showing = false
    private(set) var focus: String?
    private var generation = 0
    private var origin: String?
    var eligible: Set<String> = []
    let fallback = "open"
    var request: (String) -> Void = { _ in }
    @discardableResult func begin(from id: String) -> Int {
        generation += 1; showing = true; origin = id; focus = "close"
        return generation
    }
    func dismissed(_ ticket: Int) {
        guard showing, ticket == generation else { return }
        showing = false
        let target = origin.flatMap { eligible.contains($0) ? $0 : nil } ?? fallback
        focus = target; request(target)
    }
    func cancel(_ ticket: Int) { dismissed(ticket) }
}

struct SheetExample: View {
    @Bindable var state: PresentationState
    @State private var sheet = false
    @State private var ticket: Int?
    @AccessibilityFocusState private var focused: String?
    var body: some View {
        Button("Open details") {
            ticket = state.begin(from: "open"); sheet = true
        }
        .accessibilityFocused($focused, equals: "open")
        .sheet(isPresented: $sheet, onDismiss: {
            if let ticket { state.dismissed(ticket); focused = state.focus }
        }) {
            VStack {
                Text("Details").accessibilityAddTraits(.isHeader)
                Button("Close") { sheet = false }
                    .accessibilityFocused($focused, equals: "close")
            }
            .onAppear { focused = "close" }
        }
    }
}
