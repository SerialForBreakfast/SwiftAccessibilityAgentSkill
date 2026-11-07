# BigDog | Released 0.2.2 vs 0.3.0-rc.1

**Prepared, not dispatched.** On authorized delivery, this is one job and one return. Run the 36 cells in packet order on native Claude Code, exact model and effort in packet.json, existing subscription only. No paid usage, probes, retries, repairs, fallback, extra judge calls or follow-up sessions. An attempted session consumes its cell even if it errors or yields no answer. Normal read-only skill lookup within that session is not a retry. Do not carry forward any prior grant.

## Offline preflight

1. Verify packet.json against the digest supplied at delivery, then run `python3 -B evals/rc1-comparison/prepare.py --verify` at repo root. It checks the exact questions, controller and runtime bytes. Use the indicated source revision plus this packet. Do not expose the controller checkout to the subject.
2. Confirm non-metered subscription mode, extra usage off, named model selectable, quota available, authenticated private return share accessible, and raw answer/tool-event capture available without inference. Record CLI version, settings and usage windows. If these cannot be established, return blocked without probing.
3. Stage two clean native installations under the same skill name using the existing qualified read-only native plugin path. For released, copy **only** the releaseRuntime paths with their hierarchy; for rc.1 extract the pinned archive. Verify the staged files against the inventory/archive. No global duplicate, controller files, hidden tests, previous chat, network tools or cross-arm access. Use the same settings and fresh empty project/session per cell. Record catalog and isolation evidence; stop on leakage, transport drift or hash mismatch.

## Execute the frozen schedule

Give each subject exactly the UTF-8 text from subjectExports[task], including its trailing newline. For explicit cells only prepend explicitPrefix; verify the resulting hash against the cell. Explicit means requesting the installed skill, not injecting its body. Do not prepend a framework label or accessibility hint, even on repeat cells. Do not tell subjects their arm. Capture complete inputs, original outputs/errors and actual native events. Stop before paid fallback, quota exhaustion, or when required isolation/evidence capture fails. Mark remaining cells unattempted; do not replace failures or send an interim acknowledgment.

| Question | Comparison | Denominator if complete |
|---|---|---|
| What changes for a developer using the normal workflow? | First automatic answer for each version, same task, including non-invocations | 12 paired tasks / 24 sessions |
| How often does released disagree with itself? | Six fresh automatic repeats against their first released answer, one per OS/framework combination | 6 repeat pairs / 6 additional sessions |
| Does asking for the skill change activation or quality? | Explicit vs first automatic within each version, same three tasks (one per OS) | 6 within-version contrasts / 6 additional sessions |

Report attempted, comparable, missing and ungradable denominators separately. Do not pool repeats as new tasks. Six repeats describe observed disagreement, not a stable population noise floor. These are known development cases; some questions are ordinary app policy. An automatic non-invocation is an observation, not necessarily a routing defect.

## Grade once; deliver the evidence, not just totals

Use the pinned RC1 rubric and original task interface identically for both arms. Mask arm/version and randomize presentation before independent offline grading; preserve originals, masked copies, presentation order and the controller mapping. Accept equivalent implementations. Do not edit code to make it compile. Record output-format compliance separately. Grade quality separately from catalog advertisement, invocation, body load, reference reads and self-reported routing. For activation cite native event IDs/paths; absent telemetry is unknown, not a confirmed miss.

Use existing authorized grading facilities only. Preserve submitted bytes, original diagnostics, environment, assertions and outcomes for any unchanged native grade. Do not provision a VM, bypass external-submission safeguards or execute on a credentialed host. If native grading is unavailable, include the full source-level rubric assessment and the replay-ready originals in this return; mark native outcomes unavailable and the native grading lane incomplete. A source verdict is not a compile/unit pass. Report a grader/interface mismatch as a harness gap, not a model failure. Do not infer rendered accessibility from these units.

Return **one** private bundle to the project's existing `smb://sillycon.local/sharedstatusfile/joe-big-dog/` return location, with one controller message giving readable location, byte size, digest and complete/partial/blocked status. No public Git transcripts. Follow evals/BIGDOG-SINGLE-EXCHANGE.md (pinned). Include:

- A 36-row index: cell, task, arm, invocation mode, attempt state, session ID, returned model, stop reason, artifact paths and hashes. For unattempted cells give the reason. Include actual quota/usage, tokens and latency where available; mark unavailable telemetry explicitly.
- Exact subject inputs, original first answers/errors, sanitized native traces and permission/settings records; keep credentials out. Record redactions and limitations. Provide raw and masked grading inputs, original reviewer output, per-criterion verdict, decisive excerpts on both sides, rationale, accepted alternatives, critical losses, and any native scorecards or harness gaps. Index every artifact and verify it from the delivered bundle.
- One summary: automatic gains/losses/both-pass/both-fail/inconclusives, repeat agreement/disagreement, explicit invocation vs automatic contrasts, and measured reads vs announcement. Flag any newly lost ordinary action or navigation path regardless of totals. Explain missing comparisons rather than imputing grades. No release decision or second handoff is implied.
