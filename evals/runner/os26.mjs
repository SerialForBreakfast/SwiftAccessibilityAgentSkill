// Offline corpus/readiness gate only. No provider, shell, compiler or device execution.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath, pathToFileURL} from 'node:url';
export const digest = data => crypto.createHash('sha256').update(data).digest('hex');
const unique = (xs, label) => {if(new Set(xs).size !== xs.length) throw Error('Duplicate '+label);};
export function validateCatalog(prompts, acceptance) {
  if(prompts.schema!==1 || acceptance.schema!==1 || prompts.revision!==acceptance.revision || !prompts.cases?.length) throw Error('Invalid catalog revision/schema');
  unique(prompts.cases.map(c=>c.id),'case'); unique(acceptance.cases.map(c=>c.id),'acceptance case');
  if(acceptance.cases.length!==prompts.cases.length) throw Error('Acceptance coverage mismatch');
  for(const c of prompts.cases) {
    if(!/^GP26-\d{2}$/.test(c.id) || typeof c.prompt!=='string' || !c.prompt.includes('```swift') || c.target!=='26.0') throw Error('Invalid OS26 prompt');
    if(Object.keys(c).some(k=>['gates','criteria','expected','answer'].includes(k))) throw Error('Evaluator material in prompt catalog');
    const a=acceptance.cases.find(a=>a.id===c.id); if(!a?.gates?.length) throw Error('Missing acceptance');
    unique(a.gates.map(g=>g.id),'gate');
    for(const g of a.gates) if(!['pass','fail'].includes(g.expected) || !['review','compile','oracle','manual','unit'].includes(g.kind) || !g.assertion?.trim()) throw Error('Invalid atomic gate');
    for(const id of ['source-review','compile-host','known-good','mutation-1','mutation-2']) if(!a.gates.some(g=>g.id===id)) throw Error('Missing oracle gate '+id);
    if(a.gates.find(g=>g.id==='known-good').expected!=='pass' || ['mutation-1','mutation-2'].some(id=>a.gates.find(g=>g.id===id).expected!=='fail')) throw Error('Invalid oracle polarity');
  }
}
export function modelInput(prompts,id) {
  const c=prompts.cases.find(c=>c.id===id);if(!c)throw Error('Unknown case');
  return {role:'user',content:c.prompt};
}
function artifactValid(root,a) {
  if(!a || !/^[a-f0-9]{64}$/.test(a.sha256) || typeof a.path!=='string' || path.isAbsolute(a.path) || a.path.split(/[\\/]/).includes('..'))return false;
  try {
    const base=fs.realpathSync(root), file=fs.realpathSync(path.resolve(root,a.path));
    if(!file.startsWith(base+path.sep) || !fs.statSync(file).isFile())return false;
    return digest(fs.readFileSync(file))===a.sha256;
  }catch{return false;}
}
export function assess(prompts,acceptance,evidence,pins,evidenceRoot) {
  validateCatalog(prompts,acceptance);
  const records=evidence?.cases??[];unique(records.map(c=>c.id),'evidence case');
  if(records.some(c=>!prompts.cases.some(p=>p.id===c.id)))throw Error('Unknown evidence case');
  const pinned=evidence?.schema===1 && evidence.promptHash===pins.promptHash && evidence.acceptanceHash===pins.acceptanceHash;
  const cases=prompts.cases.map(c=>{
    const a=acceptance.cases.find(a=>a.id===c.id),r=records.find(r=>r.id===c.id);
    const recordsForCase=r?.checks??[];unique(recordsForCase.map(g=>g.id),'evidence gate');
    if(recordsForCase.some(g=>!a.gates.some(w=>w.id===g.id)))throw Error('Unknown evidence gate');
    const variants=['known-good','mutation-1','mutation-2'].map(id=>recordsForCase.find(g=>g.id===id)?.variantHash);
    const variantsValid=variants.every(h=>typeof h==='string' && /^[a-f0-9]{64}$/.test(h)) && new Set(variants).size===3;
    const gates=a.gates.map(g=>{
      const observed=recordsForCase.find(o=>o.id===g.id);
      let reason=null;
      if(!pinned)reason='missing_or_changed_input_pins';
      else if(!observed || ['not_run','not_assessable'].includes(observed.observed))reason='evidence_pending';
      else if(observed.observed!==g.expected)reason='unexpected_outcome';
      else if(g.kind==='oracle' && !variantsValid)reason='distinct_patch_variants_pending';
      else if(!observed.artifacts?.length || !observed.artifacts.every(a=>artifactValid(evidenceRoot,a)))reason='artifact_missing_or_hash_mismatch';
      else if(!r.fixtureAuthor || !r.independentReviewer || r.fixtureAuthor===r.independentReviewer)reason='independent_review_pending';
      else if(!r.sdkBuild || !r.runtimeBuild || !r.fixtureHash || !/^[a-f0-9]{64}$/.test(r.fixtureHash))reason='toolchain_fixture_identity_pending';
      return {id:g.id,ready:reason===null,reason};
    });
    return {id:c.id,status:gates.every(g=>g.ready)?'gold-ready':'blocked',gates};
  });
  return {revision:prompts.revision,total:cases.length,goldReady:cases.filter(c=>c.status==='gold-ready').length,cases,
    limitation:'Checks verify receipt completeness and artifact integrity, not the truth of external test reports. Owner acceptance and provider approval remain separate.'};
}
export function plan(prompts,readiness) {
  if(readiness.revision!==prompts.revision || readiness.total!==prompts.cases.length || readiness.goldReady!==prompts.cases.length || readiness.cases.some(c=>c.status!=='gold-ready'))throw Error('OS26 fixtures are not gold-ready; no runnable plan');
  return {revision:prompts.revision,providerExecution:false,approval:'separate-owner-approved-batch-required',cases:prompts.cases.map(c=>({id:c.id,input:modelInput(prompts,c.id)}))};
}
const here=path.dirname(fileURLToPath(import.meta.url));
if(process.argv[1] && import.meta.url===pathToFileURL(process.argv[1]).href){
  const args=process.argv.slice(2),mode=args.shift()??'status';
  if(!['status','plan'].includes(mode)||args.length>1)throw Error('Usage: node evals/runner/os26.mjs status|plan [private-evidence.json]');
  const p=fs.readFileSync(path.join(here,'../os26/prompts.json')),a=fs.readFileSync(path.join(here,'../os26/acceptance.json'));
  const prompts=JSON.parse(p),acceptance=JSON.parse(a),file=args[0];
  const result=assess(prompts,acceptance,file?JSON.parse(fs.readFileSync(file)):null,{promptHash:digest(p),acceptanceHash:digest(a)},file?path.dirname(path.resolve(file)):here);
  console.log(JSON.stringify(mode==='plan'?plan(prompts,result):result,null,2));
}
