import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {nativePlan, selectDestination, hostDestination, packageSource, unitOutcome} from './platform-core.mjs';
import {select, retrieve} from './platform-retrieval.mjs';

for (const folder of ['macos-appkit-v1', 'tvos-uikit-v1']) {
  const root = fileURLToPath(new URL(`../platforms/${folder}/`, import.meta.url));
  test(`${folder}: every manifest check resolves pinned inputs`,()=>{
    const m = JSON.parse(fs.readFileSync(root+'manifest.json'));
    for(const c of m.checks) assert.equal(nativePlan(m,root,c.id).check.id,c.id);
  });
}
test('platform package and target validation',()=>{
  assert.match(packageSource('26.0','macOS'), /\.macOS\("26.0"\)/);
  assert.match(packageSource('26.0','tvOS'), /\.tvOS\("26.0"\)/);
  assert.throws(()=>packageSource('26;bad','tvOS'));
  assert.throws(()=>packageSource('26.0','iOS'));
});
test('tvOS selection rejects iOS and wrong major',()=>{
  const devices={devices:{'com.apple.CoreSimulator.SimRuntime.iOS-26-5':[{udid:'x',isAvailable:true}]}};
  const runtimes={runtimes:[{identifier:Object.keys(devices.devices)[0],version:'26.5',isAvailable:true}]};
  assert.throws(()=>selectDestination(devices,runtimes,'x',26));
  const id='com.apple.CoreSimulator.SimRuntime.tvOS-26-5';
  const ds={devices:{[id]:[{udid:'x',isAvailable:true}]}};
  const rs={runtimes:[{identifier:id,version:'26.5',buildversion:'b',isAvailable:true}]};
  assert.deepEqual(selectDestination(ds,rs,'x',26),{version:'26.5',build:'b'});
  assert.throws(()=>selectDestination(ds,rs,'x',27));
});
test('Mac runtime must match real host and exact destination',()=>{
  const d=[{platform:'com.apple.platform.macosx',available:true,architecture:'arm64',operatingSystemVersion:'27.0 (b)',identifier:'mac'}];
  assert.equal(hostDestination(d,'27.0','b',27,'arm64').uuid,'mac');
  assert.equal(hostDestination([{...d[0],architecture:'arm64e'}],'27.0','b',27,'arm64').uuid,'mac');
  assert.throws(()=>hostDestination(d,'27.0','b',27,'x86_64'));
  assert.throws(()=>hostDestination(d,'27.0','b',26,'arm64'));
  assert.throws(()=>hostDestination([...d,...d],'27.0','b',27,'arm64'));
});
test('unit outcome requires exact platform and complete tests',()=>{
  const dst={uuid:'mac',version:'27.0',build:'b',platform:'macOS'};
  const s={totalTestCount:1,skippedTests:0,failedTests:0,passedTests:1,devicesAndConfigurations:[{device:{deviceId:'mac',osVersion:'27.0',osBuildNumber:'b',platform:'macOS'}}]};
  const log="Test Case '-[AccessibilityExamplesTests.A testOne]' passed";
  assert.equal(unitOutcome({status:0},log,s,{testIds:['A/testOne']},dst).build,'passed');
  assert.throws(()=>unitOutcome({status:0},log,s,{testIds:['A/testOther']},dst));
  assert.throws(()=>unitOutcome({status:0},log,s,{testIds:['A/testOne']},{...dst,platform:'tvOS Simulator'}));
  assert.throws(()=>unitOutcome({status:65},log,s,{testIds:['A/testOne']},dst));
});
for (const [platform,framework,topics] of [['macOS','AppKit',['actions','notifications']],['tvOS','UIKit',['actions','focus','traits']]]) {
  for(const topic of topics) test(`${platform}/${topic}: progressive reads are bounded and traced`,()=>{
    const request={platform,framework,topic};
    const g=retrieve(request), e=retrieve({...request,level:'example'}), c=retrieve({...request,level:'contract'});
    assert.ok(g.paths.length<=2); assert.ok(g.paths.every(p=>p.startsWith('references/')));
    assert.equal(e.paths.length,g.paths.length+1); assert.equal(c.paths.length,e.paths.length+2);
    assert.ok(g.loadedBytes<e.loadedBytes && e.loadedBytes<c.loadedBytes);
    assert.equal(c.trace.length,c.paths.length); assert.equal(c.tokens,null);
    assert.ok(c.paths.every(p=>!/(evaluation|NegativeFixtures|incidents|baseline)/.test(p)));
    assert.ok(c.paths.every(p=>!p.includes(platform==='macOS'?'/tvos/':'/macos/')));
  });
}
for (const [platform,framework] of [['macOS','UIKit'],['macOS','SwiftUI'],['tvOS','SwiftUI'],['iOS','UIKit'],['unknown','unknown']]) {
  test(`${platform}/${framework}: never silently fallback`,()=>{
    const r=retrieve({platform,framework,topic:'actions'}); assert.equal(r.status,'clarify'); assert.equal(r.loadedBytes,0);
  });
}
test('unsupported topics and invalid detail do not load context',()=>{
  assert.deepEqual(select({platform:'tvOS',framework:'UIKit',topic:'rotor'}).paths,[]);
  assert.throws(()=>retrieve({platform:'tvOS',framework:'UIKit',topic:'actions',level:'all'}));
});
