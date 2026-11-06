import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class ModalUIKitTests: XCTestCase {
    @discardableResult
    private func open(_ panel: RestoringPanel, background: UIView, target: UIView? = nil) -> Bool {
        panel.open(background: background, target: target, title: "Delivery options", primaryTitle: "Apply", closeTitle: "Cancel")
    }

    func testOpenExposesHeadingAndIndependentButtons() {
        let panel = RestoringPanel(), background = UIView()
        XCTAssertTrue(open(panel, background: background))
        XCTAssertTrue(panel.accessibilityViewIsModal)
        XCTAssertFalse(panel.isHidden)
        XCTAssertFalse(panel.isAccessibilityElement)
        XCTAssertFalse(panel.accessibilityElementsHidden)
        XCTAssertEqual(panel.heading.text, "Delivery options")
        XCTAssertTrue(panel.heading.accessibilityTraits.contains(.header))
        XCTAssertTrue(panel.primary.isAccessibilityElement)
        XCTAssertTrue(panel.close.isAccessibilityElement)
        XCTAssertEqual(panel.primary.title(for: .normal), "Apply")
        XCTAssertEqual(panel.close.title(for: .normal), "Cancel")
        let elements = panel.accessibilityElements as? [UIView]
        XCTAssertEqual(elements?.count, 3)
        XCTAssertTrue(elements?[0] === panel.heading)
        XCTAssertTrue(elements?[1] === panel.primary)
        XCTAssertTrue(elements?[2] === panel.close)
        XCTAssertTrue(background.accessibilityElementsHidden)
        panel.tearDown()
    }

    func testBackgroundRestoresBothOriginalValues() {
        for hidden in [false, true] {
            let panel = RestoringPanel(), background = UIView()
            panel.post = { _, _ in }
            background.accessibilityElementsHidden = hidden
            XCTAssertTrue(open(panel, background: background))
            XCTAssertTrue(panel.dismiss())
            XCTAssertEqual(background.accessibilityElementsHidden, hidden)
            XCTAssertEqual(panel.state, .closed)
            XCTAssertTrue(panel.isHidden)
            XCTAssertTrue(panel.accessibilityElementsHidden)
            XCTAssertFalse(panel.accessibilityViewIsModal)
        }
    }

    func testNotificationWaitsForCompletionAndUsesCurrentTarget() {
        let panel = RestoringPanel(), background = UIView(), first = UIButton(), replacement = UIButton()
        var completion: (@MainActor () -> Void)?, posts = 0
        panel.performDismissal = { completion = $0 }
        panel.post = { notification, target in
            posts += 1
            XCTAssertEqual(notification, .screenChanged)
            XCTAssertTrue((target as? UIView) === replacement)
            XCTAssertFalse(background.accessibilityElementsHidden)
            XCTAssertEqual(panel.state, .closed)
        }
        XCTAssertTrue(open(panel, background: background, target: first))
        XCTAssertTrue(panel.dismiss())
        XCTAssertEqual(posts, 0)
        XCTAssertTrue(background.accessibilityElementsHidden)
        panel.returnTarget = replacement
        completion?()
        completion?()
        XCTAssertEqual(posts, 1)
        XCTAssertNil(panel.returnTarget)
        panel.post = { _, _ in }
    }

    func testOrdinaryCloseAndEscapeShareDismissalGuard() {
        let panel = RestoringPanel(), background = UIView()
        var starts = 0, completion: (@MainActor () -> Void)?
        panel.performDismissal = { starts += 1; completion = $0 }
        panel.post = { _, _ in }
        XCTAssertTrue(open(panel, background: background))
        panel.canDismiss = false
        panel.close.sendActions(for: .touchUpInside)
        XCTAssertFalse(panel.accessibilityPerformEscape())
        XCTAssertEqual(starts, 0)
        panel.canDismiss = true
        panel.close.sendActions(for: .touchUpInside)
        XCTAssertEqual(starts, 1)
        XCTAssertFalse(panel.accessibilityPerformEscape())
        XCTAssertEqual(starts, 1)
        completion?()
        XCTAssertFalse(panel.dismiss())
    }

    func testEscapeCanInitiateDismissal() {
        let panel = RestoringPanel(), background = UIView()
        var posts = 0
        panel.post = { _, _ in posts += 1 }
        XCTAssertTrue(open(panel, background: background))
        XCTAssertTrue(panel.accessibilityPerformEscape())
        XCTAssertEqual(panel.state, .closed)
        XCTAssertEqual(posts, 1)
    }

    func testPrimaryActionDoesNotDismissAndIsSuppressedWhileClosing() {
        let panel = RestoringPanel(), background = UIView()
        var operations = 0
        panel.onPrimary = { operations += 1 }
        panel.performDismissal = { _ in }
        XCTAssertTrue(open(panel, background: background))
        panel.primary.sendActions(for: .touchUpInside)
        XCTAssertEqual(operations, 1)
        XCTAssertEqual(panel.state, .open)
        panel.primary.isEnabled = false
        panel.primary.sendActions(for: .touchUpInside)
        XCTAssertEqual(operations, 1)
        panel.primary.isEnabled = true
        XCTAssertTrue(panel.dismiss())
        panel.primary.sendActions(for: .touchUpInside)
        XCTAssertEqual(operations, 1)
        panel.tearDown()
    }

    func testOpenWhileActiveDoesNotOverwriteSnapshot() {
        let panel = RestoringPanel(), first = UIView(), second = UIView()
        first.accessibilityElementsHidden = true
        XCTAssertTrue(open(panel, background: first))
        XCTAssertFalse(open(panel, background: second))
        XCTAssertFalse(second.accessibilityElementsHidden)
        panel.performDismissal = { _ in }
        XCTAssertTrue(panel.dismiss())
        XCTAssertFalse(open(panel, background: second))
        panel.tearDown()
        XCTAssertTrue(first.accessibilityElementsHidden)
    }

    func testOldCompletionCannotCloseReopenedPanel() {
        let panel = RestoringPanel(), background = UIView()
        var completions: [@MainActor () -> Void] = [], posts = 0
        panel.performDismissal = { completions.append($0) }
        panel.post = { _, _ in posts += 1 }
        XCTAssertTrue(open(panel, background: background))
        XCTAssertTrue(panel.dismiss())
        panel.tearDown()
        XCTAssertFalse(background.accessibilityElementsHidden)
        XCTAssertTrue(open(panel, background: background))
        XCTAssertTrue(panel.dismiss())
        XCTAssertEqual(completions.count, 2)
        completions[0]()
        XCTAssertEqual(panel.state, .closing)
        XCTAssertTrue(background.accessibilityElementsHidden)
        XCTAssertEqual(posts, 0)
        completions[1]()
        XCTAssertEqual(posts, 1)
        XCTAssertEqual(panel.state, .closed)
    }

    func testReleasedTargetIsNotRetainedAndPostsNil() {
        let panel = RestoringPanel(), background = UIView()
        var completion: (@MainActor () -> Void)?, posts = 0
        weak var weakTarget: UIView?
        panel.performDismissal = { completion = $0 }
        panel.post = { _, target in posts += 1; XCTAssertNil(target) }
        autoreleasepool {
            let target = UIView()
            weakTarget = target
            XCTAssertTrue(open(panel, background: background, target: target))
        }
        XCTAssertNil(weakTarget)
        XCTAssertTrue(panel.dismiss())
        completion?()
        XCTAssertEqual(posts, 1)
    }

    func testTeardownIsIdempotentAndAllowsNewContent() {
        let panel = RestoringPanel(), first = UIView(), second = UIView()
        var posts = 0, staleOperations = 0
        panel.post = { _, _ in posts += 1 }
        panel.onPrimary = { staleOperations += 1 }
        XCTAssertTrue(open(panel, background: first))
        panel.tearDown()
        panel.tearDown()
        XCTAssertEqual(posts, 0)
        XCTAssertFalse(first.accessibilityElementsHidden)
        XCTAssertTrue(panel.open(background: second, target: nil, title: "Review", primaryTitle: "Confirm", closeTitle: "Back"))
        XCTAssertEqual(panel.heading.text, "Review")
        XCTAssertEqual(panel.primary.title(for: .normal), "Confirm")
        panel.primary.sendActions(for: .touchUpInside)
        XCTAssertEqual(staleOperations, 0)
        panel.tearDown()
    }

    func testRejectsBackgroundContainingPanel() {
        let parent = UIView(), panel = RestoringPanel()
        parent.addSubview(panel)
        XCTAssertFalse(open(panel, background: parent))
        XCTAssertFalse(parent.accessibilityElementsHidden)
        XCTAssertEqual(panel.state, .closed)
        XCTAssertFalse(open(panel, background: panel))
        XCTAssertFalse(open(panel, background: panel.heading))
    }
}
