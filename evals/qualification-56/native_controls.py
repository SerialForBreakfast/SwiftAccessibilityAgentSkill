"""Controller-only implementation controls. Each triplet runs an identical XCTest body."""
from common import *

def swap(s,old,new):
    assert s.count(old)==1,(old,s.count(old))
    return s.replace(old,new)

def load(path):
    return (ROOT/'code-examples'/path).read_text()

def triplet(ids,platform,path,edits,defect,body):
    ref=load(path)
    alt=ref
    for before,after in edits: alt=swap(alt,before,after)
    mut=swap(ref,*defect)
    return dict(ids=ids.split(),platform=platform,src=(ref,alt,mut),body=body,origin=path)

def uuidgen(var):
    return [(f'private var {var} = 0',f'private var {var} = UUID()'),(f'{var} += 1',f'{var} = UUID()')]

def suites():
    out=[]
    for plat,ks in [('iOS','7d8c 7622'),('tvOS','7766 a00e')]:
        path='swiftui/'+plat.lower()+'-v1/Sources/Interop.swift'
        out.append(triplet(ks,plat,path,[('private var generation = 0','private var generation = UUID()'),
                    ('generation += 1; self.button','generation = UUID(); self.button'),('generation += 1\n','generation = UUID()\n')],
                    ('self.generation == ticket, ',''),
                    '''let owner=BridgeOwner(), a=UIButton(), b=UIButton()
        var events=[String]()
        owner.configure(a,title:"First",enabled:true){events.append("A")}
        a.sendActions(for:.primaryActionTriggered)
        owner.configure(b,title:"Second",enabled:true){events.append("B")}
        a.sendActions(for:.primaryActionTriggered)
        b.sendActions(for:.primaryActionTriggered)
        owner.stop(); b.sendActions(for:.primaryActionTriggered)
        XCTAssertEqual(events,["A","B"],"witness")'''))
    out.append(triplet('51e9 89b1','iOS','pilots/uikit-dynamic-v1/Sources/DynamicUIKit.swift',
        uuidgen('revision')+[('perform(token: Int','perform(token: UUID')],('guard token == revision, active','guard active'),
        '''var log=[String]()
        let view=ReusableMessageActions { log.append($0 + ":" + $1.rawValue) }
        view.configure(id:"A",title:"First",enabled:true)
        let a=try XCTUnwrap(view.summary.accessibilityCustomActions?.last)
        view.configure(id:"B",title:"Next",enabled:true)
        XCTAssertEqual(a.actionHandler?(a),false,"witness")
        let b=try XCTUnwrap(view.summary.accessibilityCustomActions?.last)
        XCTAssertEqual(b.actionHandler?(b),true)
        view.archiveButton.sendActions(for:.touchUpInside);view.deleteButton.sendActions(for:.touchUpInside)
        XCTAssertEqual(log,["B:delete","B:archive","B:delete"],"witness")'''))
    out.append(triplet('852a a12b','tvOS','platforms/tvos-results-v1/Sources/TelevisionResults.swift',uuidgen('generation'),
        ('self.generation == revision, ',''),
        '''let v=TelevisionResults(), rows=[TelevisionResults.Item(id:"A",title:"First",actionName:"Open"),.init(id:"B",title:"Second",actionName:"Open")]
        XCTAssertTrue(v.apply(rows));let old=v.buttons[0]
        XCTAssertTrue(v.apply(rows));v.buttons[1].sendActions(for:.primaryActionTriggered)
        old.sendActions(for:.primaryActionTriggered)
        XCTAssertEqual(v.selectedID,"B","witness")'''))
    out.append(triplet('f6c7','macOS','swiftui/macos-v1/Sources/Documents.swift',
        [('private var revision = 0','private var revision = UUID()'),('revision += 1; entries','revision = UUID(); entries'),('self.revision += 1','self.revision = UUID()')],
        ('self.revision == generation,','true,'),
        '''let s=DocumentState();var removed=[String]();s.deleted={removed.append($0)}
        let a=Article(id:"a",title:"old",important:false)
        XCTAssertTrue(s.replace([a]));let old=s.action(for:"a",remove:true)
        XCTAssertTrue(s.replace([Article(id:"a",title:"new",important:true)]))
        old();XCTAssertTrue(removed.isEmpty,"witness")
        s.action(for:"a",remove:true)();XCTAssertEqual(removed,["a"])'''))
    out.append(triplet('76d9 b435','macOS','platforms/macos-closure-details-v1/Sources/DesktopRow.swift',
        [('setAccessibilityChildren([open])','// Children reported dynamically.'),('    required init?', '    override func accessibilityChildren() -> [Any]? { [open] }\n    required init?')],
        ('setAccessibilityElement(true)','setAccessibilityElement(false)'),
        '''let v=DesktopRow(frame:.zero);var opened=[String]();v.choose={opened.append($0)}
        for (i,on) in [("alpha",true),("beta",false)] {
          v.configure(id:i,title:i,selected:on,expanded:on)
          XCTAssertTrue(v.isAccessibilityElement(),"witness");XCTAssertEqual(v.accessibilityRole(),.row)
          XCTAssertEqual(v.isAccessibilitySelected(),on);XCTAssertEqual(v.isAccessibilityExpanded(),on)
          XCTAssertTrue(v.accessibilityChildren()?.contains { ($0 as? NSButton) === v.open } == true)
          XCTAssertTrue(v.open.accessibilityLabel().contains(i));v.open.performClick(nil)
        };XCTAssertEqual(opened,["alpha","beta"])'''.replace('v.open.accessibilityLabel().contains','(v.open.accessibilityLabel() ?? "").contains')))
    out.append(triplet('777d 3f81','macOS','platforms/macos-appkit-v1/Sources/DesktopActions.swift',uuidgen('generation'),
        ('save.action = #selector(saveItem)','save.action = #selector(openItem)'),
        '''let v=DesktopActions();var log=[String]()
        for i in ["A","B"] {v.configure(title:i,openName:"Open "+i,saveName:"Save "+i,onOpen:{log.append("O"+i)},onSave:{log.append("S"+i)})}
        v.open.performClick(nil); v.save.performClick(nil)
        let a=try XCTUnwrap(v.open.accessibilityCustomActions()?.first)
        XCTAssertTrue(a.handler?() == true);v.save.isEnabled=false;XCTAssertFalse(a.handler?() == true)
        XCTAssertEqual(log,["OB","SB","SB"],"witness")'''))
    for ids,defect,edits in [('4328',('self.onDetails()\n','self.onPlay()\n'),uuidgen('generation')),
        ('7b8c',('play.setTitle(playName, for: .normal); details.setTitle(detailsName, for: .normal)','play.accessibilityIdentifier = playName; details.accessibilityIdentifier = detailsName'),
        [('play.setTitle(playName, for: .normal); details.setTitle(detailsName, for: .normal)','for (button,name) in [(play,playName),(details,detailsName)] { var config = UIButton.Configuration.plain(); config.title = name; button.configuration = config }')])]:
        out.append(triplet(ids,'tvOS','platforms/tvos-uikit-v1/Sources/TelevisionActions.swift',edits,defect,
        '''let v=TelevisionActions();var log=[String]()
        for i in ["A","B"] {v.configure(title:i,playName:"Play "+i,detailsName:"Details "+i,onPlay:{log.append("P"+i)},onDetails:{log.append("D"+i)})}
        v.play.sendActions(for:.primaryActionTriggered);v.details.sendActions(for:.primaryActionTriggered)
        let a=try XCTUnwrap(v.play.accessibilityCustomActions?.first);XCTAssertEqual(a.actionHandler?(a),true)
        XCTAssertEqual(log,["PB","DB","DB"],"witness")
        for (button,title) in [(v.play,"Play B"),(v.details,"Details B")] {
          XCTAssertEqual(button.configuration?.title ?? button.title(for:.normal),title,"witness");XCTAssertEqual(button.accessibilityLabel,title)
        }'''))
    out.append(triplet('1046','tvOS','platforms/tvos-closure-v1/Sources/StateContracts.swift',
        [('selected ? "Selected" : "Not selected"','selected ? "Chosen" : "Not chosen"')],
        [('status.text = selected ? "Selected" : "Not selected"'),('status.text = ""')],
        '''let v=RegionState(frame:.zero);var words=[String]()
        for on in [true,false,true] {v.configure(name:"Item",selected:on,reduceTransparency:false)
          let word=try XCTUnwrap(v.status.text);XCTAssertFalse(word.isEmpty,"witness");words.append(word)
          XCTAssertEqual(v.button.accessibilityValue,word);XCTAssertEqual(v.button.accessibilityTraits.contains(.selected),on)
        };XCTAssertEqual(words[0],words[2]);XCTAssertNotEqual(words[0],words[1],"witness")'''))
    out.append(triplet('a5c8','iOS','pilots/uikit-v1/Sources/OrderCell.swift',
        [(r'"Priority order for \(order.customer)"',r'"\(order.customer), priority"')],
        ('accessibilityValue = order.status','if accessibilityValue == nil { accessibilityValue = order.status }'),
        '''let v=OrderCell(style:.default,reuseIdentifier:"r")
        for (name,priority,status) in [("Ana",true,"sent"),("Bo",false,"paid")] {
          v.configure(Order(customer:name,status:status,isPriority:priority))
          let label=try XCTUnwrap(v.accessibilityLabel)
          XCTAssertTrue(label.contains(name));XCTAssertEqual(label.lowercased().contains("priority"),priority)
          XCTAssertEqual(v.titleLabel.text,name);XCTAssertEqual(v.accessibilityValue,status,"witness")
        }'''))
    out.append(triplet('dd7e','macOS','platforms/macos-structure-v1/Sources/DesktopOutline.swift',
        [('nodes[node.id] === node','nodes.values.contains(where: { $0 === node })')],('nodes[node.id] === node','true'),
        '''let d=DesktopOutline();let parent=DesktopOutline.Item(id:"g",title:"Group",children:[.init(id:"a",title:"Alpha")])
        XCTAssertTrue(d.apply([parent]));let old=try XCTUnwrap(d.nodes["g"])
        XCTAssertFalse(d.apply([parent,parent]));XCTAssertTrue(d.nodes["g"] === old)
        XCTAssertTrue(d.apply([]));XCTAssertFalse(d.outlineView(d.outline,isItemExpandable:old),"witness")
        XCTAssertEqual(d.outlineView(d.outline,numberOfChildrenOfItem:old),0,"witness")'''))
    return out
