# First failures and coverage limits

## NAV-MAC-01: incoming disabled key-view link survives configuration

Classification: author implementation defect. The first Mac positive run executed
18 methods; `DesktopNavigationTests/testIncomingDisabledLinkCleared` failed with
`XCTAssertNil failed` because the excluded button still pointed to another button.
The assertion was unchanged by the repair.

The first implementation cleared the previously configured list but did not clear
links on newly supplied excluded controls before constructing the eligible cycle.
Revision2 clears the new owned list as well. This affects ownership/reconfiguration,
not the truth of Apple's nextKeyView documentation or observed keyboard delivery.

- [Exact first source](incidents/mac-key-order-first.swift.txt)
- [First manifest](incidents/mac-first-manifest.json.txt)
- Original native inputs, diagnostics and summaries are retained in the private archive.
- `original-incoming-link` re-executes that original source against the same assertion.
- [Independent developer question](../../../code-examples/platforms/macos-navigation-v1/evaluation/key-order.prompt.md)
- [Controller rubric](../../../code-examples/platforms/macos-navigation-v1/evaluation/key-order.rubric.md)

This was also identified as a risk during source review before execution. The actual
native failure establishes the observed result; it is not a blind model benchmark.

## What worked

The initial tvOS implementation passed its sixteen selected methods. Mac identity
selection, reorder, removal, duplicate rejection and direct table selection passed
the first run. The existing adapter parsed both platform results without modification.

## What remains outside these assertions

Rows and key-view links are stored configuration, not a proof of keyboard traversal,
spoken table semantics or complete rendered tables. The examples do not implement
full application layouts. Filtering, duplicate rejection and cycle ownership are
explicit application policies, not universal Apple accessibility requirements.
Injected motion settings test application response, not system preference change
notifications or the appearance of an animation. No performance ranking or causal
model comparison follows from these author observations.
