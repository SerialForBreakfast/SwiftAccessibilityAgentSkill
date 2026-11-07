"""Two contrasting text-size contracts for one label. Controller-only; export question + starter only.

The decision under test is which text-size setting owns the label:
  font-supplied-setting  the caller passes the setting; the label must show exactly that size
  font-live-environment  the label must follow its own environment, including later changes
Automatic adjustment is wrong for the first and one valid way to satisfy the second.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "rc1/grader"))
from tasks import Task

BASE = 'let label = UILabel(); label.text = "Total"; let base = UIFont.monospacedSystemFont(ofSize: 17, weight: .bold)\n'
CHECK = """    guard label.font.fontName == expected.fontName, abs(label.font.pointSize-expected.pointSize) < 0.01,
          label.text == "Total", label.numberOfLines == 0, !label.adjustsFontSizeToFitWidth else { return false }"""
SCALED = "UIFontMetrics(forTextStyle: .body).scaledFont(for: base, compatibleWith: UITraitCollection(preferredContentSizeCategory: size))"

SUPPLIED = Task(
    "font-supplied-setting", "ios", "UIKit", "pilots/uikit-choice-v1",
    "Apply our supplied, unscaled design font to this description label at the given text-size setting. "
    "Use body scaling, let the description wrap without shrinking, and leave its contents alone.",
    "func style(_ label: UILabel, base: UIFont, traits: UITraitCollection)",
    reference="""    label.font = UIFontMetrics(forTextStyle: .body).scaledFont(for: base, compatibleWith: traits)
    label.numberOfLines = 0; label.adjustsFontSizeToFitWidth = false""",
    alternative="""    let metrics = UIFontMetrics(forTextStyle: .body)
    let resized = metrics.scaledFont(for: base, compatibleWith: traits)
    (label.font, label.numberOfLines, label.adjustsFontSizeToFitWidth) = (resized, 0, false)""",
    mutant="""    label.font = UIFontMetrics(forTextStyle: .body).scaledFont(for: base, compatibleWith: traits)
    label.adjustsFontForContentSizeCategory = true
    label.numberOfLines = 0; label.adjustsFontSizeToFitWidth = false""",
    test=BASE + """for size in [UIContentSizeCategory.large, .accessibilityExtraLarge, .extraSmall] {
    style(label, base: base, traits: UITraitCollection(preferredContentSizeCategory: size))
    let expected = """ + SCALED + "\n" + CHECK + "\n}\nreturn true",
)

LIVE = Task(
    "font-live-environment", "ios", "UIKit", "pilots/uikit-choice-v1",
    "Apply our supplied, unscaled design font to this description label so its size follows the text-size "
    "setting wherever the label is shown, including later changes. Use body scaling, let the description wrap "
    "without shrinking, and leave its contents alone.",
    "func style(_ label: UILabel, base: UIFont)",
    reference="""    label.font = UIFontMetrics(forTextStyle: .body).scaledFont(for: base)
    label.adjustsFontForContentSizeCategory = true
    label.numberOfLines = 0; label.adjustsFontSizeToFitWidth = false""",
    alternative="""    let metrics = UIFontMetrics(forTextStyle: .body)
    label.font = metrics.scaledFont(for: base, compatibleWith: label.traitCollection)
    label.numberOfLines = 0; label.adjustsFontSizeToFitWidth = false
    label.registerForTraitChanges([UITraitPreferredContentSizeCategory.self]) { (view: UILabel, _: UITraitCollection) in
        view.font = metrics.scaledFont(for: base, compatibleWith: view.traitCollection)
    }""",
    mutant="""    label.font = UIFontMetrics(forTextStyle: .body).scaledFont(for: base, compatibleWith: label.traitCollection)
    label.numberOfLines = 0; label.adjustsFontSizeToFitWidth = false""",
    test=BASE + """style(label, base: base)
for size in [UIContentSizeCategory.accessibilityExtraLarge, .large, .extraExtraLarge] {
    label.traitOverrides.preferredContentSizeCategory = size
    label.updateTraitsIfNeeded()
    let expected = """ + SCALED + "\n" + CHECK + "\n}\nreturn true",
)

# Extra authored variants beyond the dataclass's one alternative and one mutant.
# The observed rc.1 mechanism (scale for a setting AND auto-adjust) is wrong when the caller owns the
# setting, and right when the environment owns it.
EXTRA = {
    "font-supplied-setting": [
        ("mutant-system-font", """    label.font = UIFont.preferredFont(forTextStyle: .body, compatibleWith: traits)
    label.numberOfLines = 0; label.adjustsFontSizeToFitWidth = false""", "contract-failure"),
    ],
    "font-live-environment": [
        ("alternative-observed-mechanism", """    label.font = UIFontMetrics(forTextStyle: .body).scaledFont(for: base, compatibleWith: label.traitCollection)
    label.adjustsFontForContentSizeCategory = true
    label.numberOfLines = 0; label.adjustsFontSizeToFitWidth = false""", "pass"),
        ("mutant-system-font", """    label.font = UIFont.preferredFont(forTextStyle: .body)
    label.adjustsFontForContentSizeCategory = true
    label.numberOfLines = 0; label.adjustsFontSizeToFitWidth = false""", "contract-failure"),
    ],
}

CONTRACTS = [SUPPLIED, LIVE]
