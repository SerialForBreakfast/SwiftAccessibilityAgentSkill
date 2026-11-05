import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import {remaining} from './ollama-next-remaining.mjs';
import {plan} from './ollama-next-questions.mjs';
const p={jobs:plan(JSON.parse(fs.readFileSync(new URL('../scenarios.json',import.meta.url))))};
const r=p.jobs.slice(0,20).map(j=>({case:`${j.scenario.id}-${j.scenario.os[0]}-2048-${j.arm}`}));
const status={state:'stopped',active:'D24-26-2048-C3-explicit',calls:21},attempted=new Set([...r.map(r=>r.case),status.active]);
test('successor excludes completed and failed cells',()=>{const a=remaining(p,r,status,attempted);assert.equal(a.length,3);assert.ok(a.every(j=>j.scenario.id==='D30'));});
test('successor refuses uncertain or already attempted cells',()=>{assert.throws(()=>remaining(p,r,{...status,calls:22},attempted));assert.throws(()=>remaining(p,r,status,new Set([...attempted,'D30-26-2048-C0'])));});
