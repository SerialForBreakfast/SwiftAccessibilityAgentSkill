# UIKit pilot revision2 results

All eight bounded checks matched their expectations on the local Apple worker.
This is candidate library evidence, not an annual anchor or gold-prompt promotion.

| Lane | Check | Expected and observed |
| --- | --- | --- |
| Compile | Three-example library | Successful type-check |
| Compile negative | Wrong label value type | Intended Int-to-String diagnostic |
| Unit | Independent row actions | Pass |
| Unit negative | Hidden descendants | Intended assertion failure |
| Unit | Same-instance cell state | Pass |
| Unit negative | Stale status | Intended assertion failure |
| Unit | Text configuration/payment callback | Pass |
| Unit negative | Scaling disabled | Intended assertion failure |

[Structured results](pilot-r2-results.json) record exact manifest and per-run
adapter/log/result hashes, toolchain/runtime identity, executed IDs, counts and
sanitized diagnostic/assertion excerpts. Each unit invocation ran exactly one
focused test with zero skips. An expected-negative check passes because the
specified failure occurred, not because its Swift test passed.

Toolchain: Xcode27.0 build27A266a, Swift6.4, iOS Simulator SDK27.0 build24A430,
arm64, deployment target26.0. Unit destination: iOS26.5 build23F77. Compile checks
do not claim runtime execution. Raw outputs, manifest/source/adapter snapshots,
command intents and xcresults remain in private local run directories.

Two earlier revision1 compile attempts are retained separately: a positive pass
and a failed negative-diagnostic match. The latter expected `String?` but the
compiler printed `String`. Revision2 captures that observed wording; it does not
rewrite the failed attempt. See the [revision history](../README.md).

The native input snapshots include the exact adapter used per invocation. Minor
unused-import cleanup happened between invocations; each adapter hash is recorded
instead of claiming every job used identical adapter bytes. Swift source and test
inputs are fixed by the same revision2 manifest across all eight checks.

No model calls, UI tests, screenshot checks, required manual verification or
simulator downloads occurred. The dedicated simulator is shut down. No test job
remains active. Frozen skill/baseline files and original evaluation fixtures were
not edited. Independent review of this new adapter/pilot and any future anchor
promotion remain separate steps.
