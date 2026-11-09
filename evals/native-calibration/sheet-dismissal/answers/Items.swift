import SwiftUI
@MainActor enum ItemRegistration {
    static var byID: [AnyHashable: () -> Void] = [:]
}
extension View {
    @MainActor func sheet<I: Identifiable, S: View>(item: Binding<I?>, onDismiss: @escaping () -> Void,
                                                    @ViewBuilder content: (I) -> S) -> some View {
        if let instance = item.wrappedValue { ItemRegistration.byID[instance.id] = onDismiss }
        return self
    }
}
