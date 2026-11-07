# Skill candidate versions

Released skill remains **0.2.2**. New development candidates use semantic versions;
`-dev.N` means an unreleased research snapshot, not a release or qualification claim.

| Skill version | Purpose | State |
| --- | --- | --- |
| 0.3.0-dev.1 | Compact baseline with owner-approved default introduction and consulted-file reporting | AGY and Claude: each 6 contracts met, 1 inconclusive |
| 0.3.0-dev.2 | Evidence-driven guidance revision with the same reporting defaults | AGY: 7 contracts met; Claude: 6 met, 1 inconclusive |

Historical letter-labeled reports remain unchanged. The first snapshot derives from
historical compact A; the second derives from historical B. Their new reporting text
means neither is byte-identical to those drafts. Historical A's 144-call results must
not be represented as results for 0.3.0-dev.1. See VERSIONS.json for exact provenance.

Both introduce the skill name/version once by default and report actual consulted
reference files, with separate explicit user opt-outs. Supporting citations remain
claim-specific. No agent silently disables these defaults. Supplied references are
reported as supplied, not as autonomous retrieval.

Changing any candidate subject text requires the next unused development version;
never overwrite a frozen snapshot. Update this registry and pin hashes. Provider
model IDs (such as gemini-3.8-flash-low) stay separate from skill versions.
This directory contains research entrypoint bodies, not an additional installable skill.

See [execution status](PREPARATION-STATUS.md) for the completed AGY and Claude comparison.

The registry and EXECUTION-STATUS.json retain their historical AGY-checkpoint bytes
because the reconciliation pins them. Current Claude completion is recorded
additively in [completion status](CLAUDE-COMPLETION-STATUS-20261106.json).
