import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import {hash} from './contracts.mjs';import {retrieve} from './closure-retrieval.mjs';
const cases=JSON.parse(fs.readFileSync('research/evaluation/cross-platform-closure-v1/prompt-records.json')).cases;
for(const c of cases)test(c.id+' paired contract and opt-in retrieval',()=>{
 const m=JSON.parse(fs.readFileSync(c.nativeManifest)),base=c.nativeManifest.replace('/manifest.json','');
 for(const f of m.files)assert.equal(hash(fs.readFileSync(base+'/'+f.path)),f.sha256);
 assert.ok(c.testIds.length>0);const rubric=fs.readFileSync(c.analysis.path,'utf8');for(const t of c.testIds)assert.ok(rubric.includes(t));
 assert.equal(hash(fs.readFileSync(c.subject.path)),c.subject.sha256);assert.doesNotMatch(c.subject.text,/ROUTING:|NegativeFixtures|test[A-Z]|manifest\.json/);
 const q={platform:c.platform,framework:c.framework,topic:c.id.split('/')[1]},g=retrieve(q),e=retrieve({...q,level:'example'}),v=retrieve({...q,level:'contract'});
 assert.equal(g.paths.length,1);assert.equal(e.paths.length,2);assert.equal(v.paths.length,4);assert.ok(g.loadedBytes<e.loadedBytes&&e.loadedBytes<v.loadedBytes);assert.equal(v.tokens,null);
 for(const t of v.trace){assert.ok(t.path.startsWith((c.retrievalPackage?'code-examples/platforms/'+c.retrievalPackage:base)+'/'));assert.equal(hash(fs.readFileSync(t.path)),t.sha256);assert.doesNotMatch(t.path,/evaluation|NegativeFixtures|incidents/);}
});
test('closure rejects wrong framework and unknown topic without cross-platform borrowing',()=>{
 for(const q of [{platform:'macOS',framework:'UIKit',topic:'text-rotor'},{platform:'tvOS',framework:'AppKit',topic:'text-rotor'},{platform:'iOS',framework:'SwiftUI',topic:'validation-ownership'}])assert.equal(retrieve(q).loadedBytes,0);
});

test('all selected source and mutant manifests validate before execution',async()=>{
 const {validateManifest}=await import('./contracts.mjs');
 for(const folder of ['ios-closure-v1','macos-closure-v1','tvos-closure-v1','macos-closure-details-v1','tvos-state-recovery-v1']){const dir='code-examples/platforms/'+folder;validateManifest(JSON.parse(fs.readFileSync(dir+'/manifest.json')),dir);}
});

test('campaign runner rejects incomplete invocation without starting native tools',async()=>{
 const {spawnSync}=await import('node:child_process');
 for(const args of [[],['run'],['freeze','relative','ios','tv'],['freeze','/private/tmp/unused','ios']]){
 const r=spawnSync(process.execPath,['code-examples/tools/closure-campaign.mjs',...args],{encoding:'utf8'});assert.notEqual(r.status,0);assert.match(r.stderr,/Usage:/);}
});
