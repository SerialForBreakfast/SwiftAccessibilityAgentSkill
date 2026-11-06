# Additive correction: Finder metadata is not evidence

Authorized November 6, 2026. The original platform collector recursively included
`code-examples/platforms/.DS_Store`. Finder later changed that folder metadata,
causing an integrity failure despite unchanged source/test/manifest files.

The original results index, collection script, native receipts, archive and recorded
hashes remain unchanged. [amendment.json](amendment.json) pins the original index
and records exactly one non-evidence exclusion. The `.DS_Store` file itself is not
deleted, restored or edited. The historical record still shows what was collected.

The current verifier applies this explicit correction. Because that verifier was
itself pinned in the original index, its exact original source is preserved in
[original-platform-evidence.test.mjs.txt](original-platform-evidence.test.mjs.txt).
The old verifier pin is checked against that preserved copy; every other substantive
pin continues to match its original path. The verifier permits no additional excluded
paths or superseded verifiers through this amendment.

The next batch collector uses an explicit source/document extension allowlist and
ignores hidden metadata. No frozen baseline, released skill, native assertion or
historical test outcome is changed. A housekeeping correction is not a new passing
accessibility test or a model failure.
