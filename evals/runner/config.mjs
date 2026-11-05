import fs from 'node:fs';
import path from 'node:path';
import {repo} from './lib.mjs';
const split=process.env.EVAL_SPLIT||'development';
if(!['development','heldout','smoke'].includes(split)) throw Error('Invalid EVAL_SPLIT');
const scenarios=JSON.parse(fs.readFileSync(path.join(repo,'evals/scenarios.json')));
export default {
 description:'Evidence-backed skill evaluation; quality grading is separate from protocol checks',
 prompts:['{{user_prompt}}'],
 providers:['bigdog','comparator'].flatMap(alias=>['C0','C1','C2','C3'].map(condition=>({id:'file://'+path.join(repo,'evals/runner/provider.mjs'),config:{alias,condition},label:`${alias}-${condition}`}))),
 tests:scenarios.filter(s=>split==='smoke'?['D01','D31'].includes(s.id):s.split===split).flatMap(s=>s.os.map(os=>({description:s.id+"-"+os,vars:{scenario_id:s.id,os,user_prompt:s.turns.at(-1)},metadata:{family:s.id,platform:s.platform,os,lane:s.lane},assert:[{type:'javascript',value:'output.trim().length > 0',metric:'Nonempty'}]}))),
 evaluateOptions:{maxConcurrency:1,repeat:split==='smoke'?1:3}
};
