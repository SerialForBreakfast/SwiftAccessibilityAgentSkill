import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {hash} from './contracts.mjs';

// All SDK commands are synthetic. These tests never invoke Xcode or a simulator.
function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(),'campaign-cli-'));
  t.after(()=>fs.rmSync(root,{recursive:true,force:true}));
  const tools = path.join(root,'code-examples/tools'), bin = path.join(root,'bin'), output = path.join(root,'run');
  fs.mkdirSync(tools,{recursive:true}); fs.mkdirSync(bin);
  for (const name of ['campaign.mjs','campaign-core.mjs','contracts.mjs','native-core.mjs'])
    fs.copyFileSync(new URL(name,import.meta.url),path.join(tools,name));
  fs.writeFileSync(path.join(tools,'native.mjs'), 'throw Error("Synthetic adapter must not execute");');
  const shim = `#!${process.execPath}
import path from 'node:path';
const args=process.argv.slice(2).join(' '), runtime='com.apple.CoreSimulator.SimRuntime.iOS-26-5';
if(path.basename(process.argv[1])==='xcodebuild') console.log('Synthetic Xcode');
else if(args.includes('devices')) console.log(JSON.stringify({devices:{[runtime]:[{udid:'fixture',isAvailable:true}]}}));
else if(args.includes('runtimes')) console.log(JSON.stringify({runtimes:[{identifier:runtime,version:'26.5',buildversion:process.env.FAKE_RUNTIME_BUILD||'anchor',isAvailable:true}]}));
else console.log('synthetic');
`;
  fs.writeFileSync(path.join(bin,'package.json'),'{}');
  // Extensionless shim is CommonJS, so use require rather than ESM syntax.
  for(const name of ['xcrun','xcodebuild']) fs.writeFileSync(path.join(bin,name),shim.replace("import path from 'node:path';","const path=require('node:path');"),{mode:0o755});
  const packages=['code-examples/pilots/fixture','research/evaluation/failure-driven/checkout-contract-v1'];
  for(const pkg of packages) {
    fs.mkdirSync(path.join(root,pkg),{recursive:true});
    fs.writeFileSync(path.join(root,pkg,'source.swift'),'import UIKit');
    const m={schema:1,id:'fixture',revision:'1',platform:'iOS',deploymentTarget:'26.0',runtimeMajor:26,
      limitations:'Synthetic offline harness fixture',claims:[{id:'c',url:'https://developer.apple.com/documentation/uikit',
      statement:'Synthetic',section:'Synthetic',availability:'Synthetic',reviewedOn:'2026-11-06'}],
      files:[{path:'source.swift',sha256:hash('import UIKit')}],
      checks:[{id:'compile',lane:'compile',expected:'success',claimIds:['c'],testIds:[],failureIds:[]}]};
    fs.writeFileSync(path.join(root,pkg,'manifest.json'),JSON.stringify(m));
  }
  const run=(mode,env={})=>spawnSync(process.execPath,[path.join(tools,'campaign.mjs'),mode,output,'fixture'],
    {encoding:'utf8',env:{...process.env,PATH:bin+path.delimiter+process.env.PATH,...env},timeout:20000});
  const frozen=run('freeze'); assert.equal(frozen.status,0,frozen.stderr);
  return {root,tools,output,run,package:packages[0]};
}
test('CLI freeze is exclusive and preserves first snapshot',t=>{
  const f=fixture(t), before=fs.readFileSync(path.join(f.output,'plan.json'));
  assert.notEqual(f.run('freeze').status,0);
  assert.deepEqual(fs.readFileSync(path.join(f.output,'plan.json')),before);
});
test('CLI resume rejects actual environment drift before invoking adapter',t=>{
  const f=fixture(t),r=f.run('run',{FAKE_RUNTIME_BUILD:'changed'});
  assert.notEqual(r.status,0);assert.match(r.stderr,/Environment fingerprint mismatch/);
});
for(const where of ['working','snapshot']) test(`CLI resume rejects ${where} source drift`,t=>{
  const f=fixture(t),base=where==='working'?f.root:path.join(f.output,'snapshot');
  fs.writeFileSync(path.join(base,f.package,'source.swift'),'changed');
  const r=f.run('run');assert.notEqual(r.status,0);assert.match(r.stderr,/Frozen input changed/);
});
test('CLI resume rejects adapter drift',t=>{
  const f=fixture(t);fs.appendFileSync(path.join(f.tools,'native.mjs'),'\n// changed');
  assert.match(f.run('run').stderr,/Adapter fingerprint mismatch/);
});
test('CLI retains interrupted attempt rather than replacing it',t=>{
  const f=fixture(t),run=path.join(f.output,'p01-compile');fs.mkdirSync(run);
  fs.writeFileSync(path.join(run,'first-diagnostic'),'original failure');
  assert.match(f.run('run').stderr,/Interrupted attempt retained/);
  assert.equal(fs.readFileSync(path.join(run,'first-diagnostic'),'utf8'),'original failure');
  assert.equal(JSON.parse(fs.readFileSync(path.join(f.output,'index.json'))).remaining,2);
});
test('CLI refuses a live campaign lock',t=>{
  const f=fixture(t);fs.writeFileSync(path.join(f.output,'execution.lock'),JSON.stringify({pid:process.pid,host:os.hostname()}));
  assert.match(f.run('run').stderr,/Campaign already running/);
});
test('CLI refuses changed plan contents',t=>{
  const f=fixture(t);fs.appendFileSync(path.join(f.output,'plan.json'),' ');
  assert.match(f.run('run').stderr,/Plan hash mismatch/);
});

