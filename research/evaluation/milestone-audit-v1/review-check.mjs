import fs from 'node:fs';import {audit} from './audit.mjs';import {safePreflight} from './guards.mjs';
if(process.argv.length!==2)throw Error('Usage: node review-check.mjs (offline only)');
const manifest=JSON.parse(fs.readFileSync(new URL('../milestone-package-v1/manifest.json',import.meta.url)));
const integrity=safePreflight(manifest);
const findings=integrity.integrityPassed?audit():null;
const reviewBlockers=findings?[...new Set(findings.rows.flatMap(r=>r.findings.filter(f=>f.severity==='revision-required'||f.id==='declared-platform-scope').map(f=>r.id+':'+f.id)))]:['package-integrity-invalid'];
console.log(JSON.stringify({schema:1,integrityPassed:integrity.integrityPassed,integrityErrors:integrity.integrityErrors,authorReviewReady:reviewBlockers.length===0,reviewKind:'author-pre-review-not-independent',reviewBlockers,independentAcceptance:false,liveRunsAuthorized:false,modelCalls:0},null,2));
process.exitCode=reviewBlockers.length||!integrity.integrityPassed?1:0;
