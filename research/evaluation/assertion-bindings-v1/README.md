# Assertion-level rubric bindings

Status: author-reviewed narrow mappings with verified syntax and historical receipts.
Not independent gold acceptance, new model grading or new native execution.

## At a glance

| Measure | Result |
| --- | ---: |
| Original development cases preserved | 60 |
| Rubric criteria explicitly accounted for | 198 |
| Criteria with bounded unit-evidence links | 81 |
| Cases with at least one bounded unit link | 35 |
| Distinct platform-specific test methods | 143 |
| Exact syntactic assertion sites | 317 |
| Methods also linked to a matching same-manifest negative control | 30 |
| Selected bindings missing matching successful unit execution | 0 |
| Independently accepted gold cases / new model calls / new native runs | 0 / 0 / 0 |

The remaining 117 criteria retain explicit source/answer-review or unbound-unit
status. They are not silently scored as covered. Related variants remain related
families; method/site counts are not independent behavioral coverage.

[Review every criterion](REVIEW.md), or inspect the complete controller-only
[binding ledger](bindings.json). Neither belongs in subject model context.

## What a link establishes

The author selects specific tests in [the mapping specification](spec.mjs), not by
keyword similarity. The syntax probe resolves owner type and method identity, exact
UTF-8 ranges, assertion expressions, conditional-compilation context and source
hashes. The builder then requires an exact current-manifest historical unit receipt:
matching platform/deployment target, sources, revision, selected/executed tests,
expected failures, process/build result, no skips and actual recorded runtime.

Each binding explains the narrow observation and remaining gap. Each contract links
manifest claims, full test-method source, exact assertion expressions, receipt hash,
recorded SDK/compiler/deployment/runtime and applicable negative controls. Primary
claim relevance and freshness still need review; a manifest source link alone is
not independent confirmation of every API recommendation.

An executed test method does not prove that every syntactic assertion ran: closures,
conditional branches and inactive platform branches may differ. Per-site execution
is not instrumented. These records are assertion locations linked to method-level
execution, not fabricated line-coverage measurements.

## Useful findings

- SwiftUI state tests support Binding roundtrips and application transitions, not
  generated accessibility semantics or installed visible/modifier action closures.
- The existing SwiftUI media test preserves AVPlayer identity, mute and volume;
  it does not prove selected audio/subtitle groups are preserved. That rubric stays
  partially supported rather than borrowing a native framework's claim.
- iOS/tvOS/macOS native media cases can link actual selected-option preservation
  and loaded metadata tests, separately from injected async-owner fixtures.
- SwiftUI text policy units do not establish live scaling, Pay callback preservation
  or rendered checkout layout. No unrelated policy pass is substituted.
- Native grouping/property checks and direct rotor search-block tests remain
  narrower than delivered traversal or rotor discoverability.
- No-change/default-control judgments, unknown ownership, availability reasoning
  and honest disclosure require source/answer review, not invented unit assertions.

## Reproduce

From the repository root, with the local syntax tool built:

```sh
node research/evaluation/assertion-bindings-v1/build.mjs > /tmp/assertion-bindings.json
node --test research/evaluation/assertion-bindings-v1/integrity.test.mjs
```

The output must match the checked-in overlay for the pinned tool/source inputs.
Building the probe uses installed Xcode modules; it does not execute example code.
The new overlay and generator preserve earlier candidate subjects, rubrics, ledgers,
native receipts, released skill and frozen baselines unchanged.

## Next decisions

An independent reviewer can inspect the linked methods and accepted alternatives
without requiring the owner to manually check each case. Focus review on whether the
narrow observation really supports the requested criterion and whether the residual
gap matters to grading. Resolve source mappings separately. Qualify reviewed cases
before freezing a substantial frontier batch; do not require one model run per link.

The earlier checkpoint is committed and pushed as 3a17ef5 (checkpoint 67916ea plus
upstream merge). This assertion-binding continuation is not yet committed or pushed.

## Failure preservation

The first selection pass accidentally applied a three-platform SwiftUI package lookup
to WatchOS/visionOS scope controls. The original spec and diagnostic excerpt remain
under [incidents](incidents/). The repair keeps all control cases and unsupported
axes out of unit bindings. This is an authoring/selection error, not an accessibility
or subject-model failure. Regression tests cover the original boundary.

## Validation checkpoint

The consolidated offline regression suite passes 900 checks, including 210 new
binding-integrity checks and 18 local-tool adapter tests. The frozen baseline
verifier still validates 210 files and the historical record verifier validates
87 pinned inputs. Released/runtime files, candidate snapshots and native example
sources are unchanged from the pushed checkpoint. `git diff --check` passes for
this continuation. No model generation, live source lookup or native example run.
