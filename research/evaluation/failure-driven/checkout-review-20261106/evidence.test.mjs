import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const root = path.dirname(fileURLToPath(import.meta.url));
const read = name => fs.readFileSync(path.join(root, name), 'utf8');
const inventory = new Set(fs.readdirSync(root));
function missingLinks(markdown, files) {
  return [...markdown.matchAll(/\]\(([^)]+)\)/g)].map(m => m[1])
    .filter(p => !/^https?:\/\//.test(p) && !p.startsWith('#'))
    .map(p => p.split('#')[0]).filter(p => !files.has(p));
}

test('documentation-only return contains every relative Markdown link target', () => {
  for (const file of inventory) {
    if (file.endsWith('.md')) assert.deepEqual(missingLinks(read(file), inventory), [], file);
  }
});

test('original private packet filename mismatch is detected, not silently accepted', () => {
  assert.deepEqual(missingLinks('[Results](results.json)', new Set(['sanitized-results.json'])), ['results.json']);
  assert.deepEqual(missingLinks('[Results](results.json)', new Set(['results.json'])), []);
});

test('first compile record retains all eight answers, no repairs and four failures', () => {
  const {cases} = JSON.parse(read('results.json'));
  assert.deepEqual(cases.map(c => c.review_id), ['R04', 'R08', 'R09', 'R10', 'R12', 'R13', 'R14', 'R16']);
  assert.deepEqual(cases.filter(c => c.exit_code !== 0).map(c => c.review_id), ['R04', 'R08', 'R09', 'R10']);
  for (const c of cases) {
    assert.equal(c.attempt, 1);
    assert.equal(c.repair_attempts, 0);
    assert.equal(c.unit_tests_run, 0); // Later units never overwrite this first compile record.
    assert.match(c.answer_sha256, /^[a-f0-9]{64}$/);
  }
});

test('expected rejection is not subject success or two failed scenarios', () => {
  const r = JSON.parse(read('unit-results.json'));
  assert.equal(r.adapterStatus, 'passed');
  assert.equal(r.subjectOutcome, 'failure');
  assert.equal(r.passedTests, 7);
  assert.equal(r.failedTests, 1);
  assert.equal(r.skippedTests, 0);
  assert.equal(r.execution.executedTestIds.length, 8);
  assert.deepEqual(r.execution.failedTestIds, ['CheckoutAnswerTests/testR16PreservesButtonTypography']);
  assert.equal(r.execution.exitCode, 65);
  assert.equal(r.execution.build, 'passed');
  assert.equal(r.repairAttempts, 0);
});
