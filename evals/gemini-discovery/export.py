"""Print exactly one sealed common question, and nothing from the controller."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("id")
    args=p.parse_args()
    data=(HERE/"subjects.jsonl").read_bytes()
    s=json.loads((HERE/"seal.json").read_bytes())
    if sha256(data).hexdigest()!=s["inputsSHA256"]:sys.exit("Subject file differs from seal")
    for line in data.splitlines():
        row=json.loads(line)
        if row["id"]==args.id:
            sys.stdout.buffer.write(row["prompt"].encode())
            break
    else:sys.exit("Unknown case ID")
