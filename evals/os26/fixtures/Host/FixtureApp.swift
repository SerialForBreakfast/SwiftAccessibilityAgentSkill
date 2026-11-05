// Add to an iOS/tvOS App target with the local OS26Fixtures package linked.
import SwiftUI
import OS26Fixtures
@main
struct FixtureApp: App {
    var body: some Scene { WindowGroup { FixtureHost() } }
}
struct FixtureHost: View {
    @State private var events: [String] = []
    @State private var enabled = false
    @State private var caseNumber = 1
    var body: some View {
        VStack {
#if os(tvOS)
            MovieShelf(movies: (1...8).map {
                Movie(id: "movie-\($0)", title: "Movie \($0)", posterName: "Poster")
            }, open: { events.append("open:\($0.id)") })
#else
            Picker("Case", selection: $caseNumber) {
                ForEach([1, 2, 3, 4, 6], id: \.self) { Text("GP26-0\($0)").tag($0) }
            }
            switch caseNumber {
            case 1: SettingsHost(onChange: { events.append("switch:\($0)") }, onHelp: { events.append("help") })
            case 2: OrderHost()
            case 3: CheckoutHost(onPay: { events.append("pay") })
            case 4:
                ForEach([Message(id: "A", subject: "Alpha"), Message(id: "B", subject: "Bravo")]) { message in
                    MessageRow(message: message, onDelete: { events.append("delete:\($0.id)") })
                }
            default:
                NotificationSettings(notificationsEnabled: $enabled)
                Text("Stored preference: \(enabled ? "on" : "off")")
            }
#endif
            Text("Events: \(events.count)").accessibilityIdentifier("event-count")
            Text(events.joined(separator: ", ")).accessibilityIdentifier("event-log")
            Button("Reset log") { events.removeAll() }
        }.padding()
    }
}
#if os(iOS)
import UIKit
struct SettingsHost: UIViewRepresentable {
    var onChange: (Bool) -> Void
    var onHelp: () -> Void
    func makeUIView(context: Context) -> SettingsRow { SettingsRow(onChange: onChange, onHelp: onHelp) }
    func updateUIView(_ uiView: SettingsRow, context: Context) {}
}
struct CheckoutHost: UIViewRepresentable {
    var onPay: () -> Void
    func makeUIView(context: Context) -> CheckoutSummary {
        CheckoutSummary(formattedTotal: "Gesamtbetrag: 1.234.567,89 EUR", onPay: onPay)
    }
    func updateUIView(_ uiView: CheckoutSummary, context: Context) {}
    func sizeThatFits(_ proposal: ProposedViewSize, uiView: CheckoutSummary, context: Context) -> CGSize? {
        uiView.systemLayoutSizeFitting(CGSize(width: proposal.width ?? 320, height: 0),
            withHorizontalFittingPriority: .required, verticalFittingPriority: .fittingSizeLevel)
    }
}
struct OrderHost: View {
    @State private var priority = true
    var body: some View {
        VStack {
            CellHost(priority: priority)
            Button("Refresh same cell") { priority.toggle() }
        }
    }
}
struct CellHost: UIViewRepresentable {
    var priority: Bool
    func makeUIView(context: Context) -> OrderCell { OrderCell(style: .default, reuseIdentifier: "same") }
    func updateUIView(_ cell: OrderCell, context: Context) {
        cell.configure(Order(customer: priority ? "Alice" : "Bob", status: priority ? "Shipped" : "Processing", isPriority: priority))
    }
}
#endif
