"""Reconcile existing frozen receipts. No network, native execution or model calls."""
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

D = Path(__file__).resolve().parent
R = D.parents[2]
E = R / 'evals/results'
Q = R / 'evals/qualification-56'
M = E / 'mutation-grade-calibration/trial1'
load = lambda p: json.loads(p.read_bytes())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

# Short descriptions of the *executed* control; not gold-answer prescriptions.
controls = {
 'C0a2c': ('Drain obsolete observer work after restart with a changed preference; a mere active-observer check refreshes the screen.', 'Replace the integer observation generation with a UUID.'),
 'C777d': ('Press ordinary Save and verify it does not dispatch Open. This is narrower than the optional shortcut contract.', 'Use a UUID revision for the action registration.'),
 'testLiveEdit': ('Edit the native field directly before the old validation reply; omission of the snapshot guard admits the obsolete reply.', 'Compare each captured field with its live native text instead of rebuilding the snapshot.'),
 'C4840': ('Deliver the retained dismissal after replacement and duplicate the current completion. Looking up the latest owner consumes the wrong presentation.', 'Invalidate a captured lifetime object instead of comparing UUIDs.'),
 'C4ec9': ('Missing item must differ from an inspected item without options. Mapping a nil item to absent fails.', 'Resolve the optional native option first, then write selection once. This alternative varies selection wiring, not state classification.'),
 'C5d12': ('Select a known caption and inspect native legible selection. A local-only update cannot pass.', 'Resolve the optional choice before a single item.select call.'),
 'C2865': ('Exercise selection on the playing item; omit the native write and the legible option does not change.', 'Use one native write after resolving the optional option.'),
 'C7d8c': ('Rebind A to another native button B, press both, then stop. Without the registration check the old control reaches the new handler.', 'Use a UUID for binding ownership.'),
 'C7766': ('Press retired and current native buttons across rebind and teardown. Removing the registration check admits stale dispatch.', 'Use a UUID rather than an integer binding revision.'),
 'C7cc5': ('Seed a selected track, request description for a language with only ordinary audio; ignoring the description flag changes selection.', 'Filter by the entire eligibility predicate, then take first.'),
 'C852a': ('Refresh with the same records, select B, then fire the old A button. Removing the generation check changes B.', 'Use UUID generations instead of an incrementing counter.'),
 'testSurvivingOrigin': ('After closing clears visible state, resolve a still-eligible origin. Using the cleared visible item wrongly chooses fallback. Not a test of SwiftUI modifier attachment.', 'Capture the origin in a consumable resolver closure.'),
 'C9c45': ('Inspect no item and then a loaded item without a group. Returning absent in both cases fails.', 'Switch on the optional item; inspect returned enum cases without requiring payload equality.'),
 'testAttachedRefusal': ('Keep the original attached but ineligible; ignoring acceptsFirstResponder misses the fallback.', 'Search ordered primary/fallback candidates with the eligibility predicate.'),
 'Cc04c': ('Invoke the older media selection after ownership changes; a missing ownership check permits stale selection.', 'Resolve the choice and Off into an optional, then make one native write.'),
 'Cc6b2': ('Reload on the same item; a superseded picker request must not apply its choice.', 'Resolve choice and Off before the common native write.'),
 'Cf483': ('Fire old picker ownership against a replacement item and inspect the actual selection, not a menu ID.', 'One item write after resolving choice or Off.'),
 'testPickerWritesPlayerItem': ('Choose a track and read the actual player-item selection. Removing the native write fails.', 'Use a single native write for both the option and Off. Not proof of every load-state transition.'),
 'Cd76c': ('Identify ordinary and tagged fixtures independently using native metadata and compare inspector output. Locale alone misclassifies audio.', 'Build the tagged native option set first, then map membership.'),
 'Cf28c': ('Compare inspector flags against known native ordinary/tagged options. Using locale as the description flag fails.', 'Precompute tagged options and check membership during mapping.'),
}
actions = {}
def group(keys, owner, action):
    for k in keys.split(): actions[k] = (owner, action)
