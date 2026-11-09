"""Behaviorally equivalent control implementations, applied only to staged sources."""
EDITS={
'ModalUIKit.swift':[
 ('private var priorHidden = false','private var priorHidden = false\n    private var restoreBackground: (() -> Void)?'),
 ('priorHidden = background.accessibilityElementsHidden','priorHidden = background.accessibilityElementsHidden\n        restoreBackground = { [weak background, priorHidden] in background?.accessibilityElementsHidden = priorHidden }'),
 ('background?.accessibilityElementsHidden = priorHidden\n        background = nil','restoreBackground?()\n        restoreBackground = nil\n        background = nil')],
'Presentation.swift':[
 ('private var active: UUID?', 'private final class Lifetime { var valid = true }\n    private var active: Lifetime?'),
 ('let id = UUID()', 'active?.valid = false\n        let id = Lifetime()'),
 ('self.active == id else { return }','id.valid else { return }\n            id.valid = false')],
'NativeSurface.swift':[
 ('private var generation = 0','private final class Registration {}\n    private var registration = Registration()'),
 ('generation += 1;', 'registration = Registration();'),
 ('let ticket = generation','let ticket = registration'),
 ('self.generation == ticket','self.registration === ticket')],
'MediaSelection.swift':[
 ('if let id {\n            if id == unlistedSelectionID','let selected: AVMediaSelectionOption?\n        if let id {\n            if id == unlistedSelectionID'),
 ('item.select(choice.option, in: group)','selected = choice.option'),
 ('item.select(nil, in: group)\n        }\n        selectionRevision', 'selected = nil\n        }\n        item.select(selected, in: group)\n        selectionRevision')]
}
def apply(name,s):
    for old,new in EDITS[name]:
        assert old in s,(name,old)
        s=s.replace(old,new)
    return s
