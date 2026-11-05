import fs from 'node:fs';import path from 'node:path';
import {repo,hash} from './lib.mjs';import {rubricBundle} from './grading.mjs';
export function checkRubrics(){
 const s=JSON.parse(fs.readFileSync(path.join(repo,'evals/scenarios.json'))),r=rubricBundle(),b=JSON.parse(fs.readFileSync(path.join(repo,'evals/evidence/grading-evidence.json')));
 if(Object.keys(r.cases).length!==s.length)throw Error('Rubric/scenario coverage mismatch');
 if(Math.abs(Object.values(r.dimensions).reduce((n,d)=>n+d.weight,0)-1)>1e-10)throw Error('Weights must sum to one');
 if(b.rubricHash!==hash(fs.readFileSync(path.join(repo,'evals/rubrics.json'))))throw Error('Stale frozen rubric evidence');
 for(const e of b.references)if(hash(e.content)!==e.sha256)throw Error('Evidence integrity failure');
 for(const scenario of s){const c=r.cases[scenario.id];if(!c?.criteria.length||!c.scope)throw Error('Missing case criteria');for(const p of c.referencePaths)if(!b.references.some(e=>e.path===p))throw Error('Missing case evidence');}
 const freeze=JSON.parse(fs.readFileSync(path.join(repo,'evals/evidence/heldout-question-freeze.json')));
 if(hash(JSON.stringify(s.filter(x=>x.split==='heldout').map(({id,turns,os,lane})=>({id,turns,os,lane}))))!==freeze.sha256)throw Error('Heldout questions changed during review');
 return {rubricCases:s.length,evidenceReferences:b.references.length,heldoutQuestionsPreserved:true,status:r.status};
}
