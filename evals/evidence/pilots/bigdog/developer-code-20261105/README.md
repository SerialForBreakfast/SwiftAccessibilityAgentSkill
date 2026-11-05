# Gemini developer-code pilot — summary

**Useful code repairs, but no consistent benefit from adding the skill in this sample.**

Six synthetic developer-code tasks, each run once without guidance (C0) and once
with frozen skill 0.2.2 plus one manually selected reference (C2). All 12 completed.
This is a preliminary, single-reviewer static comparison, not a calibrated gold
baseline or release qualification. Full prompts, generated code and transcripts
remain private under the owner's explicit publication restriction.

| Developer task | Without guidance | Skill + reference | Practical difference |
| --- | --- | --- | --- |
| Restore a settings switch and independent Help action | Plausible core repair; redundant title remains | Plausible repair; removes redundant title stop | Small C2 improvement |
| Correct stale customer/state in a reused cell | Updates all semantic state on every configuration | Same essential fix | Tie |
| Prevent large-text checkout clipping | Scalable fonts and flexible vertical layout | Same core fix, with extra configuration | No clear gain |
| Make gesture-only deletion accessible | Documented named action and context menu; keyboard claim unverified | Undocumented role overload; ordinary alternative omitted | C2 regression |
| Make TV movie tiles remotely focusable and activatable | Native Button repair; overstates focus guarantees | Native Button repair; overstates focus guarantees | No clear gain |
| Review an already-correct native Toggle | Leaves working implementation unchanged | Leaves working implementation unchanged | Tie |

The deletion answer with guidance used an overload absent from the reviewed Apple
accessibility-action declarations. This is a **suspected invented API**, pending
Apple SDK confirmation, not a recorded compiler failure. The unguided response
also made an unsupported keyboard-shortcut claim. Neither establishes complete
keyboard usability. [Apple API declarations](https://developer.apple.com/documentation/swiftui/accessible-controls).

## Usage and execution

| Measure | C0: six invocations | C2: six invocations |
| --- | ---: | ---: |
| Reported input tokens | 13,621 | 27,962 |
| Reported output tokens | 2,714 | 2,936 |
| Total reported tokens | 16,335 | 30,898 |
| Summed invocation seconds | 53.43 | 52.45 |

Total **47,233 reported tokens** and **105.88 seconds** of invocation time.
C2 used about **1.89 times** the tokens; this is not a subscription-cost conversion
or a measurement of developer review time.

Documented CLI quota snapshots displayed 66% weekly and 99% five-hour remaining
both before and after. Whole-percent precision cannot establish the consumed delta;
unchanged display does not mean zero consumption.

- Model: `gemini-3.8-flash-low`, low effort, installed Antigravity CLI 1.5.1.
- Evaluated repository: `b73c26ed19e3832190cc63c66e3f6878598f7289`;
  released skill snapshot: 0.2.2.
- Owner approved this finite 12-invocation subscription batch; no extra allocation.
- Paid-credit fallback disabled; no retries, fallback or observed billing signal.
- Per invocation: 20 KiB explicit-input limit, 120-second process deadline,
  1 MiB captured-output limit; batch expiry 30 minutes.
- Requested output target 1,024 tokens, **not** an enforceable token cap.
  Internal model-call count and hard output-token cap remain unknown.
- Alternated condition order across cases; fresh sessions/workspaces and no agent
  file, shell, web or MCP actions. References were supplied, not retrieved.
- Role-labeled text within an installed agent is a separate lane from API-controlled
  system prompts or qualified native IDE integration. No C3 qualification claimed.

## Checks and limitations

24 spend-guard tests and three offline executor process-control checks passed.
All 12 durable operation receipts and frozen input/output hashes were retained and
checked privately. No incomplete invocations were retried or silently omitted.

No Apple SDK compilation, simulator, VoiceOver, keyboard or remote tests were run.
Fixtures are synthetic partial snippets, not production code. The reviewer was
unblinded; findings are not independently calibrated scores or accuracy rates.
An observed C0/C2 difference does not isolate the cause: instructions, reference
selection, installed-agent packaging and generation variability remain confounded.
Self-reported freshness/confidence labels are not correctness evidence.

## Next version

[Evidence-led next-version plan](../../../../NEXT-SKILL-VERSION.md): improve and
validate code-based gold fixtures, establish frozen baselines, then implement
requirement-first planning, exact API evidence, complete input-mode coverage and
honest validation reporting. Test changes against fresh cases and correct-code
controls, not only this known failure. Further subscription batches require explicit
owner approval. Released skill, existing scenarios, heldout material and v1/v2
reports remain unchanged.
