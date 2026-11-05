import fs from 'node:fs';import path from 'node:path';
import Provider from './provider.mjs';import {repo,settings,fingerprint,hash,verifyBaseline} from './lib.mjs';
const split=process.env.EVAL_SPLIT||'smoke',root=process.env.EVAL_SKILL_ROOT?path.resolve(process.env.EVAL_SKILL_ROOT):repo;
if(!['smoke','development','heldout'].includes(split))throw Error('Invalid split');
const all=JSON.parse(fs.readFileSync(path.join(repo,'evals/scenarios.json'))),scenarios=all.filter(s=>split==='smoke'?['D01','D31'].includes(s.id):s.split===split);
const aliases=(process.env.EVAL_PROVIDERS||'bigdog,comparator').split(',');if(aliases.some(a=>!['bigdog','comparator'].includes(a)))throw Error('Unknown provider');
const repetitions=split==='smoke'?1:3;
const jobs=scenarios.flatMap(s=>s.os.flatMap(os=>aliases.flatMap(alias=>['C0','C1','C2','C3'].flatMap(condition=>Array.from({length:repetitions},(_,repeat)=>({s,os,alias,condition,repeat}))))));
verifyBaseline();const skillHash=fingerprint(root);
const manifest={skillHash,suiteHash:hash(fs.readFileSync(path.join(repo,'evals/scenarios.json'))),gateHash:hash(fs.readFileSync(path.join(repo,'evals/release-gates.json'))),split,repetitions,jobs:jobs.length,maxConcurrency:1,minimumModelRequests:jobs.reduce((n,j)=>n+j.s.turns.length,0),runtime:process.version};
if(!process.argv.includes('--execute')){console.log(JSON.stringify(manifest,null,2));process.exit(0);}
if(process.env.EVAL_ALLOW_NETWORK!=='1')throw Error('Run approval required: EVAL_ALLOW_NETWORK=1');
if(split==='heldout'&&process.env.EVAL_FROZEN_HASH!==skillHash)throw Error('Freeze candidate hash before heldout');
manifest.providers=aliases.map(a=>settings(a).metadata);
const output=process.env.EVAL_OUTPUT;if(!output)throw Error('Set EVAL_OUTPUT to a new private result directory');fs.mkdirSync(output);
fs.writeFileSync(path.join(output,'manifest.json'),JSON.stringify(manifest,null,2));
for(const j of jobs){
 if(fingerprint(root)!==skillHash)throw Error('Skill changed mid-run');
 const provider=new Provider({config:{alias:j.alias,condition:j.condition}});
 const result=await provider.callApi(j.s.turns.at(-1),{vars:{scenario_id:j.s.id,os:j.os}});
 const record={id:[j.alias,j.condition,j.s.id,j.os,j.repeat].join(':'),release:process.env.EVAL_RELEASE||'candidate',provider:j.alias,condition:j.condition,family:j.s.id,os:j.os,repeat:j.repeat,platform:j.s.platform,lane:j.s.lane,question:j.s.turns,turns:result.turns,rubric:j.s.rubric,evidence:j.s.references,inputTokens:result.metadata.inputTokens,focused:j.s.turns.length===1,...result};
 record.suiteHash=manifest.suiteHash; record.gateHash=manifest.gateHash;
 fs.appendFileSync(path.join(output,'records.jsonl'),JSON.stringify(record)+'\n');
 console.log('Completed '+record.id);
}
