# Gemini controlled-context comparison — 2026-11-07

Completed **48 first-attempt sessions: 24 paired scenarios in 12 related families**. Independent overall source grading found **13/24 candidate answers met the task**, versus **9/24 generic answers**. These are source judgments, not compiled or runtime results.

| Condition | Meets | Material gap | Not assessable |
| --- | ---: | ---: | ---: |
| Generic | 9 | 13 | 2 |
| Supplied 0.3.0-dev.5 context | 13 | 8 | 3 |

## Paired outcomes

| Case | Candidate context | Overall task transition | Narrow frozen-criterion transition |
| --- | --- | --- | --- |
| ios-uikit-actions | C2 | inconclusive-pair | preserved-meets |
| ios-uikit-state | C2 | inconclusive-pair | gap-to-meets |
| ios-uikit-text | C2 | preserved-material-gap | preserved-material-gap |
| ios-swiftui-semantics | C2 | preserved-meets | preserved-meets |
| ios-swiftui-lifecycle | C2 | meets-to-gap | meets-to-gap |
| ios-swiftui-media | C2 | preserved-material-gap | preserved-material-gap |
| macos-appkit-actions | C2 | inconclusive-pair | preserved-meets |
| macos-appkit-structure | C2 | gap-to-meets | gap-to-meets |
| macos-appkit-testing | C2-project-policy-only | gap-to-meets | gap-to-meets |
| macos-swiftui-state | C2-sdk-scoped | gap-to-meets | gap-to-meets |
| macos-swiftui-text | C2-sdk-scoped | preserved-material-gap | preserved-material-gap |
| macos-swiftui-lifecycle | C2-sdk-scoped | preserved-material-gap | preserved-material-gap |
| tvos-uikit-state | C2 | gap-to-meets | gap-to-meets |
| tvos-uikit-media | C2 | inconclusive-pair | inconclusive-pair |
| tvos-uikit-lifecycle | C2 | meets-to-gap | meets-to-gap |
| tvos-swiftui-actions | C2-sdk-scoped | gap-to-meets | gap-to-meets |
| tvos-swiftui-structure | C2-sdk-scoped | preserved-meets | preserved-meets |
| tvos-swiftui-testing | C2-project-policy-only | preserved-material-gap | preserved-material-gap |
| ios-uikit-no-change | C1 | gap-to-meets | gap-to-meets |
| ios-swiftui-no-change | C1 | preserved-meets | preserved-meets |
| macos-appkit-no-change | C1 | preserved-meets | preserved-meets |
| mixed-macos-owner | C1 | meets-to-gap | meets-to-gap |
| ios-missing-reference | C1 | preserved-meets | preserved-meets |
| tvos-version-boundary | C1 | preserved-meets | preserved-meets |

Overall transitions: `{"gap-to-meets": 6, "inconclusive-pair": 4, "meets-to-gap": 3, "preserved-material-gap": 5, "preserved-meets": 6}`. Integration uncertainty remains inconclusive, even when all narrower frozen criteria are met. Narrow criterion aggregates are derived transparently and do not replace independent overall judgments. No statistical release, model ranking or gold/holdout claim is made.

## What was tested

The requested client model was `gemini-4-argon-high`, high effort, AGY 1.5.3. The serving model/revision is **not exposed** in final result JSON. Requests, executable/settings and artifacts were pinned; immutable backend identity is unverified. One sample per arm, paired task bytes, alternating order, isolated nested project roots and tool-free custom agents. Original v2 payload and rubric bytes remain sealed.

The candidate arm received the frozen dev.5 body and selected inline context. Domain cases use C2 context (including SDK-scoped and project-policy-only strata); six controls use reference-free C1. This measures the supplied bundle against generic instructions. It does not isolate the skill body from references, compare released 0.2.2, or test installed discovery/native invocation. Prior cohorts remain separate.

All **24/24 candidate answers announced the correct dev.5 identity** and emitted a ROUTING line; all six reference-free controls said `ROUTING: none`. Generic answers emitted neither. The 18 domain answers identified supplied context; no subject performed reference-file reads.

The announcement demonstrates that the supplied candidate instruction was reflected in the answer. No files were retrieved by these subjects: inline references are supplied evidence, not reads. Full provider startup/tool-definition context is unavailable. SDK source currency, native compilation, unit behavior and accessibility delivery remain unverified for these generated answers. No UI/manual gate was added.

