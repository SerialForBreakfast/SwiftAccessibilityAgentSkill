# SwiftUI failure-driven native campaign

One consolidated iOS/macOS/tvOS campaign, explicitly authorized by the current owner
request. Previous "SwiftUI deferred" notes describe the earlier phase; released
SwiftUI skill guidance and frozen model baselines remain unchanged.

## Evidence

- [Coverage](COVERAGE.md): all 15 guideline rules and 217 requirements dispositioned.
- [Results](RESULTS.md): exact native attempts, anchors and failure/repair outcomes.
- [Difficulties](DIFFICULTIES.md): accidental defect, oracle defect and source-audit gaps.
- [Source scope](SOURCES.md): Apple contracts and installed declaration evidence.
- [Exact questions/rubrics](prompt-records.json):21 drafts, no invented subject outputs.
- [Authoring record](AUTHORING.md) and [owner request](OWNER-REQUEST.md).
- [One independent review packet](REVIEW-REQUEST.md): prepared, not dispatched.

Seven behavioral families cover semantics/native controls, document actions/rotors,
text/preferences, presentation lifecycle, async forms, synthetic media choices and
platform-specific native coordinators. The last three contribute to the forms/media
and mixed-framework workstreams; they are not separate requests for small tranches.

Actual SwiftUI view bodies are compiled for each target. Units exercise their
shared application state, Binding get/set paths and explicit native coordinator
methods. These are not tests of the SwiftUI-generated accessibility tree, installed
modifier callbacks, delivered focus or rendered layout. No reflection, private
introspection, UI tests, new dependencies or required manual checks.

## Progressive disclosure

```sh
node code-examples/tools/swiftui-retrieval.mjs iOS SwiftUI semantics
node code-examples/tools/swiftui-retrieval.mjs macOS SwiftUI interop example
node code-examples/tools/swiftui-retrieval.mjs tvOS SwiftUI documents contract
```

Only the selected platform/family is loaded. Default guidance stays small; example
source and contract tests are opt-in. Shared FormsMedia source serves two closely
related families; contract inspection loads the combined test module. No incident,
solution rubric or full library enters default context. Traces report actual bytes
and hashes; token telemetry is unavailable. This does not alter released routing.

## Reproduce

Use new private directories. The additive runner freezes all source/adapter hashes
and actual environment identity, then runs the existing native adapters sequentially:

```sh
node code-examples/tools/swiftui-campaign.mjs freeze /private/tmp/new-swiftui-campaign "$IOS26_UUID" "$TV 26_UUID"
node code-examples/tools/swiftui-campaign.mjs run /private/tmp/new-swiftui-campaign "$IOS26_UUID" "$TV 26_UUID"
```

Only matching inputs/environment resume; completed attempts cannot be overwritten.
Independent assertion checks continue; native infrastructure or build failures stop
the campaign. Repairs require new revisions/root and at most two repairs per failing
contract. Initial exploratory attempts retain their own per-adapter snapshots; the
final runner does not retroactively claim to have frozen those earlier attempts.

Shared-policy mutants execute on Mac; native coordinator mutation executes on all
three platforms. Unit package builds use Swift tools 6.0 while standalone compile
checks retain the original adapters' default language mode. No model calls, installs,
worker messages, Git publication or Claude activity are part of this campaign.

## Consolidated checkpoint

All current platform positives and10 intended mutant executions matched expectations.
The18 native attempts include the retained first61-method Mac suite with two failed
assertions; raw evidence is preserved by [archive receipt](archive-receipt.json).
The [checkpoint](checkpoint.json) separates method definitions, platform repetitions,
mutant patterns, execution counts and independent review state.

396 offline checks pass. All53 campaign/package Markdown files have resolving local
links. All1,136 protected tracked files,210 frozen baseline files and the earlier
87-pin evidence record verify unchanged. Two additional [controller diagnostic
questions](diagnostic-prompts.json) cover the lifetime oracle and scanner omission;
they are separate from the21 platform accessibility questions and have no fabricated
independent answers. The first216-requirement inventory remains preserved, and the
corrected217-requirement ledger explicitly leaves the OS27 paragraph unresolved.

Independent review is prepared, not sent or accepted. There are no new evaluation
model calls, spend, Claude activity, UI tests or mandatory manual gates. Source and
research changes are uncommitted/unpushed; existing private onboarding/intake work
was left untouched. Successful unit contracts do not promote the released skill.
