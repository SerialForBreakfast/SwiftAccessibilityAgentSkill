/** Bounded local llama.cpp development experiment. Import/dry-run never infer. */
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';
import {repo,evaluate,settings,verifyBaseline,fingerprint,hash} from './lib.mjs';
import {protocol} from './protocol.mjs';
export const LOOKUP_INSTRUCTION='For accessibility questions that require this skill’s repository guidance, call read_reference before giving repository-backed advice. Copy the exact path from the supplied inventory, including the references/ prefix. A listed path is not evidence that its contents were read. Cite only references whose contents were returned successfully. For questions unrelated to accessibility, answer directly without reading references.';
export function plan(scenarios){
 const ids=['D01','D02','D03','D31'];
 return ids.flatMap(id=>{const s=scenarios.find(s=>s.id===id);if(!s||s.split!=='development'||s.turns.length!==1)throw Error('Expected single-turn development case');
 return [1024,2048].flatMap(outputLimit=>['C0','C2','C3-original','C3-explicit'].map(arm=>({scenario:s,os:s.os[0],outputLimit,arm,condition:arm.startsWith('C3')?'C3':arm})));});
}
export function augment(body,arm){
 const value=structuredClone(body);
 if(arm==='C3-explicit')value.messages[0].content+='\nDevelopment lookup instruction:\n'+LOOKUP_INSTRUCTION;
 return value;
}
export function localBase(config){
 const url=new URL(config.url);
 if(url.protocol!=='http:'||!['127.0.0.1','[::1]','localhost'].includes(url.hostname)||url.pathname!=='/v1'||url.username||url.password||url.search||url.hash||config.key)throw Error('Local unauthenticated llama.cpp loopback /v1 required');
 return url.origin;
}
export function transport({config,out,arm,caseId,counter,exchanges,fetcher=fetch}){
 const base=localBase(config);
 return async(url,options)=>{
  if(url!==config.url+'/chat/completions')throw Error('Unexpected generation destination');
  if(counter.calls>=160)throw Error('Generation budget exhausted');
  const body=augment(JSON.parse(options.body),arm);
  const post=async(route,payload)=>{const r=await fetcher(base+route,{method:'POST',redirect:'error',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload),signal:AbortSignal.timeout(120000)});if(!r.ok)throw Error('Tokenizer HTTP '+r.status);return r.json();};
  const template=await post('/apply-template',{messages:body.messages,tools:body.tools||[],add_generation_prompt:true,chat_template_kwargs:{enable_thinking:false}});
  if(typeof template.prompt!=='string')throw Error('Missing template');
  const tokens=(await post('/tokenize',{content:template.prompt,add_special:true,parse_special:true})).tokens;
  if(!Array.isArray(tokens)||!tokens.every(Number.isInteger))throw Error('Invalid token count');
  if(tokens.length+config.maxTokens>config.metadata.contextLimit)throw Error('Context overflow; no truncation');
  const id=String(++counter.calls).padStart(3,'0');
  fs.writeFileSync(path.join(out,'request-'+id+'.json'),JSON.stringify({case:caseId,operation:'llamacpp-development-v1-'+id,inputTokens:tokens.length,body}),{flag:'wx',mode:0o600});
  const started=performance.now();
  const response=await fetcher(url,{...options,redirect:'error',body:JSON.stringify(body)});
  if(!response.ok)throw Error('Generation HTTP '+response.status);
  const data=await response.json();fs.writeFileSync(path.join(out,'response-'+id+'.json'),JSON.stringify(data),{flag:'wx',mode:0o600});
  exchanges.push({request:id,inputTokens:tokens.length,usage:data.usage??null,finishReason:data.choices?.[0]?.finish_reason??null,seconds:(performance.now()-started)/1000});
  return {ok:true,json:async()=>data};
 };
}
async function main(){
 const scenarios=JSON.parse(fs.readFileSync(path.join(repo,'evals/scenarios.json'))),jobs=plan(scenarios);verifyBaseline();
 const pin=fingerprint(repo),manifest={experiment:'llamacpp-development-v1',skillHash:pin,suiteHash:hash(fs.readFileSync(path.join(repo,'evals/scenarios.json'))),runnerSha256:hash(fs.readFileSync(fileURLToPath(import.meta.url))),librarySha256:hash(fs.readFileSync(path.join(repo,'evals/runner/lib.mjs'))),lookupInstruction:LOOKUP_INSTRUCTION,jobs:jobs.length,maxGenerationRequests:160,outputLimits:[1024,2048],maxConcurrency:1,heldout:false,qualityGraded:false};
 if(!process.argv.includes('--execute')){console.log(JSON.stringify(manifest,null,2));return;}
 if(process.env.EVAL_ALLOW_NETWORK!=='1')throw Error('Explicit run approval required');
 const config=settings('bigdog');localBase(config);
 if(config.extra.chat_template_kwargs?.enable_thinking!==false||config.extra.temperature!==0||config.extra.seed!==42)throw Error('Frozen settings required: thinking false, temperature 0, seed 42');
 const out=process.env.EVAL_OUTPUT;if(!out)throw Error('New private EVAL_OUTPUT required');fs.mkdirSync(out,{mode:0o700});
 fs.writeFileSync(path.join(out,'manifest.json'),JSON.stringify({...manifest,provider:config.metadata},null,2));
 const counter={calls:0};let completed=0,active=null;
 try{for(const j of jobs){
  if(fingerprint(repo)!==pin)throw Error('Skill changed mid-run');
  active=[j.scenario.id,j.os,j.outputLimit,j.arm].join('-');const exchanges=[];
  const selected={...j.scenario,os:[j.os],turns:j.scenario.turns.map(t=>j.scenario.references.length?t+'\nDeployment context: '+j.scenario.platform+' OS version '+j.os+'. Clarify platform if needed.':t)};
  const effective={...config,maxTokens:j.outputLimit,metadata:{...config.metadata,maxTokens:j.outputLimit}};
  const started=performance.now();const result=await evaluate({root:repo,condition:j.condition,scenario:selected,config:effective,fetcher:transport({config:effective,out,arm:j.arm,caseId:active,counter,exchanges})});
  result.metadata.protocol=protocol(result,fs.readFileSync(path.join(repo,'VERSION'),'utf8').trim());
  const record={case:active,arm:j.arm,outputLimit:j.outputLimit,scenario:j.scenario.id,os:j.os,seconds:(performance.now()-started)/1000,exchanges,...result};
  fs.appendFileSync(path.join(out,'records.jsonl'),JSON.stringify(record)+'\n');completed++;console.log(JSON.stringify({case:active,completed,calls:counter.calls,reads:result.metadata.trace.length,truncated:exchanges.some(e=>e.finishReason==='length')}));
 }
 fs.writeFileSync(path.join(out,'summary.json'),JSON.stringify({state:'completed',completed,calls:counter.calls}));
 }catch(error){fs.writeFileSync(path.join(out,'summary.json'),JSON.stringify({state:'stopped',completed,calls:counter.calls,active,error:error.message}));throw error;}
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))main().catch(error=>{console.error(error.message);process.exitCode=1;});