group('0a2c','Skill','Require the queued stale event to produce a different visible result if the guard is removed; otherwise deduplication masks it.')
group('3f81','Both','Use AppKit getter/setter and installed handler APIs. Add a starter-compatible shortcut test; the ordinary Save check alone is insufficient.')
group('4099 db6a','Both','Drive a field edit without the cancel helper; distinguish ignoring stale output from clearing busy and permitting the next submit. Bind the original live-edit fixture in the submitted-proof grader.')
group('4840 da78 9062','Both','Bind dismissal to the installed presentation. Retain A, open B, deliver A late and B twice; distinguish request, completion and reentrant restoration. Do not credit a helper passed the correct ticket by the test.')
group('4ec9 d4bd dc1e','Both','Require evidence for the playing item as well as distinct load states. Supply a working media fixture and separate state and selection scores; an absent fixture must not silently pass.')
group('5d12 6d2d','Both','Trace a real legible selection, preserve audio and distinguish unlisted from Off. Make the native group/option fixture available under the supplied starter interface.')
group('6bfe','Skill','Check current window membership as well as eligibility before restoring; a weak responder can still belong to another window. Accept a design answer here.')
group('7622 7766 7d8c a00e','Skill','Retain an installed old control or callback, rebind, then deliver old and current actions before and after teardown. Re-pressing the same updated button can mask the defect.')
group('7cc5','Both','Require an actually selected option and a language that matches an ordinary track. Reject language-mismatch and nil-to-nil proofs; accept any independently identified equivalent fixture.')
group('852a a12b','Grader','Keep record IDs across refresh and seed a nonempty current selection. Reconcile the exact trial proof before changing guidance: sibling questions use one shared contract.')
group('9c45','Both','Keep rc.2 case-matching guidance; test compile validity separately from behavior. Equality is valid if all payloads genuinely support it.')
group('be25','Grader','Accept either an eligibility predicate or an attached responder that refuses the request. Removing the responder is not the same contrast.')
group('c04c c6b2 f483','Both','Probe both item identity and request generation. Fire the old Off after replacement or same-item reload, then a current choice. Assert the native selection on both paths.')
group('d76c f28c','Grader','Require an independent native tag or known track identity. Splitting inspector output by its own Boolean can pass even when the labels are swapped.')
group('d82c','Skill','Keep the hosted editable field reachable; remove only duplicate wrapper semantics. rc.2 already corrects the advice. Do not infer VoiceOver reachability from a property or compile check.')
group('ddf8','Both','Attach the shortcut to a reachable owner without swallowing the ordinary buttons. A retained Delete must check registration and current permission. Grade ownership separately from assistive navigation.')

