import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import {fileURLToPath} from 'node:url';
import {nativePlan} from './platform-core.mjs';import {retrieve} from './media-retrieval.mjs';import {retrieve as previous} from './lifecycle-retrieval.mjs';
for(const folder of ['macos-media-v1','tvos-media-v1'])test(folder+' inputs and per-family rubrics resolve',()=>{
 const root=fileURLToPath(new URL('../platforms/'+folder+'/',import.meta.url)),m=JSON.parse(fs.readFileSync(root+'manifest.json'));
 for(const c of m.checks)assert.equal(nativePlan(m,root,c.id).check.id,c.id);
 const names=fs.readdirSync(root+'evaluation'),rubrics=names.filter(n=>n.endsWith('.rubric.md')).map(n=>fs.readFileSync(root+'evaluation/'+n,'utf8')).join('\n');
 for(const id of m.checks.find(c=>c.id==='positive').testIds)assert.ok(rubrics.includes(id),id);
 for(const n of names.filter(n=>n.endsWith('.prompt.md')))assert.doesNotMatch(fs.readFileSync(root+'evaluation/'+n,'utf8'),/ROUTING:|NegativeFixtures|test[A-Z]|manifest\.json/);
});
for(const [platform,framework] of [['macOS','AppKit'],['tvOS','UIKit'],['macOS','AVFoundation'],['tvOS','AVFoundation']])for(const topic of ['media-selection','media-metadata','media-inspection'])test(platform+'/'+framework+'/'+topic+' opt-in scope',()=>{
 const q={platform,framework,topic},g=retrieve(q),e=retrieve({...q,level:'example'}),c=retrieve({...q,level:'contract'});
 assert.equal(g.evidenceFramework,'AVFoundation');assert.equal(g.paths.length,1);assert.equal(e.paths.length,2);assert.equal(c.paths.length,topic==='media-inspection'?4:5);
 assert.ok(g.loadedBytes<e.loadedBytes&&e.loadedBytes<c.loadedBytes);assert.equal(c.tokens,null);
 assert.ok(c.paths.every(p=>p.includes(platform==='macOS'?'macos-media-v1':'tvos-media-v1')));
 assert.ok(c.paths.every(p=>!/evaluation|incidents|NegativeFixtures/.test(p)));
});
test('previous routes unchanged; wrong frameworks do not borrow media evidence',()=>{
 for(const q of [{platform:'macOS',framework:'AppKit',topic:'modal-restoration',level:'example'},{platform:'tvOS',framework:'UIKit',topic:'filtered-results'},{platform:'macOS',framework:'AppKit',topic:'actions'}])assert.deepEqual(retrieve(q),previous(q));
 for(const q of [{platform:'macOS',framework:'SwiftUI'},{platform:'macOS',framework:'UIKit'},{platform:'tvOS',framework:'AppKit'},{platform:'iOS',framework:'AVFoundation'}])assert.equal(retrieve({...q,topic:'media-selection'}).loadedBytes,0);
 assert.throws(()=>retrieve({platform:'macOS',framework:'AppKit',topic:'media-selection',level:'all'}));
});
