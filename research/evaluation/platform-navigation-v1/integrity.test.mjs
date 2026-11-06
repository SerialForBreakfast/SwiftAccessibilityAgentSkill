import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {fileURLToPath} from 'node:url';
import {hash} from '../../../code-examples/tools/contracts.mjs';
const root=fileURLToPath(new URL('../../../',import.meta.url));
const read=p=>fs.readFileSync(root+p);
const report=JSON.parse(read('research/evaluation/platform-navigation-v1/results-index.json'));
for(const folder of ['macos-navigation-v1','tvos-results-v1'])test(folder+' current checks have matching receipts',()=>{
 const bytes=read('code-examples/platforms/'+folder+'/manifest.json'),m=JSON.parse(bytes);
 for(const c of m.checks){const rs=report.attempts.filter(r=>r.manifestHash===hash(bytes)&&r.checkId===c.id&&r.status==='passed');assert.ok(rs.length>=1,c.id);for(const r of rs){assert.equal(r.observed,c.expected);assert.deepEqual([...r.execution.executedTestIds].sort(),[...c.testIds].sort());assert.deepEqual([...r.execution.failedTestIds].sort(),[...c.failureIds].sort());assert.equal(r.environment.platform,m.platform);if(c.lane==='unit')assert.equal(Number(r.environment.runtimeVersion.split('.')[0]),m.runtimeMajor);}}
});
test('source pins exclude filesystem metadata and retain first failure',()=>{
 assert.ok(report.pins.length>0);for(const p of report.pins){assert.ok(!p.path.split('/').some(x=>x.startsWith('.')));assert.equal(hash(read(p.path)),p.sha256);}
 assert.ok(report.attempts.some(r=>r.status==='failed'&&r.execution.failedTestIds.includes('DesktopNavigationTests/testIncomingDisabledLinkCleared')));
 assert.equal(report.attempts.filter(r=>r.checkId==='repeatedanimation').length,2,'both actual executions remain visible');
});
