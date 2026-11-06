// Synthetic assembler checks, not native Apple validation evidence.
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {assemble} from './os26-native-receipts.mjs';
import {assess,digest} from './os26.mjs';

const base=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../os26');
function fixture(t) {
  const root=fs.mkdtempSync(path.join(os.tmpdir(),'os26-receipt-test-'));
  t.after(()=>fs.rmSync(root,{recursive:true,force:true}));
  const bytes=fs.readFileSync(path.join(base,'fixtures/manifest.json'));
  const manifest=JSON.parse(bytes),records=[];
  fs.writeFileSync(path.join(root,'fixture-manifest.json'),bytes);
  fs.writeFileSync(path.join(root,'xcode.txt'),'Xcode synthetic\nBuild version synthetic');
  for(const c of manifest.cases)for(const variant of [c.candidate,...c.mutations]) {
    const id=variant.id??'candidate',stem=c.id+'-'+id;
    const log='SYNTHETIC ONLY '+(c.platform==='iOS'?'iPhoneSimulator':'AppleTVSimulator')+'27.0.sdk';
    const record={case:c.id,variant:id,observed:variant.expected,variantHash:variant.sha256,
      testSuiteHash:'a'.repeat(64),executedTestIds:[c.testId],
      failedTestIds:id==='candidate'?[]:[c.testId],expectedFailureTestIds:id==='candidate'?[]:[c.testId],
      logHash:digest(log),summary:{totalTestCount:1,skippedTests:0,
        devicesAndConfigurations:[{device:{osBuildNumber:'synthetic'}}]}};
    fs.writeFileSync(path.join(root,stem+'.log'),log);
    fs.writeFileSync(path.join(root,stem+'-intent.json'),JSON.stringify(record));
    records.push(record);
  }
  const save=()=>fs.writeFileSync(path.join(root,'results.json'),JSON.stringify(records));
  save();return {root,records,save};
}
test('assembler keeps all six cases blocked without independent review',t=>{
  const {root}=fixture(t),evidence=assemble(root);
  const p=fs.readFileSync(path.join(base,'prompts.json')),a=fs.readFileSync(path.join(base,'acceptance.json'));
  const status=assess(JSON.parse(p),JSON.parse(a),evidence,{promptHash:digest(p),acceptanceHash:digest(a)},root);
  assert.equal(evidence.cases.length,6);assert.equal(status.goldReady,0);
  assert.ok(evidence.cases.every(c=>!c.independentReviewer));
  assert.ok(status.cases.every(c=>c.gates.some(g=>g.reason==='independent_review_pending')));
});
for(const [name,change] of [
  ['incomplete matrix',f=>f.records.pop()],
  ['duplicate matrix',f=>f.records[1]=f.records[0]],
  ['infrastructure failure',f=>f.records[1].observed='error'],
  ['skipped test',f=>f.records[1].summary.skippedTests=1],
  ['wrong test',f=>f.records[1].executedTestIds=['Other/test']],
  ['changed suite',f=>f.records[1].testSuiteHash='b'.repeat(64)],
  ['changed variant',f=>f.records[1].variantHash='b'.repeat(64)],
  ['changed intent',f=>f.records[1].expectedFailureTestIds=[]],
  ['changed log',f=>fs.appendFileSync(path.join(f.root,'GP26-01-candidate.log'),'changed')],
])test('assembler rejects '+name,t=>{const f=fixture(t);change(f);f.save();assert.throws(()=>assemble(f.root));});
