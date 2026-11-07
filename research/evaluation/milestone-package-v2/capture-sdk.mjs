// Read installed public declarations only. No compilation or example execution.
import fs from 'node:fs';import {execFileSync} from 'node:child_process';import {createHash} from 'node:crypto';
const hash=b=>createHash('sha256').update(b).digest('hex');
const specs=[
 {id:'macos-value',platform:'macOS',module:'SwiftUI',needle:'nonisolated public func accessibilityValue(_ valueDescription: SwiftUICore.Text)',api:'View.accessibilityValue(Text)',version:'11.0'},
 {id:'macos-dynamic-size',platform:'macOS',module:'SwiftUICore',needle:'public var dynamicTypeSize:',api:'EnvironmentValues.dynamicTypeSize',version:'12.0'},
 {id:'macos-scaled-metric',platform:'macOS',module:'SwiftUICore',needle:'@propertyWrapper public struct ScaledMetric<',api:'ScaledMetric',version:'11.0'},
 {id:'macos-focus',platform:'macOS',module:'SwiftUI',needle:'nonisolated public func accessibilityFocused<Value>',api:'View.accessibilityFocused(_:equals:)',version:'12.0'},
 {id:'tvos-action',platform:'tvOS',module:'SwiftUI',needle:'nonisolated public func accessibilityAction(named name: SwiftUICore.Text,',api:'View.accessibilityAction(named: Text, _:)',version:'13.0'},
 {id:'tvos-children',platform:'tvOS',module:'SwiftUI',needle:'nonisolated public func accessibilityElement(children:',api:'View.accessibilityElement(children:)',version:'13.0'}
];
export function capture(){return {schema:1,scope:'Installed SDK27 public annotations, not runtime behavior or earliest behavioral change',records:specs.map(s=>{
 const sdk=s.platform==='macOS'?'macosx':'appletvsimulator',root=execFileSync('xcrun',['--sdk',sdk,'--show-sdk-path'],{encoding:'utf8'}).trim(),arch=s.platform==='macOS'?'arm64e-apple-macos':'arm64-apple-tvos-simulator';
 const file=root+'/System/Library/Frameworks/'+s.module+'.framework/Modules/'+s.module+'.swiftmodule/'+arch+'.swiftinterface',b=fs.readFileSync(file),lines=b.toString().split('\n'),index=lines.findIndex(l=>l.includes(s.needle));if(index<0)throw Error('Declaration not found: '+s.id);
 let start=index;while(start>=0&&!lines[start].startsWith('@available('))start--;if(start<0||index-start>20)throw Error('Enclosing availability unclear: '+s.id);
 const annotation=lines[start],match=annotation.match(new RegExp(s.platform+' ([0-9.]+)'));if(!match||match[1]!==s.version)throw Error('Reviewed availability changed: '+s.id);
 return {...s,sdkVersion:execFileSync('xcrun',['--sdk',sdk,'--show-sdk-version'],{encoding:'utf8'}).trim(),file,fileSha256:hash(b),line:index+1,startLine:start+1,annotation,excerpt:lines.slice(start,index+1).join('\n'),deploymentTarget:'26.0',declaredSupportedAtTarget:true,interpretation:'Use @available for declaration availability. @_originallyDefinedIn is module history, not a later API introduction. This record makes no interaction or propagation claim.'};
 })};}
if(process.argv[1]?.endsWith('/capture-sdk.mjs'))console.log(JSON.stringify(capture(),null,2));