## Grading and calibration

A separate reviewer graded condition-masked packets against the composite controller, with identity and ROUTING lines removed and arm mappings withheld. Code/citations can still reveal context, and the reviewer had prior controller/calibration exposure: masking is imperfect. Four dimensions use 0.40 correctness, 0.35 task success, 0.15 calibration and 0.10 relevance; each is 0–4, normalized by 4. Supported critical flags and uncertainty are separate.

Before live grading, 48 author-created design fixtures across 12 representative families were independently classified: 24 meets, 12 material gaps, 12 not assessable, all reconciled with withheld author labels. This is bounded source-grading calibration, not tested-model performance, platform qualification or native validation. Provisional block-1 judgments and subsequent owner-path clarification are retained privately rather than overwritten as historical evidence. Stable alternative implementations are accepted; missing native/UI verification alone is not a failure.

## Subscription and efficiency

Provider-reported total tokens: generic **173,217**, candidate **183,547** (+5.96%). Median per-session totals: 7,963.5 versus 8,255.5. Reported token conventions are not subscription percent debit or provider-internal request counts.

Displayed **Argon weekly usage rose from 0% to 17%**. General Gemini weekly and five-hour windows stayed at 0% used. These are rounded account-wide observations, not exact batch/per-arm charges. Extra credits were disabled; no paid/API fallback, retries, repairs or extra probes were used. All 48 reservations were consumed once and the batch grant was closed. Total run time was about 52 minutes.

## Acceptance and next steps

Status: executed and independently source-graded. No release promotion or frozen-baseline change. Preserve dev.5, inspect exact gap/regression cases against their source contracts, then reconcile those needs with the incoming dev.6 media candidate before preparing any later semantic-version snapshot. Compile/unit verification of selected answers requires separately authorized native scope. A later benefit claim needs reviewed fresh cases and a qualified harness; installed skill loading remains a separate test. The earlier 12-session explicit/native diagnostic stays on hold.

The owner’s “Do it” followed by “No you can start it no need to stop to tell me” authorized this complete run. Earlier package/controller hold flags preserve historical preparation state and were not rewritten. Existing Sillycon delivery and independent review are incorporated through the pinned v2/composite records; no new remote native work or worker message was started.

## Verification and records

Offline verification: 22 harness unit tests pass, all 210 baseline files verify, sealed v2 rebuild integrity passes, and grading hashes, excerpts, normalized scores and complete pair accounting are audited. [Machine-readable results](summary.json) retain per-answer source grades, pair transitions, strata and provenance hashes. Exact private logs are retained locally; no raw answers, conversation IDs, credentials or account logs are published.

Related records: [v2 package](../milestone-package-v2/README.md), [independent review](../independent-v2-review-20261107/REVIEW.md), [composite controller](../v2-controller-resolution-20261107/README.md).

## Remote reconciliation

After execution, origin/main advanced to ff846ac and was fast-forwarded without conflict. Its separate SwiftUI review reports 44 corrected media methods on each of three platforms, three original-defect reproductions and two intended mutant rejections. Those are historical native receipts for revised examples, not native checks of these 48 answers. Dev.6 adds stale Off ownership, unmapped-selection representation, notification/cancellation distinctions and explicit store/reload ownership. It has no measured answer-quality lift yet. See [remote results](../swiftui-review-v1/RESULTS.md) and [dev.6](../failure-driven/candidates/0.3.0-dev.6/README.md). The pre-merge 147-file audit is retained; updated task history is a legitimate later checkpoint, not a payload rewrite.

## Priority findings for the next revision

Both observed domain regressions concern dismissal integration: the candidate SwiftUI answer completes restoration at the Close request rather than the actual completion boundary; the candidate UIKit answer proposes reentrant overlapping mutation of its coordinator. These are source-level findings, with no compiler/runtime result claimed. The third regression, in the mixed AppKit ownership control, overgeneralizes `isAccessibilityElement == true` as necessarily hiding child controls; AppKit role/child semantics need separate assessment. Investigate these exact contracts before widening general guidance.

Candidate gains should be preserved at their measured scope. Persistent gaps and unresolved owner/exposure paths require targeted contracts and alternative-aware grading. Remote ff846ac already contains a separate 0.3.0-dev.6 media candidate. Review its changes against these failures before drafting another version; keep dev.5 and the released skill unchanged. Prepare a comparison offline, then estimate subscription percentage before requesting a new live run.