function receipt(f,index,status='passed') {
  const plan=JSON.parse(fs.readFileSync(path.join(f.output,'plan.json'))), c=plan.checks[index];
  const pkg=plan.packages.find(p=>p.key===c.package), output=path.join(f.output,c.key);
  fs.mkdirSync(output); fs.writeFileSync(path.join(output,'evidence.txt'),'synthetic only');
  const failed=status==='failed',infra=status==='error';
  const r={schema:1,runId:'synthetic-'+index,manifestHash:pkg.manifestHash,checkId:c.check,
    recordedAt:'2026-11-06T00:00:00Z',sourceRevision:'synthetic',provenance:'synthetic',status,
    observed:infra?'not-assessed':failed?'failure':'success',reason:infra?'Synthetic infrastructure stop':undefined,
    environment:{...plan.environment,platform:'iOS',deploymentTarget:'26.0',destinationType:'compile-only',runtimeVersion:null,runtimeBuild:null},
    command:['synthetic-no-execution'],artifacts:[{path:'evidence.txt',sha256:hash('synthetic only')}],
    execution:{exitCode:failed?1:0,signal:null,infrastructureError:null,build:failed?'failed':'passed',skippedTests:0,
      executedTestIds:[],failedTestIds:[],diagnosticIds:failed?['synthetic-error']:[]}};
  const file=path.join(output,'result.json');fs.writeFileSync(file,JSON.stringify(r));return file;
}
test('CLI resume validates completed receipts without rewriting or rerunning them',t=>{
  const f=fixture(t),files=[receipt(f,0),receipt(f,1)],before=files.map(p=>hash(fs.readFileSync(p)));
  const r=f.run('run');assert.equal(r.status,0,r.stderr);
  assert.deepEqual(files.map(p=>hash(fs.readFileSync(p))),before);
  assert.equal(JSON.parse(fs.readFileSync(path.join(f.output,'index.json'))).remaining,0);
});
test('CLI continues to independent check after a contract failure',t=>{
  const f=fixture(t);receipt(f,0,'failed');receipt(f,1);
  const r=f.run('run');assert.equal(r.status,0,r.stderr);
  const index=JSON.parse(fs.readFileSync(path.join(f.output,'index.json')));
  assert.deepEqual(index.rows.map(r=>r.classification),['unexpected-contract-failure','positive-pass']);
});
test('CLI stops at infrastructure failure and leaves later receipt untouched',t=>{
  const f=fixture(t);receipt(f,0,'error');const later=receipt(f,1),before=hash(fs.readFileSync(later));
  assert.match(f.run('run').stderr,/Stop after infrastructure/);
  const index=JSON.parse(fs.readFileSync(path.join(f.output,'index.json')));
  assert.equal(index.remaining,1);assert.equal(hash(fs.readFileSync(later)),before);
});
