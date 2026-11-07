import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {transition,median} from './compare.mjs';
const root=fileURLToPath(new URL('../../../',import.meta.url));
const hash=b=>createHash('sha256').update(b).digest('hex');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p)));
const outcomes={met:'pass',meets:'pass',gap:'fail','material-gap':'fail',inconclusive:'inconclusive','not-assessable':'inconclusive'};
function counts(rows){return Object.fromEntries(['gain','regression','preserved','persistent-failure','inconclusive','missing'].map(k=>[k,rows.filter(r=>r.transition===k).length]));}
export function history(){
 const paths=['evals/reports/local-compact-b-20261106/summary.json','evals/reports/skill-0.3.0-dev.1-vs-0.3.0-dev.2-20261106/summary.json','evals/reports/skill-0.3.0-dev.1-vs-0.3.0-dev.2-claude-20261106/summary.json'];
 const [local,agy,claude]=paths.map(read),experiments=[];
 for(const model of Object.keys(local.modelIdentities)){
  const rows=[];for(const prompt of [...new Set(local.rows.filter(r=>r.model===model).map(r=>r.prompt))]){
   const before=local.rows.find(r=>r.model===model&&r.prompt===prompt&&r.condition==='F'),after=local.rows.find(r=>r.model===model&&r.prompt===prompt&&r.condition==='BR');
   const compilerOutcome=v=>v==='typecheck_pass'?'pass':v==='typecheck_failed'?'fail':'inconclusive';
   rows.push({case:prompt,platform:before?.platform??after?.platform,framework:before?.framework??after?.framework,before:before?.core??'missing',after:after?.core??'missing',transition:transition(before?outcomes[before.core]:'missing',after?outcomes[after.core]:'missing'),inputTokenChange:before?.inputTokens>0&&Number.isFinite(after?.inputTokens)?after.inputTokens/before.inputTokens-1:null,compiler:{before:before?.compiler??null,after:after?.compiler??null,transition:transition(compilerOutcome(before?.compiler),compilerOutcome(after?.compiler))},finish:{before:before?.finishReason??null,after:after?.finishReason??null},answerHashes:{before:before?.answerHash??null,after:after?.answerHash??null}});
  }
  experiments.push({id:'local-'+model,modelRevision:local.modelIdentities[model].digest,scope:'Diagnostic small-model historical source review, not frontier optimization target',beforeCondition:'F',afterCondition:'BR',rows,counts:counts(rows),medianInputTokenChange:median(rows.map(r=>r.inputTokenChange).filter(Number.isFinite)),causalLiftQualified:false,qualification:'Exact historical task/harness serialization and independent semantic grading not revalidated here; compiler axis remains separate.'});
 }
 const agyRows=agy.cases.map(c=>({case:c.case,before:c['0.3.0-dev.1'].core,after:c['0.3.0-dev.2'].core,transition:transition(outcomes[c['0.3.0-dev.1'].core],outcomes[c['0.3.0-dev.2'].core])}));
 const claudeRows=Object.entries(claude.cases).map(([id,c])=>({case:id,before:c['0.3.0-dev.1'],after:c['0.3.0-dev.2'],transition:transition(outcomes[c['0.3.0-dev.1']],outcomes[c['0.3.0-dev.2']])}));
 experiments.push({id:'historical-agy-dev1-dev2',modelRevision:agy.models.returned_model_identity,scope:'Historical frontier source-only grades; no native answer checks',rows:agyRows,counts:counts(agyRows),reportedTotalTokenChangePercent:agy.total_token_change_percent,reportedMedianTokenChangePercent:agy.median_token_change_percent,causalLiftQualified:false,qualification:'Inconclusive-to-pass is not fail-to-pass. Raw answers and exact returned model revision are unavailable in this public summary.'});
 experiments.push({id:'historical-claude-dev1-dev2',modelRevision:claude.model,scope:'Historical frontier source-only grades; no native answer checks',rows:claudeRows,counts:counts(claudeRows),reportedTotalTokenChangePercent:claude.total_token_change_percent,reportedMedianTokenChangePercent:claude.median_token_change_percent,causalLiftQualified:false,qualification:'Source grading is preserved, not regraded with operational-1. Full exact matched execution metadata is not reconstructed.'});
 return {schema:1,scope:'Read-only reinterpretation of reported historical transitions; no new answers or grades',inputs:paths.map(p=>({path:p,sha256:hash(fs.readFileSync(path.join(root,p)))})),experiments,pooledScore:null,releaseEligible:false,modelCalls:0,warnings:['Gains/regressions here describe original source grades, not validated native task outcomes.','Do not pool models, harnesses, rubric revisions, conditions or token accounting conventions.','No result for dev.3/dev.4/dev.5 is inferred from earlier snapshots.']};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))console.log(JSON.stringify(history(),null,2));
