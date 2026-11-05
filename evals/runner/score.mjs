import fs from 'node:fs';
// Merge independently graded, blinded answers with the private mapping.
const [mappingPath,gradesPath]=process.argv.slice(2);
const mapping=JSON.parse(fs.readFileSync(mappingPath)),grades=JSON.parse(fs.readFileSync(gradesPath));
const seen=new Set(),rows=[];
for(const g of grades){
 if(seen.has(g.id))throw Error('Duplicate grading packet');seen.add(g.id);
 const pair=mapping.find(p=>p.id===g.id);if(!pair)throw Error('Unknown grading packet');
 for(const side of ['A','B']){const v=g[side];if(!Number.isFinite(v?.quality)||v.quality<0||v.quality>1||!Number.isInteger(v.criticalErrors)||v.criticalErrors<0||!v.reason||!g.judge)throw Error('Incomplete grade');const r=pair[side];rows.push({...r,quality:v.quality,criticalErrors:v.criticalErrors,gradingReason:v.reason,judge:g.judge});}
}
if(seen.size!==mapping.length)throw Error('Missing grades');
console.log(JSON.stringify(rows,null,2));
