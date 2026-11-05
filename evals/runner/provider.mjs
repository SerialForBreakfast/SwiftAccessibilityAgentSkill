import fs from 'node:fs';
import path from 'node:path';
import {repo,evaluate,settings,verifyBaseline,fingerprint} from './lib.mjs';
import {protocol} from './protocol.mjs';
export default class SkillProvider {
  constructor(options) {this.config=options.config;}
  id() {return `skill:${this.config.alias}:${this.config.condition}`;}
  async callApi(prompt, context) {
    if(process.env.EVAL_ALLOW_NETWORK!=='1') throw Error('Set EVAL_ALLOW_NETWORK=1 after approving model runs');
    const scenarios=JSON.parse(fs.readFileSync(path.join(repo,'evals/scenarios.json')));
    const scenario=scenarios.find(s=>s.id===context.vars.scenario_id);
    if(!scenario) throw Error('Unknown scenario');
    const root=process.env.EVAL_SKILL_ROOT?path.resolve(process.env.EVAL_SKILL_ROOT):repo;
    verifyBaseline();
    if(scenario.split==='heldout' && process.env.EVAL_FROZEN_HASH!==fingerprint(root)) throw Error('Held-out run requires matching EVAL_FROZEN_HASH');
    const selected={...scenario,os:[context.vars.os],turns:scenario.turns.map((t,i)=>i===0&&scenario.references.length?t+'\nDeployment context: '+scenario.platform+' OS version '+context.vars.os+'. Clarify platform if needed.':t)};
    const result=await evaluate({root,condition:this.config.condition,scenario:selected,config:settings(this.config.alias)});
    result.metadata.protocol=protocol(result,fs.readFileSync(path.join(root,'VERSION'),'utf8').trim());
    return result;
  }
}
