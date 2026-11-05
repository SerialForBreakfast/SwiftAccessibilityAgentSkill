import fs from 'node:fs';import {pathToFileURL} from 'node:url';import {compare} from './report.mjs';
export function contrast(rows,control,treatment,release='candidate'){
 if(!['C0','C1','C2','C3'].includes(control)||!['C0','C1','C2','C3'].includes(treatment)||control===treatment)throw Error('Choose distinct C0-C3 conditions');
 const selected=rows.filter(r=>r.release===release&&[control,treatment].includes(r.condition));
 if(!selected.length)throw Error('No matching scores');
 const roots=new Set(selected.map(r=>r.metadata?.skillHash));if(roots.size!==1||roots.has(undefined))throw Error('Contrast requires one frozen skill root');
 const normalized=selected.map(r=>({...r,originalCondition:r.condition,release:r.condition===control?'baseline':'candidate',condition:treatment+'-'+control}));
 return {control,treatment,skillRelease:release,...compare(normalized),interpretation:'Condition effect on the same skill root; not a candidate-release acceptance decision.'};
}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href)console.log(JSON.stringify(contrast(JSON.parse(fs.readFileSync(process.argv[2])),process.argv[3],process.argv[4],process.argv[5]||'candidate'),null,2));
