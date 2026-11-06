import XCTest
import UIKit
@testable import AccessibilityExamples

@MainActor
final class ContainerUIKitTests: XCTestCase {
    func testEmptyGridDeclaresContainerAndDimensions() {
        let grid = DataGrid(rows: 3, columns: 2)
        XCTAssertFalse(grid.isAccessibilityElement)
        XCTAssertEqual(grid.accessibilityContainerType, .dataTable)
        XCTAssertEqual(grid.accessibilityRowCount(), 3)
        XCTAssertEqual(grid.accessibilityColumnCount(), 2)
        XCTAssertEqual(grid.accessibilityElements?.count, 0)
        XCTAssertNil(grid.accessibilityDataTableCellElement(forRow: 0, column: 0))
    }

    func testSpanningCellResolvesEveryCoveredCoordinate() {
        let grid = DataGrid(rows: 3, columns: 3)
        XCTAssertTrue(grid.insert(label: "Combined", rows: NSRange(location: 1, length: 2), columns: NSRange(location: 0, length: 2)))
        let cell = grid.cells[0]
        XCTAssertEqual(cell.accessibilityRowRange(), NSRange(location: 1, length: 2))
        XCTAssertEqual(cell.accessibilityColumnRange(), NSRange(location: 0, length: 2))
        for row in 1...2 {
            for column in 0...1 {
                XCTAssertTrue((grid.accessibilityDataTableCellElement(forRow: row, column: column) as? DataCell) === cell)
            }
        }
        XCTAssertNil(grid.accessibilityDataTableCellElement(forRow: 0, column: 0))
        XCTAssertNil(grid.accessibilityDataTableCellElement(forRow: 1, column: 2))
    }

    func testInvalidCoordinatesReturnNil() {
        let grid = DataGrid(rows: 1, columns: 1)
        for (row, column) in [(-1, 0), (0, -1), (1, 0), (0, 1), (Int.max, Int.max)] {
            XCTAssertNil(grid.accessibilityDataTableCellElement(forRow: row, column: column))
        }
    }

    func testInvalidRangesLeaveContainerUnchanged() {
        let grid = DataGrid(rows: 2, columns: 2)
        for range in [NSRange(location: -1, length: 1), NSRange(location: 0, length: 0), NSRange(location: 1, length: 2), NSRange(location: NSNotFound, length: 1), NSRange(location: 0, length: Int.max)] {
            XCTAssertFalse(grid.insert(label: "Invalid", rows: range, columns: NSRange(location: 0, length: 1)))
            XCTAssertFalse(grid.insert(label: "Invalid", rows: NSRange(location: 0, length: 1), columns: range))
        }
        XCTAssertTrue(grid.cells.isEmpty)
        XCTAssertEqual(grid.accessibilityElements?.count, 0)
    }

    func testOverlapRejectedWithoutReplacingExistingCell() {
        let grid = DataGrid(rows: 2, columns: 2)
        XCTAssertTrue(grid.insert(label: "Original", rows: NSRange(location: 0, length: 2), columns: NSRange(location: 0, length: 1)))
        let original = grid.cells[0]
        XCTAssertFalse(grid.insert(label: "Overlap", rows: NSRange(location: 1, length: 1), columns: NSRange(location: 0, length: 2)))
        XCTAssertEqual(grid.cells.count, 1)
        XCTAssertTrue(grid.cells[0] === original)
    }

    func testHeaderMetadataAndVirtualContainerIdentity() {
        let grid = DataGrid(rows: 2, columns: 2)
        XCTAssertTrue(grid.insert(label: "Quarter", rows: NSRange(location: 0, length: 1), columns: NSRange(location: 0, length: 2), header: true))
        let header = grid.cells[0]
        XCTAssertEqual(header.accessibilityLabel, "Quarter")
        XCTAssertTrue(header.accessibilityTraits.contains(.header))
        XCTAssertTrue(header.accessibilityTraits.contains(.staticText))
        XCTAssertTrue((header.accessibilityContainer as? DataGrid) === grid)
        for column in 0...1 {
            let headers = grid.accessibilityHeaderElements(forColumn: column)
            XCTAssertEqual(headers?.count, 1)
            XCTAssertTrue((headers?.first as? DataCell) === header)
        }
        XCTAssertNil(grid.accessibilityHeaderElements(forColumn: 2))
    }

