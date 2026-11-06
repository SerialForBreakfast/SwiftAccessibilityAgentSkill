# Availability Sweep Difficulties

- The new metadata tranche exposed a deprecated locale accessor despite successful
  compilation. Preserve warning outcomes separately from failures. Its exact source,
  warning and repair are in the metadata tranche's revision history.
- A search for availability guards found only platform wrappers, not OS-version
  fallbacks. Do not manufacture fallback logic to satisfy a coverage count.
- Recompiling Sources does not audit test helpers or all defining declarations.
  Keep those scopes explicit and UPAIR-07 open until the declaration matrix exists.
- Sixteen pilot compilations are sixteen source sets, not sixteen independent
  accessibility correctness questions or runtime executions.

The compile report retains every warning/error line emitted in the sweep with
private paths sanitized. Raw source snapshots and diagnostics stay in immutable
private run directories; report hashes identify the originals.
