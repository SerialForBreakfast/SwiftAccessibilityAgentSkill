iOS 26.0, SwiftUI.

We're doing an accessibility review of the Help screen. The FAQ rows spring open when tapped, and we already turn that off when Reduce Motion is on. One reviewer thinks the Reduce Motion behavior "just pops in" and is worried that's an accessibility problem. Can you check the expand/collapse handling for motion and accessibility and change whatever actually needs changing?

Keep `FAQEntry`, `FAQModel(entries:)`, `expandedID`, `toggle(_:)`, `isExpanded(_:)`, `didExpand`, `FAQModel.expansionAnimation(reduceMotion:)` and `FAQView(model:)` with their current names and types.
