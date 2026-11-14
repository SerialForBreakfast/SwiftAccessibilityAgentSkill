"""Verify the private return; emit a public answer-hash index and review triage."""
import argparse
import csv
import hashlib
import io
import json
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
SEAL = '31c7cd786df83753e415b382c5ba87d7800528b352d3c7416b70a5d921f2381e'
# Explicit recommendations read in controller order, not correctness labels.
PATCH_NO = {1,2,3,4,5,6,7,9,10,11,13,14,15,17,18,19,20,21,22,23,25,26,27,29,30,31,33,34,35,36,37,38,39,41,42,43,45,47,49,51,53,55,57,59,60,61,63,65,66,67,69}
CODE_YES = {5,16,20,30,32,37,40,45,60,64,65,70,71}
# Cell 16 explicitly concludes that the moved button works as intended.
def digest(data):
    return hashlib.sha256(data).hexdigest()

def need(condition, message):
    if not condition:
        raise ValueError(message)

def run(bundle):
    need(digest(bundle.read_bytes()) == SEAL, 'outer seal')
    with ZipFile(bundle) as z, ZipFile(PACKET/'subjects.zip') as subjects:
        def load(name):
            return json.loads(z.read(name))
        index = load('SHA256.json')
        need(len(z.namelist()) == len(set(z.namelist())) and set(z.namelist()) == set(index) | {'SHA256.json'}, 'manifest membership')
        for path, h in index.items():
            need(digest(z.read(path)) == h, path)
        for name in ('controller.json', 'subjects.zip', 'freeze.json', 'GRADING.md'):
            need((PACKET/name).read_bytes() == z.read('controller/'+name), name)
        schedule = json.loads(subjects.read('schedule.json'))
        catalog = json.loads((PACKET/'controller.json').read_bytes())
        freeze = load('controller/answer-freeze.json')
        mapping = load('controller/private-map.json')
        blind = {v:k for k,v in mapping.items()}
        ids = {r['id'] for r in catalog}
        need(len(ids) == len(mapping) == len(schedule) == 500 and ids == set(blind) == set(freeze) == {r['id'] for r in schedule}, 'coverage')
        modes = {}
        rows = []
        times = []
        tokens = 0
        for r in catalog:
            i,mode = r['id'],r['mode']
            base = 'raw/'+i+'/'
            prompt = subjects.read(r['path'])
            answer = z.read(base+'answer.txt')
            receipt,req = load(base+'receipt.json'),load(base+'request.json')
            need(prompt == z.read(f'blind/{blind[i]}/prompt.md') == req['argv'][-1].encode() and digest(prompt) == r['promptSHA256'], i+' prompt')
            need(answer.strip() and answer == z.read(f'blind/{blind[i]}/answer.txt') and digest(answer) == receipt['answer_sha256'] == freeze[i], i+' answer')
            need(req['index'] == receipt['index'] == i and req['arm'] == receipt['arm'] == 'unaided' and receipt['status'] == 'SUCCESS' and receipt['rc'] == 0 and req['skillSHA256'] is None, i+' condition')
            times.append(load(base+'reservation.json')['at'])
            tokens += receipt['usage']['total_tokens']
            n = modes.get(mode,0)
            modes[mode] = n+1
            key = observed = direction = ''
            if mode in ('patch-review','code-review'):
                prefixes = ('Accept the scoped fix.', 'Reject the regression.') if mode=='patch-review' else ('Preserve the working path.', 'Repair the supplied path.')
                need(r['required'].startswith(prefixes), i+' key')
                key = 'yes' if r['required'].startswith(prefixes[0]) else 'no'
                positive = n not in PATCH_NO if mode=='patch-review' else n in CODE_YES
                observed = 'yes' if positive else 'no'
                direction = 'agrees' if key==observed else 'inspect'
            rows.append([i,r['platform'],r['framework'],mode,r['promptSHA256'],freeze[i],key,observed,direction or 'not-assessed'])
        need(tokens == load('SUMMARY.json')['reportedTokens']['total_tokens'], 'usage')
        print('Verified',len(index),'members;',tokens,'reported tokens; reservation range:',*[datetime.fromtimestamp(t,ZoneInfo('America/Los_Angeles')).isoformat() for t in (min(times),max(times))])
    stream = io.StringIO()
    writer = csv.writer(stream,lineterminator='\n')
    writer.writerow(['id','platform','framework','mode','promptSHA256','answerSHA256','keyDirection','answerDirection','triage'])
    writer.writerows(rows)
    return stream.getvalue()

if __name__=='__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('bundle',type=Path)
    p.add_argument('--write',action='store_true')
    a=p.parse_args()
    data=run(a.bundle)
    dest=HERE/'index.csv'
    if a.write:
        dest.write_text(data)
    else:
        need(dest.read_text()==data,'index drift')
