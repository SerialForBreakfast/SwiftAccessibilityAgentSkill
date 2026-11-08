# Zero-base v1: prepared offline, not performance-tested

[Decision](../../adr/ADR-005-failure-derived-skill.md) | [56-case board](BOARD.md) | [controller matrix](matrix.json) | [arm hashes and byte sizes](manifest.json) | [challenger archive](archives/full.zip)

The stopped inventory was reusable: 369 graded observations from nine source groups, 56 case identities, not 369 independent failures. Fifteen cases have at least one Haiku failure, fourteen have failures only outside Haiku, and 27 are passing controls. With/without content is exposure, not randomized treatment: uninvoked and generic answers remain distinguishable in source records. Per-case mixtures are not estimates of effect. Aggregate-only counts (notably Flash S2) have no recoverable answer-to-repeat mapping from that source. An inconclusive pair is not evidence that both individual answers failed. Native confirmation is case-specific; it does not authenticate every answer attributed to the family.

## What's installed

Use an isolated project and extract just one archive there under the host's usual skill directory; all have the same discovery identity. No installer or model session is required for byte verification. The neutral shell has identity and read attribution only. The full arm adds two shared rules and seven focused notes. Each minus arm removes exactly one rule and its route, if any. No inherited entry point, code exemplar, grading criterion, prompt ID or incident narrative is shipped. The private evidence index is not a runtime dependency.

## How rules were distilled

| Rule | Distinction retained instead of an overbroad instruction |
|---|---|
| restraint | Preserve a working control; don't treat all native controls as correct. Pair the Slider with a custom adjustable knob. |
| ordinary | Preserve independent ordinary activation; add a path when a gesture is the only one. A shortcut isn't a replacement. |
| children | Narrow grouping advice to the owning AppKit/hosted layer rather than importing an iOS grouping recipe. |
| refresh | Merge reuse and same-instance refresh. Clear only owned optional state, not unrelated help or traits. |
| dismissal | Separate requesting a close from completing it; a later matching owner may restore, an obsolete one may not. |
| layout | Require a reachable installed control across callbacks, not a particular stored property or stack orientation. |
| font | Keep supplied-setting vs live-environment examples distinct; neither a universal tracking ban nor an unconditional flag survives both. |
| media | Merge stale-result checks only where their owners match: same item/new request differs from an external replacement. |
| proof / callbacks | Keep evidence wording in the entry; open test-design detail only for an implementation question. Wiring and delivering an input are distinct claims. |

The nine rule revisions and removal cases are in matrix.json. Rotor landmark identity has passing control evidence; AppKit grouping failures do not establish a Haiku rotor failure. No standalone rotor/API recipe was admitted on that basis. API availability is an evidence-boundary question pending a graded wrong-API example with exact source and platform. W6's iPad deletion incident is historical collateral, not a new platform commitment. An unchanged name/accessibility label in an otherwise unchanged control should not switch the recommended mechanism. The next portfolio must include these invariance checks alongside decision-changing controls.

## Offline reproduction

From the project root, run:

```sh
python3 -B research/evaluation/failure-inventory/build.py --check
python3 -B research/evaluation/zero-base-v1/build.py --check
python3 -B research/evaluation/zero-base-v1/check.py --private
python3 -B evals/rc1-comparison/verify_return.py
python3 -B evals/rc1/verify.py
```

Without private bundles use check.py without --private against the prepared inventory. The inventory rebuild requires its original evidence. The private check resolves 114 input/answer pairs from the dev.7, seven-case replay and two rc.1 cohorts and writes a content-addressed locator index under ignored evals/results/. These are a linked subset, not 114 new sessions. Other sources remain linked at their available granularity; no reconstruction of transcripts from grades. Full prompt and grader records remain at source. The chat authoring instruction is the owner's ADR-005 implementation request and continuation with the stopped-work transcript; no exact authoring-session export was supplied to this package.

The existing ten pool tasks (eight development, two labeled transfer) are authored fixtures, with no checked-in cell qualification receipts at intake. Treat published/inspected transfer tasks as development analogues, not a fresh blind transfer family. Use the pool to qualify intact integrations and genuine alternatives; do not silently promote it. Protected historical checkout grading is reproducible separately; no native run was needed to assemble this package.

## Proposed next evaluation (not a dispatch)

Freeze one exact subject input per admitted case and disqualify any case lacking the full starter, neutral prompt or valid oracle. A case listed by hash alone is not execution-ready. Reuse the 24-case scoring registry and its narrower criterion-to-assertion mappings; units for helpers do not qualify their callers. For the other cases use the original rubric, not this matrix as an answer key. Pin the target to Claude Haiku 5.5 low. Use separate clean sessions and counterbalance arm order. Keep discovery separate and actual reads distinct from self-report.

For N approved, input-ready tasks, one explicit comparison of shell, full and incumbent costs 3N sessions per repeat; all 56 would mean 168 first sessions, **not an allocation**. The nine removal arms on three designated cases each would add 27 first sessions when the matching full answers already exist with identical inputs/settings. Use the supplied-vs-live font pair as an additional removal contrast when its qualified task is admitted. Repeat a preselected cross-family subset to assess variation; keep new post-freeze transfer families and automatic invocation as separate lanes with their own arithmetic. No session unless the owner approves that exact plan. For a smaller allowance prefer paired breadth; do not claim rule attribution for arms not run.

Return one case-level board, with fixed/persistent/regressed/preserved/inconclusive, grader type, evidence excerpts, critical action losses, usage and loaded bytes. Select the cheaper candidate only after quality constraints. A rule surviving construction is a hypothesis, not a measured win.

### Recovered unit evidence

The initial coverage script looked only for a per-cell published scorecard. An additional read-only reconciliation found prior private receipts. [Qualification ledger](pool-receipts.json) checks each current source and oracle hash, expected result and artifact bytes against those attempts. Eight tasks match accepted receipts (including integrated checkout, external media replacement and two Mac button cases). Two must **not** grade answers: sync-status-refresh rejects its reference and alternative; account-rename-focus fails its alternative and three mutants for the wrong reason. The former's pending-state oracle expects old error copy gone, while the reference leaves retry help visible during loading. The latter's alternative calls cancelRename from the view without defining that method. Preserve both first attempts, resolve the product contract before adjusting the oracle, and keep exposed transfer material out of a blind test. Recheck with `python3 -B research/evaluation/zero-base-v1/pool_evidence.py --check`. No fixtures or old outcomes were repaired to inflate qualification.

**Subject isolation:** subjects/ contains 50 developer-only input exports, pinned by matrix.json. Historical controlled comparisons embedded reference text inside the user message itself; the exporter takes only its request field, not that message or its old system prompt. Six EV cases remain linked to a public hash catalog; retrieve their original inputs through authorized records before admission rather than recreating them from grades. Exporting a question is not certifying its rubric or making it a holdout.
