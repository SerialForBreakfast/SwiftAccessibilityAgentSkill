# Held job: signal-v7-smoke1

**This packet is not permission to run.** Dispatch only with owner approval that names this seal, the transport, the model, the scope, the quota and the stop policy.

## Proposed run

- **Transport:** the same AGY Gemini 3.8 Flash Low subscription transport as signal-v6 run 1. Subscription only, zero extra spend.
- **No probing:** confirm availability without probing.
- **No extras:** no fallback, retry, judge model, continuation grant or other worker request.
- **Scope:** at most 56 first attempts, one per question, all on the signal-v7 arm. This is not a standing cap. If the scope changes, reseal before dispatch.

## Arm and isolation

- **Skill:** install `signal-v7` exactly as `arms/signal-v7.zip`.
- **Input:** use `subjects/` verbatim as the only developer input.
- **Sessions:** one fresh, isolated workspace and session per question.
- **Settings:** use the same automatic skill discovery, model revision, settings, tool permissions and neutral envelope as signal-v6 run 1.
- **Nothing shared:**
  - no shared context between cells;
  - no working checkout, evaluator files, historical answers or hidden harness in subject access.
- **No interference:** do not force a read, and do not discard non-invocations.
- **Before execution:** validate `SHA256.json` and the external packet SHA.

## Stop policy

- **Stop immediately** if model identity, quota, isolation, transport or evidence capture fails. No repair or resend.
- **Batches:** run `schedule.json` in order, in batches that fit the approved quota window. Stop at the owner's quota limit.
- **Partial return:** a partial return lists the attempted cells. Return blocked if there is no usable evidence.

## Evidence

**No grading in this job.** Preserve, for each cell:
- the verbatim raw answer, or the exact error;
- the actual envelope, the settings and the install receipt;
- the session and tool transcripts and the actual file reads;
- usage and latency when exposed.

Record unavailable telemetry explicitly.

## Return

- **Delivery:** one `signal-v7-smoke1-return.zip` via the established private joe-big-dog share. It contains `return.json` plus all referenced evidence, under `controller/RETURN.md` and the single-exchange checklist.
- **Privacy:** never publish private answers.
- **Self-check:** verify the zip with `controller/check_return.py` before returning it.
- **Report:** give the planned, attempted and answered counts, the cells that opened `SKILL.md`, and which reference files each cell read.
- **Claims:** make no comparison or causal claim. This is a single exchange: no second handoff.
