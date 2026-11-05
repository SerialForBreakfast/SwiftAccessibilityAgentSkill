// Structural integrity only; these tests do not execute Swift or establish oracle results.
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
const root = new URL('../os26/fixtures/', import.meta.url);
const read = p => fs.readFileSync(new URL(p, root), 'utf8');
const manifest = JSON.parse(read('manifest.json'));
const prompts = JSON.parse(fs.readFileSync(new URL('../os26/prompts.json', import.meta.url)));
const digest = s => crypto.createHash('sha256').update(s).digest('hex');
test('all six draft cases have pinned candidate and two distinct isolated variants', () => {
    assert.deepEqual(manifest.cases.map(c => c.id), prompts.cases.map(c => c.id));
    assert.equal(manifest.status, 'unvalidated');
    for (const c of manifest.cases) {
        assert.equal(c.mutations.length, 2);
        const variants = [c.candidate, ...c.mutations];
        assert.equal(new Set(variants.map(v => v.sha256)).size, 3);
        for (const v of variants) {
            assert(!v.path.includes('..') && !v.path.startsWith('/'));
            assert.equal(digest(read(v.path)), v.sha256);
            assert.equal(v.observed, 'not_run');
            assert(read(v.path).includes('PATCH BEGIN ' + c.id));
        }
        assert.equal(c.candidate.expected, 'pass');
        for (const v of c.mutations) {
            assert.equal(v.expected, 'fail');
            assert(v.path.startsWith('Mutations/' + c.id + '/'));
        }
    }
});
test('host and test preparation remain separate from promotion receipts', () => {
    assert(read('Host/FixtureApp.swift').includes('event-log'));
    assert(read('Tests/OS26FixturesTests/UIKitTests.swift').includes('testReconfigurationWithoutPrepareForReuse'));
    assert(read('README.md').includes('not gold-ready'));
    assert.equal(manifest.cases.some(c => 'checks' in c), false);
});
