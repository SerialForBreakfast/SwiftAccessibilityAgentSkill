import SwiftUI

@MainActor final class SheetOwner {
    private var active: UUID?
    private let restore: (String) -> Void
    init(restore: @escaping (String) -> Void) { self.restore = restore }

    func presentation(origin: String, showing: Binding<Bool>) -> OwnedSheet {
        let id = UUID()
        active = id
        return OwnedSheet(showing: showing) { [weak self] in
            guard let self, self.active == id else { return }
            self.active = nil
            self.restore(origin)
        }
    }
}

// Keep this modifier with its presentation instance, not in shared mutable callback storage.
struct OwnedSheet: ViewModifier {
    let showing: Binding<Bool>
    let onDismiss: () -> Void
    func body(content: Content) -> some View {
        content.sheet(isPresented: showing, onDismiss: onDismiss) { Text("Editor") }
    }
}
