#if os(iOS)
import SwiftUI
public struct Message: Identifiable {
    public let id: String
    public let subject: String
    public init(id: String, subject: String) { self.id = id; self.subject = subject }
}
public struct MessageRow: View {
    @FocusState private var deleteFocused: Bool
    let message: Message
    let onDelete: (Message) -> Void
    public init(message: Message, onDelete: @escaping (Message) -> Void) {
        self.message = message; self.onDelete = onDelete
    }
    // PATCH BEGIN GP26-04
    public var body: some View {
        HStack {
            Text(message.subject)
                .padding()
                .contentShape(Rectangle())
                .gesture(DragGesture().onEnded { value in
                    if value.translation.width < -80 { onDelete(message) }
                })
            Button("Delete", role: .destructive) { onDelete(message) }
                .accessibilityLabel("Delete \(message.subject)")
                .focused($deleteFocused)
                .onChange(of: deleteFocused) { _, focused in
                    if focused { onDelete(message) }
                }
        }
    }
    // PATCH END GP26-04
}
#endif
