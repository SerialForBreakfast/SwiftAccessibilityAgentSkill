import fs from 'node:fs';
const base='research/evaluation/rubric-closure-v1/',d=JSON.parse(fs.readFileSync(base+'rubrics.json'));
let text='# Operational rubric review\n\nController-only author revision. Original subject files and rubrics remain unchanged.\nThese are grading specifications, not scored model answers or independent acceptance.\n\n';
for(const r of d.rows){text+='## '+r.id+'\n\nAccepted alternatives:\n\n'+r.acceptedAlternatives.map(a=>'- '+a).join('\n')+'\n\n';for(const c of r.criteria){text+='### Criterion '+(c.index+1)+'\n\n'+c.originalText+'\n\n- Pass: '+c.pass+'\n- Gap: '+c.fail+'\n- Insufficient evidence: '+c.missing+'\n- Review channels: '+c.channels.join(', ')+'.\n\n';}text+='Source/policy anchors: '+r.sources.map(s=>'['+s.path.split('/').at(-1)+':'+s.line+'](../../../'+s.path+'#L'+s.line+')').join(', ')+'.\n\n';}
fs.writeFileSync(base+'REVIEW.md',text.trimEnd()+'\n');
