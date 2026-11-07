"""Check distribution, fixture-to-scorecard pins and install smoke independently of model runs."""
import argparse
from collections import Counter
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys
from zipfile import ZipFile

sys.dont_write_bytecode = True
RC = Path(__file__).resolve().parent
sys.path.insert(0,str(RC/"grader"))
from tasks import TASKS
from grade import oracle
spec = importlib.util.spec_from_file_location("rcbuild",RC/"package/build.py")
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)


def check(receipt, installed=None):
    if not __debug__:
        raise RuntimeError("normal Python assertion checking required")
    distribution = RC/"swift-accessibility-agent-0.3.0-rc.1.zip"
    expected = package.contents()
    with ZipFile(distribution) as archive:
        assert len(archive.namelist()) == len(expected)
        for name,data in expected.items():
            assert archive.read("swift-accessibility-agent/"+name) == data
            if installed:
                assert (installed/name).read_bytes()==data
    assert set(Counter((t.platform,t.framework) for t in TASKS).values()) == {2}
    assert len({(t.platform,t.framework) for t in TASKS})==6
    card = json.loads(receipt.read_bytes())
    assert card["accepted"] and len(card["rows"])==36
    lookup={(r["task"],r["variant"]):r for r in card["rows"]}
    for t in TASKS:
        assert (RC.parents[1]/"code-examples"/t.source/"manifest.json").is_file()
        for variant in ("reference","alternative","mutant"):
            r=lookup[t.id,variant]
            assert r["compiled"] and r["status"]==("contract-failure" if variant=="mutant" else "pass")
            for key,data in (("submissionSHA256",t.solution(getattr(t,variant))),("oracleSHA256",oracle(t))):
                assert r[key]==sha256(data.encode()).hexdigest()
    print(f"PASS: archive ({len(expected)} files), six cells, 36 compiled fixture outcomes and source/oracle pins.")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--receipt",type=Path,default=RC/"scorecard.json")
    parser.add_argument("--installed",type=Path)
    args=parser.parse_args()
    check(args.receipt,args.installed)
