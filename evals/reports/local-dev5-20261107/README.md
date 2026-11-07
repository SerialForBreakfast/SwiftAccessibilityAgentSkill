# Local development-skill comparison — November 7, 2026

Status: **bounded partial execution; all 32 captured answers source-reviewed
provisionally.** At the owner-approved 90-minute cutoff, 34/36 cells had been
attempted: 32 answers, two no-output stops and two unattempted cells. This is a
known development diagnostic, not independent qualification or release evidence.

Dev.5 reduced median reported input tokens by **43.3% for Gemma and 43.8% for
Qwen**, against released instructions with identical references. It did not yield
a complete implementation meeting the source-reviewed task contracts in this
sample. There are narrower improvements and regressions; token savings are not
evidence of quality-preserving efficiency.

The project-only output safeguards were committed as `a357ed6`; remote changes were
merged at `ec389c5`. The comparison uses the newly fetched, sealed milestone-v2
payloads for development candidate `0.3.0-dev.5` and its
`policy-and-target-sdk-v2` reference bundle. Released skill `0.2.2` remains unchanged.

## Frozen comparison

| Arm | Instructions | Supplied references |
| --- | --- | --- |
| C0 | Exact sealed generic assistant payload | None |
| R | Released root `SKILL.md`, including metadata, in the same outer wrapper | Identical user/reference message to D5 |
| D5 | Exact sealed development candidate payload | Sealed task-specific references |

R versus D5 compares instructions with the reference-bearing user message fixed.
C0 versus D5 measures the combined instruction/reference condition. It cannot
isolate an instruction-only effect. No model has tools, filesystem access, prior
conversation or actual retrieval; a supplied document is not a read trace.

The six applications are iOS/UIKit state, iOS/SwiftUI native-control preservation,
macOS/AppKit actions, macOS/SwiftUI text, tvOS/UIKit state and tvOS/SwiftUI actions.
They cover four related families, not six independent semantic replications.
These new questions are development cases; frozen qualified gold fixtures were
not changed.

Models are installed `gemma4:12b` (11.9B, Q4_K_M) and `qwen3.5:latest` (9.7B,
Q4_K_M), accessed through Ollama `0.40.11`. Exact digests and runtime metadata are
retained privately. There are 36 planned first attempts, serialized by model,
with initially rotated arm order. Settings are temperature 0, seed 42, context 16,384,
output cap 1,536, thinking disabled and a 240-second request limit. No downloads,
subscription calls, fallback models, answer repairs or automatic retries.

The owner extended the initial one-hour bound to 90 minutes with the 36-call and
55,296-output-token caps unchanged. Phase1 finished eight calls. Its input-integrity
guard then stopped it between requests after the deliberate runner amendment;
phase2 imported only the 28 proven unattempted cells. Its released-skill tvOS-state
request timed out after 240 seconds with output/usage unavailable. That cell is
inconclusive and is not repeated. Phase3 continued only the remaining 23 cells;
later timeouts are retained without retries, with model unloading confirmed before
further dispatch. Prompts/settings and model digests must match across phases.

Near the deadline, phase4 moved the still-unattempted tvOS SwiftUI action case
ahead of the second UIKit state application, prioritizing D5/R before C0. This
adaptive, unblinded coverage decision preserved all request bodies and settings;
it was not a preregistered ordering experiment. The D5/R pair finished. C0 then
received only 2.83 seconds before the global cutoff and returned no captured
answer. That is a **controller scheduling artifact**, not a 240-second model
timeout or a correctness failure. The future runner now reserves a full request
window before dispatch. No model was rerun after this fix.

The two unattempted cells are Qwen's tvOS/UIKit state C0 and R. Both models were
unloaded at closeout. The 36-cell matrix was not completed within the allocation.

## Observed outcomes

