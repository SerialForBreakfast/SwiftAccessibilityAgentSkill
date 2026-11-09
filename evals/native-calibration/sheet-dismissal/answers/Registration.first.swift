import SwiftUI

// In the subject module, intercept just these two registrations. SwiftUI still
// mounts the view's real state. Nothing here manufactures a dismissal ticket.
@MainActor enum Registrations {
    static var open: (() -> Void)?
    static var shown: (Binding<Bool>, () -> Void)?
    static var revision = 0
}
@MainActor func Button(_ title: String, action: @escaping () -> Void) -> SwiftUI.Button<Text> {
    if title == "Open details" { Registrations.open = action }
    return SwiftUI.Button(title, action: action)
}
extension View {
    @MainActor func sheet<S: View>(isPresented: Binding<Bool>, onDismiss: @escaping () -> Void,
                                   @ViewBuilder content: () -> S) -> some View {
        Registrations.revision += 1
        Registrations.shown = (isPresented, onDismiss)
        return self
    }
}