    func testRemovingVirtualElementsClearsBothLookupPaths() {
        let grid = DataGrid(rows: 1, columns: 1)
        XCTAssertTrue(grid.insert(label: "Value", rows: NSRange(location: 0, length: 1), columns: NSRange(location: 0, length: 1)))
        XCTAssertEqual(grid.accessibilityElements?.count, 1)
        grid.removeAllCells()
        XCTAssertTrue(grid.cells.isEmpty)
        XCTAssertEqual(grid.accessibilityElements?.count, 0)
        XCTAssertNil(grid.accessibilityDataTableCellElement(forRow: 0, column: 0))
    }

    func testEscapeDismissesAndClearsModalState() {
        let panel = DismissiblePanel()
        var calls = 0
        panel.onDismiss = { calls += 1 }
        panel.open()
        XCTAssertTrue(panel.accessibilityViewIsModal)
        XCTAssertFalse(panel.accessibilityElementsHidden)
        XCTAssertTrue(panel.accessibilityPerformEscape())
        XCTAssertFalse(panel.isOpen)
        XCTAssertTrue(panel.isHidden)
        XCTAssertTrue(panel.accessibilityElementsHidden)
        XCTAssertFalse(panel.accessibilityViewIsModal)
        XCTAssertEqual(calls, 1)
        XCTAssertFalse(panel.accessibilityPerformEscape())
        XCTAssertEqual(calls, 1)
    }

    func testRejectedEscapePreservesOpenState() {
        let panel = DismissiblePanel()
        panel.open()
        panel.canDismiss = false
        panel.onDismiss = { XCTFail("Rejected dismissal invoked callback") }
        XCTAssertFalse(panel.accessibilityPerformEscape())
        XCTAssertTrue(panel.isOpen)
        XCTAssertTrue(panel.accessibilityViewIsModal)
        XCTAssertFalse(panel.isHidden)
    }

    func testOrdinaryCloseButtonUsesSameDismissal() {
        let panel = DismissiblePanel()
        var calls = 0
        panel.onDismiss = { calls += 1 }
        panel.open()
        panel.closeButton.sendActions(for: .touchUpInside)
        XCTAssertFalse(panel.isOpen)
        XCTAssertFalse(panel.accessibilityViewIsModal)
        XCTAssertEqual(calls, 1)
    }

    func testPanelCanReopenAfterEscape() {
        let panel = DismissiblePanel()
        panel.open()
        XCTAssertTrue(panel.accessibilityPerformEscape())
        panel.open()
        XCTAssertTrue(panel.isOpen)
        XCTAssertFalse(panel.isHidden)
        XCTAssertFalse(panel.accessibilityElementsHidden)
        XCTAssertTrue(panel.accessibilityViewIsModal)
    }

    func testActivationReturnsHandlerSuccessAndFailure() {
        let control = ActivationControl()
        var calls = 0
        control.perform = { calls += 1; return true }
        XCTAssertTrue(control.accessibilityActivate())
        control.perform = { calls += 1; return false }
        XCTAssertFalse(control.accessibilityActivate())
        XCTAssertEqual(calls, 2)
        XCTAssertTrue(control.accessibilityTraits.contains(.button))
        XCTAssertTrue(control.isAccessibilityElement)
    }

    func testDisabledActivationDoesNotInvokeHandler() {
        let control = ActivationControl()
        var calls = 0
        control.perform = { calls += 1; return true }
        control.isEnabled = false
        XCTAssertFalse(control.accessibilityActivate())
        XCTAssertEqual(calls, 0)
    }
}
