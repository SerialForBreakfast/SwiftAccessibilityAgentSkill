# First-pass gold-parity evidence audit

**Executed author audit of all 24 scenarios / 78 criteria / 12 families.** This
completes GPAR-01's first-pass deliverable within its two-hour cap; independent
acceptance, Mac evidence reconciliation and qualification remain pending.

The reviewed controller's **73 selected assertion methods in 15 packages** resolve
to matching current method/source hashes and exact positive test selections. The
offline checker also inspected **94 existing receipt rows** for those packages:
declared outcomes, selected tests, build/infrastructure state, skipped tests and
intended negative failures are consistent. These are historical receipt checks,
not 94 new runs or authentication of every full private original.

Those rows contain 14 compile successes, 15 positive unit selections and 65
intended negative selections across the linked packages. Many negatives concern
other assertions in those packages. Of the 15 scenarios with bound native
assertions, four have no negative check touching a selected assertion, seven have
one and four have at least two. Even two checks may concern different examples;
that count does not establish two mutants for one coherent task contract. Review
reasoning controls in their appropriate lane and retain the original code-gold
standard rather than silently weakening it or demanding mutants per criterion.

| First-pass coverage | Criteria | Meaning |
| --- | ---: | --- |
| Direct bounded evidence | 2 | tvOS native restoration-helper decisions and ownership assertions |
| Partial evidence | 35 | Relevant assertions/composition with explicitly named integration or scope limits |
| Review-only | 39 | Source, task-preservation, provenance and evidence-boundary judgments |
| Implementation-evidence gap in inspected package | 2 | macOS SwiftUI checkout/font/layout and existing-Pay preservation contracts |
| Not audited | 0 | Every selected criterion received an author finding and next action |

These categories are **not answer grades or gold-readiness scores**. Review-only
criteria do not need invented unit tests; partial evidence does not invalidate
the existing tests. The two implementation gaps may narrow further when the Mac
returns its existing evidence. No case is newly qualified here.

## What the audit changed

- Replaced topic/name-match confidence with criterion-specific findings, exact
  assertion bytes and receipt/environment identities. The original ledger remains
  intact. Its general container/reuse associations are discovery leads, not the
  current controller's exact action/card contracts.
- Identified existing evidence behind previously empty ledger mappings, especially
  tvOS media and lifecycle. Missing ledger linkage is not a reason to run tests.
- Verified **14 additional existing assertion methods** as reuse candidates: eight
  newer iOS media methods, three tvOS eligibility methods and three AppKit action
  methods. Their source, executed selections and receipts resolve. These additions
  are proposed evidence links; they do not rewrite the frozen controller.
- Cross-checked all six original gold questions against the selected questions.
  None is an exact question duplicate. Related concerns and reusable contracts are
  listed in the crosswalk; the six original qualification decisions do not transfer
  to new prompts. The gold-ready count remains six.
- Preserved the reviewed stable current-owner action alternative and conditional
  same-item request requirement. A missing token/helper spelling is not itself a
  defect. Optional rotors, safe no-target restoration and justified flexible
  layouts remain valid alternatives.

## Highest-value findings

**Completion wiring:** helper tests reject stale/duplicate tickets and support
reentrancy, but that does not establish that an actual sheet completion owns the
right ticket or waits until dismissal finishes. The current SwiftUI example reads
mutable `ticket` in `onDismiss`; that wiring needs explicit review, not an assumed
runtime defect from this inspection. The completed Gemini comparison's two
lifecycle regressions make this a priority. No generated answer was compiled or
executed by this audit.

**Media selection:** the original iOS SwiftUI preference unit checks volume/mute
and player identity; it does not check selected audio/subtitle options. Newer
fixture-backed media-v2 units provide useful item, phase and selected-caption
evidence. Reuse them before proposing another suite. Preserve the difference
between synthetic selected IDs, native media selection, metadata flags and actual
playback. Dev.6 remains a separate research candidate with no measured model lift.

**Composed state and text contracts:** card state criteria currently combine
settings, media-owner and ordinary-action examples. Checkout evidence combines a
total/Pay example with a separate long-text choice cell. Those are useful pieces,
but they do not jointly prove the requested card or total/description/design-font
update path. macOS text has declaration evidence and a preference example, but no
bound checkout/Pay contract in the inspected package.

**AppKit and provenance:** an AppKit parent element flag alone is not enough to
judge child exposure. The mixed-owner regression needs a platform-correct grading
alternative. Five non-testing criteria must continue treating the testing note as
controller policy, not as a supplied or read subject reference. The reviewed
IR-01/IR-02 interpretation fixes are retained; this audit does not reopen them.

## Remaining evidence dependencies

The Mac GPAR-M01 packet has not been received. GPAR-02 is therefore **not complete**.
The returned packet should establish what private originals/source declarations
can be authenticated and whether any remaining contract already exists. Use the
specific questions in [the next tranche](NEXT-TRANCHE.md), within the original
read-only handoff; do not expand the worker into builds or repairs.

The completed comparison reports 48 independently reconciled design-calibration
fixtures. Their private directory, `evals/results/gemini-controlled-v2-20261107-r1`,
is absent from this checkout. This is an **artifact-availability gap**, not evidence
that calibration was never performed. A source-side export/index is needed to map
the actual fixtures and labels to these 78 criteria and valid alternatives. Do
not regenerate the old 96-slot template or run a model to fill missing history.

Existing primary/declaration snapshots are pinned, not freshly authenticated
against Apple or the worker's SDK by this audit. Full provider context and some
private historical originals remain unavailable here. These limitations block
unsupported qualification claims, not preservation of the findings.

## Artifacts and checks

- [Criterion matrix](MATRIX.md): one finding and next action per criterion.
- [Machine-readable audit](audit.json): source/method/receipt pins, exact assertion
  sources, environments, negative witnesses, supplemental reuse and original-six
  crosswalk.
- [Authored decisions](decisions.json): semantic judgments separate from the
  deterministic evidence collector. This author is not an independent reviewer.
- [Consolidated next tranche](NEXT-TRANCHE.md): family estimates, closure order and
  precise existing-evidence requests.

From the project root:

```sh
python3 -B research/evaluation/gold-parity-v1/audit-v1/audit.py --check
```

`--write` regenerates only the additive audit JSON/matrix after deliberate edits
to its authored decisions. It does not change native sources, test manifests,
subject payloads, frozen rubrics or runtime skill files. It performs no network,
model or native execution. All task records, logs and authoring captures stay in
project-local `evals/results/gold-parity-v1/`.

Twelve synthetic parser-safety checks pass. They reject empty/wrong selections,
skipped tests, changed source pins, build/infrastructure failures counted as
mutant kills and inconsistent negative exit status. They test the evidence tool,
not the semantic author decisions or native accessibility behavior.

No gold promotion, new evaluation-model run, native build/test or worker message
was performed in this audit. The owner separately authorized Git publication of
the audit and updated tasks for the Mac to pull; publication does not establish
worker acceptance or evidence reconciliation.
