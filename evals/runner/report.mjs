import fs from 'node:fs';
import {pathToFileURL} from 'node:url';
const mean=a=>a.reduce((s,x)=>s+x,0)/a.length;
const median=a=>{const s=[...a].sort((a,b)=>a-b);return s.length%2?s[(s.length-1)/2]:(s[s.length/2-1]+s[s.length/2])/2;};
export function compare(rows) {
  const groups=new Map();
  for(const r of rows) {
    if(!['baseline','candidate'].includes(r.release)||!Number.isFinite(r.quality)||r.quality<0||r.quality>1||!Number.isInteger(r.criticalErrors)||r.criticalErrors<0) throw Error('Invalid scored row');
    const key=JSON.stringify([r.provider,r.condition,r.family,r.os]);
    if(!groups.has(key)) groups.set(key,{baseline:[],candidate:[]});
    const a=groups.get(key)[r.release];if(a.some(x=>x.repeat===r.repeat)) throw Error('Duplicate paired sample');a.push(r);
  }
  if(!groups.size) throw Error('No scores');
  const families=new Map(), regressions=[], tokens={baseline:[],candidate:[]}; let newCritical=0;
  for(const [key,g] of groups) {
    if(g.baseline.length!==3||g.candidate.length!==3||g.baseline.some(r=>!g.candidate.some(c=>c.repeat===r.repeat))) throw Error('Three matching repetitions required: '+key);
    const d=mean(g.candidate.map(r=>r.quality))-mean(g.baseline.map(r=>r.quality));
    const family=g.baseline[0].family;if(!families.has(family))families.set(family,[]);families.get(family).push(d);
    if(d<0)regressions.push({key,delta:d});
    for(const before of g.baseline) {
      const after=g.candidate.find(r=>r.repeat===before.repeat);
      if(before.suiteHash!==after.suiteHash || before.gateHash!==after.gateHash || before.rubricHash!==after.rubricHash || before.gradingEvidenceHash!==after.gradingEvidenceHash) throw Error('Suite or gates changed between paired runs');
      if(JSON.stringify(before.metadata?.provider)!==JSON.stringify(after.metadata?.provider)) throw Error('Provider settings changed between paired runs');
      newCritical+=Math.max(0,after.criticalErrors-before.criticalErrors);
      if(before.focused&&after.focused&&Number.isFinite(before.inputTokens)&&Number.isFinite(after.inputTokens)) {
        tokens.baseline.push(before.inputTokens); tokens.candidate.push(after.inputTokens);
      }
    }
  }
  const deltas=[...families.values()].map(mean);let seed=20261104;const random=()=>{seed=(Math.imul(1664525,seed)+1013904223)>>>0;return seed/4294967296;};
  const boot=Array.from({length:10000},()=>mean(deltas.map(()=>deltas[Math.floor(random()*deltas.length)]))).sort((a,b)=>a-b);
  const interval=[boot[250],boot[9749]],enough=deltas.length>=20;
  const tokenReduction=tokens.baseline.length&&tokens.baseline.length===tokens.candidate.length&&median(tokens.baseline)>0?1-median(tokens.candidate)/median(tokens.baseline):null;
  return {families:deltas.length,qualityDelta:mean(deltas),interval95:interval,newCritical,regressions,nonInferiority:enough&&interval[0]>=-0.02&&newCritical===0,improvement:enough&&interval[0]>0&&newCritical===0,tokenReduction,efficiencyTargetMet:tokenReduction!==null&&tokenReduction>=0.15,status:'Statistical evidence only; package checks, platform review and grading calibration remain required.'};
}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href) console.log(JSON.stringify(compare(JSON.parse(fs.readFileSync(process.argv[2]))),null,2));
