# Answer distinctions before revision

Controller only. Source: [first comparison, overall pair table and priority findings](../gemini-controlled-run-20261107/README.md). These are source judgments, not compiler results.

| Development question | Accept | Material defect |
|---|---|---|
| iOS SwiftUI details dismissed | Bind restoration to completion of that presentation, including non-button dismissal. Resolve current origin or specified fallback then. A sheet callback or equivalent owner is valid. | Setting focus in Close confuses intent with completion. An old callback reading the latest presentation token can steal ownership. |
| tvOS UIKit details dismissed | Consume the matching owner and finish mutating state before calling an external requester. A returned target applied by the caller is valid. | Calling back through a still-mutating coordinator permits overlapping access or erases a replacement presentation. |
| Unknown SwiftUI/AppKit grouping | Ask for the host grouping configuration and native role/children/actions, or reason conditionally. Keeping both controls is the requirement. | Inferring that an accessible AppKit parent always hides its children diagnoses a cause absent from the question. |

Do not teach the oracle: an omitted helper name, optional rotor, particular layout axis, or different owner representation is not a defect. Compare behavior, not resemblance to our examples.
