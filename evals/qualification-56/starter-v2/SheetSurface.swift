struct SheetRegistration: ViewModifier {
    let showing: Binding<Bool>
    let onDismiss: () -> Void
    @AccessibilityFocusState private var focused: Bool

    func body(content: Content) -> some View {
        content.sheet(isPresented: showing, onDismiss: onDismiss) {
            Button("Close") { showing.wrappedValue = false }
                .accessibilityFocused($focused)
                .onAppear { focused = true }
        }
    }
}

@MainActor @Observable final class SheetHost {
    let state: PresentationState
    private var currentTicket: Int?
    private(set) var installed: SheetRegistration?
    init(state: PresentationState) { self.state = state }

    @discardableResult
    func present(from origin: String, showing: Binding<Bool>) -> SheetRegistration {
        let ticket = state.begin(from: origin)
        currentTicket = ticket
        let registration = SheetRegistration(showing: showing) { [weak self] in
            guard let self, let closingTicket = self.currentTicket else { return }
            self.state.dismissed(closingTicket)
        }
        installed = registration
        showing.wrappedValue = true
        return registration
    }
}

struct SheetExample: View {
    let host: SheetHost
    @State private var showing = false
    @AccessibilityFocusState private var focus: String?
    var body: some View {
        let open = Button("Open details") { host.present(from: "open", showing: $showing) }
            .accessibilityFocused($focus, equals: "open")
        Group {
            if let installed = host.installed { open.modifier(installed) } else { open }
        }
        .onChange(of: host.state.focus) { _, target in focus = target }
    }
}
