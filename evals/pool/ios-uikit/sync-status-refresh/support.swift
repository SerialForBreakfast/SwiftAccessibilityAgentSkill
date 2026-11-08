/// No UIApplication runs in a unit process: invoke each registered handler for the event directly.
@MainActor func activate(_ control: UIControl, _ events: UIControl.Event = [.primaryActionTriggered, .touchUpInside]) {
    control.enumerateEventHandlers { action, targetAction, event, _ in
        guard !event.intersection(events).isEmpty else { return }
        if let action { control.sendAction(action) }
        else if let (target, selector) = targetAction, let object = target as? NSObject {
            _ = object.perform(selector, with: control)
        }
    }
}
