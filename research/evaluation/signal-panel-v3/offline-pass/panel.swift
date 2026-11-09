import XCTest
import UIKit
@testable import YourAppModule

@MainActor final class PanelReplay: XCTestCase {
    func testReopenRestoresBackground() throws {
        let background = UIView()
        var finishes = [() -> Void]()
        let panel = CustomActionPanelController(backgroundContainer: background,
            dismissAnimator: { _, done in finishes.append(done) }, notificationSender: { _, _ in })
        background.accessibilityElementsHidden = false
        panel.present(from: nil)
        panel.dismiss()
        panel.present(from: nil)
        panel.dismiss()
        XCTAssertEqual(finishes.count, 2)
        try XCTUnwrap(finishes.first)()
        XCTAssertTrue(background.accessibilityElementsHidden)
        try XCTUnwrap(finishes.last)()
        XCTAssertFalse(background.accessibilityElementsHidden, "final dismissal restores original background")
    }
    func testApplyAttached() {
        let panel = CustomActionPanelController()
        XCTAssertTrue(panel.applyButton.isDescendant(of: panel.panelView), "ordinary Apply is attached")
    }
}
