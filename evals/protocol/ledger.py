"""Attempt-reservation ledger: every session is charged to the original authorization before it opens.

A worker calls reserve() and must get a reservation back *before* launching a subject session.
The ledger is append-only JSONL, fsynced per event. It refuses:
  - any reservation after the job stopped (harness rejection, quota-read failure, isolation failure)
  - a packet other than the authorized one (a "derived" or rewritten packet is not authorization)
  - a prompt whose hash differs from the authorized cell
  - an unknown cell, a cell already reserved (no retries), or one past maxAttempts
There is no reopen, continue or reset: a new authorization is a new ledger file with a new job id.
"""
from collections import Counter
import json
import os
from pathlib import Path

STOPPING = {"harness-rejected", "quota-read-failed", "isolation-failed", "evidence-capture-failed", "quota-exhausted"}


class Refused(Exception):
    pass


class Ledger:
    def __init__(self, path, authorization):
        """authorization: dict(job, packetSHA256, maxAttempts, cells={cell: promptSHA256})."""
        self.path, self.auth = Path(path), authorization
        self.events = []
        if self.path.exists():
            self.events = [json.loads(l) for l in self.path.read_text().splitlines() if l.strip()]
            if self.events[0] != {"event": "authorize", **authorization}:
                raise Refused("ledger belongs to a different authorization")
        else:
            self._append({"event": "authorize", **authorization})

    def _append(self, event):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, "a") as f:
            f.write(json.dumps(event, sort_keys=True) + "\n")
            f.flush()
            os.fsync(f.fileno())
        self.events.append(event)

    @property
    def stopped(self):
        return next((e for e in self.events if e["event"] == "stop"), None)

    def reserved(self):
        return [e["cell"] for e in self.events if e["event"] == "reserve"]

    def reserve(self, cell, prompt_sha256, packet_sha256):
        reason = None
        if self.stopped:
            reason = f"job stopped ({self.stopped['reason']}); no further launches"
        elif packet_sha256 != self.auth["packetSHA256"]:
            reason = "packet is not the authorized packet; a derived packet creates no authorization"
        elif cell not in self.auth["cells"]:
            reason = "cell is not authorized"
        elif prompt_sha256 != self.auth["cells"][cell]:
            reason = "prompt differs from the authorized cell"
        elif cell in self.reserved():
            reason = "cell already consumed; no retries"
        elif len(self.reserved()) >= self.auth["maxAttempts"]:
            reason = "attempt limit reached"
        if reason:
            self._append({"event": "refuse", "cell": cell, "reason": reason})
            raise Refused(reason)
        self._append({"event": "reserve", "cell": cell, "n": len(self.reserved()) + 1})
        return len(self.reserved())

    def record(self, cell, outcome, stop_reason=None):
        """Record the attempt's outcome. A stop_reason in STOPPING closes the job permanently."""
        if cell not in self.reserved():
            raise Refused("outcome for a cell that was never reserved")
        self._append({"event": "outcome", "cell": cell, "outcome": outcome})
        if stop_reason:
            self.stop(stop_reason)

    def stop(self, reason):
        assert reason in STOPPING, reason
        if not self.stopped:
            self._append({"event": "stop", "reason": reason})

    def summary(self):
        outcomes = Counter(e["outcome"] for e in self.events if e["event"] == "outcome")
        attempted = len(self.reserved())
        state = ("complete" if attempted == len(self.auth["cells"]) and not self.stopped
                 else "partial" if attempted else "blocked")
        return dict(job=self.auth["job"], state=state, attempted=attempted, outcomes=dict(outcomes),
                    unattempted=len(self.auth["cells"]) - attempted,
                    refusals=sum(e["event"] == "refuse" for e in self.events),
                    stop=self.stopped["reason"] if self.stopped else None)
