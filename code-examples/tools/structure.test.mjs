import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import {fileURLToPath} from 'node:url';
import {nativePlan} from './platform-core.mjs';import {retrieve} from './structure-retrieval.mjs';import {retrieve as previous} from './media-retrieval.mjs';
for(const folder of ['macos-structure-v1','tvos-structure-v1'])test(folder+' hashed native inputs and rubrics resolve',()=>{
 const root=fileURLToPath(new URL('../platforms/'+folder+'/',import.meta.url)),m=JSON.parse(fs.readFileSync(root+'manifest.json'));
 for(const c of m.checks)assert.equal(nativePlan(m,root,c.id).check.id,c.id);
 const names=fs.readdirSync(root+'evaluation'),rubrics=names.filter(n=>n.endsWith('.rubric.md')).map(n=>fs.readFileSync(root+'evaluation/'+n,'utf8')).join('\n');
 for(const id of m.checks.find(c=>c.id==='positive').testIds)assert.ok(rubrics.includes(id),id);
 for(const n of names.filter(n=>n.endsWith('.prompt.md')))assert.doesNotMatch(fs.readFileSync(root+'evaluation/'+n,'utf8'),/ROUTING:|NegativeFixtures|test[A-Z]|manifest\.json/);
});
for(const [platform,framework,topic] of [['macOS','AppKit','form-recovery'],['macOS','AppKit','outline-structure'],['tvOS','UIKit','form-recovery'],['tvOS','UIKit','shelf-structure']])test(platform+'/'+topic+' scoped opt-in loading',()=>{
 const q={platform,framework,topic},g=retrieve(q),e=retrieve({...q,level:'example'}),c=retrieve({...q,level:'contract'});
 assert.equal(g.paths.length,1);assert.equal(e.paths.length,2);assert.equal(c.paths.length,4);
 assert.ok(g.loadedBytes<e.loadedBytes&&e.loadedBytes<c.loadedBytes);assert.equal(c.tokens,null);
 assert.ok(c.paths.every(p=>p.includes(platform==='macOS'?'macos-structure-v1':'tvos-structure-v1')));assert.ok(c.paths.every(p=>!/evaluation|incidents|NegativeFixtures/.test(p)));
});
test('previous routes retain behavior and unsupported framework does not borrow contracts',()=>{
 for(const q of [{platform:'macOS',framework:'AVFoundation',topic:'media-metadata',level:'example'},{platform:'tvOS',framework:'UIKit',topic:'modal-restoration'},{platform:'macOS',framework:'AppKit',topic:'table-selection'}])assert.deepEqual(retrieve(q),previous(q));
 for(const q of [{platform:'macOS',framework:'SwiftUI'},{platform:'macOS',framework:'UIKit'},{platform:'tvOS',framework:'AppKit'},{platform:'iOS',framework:'UIKit'}])assert.equal(retrieve({...q,topic:'form-recovery'}).loadedBytes,0);
 assert.equal(retrieve({platform:'tvOS',framework:'UIKit',topic:'outline-structure'}).loadedBytes,0);
 assert.throws(()=>retrieve({platform:'macOS',framework:'AppKit',topic:'form-recovery',level:'all'}));
});
