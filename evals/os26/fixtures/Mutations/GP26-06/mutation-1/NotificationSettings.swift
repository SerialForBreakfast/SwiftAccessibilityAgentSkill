#if os(iOS)
import SwiftUI
public struct NotificationSettings: View {
    @Binding var notificationsEnabled: Bool
    public init(notificationsEnabled: Binding<Bool>) { _notificationsEnabled = notificationsEnabled }
    // PATCH BEGIN GP26-06
    var toggleBinding: Binding<Bool> { .constant(false) }
    public var body: some View {
        Form {
            Toggle("Notifications", isOn: toggleBinding)
        }
    }
    // PATCH END GP26-06
}
#endif
