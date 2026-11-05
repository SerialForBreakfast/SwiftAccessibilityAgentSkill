# Worker request: return existing evidence through Git

Recipients: BigDog and MaxMini. Delivery: owner-pushed Git commits or copy/paste only.
No coordinator contact. This request prioritizes export and review of existing runs,
not additional inference, paid calls, model downloads, or continuation of old batches.

## BigDog request

Please review the latest evaluation changes and commit a sanitized evidence bundle
for any completed work beyond the already published smoke/development-v1 artifacts.
If nothing newer ran, commit a short status noting that fact, your current capability
confirmation and blockers. Do not rerun old cases to fill missing evidence.

For already-published runs, link the original immutable artifact paths and hashes
rather than copying or rewriting them. Return exact model/runtime/template identities,
tokenizer and tool support, and whether the portable pilot contract can be enforced.
Small-model inference is now a diagnostic lane, not our primary release target.
Do not launch a broader local campaign in response to this request.

## MaxMini request

Please commit sanitized evidence for the reported 32-cell comparison (34 generation
requests, three truncations), and the subsequent 24-cell batch (23 answers and one
timeout, including the three-cell continuation). Those counts are currently peer
reports; the shared repository needs the underlying records to verify them.

Include the prepared randomized review packets, original source/input hashes and
selected compiler checks. Keep private A/B mappings separate from judge-facing
packets; the controller may retain mappings in the evidence bundle, but must never
send them to a blinded judge. Explain the D04/D09/D11 ambiguities without editing
the original questions. Coordinator cursors are not an accessible evidence handoff.

Return the original qualification evidence linking the installed model manifest,
weights-layer hash and serving runtime. Distinguish these different hashes. The new
adapter checks are for future experiments; do not claim they were used historically.

## Bundle layout

Use a new directory per worker and original run:

```text
evals/evidence/worker-results/<bigdog|maxmini>/<original-run-id>/
  README.md                 # provenance, approval, limits, missing evidence
  manifest.json             # sanitized original manifest with provenance
  records.jsonl             # effective prompts, answers, actual read traces
  outcomes.jsonl            # every planned cell, including timeout/unattempted
  checksums.json            # SHA-256 of every exported file except this index
  redactions.json           # field paths/categories and impact; never secret values
  requests/                 # synthetic/public request and response evidence
  qualification/            # public-safe identity and capability evidence
  grading/                  # existing reviews, clearly labeled provisional
  sdk/                      # snippets, wrappers, SDK/build/targets, diagnostics
```

Retain original IDs, input revisions, finish reasons, available token telemetry,
request counts, partial responses and failure states. Record absent evidence as
unavailable. Do not fabricate portable receipts for historical runs that used a
different contract. If adapting records, preserve the sanitized original and label
derived records with transformation version and source hash.

## Sanitization and audit

1. Export only public/synthetic fixture material. Remove credentials, authorization
   headers, endpoints, personal absolute paths, host/account identifiers and unrelated
   private code/messages. Inspect both prompts and model outputs.
2. Keep originals privately unchanged. Generate export hashes after redaction; do not
   present them as original hashes. Preserve original hash references where safe.
3. Log each redacted field/category and whether it affects grading. If sanitization
   changes relevant code or question meaning, mark that cell ungradable from the
   export. Never include removed secret values in the log.
4. Include all cells, not only successful or attractive answers. Missing source
   records remain visible. Separate generation evidence, existing reviews and SDK
   diagnostics. Neither compilation nor a reviewer score proves user usability.
5. Run offline tests and integrity checks. Stage only the new bundle and a short
   status link. Do not force-add ignored result trees, rewrite historical reports,
   touch images, alter heldout questions or include unrelated files.
6. Commit with the worker/run IDs in the message and return the commit hash. Push
   through the owner's approved Git route without force-pushing or discarding work.

## Acceptance before grading

We will check hashes, reconcile planned/completed/failed/missing cells, verify
effective prompt and model identities, and identify comparable subsets. Only then
will we create judge packets against fixed primary-source criteria. Ambiguous or
redacted cases stay separately unassessed pending adjudication. A handoff can be
accepted as complete accounting even when some answers or measurements are missing.

No new quality dashboard or skill release should imply that these diagnostic local
runs establish effectiveness for frontier coding agents. See [target strategy](TARGET-EVALUATION.md).
