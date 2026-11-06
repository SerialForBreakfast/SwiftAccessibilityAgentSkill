# UPAIR-03 Controller Rubric

Draft development case, independent review pending. The subject sees only the prompt
string and separately approved condition material. Do not expose source, tests,
mutations, expected routes, this rubric or the difficulty narrative.

## Criteria

| Outcome | Weight | Evidence / accepted alternatives |
| --- | --- | --- |
| Correct contrast arithmetic | 2 | Independent black/white, identical, primary and gray numerical oracles; appropriate linearization and ratio ordering |
| Correct color-space interpretation | 2 | Known linear-sRGB color converted before component use; equivalent documented conversion approaches accepted |
| Explicit trait handling for both inputs | 2 | Light/dark and normal/high dynamic fixture; no dependence solely on ambient current appearance |
| Honest unsupported-input handling | 2 | Invalid components/thresholds and alpha handled explicitly; rejecting translucent colors or correctly compositing with an explicit known backdrop are both valid |
| Threshold without rounding to pass | 1 | Near-threshold fixture; equivalent close-boundary values accepted |
| Useful configured semantic-pair test | 1 | Named foreground/background and trait contexts; no universal promise for every semantic color |
| Evidence and scope calibrated | 1 | Unit calculation not proof of rendered pixels, material contrast or full accessibility; W3C math distinct from Apple API support |

Normalize weighted outcomes to the existing0-4 task-success scale; score correctness,
calibration and relevance separately. Invented APIs, fabricated evidence and unsupported
availability remain separately reviewed critical errors. C0 need not announce skill identity.

The implementation's opaque-only restriction is one valid solution, not a hidden
requirement to reject all transparency. Do not award a solution that discards alpha
without explaining its effect. Do not require our class names, conversion intent,
exact fixtures, error cases or `.label` pair when an equivalent scoped solution works.

## Oracle Review

Pure numeric oracles do not call the implementation to generate expected values.
Black/white extremes and primary weights provide independent checks; mid-gray and
transfer-boundary constants follow the cited W3C definition. A linear-sRGB source
fixture tests color conversion rather than merely testing RGB extraction on RGB input.
Injected dynamic colors make trait routing testable independently of Apple's palette.

The `.label`/`.systemBackground` check records actual anchor results. A future failure
could reflect configuration, conversion, oracle or platform change; investigate before
claiming Apple broke accessibility. No captured ratio proves a rendered outcome.

Before freeze, independently review sources, numerical oracles, prompt ambiguity and
one valid alternative implementation. Grade intentional defects as oracle calibration,
not evidence that a model produced those defects. Keep this exposed family in development.
Only a separately approved zero-spend baseline/candidate run can measure skill value.
