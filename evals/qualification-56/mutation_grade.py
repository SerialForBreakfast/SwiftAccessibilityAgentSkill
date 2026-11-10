"""Offline mutation grader: does a model's submitted XCTest discriminate the fix from a defect?

For every answered cell on a question with a qualified native control (native_controls.py,
more_controls.py, final_controls.py), the submitted test fences (the fences grade_run.select()
leaves out of the subject) run unchanged against the control's reference, alternative and
defect-mutant sources through research/evaluation/signal-panel-v4/replay/native.py.

  python3 -B evals/qualification-56/mutation_grade.py stage RETURN.zip [--trials 1] [--name NAME]
  python3 -B evals/qualification-56/mutation_grade.py run NAME        # ref, then mutant, then alternative
  python3 -B evals/qualification-56/mutation_grade.py verdicts NAME   # NAME/verdicts.json + coverage
  python3 -B evals/qualification-56/mutation_grade.py calibrate NAME  # agreement with the 1507 grades
  python3 -B evals/qualification-56/mutation_grade.py all RETURN.zip [--trials 1] [--name NAME]

Verdicts (per answer):
  discriminating  passes on reference and alternative, fails on the mutant
  vacuous         passes on the mutant (reference also passes)
  wrong           fails on the reference
  overfit         passes on reference, fails on mutant, but rejects the acceptable alternative
                  (assertion failure, or does not compile against it: coupled to one implementation)
  not-runnable    no submitted test, test/subject compile failure on the reference, or a harness
                  outcome (timeout, offline build only, no tests discovered). Never a model failure.
                  `control-api-mismatch:` marks a compile failure on a question whose starter declares
                  types the control reference lacks (the control exercises an equivalent example).

Staging is mechanical and arm-blind, never a repair: a test fence without an XCTest import gets the
grade_run.py header; a bare `func test...` fragment gets prepare.py's wrapper class; a missing
`@testable import <module>` is added; a declaration in a test fence that redefines a type the
control source declares is removed (recorded as `stripped`). The variant source replaces the
model's own implementation. Runs are sequential, offline, no network, no model calls.
Everything is written under evals/results/mutation-grade-calibration/NAME/ (private).
"""
from common import *
from grade_run import select, TEST, TYPE
from native_controls import suites
from more_controls import specs as more_specs
from final_controls import specs as final_specs
import os, re, subprocess, tempfile, zipfile, hashlib
from collections import Counter, defaultdict

OUT = ROOT / 'evals/results/mutation-grade-calibration'
NATIVE = V4 / 'replay/native.py'
VARIANTS = ('ref', 'alt', 'mut')
GRADES = ROOT / 'evals/results/1507-grade/final-review'
NOT_RUN = 'not-run-mutation-grade'


def controls():
    out = {}
    for s in suites() + more_specs() + final_specs():
        for i in s['ids']:
            assert i not in out, i
            out[i] = s
    return out


def decls(src):
    return set(TYPE.findall(src))


def prepare_tests(answer, question, platform, ref):
    """Return (mode, module, [test sources], stripped names) or (mode, None, [], []) if no test."""
    mode, parts = select(answer, question), blocks(answer)
    tests = [p for p in parts if TEST.search(p)]
    if not tests:
        return mode, None, [], []
    module = next((m[1] for s in tests for m in re.finditer(r'@testable import (\w+)', s)), 'YourAppModule')
    fw = 'AppKit' if platform == 'macOS' else 'UIKit'
    header = f'import XCTest\nimport SwiftUI\nimport AVFoundation\nimport {fw}\n@testable import {module}\n'
    out, stripped, subject_types = [], [], decls(ref)
    for s in tests:
        for name in sorted(decls(s) & subject_types):
            pat = r'\b(?:final\s+)?(?:class|struct|enum|actor|protocol)\s+' + name + r'\b'
            while re.search(r'(?m)^.*?' + pat, s):
                s = s.replace(declaration(s, pat), '', 1)
                stripped.append(name)
        if 'XCTestCase' not in s and '@Test' not in s and re.search(r'\bfunc test', s):
            s = '@MainActor final class Submitted: XCTestCase {\n' + s + '\n}\n'
        if 'import XCTest' not in s and 'import Testing' not in s:
            s = header + s
        elif not re.search(r'import\s+' + module + r'\b', s):
            s = f'@testable import {module}\n' + s
        out.append(s)
    return mode, module, out, stripped


