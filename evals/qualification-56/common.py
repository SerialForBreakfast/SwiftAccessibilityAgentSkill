import json, sys
from pathlib import Path
D=Path(__file__).resolve().parent
ROOT=D.parents[1]
V4=ROOT/'research/evaluation/signal-panel-v4'
sys.path.insert(0,str(V4/'replay'))
from prepare import packet,blocks,H,oracle,declaration,modes
PANEL=json.loads((V4/'controller.json').read_bytes())
BASE=ROOT/'evals/results/persistent-replay'
def questions():
    return packet(V4/'readiness/held.zip','5e73c208ef105df6a93364a7925363178dd527b3b7d5c8e7cbd5ed1c9180f103')
def answers():
    return packet(ROOT/'evals/results/signal-v4-review/signal-v4-return.zip','f14305f1ff84de8bd03a79752e70e15e51b0fe8e5f70008b3be855a8bfb7ff09')
