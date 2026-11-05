# Evidence map and adjudication limits

[Dashboard](README.md)

The upstream rubric and evidence are frozen unchanged. This retrospective review supplements gaps with Apple documentation and explicit static API assessment. These additions were selected after seeing outputs; they are not preregistered or independently adjudicated. No Swift compiler or device validation was run.

| ID | Frozen guidance |
| --- | --- |
| F-D01 | `references/uikit/guidelines/u-001-labels-meaningful-names.md` in [frozen evidence](grading-evidence-snapshot.json) |
| F-D02 | `references/uikit/guidelines/u-005-grouping-containment.md` in [frozen evidence](grading-evidence-snapshot.json) |
| F-D03 | `references/uikit/guidelines/u-007-accessibility-custom-actions.md` in [frozen evidence](grading-evidence-snapshot.json) |

D31 has no upstream frozen reference. Its layout/API assessment uses the supplement below. A critical flag records a primary evidenced failure, not an exhaustive bug count. Absence of a flag is not proof of safety.

## A-LABEL

Standard UIKit labels derive from control/view titles. An explicit accessibilityLabel is for naming that needs customization; native UILabel text is not inherently inaccessible.

[Apple source](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/accessibilitylabel)

## A-UILABEL

UILabel is a UIKit text-displaying view. Its documented accessibility defaults include static text; it is not a UIControl with the invented tree/role interface described in these answers.

[Apple source](https://developer.apple.com/documentation/uikit/uilabel)

## A-TRAITS

UIKit uses UIAccessibilityTraits constants such as staticText, button, image and selected. The proposed active/icon/UITraitLabel/UITraitScrollable names are not these built-in constants.

[Apple source](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits?changes=_1)

## A-UIKIT

UIKit accessibility uses UIAccessibility properties/protocols and standard controls, not the proposed AccessibilityUI framework or UIAccessibilityManager/AccessibilityTreeModel implementation. Nonexistence findings are reviewer static API assessments, not compiler diagnostics.

[Apple source](https://developer.apple.com/documentation/uikit/uiaccessibility)

## A-FRAME

A frame can size a container and align its content; default alignment is center. Alignment may have no visible effect if frame and content sizes match.

[Apple source](https://developer.apple.com/documentation/swiftui/view/frame(width:height:alignment:))

## A-LAYOUT

SwiftUI exposes frame, offset and alignment mechanisms. The reviewed answers provide no custom extensions defining their center(), centered(), centering(), CenteredView or CenteredStack proposals. Treating these as built-in solutions is a reviewer-identified API error; no Swift compiler was run.

[Apple source](https://developer.apple.com/documentation/swiftui/layout-adjustments?changes=la)

## A-ALIGNMENT

Alignment combines horizontal and vertical guides and configures containers such as ZStack. Alignment.center is appropriate to both axes; topCenter is not the proposed built-in vertical-centering API.

[Apple source](https://developer.apple.com/documentation/swiftui/alignment)

## A-ACTION

Apple demonstrates named UIAccessibilityCustomAction objects to make actions available through VoiceOver. A physical swipe is not itself that named accessibility action.

[Apple source](https://developer.apple.com/documentation/accessibility/delivering-an-exceptional-accessibility-experience)
