# UPAIR-07 Draft Rubric

Send only prompt.json. Do not include this rubric, source inventory, diagnostics,
expected routes or reference implementation in subject inputs. Independent review
and calibration are pending; this known incident is a development case.

Score each item 0 incorrect/missing, 1 partial, 2 satisfied:

1. Separates build SDK, deployment minimum and actual simulator/runtime version.
2. Uses documented member availability to decide guards; a new SDK alone does not
   authorize newer-only APIs on older supported runtimes.
3. Recognizes the locale languageCode deprecation and proposes a supported equivalent
   preserving optionality (or an independently justified equivalent implementation).
4. Treats warnings as warnings and compilation as compile evidence, not runtime coverage.
5. Proposes bounded current/previous anchors and relevant compile/unit checks without
   demanding every minor release, UI automation or mandatory manual verification.
6. Avoids unnecessary fallbacks when the supported deployment floor already covers
   the replacement API; identifies missing evidence instead of inventing version dates.

Critical errors: guarantees all27 APIs work at26, suppresses an availability error
instead of fixing it, or claims an unexecuted runtime was tested. Accept different
valid investigation tools and code organization. Never repair a model answer before
recording its original result. Case status is draft, with zero inference runs.