def stage(path, trials, name):
    raw = Path(path).read_bytes()
    sha = H(raw)
    ctrl = controls()
    OUT.mkdir(parents=True, exist_ok=True)
    batch = OUT / name if name else Path(tempfile.mkdtemp(prefix='run-', dir=OUT))
    if name:
        batch.mkdir()
    rows = {r['id']: r for r in PANEL}
    answers = []
    with zipfile.ZipFile(path) as ret, questions() as qs:
        for c in json.loads(ret.read('return.json'))['cells']:
            if c.get('trial', 1) not in trials:
                continue
            key = f"{c['id']}.{c['arm']}.t{c.get('trial', 1)}"
            row, k = rows[c['id']], c['id'][2:6]
            rec = dict(key=key, id=c['id'], arm=c['arm'], trial=c.get('trial', 1), platform=row['platform'],
                       state=c['state'], control=None)
            if k not in ctrl:
                rec['verdict'] = 'no-control'
                answers.append(rec); continue
            spec = ctrl[k]
            assert spec['platform'] == row['platform'], (k, spec['platform'], row['platform'])
            rec['control'] = dict(origin=spec['origin'], ids=spec['ids'], src={v: H(s.encode()) for v, s in zip(VARIANTS, spec['src'])})
            if c['state'] != 'answered':
                rec['verdict'], rec['reason'] = 'not-runnable', 'no-answer:' + c['state']
                answers.append(rec); continue
            q = qs.read('subjects/' + c['id'] + '.txt'); assert H(q) == c['questionSHA256'] == row['questionSHA256']
            a = ret.read(c['answer']['path']); assert H(a) == c['answer']['sha256']
            mode, module, tests, stripped = prepare_tests(a.decode(), q.decode(), row['platform'], spec['src'][0])
            rec.update(answerSHA256=H(a), selection=mode, module=module, stripped=stripped, tests=len(tests))
            if not tests:
                rec['verdict'], rec['reason'] = 'not-runnable', 'no-submitted-test'
            else:
                d = batch / 'tests' / key; d.mkdir(parents=True)
                for n, s in enumerate(tests):
                    (d / f'Proof{n}.swift').write_text(s)
            answers.append(rec)
    manifest = dict(returnSHA256=sha, returnPath=os.path.relpath(path, ROOT), trials=sorted(trials), answers=answers)
    (batch / 'manifest.json').write_text(json.dumps(manifest, indent=1) + '\n')
    staged = sum('verdict' not in a for a in answers)
    print(batch.name, f'{len(answers)} cells, {staged} with a submitted test on a controlled question')
    return batch.name


def cell(batch, rec, variant):
    """Stage one native.py cell (proof lane only) for this answer and control variant."""
    d = batch / f"{rec['key']}.{variant}"
    if d.exists():
        return d
    d.mkdir()
    spec = controls()[rec['id'][2:6]]
    (d / 'Subject.swift').write_text(spec['src'][VARIANTS.index(variant)])
    for f in sorted((batch / 'tests' / rec['key']).glob('Proof*.swift')):
        (d / f.name).write_bytes(f.read_bytes())
    meta = dict(id=rec['id'], arm=rec['arm'], trial=rec['trial'], platform=rec['platform'], module=rec['module'],
                selection=rec['selection'], variant=variant, control=spec['origin'],
                inputs={p.name: H(p.read_bytes()) for p in d.iterdir()})
    (d / 'input.json').write_text(json.dumps(meta, indent=2))
    # The independent contract lane is not part of this grade: mark it so native.py runs only the proof lane.
    with (d / 'contract.json').open('x') as f:
        json.dump(dict(lane='contract', environment=rec['platform'], status=NOT_RUN), f, indent=2)
    return d


def status(batch, rec, variant):
    p = batch / f"{rec['key']}.{variant}" / 'proof.json'
    return json.loads(p.read_text())['status'] if p.exists() else None


def native(batch):
    arg = os.path.relpath(batch, ROOT / 'evals/results/persistent-replay')
    rc = subprocess.run([sys.executable, '-B', str(NATIVE), arg], cwd=ROOT).returncode
    if rc:
        raise SystemExit(f'native.py exited {rc}')


def run(name):
    batch = OUT / name
    answers = json.loads((batch / 'manifest.json').read_text())['answers']
    todo = [a for a in answers if 'verdict' not in a]
    for variant, gate in [('ref', None), ('mut', 'ref'), ('alt', 'mut')]:
        want = {'ref': None, 'mut': 'unit-pass', 'alt': 'unit-failure'}[variant]
        chosen = [a for a in todo if gate is None or status(batch, a, gate) == want]
        for a in chosen:
            cell(batch, a, variant)
        print(f'phase {variant}: {len(chosen)} cells', flush=True)
        if chosen:
            native(batch)


COMPILE = {'test-compile-failure', 'subject-compile-failure'}


