"""Offline package, source-wiring, and SDK checks; no models or UI automation."""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from build import BASE, OUT, ROOT, VERSION, package

def main():
    repo = HERE.parents[2]
    results = repo / 'evals/results'
    work = Path(tempfile.mkdtemp(prefix='rc2-check-', dir=results))
    print(work.relative_to(repo), flush=True)
    env = dict(os.environ, TMPDIR=str(work))
    def run(name, args, expected=0, diagnostic=None):
        result = subprocess.run(args, env=env, capture_output=True, timeout=120)
        log = result.stdout + result.stderr
        (work / (name + '.log')).write_bytes(log)
        if result.returncode != expected or (diagnostic and diagnostic not in log.decode()):
            raise RuntimeError(f'{name}: inspect {work}/{name}.log')
    assert (repo / 'VERSION').read_text().strip() == '0.2.2'
    assert hashlib.sha256((repo / 'SKILL.md').read_bytes()).hexdigest() == '2f4ce5ea5a6c8fa7c7cdd08eea620c606eedcc7ae389ac19a493d73078f7c3e3'
    assert OUT.read_bytes() == package()
    with ZipFile(BASE) as old, ZipFile(OUT) as rc:
        assert old.namelist() == rc.namelist()
        changed = {n.removeprefix(ROOT) for n in rc.namelist() if rc.read(n) != old.read(n)}
        assert changed == {'SKILL.md','references/actions.md','references/media.md','references/facts.md'}
        assert f'version: {VERSION}' in rc.read(ROOT+'SKILL.md').decode()
        desc = next(s for s in rc.read(ROOT+'SKILL.md').decode().splitlines() if s.startswith('description: '))
        assert isinstance(json.loads(desc.removeprefix('description: ')), str)
        for card, markers in {
            'actions': ('NSSearchField', 'hiding the representable', 'ordinary single tap', 'touch handler'),
            'media': ('without the requested group', 'matching its cases', 'Equatable'),
        }.items():
            assert 'references/'+card+'.md' in rc.read(ROOT+'SKILL.md').decode()
            note = rc.read(ROOT+'references/'+card+'.md').decode()
            assert all(marker in note for marker in markers)
        rc.extractall(work / 'staging')
    if len(sys.argv) == 2:
        cli = Path(sys.argv[1]).resolve(strict=True)
        project = work / 'project'
        project.mkdir()
        home = work / 'home'
        home.mkdir()
        staging = work / 'staging' / ROOT.rstrip('/')
        result = subprocess.run(['node', str(cli), 'add', str(staging), '--skill', ROOT.rstrip('/'),
                                 '--agent', 'codex', '--yes'], cwd=project, timeout=60,
                                env=dict(env, HOME=str(home), DO_NOT_TRACK='1', DISABLE_TELEMETRY='1',
                                         NODE_DISABLE_COMPILE_CACHE='1'), capture_output=True)
        (work/'install.log').write_bytes(result.stdout + result.stderr)
        assert result.returncode == 0
        def contents(folder):
            return {p.relative_to(folder): p.read_bytes() for p in folder.rglob('*') if p.is_file()}
        assert contents(project/'.agents/skills'/ROOT.rstrip('/')) == contents(staging)
        print('Project-local CLI install matches all archive files.')
    # These two checks audit the wiring of this fixture only; no assertion about
    # a generated AX tree or delivery of a physical gesture follows from them.
    source = (HERE / 'Contracts.swift').read_text()
    def wiring(s):
        owner = s.split('struct Sidebar: View {')[1].split('#endif')[0]
        surface = s.split('struct ChapterSurface: View {')[1].split('// An inspector')[0]
        return ('CatalogSearch()' in owner and not re.search(
                    r'CatalogSearch\(\)\s*\.(accessibilityHidden\(true\)|accessibilityRepresentation)', owner),
                ('.onTapGesture(count: 1, perform: controls.tap)' in surface or
                 '.onTapGesture { controls.tap() }' in surface)
                and '.accessibilityAdjustableAction(controls.adjust)' in surface)
    def variant(old, new):
        assert source.count(old) == 1, old
        return source.replace(old,new)
    def swift(name,s,sdk,target,executable=False,expected=0,diagnostic=None):
        path=work/(name+'.swift'); path.write_text(s)
        args=['xcrun','--sdk',sdk,'swiftc','-parse-as-library','-module-cache-path',str(work/'cache'),'-target',target]
        if executable: args += ['-o',str(work/name)]
        else: args += ['-typecheck']
        run(name+'-compiler',args+[str(path)],expected,diagnostic)
    mac='arm64-apple-macos26.0'
    assert wiring(source)==(True,True)
    swift('positive',source,'macosx',mac,True)
    run('unit',[str(work/'positive')])
    swift('ios',source,'iphonesimulator','arm64-apple-ios26.0-simulator')
    alternate = variant('some View { CatalogSearch() }',
                        'some View { HStack { Image(systemName: "magnifyingglass").accessibilityHidden(true); CatalogSearch() } }')
    alternate = alternate.replace('.onTapGesture(count: 1, perform: controls.tap)', '.onTapGesture { controls.tap() }')
    swift('alternative',alternate,'macosx',mac,True)
    run('alternative-unit',[str(work/'alternative')])
    assert wiring(alternate)==(True,True)
    hide=variant('some View { CatalogSearch() }','some View { CatalogSearch().accessibilityHidden(true) }')
    assist=variant('.onTapGesture(count: 1, perform: controls.tap)', '.accessibilityAction { controls.tap() }')
    for name,mutant,want in [('hidden-editor',hide,(False,True)),('assist-only',assist,(True,False))]:
        swift(name,mutant,'macosx',mac)
        assert wiring(mutant)==want
    swift('invalid-equality',variant('enum Tracks {','enum Tracks: Equatable {'),'macosx',mac,expected=1,
          diagnostic="type 'Tracks' does not conform to protocol 'Equatable'")
    swap=variant('guard let item else { return .unavailable }','guard let item else { return .absent }')
    swift('wrong-result',swap,'macosx',mac,True)
    run('wrong-result-unit',[str(work/'wrong-result')],42,'missing item')
    print('Package, routing links, host units, iOS compilation and four negative controls passed.')
    return work

if __name__ == '__main__':
    main()
