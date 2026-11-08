let entries = [FAQEntry(id: "refund", question: "How do refunds work?", answer: "Within 14 days."),
               FAQEntry(id: "ship", question: "When will it ship?", answer: "In two days.")]
let model = FAQModel(entries: entries)
var opened: [String] = []
model.didExpand = { opened.append($0) }
_ = FAQView(model: model)

// Full motion keeps the existing spring.
let spring = Animation.spring(duration: 0.45, bounce: 0.3)
guard FAQModel.expansionAnimation(reduceMotion: false) == spring else { return false }

// Reduce Motion: no animation, or a non-moving one; never the spring or another spring preset.
if let reduced = FAQModel.expansionAnimation(reduceMotion: true) {
    let springs: [Animation] = [spring, .default, .spring, .spring(), .bouncy, .snappy, .smooth, .interactiveSpring()]
    guard !springs.contains(reduced) else { return false }
}

// Expansion state changes immediately and independently of motion, with one analytics event per open.
model.toggle("refund")
guard model.expandedID == "refund", model.isExpanded("refund"), opened == ["refund"] else { return false }
model.toggle("ship")
guard model.expandedID == "ship", !model.isExpanded("refund"), opened == ["refund", "ship"] else { return false }
model.toggle("ship")
guard model.expandedID == nil, opened == ["refund", "ship"] else { return false }
model.toggle("missing")
guard model.expandedID == nil, opened.count == 2 else { return false }
return true
