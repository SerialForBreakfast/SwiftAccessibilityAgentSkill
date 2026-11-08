"""Attempt-reservation ledger: every session is charged to the owner's budget before it opens.

The owner sets the budget and the policy in the authorization; the ledger enforces what was chosen.
A worker must call reserve() and get a reservation back *before* launching a subject session.
The ledger is append-only JSONL, fsynced per event.

Authorization fields:
  job, packetSHA256, maxAttempts, cells={cell: promptSHA256}
  policy (optional; defaults to STRICT):
    onInterruption  "end-job"   a delivery interruption ends the job with one partial return
                    "continue"  the worker may fix delivery and keep going inside the same budget
    promptRevisions "refuse"    only the authorized prompts may run
                    "new-cohort" the worker may register revised prompts (with a reason); their
                                sessions are charged to the same budget and labeled as a separate
                                cohort, which is analyzed as a separate comparison, never pooled

Always enforced, whatever the policy: the budget, no retry of a cell within a cohort, unknown cells
refused, and a stop for quota exhaustion or isolation failure (those end the job outright).
"""
from collections import Counter
import json
import os
from pathlib import Path

STRICT = {"onInterruption": "end-job", "promptRevisions": "refuse"}
INTERRUPTIONS = {"harness-rejected", "quota-read-failed", "evidence-capture-failed"}  # owner decides
TERMINAL = {"quota-exhausted", "isolation-failed"}  # always end the job
SEALED = "sealed"


class Refused(Exception):
    pass


class Ledger:
    def __init__(self, path, authorization):
        self.path = Path(path)
        self.auth = dict(authorization, policy={**STRICT, **authorization.get("policy", {})})
        self.events = []
        if self.path.exists():
            self.events = [json.loads(l) for l in self.path.read_text().splitlines() if l.strip()]
            if self.events[0] != {"event": "authorize", **self.auth}:
                raise Refused("ledger belongs to a different authorization")
        else:
            self._append({"event": "authorize", **self.auth})

    def _append(self, event):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, "a") as f:
            f.write(json.dumps(event, sort_keys=True) + "\n")
            f.flush()
            os.fsync(f.fileno())
        self.events.append(event)

    def _of(self, kind):
        return [e for e in self.events if e["event"] == kind]

    def cohorts(self):
        out = {SEALED: dict(packetSHA256=self.auth["packetSHA256"], cells=self.auth["cells"])}
        for e in self._of("revise"):
            out[e["cohort"]] = dict(packetSHA256=e["packetSHA256"], cells=e["cells"])
        return out

    @property
    def ended(self):
        return next((e for e in self._of("stop") if e["ends"]), None)

    def revise(self, cohort, packet_sha256, cells, reason):
        """Register revised prompts as a new cohort. Allowed only if the owner's policy says so."""
        if self.auth["policy"]["promptRevisions"] != "new-cohort":
            self._append({"event": "refuse", "cohort": cohort, "reason": "policy refuses prompt revisions"})
            raise Refused("policy refuses prompt revisions")
        if self.ended or cohort in self.cohorts() or not reason or not set(cells) <= set(self.auth["cells"]):
            self._append({"event": "refuse", "cohort": cohort, "reason": "invalid revision"})
            raise Refused("invalid revision: job ended, cohort exists, no reason, or unknown cells")
        self._append({"event": "revise", "cohort": cohort, "packetSHA256": packet_sha256,
                      "cells": cells, "reason": reason})

    def reserve(self, cell, prompt_sha256, packet_sha256, cohort=SEALED):
        cohorts, reserved = self.cohorts(), self._of("reserve")
        c = cohorts.get(cohort)
        reason = None
        if self.ended:
            reason = f"job ended ({self.ended['reason']}); no further launches"
        elif c is None:
            reason = "cohort is not registered; a derived packet needs a policy-allowed revision"
        elif packet_sha256 != c["packetSHA256"]:
            reason = "packet does not match this cohort"
        elif cell not in c["cells"]:
            reason = "cell is not authorized"
        elif prompt_sha256 != c["cells"][cell]:
            reason = "prompt differs from the registered prompt for this cohort"
        elif any(r["cell"] == cell and r["cohort"] == cohort for r in reserved):
            reason = "cell already consumed in this cohort; no retries"
        elif len(reserved) >= self.auth["maxAttempts"]:
            reason = "budget reached"
        if reason:
            self._append({"event": "refuse", "cell": cell, "cohort": cohort, "reason": reason})
            raise Refused(reason)
        self._append({"event": "reserve", "cell": cell, "cohort": cohort, "n": len(reserved) + 1})
        return len(reserved) + 1

    def record(self, cell, outcome, cohort=SEALED, stop_reason=None):
        if not any(r["cell"] == cell and r["cohort"] == cohort for r in self._of("reserve")):
            raise Refused("outcome for a cell that was never reserved")
        self._append({"event": "outcome", "cell": cell, "cohort": cohort, "outcome": outcome})
        if stop_reason:
            self.stop(stop_reason)

    def stop(self, reason):
        assert reason in INTERRUPTIONS | TERMINAL, reason
        ends = reason in TERMINAL or self.auth["policy"]["onInterruption"] == "end-job"
        if not self.ended:
            self._append({"event": "stop", "reason": reason, "ends": ends})

    def summary(self):
        by = {}
        for name in self.cohorts():
            res = [r for r in self._of("reserve") if r["cohort"] == name]
            out = Counter(e["outcome"] for e in self._of("outcome") if e["cohort"] == name)
            by[name] = dict(attempted=len(res), outcomes=dict(out),
                            unattempted=len(self.cohorts()[name]["cells"]) - len(res))
        attempted = len(self._of("reserve"))
        complete = all(v["unattempted"] == 0 for v in by.values()) and not self.ended
        return dict(job=self.auth["job"], policy=self.auth["policy"], budget=self.auth["maxAttempts"],
                    state="complete" if complete else "partial" if attempted else "blocked",
                    attempted=attempted, cohorts=by,
                    interruptions=[e["reason"] for e in self._of("stop")],
                    refusals=Counter(e["reason"].split(" (")[0] for e in self._of("refuse")),
                    ended=self.ended["reason"] if self.ended else None)
