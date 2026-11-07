# Project-local working files

All new working files belong inside this project. Private generated artifacts use
`evals/results/`, which is ignored by Git and visible in the project file tree.
Do not use an operating-system temporary directory or another external directory.

| Location | Contents |
| --- | --- |
| `evals/results/local-compact-b-20261106-r1/` | Frozen local-model inputs, original responses, model metadata, controller, and retained evidence |
| `evals/results/local-compact-b-20261106-r1/probes/` | Reviewed Swift sources, adaptations, compiler results and snapshots |
| `evals/results/local-compact-b-20261106-r1/communications/` | Prepared Sillycon update and messaging diagnostics; the update has not been sent |
| `evals/reports/local-compact-b-20261106/` | Published comparison, source review and sanitized metrics |

Future inference and compiler runs default to a fresh directory under
`evals/results/`. Compiler scratch files and caches use that run's `scratch/` and
`cache/` directories. The local evaluation tools reject outside-project output paths,
including paths that escape through symlinks. Existing historical records retain
their original paths and hashes; they are not rewritten to imply a different run.
