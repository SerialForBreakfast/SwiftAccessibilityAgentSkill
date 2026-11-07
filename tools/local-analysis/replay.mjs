// Offline Promptfoo evaluation. Only a captured-string provider and deterministic JS assertions.
import net from 'node:net';
import { fileURLToPath } from 'node:url';
export async function replay(records){
 const tests=records.map(r=>{
  if(typeof r.output!=='string'||r.output.length>1000000)throw Error('Captured output string required, at most one million characters');
  const assertions=r.assertions??(typeof r.expected==='string'?[{type:'equals',value:r.expected}]:[]);
  if(!assertions.length)throw Error('Reviewed deterministic expectation required');
  if(assertions.filter(a=>a.type==='equals').length>1)throw Error('One equality expectation per record');
  for(const a of assertions){
   if(!['equals','contains','not-contains','is-json'].includes(a.type))throw Error('Assertion type is not approved for offline replay');
   if(a.type!=='is-json'&&typeof a.value!=='string')throw Error('String expectation required');
   if(Object.keys(a).some(k=>!['type','value'].includes(k)))throw Error('Unexpected assertion options');
  }
  // Fixed code, never an expression supplied by an answer or an input record.
  const mapped=assertions.map(a=>a.type==='equals'?{type:'javascript',value:'output === context.vars.expected'}:a);
  return {description:r.id,vars:{captured:r.output,expected:assertions.find(a=>a.type==='equals')?.value??''},assert:mapped};
 });
 const env={...process.env};
 Object.assign(process.env,{PROMPTFOO_CONFIG_DIR:fileURLToPath(new URL('.cache/promptfoo/',import.meta.url)),PROMPTFOO_DISABLE_TELEMETRY:'1',PROMPTFOO_DISABLE_UPDATE_CHECK:'1',PROMPTFOO_CACHE_ENABLED:'false',PROMPTFOO_LOG_LEVEL:'error'});
 const connect=net.Socket.prototype.connect,fetch=globalThis.fetch;
 net.Socket.prototype.connect=function(){throw Error('Network disabled during offline replay');};
 globalThis.fetch=async()=>{throw Error('Network disabled during offline replay');};
 try{
  const {evaluate}=await import('promptfoo');
  const provider={id:()=> 'captured-output-only',callApi:async(_prompt,context)=>({output:context.vars.captured})};
  const result=await evaluate({prompts:['{{captured}}'],providers:[provider],tests},{maxConcurrency:1,writeResultsToDatabase:false,cache:false,showProgressBar:false});
  const summary=await result.toEvaluateSummary();
  return {scope:'Reviewed deterministic text checks, not general answer correctness or new generation',modelCalls:0,records:records.length,stats:summary.stats,results:summary.results?.map(r=>({success:r.success,score:r.score,error:r.error??null}))};
 }finally{net.Socket.prototype.connect=connect;globalThis.fetch=fetch;for(const k of Object.keys(process.env))if(!(k in env))delete process.env[k];Object.assign(process.env,env);}
}
