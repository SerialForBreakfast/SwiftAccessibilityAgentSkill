# Single return format (answers only)

## return.json

`return.json` is a JSON object with these fields:
- `job` = `"signal-v7-1-smoke1"`;
- `packetSHA256`;
- `status`: complete, partial or blocked;
- `stopReason`;
- `report`;
- `runLedger`;
- `cells`.

Each artifact reference is `{"path": "relative/member", "sha256": "hex digest"}`. Use actual files, not worker-local paths.

`runLedger` includes the reservation, timestamps, billed spend and approved configuration.

## Cells

Include one cell per schedule entry, even if it was never started: `id`, `arm`, `trial`, `state`, `attempts`.

| State | Required |
|---|---|
| unattempted | zero attempts and a reason |
| error | one attempt; `questionSHA256`; `skillSHA256`; `request`, `receipt`, `transport`, `usage` and `trace` artifacts; plus an `error` artifact |
| answered | everything listed for error, except that an `answer` artifact replaces the `error` artifact |

- **Reads:** `trace` lists the actual file reads as `reads`.
- **Missing telemetry:** record it explicitly inside the corresponding artifact.
- **No grades:** do not include grades or grader output.

## Checking

Run the included checker against the actual held zip, the externally supplied SHA and the final return zip. It validates structure, case accounting and hashes. It cannot attest that the worker used the approved subscription. A missing evidence lane must be disclosed, not simulated.