| Model | Attempts | Answers | Normal / length stops | Implementation observations |
| --- | ---: | ---: | ---: | --- |
| Gemma4:12b | 18 | 17 | 17 / 0 | 14 task gaps |
| Qwen3.5:latest | 16 | 15 | 6 / 9 | 11 task gaps; one truncated/inconclusive |

All six no-change answers preserve the working Toggle. Five have technical or
provenance caveats; Qwen D5 provides the cleanest bounded no-change answer. These
are provisional source observations, not independently accepted gold scores or a
model ranking. Truncation, time limits and incomplete coverage particularly limit
conclusions about Qwen's implementation ability.

| R → D5, same reference message | Matched cases | Median input reduction | Median reported total-token reduction |
| --- | ---: | ---: | ---: |
| Gemma4:12b | 5 | 43.3% | 36.6% |
| Qwen3.5:latest | 5 | 43.8% | 47.2% |

The five matched cases exclude tvOS/UIKit state because R has no answer. Qwen D5
finishes normally in four of those five pairs, versus one for R, but its completed
implementation examples still have errors. Reported successful-response usage is
47,774 input + 33,445 output = **81,219 tokens**. Usage for the two no-output
attempts is unavailable, not zero. Totals and stop rates do not establish a
quality-equivalent efficiency gain.

## Evidence and review limits

All generated artifacts stay inside this project. Private roots are
`evals/results/local-dev5-20261107-r1/` through
`evals/results/local-dev5-20261107-r4/`; see the
[output index](../../LOCAL-OUTPUTS.md). They retain expanded requests, raw original
responses, frozen inputs, hashes, events, model metadata, separate controller
rubrics/reviews and reviewed compiler probes. No completed response is replayed.

The package reproducibility check and all 36 milestone-v2 integrity tests passed
on this host, including its captured SDK declaration checks (zero skips).
Harness checks cover matched contexts, outside-project rejection and safe
continuation without replay, explicit coverage priority and the post-run budget
guard; all **19** integrated harness/path/probe checks passed.
Compiler probes use Swift6 language mode at deployment26.0 with SDK27, with
the installed SDK paths and exact commands recorded. They type-check explicitly
reviewed original fences; any scaffolding must be declared. They do not execute
generated code or establish UI layout, native dispatch, focus or speech.
If only a Markdown fence is cut while complete Swift declarations remain, an
explicit reviewed UTF16 range can select those original bytes without adding
braces. Truly incomplete code stays unassessable. Complete retained source blocks
may still establish independent errors even when later discussion is truncated.

There are 30 compiler invocations: eight pass, 18 fail with ordinary diagnostics,
two mix independent source errors with a SwiftUI macro-plugin environment failure,
and two probes of one Qwen block hit `failed to produce diagnostic`. Two further
incomplete sources are not compiled. These are **probe counts**, including declared
import/model scaffolds, not counts of correct model answers. Native no-change
answers need no compile probe. Compiler failures and environment limitations are
retained separately; generated code and model-authored tests are never executed.

Review uses the existing operational rubric and accepted alternatives, with one
unblinded Codex controller. Local grades are not independently accepted. The
[initial independent v2 review](../../../research/evaluation/independent-v2-review-20261107/REVIEW.md)
identified an action-owner oracle ambiguity and stale source bindings. The later
[controller-overlay review](../../../research/evaluation/v2-controller-resolution-20261107/REVIEW.md)
records additive IR-01/IR-02 grading-interpretation resolutions; native, baseline
and release qualification remain separate. This local diagnostic does not claim
independent acceptance or adoption of the upstream composite controller. Stable handlers
resolving the current owner are accepted; action observations rely on independent
API, ordinary-control and integration defects rather than a fixture-specific
stale-generation rule. Additive case/source mappings and qualifications are
retained in `controller/closeout-qualifications.json`. Controller
chat/provider context is only partially available; that limitation is explicit
in `controller/capture.json`. Exact subject HTTP inputs/outputs are retained.

