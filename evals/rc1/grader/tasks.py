"""Controller-only test vectors. Export only the question and starter() to the subject."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    id: str
    platform: str
    framework: str
    source: str
    question: str
    signature: str
    reference: str
    alternative: str
    mutant: str
    test: str

    def solution(self, body):
        return f"import {self.framework}\n\n@MainActor\n{self.signature} {{\n{body}\n}}\n"


TASKS = [
Task("checkout-font", "ios", "UIKit", "pilots/uikit-choice-v1",
"Apply our supplied, unscaled design font to this description label at the given text-size setting. Use body scaling, let the description wrap without shrinking, and leave its contents alone.",
"func style(_ label: UILabel, base: UIFont, traits: UITraitCollection)",
"""    label.font = UIFontMetrics(forTextStyle: .body).scaledFont(for: base, compatibleWith: traits)
    label.numberOfLines = 0; label.adjustsFontSizeToFitWidth = false""",
"""    let metrics = UIFontMetrics(forTextStyle: .body)
    let resized = metrics.scaledFont(for: base, compatibleWith: traits)
    (label.font, label.numberOfLines, label.adjustsFontSizeToFitWidth) = (resized, 0, false)""",
"""    label.font = UIFont.preferredFont(forTextStyle: .body, compatibleWith: traits)
    label.numberOfLines = 0; label.adjustsFontSizeToFitWidth = false""",
"""let label = UILabel(); label.text = "Total"; let base = UIFont.monospacedSystemFont(ofSize: 17, weight: .bold)
for size in [UIContentSizeCategory.large, .accessibilityExtraLarge] {
    let traits = UITraitCollection(preferredContentSizeCategory: size)
    style(label, base: base, traits: traits)
    let expected = UIFontMetrics(forTextStyle: .body).scaledFont(for: base, compatibleWith: traits)
    guard label.font.fontName == expected.fontName, abs(label.font.pointSize-expected.pointSize) < 0.01,
          label.text == "Total", label.numberOfLines == 0, !label.adjustsFontSizeToFitWidth else { return false }
}
return true"""),
Task("switch-preservation", "ios", "UIKit", "pilots/uikit-semantics-v1",
"This existing switch works. On reuse only its accessible name changes; pass the very same switch back, without resetting its state, traits or help.",
"func rename(_ control: UISwitch, to name: String) -> UISwitch",
"    control.accessibilityLabel = name; return control",
"    if control.accessibilityLabel != name { control.accessibilityLabel = name }; return control",
"    let copy = UISwitch(); copy.accessibilityLabel = name; return copy",
"""let s = UISwitch(); s.isOn = true; s.accessibilityHint = "Keep"; let traits = s.accessibilityTraits
for name in ["Wi-Fi", "Cellular"] {
    guard rename(s, to: name) === s, s.accessibilityLabel == name, s.isOn,
          s.accessibilityTraits == traits, s.accessibilityHint == "Keep" else { return false }
}
return true"""),
Task("toggle-binding", "ios", "SwiftUI", "swiftui/ios-v1",
"Our Toggle edits an existing setting. Return a binding that reads the live value and ignores duplicate writes and writes while the setting is locked.",
"func editable(_ source: Binding<Bool>, locked: @escaping () -> Bool) -> Binding<Bool>",
"    Binding(get: { source.wrappedValue }, set: { if !locked() && $0 != source.wrappedValue { source.wrappedValue = $0 } })",
"""    func commit(_ next: Bool) { guard next != source.wrappedValue, !locked() else { return }; source.wrappedValue = next }
    return Binding(get: { source.wrappedValue }, set: commit)""",
"    source",
"""var value = false, locked = false, writes = 0
let b = editable(Binding(get: { value }, set: { value = $0; writes += 1 }), locked: { locked })
b.wrappedValue = true; b.wrappedValue = true; locked = true; b.wrappedValue = false
guard b.wrappedValue, writes == 1 else { return false }
value = false; return !b.wrappedValue"""),
Task("adjustable-volume", "ios", "SwiftUI", "swiftui/ios-v1",
"Our custom volume control moves by five. Compute the next percent for a SwiftUI accessibility adjustment and stop at 0 and 100. Inputs are in range.",
"func adjusted(_ percent: Int, _ direction: AccessibilityAdjustmentDirection) -> Int",
"""    switch direction { case .increment: return min(100, percent + 5); case .decrement: return max(0, percent - 5); @unknown default: return percent }""",
"""    let delta: Int
    switch direction { case .increment: delta = 5; case .decrement: delta = -5; @unknown default: delta = 0 }
    return max(0, min(percent + delta, 100))""",
"    direction == .increment ? percent + 5 : percent - 5",
"""return adjusted(99,.increment)==100 && adjusted(2,.decrement)==0 && adjusted(31,.increment)==36 && adjusted(55,.decrement)==50"""),
Task("ordinary-buttons", "macos", "AppKit", "platforms/macos-appkit-v1",
"Connect both existing buttons to their distinct supplied actions. This row can be configured again with a different owner; clicking must reach only that owner.",
"func wire(_ open: NSButton, _ save: NSButton, owner: NSObject, openAction: Selector, saveAction: Selector)",
"    open.target = owner; open.action = openAction; save.target = owner; save.action = saveAction",
"    for (button, action) in [(open, openAction), (save, saveAction)] { button.action = action; button.target = owner }",
"    save.target = owner; save.action = saveAction",
"""let open = NSButton(), save = NSButton(), a = Receiver(), b = Receiver()
for target in [a,b] {
    wire(open, save, owner: target, openAction: #selector(Receiver.open), saveAction: #selector(Receiver.save))
    for button in [open,save] {
        guard let sel = button.action, button.target === target, target.responds(to: sel) else { return false }
        _ = target.perform(sel, with: button)
    }
}
return a.events == ["open","save"] && b.events == a.events"""),
Task("status-change", "macos", "AppKit", "platforms/macos-appkit-v1",
"Update the existing status field. Notify the caller once after its string changes and stay quiet if the same value arrives again.",
"func update(_ label: NSTextField, _ value: String, changed: () -> Void)",
"    guard label.stringValue != value else { return }; label.stringValue = value; changed()",
"    let old = label.stringValue; label.stringValue = value; if old != label.stringValue { changed() }",
"    label.stringValue = value; changed()",
"""let label = NSTextField(labelWithString: ""); var seen: [String] = []
for v in ["","Ready","Ready",""] { update(label,v) { seen.append(label.stringValue) } }
return seen == ["Ready",""] && label.stringValue.isEmpty"""),
Task("landmark-identity", "macos", "SwiftUI", "swiftui/macos-v1",
"Our report rotor lists important entries. Return their stable IDs in the current display order, including after reorder or deletion; don't use positions as IDs.",
"func landmarks(_ rows: [(id: String, important: Bool)]) -> [String]",
"    rows.filter { $0.important }.map { $0.id }",
"    rows.reduce(into: []) { if $1.important { $0.append($1.id) } }",
"    rows.enumerated().compactMap { $0.element.important ? String($0.offset) : nil }",
"""return landmarks([("B",true),("A",false),("C",true)]) == ["B","C"] && landmarks([("C",true),("B",false)]) == ["C"] && landmarks([]).isEmpty"""),
Task("checkout-layout", "macos", "SwiftUI", "swiftui/macos-v1",
"Our scene supplies a DynamicTypeSize preference. The checkout's app policy stacks controls at every accessibility size and uses the ordinary arrangement otherwise. Return the layout decision; do not infer a system preference feed.",
"func stackCheckout(_ size: DynamicTypeSize) -> Bool",
"    size.isAccessibilitySize",
"    size >= .accessibility1",
"    size == .accessibility1",
"""return [DynamicTypeSize.xSmall,.large,.xxxLarge].allSatisfy { !stackCheckout($0) }
    && [DynamicTypeSize.accessibility1,.accessibility2,.accessibility3,.accessibility4,.accessibility5].allSatisfy(stackCheckout)"""),
Task("restoration-eligibility", "tvos", "UIKit", "platforms/tvos-lifecycle-v1",
"When a panel finishes dismissing, choose the original button if it is still in the supplied eligible list and enabled; otherwise use the first enabled button in the list, or nil. Return a request target only.",
"func restore(_ opener: UIButton?, eligible: [UIButton]) -> UIButton?",
"    if let opener, opener.isEnabled, eligible.contains(where: { $0 === opener }) { return opener }; return eligible.first { $0.isEnabled }",
"    let live = eligible.filter { $0.isEnabled }; return live.first { $0 === opener } ?? live.first",
"    if let opener, eligible.contains(where: { $0 === opener }) { return opener }; return eligible.first { $0.isEnabled }",
"""let a = UIButton(), b = UIButton()
guard restore(b,eligible:[a,b]) === b, restore(b,eligible:[a]) === a else { return false }
b.isEnabled = false
guard restore(b,eligible:[b,a]) === a else { return false }
a.isEnabled = false; return restore(a,eligible:[a,b]) == nil && restore(nil,eligible:[]) == nil"""),
Task("row-traits", "tvos", "UIKit", "platforms/tvos-state-recovery-v1",
"This button's selected state changes on reuse. Update just the accessibility selected trait without erasing any other traits.",
"func selection(_ button: UIButton, _ selected: Bool)",
"    if selected { button.accessibilityTraits.insert(.selected) } else { button.accessibilityTraits.remove(.selected) }",
"    let old = button.accessibilityTraits; button.accessibilityTraits = selected ? old.union(.selected) : old.subtracting(.selected)",
"    button.accessibilityTraits = selected ? .selected : []",
"""let b = UIButton(); b.accessibilityTraits = [.button,.header]
for flag in [true,true,false] { selection(b,flag); guard b.accessibilityTraits == (flag ? [.selected,.header,.button] : [.header,.button]) else { return false } }
return true"""),
Task("motion-policy", "tvos", "SwiftUI", "swiftui/tvos-v1",
"Our focus effect is optional. Return the supplied SwiftUI animation unchanged when motion is allowed, but no animation for Reduce Motion. An absent effect should remain absent.",
"func effect(_ proposed: Animation?, reduceMotion: Bool) -> Animation?",
"    reduceMotion ? nil : proposed",
"    guard !reduceMotion, let proposed else { return nil }; return proposed",
"    proposed",
"""let custom = Animation.linear(duration: 0.82)
return effect(custom,reduceMotion:true) == nil && effect(custom,reduceMotion:false) == custom && effect(nil,reduceMotion:false) == nil"""),
Task("stale-media-reply", "tvos", "SwiftUI", "swiftui/tvos-v1",
"A delayed stream status reply updates our SwiftUI binding. Accept only the current item's current request, even if two loads were for the same item. Rejected replies must not write the binding.",
"func receive(_ status: Binding<String>, current: (String, Int), reply: (String, Int), value: String)",
"    guard current == reply else { return }; status.wrappedValue = value",
"    if reply.0 == current.0 && reply.1 == current.1 { status.wrappedValue = value }",
"    if current.0 == reply.0 { status.wrappedValue = value }",
"""var writes: [String] = []; let binding = Binding<String>(get: { writes.last ?? "" }, set: { writes.append($0) })
for reply in [("A",2),("B",1),("B",2)] { receive(binding,current:("B",2),reply:reply,value:"Ready") }
return writes == ["Ready"]"""),
]
