# Project-local working files

All new working files belong inside this project. Private generated artifacts use
`evals/results/`, which is ignored by Git and visible in the project file tree.
Do not use an operating-system temporary directory or another external directory.

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
