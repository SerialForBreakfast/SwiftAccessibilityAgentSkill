import AppKit
import SwiftUI

struct RecipientField: NSViewRepresentable {
    static func makeField() -> NSSearchField {
        let field = NSSearchField()
        field.isEditable = true
        field.setAccessibilityLabel("Recipient")
        return field
    }
    func makeNSView(context: Context) -> NSSearchField { Self.makeField() }
    func updateNSView(_ field: NSSearchField, context: Context) {}
}

struct AddressBar: View {
    var body: some View {
        HStack {
            Image(systemName: "person").accessibilityHidden(true)
            RecipientField()
        }
    }
}
