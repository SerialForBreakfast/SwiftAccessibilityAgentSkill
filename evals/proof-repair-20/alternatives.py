"""Controller-only alternate implementations; replace once at the behavior under test."""
CHANGES={
'Q002':('button.accessibilityTraits.insert(.selected)','button.accessibilityTraits = button.accessibilityTraits.union(.selected)'),
'Q006':('accessibilityElements = ordered','accessibilityElements = records.compactMap { byID[$0.id] }'),
'Q010':('value <= 0.04045 ? value / 12.92 : pow((value + 0.055) / 1.055, 2.4)','if value > 0.04045 { return pow((value + 0.055) / 1.055, 2.4) }; return value / 12.92'),
'Q018':('guard let self, self.generation == token, let remove = self.onRemove else { return false }','guard let self, let remove = self.onRemove else { return false }; if token != self.generation { return false }'),
'Q024':('guard self.snapshot == input else','guard input.allSatisfy({ self.fields[$0.key]?.text ?? "" == $0.value }) else'),
'Q027':('            NSLocationInRange(column, $0.accessibilityColumnRange())','            ($0.accessibilityColumnRange().location..<NSMaxRange($0.accessibilityColumnRange())).contains(column)'),
'Q031':('guard let self, self.state == .closing, self.generation == token else { return }\n            self.finish(notify: true)','if let panel = self, panel.generation == token, panel.state == .closing { panel.finish(notify: true) }'),
'Q041':('forName: UIAccessibility.reduceMotionStatusDidChangeNotification','forName: Notification.Name(rawValue: UIAccessibility.reduceMotionStatusDidChangeNotification.rawValue)'),
'Q054':('decoration.isAccessibilityElement = false','if decoration.isAccessibilityElement { decoration.isAccessibilityElement = false }'),
'Q057':('guard rate != selectedRate else { return true }\n        selectedRate = rate\n        render()\n        onChange?(rate)','if rate != selectedRate { selectedRate = rate; render(); onChange?(rate) }'),
'Q059':('accessibilityTraits.insert(.selected)','accessibilityTraits.formUnion(.selected)'),
'Q066':('let save = NSButton(title: "Save", target: nil, action: nil)','lazy var save = NSButton(title: "Save", target: self, action: #selector(saveItem))'),
'Q067':('let previous = selectedID','let previous = items.indices.contains(table.selectedRow) ? items[table.selectedRow].id : nil'),
'Q072':('return target.isDescendant(of: root) && target.isEnabled && target.acceptsFirstResponder && !target.isHiddenOrHasHiddenAncestor','guard target.acceptsFirstResponder, !target.isHiddenOrHasHiddenAncestor else { return false }; return target.isEnabled && target.isDescendant(of: root)'),
'Q080':('select(selected)','if let id = selected, let node = nodes[id], outline.row(forItem: node) >= 0 { outline.selectRowIndexes(IndexSet(integer: outline.row(forItem: node)), byExtendingSelection: false) } else { outline.deselectAll(nil) }'),
'Q081':('setAccessibilitySelected(selected)','if isAccessibilitySelected() != selected { setAccessibilitySelected(selected) }'),
'Q083':('label.text = text\n        label.accessibilityLabel = text','label.accessibilityLabel = text\n        label.text = text'),
'Q089':('guard let self, self.details.isEnabled else { return }; self.onDetails()','if let card = self, card.details.isEnabled { card.onDetails() }'),
'Q092':('reduceMotion ? 0 : 0.25','if reduceMotion { return .zero }; return 0.25'),
'Q099':('shelf.isAccessibilityElement = false','if shelf.isAccessibilityElement { shelf.isAccessibilityElement = false }')
}
