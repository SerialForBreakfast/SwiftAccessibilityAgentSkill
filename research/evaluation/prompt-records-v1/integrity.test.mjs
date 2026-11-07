import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {hash} from '../../../code-examples/tools/contracts.mjs';
const root=fileURLToPath(new URL('../../../',import.meta.url));
const index=JSON.parse(fs.readFileSync(new URL('./platform-prompts.json',import.meta.url)));
test('all question files in the original indexed packages appear exactly once',()=>{
  const folders=[...new Set(index.cases.map(c=>path.dirname(c.subject.path)))];
  const paths=folders.flatMap(relative=>{
    if(!fs.existsSync(path.join(root,relative)))return [];
    return fs.readdirSync(path.join(root,relative)).filter(n=>n.endsWith('.prompt.md')).map(n=>relative+'/'+n);
  });
  assert.deepEqual(index.cases.map(c=>c.subject.path).sort(),paths.sort());
  assert.equal(new Set(index.cases.map(c=>c.id)).size,index.cases.length);
});
test('question bytes and separate controller rubric hashes match',()=>{
  for(const c of index.cases){
    const bytes=fs.readFileSync(path.join(root,c.subject.path));
    assert.equal(c.subject.text,bytes.toString('utf8'));
    assert.equal(c.subject.sha256,hash(bytes));
    assert.equal(c.analysis.sha256,hash(fs.readFileSync(path.join(root,c.analysis.path))));
    assert.ok(fs.existsSync(path.join(root,c.nativeManifest)));
  }
});
test('drafts do not masquerade as executed answers or complete captures',()=>{
  for(const c of index.cases){
    assert.equal(c.lifecycle,'draft-not-run');
    assert.equal(c.outputs.status,'not-run');assert.deepEqual(c.outputs.attempts,[]);
    assert.equal(c.analysis.answerAnalysis,null);
    assert.equal(c.additionalModelInputs.status,'not-assembled');
    assert.equal(c.authoringTranscript.status,'not-exported');
  }
});
