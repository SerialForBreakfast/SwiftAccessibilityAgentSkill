import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class TelevisionShelvesTests: XCTestCase {
    typealias Section = TelevisionShelves.Section
    typealias Item = TelevisionShelves.Item
    typealias Key = TelevisionShelves.Key
    private func sections() -> [Section] { [Section(id: "s1", title: "Featured", items: [Item(id: "a", title: "Alpha"), Item(id: "b", title: "Beta")]), Section(id: "s2", title: "Recent", items: [Item(id: "a", title: "Again")])] }
    private func configured() -> TelevisionShelves { let v = TelevisionShelves(); XCTAssertTrue(v.apply(sections())); return v }
    func testShelvesPreserveIndependentHeadingAndButtons() {
        let v = configured(), shelf = v.shelves[0]
        XCTAssertFalse(v.isAccessibilityElement); XCTAssertFalse(shelf.isAccessibilityElement)
        XCTAssertTrue(shelf.heading.isAccessibilityElement); XCTAssertTrue(shelf.heading.accessibilityTraits.contains(.header))
        XCTAssertEqual(shelf.heading.text, "Featured")
        XCTAssertEqual(shelf.buttons.map { $0.title(for: .normal) }, ["Alpha", "Beta"])
        XCTAssertEqual(shelf.buttons.map(\.accessibilityLabel), ["Alpha", "Beta"])
    }
    func testExplicitContainerOrderMatchesHierarchy() {
        let v = configured(), shelf = v.shelves[0]
        XCTAssertTrue((v.accessibilityElements?.first as? UIView) === shelf)
        XCTAssertEqual(v.accessibilityElements?.count, 2)
        XCTAssertTrue((shelf.accessibilityElements?.first as? UILabel) === shelf.heading)
        XCTAssertTrue((shelf.accessibilityElements?[1] as? UIButton) === shelf.buttons[0])
        XCTAssertTrue((shelf.accessibilityElements?[2] as? UIButton) === shelf.buttons[1])
    }
    func testSameItemIDInDifferentSectionsRemainsDistinct() {
        let v = configured(); v.select(Key(section: "s2", item: "a"))
        XCTAssertEqual(v.keys.count, 3)
        XCTAssertFalse(v.shelves[0].buttons[0].accessibilityTraits.contains(.selected))
        XCTAssertTrue(v.shelves[1].buttons[0].accessibilityTraits.contains(.selected))
    }
    func testDuplicateSectionIDsRejectedAtomically() {
        let v = configured(), old = v.shelves[0]
        XCTAssertFalse(v.apply([Section(id: "same", title: "One", items: []), Section(id: "same", title: "Two", items: [])]))
        XCTAssertTrue(v.shelves[0] === old); XCTAssertEqual(v.keys.count, 3)
    }
    func testDuplicateItemIDsWithinSectionRejected() {
        let v = configured()
        XCTAssertFalse(v.apply([Section(id: "new", title: "New", items: [Item(id: "x", title: "One"), Item(id: "x", title: "Two")])]))
        XCTAssertEqual(v.shelves.count, 2)
    }
    func testOrdinaryButtonSelectsAndCallsCurrentAction() {
        let v = configured(); var chosen: [Key] = []; v.onChoose = { chosen.append($0) }
        v.shelves[0].buttons[1].sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(chosen, [Key(section: "s1", item: "b")]); XCTAssertEqual(v.selected, chosen.first)
    }
    func testDisabledButtonDoesNotChoose() {
        let v = configured(); var calls = 0; v.onChoose = { _ in calls += 1 }
        let b = v.shelves[0].buttons[0]; b.isEnabled = false; b.sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, 0); XCTAssertNil(v.selected)
    }
    func testOldGenerationRejectedEvenWhenButtonReattached() {
        let v = configured(), old = v.shelves[0].buttons[0]
        var calls = 0; v.onChoose = { _ in calls += 1 }
        XCTAssertTrue(v.apply(sections())); v.addSubview(old)
        old.sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, 0); XCTAssertNil(v.selected)
    }
    func testDetachedCurrentButtonCannotChoose() {
        let v = configured(), b = v.shelves[0].buttons[0]
        var calls = 0; v.onChoose = { _ in calls += 1 }
        b.removeFromSuperview(); b.sendActions(for: .primaryActionTriggered)
        XCTAssertEqual(calls, 0); XCTAssertNil(v.selected)
    }
    func testReplacingSectionsDetachesOldShelves() {
        let v = configured(), old = v.shelves[0]
        XCTAssertTrue(v.apply([Section(id: "new", title: "New", items: [])]))
        XCTAssertNil(old.superview); XCTAssertEqual(v.subviews.count, 1)
    }
    func testSelectionSurvivesSectionReorder() {
        let v = configured(), key = Key(section: "s1", item: "b")
        v.select(key); XCTAssertTrue(v.apply(Array(sections().reversed())))
        XCTAssertEqual(v.selected, key); XCTAssertTrue(v.shelves[1].buttons[1].accessibilityTraits.contains(.selected))
    }
    func testRemovedSelectionClears() {
        let v = configured(); v.select(Key(section: "s1", item: "a"))
        XCTAssertTrue(v.apply([Section(id: "new", title: "New", items: [])]))
        XCTAssertNil(v.selected)
    }
    func testSameItemMovedToOtherSectionDoesNotStealSelection() {
        let v = configured(); v.select(Key(section: "s1", item: "a"))
        XCTAssertTrue(v.apply([Section(id: "s2", title: "Recent", items: [Item(id: "a", title: "Again")])]))
        XCTAssertNil(v.selected)
    }
    func testSelectionPreservesUnrelatedTraits() {
        let v = configured(), b = v.shelves[0].buttons[0]
        b.accessibilityTraits.insert(.startsMediaSession)
        v.select(Key(section: "s1", item: "a")); v.select(nil)
        XCTAssertTrue(b.accessibilityTraits.contains(.startsMediaSession)); XCTAssertFalse(b.accessibilityTraits.contains(.selected))
    }
    func testEmptySectionKeepsHeadingAndNoActions() {
        let v = TelevisionShelves()
        XCTAssertTrue(v.apply([Section(id: "empty", title: "No results", items: [])]))
        XCTAssertEqual(v.shelves[0].accessibilityElements?.count, 1)
        XCTAssertEqual(v.shelves[0].heading.text, "No results"); XCTAssertTrue(v.keys.isEmpty)
    }
    func testRepeatedConfigurationDoesNotAccumulateChildren() {
        let v = configured(); XCTAssertTrue(v.apply(sections())); XCTAssertTrue(v.apply(sections()))
        XCTAssertEqual(v.subviews.count, 2); XCTAssertEqual(v.shelves[0].subviews.count, 3)
    }
    func testRetainedButtonDoesNotRetainOwner() {
        var v: TelevisionShelves? = configured(); weak var weakView = v
        let button = v!.shelves[0].buttons[0]; v = nil
        XCTAssertNil(weakView); button.sendActions(for: .primaryActionTriggered)
    }
}
