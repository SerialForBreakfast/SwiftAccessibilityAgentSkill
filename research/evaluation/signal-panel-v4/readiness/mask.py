"""Create private, arm-masked calibration inputs before reading native outcomes."""
import hashlib,json,random,re,secrets
from pathlib import Path
from zipfile import ZipFile
D=Path(__file__).resolve().parent
ROOT=D.parents[3]
OUT=ROOT/'evals/results/signal-v4-calibration'
H=lambda b:hashlib.sha256(b).hexdigest()
def prepare():
    OUT.mkdir(exist_ok=False)
    ret=ROOT/'evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip'
    assert H(ret.read_bytes())=='9929eb1bddb1eb850bdc6ff026bb0469852e8ecab19ef7100689595788990368'
    rows=[r for r in json.loads((D.parent/'controller.json').read_bytes()) if r['id'][2:6] in {'4099','be25','35ee','9062','7d27'}]
    jobs=[(r,arm) for r in rows for arm in ('unaided','skill')]
    assert len(jobs)==10
    random.SystemRandom().shuffle(jobs)
    key={}
    with ZipFile(ret) as z, ZipFile(D.parents[1]/'signal-panel-v2/held.zip') as q:
        for n,(r,arm) in enumerate(jobs,1):
            slot=f'B{n:02}'; w=OUT/slot;w.mkdir()
            raw=z.read(f'records/{r["id"]}.{arm}/answer.txt')
            text=raw.decode()
            text=re.sub(r'(?im)^.*(?:ROUTING:|Swift Accessibility Agent|signal-v2|\.agents/skills/).*(?:\n|$)','',text)
            (w/'answer.txt').write_text(text)
            question=q.read(f'subjects/{r["id"]}.txt'); assert H(question)==r['questionSHA256']
            (w/'question.txt').write_bytes(question)
            key[slot]=dict(id=r['id'],arm=arm,answerSHA256=H(raw),maskedSHA256=H(text.encode()))
    (OUT/'key.json').write_text(json.dumps(key,indent=2))
if __name__=='__main__':prepare()
