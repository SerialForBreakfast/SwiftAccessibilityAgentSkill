# Prompt Catalog by Framework

This index separates existing evaluation cases from the new UIKit-first unit
library. It is controller-side navigation, not a change to frozen prompts,
grading criteria, reports or installed skill instructions.

## At a Glance

| Segment | Cases | Meaning |
| --- | --- | --- |
| UIKit-specific | GP26-01, 02, 03 | Existing qualified gold fixtures: settings actions, cell reuse, checkout layout; iOS |
| UIKit-specific | GP26-07, 08, 09, 10 | Exploratory development cases: dismissal target, popup state, adjustable knob, download state; iOS |
| SwiftUI-specific | GP26-04, 05, 06 | Existing qualified gold fixtures: deletion (iPadOS), poster activation (tvOS), native Toggle (iOS) |
| SwiftUI-specific | GP26-11, 12 | Exploratory development cases: native Slider and Reduce Motion; iOS |
| Shared principles | EV01 through EV06 | Evidence honesty and limits: screenshots, audit claims, missing sources, OS-change claims, version reporting and direct-callback evidence |
| Interop | None in the twelve GP26 code cases above | Reserve for questions whose contract actually crosses framework ownership; do not infer interop from a mismatched injected reference |

The 18-case compact comparison therefore includes **7 UIKit code cases, 5 SwiftUI
code cases and 6 shared-evidence questions** per condition. Those are not 18 UIKit
tests. Gold qualification, exploratory status and framework classification are
separate dimensions. Shared-evidence cases may mention an Apple control or tool;
their scoring concerns evidence reasoning, not proof of that control's semantics.

Source catalogs: [qualified cases](os26/prompts.json),
[exploratory cases](os26/expansion-1/prompts.json), and
[comparison report](reports/compact-candidate-a-20261106/README.md).

## New UIKit-First Pairs

UPAIR-01 naming, UPAIR-02 text/selection, UPAIR-03 contrast, UPAIR-04 modal lifecycle,
UPAIR-05 edited rotors, UPAIR-06A time/buffering, UPAIR-06B media metadata,
UPAIR-06C speed controls and UPAIR-07 availability are **UIKit/iOS development
work**, with related Foundation/AVFoundation APIs where applicable. Their prompts
and rubrics are drafts, not newly qualified gold cases. UPAIR-08 is a coverage
audit, not one oversized model question. SwiftUI implementation expansion remains
deferred; historical SwiftUI evaluation results do not change that sequence.

## Classification and Reporting Rules

- Give each new case one primary segment: shared principles, UIKit, SwiftUI or
  explicit interop. Record platform separately: SwiftUI does not imply iOS.
- Classify by the actual task and code, not its topic name, file extension, or the
  reference injected by an evaluator. A SwiftUI Slider is not UISlider evidence.
- Shared principles may guide either framework; API defaults, availability and
  test observations remain attached to the framework/platform actually examined.
- For interop, name the control owner and the boundary being assessed. Do not
  duplicate one result into both framework totals.
- Lead future reports with per-segment results and denominators, plus gold versus
  exploratory status. Label any aggregate as mixed-framework. Shared-evidence
  passes must not inflate UIKit or SwiftUI implementation scores.
- Review prompt neutrality, rubric alternatives and evidence scope within the
  segment. Tests from one framework cannot qualify a case in another.
- Keep this classification outside subject payloads for existing frozen runs.
  Changing model-visible routing language is a separate benchmarked candidate.

## Why This Exists

A project summary used the historical SwiftUI Slider evaluation to illustrate
UIKit-first unit work. That conflated two distinct efforts. This index makes the
boundary visible for maintainers, reviewers and agents rather than relying on
memory. Earlier mixed-framework reports remain unchanged historical evidence.
