import XCTest
@testable import YourAppModule

@MainActor final class SheetReplay: XCTestCase {
    func testReturnToSurvivingOrigin() {
        let model = PresentationCoordinator()
        let item = Item(id: "existing", title: "Existing")
        model.openSheet(for: item)
        let ticket = model.activeGeneration
        model.requestDismissal()
        var restored: [FocusField] = []
        XCTAssertTrue(model.resolveDismissalCompletion(generation: ticket, availableItems: [item]) { restored.append($0) })
        XCTAssertEqual(restored, [.item(item.id)], "eligible origin survives dismissal")
    }
}
