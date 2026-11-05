import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {requestTimeout, recordedDeadline, verifyIdentity} from './ollama-safety.mjs';
import {transport} from './ollama-development.mjs';

const digest = 'a'.repeat(64);
test('timeouts respect remaining absolute budget and reject missing/expired deadlines', () => {
  assert.equal(requestTimeout(1050,1000),50);
  assert.equal(requestTimeout(999999,1000),120000);
  assert.throws(()=>requestTimeout(1000,1000));
  assert.throws(()=>recordedDeadline({}));
  assert.throws(()=>recordedDeadline({deadlineEpochMs:1}));
});
test('mutable model tag must resolve to the qualified manifest digest', async () => {
  const args={model:'local',expectedDigest:digest,deadlineEpochMs:Date.now()+5000};
  const fetcher=async()=>({ok:true,json:async()=>({models:[{name:'local',digest:'b'.repeat(64)}]})});
  await assert.rejects(verifyIdentity({...args,fetcher}),/identity changed/);
  await assert.rejects(verifyIdentity({...args,expectedDigest:undefined,fetcher}),/digest required/);
});
test('identity failure prevents generation and request accounting', async()=>{
  let generations=0;
  const counter={calls:0};
  const send=transport({counter,expectedDigest:digest,deadlineEpochMs:Date.now()+5000,
    fetcher:async(url)=>{if(url.endsWith('/api/chat'))generations++;return {ok:true,json:async()=>({models:[]})};}});
  await assert.rejects(send('http://127.0.0.1:11434/v1/chat/completions',{
    body:JSON.stringify({model:'local',messages:[],max_completion_tokens:1024})}),/identity changed/);
  assert.equal(generations,0);assert.equal(counter.calls,0);
});
test('post-generation tag drift preserves response and rejection evidence', async()=>{
  const out=fs.mkdtempSync(path.join(os.tmpdir(),'ollama-safety-'));
  let checks=0;
  try {
    const send=transport({out,caseId:'test',arm:'C0',counter:{calls:0},exchanges:[],
      expectedDigest:digest,deadlineEpochMs:Date.now()+5000,
      fetcher:async(url)=>({ok:true,json:async()=>url.endsWith('/api/tags')?
        {models:[{name:'local',digest:++checks===1?digest:'b'.repeat(64)}]}:
        {model:'local',done:true,message:{content:'answer'},prompt_eval_count:10,eval_count:2}})});
    await assert.rejects(send('http://127.0.0.1:11434/v1/chat/completions',{
      body:JSON.stringify({model:'local',messages:[],max_completion_tokens:1024})}),/identity changed/);
    assert.ok(fs.existsSync(path.join(out,'response-001.json')));
    assert.equal(JSON.parse(fs.readFileSync(path.join(out,'failure-001.json'))).status,'response_rejected');
  } finally {fs.rmSync(out,{recursive:true,force:true});}
});
