import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import {route} from './route.mjs';
const base='research/evaluation/failure-driven/candidates/0.3.0-dev.5/';
const hash=x=>createHash('sha256').update(x).digest('hex');
const manifest=JSON.parse(fs.readFileSync(base+'candidate.json'));
const catalog=JSON.parse(fs.readFileSync(base+'routes.json')).routes;
const cases=JSON.parse(fs.readFileSync(base+'evaluation/controller.json')).cases;
for(const c of cases)test(c.id+' preserves separate subject, rubric and unrun status',()=>{
 const text=fs.readFileSync(c.subject.path,'utf8');
 assert.equal(hash(text),c.subject.sha256);
 assert.ok(text.length>100);
 assert.ok(!/expectedRoute|acceptedAlternatives|references\/tasks|rubric|controller\.json/.test(text));
 assert.ok(c.controller.criteria.length>=3);
 assert.ok(c.controller.acceptedAlternatives.length>=2);
 assert.equal(c.status,'draft-gold-candidate');
 assert.equal(c.cohort,'development-not-holdout');
 assert.equal(c.outputsAvailable,false);
 assert.deepEqual(c.attempts,[]);
});
for(const row of catalog)test([row.platform,row.framework,row.topic].join('/')+' complete matrix and real reads',()=>{
 const matches=cases.filter(c=>c.platform===row.platform&&c.framework===row.framework&&c.topic===row.topic&&c.controller.note);
 assert.equal(matches.length,1);
 const c=matches[0],r=route(row);
 assert.equal(c.controller.expectedRoute,row.guideline);
 assert.equal(c.controller.sourceGap,!row.guideline);
 if(!row.guideline){assert.equal(r.status,'requires-primary-source');assert.equal(r.deliveredBytes,0);assert.deepEqual(r.trace,[]);return;}
 assert.equal(r.status,'selected');assert.equal(r.paths.length,2);
 assert.ok(r.paths.includes(base+row.note));assert.ok(r.paths.includes(row.guideline));
 for(const t of r.trace)assert.equal(hash(fs.readFileSync(t.path)),t.sha256);
 for(const key of ['exampleSource','exampleManifest'])if(row[key])assert.ok(fs.existsSync(row[key]));
 assert.ok(!r.paths.some(p=>p.includes('/evaluation/subjects/')||p.endsWith('controller.json')));
});
test('six explicit lanes, eight related topics and twelve controls, not sixty independent families',()=>{
 assert.equal(catalog.length,48);assert.equal(cases.length,60);
 assert.equal(new Set(cases.map(c=>c.id)).size,60);
 assert.equal(new Set(catalog.map(r=>r.platform+'/'+r.framework)).size,6);
 assert.equal(new Set(catalog.map(r=>r.topic)).size,8);
 assert.equal(cases.filter(c=>!c.controller.note).length,12);
 assert.equal(catalog.filter(r=>!r.guideline).length,3);
});
test('ownership, unsupported target and budget fail closed',()=>{
 assert.equal(route({framework:'mixed',platform:'iOS',topic:'actions'}).status,'needs-owner');
 for(const platform of ['watchOS','visionOS'])assert.equal(route({platform,framework:'SwiftUI',topic:'text'}).status,'unsupported');
 const r=route({platform:'iOS',framework:'UIKit',topic:'state',maxBytes:1});
 assert.equal(r.status,'budget-exceeded');assert.deepEqual(r.documents,[]);assert.deepEqual(r.trace,[]);
});
test('candidate pins actual source and has no release or evaluation authority',()=>{
 assert.equal(hash(fs.readFileSync(manifest.subject.path)),manifest.subject.sha256);
 assert.equal(hash(fs.readFileSync(base+'routes.json')),manifest.catalogSha256);
 assert.equal(hash(fs.readFileSync(base+'evaluation/controller.json')),manifest.controllerSha256);
 for(const p of [...manifest.assets,...manifest.evidencePins])assert.equal(hash(fs.readFileSync(p.source??p.path)),p.sha256);
 assert.equal(manifest.modelCalls,0);assert.equal(manifest.independentlyReviewed,0);
 assert.equal(manifest.releaseEligible,false);assert.ok(!fs.existsSync(base+'SKILL.md'));
});