def api_mismatch():
    """Questions whose starter (or scaffold) declares types the control's reference does not.
    A submitted test written against the question's API cannot compile against such a control:
    that is a control coverage gap, not a model failure."""
    ctrl, out = controls(), {}
    with questions() as qs:
        for r in PANEL:
            k = r['id'][2:6]
            if k not in ctrl:
                continue
            st = blocks(qs.read('subjects/' + r['id'] + '.txt').decode())
            sc = D / 'scaffolds' / (k + '.swift')
            src = st[0] if st else sc.read_text() if sc.exists() else ''
            miss = sorted(decls(src) - decls(ctrl[k]['src'][0]))
            if miss:
                out[r['id']] = miss
    return out


def verdict(batch, rec, mismatch={}):
    if 'verdict' in rec:
        return rec['verdict'], rec.get('reason')
    r, m, a = (status(batch, rec, v) for v in ('ref', 'mut', 'alt'))
    if r is None:
        return 'pending', 'reference not run'
    if r in COMPILE:
        return 'not-runnable', ('control-api-mismatch:' if rec['id'] in mismatch else 'reference:') + r
    if r == 'unit-failure':
        return 'wrong', 'fails on reference'
    if r != 'unit-pass':
        return 'not-runnable', 'harness:' + r
    if m is None:
        return 'pending', 'mutant not run'
    if m == 'unit-pass':
        return 'vacuous', 'passes on mutant'
    if m != 'unit-failure':
        return 'not-runnable', 'mutant:' + m
    if a is None:
        return 'pending', 'alternative not run'
    if a == 'unit-pass':
        return 'discriminating', 'ref pass, alt pass, mutant fail'
    if a == 'unit-failure':
        return 'overfit', 'alternative: assertion failure'
    if a in COMPILE:
        return 'overfit', 'alternative:' + a
    return 'not-runnable', 'alternative:' + a


def verdicts(name):
    batch = OUT / name
    man = json.loads((batch / 'manifest.json').read_text())
    rows, mismatch = [], api_mismatch()
    for rec in man['answers']:
        v, why = verdict(batch, rec, mismatch)
        diag = []
        for var in VARIANTS:
            p = batch / f"{rec['key']}.{var}" / 'proof.json'
            if p.exists():
                diag += [f'{var}: {x}' for x in json.loads(p.read_text()).get('diagnostics', [])[:2]]
        rows.append(dict(key=rec['key'], id=rec['id'], arm=rec['arm'], trial=rec['trial'], platform=rec['platform'],
                         control=(rec['control'] or {}).get('origin'), selection=rec.get('selection'),
                         controlApiMismatch=mismatch.get(rec['id'], []),
                         stripped=rec.get('stripped', []), verdict=v, reason=why,
                         statuses={var: status(batch, rec, var) for var in VARIANTS}, diagnostics=diag))
    (batch / 'verdicts.json').write_text(json.dumps(rows, indent=1) + '\n')
    cov = coverage(rows)
    (batch / 'coverage.json').write_text(json.dumps(cov, indent=1) + '\n')
    for arm, c in cov.items():
        print(arm, c)
    return rows


def coverage(rows):
    out = {}
    for arm in sorted({r['arm'] for r in rows}):
        rs = [r for r in rows if r['arm'] == arm and r['verdict'] != 'no-control']
        v = Counter(r['verdict'] for r in rs)
        out[arm] = dict(controlledAnswers=len(rs), runnable=sum(v[k] for k in ('discriminating', 'vacuous', 'wrong', 'overfit')),
                        verdicts=dict(v), notRunnableReasons=dict(Counter(r['reason'].split(':')[0] + ':' + r['reason'].split(':')[-1] if ':' in r['reason'] else r['reason'] for r in rs if r['verdict'] == 'not-runnable')))
    return out


VMISS = 'Material miss in the requested verification'


def source_class(g):
    w = g['source']['whole']
    if w['verdict'] == 'pass':
        return 'whole-pass'
    if w['verdict'] == 'fail':
        return 'verification-miss' if w['reason'].startswith(VMISS) else 'whole-fail-other'
    return 'whole-' + w['verdict']


