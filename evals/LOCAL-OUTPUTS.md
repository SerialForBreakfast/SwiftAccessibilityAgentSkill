# Project-local working files

All new working files belong inside this project. Private generated artifacts use
`evals/results/`, which is ignored by Git and visible in the project file tree.
Do not use an operating-system temporary directory or another external directory.

## What to commit

| Commit to Git | Keep local under `evals/results/<run-id>/` |
| --- | --- |
| Questions, fixture definitions, rubrics, runner source and offline checks | Original answers, worker deliveries, request/receipt files and private join maps |
| Reviewed summaries, case IDs, artifact hashes and bounded assertion excerpts | Materialized replay projects, full diagnostics, result bundles and compiler caches |
| Reviewed public starter or candidate archives required by an existing seal | Subject ZIPs regenerated from private inputs and scratch archives |

For example, the [proof-repair replay board](proof-repair-20/replay/RESULTS.md)
can be read from a clean checkout. Re-executing that historical replay requires
the original private returns; their hashes are evidence pointers, not downloads.
Keep new reusable code beside its campaign and every run under the single
private root. A campaign's own `results/README.md` can be public; do not
globally ignore `results/`, ZIP files, or JSON. Before publishing, run
`sh scripts/check-publication-boundary.sh` from the repository root and review
the staged contents. Ignore rules screen paths, not secrets inside allowed files.

| Location | Contents |
| --- | --- |
| `evals/results/local-dev5-20261107-r1/` | Local dev.5 three-arm diagnostic: frozen inputs, exact requests/responses, model identities, events and separate controller review |
| `evals/results/local-dev5-20261107-r2/` | Continuation of only unattempted cells after the approved 90-minute time amendment; no repeated calls |
| `evals/results/local-dev5-20261107-r3/` | Remaining unattempted cells after a retained request timeout; timed-out cells are not repeated |
| `evals/results/local-dev5-20261107-r4/` | Final unattempted cells under adaptive coverage/paired-comparison order; original global deadline and quota retained |
| `evals/results/local-dev5-preflight/` | Offline plan and project-local scratch for package/harness checks |
| `evals/results/local-dev5-preflight/git-ref-quarantine/` | Preserved invalid duplicate `origin/HEAD 2` ref and hash from fetch repair |
| `evals/reports/local-dev5-20261107/` | Sanitized bounded-run results, source review, usage and qualifications |
| `evals/results/local-compact-b-20261106-r1/` | Frozen local-model inputs, original responses, model metadata, controller, and retained evidence |
| `evals/results/local-compact-b-20261106-r1/probes/` | Reviewed Swift sources, adaptations, compiler results and snapshots |
| `evals/results/local-compact-b-20261106-r1/communications/` | Prepared Sillycon update and messaging diagnostics; the update has not been sent |
| `evals/reports/local-compact-b-20261106/` | Published comparison, source review and sanitized metrics |

Future inference and compiler runs default to a fresh directory under
`evals/results/`. Compiler scratch files and caches use that run's `scratch/` and
`cache/` directories. The local evaluation tools reject outside-project output paths,
including paths that escape through symlinks. Existing historical records retain
their original paths and hashes; they are not rewritten to imply a different run.

## Sillycon evaluation returns

When sending completed or partial evaluation results to Sillycon, include the controller evidence with the first results notice. Publish the sanitized summary in Git and deliver the answer-level material through the established private project share. Give the results revision, share location, archive size, SHA-256 and entry point in the project inbox. Verify the uploaded bytes before sending.

For each completed attempt, link the sealed input and complete original answer to its masked ID, original answer hash, criterion verdicts, verbatim evidence spans, reviewer rationale, integration judgment and critical flags. Include the masked packet and grade files with their published hashes. Complete answers let the recipient inspect omissions such as a button whose action was never connected. Include per-arm results, recorded usage, stop reasons, unattempted cells and known evidence gaps. Keep credentials, account identifiers and raw session metadata out of the transfer. Keep answer keys in the controller bundle. Record the inbox receipt separately from recipient acknowledgment.
