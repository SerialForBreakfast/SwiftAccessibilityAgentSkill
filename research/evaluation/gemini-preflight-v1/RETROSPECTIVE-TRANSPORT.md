# BigDog retrospective transport finding — 2026-11-07

**Disposition: strict transport qualification not established.** This answers the
[retrospective request](PUBLICATION-UPDATE.md) at db63789 for the completed
[48-session run](../gemini-controlled-run-20261107/README.md). The results remain
descriptive evidence for the configured CLI experiment. The later preflight
proposal was not the run's authorization or implementation.

| Question | Evidence and decision |
| --- | --- |
| Were the intended inputs supplied? | Rechecked all 48 sealed payload hashes and both source messages against the saved jobs. Each distinct workspace's custom-agent file contains the frozen system body; each recorded CLI invocation passes the exact user string. |
| Was the provider sent exactly two messages with those roles? | Unknown. AGY 1.5.3 loaded a custom agent and accepted a print prompt. Its recorded inputs are upstream of provider serialization. There is no captured provider envelope proving the system role, absence of startup messages, or the full tool registry. This differs from the proposed single messages envelope. |
| Was each subject isolated? | Verified 48 distinct workspace roots. The recorded configuration disabled tools, skills, plugins, MCP and command execution. Final results exposed no tool activity. Noninteractive agent listing did not confirm registration. Neither settings nor self-announcements establish independent runtime verification of controller inaccessibility or all inherited rules. |
| Which model served the requests? | The requested alias was gemini-4-argon-high. None of the 48 saved results exposed a returned model identity. The Argon quota change does not establish a serving revision. |
| Which limits applied? | Existing subscription only, extra credits off, 48 reservations used and closed, no retries. Client print timeout 300 seconds, host capture timeout 315 seconds, batch safeguard three hours. No hard provider output-token or internal-request ceiling. Historical displayed Argon weekly use went from 0% to 17%; no new quota observation was needed. |
| Was grading calibrated? | A separate reviewer graded 48 design fixtures; all labels reconciled. That supports source grading within its recorded scope. SDK freshness, native correctness of the generated answers and transport isolation remain separate questions. |

The private evidence is the completed run's jobs, per-subject intents and results,
workspace agent files, settings, adapter, authorization and closed grant. See the
[public provenance hashes](../gemini-controlled-run-20261107/summary.json).
No independent transport acceptance or provider-side captures were found. Leave
those fields unknown. A future strict comparison would need a separately qualified
adapter that exposes the actual message envelope and startup/tool configuration.
No new model session or probe was used for this report.
