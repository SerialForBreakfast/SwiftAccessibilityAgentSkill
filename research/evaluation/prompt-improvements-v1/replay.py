"""Offline integration lane. Run only individually reviewed, hash-bound answer bytes."""
import json
import os
from pathlib import Path
import sys
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / 'evals/pool'))
import pool
from answer_contract import extract
from pool import grade

APPROVED = {
    'checkout-integrated': '5fb87c6ed0d66719296e759ee18c26006094c81277af29efb249e6f382c2b5b9',
    'file-row-delete-action': 'de56e1088cd3485a1875715a76395ac2703401d3ff4351150607c3762b06cd2c',
    'receipt-font-traits': '76d75d12f4f93fc03ef7f29943b02ba8c6f03931607dac61a33f850dab0f97f6',
}

def main():
    base = ROOT / 'evals/results/prompt-improvements-v1'
    tasks, submissions, holds, expected = [], {}, {}, {}
    review = {v: dict(task=k, decision='run') for k, v in APPROVED.items()}
    path = base / 'reviewed-submissions.json'
    path.write_text(json.dumps(review, indent=2))
    os.environ['RC1_REVIEWED_LOCAL'] = str(path)
    for r in json.loads((HERE / 'items.json').read_bytes())['items']:
        if r['lane'] != 'integration':
            continue
        t, = pool.load(task=Path(r['source']).parent.name)
        tasks.append(t)
        a = json.loads((base/'items'/f"{r['id']}.json").read_bytes())['answer']
        e = extract(a)
        reason = e['status'] if e['code'] is None else grade.reviewed(t, e['code'])
        if reason:
            holds[t.id] = dict(reason=reason, screen=grade.screen(t,e['code']) if e['code'] else [])
        else:
            submissions[t.id] = e['code']
        expected.update({(t.id,k): v for k,_,v in t.variants})
    def variants(t):
        return [(k,b) for k,b,_ in t.variants] + ([('first-answer',submissions[t.id])] if t.id in submissions else [])
    report = grade.execute(tasks, variants, base/'native', lambda r: expected.get((r['task'],r['variant']), 'ungraded'))
    rows = report['rows']
    result = dict(environment={k:report.get(k) for k in ('host','xcode','swift','sdkVersions','simulatorRuntime','deployment')},
                  privateReceipt=report['attempt'],infra=report.get('infrastructureError'),held=holds,
                  checks=[{k:r[k] for k in ('task','variant','submissionSHA256','oracleSHA256','status')} |
                          dict(expected=expected.get((r['task'],r['variant']))) for r in rows])
    # Preserve the earliest scorecard. A rerun has its own private immutable receipt.
    grade.write_once(HERE/'native-results.json', result)

if __name__ == '__main__':
    main()
