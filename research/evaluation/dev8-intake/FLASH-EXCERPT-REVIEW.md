# Flash regression review: awaiting original graded passages

Source: [BigDog's published paired findings and critical flags](../dev7-flash-haiku-results-20261107/README.md), commit `14295d6`. All three cases moved from meets (dev.5) to material gap (dev.7). These are whole-answer source judgments, not native failures. The public grade hashes identify grading artifacts; they do not reveal which passage caused a regression.

| Case | What can already be checked against dev.8 | What the original grading must resolve |
|---|---|---|
| ios-uikit-text | The checkout note covers initial and later sizing, flexible layout, existing button configuration and payment wiring. | Which obligation did the answer miss? Do not attribute this result to a font or callback defect from a different checkout cohort. |
| macos-appkit-actions | The published critical flag identifies missing ordinary Open wiring. The AppKit actions note explicitly requires connecting each new button to an actual recipient, or retaining the existing action. No additional rule is justified from this summary. | Compare the accepted ordinary path with the deficient implementation in context; a short fragment alone cannot demonstrate an omission elsewhere in the answer. |
| tvos-uikit-lifecycle | The UIKit dismissal note separates completion, owner consumption, target selection and dispatch. | Determine the reviewer’s actual objection; do not import the SwiftUI critical flags or assume reentrant mutation was the cause in this Flash answer. |

Request `swift-accessibility-dev8-flash-excerpts-r1` asks for the existing six answer passages and criterion rationales, not a regrade. Coordinator receipt 1445 recorded storage only. On return, match provider/case/arm, packet and grade hashes against the published summary; distinguish verified excerpt membership from worker-attested extraction when full originals are unavailable. Record the decisive difference and the smallest justified guidance delta per case. Retain existing guidance where it already covers that difference. No model run is required for this review.
