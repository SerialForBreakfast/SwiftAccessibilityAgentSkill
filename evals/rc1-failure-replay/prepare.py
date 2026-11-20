"""Prepare subject-only inputs and the controller index from archived Haiku runs."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ARCHIVE = ROOT.parent / 'BigDog-Coordinator/.local/swift-accessibility-eval'
NATIVE = ROOT / 'evals/results/native-activation-lift-20261106-r5'


def read(path):
    return json.loads(path.read_bytes())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    packet = read(ROOT / 'evals/rc1-comparison/packet.json')
    prefix = packet['explicitPrefix']
    model = packet['model']
    runtime = next(path for path in packet['pins'] if path.endswith('.zip'))
    assert digest((ROOT / runtime).read_bytes()) == packet['pins'][runtime]
    tasks = {}

    def register(case, prompt, expected, run, job, answer, verdict, criterion):
        assert digest(prompt.encode()) == expected
        task = tasks.setdefault(case, dict(original=prompt, rubric=criterion, controls=[]))
        assert task['original'] == prompt and task['rubric'] == criterion
        task['controls'].append(dict(run=run, job=job, answerSHA256=digest(answer.encode()),
                                     grade=verdict))

    for run, condition in [('claude-haiku-baseline-20261105-r1', 'C0'),
                           ('compact-a-development144-20261105-r1', 'N')]:
        directory = ARCHIVE / run
        grades = read(directory / 'review.json')
        criteria = {}
        for name in ['gold-acceptance', 'exploratory-acceptance', 'evidence-questions']:
            source = read(directory / (name + '.json'))
            for item in source if isinstance(source, list) else source['cases']:
                criteria[item['id']] = item
        for job in read(directory / 'jobs.json'):
            if job['condition'] != condition or job.get('model', model) != model:
                continue
            key = job['id']
            raw = (directory / 'run' / (key + '-stdout.json')).read_bytes()
            response = json.loads(raw)
            assert set(response['modelUsage']) == {model} and not response['is_error']
            answer = response['result']
            grade = grades[key]
            if 'output_sha256' in grade:
                assert digest(raw) == grade['output_sha256']
            else:
                assert digest(answer.encode()) == grade['answer_sha256']
            register(job['case'], job['prompt'], job.get('sha256') or job['prompt_sha256'],
                     run, key, answer, grade['core'], criteria[job['case']])

    grades = {x['id']: x for x in read(NATIVE / 'independent-quality-grades.json')['records']}
    mapping = {x['job']: x for x in read(NATIVE / 'quality-mapping-private.json')}
    for job in read(NATIVE / 'jobs.json'):
        if job['condition'] != 'generic':
            continue
        key = job['id']
        row = mapping[key]
        grade = grades[row['id']]
        if grade['core'] != 'material-gap':
            continue
        response = read(NATIVE / 'run' / (key + '-parsed.json'))
        assert set(response['result']['modelUsage']) == {model}
        assert not response['tool_calls'] and not response['skill_results']
        assert digest(response['answer'].encode()) == row['original_answer_sha256']
        register(job['case'], job['prompt'], job['prompt_sha256'], NATIVE.name, key,
                 response['answer'], grade['core'],
                 next(c for c in read(NATIVE / 'quality-packet.json')['contracts']['question_contract_review']
                      if c['id'] == job['case']))

    inputs = HERE / 'inputs'
    inputs.mkdir(exist_ok=True)
    cases = {}
    for case, task in sorted(tasks.items()):
        if not any(x['grade'] == 'material-gap' for x in task['controls']):
            continue
        original = task.pop('original').encode()
        subject = prefix.encode() + original
        path = inputs / (case + '.txt')
        path.write_bytes(subject)
        assert path.read_bytes()[len(prefix.encode()):] == original
        cases[case] = dict(input=str(path.relative_to(HERE)), originalSHA256=digest(original),
                           subjectSHA256=digest(subject), **task)
    assert set(cases) == {'EV02', 'EV06', 'GP26-02', 'GP26-03', 'GP26-04', 'GP26-11',
                          'IOS-MEDIA-OWNERSHIP-R1'}
    manifest = dict(model=model, effort='low', runtime=runtime, runtimeSHA256=packet['pins'][runtime],
                    explicitPrefix=prefix, cases=cases)
    (HERE / 'controller.json').write_text(json.dumps(manifest, indent=2) + '\n')


if __name__ == '__main__':
    main()
