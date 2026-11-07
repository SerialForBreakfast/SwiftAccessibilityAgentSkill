import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {nativePlan} from './platform-core.mjs';
import {retrieve} from './lifecycle-retrieval.mjs';
import {retrieve as previous} from './navigation-retrieval.mjs';
for(const folder of ['macos-lifecycle-v1','tvos-lifecycle-v1']) {
  test(`${folder}: pinned native inputs and separate prompts resolve`,()=>{
    const root=fileURLToPath(new URL(`../platforms/${folder}/`,import.meta.url));
    const m=JSON.parse(fs.readFileSync(root+'manifest.json'));
    for(const c of m.checks)assert.equal(nativePlan(m,root,c.id).check.id,c.id);
    const names=fs.readdirSync(root+'evaluation');
    const rubrics=names.filter(n=>n.endsWith('.rubric.md')).map(n=>fs.readFileSync(root+'evaluation/'+n,'utf8')).join('\n');
    for(const id of m.checks.find(c=>c.id==='positive').testIds)assert.ok(rubrics.includes(id),id);
    for(const name of names.filter(n=>n.endsWith('.prompt.md')))assert.doesNotMatch(fs.readFileSync(root+'evaluation/'+name,'utf8'),/ROUTING:|NegativeFixtures|test[A-Z]|manifest\.json/);
  });
}
for(const [platform,framework,topic,folder] of [
  ['macOS','AppKit','modal-restoration','macos-lifecycle-v1'],['macOS','AppKit','display-preferences','macos-lifecycle-v1'],
  ['tvOS','UIKit','modal-restoration','tvos-lifecycle-v1'],['tvOS','UIKit','display-preferences','tvos-lifecycle-v1']]) {
  test(`${platform}/${topic}: detail is opt-in and platform-specific`,()=>{
    const r={platform,framework,topic},g=retrieve(r),e=retrieve({...r,level:'example'}),c=retrieve({...r,level:'contract'});
    assert.equal(g.paths.length,1);assert.ok(g.paths[0].startsWith('references/'));
    assert.equal(e.paths.length,2);assert.ok(e.paths[1].includes(folder));assert.equal(c.paths.length,4);
    assert.ok(g.loadedBytes<e.loadedBytes&&e.loadedBytes<c.loadedBytes);assert.equal(c.tokens,null);
    assert.equal(c.trace.length,4);assert.ok(c.paths.every(p=>!/evaluation|incidents|NegativeFixtures/.test(p)));
    const wrong=retrieve({...r,platform:platform==='tvOS'?'macOS':'tvOS'});assert.equal(wrong.loadedBytes,0);
  });
}
test('existing routes retain byte-for-byte behavior',()=>{
  for(const r of [{platform:'macOS',framework:'AppKit',topic:'actions'},{platform:'tvOS',framework:'UIKit',topic:'focus',level:'example'}])assert.deepEqual(retrieve(r),previous(r));
});
test('SwiftUI, Catalyst and unsupported detail cannot load companion examples',()=>{
  assert.equal(retrieve({platform:'macOS',framework:'SwiftUI',topic:'modal-restoration'}).loadedBytes,0);
  assert.equal(retrieve({platform:'macOS',framework:'UIKit',topic:'modal-restoration'}).loadedBytes,0);
  assert.throws(()=>retrieve({platform:'tvOS',framework:'UIKit',topic:'display-preferences',level:'all'}));
});
