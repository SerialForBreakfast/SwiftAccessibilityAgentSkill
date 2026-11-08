let styler = ReceiptRowStyler()
let base = styler.brandFont
let text = "2 × Oat flat white, extra hot, no lid, with a long note"
var sizes: [CGFloat] = []
for category in [UIContentSizeCategory.small, .large, .accessibilityExtraLarge, .accessibilityExtraExtraExtraLarge, .large] {
    let traits = UITraitCollection(preferredContentSizeCategory: category)
    let label = styler.makeDescriptionLabel(text: text, traits: traits)
    let expected = UIFontMetrics(forTextStyle: .body).scaledFont(for: base, compatibleWith: traits)
    // Brand typeface at the body-scaled size for the supplied setting.
    guard label.font.fontName == base.fontName,
          abs(label.font.pointSize - expected.pointSize) < 0.5 else { return false }
    // Wording, colour and accessible name are unchanged; the text wraps and never shrinks.
    guard label.text == text, label.textColor == styler.detailColor,
          label.accessibilityLabel == nil || label.accessibilityLabel == text,
          label.numberOfLines == 0, !label.adjustsFontSizeToFitWidth else { return false }
    sizes.append(label.font.pointSize)
}
// Larger settings really give larger text.
return sizes[0] < sizes[1] && sizes[2] > sizes[1] * 1.5 && sizes[3] > sizes[2]
