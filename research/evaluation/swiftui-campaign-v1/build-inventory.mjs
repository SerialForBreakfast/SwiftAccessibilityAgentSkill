import fs from 'node:fs';import {hash} from '../../../code-examples/tools/contracts.mjs';
const root='references/swiftui/guidelines/',out='research/evaluation/swiftui-campaign-v1/';
const documents=[];
for(const name of fs.readdirSync(root).filter(n=>/^g-\d{3}-.*\.md$/.test(n)).sort()){
 const path=root+name,bytes=fs.readFileSync(path),lines=bytes.toString().split('\n'),id=name.slice(0,5).toUpperCase();let section='',subsection='';const clauses=[];let rule='';
 for(let i=0;i<lines.length;i++){const line=lines[i];if(line.startsWith('## ')){section=line.slice(3);subsection='';continue;}if(line.startsWith('### ')){subsection=line.slice(4);continue;}
 if(section==='Rule'&&line.trim())rule+=(rule?' ':'')+line.trim();
 if(['How To Implement','How To Test',"Do / Don't"].includes(section)&&line.startsWith('- '))clauses.push({id:id+'-L'+(i+1),line:i+1,section,subsection,text:line.slice(2)});
 else if((section.startsWith('Interaction Refinement')||section.startsWith('OS 27 Media Update'))&&line.trim()&&!line.startsWith('Sources:'))clauses.push({id:id+'-P'+(i+1),line:i+1,section,subsection,text:line.trim()});
 }
 documents.push({id,path,sha256:hash(bytes),rule,clauses,sourceURLs:[...new Set(bytes.toString().match(/https:\/\/(?:developer|support)\.apple\.com\/[^\s)]+/g)??[])]});
}
fs.writeFileSync(out+'inventory.json',JSON.stringify({schema:1,scope:'All15 SwiftUI guidelines; implementation/refinement, test, and do/dont requirements. Frozen source hashes; platform availability evaluated separately.',documents},null,2)+'\n');console.log({guidelines:documents.length,clauses:documents.reduce((n,d)=>n+d.clauses.length,0)});
