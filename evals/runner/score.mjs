import fs from 'node:fs';import {mergeGrades} from './grading.mjs';
const [mappingPath,gradesPath]=process.argv.slice(2);
if(!mappingPath||!gradesPath)throw Error('Usage: node score.mjs private-mapping.json grades.json');
console.log(JSON.stringify(mergeGrades(JSON.parse(fs.readFileSync(mappingPath)),JSON.parse(fs.readFileSync(gradesPath))),null,2));
