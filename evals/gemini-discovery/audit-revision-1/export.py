"""Export only the revised developer question and original supplied source."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

here = Path(__file__).resolve().parent
cases = json.loads((here / "cases.json").read_text())
subjects = {row["id"]: row["prompt"] for row in
            map(json.loads, (here.parent / "subjects.jsonl").read_text().splitlines())}
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("case", choices=cases)
case = cases[parser.parse_args().case]
source = subjects[case["parent"]]
parts = source.split("\n\n", 2)
question = case["opening"] + "\n"
if len(parts) == 3:
    request = "Explain your conclusion and give a focused check. Include integrated Swift changes if the requested behavior needs them."
    question = "\n\n".join((case["opening"], request, parts[2]))
for value, expected in [(source, case["parent_sha256"]), (question, case["prompt_sha256"])]:
    if hashlib.sha256(value.encode()).hexdigest() != expected:
        sys.exit("Question digest mismatch")
sys.stdout.buffer.write(question.encode())
