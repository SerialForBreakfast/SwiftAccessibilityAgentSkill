/** Local Ollama comparison. Reuses frozen BigDog cases; never downloads models. */
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';
import {repo,evaluate,fingerprint,hash,verifyBaseline} from './lib.mjs';
import {requestTimeout,verifyIdentity,executionSafety,saveFailure} from './ollama-safety.mjs';
import {plan,augment} from './llamacpp-development.mjs';import {protocol} from './protocol.mjs';
export function nativeBody(body){return {model:body.model,messages:body.messages.map(m=>({role:m.role,content:m.content??'',...(m.tool_calls?{tool_calls:m.tool_calls.map(t=>({function:{name:t.function.name,arguments:typeof t.function.arguments==='string'?JSON.parse(t.function.arguments):t.function.arguments}}))}:{}),...(m.role==='tool'?{tool_name:'read_reference'}:{})})),...(body.tools?{tools:body.tools}:{}),stream:false,think:false,keep_alive:'10m',options:{num_ctx:16384,num_predict:body.max_completion_tokens,temperature:0,seed:42,top_p:1,top_k:0,presence_penalty:0,repeat_penalty:1}};}
export function openAI(data,id){if(!data.done||!data.message||data.message.thinking)throw Error('Incomplete response or unexpected thinking');const m=data.message;return {choices:[{message:{role:'assistant',content:m.content||'',...(m.tool_calls?.length?{tool_calls:m.tool_calls.map((t,i)=>({id:`local-${id}-${i}`,type:'function',function:{name:t.function.name,arguments:JSON.stringify(t.function.arguments)}}))}:{})},finish_reason:data.done_reason==='length'?'length':m.tool_calls?.length?'tool_calls':data.done_reason}],usage:{prompt_tokens:data.prompt_eval_count,completion_tokens:data.eval_count}};}
export function transport({out,arm,caseId,counter,exchanges,expectedDigest,deadlineEpochMs,fetcher=fetch}) {
  return async(url,options)=>{
    if(url!=='http://127.0.0.1:11434/v1/chat/completions') throw Error('Loopback required');
    requestTimeout(deadlineEpochMs);
    if(counter.calls>=160) throw Error('Request budget exhausted');
    const body=nativeBody(augment(JSON.parse(options.body),arm));
    const identity=await verifyIdentity({model:body.model,expectedDigest,deadlineEpochMs,fetcher});
    const id=String(++counter.calls).padStart(3,'0');
    fs.writeFileSync(path.join(out,`request-${id}.json`),JSON.stringify({case:caseId,body,identity,deadlineEpochMs}),{flag:'wx',mode:0o600});
    const started=performance.now();
    let received=false;
    try {
      const response=await fetcher('http://127.0.0.1:11434/api/chat',{method:'POST',redirect:'error',headers:{'Content-Type':'application/json'},body:JSON.stringify(body),signal:AbortSignal.timeout(requestTimeout(deadlineEpochMs))});
      if(!response.ok) throw Error('Ollama HTTP '+response.status);
      const data=await response.json();
      fs.writeFileSync(path.join(out,`response-${id}.json`),JSON.stringify(data),{flag:'wx',mode:0o600});
      received=true;
      requestTimeout(deadlineEpochMs);
      if(data.model!==body.model) throw Error('Model identity changed');
      const after=await verifyIdentity({model:body.model,expectedDigest,deadlineEpochMs,fetcher});
      fs.writeFileSync(path.join(out,`identity-${id}.json`),JSON.stringify({before:identity,after}),{flag:'wx',mode:0o600});
      if(!Number.isSafeInteger(data.prompt_eval_count)||data.prompt_eval_count<0||!Number.isSafeInteger(data.eval_count)||data.eval_count<0) throw Error('Token telemetry unavailable');
      if(data.prompt_eval_count+body.options.num_predict>16384) throw Error('Context budget exceeded');
      const result=openAI(data,id);
      exchanges.push({request:id,inputTokens:data.prompt_eval_count,usage:result.usage,finishReason:result.choices[0].finish_reason,seconds:(performance.now()-started)/1000,loadDurationNs:data.load_duration,evalDurationNs:data.eval_duration});
      return {ok:true,json:async()=>result};
    } catch(error) {
      saveFailure(out,id,received?'response_rejected':'unknown_outcome');
      throw error;
    }
  };
}
async function main(){verifyBaseline();const jobs=plan(JSON.parse(fs.readFileSync(path.join(repo,'evals/scenarios.json'))));const pin=fingerprint(repo),model='qwen3.5:latest',metadata={alias:'maxmini',model,revision:'dec52a44569a2a25341c4e4d3fee25846eed4f6f0b936278e3a3c900bb99d37c',serving:'Ollama 0.40.11 Metal',quantization:'Q4_K_M',contextLimit:16384,reasoning:'off',sampling:{temperature:0,seed:42,top_p:1,top_k:0,presence_penalty:0,repeat_penalty:1},concurrency:1};const manifest={experiment:'maxmini-ollama-development-v1',skillHash:pin,suiteHash:hash(fs.readFileSync(path.join(repo,'evals/scenarios.json'))),adapterSha256:hash(fs.readFileSync(fileURLToPath(import.meta.url))),librarySha256:hash(fs.readFileSync(path.join(repo,'evals/runner/lib.mjs'))),provider:metadata,jobs:32,maxGenerationRequests:160,heldout:false,qualityGraded:false,limitations:['Different weights and serving backend from BigDog; not hardware isolation.','Ollama has no qualified pre-generation tokenizer endpoint in this adapter. Prompt counts are checked after response; server logs must show no context truncation.','No retries, fallback, heldout tuning or model downloads.','Tool serialization follows native Ollama; prompt content and case membership reuse frozen BigDog plan.']};if(!process.argv.includes('--execute')){console.log(JSON.stringify(manifest,null,2));return;}if(process.env.EVAL_ALLOW_NETWORK!=='1')throw Error('Execution approval required');const safety=executionSafety(45);Object.assign(manifest,{safety,deadlineEpochMs:safety.deadlineEpochMs,experiment:'maxmini-ollama-development-safeguards-v2'});const out=process.env.EVAL_OUTPUT;if(!out)throw Error('New output required');fs.mkdirSync(out,{mode:0o700});fs.writeFileSync(path.join(out,'manifest.json'),JSON.stringify(manifest,null,2));let completed=0,active=null;const counter={calls:0};try{for(const j of jobs){if(fingerprint(repo)!==pin)throw Error('Skill changed');active=[j.scenario.id,j.os,j.outputLimit,j.arm].join('-');const selected={...j.scenario,os:[j.os],turns:j.scenario.turns.map(t=>j.scenario.references.length?t+'\nDeployment context: '+j.scenario.platform+' OS version '+j.os+'. Clarify platform if needed.':t)},exchanges=[],config={url:'http://127.0.0.1:11434/v1',model,maxTokens:j.outputLimit,extra:{temperature:0,seed:42},metadata:{...metadata,maxTokens:j.outputLimit}},started=performance.now();const result=await evaluate({root:repo,condition:j.condition,scenario:selected,config,fetcher:transport({out,arm:j.arm,caseId:active,counter,exchanges,...safety})});result.metadata.protocol=protocol(result,fs.readFileSync(path.join(repo,'VERSION'),'utf8').trim());fs.appendFileSync(path.join(out,'records.jsonl'),JSON.stringify({case:active,arm:j.arm,outputLimit:j.outputLimit,scenario:j.scenario.id,os:j.os,seconds:(performance.now()-started)/1000,exchanges,...result})+'\n');completed++;console.log(JSON.stringify({case:active,completed,calls:counter.calls,reads:result.metadata.trace.length,truncated:exchanges.some(e=>e.finishReason==='length')}));}fs.writeFileSync(path.join(out,'summary.json'),JSON.stringify({state:'completed',completed,calls:counter.calls}));}catch(e){fs.writeFileSync(path.join(out,'summary.json'),JSON.stringify({state:'stopped',completed,calls:counter.calls,active,error:e.message}));throw e;}}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))main().catch(e=>{console.error(e.message);process.exitCode=1;});
