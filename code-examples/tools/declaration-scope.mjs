// Bounded header-scope scan, not a C preprocessor or complete Objective-C parser.
export function enclosingObjCScope(lines, declarationLine) {
  const clean = lines.join('\n').replace(/\/\*[\s\S]*?\*\//g, s => s.replace(/[^\n]/g,' '))
    .split('\n').map(s => s.replace(/\/\/.*$/, ''));
  let enclosing = null;
  for (let i = 0; i < declarationLine; i++) {
    if (/^\s*@end\b/.test(clean[i] ?? '')) enclosing = null;
    else if (/^\s*@(?:interface|protocol)\s+\w/.test(clean[i] ?? '') && !clean[i].includes(';'))
      enclosing = {line:i+1, context:lines.slice(Math.max(0,i-4),i+2)};
  }
  return enclosing;
}