An inherited state criterion requires same-item request-generation protection,
while the questions explicitly describe late A after replacement by B. This
review separates that broader oracle gap from the stated A/B contract. A missing
generation token alone is not a failure. A concise correct no-change answer needs
no compiler probe; unsupported optional API advice is reported separately.
Native-label updates are accepted without requiring unnecessary custom overrides.
Three early controller criterion notes were corrected on that point; their
original notes and calibration history are retained, and no overall task verdict
changed. This correction belongs to the controller, not to the skill or model.

The machine-readable [summary](summary.json) reconciles frozen inputs, requests,
provider receipts, output hashes, model digests and controller review hashes. Its
final status is `bounded_partial`; it does not generate semantic grades.

To reproduce that reconciliation from the retained private evidence:

```sh
node evals/runner/local-milestone-summary.mjs \
  evals/results/local-dev5-20261107-r1 \
  evals/results/local-dev5-20261107-r2 \
  evals/results/local-dev5-20261107-r3 \
  evals/results/local-dev5-20261107-r4 \
  evals/reports/local-dev5-20261107
```

## Gemma source observations

Gemma finished 18 first attempts: 17 retained answers and one request timeout.
All captured answers ended normally, not at the output-token limit.

| Case | Generic C0 | Released R | Development D5 |
| --- | --- | --- | --- |
| iOS/UIKit state | Contract gap; compiles | Contract gap; compiles | Contract gap; compiles with concurrency warnings |
| Native Toggle preservation | Correct preservation, technical caveats; no code needed | Correct preservation, technical caveats; no code needed | Correct preservation, technical caveats; no code needed |
| macOS/AppKit actions | Contract gap; fails compilation | Contract gap; fails even after import scaffold | Contract gap; fails compilation |
| macOS/SwiftUI text | Contract gap; fails compilation | Contract gap; fails compilation | Contract gap; fails compilation |
| tvOS/UIKit state | Contract gap; fails compilation | Timeout; correctness inconclusive | Contract gap; compiles |
| tvOS/SwiftUI actions | Contract gap; invalid API plus macro environment error | Contract gap; missing import, API probe passes with import | Contract gap; compiles |

The implementation gaps include absent Open/payment callback integration, stale
accessible values after reconfiguration, invented AppKit APIs and invalid Swift
argument/declaration syntax. Generic tvOS state advice explicitly hides Open when
optional status is absent, then proposes a test that would bless that regression.
Those generated tests are not adopted as evaluation oracles.

There are narrower positives: D5's SwiftUI action guards both Delete paths and uses
a supported API, where C0 invents a child-behavior case and leaves ordinary Delete
unguarded. Declarative current-item bindings are accepted; no fixture-specific
generation box is required. The compiler accepts the String-named action overload
at deployment26 even though the supplied card excerpts the Text overload.
Neither result proves native action delivery or generated navigation.

All five Gemma D5 answers with supplied references label them `read:` despite the
absence of tools/retrieval. The no-reference control correctly reports
`ROUTING: none`. Self-reported routing is therefore not treated as read evidence.

These findings concern this local, text-only harness. Concurrent reviewed compiler
checks and model reloads can affect elapsed times; no throughput ranking is made.
Earlier GP26/compact-B runs used different questions/contexts/output caps and are
not pooled into a longitudinal skill-quality claim.

## Qwen source observations

