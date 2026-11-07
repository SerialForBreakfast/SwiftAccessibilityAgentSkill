# Local qualification: prove contracts before distilling instructions

Status: executed offline evidence audit; author/controller work, not independent
review or proof of better model responses. No new model, compiler or simulator runs.

## Results

| What was checked | Result | Meaning |
| --- | ---: | --- |
| Draft developer cases accounted for | 60 | All existing dev.5 inputs retained |
| Cases with an example manifest | 36 | Explicit companion links, not full prompt coverage |
| Linked cases with a valid matching contract receipt | 36 | Recorded checks match source pins, revision, target and executed test IDs |
| Cases without an executable example binding | 24 | Boundary controls, testing questions and remaining mapping work |
| Explicit primary-source mapping gaps | 3 | AppKit text/media and tvOS/UIKit text |
| Independently qualified gold cases | 0 | No automatic promotion from a package pass |
| New model calls / additional spend | 0 / $0 | Quality comparison remains pending |

Read the complete [evidence ledger](evidence-ledger.json). It records each question,
criterion, source hash, Apple link found in the existing guideline, manifest/source
pins, check, matching receipt, exact environment and proposed test leads. The ledger
is controller-only and must not enter normal skill context or model inputs.

Test leads use explicit topic/name matching to reduce review effort. They are not
semantic assertion review. This pass has not freshly verified Apple pages; local
existence and prior review dates do not establish current freshness.

## What improved through local iteration

The initial audit found 29 linked cases through research results indexes. Older UIKit
packages stored their receipts locally. Adding that existing record format brought
all 36 manifest-linked cases into the join without rerunning native tests or changing
historical outcomes. The [first implementation](iterations/first-audit.mjs.txt) and
[first summary](iterations/first-summary.json) preserve that discovery limitation.
This was an evidence-discovery limitation, not an accessibility or subject-model error.

The verifier rejects process failures hidden behind a success label, mismatched
manifest/package/check/target, changed source pins, absent runtime/toolchain data,
skipped/missing/extra tests, unexpected failed assertions and infrastructure errors.
Expected deliberate assertion failures remain distinct from failed builds.

87 offline checks include 60 case-provenance checks plus adversarial receipt checks,
reproducibility and summary checks. Receipt mutants test this verifier, not UIKit,
AppKit or SwiftUI behavior. No new native behavioral coverage is claimed.

## Next local work, before frontier evaluation

1. Resolve the three source mappings using applicable Apple documents/declarations.
2. Review the actual assertion bodies for each proposed test lead. Bind rubric
   criteria individually; mark non-unit observations documentation-supported.
3. Replace generic rubric requirements with observable, target-appropriate acceptance
   criteria. Keep valid alternatives; distinguish optional guidance from task failure.
4. Check each relevant existing native negative control and link its intended failed
   assertion and matching execution, rather than requiring a new mutant per question.
5. Qualify source freshness and API availability separately from execution receipts.
6. Freeze a representative approved development selection and preserve independent
   holdouts before requesting one bounded frontier comparison.

Missing bindings do not mean missing behavior or require blindly adding more tests.
The right next action may be connecting existing evidence, narrowing a claim, or
writing a better question. No mandatory human/manual accessibility verification or
UI automation is introduced. Independent review can be performed by a separate
reviewer; the owner is not required to manually validate every case.

## Distillation rule

Do not compress away a constraint just because its wording is long. First establish
its source-backed contract and failure sensitivity; then measure the candidate on
frozen questions. Distill only material whose outcome contribution can be defended.
Track bytes locally, actual tokens during approved runs, and correctness separately.
Keep examples, failure archives and this ledger on demand, outside default context.

## Reproduce

From the repository root:

```sh
node research/evaluation/local-qualification-v1/audit.mjs > /tmp/local-qualification.json
node --test research/evaluation/local-qualification-v1/integrity.test.mjs
```

The checked-in ledger is deterministic for its current input files. If sources or
receipts change, preserve the old candidate/ledger and produce a new revision; do not
silently replace historical evidence or automatically promote questions.
