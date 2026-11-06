import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class LifecycleUIKitTests: XCTestCase {
    func testInitialMotionReadAndNotificationRefresh() {
        let center = NotificationCenter()
        var preference = false, reads = 0
        let model = MotionPreference(center: center) { reads += 1; return preference }
        XCTAssertFalse(model.reduceMotion)
        XCTAssertEqual(reads, 1)
        preference = true
        center.post(name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
        XCTAssertTrue(model.reduceMotion)
        XCTAssertEqual(reads, 2)
        preference = false
        center.post(name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
        XCTAssertFalse(model.reduceMotion)
        XCTAssertEqual(reads, 3)
    }

    func testUnrelatedNotificationDoesNotReadPreference() {
        let center = NotificationCenter()
        var reads = 0
        let model = MotionPreference(center: center) { reads += 1; return false }
        center.post(name: UIAccessibility.voiceOverStatusDidChangeNotification, object: nil)
        XCTAssertEqual(reads, 1)
        XCTAssertFalse(model.reduceMotion)
    }

    func testStopRemovesObserverAndRestartRefreshes() {
        let center = NotificationCenter()
        var preference = false, reads = 0
        let model = MotionPreference(center: center) { reads += 1; return preference }
        model.stop()
        preference = true
        center.post(name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
        XCTAssertEqual(reads, 1)
        XCTAssertFalse(model.reduceMotion)
        model.start()
        XCTAssertEqual(reads, 2)
        XCTAssertTrue(model.reduceMotion)
        center.post(name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
        XCTAssertEqual(reads, 3)
    }

    func testRepeatedStartDoesNotDuplicateRegistration() {
        let center = NotificationCenter()
        var reads = 0
        let model = MotionPreference(center: center) { reads += 1; return false }
        model.start()
        model.start()
        center.post(name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
        XCTAssertEqual(reads, 2)
    }

    func testObservationDoesNotRetainOwner() {
        let center = NotificationCenter()
        weak var weakModel: MotionPreference?
        var reads = 0
        autoreleasepool {
            let model = MotionPreference(center: center) { reads += 1; return false }
            weakModel = model
            XCTAssertNotNil(weakModel)
        }
        XCTAssertNil(weakModel)
        center.post(name: UIAccessibility.reduceMotionStatusDidChangeNotification, object: nil)
        XCTAssertEqual(reads, 1)
    }

    func testPresentationConfigurationCanRestoreDismissal() {
        let controller = UIViewController()
        PresentationConfiguration.configure(controller, preventDismissal: true)
        XCTAssertEqual(controller.modalPresentationStyle, .formSheet)
        XCTAssertTrue(controller.isModalInPresentation)
        PresentationConfiguration.configure(controller, preventDismissal: false)
        XCTAssertFalse(controller.isModalInPresentation)
        XCTAssertNil(controller.presentingViewController)
        XCTAssertFalse(controller.isViewLoaded)
    }

    func testReadOnlyStateRemovesEditCategoryAndHint() {
        let button = UIButton(type: .system)
        ContextActions.configure(button, editable: true) { _ in true }
        XCTAssertEqual(button.accessibilityCustomActions?.count, 1)
        XCTAssertEqual(button.accessibilityCustomActions?.first?.category, UIAccessibilityCustomAction.editCategory)
        ContextActions.configure(button, editable: false) { _ in true }
        XCTAssertEqual(button.accessibilityCustomActions?.count, 0)
        XCTAssertNil(button.accessibilityHint)
    }

    func testReenabledEditingUsesReplacementHandler() {
        let button = UIButton(type: .system)
        var oldCalls = 0, newCalls = 0
        ContextActions.configure(button, editable: true) { _ in oldCalls += 1; return true }
        ContextActions.configure(button, editable: false) { _ in false }
        ContextActions.configure(button, editable: true) { _ in newCalls += 1; return true }
        let action = button.accessibilityCustomActions![0]
        XCTAssertTrue(action.actionHandler!(action))
        XCTAssertEqual(oldCalls, 0)
        XCTAssertEqual(newCalls, 1)
        XCTAssertNotNil(button.accessibilityHint)
    }
}
