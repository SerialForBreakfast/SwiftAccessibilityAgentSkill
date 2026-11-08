let vc = CheckoutViewController()
vc.view.frame = CGRect(x: 0, y: 0, width: 320, height: 640)
vc.loadViewIfNeeded()
let label = vc.totalLabel, button = vc.payButton

// Pay is the same working control: same title and plain configuration, still wired to pay().
guard button.isDescendant(of: vc.view), !button.isHidden, button.isEnabled,
      button.title(for: .normal) == "Pay now", button.configuration == nil,
      (button.actions(forTarget: vc, forControlEvent: .primaryActionTriggered) ?? []).contains("pay")
else { return false }
// No UIApplication in a unit process, so sendActions can't deliver; invoke the registered actions directly.
for name in button.actions(forTarget: vc, forControlEvent: .primaryActionTriggered) ?? [] {
    _ = vc.perform(NSSelectorFromString(name), with: button)
}
guard vc.payCount == 1 else { return false }

// The total keeps its text, wraps and never shrinks.
guard label.isDescendant(of: vc.view), label.text == vc.formattedTotal,
      label.numberOfLines == 0, !label.adjustsFontSizeToFitWidth
else { return false }

// Text size follows the environment, including a later change and a change back.
func apply(_ size: UIContentSizeCategory) {
    vc.traitOverrides.preferredContentSizeCategory = size
    vc.updateTraitsIfNeeded()
    vc.view.updateTraitsIfNeeded()
    label.updateTraitsIfNeeded()
    vc.view.setNeedsLayout()
    vc.view.layoutIfNeeded()
}
apply(.large)
let regular = label.font.pointSize
apply(.accessibilityExtraExtraExtraLarge)
let largest = label.font.pointSize
guard largest > regular * 1.5 else { return false }

// At the largest size the label is given the height its wrapped text needs.
let needed = label.sizeThatFits(CGSize(width: label.bounds.width, height: .greatestFiniteMagnitude)).height
guard label.bounds.width > 0, label.bounds.height + 0.5 >= needed else { return false }

apply(.large)
guard abs(label.font.pointSize - regular) < 0.5 else { return false }
return true
