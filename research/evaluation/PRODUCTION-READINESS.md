# Production readiness: decisions and delegated work

Current assessment: November 6, 2026. This is a release-work map, not new execution
permission or a relaxation of the frozen release criteria.

## Current status in plain language

| Deliverable | Actual state | Next action / owner |
| --- | --- | --- |
| Released skill 0.2.2 | Available; preserved as comparison baseline | Maintainer agent preserves it while preparing a candidate |
| Six OS26 code-contract questions | Qualified by the [reviewed closeout](../../evals/os26/reports/2026-11-05-gold-closeout/REVIEW.md) | Evaluation worker can run an approved bounded comparison after client/quota preflight |
| UIKit companion campaign | Native tests executed; independent campaign review remains outstanding | Independent reviewer audits claims, assertions and rubrics |
| Mac/TV companion batches | 119 Mac and 121 TV positive methods passed at recorded anchors, including shared AVFoundation contracts; 23 draft pairs across original, lifecycle, media and structure sets | Independent reviewer qualifies pairs and source/availability claims |
| Companion retrieval candidate | Offline selection/read-trace checks pass | Worker measures actual installed-agent retrieval and answer quality before promotion |
| Prompt records | Available local records archived with gaps disclosed; new drafts have no subject outputs | Maintainer maps cases; workers capture exact new requests/answers/analysis |
| Candidate skill improvement | Not yet established by paired frontier results | Author applies focused fixes after baseline; independent grader compares outcomes |

The old per-case "evidence pending" lines in GoldPrompts.md contradicted its header
and linked closeout. They have been corrected as presentation status only. The
questions, reference fixtures, released skill and frozen baseline remain unchanged.

## What the owner needs to decide

1. **Evaluation allocation:** approve one scoped campaign manifest with an exact
   supported frontier model, included subscription quota, total ceilings and stop
   conditions. The worker verifies availability and zero incremental spend before
   running. One approval may explicitly cover several bounded chunks; it need not
   become a separate user handoff for each prompt.
2. **Product choices:** decide only genuinely ambiguous intended behavior that cannot
   be resolved from the task or Apple sources. Reviewers should return a short list
   of concrete decisions, not ask the owner to inspect every test.
3. **Release:** approve the tested candidate scope/version after receiving the final
   results, regressions, remaining limitations and rollback plan.

These decisions do not require manual device accessibility testing, UI automation,
or personally reading every rubric. Technical reviews can be performed by an
independent agent in a separate session, distinct from the fixture author. Model
review itself consumes quota and belongs in the approved campaign allocation.

## Work agents should complete

### 1. Consolidated technical review

Review the actual code/assertions, Apple claims, available API annotations, expected
negative failures and prompt neutrality. Audit repaired oracles and accept valid
alternative implementations. Return one findings report with blocking defects,
fixes and remaining product decisions. Agent author resolves technical findings;
reviewer verifies the corrections. Submission is not acceptance.

### 2. Frontier baseline and scoring calibration

Begin with a small eligible UIKit development subset; SwiftUI expansion stays
explicitly deferred. The already-qualified OS26 UIKit questions can proceed without
waiting for every new Mac/TV draft or the entire historical transcript backfill.
Capture complete available input/output/tool records and label provider limitations.
Use C0 versus C2 initially to distinguish unaided answers from reference-assisted
answers; include C3 when testing routing/installed retrieval claims. Independent
blinded grading and calibration remain separate from the author's own opinion.

A small pilot verifies the harness and finds failures. It does not satisfy the full
release statistics by itself. After qualification, execute the frozen release
protocol at the approved scope and quota. No silent model substitution, paid fallback,
unauthorized retries or automatic expansion beyond that manifest.

### 3. Candidate fixes and release evidence

Use observed errors to author a versioned candidate, not an in-place baseline edit.
Run paired comparisons and check the existing [release criteria](../../evals/release-gates.json):
packaging/reference integrity, no new critical errors, the two-percentage-point
non-inferiority margin, platform review, judge calibration and source provenance.
The protocol also records three repetitions and a minimum 20 held-out families.
Claims of measurable improvement require supported paired uncertainty estimates.
The 15% input-token reduction is an efficiency target with quality preserved, not a
reason to discard correctness. Scope or protocol changes need explicit approval
before inspecting candidate outcomes; they are not silently relaxed here.

Promote only the validated changes. A staged release need not include every planned
platform feature, but its claims and tests must match its actual scope and approved
release protocol.

## What is not an owner-review blocker

- Bounded unit-test conclusions are the intended acceptance endpoint. Delivered
  speech, keyboard/focus behavior and universal usability are distinct claims, not
  hidden requirements for this unit-only project.
- Historical transcript gaps remain documented. They do not prevent collecting a
  clean new baseline, and missing historical outputs must not be invented.
- An unavailable remote reviewer should lead to reassignment to another independent
  session, not repeated requests for the owner to perform the technical audit.

Report state as **draft**, **native-validated**, **independently reviewed**,
**baseline-measured**, or **release-approved**. Keep evidence scope in one report
section rather than repeating a generic warning under every question.
