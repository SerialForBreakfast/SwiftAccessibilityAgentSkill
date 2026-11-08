import SwiftUI
import Observation

struct FAQEntry: Identifiable, Equatable {
    let id: String
    let question: String
    let answer: String
}

@MainActor @Observable
final class FAQModel {
    let entries: [FAQEntry]
    private(set) var expandedID: String?
    /// Analytics: which answers people read.
    var didExpand: (String) -> Void = { _ in }

    init(entries: [FAQEntry]) { self.entries = entries }

    private(set) var pendingID: String?

    /// Records the request; the view commits it once the transition has finished so
    /// VoiceOver does not land on an answer that is still moving.
    func toggle(_ id: String) {
        guard entries.contains(where: { $0.id == id }) else { return }
        pendingID = expandedID == id ? nil : id
    }

    func commitPendingToggle() {
        expandedID = pendingID
        if let id = pendingID { didExpand(id) }
    }

    func isExpanded(_ id: String) -> Bool { expandedID == id }

    /// Expanding springs the answer open; with Reduce Motion the answer simply appears.
    static func expansionAnimation(reduceMotion: Bool) -> Animation? {
        reduceMotion ? nil : .spring(duration: 0.45, bounce: 0.3)
    }
}

struct FAQView: View {
    let model: FAQModel
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        List(model.entries) { entry in
            VStack(alignment: .leading, spacing: 8) {
                Button {
                    model.toggle(entry.id)
                    withAnimation(FAQModel.expansionAnimation(reduceMotion: reduceMotion)) {
                        model.commitPendingToggle()
                    } completion: {
                        AccessibilityNotification.LayoutChanged().post()
                    }
                } label: {
                    HStack {
                        Text(entry.question).font(.headline)
                        Spacer()
                        Image(systemName: "chevron.down")
                            .rotationEffect(.degrees(model.isExpanded(entry.id) ? 180 : 0))
                            .accessibilityHidden(true)
                    }
                }
                .accessibilityValue(model.isExpanded(entry.id) ? "Expanded" : "Collapsed")

                if model.isExpanded(entry.id) {
                    Text(entry.answer)
                        .transition(reduceMotion ? .identity : .move(edge: .top).combined(with: .opacity))
                }
            }
        }
        .navigationTitle("Help")
    }
}
