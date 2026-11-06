import UIKit

@MainActor
public final class DataCell: UIAccessibilityElement, UIAccessibilityContainerDataTableCell {
    private let rows: NSRange
    private let columns: NSRange

    public init(container: Any, label: String, rows: NSRange, columns: NSRange, header: Bool) {
        self.rows = rows
        self.columns = columns
        super.init(accessibilityContainer: container)
        accessibilityLabel = label
        accessibilityTraits = header ? [.staticText, .header] : .staticText
    }

    public func accessibilityRowRange() -> NSRange { rows }
    public func accessibilityColumnRange() -> NSRange { columns }
}

@MainActor
public final class DataGrid: UIView, UIAccessibilityContainerDataTable {
    public private(set) var cells: [DataCell] = []
    private let rows: Int
    private let columns: Int

    public init(rows: Int, columns: Int) {
        precondition(rows >= 0 && columns >= 0)
        self.rows = rows
        self.columns = columns
        super.init(frame: .zero)
        isAccessibilityElement = false
        accessibilityContainerType = .dataTable
        accessibilityElements = []
    }

    public required init?(coder: NSCoder) { fatalError("Programmatic example") }

    @discardableResult
    public func insert(label: String, rows: NSRange, columns: NSRange, header: Bool = false) -> Bool {
        // Subtraction avoids overflow when validating untrusted range lengths.
        guard rows.location >= 0, rows.location < self.rows,
              rows.length > 0, rows.length <= self.rows - rows.location,
              columns.location >= 0, columns.location < self.columns,
              columns.length > 0, columns.length <= self.columns - columns.location else { return false }
        guard !cells.contains(where: {
            NSIntersectionRange($0.accessibilityRowRange(), rows).length > 0 &&
            NSIntersectionRange($0.accessibilityColumnRange(), columns).length > 0
        }) else { return false }
        let cell = DataCell(container: self, label: label, rows: rows, columns: columns, header: header)
        cells.append(cell)
        accessibilityElements = cells
        return true
    }

    public func removeAllCells() {
        cells.removeAll()
        accessibilityElements = []
    }

    public func accessibilityRowCount() -> Int { rows }
    public func accessibilityColumnCount() -> Int { columns }

    public func accessibilityDataTableCellElement(forRow row: Int, column: Int) -> (any UIAccessibilityContainerDataTableCell)? {
        guard row >= 0, row < rows, column >= 0, column < columns else { return nil }
        return cells.first {
            NSLocationInRange(row, $0.accessibilityRowRange()) &&
            column == $0.accessibilityColumnRange().location
        }
    }

    public func accessibilityHeaderElements(forColumn column: Int) -> [any UIAccessibilityContainerDataTableCell]? {
        guard column >= 0, column < columns else { return nil }
        return cells.filter {
            $0.accessibilityTraits.contains(.header) && NSLocationInRange(column, $0.accessibilityColumnRange())
        }
    }
}

@MainActor
public final class DismissiblePanel: UIView {
    public let closeButton = UIButton(type: .system)
    public private(set) var isOpen = false
    public var canDismiss = true
    public var onDismiss: () -> Void = {}

    public override init(frame: CGRect) {
        super.init(frame: frame)
        isAccessibilityElement = false
        closeButton.setTitle("Close", for: .normal)
        addSubview(closeButton)
        closeButton.addAction(UIAction { [weak self] _ in _ = self?.dismiss() }, for: .touchUpInside)
        accessibilityElements = [closeButton]
        isHidden = true
        accessibilityElementsHidden = true
    }

    public required init?(coder: NSCoder) { fatalError("Programmatic example") }

    public func open() {
        isOpen = true
        isHidden = false
        accessibilityElementsHidden = false
        accessibilityViewIsModal = true
    }

    @discardableResult
    public func dismiss() -> Bool {
        guard isOpen && canDismiss else { return false }
        isOpen = false
        isHidden = true
        accessibilityElementsHidden = true
        accessibilityViewIsModal = false
        onDismiss()
        return true
    }

    public override func accessibilityPerformEscape() -> Bool { dismiss() }
}

@MainActor
public final class ActivationControl: UIControl {
    public var perform: () -> Bool = { false }

    public override init(frame: CGRect) {
        super.init(frame: frame)
        isAccessibilityElement = true
        accessibilityLabel = "Confirm"
        accessibilityTraits.insert(.button)
    }

    public required init?(coder: NSCoder) { fatalError("Programmatic example") }

    public override func accessibilityActivate() -> Bool {
        guard isEnabled else { return false }
        return perform()
    }
}
