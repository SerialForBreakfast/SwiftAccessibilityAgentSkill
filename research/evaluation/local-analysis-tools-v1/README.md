# Off-the-shelf local analysis checkpoint

Executed without model generation or additional spend. Released skill, frozen
baselines and native evidence remain unchanged. Tool code and reports are uncommitted.

## Results

| Lane | Recorded result | Scope |
| --- | --- | --- |
| Ajv 8.17.1 | 15 records pass | Draft controller, evidence ledger, 13 distinct manifests |
| Xcode SwiftSyntax / SwiftParser | 110 files parse; 346 test functions have direct XCTest assertions | Syntax observations, not assertion adequacy or compilation |
| SwiftLint 0.65.1 | Zero findings | Four selected code-quality rules, not all SwiftLint rules |
| markdownlint 0.38.0 | Zero findings | Four selected current documents, not the whole research archive |
| Promptfoo 0.125.1 | 26 preserved excerpt equality checks pass | Replay infrastructure, not whole-answer or accessibility grading |

The [report](report.json) contains source hashes, syntax observations and tool
fingerprints. The [first successful run](first-success.json) remains separate.
Working logs are retained locally with [published hashes](attempt-log-hashes.json).

Seventeen adapter regression tests also exercise deliberately bad inputs: missing
fields, invalid hashes/status, invented outputs, malformed Markdown/Swift, an actual
forced cast, changed replay text and forbidden judge/executable assertion types.

The broader offline regression suite passes 689 checks, including all 17 adapter tests.
These counts describe checks, not independent accessibility behaviors.

## Boundaries and useful next steps

The exact-text replay proves preserved text reaches deterministic assertions. It is
not evidence the answers are correct. Allowlisted contains/not-contains/JSON checks
are also available, but their expectations require reviewed contracts. The public
historical local-model summary has 36 answer hashes/grades, not full answer text;
those answers were not reconstructed or silently replaced by excerpts.

Use syntax-derived test declarations and assertion calls to replace weak name-only
leads in the qualification ledger next. Each proposed criterion still needs actual
assertion/source review; assertion count is not semantic coverage. Continue using
existing native receipts for behavior and bounded native runs when needed.

Distillation remains downstream of source-backed contracts and an approved paired
model evaluation. No automatic release promotion or new frontier batch follows this
checkpoint. Independent review and three primary-source mapping gaps remain open.

## Reproduction

See [tool setup and commands](../../../tools/local-analysis/README.md).
Dependencies are repository-local and ignored, with pinned manifests and a lockfile.
Dependency scripts were disabled. SwiftLint was downloaded as a Homebrew bottle and
extracted locally, not globally installed. SwiftSyntax uses selected Xcode host modules;
the compiler version is recorded in the report. No new Swift dependency was fetched.
Promptfoo's broader dependency tree is installed, but this lane uses only a captured
provider and deterministic checks; no cloud provider or LLM judge is configured.

The runner creates a new attempt folder on each run and refuses report overwrite. Findings from
historical examples are advisory and do not authorize changing evidence files.

## Integration failures retained

1. An incorrect default Markdown import failed before analysis. A second guessed
   named import also failed; inspecting the pinned package established `lint`.
2. SwiftLint tried a global cache; using its supported `--no-cache` isolated the run.
3. Promptfoo tried its default home-directory config; the adapter now supplies a
   repository-local directory. A URL pathname initially retained encoded spaces;
   `fileURLToPath` fixed that path conversion.
4. A failed shell edit briefly left the path helper unimported; the import was added
   with a verified patch before replay resumed.

These are adapter/authoring defects, not accessibility failures or subject-model
outcomes. No native example was repaired or regraded because of them.
