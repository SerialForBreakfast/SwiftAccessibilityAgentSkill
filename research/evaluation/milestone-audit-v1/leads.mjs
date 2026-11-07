// Existing evidence leads for review; never supplied to subject payloads.
import fs from 'node:fs';import {audit,hash} from './audit.mjs';import {collectReceipts} from '../assertion-bindings-v1/build.mjs';import {receiptIssues} from '../local-qualification-v1/audit.mjs';
const declarationPath='research/evaluation/swiftui-campaign-v1/api-declarations.json';
export function leads(){
 const d=JSON.parse(fs.readFileSync(declarationPath)),receipts=collectReceipts();
 const patterns={state:/func accessibilityValue/,text:/dynamicTypeSize|ScaledMetric/,lifecycle:/accessibilityFocused|AccessibilityFocusState/,actions:/func accessibilityAction/,structure:/func accessibilityElement/};
 const rows=audit().rows.filter(r=>r.findings.some(f=>f.id==='declared-platform-scope')).map(c=>{
  const mp='code-examples/swiftui/'+({iOS:'ios',macOS:'macos',tvOS:'tvos'}[c.platform])+'-v1/manifest.json';const b=fs.readFileSync(mp),m=JSON.parse(b);const folder=mp.slice(0,-'/manifest.json'.length);const pins=m.files.map(f=>({path:folder+'/'+f.path,sha256:f.sha256}));const good=pins.every(p=>hash(fs.readFileSync(p.path))===p.sha256);
  const check=m.checks.find(c=>c.lane==='compile'&&c.expected==='success');const found=receipts.find(r=>!receiptIssues(m,hash(b),check,r.attempt,good).length);if(!found)throw Error('Missing matched platform compile receipt');
  return {id:c.id,platform:c.platform,topic:c.topic,sourceScopeIssue:c.references.filter(r=>r.outOfDeclaredScope).map(r=>r.path),manifest:{path:mp,sha256:hash(b),sourcePins:pins,limitations:m.limitations},compile:{index:found.path,sha256:found.sha256,attempt:found.attempt.attempt,environment:found.attempt.environment},declarationLeads:patterns[c.topic]?d.records.filter(r=>r.platform===c.platform).flatMap(r=>r.matches.filter(m=>patterns[c.topic].test(m.declaration)).slice(0,2).map(m=>({interface:r.interface,interfaceSha256:r.sha256,line:m.line,preceding:m.preceding,declaration:m.declaration}))):[],reviewStatus:'lead-only-not-source-applicability-approval',limit:'Existing composition compilation is not proof every guideline claim or extracted declaration is used, nor rendered semantics. Raw excerpt context can omit enclosing annotations; do not infer exact introduction boundaries.'};
 });
 return {schema:1,declarationCatalog:{path:declarationPath,sha256:hash(fs.readFileSync(declarationPath))},rows,independentlyAccepted:0,modelCalls:0,newNativeRuns:0};
}
if(process.argv[1]?.endsWith('/leads.mjs'))console.log(JSON.stringify(leads(),null,2));