def calibrate(name):
    batch = OUT / name
    rows = verdicts(name)
    ledger = {(g['id'], g['trial'], g['arm']): g for g in json.loads((GRADES / 'controller-ledger.json').read_text())}
    board = {q['id']: q for q in json.loads((GRADES / 'matched-board.json').read_text())}
    notes_path = OUT / 'explanations.json'
    notes = json.loads(notes_path.read_text()) if notes_path.exists() else {}
    runnable = ('discriminating', 'vacuous', 'wrong', 'overfit')
    table, matrix, dis = [], Counter(), []
    for r in rows:
        if r['verdict'] == 'no-control':
            continue
        g = ledger.get((r['id'], r['trial'], r['arm']))
        sc = source_class(g) if g else 'ungraded'
        ver = g['source']['verification']['verdict'] if g else None
        r2 = dict(r, source=sc, sourceVerification=ver, sourceWholeReason=g['source']['whole']['reason'] if g else None,
                  boardMatched=str(r['trial']) in board.get(r['id'], {}).get('matched', {}))
        table.append(r2)
        if r['verdict'] in runnable:
            matrix[(r['verdict'], sc)] += 1
            kind = None
            if r['verdict'] == 'discriminating' and sc == 'verification-miss':
                kind = 'discriminating but 1507 found a verification miss'
            elif r['verdict'] == 'vacuous' and (sc == 'whole-pass' or ver == 'pass'):
                kind = 'vacuous but 1507 passed the answer'
            elif r['verdict'] == 'wrong' and (sc == 'whole-pass' or ver == 'pass'):
                kind = 'wrong but 1507 passed the answer'
            elif r['verdict'] == 'overfit' and sc == 'whole-pass':
                kind = 'overfit but 1507 passed the answer'
            if kind:
                dis.append(dict(key=r['key'], kind=kind, verdict=r['verdict'], reason=r['reason'], source=sc,
                                sourceVerification=ver, sourceWholeReason=r2['sourceWholeReason'],
                                explanation=notes.get(r['key'], 'not yet reviewed')))
    disc = [t for t in table if t['verdict'] == 'discriminating']
    vac = [t for t in table if t['verdict'] == 'vacuous']
    summary = dict(
        batch=name,
        coverage=coverage(rows),
        matrix={f'{a} | {b}': n for (a, b), n in sorted(matrix.items())},
        discriminatingVsSourcePass=dict(discriminating=len(disc), ofWhichWholePass=sum(t['source'] == 'whole-pass' for t in disc),
                                        ofWhichVerificationMiss=sum(t['source'] == 'verification-miss' for t in disc)),
        vacuousVsVerificationMiss=dict(vacuous=len(vac), ofWhichVerificationMiss=sum(t['source'] == 'verification-miss' for t in vac),
                                       ofWhichWholePass=sum(t['source'] == 'whole-pass' for t in vac)),
        disagreements=dis)
    (OUT / f'{name}-cells.json').write_text(json.dumps(table, indent=1) + '\n')
    (OUT / f'{name}-agreement.json').write_text(json.dumps(summary, indent=1) + '\n')
    lines = [f'# Mutation-grade calibration: {name}', '',
             'Rows: mutation verdict on runnable answers. Columns: 1507 whole grade (controller-ledger.json); '
             '`verification-miss` = whole fail whose reason begins "Material miss in the requested verification".', '']
    cols = sorted({b for (_, b) in matrix})
    lines += ['| verdict | ' + ' | '.join(cols) + ' | total |', '|---|' + '---:|' * (len(cols) + 1)]
    for v in runnable:
        lines.append(f'| {v} | ' + ' | '.join(str(matrix[(v, c)]) for c in cols) + f' | {sum(matrix[(v, c)] for c in cols)} |')
    lines += ['', '## Coverage per arm', '', '| arm | controlled answers | runnable | discriminating | vacuous | wrong | overfit | not-runnable |', '|---|---:|---:|---:|---:|---:|---:|---:|']
    for arm, c in summary['coverage'].items():
        v = c['verdicts']
        lines.append(f"| {arm} | {c['controlledAnswers']} | {c['runnable']} | " + ' | '.join(str(v.get(k, 0)) for k in ('discriminating', 'vacuous', 'wrong', 'overfit', 'not-runnable')) + ' |')
    lines += ['', '## Disagreements', '']
    lines += [f"- `{d['key']}` — {d['kind']} ({d['reason']}). 1507: {d['source']}, verification component {d['sourceVerification']}. Explanation: {d['explanation']}" for d in dis] or ['None.']
    (OUT / f'{name}-agreement.md').write_text('\n'.join(lines) + '\n')
    print('\n'.join(lines))


if __name__ == '__main__':
    cmd, args = sys.argv[1], sys.argv[2:]
    opt = lambda k, d=None: args[args.index(k) + 1] if k in args else d
    trials = {int(t) for t in opt('--trials', '1').split(',')}
    if cmd in ('stage', 'all'):
        n = stage(args[0], trials, opt('--name'))
        if cmd == 'all':
            run(n); calibrate(n)
    elif cmd == 'run':
        run(args[0])
    elif cmd == 'verdicts':
        verdicts(args[0])
    elif cmd == 'calibrate':
        calibrate(args[0])
    else:
        raise SystemExit(__doc__)
