import AVFoundation
import SwiftUI
#if os(macOS)
import AppKit

@MainActor
struct CatalogSearch: NSViewRepresentable {
    static func field() -> NSSearchField {
        let field = NSSearchField()
        field.isEditable = true
        field.setAccessibilityLabel("Catalog search")
        return field
    }
    func makeNSView(context: Context) -> NSSearchField { Self.field() }
    func updateNSView(_ field: NSSearchField, context: Context) {}
}

struct Sidebar: View {
    var body: some View { CatalogSearch() }
}
#endif

@MainActor
final class PlayerControls {
    var playing = false
    var chapter = 0
    func tap() { playing.toggle() }
    func adjust(_ direction: AccessibilityAdjustmentDirection) {
        switch direction {
        case .increment: chapter = min(chapter + 1, 2)
        case .decrement: chapter = max(chapter - 1, 0)
        @unknown default: break
        }
    }
}

struct ChapterSurface: View {
    let controls: PlayerControls
    var body: some View {
        Text("Chapters")
            .onTapGesture(count: 1, perform: controls.tap)
            .accessibilityAdjustableAction(controls.adjust)
    }
}

// An inspector's payload is not required to provide equality.
struct Track { let name: String }
enum Tracks { case unavailable, absent, loaded([Track]) }

func inspect(_ item: AVPlayerItem?) async throws -> Tracks {
    guard let item else { return .unavailable }
    guard let group = try await item.asset.loadMediaSelectionGroup(for: .audible)
    else { return .absent }
    return .loaded(group.options.map { Track(name: $0.displayName) })
}

#if os(macOS)
@main
struct Check {
    @MainActor static func main() async throws {
        let field = CatalogSearch.field()
        precondition(field.isEditable && field.isSelectable)
        field.stringValue = "Rain"
        precondition(field.stringValue == "Rain" && field.accessibilityLabel() == "Catalog search")
        let controls = PlayerControls()
        controls.tap()
        precondition(controls.playing && controls.chapter == 0)
        controls.adjust(.increment)
        precondition(controls.playing && controls.chapter == 1)
        controls.tap()
        precondition(!controls.playing && controls.chapter == 1)
        guard case .unavailable = try await inspect(nil) else { print("missing item"); exit(42) }
        let empty = AVPlayerItem(asset: AVMutableComposition())
        guard case .absent = try await inspect(empty) else { fatalError("absent group") }
    }
}
#endif
