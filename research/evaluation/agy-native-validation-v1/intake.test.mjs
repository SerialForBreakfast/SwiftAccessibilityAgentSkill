import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import {hash} from '../../../code-examples/tools/contracts.mjs';
const base='research/evaluation/agy-native-validation-v1/',p=JSON.parse(fs.readFileSync(base+'expected-cells.json'));
test('intake pins14 AGY cells without enabling inference or Claude',()=>{assert.equal(hash(fs.readFileSync(p.proposal.path)),p.proposal.sha256);assert.equal(p.cells.length,14);assert.equal(new Set(p.cells.map(c=>c.id)).size,14);assert.ok(p.cells.every(c=>c.model==='gemini-3.8-flash-low'));assert.equal(p.claudeAllowed,false);assert.equal(p.modelCallsAllowed,0);});
test('each known UIKit task retains two versions and identical supplied inputs',()=>{
 const catalogs=['evals/os26/prompts.json','evals/os26/expansion-1/prompts.json'].flatMap(f=>JSON.parse(fs.readFileSync(f)).cases);
 for(const id of ['GP26-01','GP26-02','GP26-03','GP26-07','GP26-08','GP26-09','GP26-10']){const cells=p.cells.filter(c=>c.case===id);assert.equal(cells.length,2);assert.deepEqual(cells.map(c=>c.skill_version).sort(),['0.3.0-dev.1','0.3.0-dev.2']);assert.equal(cells[0].user_sha256,cells[1].user_sha256);assert.equal(cells[0].reference_sha256,cells[1].reference_sha256);const c=catalogs.find(c=>c.id===id);assert.equal(c.framework,'UIKit');assert.equal(hash(c.prompt),cells[0].user_sha256);}
});
