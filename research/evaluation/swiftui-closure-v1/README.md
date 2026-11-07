# SwiftUI coverage reconciliation and media integration

Research companion work against checkpoint `8e51ee9`. Released instructions,
frozen baselines, BigDog's sealed v2 comparison package and previous native evidence
are protected by [input hashes](protected-inputs.json). This package is not a skill
release or a new independent benchmark.

## Review At A Glance

| Area | Accounted-for scope |
| --- | --- |
| Inventory | All 217 original requirements and 15 guideline rules |
| Existing evidence | Original assertions/receipts plus the 13-row forwarding supplement |
| New implementation | Real AVFoundation choices connected to a SwiftUI picker |
| Platform lanes | SwiftUI/iOS, SwiftUI/macOS, SwiftUI/tvOS, all deployment26 |
| Evaluation | Three behavioral families, nine draft platform question/rubric pairs |
| First failures | Test compilation, adapter packaging and an incorrect native-default oracle |
| Remaining testable work | Live stream-state observation/teardown, explicitly unresolved |
| Promotion | Independent review and model comparison remain separate |

See [results](RESULTS.md), [coverage dispositions](COVERAGE.md),
[failure analysis](DIFFICULTIES.md), [review packet](REVIEW-REQUEST.md) and
[authoring capture limits](AUTHORING.md). The [machine ledger](coverage-ledger.json)
retains source text/hashes, Apple source links, narrow assertion bindings and
matching historical execution hashes. Repeated evidence is interned once rather
than expanding the same test lists into every clause.
Accepted findings can inform the [later candidate backlog](CANDIDATE-CHANGES.md).

## What The Example Does

The `MediaSelectionStore` and `MediaSelectionExample` share one player. Option
choices use that item's actual media-selection group, rather than changing a
synthetic selected string. Full-subtitle choices exclude forced-only options as
an explicit example policy. Unavailable choices preserve selection; changes to one
group preserve the other group. Off follows the native group's permission.

Generation and item identity own load results. Duplicate/old replies cannot replace
newer state. Cancelling an old task must not cancel a new request. Distinct states
represent no item, loading, no group and errors. Native choices are read through
the binding, and writes invalidate observable selection state.

Ordinary VideoPlayer controls remain in the composition; supplementary choices are
siblings rather than replacements. Tests and compilation establish the named
configuration/application contracts, not generated accessibility semantics,
rendered captions, focus, narration quality or visual reachability. Native external
changes can be read through the binding, but automatic external-change observation
is not asserted. Reload after item replacement. Production supplies localization
and actual content/stream handling; the media fixture is local and synthetic.

## On-Demand Examples

```sh
node code-examples/tools/swiftui-media-retrieval.mjs iOS SwiftUI selection
node code-examples/tools/swiftui-media-retrieval.mjs macOS SwiftUI ownership example
node code-examples/tools/swiftui-media-retrieval.mjs tvOS SwiftUI wiring contract
```

Default reads one short guidance file; examples and runnable contracts are opt-in.
Controller rubrics, incidents and the full library stay out of subject context.
The contract level includes the complete synthetic fixture needed to reproduce the
tests. Traces measure actual bytes/hashes; token telemetry is unavailable. This
research tool does not change installed routing.

## Reproduction

```sh
node research/evaluation/swiftui-closure-v1/prepare.mjs
node research/evaluation/swiftui-closure-v1/build-ledger.mjs
node --test research/evaluation/swiftui-closure-v1/integrity.test.mjs
node code-examples/tools/swiftui-media-campaign.mjs freeze /private/tmp/NEW_ROOT IOS26_UUID TV26_UUID
node code-examples/tools/swiftui-media-campaign.mjs run /private/tmp/NEW_ROOT IOS26_UUID TV26_UUID
```

`prepare.mjs` rebuilds the current additive package from shared sources; historical
attempts are never overwritten. Use it only before freezing a new attempt. Native
execution is sequential, source/environment fingerprints must match, completed
attempts are immutable, and infrastructure errors stop further native execution.
Assertion failures remain visible while independent checks continue. Original
adapters remain unchanged; additive adapters classify compilation failures with
zero test credit. Existing process timeouts apply. No models, installations,
paid dependencies, UI tests or mandatory manual checks.

## Next Highest-Value Step

Review this package as one evidence batch while BigDog evaluates its separately
sealed inputs. Incorporate accepted findings into a later candidate revision,
not into BigDog's in-flight comparison. Do not claim skill lift from unit passes.
