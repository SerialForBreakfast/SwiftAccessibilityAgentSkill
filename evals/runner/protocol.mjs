export function protocol(result, version) {
 const {condition,trace}=result.metadata, text=result.turns.join('\n');
 if(condition==='C0')return {applicable:false};
 const names=new Set(trace.map(r=>r.path.split('/').at(-1)));
 const routes=[...text.matchAll(/^ROUTING:\s*\[([^\]]*)\]/gm)].flatMap(m=>m[1].split(',').map(x=>x.trim().split(':').at(-1)));
 return {applicable:true,identityFirst:result.turns[0].includes(`Swift Accessibility Agent (v${version})`),identityRepeated:result.turns.slice(1).some(t=>t.includes(`Swift Accessibility Agent (v${version})`)),unreadRoutes:routes.filter(n=>!names.has(n)),routingWhenRead:trace.length===0||routes.length>0,sourceFooterWhenRead:trace.length===0||/^Sources:/m.test(text)};
}
