"""Deterministic packet and accounting checks; no model transport."""
import json
from collections import Counter
from copy import deepcopy
from pathlib import Path
import re
import unittest
from build import HERE, ROOT, artifacts, read, sha
from score import summarize


class Packet(unittest.TestCase):
    def test_seal_and_subject_boundary(self):
        for name,data in artifacts().items():
            self.assertEqual((HERE/name).read_bytes(),data,name)
        s=read(HERE/"seal.json"); self.assertFalse(s["authorized"])
        subjects=[json.loads(x) for x in (HERE/"subjects.jsonl").read_text().splitlines()]
        cases={r["id"]:r for r in read(HERE/"controller.json")}
        self.assertEqual([x["id"] for x in subjects],s["schedule"])
        self.assertEqual(len(set(s["schedule"])),s["cases"])
        self.assertEqual(set(cases),set(s["schedule"]))
        for x in subjects:
            self.assertEqual(set(x),{"id","prompt"})
            self.assertEqual(sha(x["prompt"].encode()),cases[x["id"]]["inputSHA256"])
            self.assertNotRegex(x["prompt"],r'(?i)negativefixtures/|deliberate mutant|controller-only|suppliedReferences|expected route|zero-base-v1')
        self.assertEqual(s["challengerSHA256"],sha((ROOT/"research/evaluation/zero-base-v1/archives/full.zip").read_bytes()))

    def test_contracts(self):
        cases=read(HERE/"controller.json"); buckets=Counter()
        for c in cases:
            self.assertTrue((ROOT/c["source"]).is_file())
            buckets[c["platform"],c["framework"]]+=1
            if c["lane"] in ("repair","preservation"):
                manifest=read(ROOT/c["source"])
                check=next(ch for ch in manifest["checks"] if ch["id"]==c["check"])
                self.assertEqual(c["assertions"],check["failureIds"])
                self.assertTrue(c["assertions"] and c["claims"])
                if c["lane"]=="repair":self.assertEqual(check["replacement"]["source"],c["sourceFile"])
            elif c.get("rubric"):self.assertTrue((ROOT/c["rubric"].split("#")[0]).is_file())
            else:self.assertTrue(c["criterion"])
        self.assertTrue(all(buckets[os,fw] for os,fw in [
            ("iOS","UIKit"),("iOS","SwiftUI"),("tvOS","UIKit"),("tvOS","SwiftUI"),("macOS","AppKit"),("macOS","SwiftUI")]))


class Accounting(unittest.TestCase):
    def setUp(self):
        self.cases=[dict(id=str(i),inputSHA256="q"+str(i),decision="one",platform="tvOS",framework="UIKit",
                         lane="repair" if i<2 else "preservation") for i in range(3)]
        self.seal=dict(model="m",challengerSHA256="s")
        self.rows=[]
        for c in self.cases:
            for arm in ("unaided","challenger"):
                v="fail" if c["lane"]=="repair" and arm=="unaided" else "pass"
                self.rows.append(dict(id=c["id"],inputSHA256=c["inputSHA256"],model="m",arm=arm,sealSHA256="h",
                    skillSHA256=None if arm=="unaided" else "s",verdict=v,primary=v,critical=False,cohort="native-low",
                    answerSHA256="fixture",rationale="fixture",evidence="fixture"))
    def score(self):return summarize(self.cases,self.rows,self.seal,"h")
    def test_shared_key(self):
        s=self.score()
        self.assertEqual(s["pairOutcomes"],{"rescued":2,"preserved":1})
        self.assertEqual(s["primaryDistinctFailures"],["one"])
        self.assertEqual(s["fullyRescuedDecisions"],["one"])
    def test_baseline_only(self):
        self.rows=self.rows[::2]
        s=self.score()
        self.assertEqual(s["primaryDistinctFailures"],["one"])
        self.assertFalse(s["fullyRescuedDecisions"])
    def test_regression_blocks_full_rescue(self):
        self.rows[-1].update(verdict="fail",primary="fail",critical=True)
        s=self.score()
        self.assertFalse(s["fullyRescuedDecisions"])
        self.assertEqual(s["regressions"],["2"])
        self.assertEqual(s["candidateCriticalFlagsNotSeenOnBaseline"],["2"])
    def test_unpaired(self):
        self.rows[1]["cohort"]="other"
        self.assertFalse(self.score()["fullyRescuedDecisions"])
    def test_reject_drift_and_retries(self):
        self.rows.append(deepcopy(self.rows[0]))
        with self.assertRaises(ValueError):self.score()
        self.rows.pop();self.rows[1]["inputSHA256"]="different"
        with self.assertRaises(ValueError):self.score()
    def test_format_is_not_primary_loss(self):
        for r in self.rows:
            if r["verdict"]=="fail":r["primary"]="inconclusive"
        self.assertFalse(self.score()["primaryDistinctFailures"])

if __name__=="__main__":unittest.main()
