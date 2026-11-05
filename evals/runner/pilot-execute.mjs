/** Manifest-driven, serial local pilot. Import is offline; execution never retries. */
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {repo, hash, evaluate, verifyBaseline, readReference} from './lib.mjs';
import {planPilot} from './pilot.mjs';
import {coverage} from './campaign.mjs';
import {localBase} from './llamacpp-development.mjs';

export class Stop extends Error {
 constructor(status, message, fatal=false) { super(message); this.status=status; this.fatal=fatal; }
}
const save=(p,value)=>{const fd=fs.openSync(p,'wx',0o600);try{fs.writeFileSync(fd,JSON.stringify(value,null,2));fs.fsyncSync(fd);}finally{fs.closeSync(fd);}};
const read=p=>JSON.parse(fs.readFileSync(p));
export function validatePlan(plan) {
 if(JSON.stringify(plan)!==JSON.stringify(planPilot('bigdog')))throw Error('Manifest differs from current pinned BigDog pilot');
 verifyBaseline();
}
export function validateConfig(c) {
 localBase(c);
 if(c.maxTokens!==1024||c.metadata.contextLimit!==8192||c.extra.temperature!==0||c.extra.seed!==42||c.extra.chat_template_kwargs?.enable_thinking!==false)throw Error('Pilot requires 8192/1024, temperature 0, seed 42, thinking off');
 if(Object.keys(c.extra).sort().join(',')!=='chat_template_kwargs,seed,temperature'||!c.metadata.revision||!c.metadata.runtimeRevision)throw Error('Unqualified settings or identity');
}
export class Session {
 constructor({config,out,deadline,fetcher=fetch,now=Date.now,maxRequests=200}) {
  this.config=config;this.base=localBase(config);this.out=out;this.deadline=deadline;this.fetcher=fetcher;this.now=now;this.maxRequests=maxRequests;this.calls=0;this.jobId=null;this.preflights=0;
  if(!Number.isFinite(deadline)||!Number.isInteger(maxRequests)||maxRequests<0||maxRequests>200)throw Error('Invalid bounds');
 }
 remaining() {const n=this.deadline-this.now();if(n<=0)throw new Stop('cancelled','Entire execution deadline exhausted',true);return n;}
 async post(route,body,generation=false) {
  const timeout=Math.min(120000,this.remaining());
  let id;
  if(generation){
   if(this.calls>=this.maxRequests)throw new Stop('cancelled','Generation request cap exhausted',true);
   id=String(this.calls+1).padStart(3,'0');
   save(path.join(this.out,`request-${id}.json`),{operation:`${path.basename(this.out)}-${id}`,jobId:this.jobId,body,createdAt:this.now()});
   this.calls++;
  }
  const start=this.now();
  try {
   const response=await this.fetcher(this.base+route,{method:'POST',redirect:'error',headers:{'Content-Type':'application/json'},body:JSON.stringify(body),signal:AbortSignal.timeout(Math.max(1,Math.floor(timeout)))});
   if(!response.ok)throw Error(`HTTP ${response.status}`);
   let text;
   if(response.body?.getReader){
    const reader=response.body.getReader(),chunks=[];let size=0;
    while(true){const {done,value}=await reader.read();if(done)break;size+=value.length;if(size>8*1024*1024){await reader.cancel();throw Error('Response exceeds 8 MiB');}chunks.push(Buffer.from(value));}
    text=Buffer.concat(chunks).toString('utf8');
   }else{text=await response.text();if(Buffer.byteLength(text)>8*1024*1024)throw Error('Response exceeds 8 MiB');}
   const data=JSON.parse(text);
   if(generation){save(path.join(this.out,`response-${id}.json`),{jobId:this.jobId,seconds:(this.now()-start)/1000,data});}
   else fs.appendFileSync(path.join(this.out,'metadata.jsonl'),JSON.stringify({route,bodyHash:hash(JSON.stringify(body)),resultHash:hash(text),seconds:(this.now()-start)/1000})+'\n');
   return data;
  } catch(e) {
   if(generation)throw new Stop('unknown_outcome',`Contact ${id} uncertain; original intent retained, no replay`,true);
   throw new Stop('tokenizer_unavailable','Template/tokenizer request failed; no generation submitted',true);
  }
 }
 async generate(body) {
  this.remaining();if(this.calls>=this.maxRequests)throw new Stop('cancelled','Generation request cap exhausted',true);
  const preflightId=String(++this.preflights).padStart(3,'0');
  save(path.join(this.out,`input-${preflightId}.json`),{jobId:this.jobId,body,bodyHash:hash(JSON.stringify(body)),createdAt:this.now()});
  const rendered=await this.post('/apply-template',{messages:body.messages,tools:body.tools||[],add_generation_prompt:true,chat_template_kwargs:body.chat_template_kwargs,...(body.tool_choice?{tool_choice:body.tool_choice}:{})});
  if(typeof rendered.prompt!=='string')throw new Stop('tokenizer_unavailable','Template missing',true);
  const result=await this.post('/tokenize',{content:rendered.prompt,add_special:true,parse_special:true});
  if(!Array.isArray(result.tokens)||!result.tokens.every(Number.isInteger))throw new Stop('tokenizer_unavailable','Exact tokenizer unavailable',true);
  const fit={jobId:this.jobId,bodyHash:hash(JSON.stringify(body)),renderedHash:hash(rendered.prompt),inputTokens:result.tokens.length,outputTokens:body.max_completion_tokens,contextTokens:this.config.metadata.contextLimit};
  fs.appendFileSync(path.join(this.out,'token-fit.jsonl'),JSON.stringify(fit)+'\n');
  if(fit.inputTokens+fit.outputTokens>fit.contextTokens)throw new Stop('context_overflow','Full input plus reserved output exceeds context; not shortened');
  const data=await this.post('/v1/chat/completions',body,true);
  if(!data.choices?.[0]?.message||!['stop','length','tool_calls'].includes(data.choices[0].finish_reason))throw new Stop('transport_error','Invalid assistant response retained',true);
  return data;
 }
 transport=async(url,options)=>{
  if(url!==this.config.url+'/chat/completions')throw new Stop('transport_error','Unexpected generation destination',true);
  const body=JSON.parse(options.body);
  if(this.root){
   for(const m of body.messages){
    if(m.role!=='tool')continue;
    const call=body.messages.flatMap(x=>x.tool_calls||[]).find(x=>x.id===m.tool_call_id);
    try{const r=readReference(this.root,JSON.parse(call.function.arguments).path);
     if(r.content===m.content&&!this.reads.some(x=>x.path===r.path))this.reads.push({path:r.path,sha256:r.sha256,bytes:r.bytes,origin:'model-tool'});
    }catch{}
   }
  }
  const data=await this.generate(body);return {ok:true,json:async()=>data};
 };
}
export async function qualify(session) {
 const c=session.config;
 const tool={type:'function',function:{name:'read_reference',description:'Read a supplied reference.',parameters:{type:'object',properties:{path:{type:'string'}},required:['path'],additionalProperties:false}}};
 const common={model:c.model,max_completion_tokens:128,...c.extra,stream:false,tools:[tool]};
 const messages=[{role:'user',content:'Call read_reference for references/fixture.md.'}];
 session.jobId='qualification';
 const first=await session.generate({...common,messages,tool_choice:{type:'function',function:{name:'read_reference'}}});
 const msg=first.choices[0].message,tc=msg.tool_calls;
 let args;try{args=JSON.parse(tc?.[0]?.function?.arguments);}catch{}
 if(tc?.length!==1||!tc[0].id||tc[0].function.name!=='read_reference'||typeof args?.path!=='string')throw new Stop('unsupported_tools','Structured tool parser qualification failed',true);
 // Synthetic tool exchange only. No requested path is executed during qualification.
 const second=await session.generate({...common,messages:[...messages,msg,{role:'tool',tool_call_id:tc[0].id,content:'Synthetic reference fact: the verification word is BLUEBIRD. Reply with BLUEBIRD only.'}],tool_choice:'none'});
 const answer=second.choices[0];
 if(answer.message.tool_calls?.length||!answer.message.content?.includes('BLUEBIRD')||answer.finish_reason!=='stop')throw new Stop('unsupported_tools','Tool-result qualification failed',true);
 return {status:'passed',generationRequests:2,argumentMatchedRequestedPath:args.path==='references/fixture.md',note:'Forced synthetic parser/round-trip probe; not evidence of autonomous retrieval. Included in 200-request limit.'};
}
export function receipt(plan,c,job,status,count,extra={}) {
 return {planHash:plan.planHash,jobId:job.id,workerId:'bigdog',modelRevision:c.metadata.revision,runtimeRevision:c.metadata.runtimeRevision,status,generationRequests:count,referenceReads:[],...extra};
}
export function reconcile(plan,config,out,reason='Executor stopped; no replay') {
 // Accounting only. Never contacts the runtime or resubmits any intent.
 const requests=fs.readdirSync(out).filter(n=>/^request-\d+\.json$/.test(n)).map(n=>({name:n,...read(path.join(out,n))}));
 const rows=[];
 for(const job of plan.jobs){
  const file=path.join(out,`receipt-${job.id}.json`);
  if(!fs.existsSync(file)){
   const intents=requests.filter(x=>x.jobId===job.id);
   const uncertain=intents.some(x=>!fs.existsSync(path.join(out,x.name.replace('request-','response-'))));
   save(file,receipt(plan,config,job,uncertain?'unknown_outcome':'cancelled',intents.length,{reason,partialResponsesRetained:intents.length>0}));
  }
  rows.push(read(file));
 }
 fs.writeFileSync(path.join(out,'receipts.jsonl'),rows.map(x=>JSON.stringify(x)).join('\n')+'\n');
 const result=coverage(plan,rows);
 fs.writeFileSync(path.join(out,'coverage.json'),JSON.stringify(result,null,2));
 return {coverage:result,generationRequests:requests.length,qualificationRequests:requests.filter(x=>x.jobId==='qualification').length};
}
export async function execute({plan,config,out,deadline,fetcher=fetch,now=Date.now,qualification=qualify,validate=true}) {
 if(validate){validatePlan(plan);validateConfig(config);}
 if(!Number.isFinite(deadline)||deadline>now()+45*60*1000)throw Error('Invalid entire-run deadline');
 fs.mkdirSync(out,{mode:0o700});save(path.join(out,'plan.json'),plan);save(path.join(out,'deployment.json'),config.metadata);
 const session=new Session({config,out,deadline,fetcher,now});let reason='Completed planned jobs';
 try {
  const q=await qualification(session);save(path.join(out,'qualification.json'),q);
  const scenarios=read(path.join(repo,'evals/scenarios.json'));
  for(const job of plan.jobs){
   session.jobId=job.id;session.reads=[];const before=session.calls;
   try {
    session.remaining();if(validate)validatePlan(plan);
    const source=scenarios.find(x=>x.id===job.family);
    const scenario={...source,os:[job.os],turns:job.userTurns,references:job.referencePaths};
    session.root=path.resolve(repo,plan.roots[job.release].relativePath);session.reads=[];
    if(job.condition==='C2')for(const name of job.referencePaths){try{const r=readReference(session.root,name);session.reads.push({path:r.path,sha256:r.sha256,bytes:r.bytes,origin:'harness-injection'});}catch{}}
    const result=await evaluate({root:path.resolve(repo,plan.roots[job.release].relativePath),condition:job.condition,scenario,config,fetcher:session.transport});
    save(path.join(out,`result-${job.id}.json`),result);
    save(path.join(out,`receipt-${job.id}.json`),receipt(plan,config,job,result.metadata.truncated?'truncated':'completed',session.calls-before,{referenceReads:result.metadata.trace.map(x=>({...x,origin:job.condition==='C2'?'harness-injection':'model-tool'})),finishReasons:result.metadata.finishReasons,inputTokens:result.metadata.inputTokens,outputTokens:result.metadata.outputTokens,latencyMs:result.metadata.latencyMs}));
   }catch(e){
    save(path.join(out,`receipt-${job.id}.json`),receipt(plan,config,job,e.status||'transport_error',session.calls-before,{reason:e.message,partialResponsesRetained:session.calls>before,referenceReads:session.reads||[]}));
    if(e.fatal||!(e instanceof Stop))throw e;
   }
   console.log(JSON.stringify({jobId:job.id,family:job.family,condition:job.condition,release:job.release,generationRequests:session.calls}));
  }
 }catch(e){reason=e.message;if(!fs.existsSync(path.join(out,'qualification.json')))save(path.join(out,'qualification.json'),{status:'blocked',reason,generationRequests:session.calls});}
 const summary={...reconcile(plan,config,out,reason),reason};save(path.join(out,'summary.json'),summary);return summary;
}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href){
 const [mode,planFile,configFile,out,deadline]=process.argv.slice(2);
 if(mode==='execute'&&process.env.EVAL_ALLOW_NETWORK==='1')await execute({plan:read(planFile),config:read(configFile),out,deadline:Number(deadline)});
 else if(mode==='reconcile')console.log(JSON.stringify(reconcile(read(planFile),read(configFile),out)));
 else throw Error('Usage: EVAL_ALLOW_NETWORK=1 node pilot-execute.mjs execute plan config NEW_OUT deadlineEpochMs; or reconcile plan config OUT (offline only)');
}
