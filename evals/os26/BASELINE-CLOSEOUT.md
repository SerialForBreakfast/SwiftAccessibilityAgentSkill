# OS26 gold validation closeout

Date: 2026-11-05. Scope: `os26-code-contract-3`, six development cases.
Current status: **0/6 gold-ready**. No native execution or Gemini run authorized
by this checklist. Unit tests and compile checks support source review; no mandatory
manual verification, UI tests, observed speech/navigation or rendered-layout gates.

## Coordination receipt

Direct request `swift-accessibility-os26-unit-gates-20261105-r1` stored by BigDog
at project cursor1389, message `446b4d35-3a3a-4934-a5af-060eebe07af0`.
Storage is confirmed; acceptance and worker assignments are pending. It follows
`bigdog-sillycon-swift-os26-fixtures-20261105-v1`, without accepting native work on
this busy Mac. Prefer an approved available Apple worker, potentially MaxMini.

Changes remain uncommitted on top of29fc48b. BigDog cannot fetch these changes yet;
source delivery is a prerequisite, not an assumed completed handoff.

| File | SHA-256 of coordinated revision |
| --- | --- |
| prompts.json | dee47de12a6fe3c46c513036130e6f1973072c650406242a3778b7db7caa6381 |
| acceptance.json | 74cada603981b87ec3896f43141780af3382e7f7c8a5c248050bb6bf844de5e3 |
| ../runner/os26.mjs | 12cd5c16ca99c8395bc504475c369e5367a8be16d4167cb192a9b200285fdc13 |

Subsequent local evidence hardening supersedes the runner hash above with
`51d035cf2857e97f96dbaef308f77e0aafc1a9cb31c4be6a9be7110824197a1f`.
The r2 coordinator delta explains required execution/test-selection evidence.
97 offline tests pass; prompt/acceptance hashes are unchanged. UIKit switch-name
and callback-isolation assertions were added but remain unexecuted on Apple runtimes.

## Per-case work

| Case | Existing preparation | Required before promotion |
| --- | --- | --- |
| GP26-01 settings | UIKit test dispatches switch/Help callbacks and checks container flags | Assert switch name/state and child exposure, verify callbacks remain independent; compile and kill both mutants |
| GP26-02 reused cell | A/B/A/B configuration test on one instance | Execute test and stale-name/stale-value variants; accepted alternatives must not require the reference fix's exact sentence |
| GP26-03 checkout | Scaling/multiline/height prerequisites and payment callback test | Execute both mutants; strengthen parent/descendant constraint and preserved configuration checks as appropriate, without claiming rendered layout |
| GP26-04 delete | SwiftUI candidate and focus/hidden-control variants | Extract or expose real production activation paths, test correct IDs/exactly once/no nonactivation deletion; version unit-observable mutants; review native-control wiring separately |
| GP26-05 movies | Native Button candidate and callback/focus-reset variants | Test real per-ID activation path; replace focus-reset mutant with an explicit task-relevant unit-observable defect; native focus remains outside endpoint |
| GP26-06 toggle | Correct-code control and binding/hidden-toggle variants | Test production binding path, not a disconnected test binding; version a second unit-observable mutant; source-review native Toggle exposure; preserve no-change as a valid answer |

Do not introduce production test seams merely to assert a copied model of the UI.
The test must exercise code actually used by the example. Unit tests of handlers
do not establish that SwiftUI delivers a keyboard/remote/VoiceOver event to them.
Native-control wiring is an independent source-review criterion. If a condition
cannot honestly be asserted with the available public APIs, report it as unsupported
and revise the measurement before freezing, rather than adding reflection/UI tests.

Each known-good and each of two distinct mutations must run the SAME relevant
unit assertions. A compile error, missing runtime, zero discovered tests or crash is
not a unit mutation kill. Keep build errors distinct from expected assertion failures.
Archive existing variants and update fixture revision/hashes when replacing them.

## Required deliverables and proposed owners

1. **Source delivery, local maintainer:** publish the coordinated changes via an
   owner-approved commit/push or approved scoped artifact. BigDog acknowledges
   exact hashes; do not evaluate the older manual-gated revision by mistake.
2. **Fixture implementation, owner to confirm:** complete the gaps above, executable
   test selection and mutation runner. Add offline tests for zero-test results,
   missing SDK/runtime, wrong mutation identity and unrelated failure classification.
3. **Apple validation, worker to confirm:** inventory actual installed Xcode/SDK26
   and OS26 runtime builds without downloads. Pin destination and deployment target.
   Return good/mutant logs, assertion/test counts, source hashes and exit outcomes.
   An OS27 host can build for26 but cannot relabel OS27 runtime observations as26.
4. **Independent reviewer, BigDog to nominate:** review exact Apple sections,
   availability and accepted alternatives. Fixture author is not sole reviewer.
   Preserve discrepancies; a source URL list alone does not satisfy this gate.
5. **Receipt assembly, BigDog with worker:** map evidence to each gate ID and method
   (`review`, `compile`, `unit`); oracle checks require unit evidence. Run the offline
   promotion gate against real artifacts. Complete accounting is not proof of truth.
6. **Gemini execution qualification, BigDog:** reconfirm subscription-only auth,
   no paid fallback, exact model/effort/client, fresh isolated workspace, input hashes,
   receipt retention, finite owner quota, cancellation and export boundaries.
7. **Freeze and run, owner allocation required:** freeze corpus, evidence, fixtures,
   grading and adapter before the baseline. Keep exploratory runs separate. Calibrate
   answer grading using independent review before reporting semantic quality gains.

## Small first baseline proposal

Use the six OS26 cases, frozen v0.2.2 and the qualified historical subscription
lane: C0 versus C2, one repetition = **12 conversations**, not 12 guaranteed model
requests. This measures supplied-guidance contribution, not automatic retrieval.
Use a separately approved finite allocation; the historical batch's approval is
exhausted. Declare this a first development pass, not release acceptance.

The historical Gemini pilot used `gemini-3.8-flash-low`, Antigravity CLI1.5.1,
fresh workspaces and no tools. Those are past observations, not current capability
proof. Hard output-token/internal-request caps were unknown. Keep these limits
visible; require enforceable process/input bounds and quota safeguards. C1/C3 can
follow only after their isolation/tool instrumentation is qualified. Do not block
an honest C0/C2 development baseline by pretending it needs unimplemented C3.

Further repetitions, independent judging and platform expansion need allocations.
Six revised code families do not replace the historical60-family coverage or meet
existing release gates. Preserve correct-code controls and ordinary C0 successes.

## Completion checklist

- [ ] BigDog acknowledges revised scope and exact delivered source hashes.
- [ ] Fixture author, Apple worker and independent reviewer accept their tasks.
- [ ] Six known-good and twelve unit-observable mutation outcomes recorded.
- [ ] All six cases pass source, compile, unit and oracle promotion gates.
- [ ] Gemini adapter and current $0 subscription constraints requalified.
- [ ] Owner allocates the frozen12-conversation development batch.
- [ ] Every output/failure retained; independent grading calibration recorded.

Until these checks pass, publish progress as preparation, not a validated baseline.
