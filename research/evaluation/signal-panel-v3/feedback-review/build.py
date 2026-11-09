"""Build a reviewed research variant and audit the private return without publishing answers."""
from collections import Counter
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import sys
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

D = Path(__file__).resolve().parent
ROOT = D.parents[3]
P = 'swift-accessibility-agent/'
digest = lambda b: sha256(b).hexdigest()


def candidate():
    parent = (D.parent / 'candidate.zip').read_bytes()
    assert digest(parent) == '3e291a1f8ce9fc2fdc1f57abbce318c23bfb48feb6d4270e9c49037fc6ec2df9'
    with ZipFile(BytesIO(parent)) as z:
        files = {n: z.read(n) for n in z.namelist()}
    key = P + 'SKILL.md'
    files[key] = files[key].replace(b'signal-v3', b'signal-v3-review.1').replace(
        b'action callbacks in SwiftUI wrappers of native controls',
        b'native-control wrappers, first-responder fallback, media picker bindings and asynchronous form validation')
    for card, note in {
        'return': 'For an AppKit responder request, membership in the originating window is a precondition, not success. If makeFirstResponder returns false and the task calls for a fallback, try the eligible fallback in that window while this presentation still owns restoration. Test refusal by an attached target, not just detachment.',
        'validation': 'Exercise the edit path used by the native field, not only a helper that cancels pending work. Wire editing events to invalidation or compare the live input with the submitted snapshot at completion; a stale result must neither publish feedback nor strand its own pending state.',
        'actions': 'If the native editor is the intended accessible editing stop, remove redundant wrapper semantics without hiding the represented subtree. For a shortcut mirroring a button, check current permission even when identity is unchanged. In tests drive the registered callback: for closure-backed actions, UIKit actionHandler?(action) and AppKit handler?() have different signatures. Check each ordinary control separately; direct dispatch alone does not establish attachment.',
        'media': 'Distinguish a missing player item from a loaded group with no eligible options when reporting inspection results. For described audio, inspect .describesVideoForAccessibility; identify fixture tracks independently of the characteristic being tested.'
    }.items():
        files[P + 'references/' + card + '.md'] += ('\n' + note + '\n').encode()
    out = BytesIO()
    with ZipFile(out, 'w') as z:
        for n, content in sorted(files.items()):
            z.writestr(ZipInfo(n, (2026, 1, 1, 0, 0, 0)), content, compress_type=ZIP_DEFLATED)
    return out.getvalue()


def audit():
    raw = (ROOT / 'evals/results/signal-v2-review-20261108/signal-panel-v2-return.zip').read_bytes()
    assert digest(raw) == '9929eb1bddb1eb850bdc6ff026bb0469852e8ecab19ef7100689595788990368'
    with ZipFile(BytesIO(raw)) as z:
        read = lambda n: json.loads(z.read(n))
        hashes = read('SHA256.json')
        assert set(hashes) == set(z.namelist()) - {'SHA256.json'}
        assert all(digest(z.read(k)) == v for k, v in hashes.items())
        grades = {(g['id'], g['arm']): g for g in read('grades.json')}
        receipt = json.loads((D.parents[1]/'signal-panel-v2/receipt.json').read_bytes())
        assert digest(z.read('held.zip')) == receipt['packetSHA256']
        reservations = [e['cell'] for line in z.read('attempts.jsonl').splitlines()
                        if (e := json.loads(line))['event'] == 'reserve']
        assert len(set(reservations)) == len(reservations) == 112
        freeze = read('grade-freeze.json')
        for (i, arm), g in grades.items():
            mask = g['mask']
            name = f'masked-grades/{mask}.json'
            assert digest(z.read(name)) == freeze[name]
            assert read(name) == {k:v for k,v in g.items() if k not in ('id','arm')}
            assert read('private-map/'+mask[:-1])[mask] == i+'.'+arm
            answer = read(f'masked/{mask}.json')['answer'].lower()
            assert not any(marker in answer for marker in ('routing:', 'signal-v2', 'swift accessibility agent'))
        traces = read('traces.json')
        rows = []
        for case in read('transitions.json'):
            i = case['id']
            u, s = (grades.get((i, arm)) for arm in ('unaided', 'skill'))
            change = {('pass','pass'):'preserved', ('fail','pass'):'rescue',
                      ('pass','fail'):'regression', ('fail','fail'):'persistent'}
            whole = change[u['whole'], s['whole']] if u and s else 'inconclusive'
            assert whole == case['transitions']['whole']
            paths = sorted({Path(r['path']).name for r in traces.get(i+'.skill', {}).get('reads', [])
                            if r['status'] == 3 and r['returned_excerpt']})
            rows.append([i,case['platform'],case['framework'],case['family'],whole,
                         s['primary'] if s else '-',s['whole'] if s else '-',
                         ', '.join(paths) or ('none' if s else 'unavailable')])
        assert len(grades) == 107 and len(set(r[0] for r in rows)) == len(rows) == 56
        print(len(hashes), 'verified members;', dict(Counter(r[4] for r in rows)))
        for body in (True, False):
            group = [r for r in rows if r[6]!='-' and ('SKILL.md' in r[7]) == body]
            print('body read:', body, 'n:', len(group), 'whole:', sum(r[6]=='pass' for r in group),
                  'primary:', sum(r[5]=='pass' for r in group), 'rescues:',sum(r[4]=='rescue' for r in group))
        return ('| Case | Platform | Framework | Family | Paired whole | Installed primary | Installed whole | Corroborated installed reads |\n'
                '|---|---|---|---|---|---|---|---|\n'+''.join('| '+' | '.join(r)+' |\n' for r in rows)).encode()


for name, data in [('candidate.zip', candidate()), ('case-audit.md', audit())]:
    if '--check' in sys.argv:
        assert (D/name).read_bytes() == data, name
    else:
        (D/name).write_bytes(data)
