@MainActor final class Owner: NSObject, AttachmentChipDelegate {
    var previewed: [Int] = [], removed: [Int] = []
    func chipDidRequestPreview(_ attachment: Attachment) { previewed.append(attachment.id) }
    func chipDidRequestRemoval(_ attachment: Attachment) { removed.append(attachment.id) }
}

@MainActor func press(_ control: NSControl) -> Bool {
    guard let action = control.action else { return false }
    if let target = control.target as? NSObject {
        guard target.responds(to: action) else { return false }
        _ = target.perform(action, with: control)
        return true
    }
    var responder: NSResponder? = control
    while let r = responder {
        if r.responds(to: action) { _ = r.perform(action, with: control); return true }
        responder = r.nextResponder
    }
    return false
}

@MainActor func fire(_ action: NSAccessibilityCustomAction) -> Bool {
    if let handler = action.handler { return handler() }
    if let target = action.target as? NSObject, let selector = action.selector, target.responds(to: selector) {
        _ = target.perform(selector, with: action)
        return true
    }
    return false
}

@MainActor func reachable(_ control: NSControl, from root: NSView) -> Bool {
    guard !control.isHiddenOrHasHiddenAncestor, control.isDescendant(of: root),
          control.cell?.isAccessibilityElement() ?? control.isAccessibilityElement() else { return false }
    var queue: [Any] = [root], visited = 0
    while !queue.isEmpty, visited < 500 {
        let element = queue.removeFirst(); visited += 1
        if (element as AnyObject) === control || (element as AnyObject) === control.cell { return true }
        if let node = element as? NSAccessibilityProtocol { queue += node.accessibilityChildren() ?? [] }
    }
    return false
}
