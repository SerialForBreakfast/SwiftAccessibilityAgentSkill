"""Build review and subject copies from hash-verified repository fixtures."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
SOURCE = REPO / 'code-examples'
SUBJECT = ROOT / 'subjects'
SUBJECT.mkdir(exist_ok=True)
key = []
catalog = []
pages = []
hash_text = lambda s: sha256(s.encode()).hexdigest()

def methods(text):
    # Fixtures use conventional XCTest method declarations with balanced bodies.
    spans = {}
    for match in re.finditer(r'(?m)^[ \t]*(?:@MainActor\s+)?func (test\w+)\s*\(', text):
        start = text.index('{', match.end())
        depth = 1
        i = start + 1
        while depth:
            depth += (text[i] == '{') - (text[i] == '}')
            i += 1
        assert match[1] not in spans
        spans[match[1]] = (match.start(), i)
    return spans

def fenced(text):
    text = re.sub(r'(?im)^\s*//[^\n]*(?:mutant|deliberat)[^\n]*$', '', text)
    text = re.sub(r'/\*[^*]*deliberate[^*]*\*/', '', text, flags=re.I)
    return '\n```swift\n' + text.strip() + '\n```\n'

def relative(path):
    return str(path.relative_to(REPO))

def verified(pkg, manifest, path):
    raw = (pkg/path).read_bytes()
    expected = next(f['sha256'] for f in manifest['files'] if f['path'] == path)
    assert sha256(raw).hexdigest() == expected, path
    return raw.decode()

repairs = [l.split('|') for l in (ROOT/'cases.tsv').read_text().splitlines()]
proofs = [l.split('|') for l in (ROOT/'proof-cases.tsv').read_text().splitlines()]
assert (len(repairs), len(proofs)) == (80, 20)
# Interleave working and faulty implementations. Numbers do not encode condition.
items = sorted(repairs + proofs, key=lambda x: hash_text(x[2]))
for number, item in enumerate(items, 1):
    name, check, question, *weak = item
    pkg, = SOURCE.glob('*/' + name)
    manifest = json.loads((pkg/'manifest.json').read_text())
    oracle = next(c for c in manifest['checks'] if c['id'] == check)
    target = oracle['replacement']['target']
    bad = oracle['replacement']['source']
    source = verified(pkg, manifest, target if weak else bad)
    suite, method = oracle['failureIds'][0].split('/')
    testpath, = [p for p in pkg.glob('Tests/*.swift') if method in methods(p.read_text())]
    tests = verified(pkg, manifest, str(testpath.relative_to(pkg)))
    spans = methods(tests)
    a,b = spans[method]
    expected_test = tests[a:b].strip()
    code = fenced(source)
    if weak:
        # Preserve real setup, helpers and test doubles. Omit all original test methods.
        for old,(a,b) in sorted(spans.items(), key=lambda x:-x[1][0]):
            replacement = '' if old != method else '    @MainActor func testCurrentBehavior() throws {\n        '+weak[0]+'\n    }'
            tests = tests[:a]+replacement+tests[b:]
        tests = re.sub(r'\n(?:[ \t]*\n){2,}', '\n\n', tests).strip()
        code += '\nCurrent XCTest file\n' + fenced(tests)
    platform = manifest['platform']
    identifier = f'Q{number:03d}'
    framework = 'SwiftUI' if pkg.parent.name=='swiftui' else 'AppKit' if platform=='macOS' else 'UIKit'
    instruction = ('Return the revised XCTest and explain which observation would turn red if the behavior broke. Change production code only if you can demonstrate a defect.'
                   if weak else 'Return the corrected Swift and a focused XCTest. Exercise the relevant entry point, show the expected outcome and check an ordinary behavior the change must preserve.')
    prompt = f'{platform}, {framework}. {question}\n\n{instruction}\n\nCurrent implementation\n'+code
    # Include referenced sibling production files when the target depends on their types.
    provided = source + (tests if weak else '')
    pending = [f['path'] for f in manifest['files'] if f['path'].startswith('Sources/') and f['path'] != target]
    while pending:
        progress=False
        for path in pending.copy():
            sibling = verified(pkg,manifest,path)
            names = re.findall(r'\b(?:class|struct|enum|protocol|typealias|extension)\s+(\w+)', sibling)
            if any(re.search(r'\b'+re.escape(n)+r'\b',provided) for n in names):
                prompt += '\nSupporting source\n'+fenced(sibling)
                provided += sibling
                pending.remove(path)
                progress=True
        if not progress:break
    (SUBJECT/f'{identifier}.md').write_text(prompt)
    digest=hash_text(prompt)
    pages.append(f'<a id="{identifier.lower()}"></a>\n\n## {identifier}\n\n'+prompt)
    catalog.append(f'| [{identifier}](subjects/{identifier}.md) | {platform} · {framework} | {question} |')
    key.append(dict(id=identifier,kind='test repair' if weak else 'implementation repair',family=name,platform=platform,
                    promptSHA256=digest,question=question,manifest=relative(pkg/'manifest.json'),check=check,
                    workingSource=relative(pkg/target),defectiveSource=relative(pkg/bad),oracleSuite=relative(testpath),
                    expectedFailures=oracle['failureIds'],exampleCheck=expected_test,
                    sourceClaims=[c for c in manifest['claims'] if c['id'] in oracle['claimIds']],limitations=manifest['limitations']))
assert len(key)==len({x['promptSHA256'] for x in key})==100
(ROOT/'controller.json').write_text(json.dumps(key,indent=2,ensure_ascii=False)+'\n')
(ROOT/'ALL-100.md').write_text('# All 100 Swift accessibility prompts\n\nEach numbered section contains one complete subject prompt. Send one section per fresh session.\n\n'+'\n'.join(pages))
(ROOT/'INDEX.md').write_text('# Browse the 100 questions\n\n| Prompt and code | Platform | Developer question |\n|---|---|---|\n'+'\n'.join(catalog)+'\n')
(ROOT/'ANSWER-KEY.md').write_text('# Controller answer key\n\nKeep this file outside subject sessions. Each XCTest excerpt belongs to the linked suite, which contains its setup and helpers. Accept equivalent observable behavior.\n\n'+'\n'.join(
    f"## {x['id']} · {x['kind']}\n\n{x['question']}\n\n[Working implementation](../../{x['workingSource']}) · [Defective implementation](../../{x['defectiveSource']}) · [Full test suite](../../{x['oracleSuite']}) · [Source contract](../../{x['manifest']})\n\nRegistered failing assertion(s): {', '.join(x['expectedFailures'])}.\n"+fenced(x['exampleCheck']) for x in key))
print(Counter(x['platform'] for x in key),Counter(x['kind'] for x in key))
