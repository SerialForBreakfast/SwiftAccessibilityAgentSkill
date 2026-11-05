/** Runs only unattempted cells after a preserved stopped campaign. Never retries. */
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';
import {repo,evaluate,fingerprint,hash} from './lib.mjs';
import {recordedDeadline} from './ollama-safety.mjs';
import {transport} from './ollama-development.mjs';import {protocol} from './protocol.mjs';
export function remaining(parent,records,status,attemptedCases){
  if(status.state!=='stopped'||status.active!=='D24-26-2048-C3-explicit'||records.length!==20||status.calls!==21)throw Error('Unexpected parent state');
  const seen=new Set(records.map(r=>r.case));if(seen.size!==20||seen.has(status.active))throw Error('Conflicting case states');
  const jobs=parent.jobs.filter(j=>!seen.has(`${j.scenario.id}-${j.scenario.os[0]}-2048-${j.arm}`)&&`${j.scenario.id}-${j.scenario.os[0]}-2048-${j.arm}`!==status.active);
  if(jobs.length!==3||jobs.some(j=>j.scenario.id!=='D30')||jobs.some(j=>attemptedCases.has(`${j.scenario.id}-${j.scenario.os[0]}-2048-${j.arm}`)))throw Error('Unattempted hosting cells only');
  return jobs;
}
async function main(){
  const parentDir=path.join(repo,'evals/results/maxmini-qwen35-questions-v2'),parentFile=path.join(parentDir,'manifest.json'),parent=JSON.parse(fs.readFileSync(parentFile)),status=JSON.parse(fs.readFileSync(path.join(parentDir,'summary.json'))),records=fs.readFileSync(path.join(parentDir,'records.jsonl'),'utf8').trim().split('\n').map(JSON.parse);
  const requestFiles=fs.readdirSync(parentDir).filter(n=>/^request-\d+\.json$/.test(n));if(requestFiles.length!==21)throw Error('Unexpected request count');
  const attempted=new Set(requestFiles.map(n=>JSON.parse(fs.readFileSync(path.join(parentDir,n))).case)),jobs=remaining(parent,records,status,attempted);
  for(const p of parent.sourcePins)if(hash(fs.readFileSync(path.join(repo,p.path)))!==p.sha256)throw Error('Parent source changed');
  if(fingerprint(repo)!==parent.skillHash)throw Error('Skill changed');
  const manifest={experiment:'maxmini-ollama-questions-v2-remaining-v1',parentManifestSHA256:hash(fs.readFileSync(parentFile)),parentExperiment:parent.experiment,parentCompleted:20,parentFailedCase:status.active,parentCalls:21,failedCaseRetried:false,jobs,provider:parent.provider,sourceSHA256:hash(fs.readFileSync(fileURLToPath(import.meta.url))),remainingRequestBudget:99,originalDeadlineEpochMs:recordedDeadline(parent),heldout:false,qualityGraded:false};
  if(!process.argv.includes('--execute')){console.log(JSON.stringify(manifest,null,2));return;}
  if(process.env.EVAL_ALLOW_NETWORK!=='1'||!process.env.EVAL_OUTPUT)throw Error('Execution and new directory required');
  const out=process.env.EVAL_OUTPUT;fs.mkdirSync(out,{mode:0o700});fs.writeFileSync(path.join(out,'manifest.json'),JSON.stringify(manifest,null,2));
  const counter={calls:0};let completed=0,active=null;
  try{for(const j of jobs){
    if(fingerprint(repo)!==parent.skillHash)throw Error('Skill changed');
    for(const p of parent.sourcePins)if(hash(fs.readFileSync(path.join(repo,p.path)))!==p.sha256)throw Error('Parent source changed');
    active=`${j.scenario.id}-${j.scenario.os[0]}-2048-${j.arm}`;const exchanges=[],started=performance.now(),config={url:'http://127.0.0.1:11434/v1',model:parent.provider.model,maxTokens:2048,extra:{temperature:0,seed:42},metadata:parent.provider};
    const send=transport({out,arm:j.arm,caseId:active,counter,exchanges,expectedDigest:parent.safety?.expectedDigest,deadlineEpochMs:manifest.originalDeadlineEpochMs}),bounded=async(...args)=>{if(counter.calls>=99||Date.now()>manifest.originalDeadlineEpochMs)throw Error('Original campaign budget exhausted');return send(...args);};
    const result=await evaluate({root:repo,condition:j.condition,scenario:j.scenario,config,fetcher:bounded});result.metadata.protocol=protocol(result,fs.readFileSync(path.join(repo,'VERSION'),'utf8').trim());
    fs.appendFileSync(path.join(out,'records.jsonl'),JSON.stringify({case:active,arm:j.arm,outputLimit:2048,scenario:j.scenario.id,os:j.scenario.os[0],question:j.scenario.turns,seconds:(performance.now()-started)/1000,exchanges,...result})+'\n');completed++;console.log(JSON.stringify({case:active,completed,calls:counter.calls,reads:result.metadata.trace.length}));
  }fs.writeFileSync(path.join(out,'summary.json'),JSON.stringify({state:'completed',completed,calls:counter.calls}));
  }catch(e){fs.writeFileSync(path.join(out,'summary.json'),JSON.stringify({state:'stopped',completed,calls:counter.calls,active,error:e.message}));throw e;}
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))main().catch(e=>{console.error(e.message);process.exitCode=1;});