| Case | Generic C0 | Released R | Development D5 |
| --- | --- | --- | --- |
| iOS/UIKit state | Truncated; observed stale-result/verification defects; compiler diagnostic limitation | Truncated inside code; incomplete/unassessable | Truncated after complete declarations; observed stale-result defect; fails on UIKit `accessibilityRole` |
| Native Toggle preservation | Correct preservation; unsupported role-name caveat | Correct preservation; unrelated routing/source caveats | Correct preservation; no-change contract met |
| macOS/AppKit actions | Truncated; complete blocks contain invalid APIs | Truncated; invalid APIs/ownership and test-oracle concerns | Normal stop; invalid `@Action`, framework rewrite, missing Open |
| macOS/SwiftUI text | Complete retained code compiles; given OS premise rejected; font/settings gaps | Complete retained code compiles; callback/font/settings/verification gaps | Normal stop; fails on `DynamicTypeSize.accessibility`; callback/font gaps |
| tvOS/UIKit state | Unattempted | Unattempted | Truncated; explicit stale-result test/preservation defects; no complete source to compile |
| tvOS/SwiftUI actions | Global-budget cutoff after2.83 seconds; no answer | Truncated after complete implementation block; source defects and mixed macro/compiler limits | Normal stop; missing model/Open and invalid `handler:` label |

The macOS text case is a narrow compiler regression: C0/R's retained source
compiles, while D5 invents an enum case. C0 does preserve a declared payment
closure there, unlike R/D5, but rejects the given SDK/OS anchors and lacks the
requested font/settings integration. Supplied SDK cards help ground availability
without establishing overall task correctness.

Several generated tests would bless the wrong contract: accepting late A over
active B, hiding Open when optional status is absent, or expecting a previously
set callback flag to become false without resetting it. These are model-authored
oracle defects, not accepted gold criteria. Compiler diagnostics, task semantics,
source applicability and protocol fidelity must remain separate axes.

Qwen usually distinguishes supplied references in D5, but falsely labels the
macOS SDK card `read:`. Its D5 answers omit the required identity. These are
protocol findings, not substitutes for judging Swift correctness.

## Feedback and next useful test

The local evidence supports retaining small models as **diagnostic probes**.
Compact instructions alone do not repair general Swift/API knowledge or missing
application integration. Do not promote a runtime skill or optimize its release
around these local scores. This experiment does not establish whether capable
frontier coding agents benefit; that remains the separate BigDog lane.

Before another local batch, use a small, fully matched scope with compile-valid,
neutral starter code and supplied ordinary callback interfaces. That focuses the
answer budget on the accessibility change rather than rebuilding a whole UI.
Gate general Swift/callback competence separately, audit generated tests, reserve
request time before dispatch and allocate balanced coverage/per-model budgets.
Measure actual tool traces separately when evaluating installed skill retrieval.

## Updates received during this run

Remote checkpoint `ff846ac` was fast-forwarded at closeout, preserving the local
results. It adds research-only
[0.3.0-dev.6 media ownership guidance](../../../research/evaluation/failure-driven/candidates/0.3.0-dev.6/README.md)
and nine corrected media-only starter/prompt/rubric pairs. Its non-media router
delegates to pinned dev.5; its new media changes **were not model-tested here**.
All **16 offline dev.6 routing/integrity checks passed**, which establishes package
consistency, not answer-quality lift. The existing BigDog comparison remains a
separate bundle; no additional model allocation or release promotion is implied.

The refreshed fetch initially failed on an invalid local cached ref
`refs/remotes/origin/HEAD 2`. Its original bytes/hash are preserved inside
`evals/results/local-dev5-preflight/git-ref-quarantine/`; removing that invalid
duplicate from Git's ref directory restored fetching. All raw evidence, scratch,
caches and reconciliation artifacts stay inside this project.

Another update, `3e8bad4`, arrived before publication and was merged. Its
[separate BigDog Gemini comparison](../../../research/evaluation/gemini-controlled-run-20261107/README.md)
reports 13/24 candidate task-meets versus9/24 generic, with six paired gains,
three regressions and four inconclusive pairs. Those are independently
source-graded supplied-bundle results, without compilation/runtime verification,
released-skill comparison or immutable returned model identity. They are not
pooled with this local run. Its
[composite controller](../../../research/evaluation/v2-controller-resolution-20261107/composite-controller.json)
is a separate grading identity; this local run retains its own provisional
calibration rather than being retrospectively relabeled as using that controller.
