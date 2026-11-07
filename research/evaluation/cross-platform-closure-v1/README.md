# Cross-platform native coverage campaign

One coordinated campaign across UIKit/iOS, UIKit/tvOS and AppKit/macOS. The preceding
structure/forms batch was committed as `a02023c`; this campaign is separate working
content until its publication is authorized.

## Scope and completion

- [Coverage ledger](COVERAGE.md): every bounded clause and guideline rule has a disposition.
- [Native results](RESULTS.md): actual positive/negative outcomes, first failures and environments.
- [Independent questions](prompt-records.json): exact inputs and separate rubrics; model outputs stay `not-run`.
- [Difficulties](DIFFICULTIES.md): accidental defects, deliberate controls and oracle limits.
- [Sources](SOURCES.md): Apple documents and version-qualified SDK declarations.
- [Authoring capture](AUTHORING.md): available prompts, inputs, outputs and capture limits.
- [One review packet](REVIEW-REQUEST.md): prepared, not sent or accepted.

Completion means the bounded corpus is accounted for and selected native contracts
have matching execution evidence. It does not mean every broad accessibility claim
is unit-tested. Independent review, model baselines and skill promotion remain
separate. Missing testable contracts stay visible rather than being relabeled as
outside scope. SwiftUI and TV27 system behavior remain deferred.

## On-demand candidate retrieval

```sh
node code-examples/tools/closure-retrieval.mjs iOS UIKit validation-ownership
node code-examples/tools/closure-retrieval.mjs macOS AppKit text-rotor example
node code-examples/tools/closure-retrieval.mjs tvOS UIKit media-load-ownership contract
```

Guidance is small by default; source and tests are opt-in. Wrong-framework requests
do not borrow another platform's implementation. Actual file hashes and bytes are
reported; tokens are unavailable. Controller rubrics and incident archives are not
loaded. This repository tool does not change installed skill routing.

## Reproduce safely

Existing native adapters execute individual manifest checks in a new private output
directory. `native.mjs` handles iOS; `platform-native.mjs` handles Mac/TV. Mac uses the
actual host, not a pretend OS version flag. Simulator runs require a matching installed
runtime. No installs or model calls occur.

The additive runner freezes source/adapter hashes and toolchain/destination identity:

```sh
node code-examples/tools/closure-campaign.mjs freeze /private/tmp/new-closure-run "$IOS26_UUID" "$TV26_UUID"
node code-examples/tools/closure-campaign.mjs run /private/tmp/new-closure-run "$IOS26_UUID" "$TV26_UUID"
```

Only matching snapshots/environments resume. Attempts are immutable. Independent
assertion checks continue; infrastructure/build failures stop execution. Repairs
require a new revision/root, with at most two documented repair attempts per failing
contract. The initial author run used sequential adapter calls, each with its own
frozen input/environment evidence; the new full-run wrapper is not retroactively
claimed as the source of those runs.

Annual tested anchors, optional interim updates, zero spend, compile/unit only.
No mandatory manual verification, UI automation or changes to released skill files.

## Final local verification

- 35 immutable native attempts: 33 expected outcomes, two preserved first failures.
- All current positives pass; 23 deliberate controls are rejected as intended.
- 351 offline integrity/regression checks pass; 38 new-package/research Markdown
  files have no broken local links.
- 210 frozen baseline files and the historical87-pin evidence archive verify.
- Raw inputs, diagnostics, summaries and result bundles are retained in the private
  archive identified by [receipt](archive-receipt.json).

Local execution is complete for the selected contracts. The coverage ledger still
records partial broad claims, deferred frameworks/versions and the incomplete new
member-level API inventory. Independent technical acceptance and measured skill
improvement are not inferred from unit success. New campaign work is uncommitted;
only the preceding batch was committed by the initial request.
