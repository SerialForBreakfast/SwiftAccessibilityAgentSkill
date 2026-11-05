import {validateCatalog} from './os26.mjs';
import {checkSources} from './source-check.mjs';
import {checkRubrics} from './rubric-check.mjs';
import fs from 'node:fs';
import path from 'node:path';
import {repo,verifyBaseline,readReference,fingerprint} from './lib.mjs';
const scenarios=JSON.parse(fs.readFileSync(path.join(repo,'evals/scenarios.json')));
validateCatalog(JSON.parse(fs.readFileSync(path.join(repo,'evals/os26/prompts.json'))),JSON.parse(fs.readFileSync(path.join(repo,'evals/os26/acceptance.json'))));
if(scenarios.length!==60||scenarios.filter(s=>s.split==='development').length!==40||new Set(scenarios.map(s=>s.id)).size!==60)throw Error('Invalid scenario split');
for(const s of scenarios) {
 if(!s.rubric||!s.turns.length)throw Error('Missing rubric or prompt');
 for(const r of s.references) if(s.id!=='D33')readReference(repo,r);
}
for(const name of ['core.json','routes.json','task-presets.json','platform-presets.json']) {
 const a=fs.readFileSync(path.join(repo,'references/manifests',name),'utf8'),b=fs.readFileSync(path.join(repo,'skill/manifests',name),'utf8');
 if(a!==b)throw Error('Manifest mirror drift: '+name);
 const visit=v=>{if(typeof v==='string'&&v.startsWith('references/')&&!fs.existsSync(path.join(repo,v)))throw Error('Broken manifest path: '+v);if(v&&typeof v==='object')Object.values(v).forEach(visit);};visit(JSON.parse(a));
}
for(const p of ['core/reading-content.md','core/media-updates.md','core/source-refresh-2026-11.md','tvos/guidelines/t-011-larger-text.md']) if(fs.readFileSync(path.join(repo,'docs',p),'utf8')!==fs.readFileSync(path.join(repo,'references',p),'utf8'))throw Error('Documentation mirror drift: '+p);
console.log(JSON.stringify({grading:checkRubrics(),sourceAudit:checkSources(),baselineFilesVerified:verifyBaseline(),scenarios:60,development:40,heldout:20,candidateHash:fingerprint(repo),version:fs.readFileSync(path.join(repo,'VERSION'),'utf8').trim()},null,2));
