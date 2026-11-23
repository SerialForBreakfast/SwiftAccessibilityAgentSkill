// The non-discriminating tests each recipe warns about. Each must PASS on its defect.
import AVFoundation
import XCTest
#if canImport(UIKit)
import UIKit
#endif
@testable import Q

@MainActor final class WrongTests: XCTestCase {
#if canImport(UIKit)
    func testWrong_callbacks() {                 // press only the current control
        let subject = Binder(), button = UIButton(type: .system)
        var log: [String] = []
        subject.bind(button) { log.append("A") }
        subject.bind(button) { log.append("B") }
        button.sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(log, ["B"])
    }
    func testWrong_late() {                      // old reply without changing the field
        let field = UITextField(); field.text = "a@example.com"
        let form = SignupForm(field: field)
        let reply = form.submit()
        reply(.failure(.taken))
        XCTAssertFalse(form.isBusy)
    }
#endif
    func testWrong_observer() {                  // drain without changing the value
        let source = FakePreferenceSource(), screen = PreferenceScreen(source: source)
        screen.start()
        source.value = true; source.queue()
        screen.stop(); screen.start()
        source.drainFirst()
        XCTAssertEqual(screen.applied, [])
    }
    func testWrong_dismissal() {                 // only one presentation
        var restored: [String] = []
        let coordinator = ReturnCoordinator { restored.append($0) }
        let dismiss = coordinator.open(origin: "rowA")
        dismiss()
        XCTAssertEqual(restored, ["rowA"])
    }
#if !os(tvOS)
    func testWrong_media() async throws {        // assert the picker's own value
        let (item, _, _) = try await makeMediaItem()
        let store = CaptionStore(player: AVPlayer(playerItem: item))
        try await store.load()
        store.selection.wrappedValue = store.choices[1].id
        XCTAssertEqual(store.selectedID, store.choices[1].id)
    }
#endif
}