def main():
    board = E/'1507-grade/final-review/matched-board.json'
    verdicts = M/'verdicts.json'
    panel = {r['id']:r for r in load(Q/'board.json')['questions']}
    with (Q/'source-calibration.tsv').open() as f:
        source = {x['prefix']:x for x in csv.DictReader(f,delimiter='\t')}
    cohort = [r for r in load(board) if r['vsRelease'] in ('regression','persistent failure')]
    assert Counter(r['vsRelease'] for r in cohort)=={'regression':2,'persistent failure':27}
    assert set(actions)=={r['id'][2:6] for r in cohort}
    rows=[]; counts=Counter(); reasons=Counter()
    for r in cohort:
        i=r['id'];k=i[2:6];q=panel[i]; qualified=[c for c in q['controls'] if c['qualified']]
        assert q['questionSHA256'].startswith(i[2:])
        if qualified:
            c,=qualified; method=c['methodPrefix'][4:]; scope='native'
            assert c['verdicts']=={'Reference':'passed','Alternative':'passed','Mutant':'caught at witness'}
            test,alt=controls[method]
        elif 'priorControl' in q:
            c=q['priorControl']; method=c['method']; test,alt=controls[method];scope='prior native'
            assert set(c['receiptHashes'])=={'positive','alternative','mutant'}
        else:
            c=source[k];method='source contrast';test=c['mutant']+' Rejected: '+c['rejection'];alt=c['alternative'];scope='source only'
        proofs={}
        for cell in load(verdicts):
            if cell['id']!=i:continue
            if cell['verdict']=='no-control':
                assert not qualified
                continue
            assert cell['trial']==1 and cell['arm'] not in proofs
            for var,status in cell['statuses'].items():
                if status is None:continue
                folder=M/(cell['key']+'.'+var); receipt=load(folder/'proof.json')
                assert receipt['status']==status and sha(folder/'proof.log')==receipt['log']
            proofs[cell['arm']]={'verdict':cell['verdict'],'statuses':cell['statuses'],'reason':cell['reason']}
        assert len(proofs)==(3 if qualified else 0)
        if proofs:
            counts[proofs['signal-v6']['verdict']]+=1; reasons[proofs['signal-v6']['reason']]+=1
        rows.append(dict(id=i,family=r['family'],platform=q['platform'],framework=q['framework'],transition=r['vsRelease'],method=method,scope=scope,witness=test,alternative=alt,control=c,earlierControls=q['controls'],trial1=proofs,owner=actions[k][0],nextAction=actions[k][1]))
    inputs={str(p.relative_to(R)):sha(p) for p in [board,Q/'board.json',Q/'source-calibration.tsv',verdicts]}
    (D/'audit.json').write_text(json.dumps(dict(inputs=inputs,rows=rows),indent=2)+'\n')
    lines=['# V6 failure audit: 29 matched development questions','',
    'Selection: every persistent whole-question failure and regression against 0.2.2 in the final frozen board. Reconciliation of existing runs, not new model inference, native execution or regrading. Trial 1 is a submitted-proof sample, not the three-trial whole-question majority. Shared methods are counted once per question here, not as independent discoveries.','',
    '## What the checks establish','',
    'Native = the repository test accepted its reference and alternative and rejected the named mutant at the intended witness. Prior native = earlier qualified test, not wired into trial-1 submitted-proof calibration. Source only = accepted and rejected reasoning, not executed behavior. “Not runnable” and “not replayed” are not answer failures. Grader/skill assignments are proposed work, not changed instructions.','',
    '| Question | Platform | Repository test and defect it catches | Valid alternative (evidence level at left) | Submitted v6 proof, trial 1 | Next change |','|---|---|---|---|---|---|']
    for x in rows:
        proof=x['trial1'].get('signal-v6');out=(proof['verdict']+': '+proof['reason']) if proof else 'Not replayed'
        lines.append('| '+' | '.join([x['id']+' ('+x['transition']+')',x['platform']+' '+x['framework'],x['scope']+': '+x['method']+'. '+x['witness'],x['alternative'],out,x['owner']+': '+x['nextAction']]).replace('\n',' ')+' |')
    lines+=['','## Read the evidence','', 'See [the machine-readable ledger](audit.json) for intake hashes, all three arms’ submitted-proof verdicts, per-variant statuses, first unsuccessful controls and receipt identifiers. Source-only alternatives are proposals validated by rubric contrast, not native passes. On the evidence host run `python3 -B evals/qualification-56/report.py --check` to revalidate control source and native logs, then `python3 -B research/evaluation/v6-failure-audit/build.py` to verify submitted-proof receipts and reproduce both tables. The historical model answers are private and are not included.','',
    'The Mac search source contrast is supplemented by [rc.2 fixture checks](../../../evals/rc2/README.md): visible editable field and hidden decorative sibling are accepted; hiding the representable is rejected by fixture wiring inspection, not a runtime accessibility-tree assertion. The media regression also has independent rc.2 compile and empty-item checks. Neither rc.2 check retroactively grades a v6 answer.']
    (D/'README.md').write_text('\n'.join(lines)+'\n')
    print(counts, reasons, Counter(x['scope'] for x in rows),Counter(x['owner'] for x in rows))
if __name__=='__main__':main()
