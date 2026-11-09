from more_controls import *

def specs():
    out=[]
    panel='pilots/uikit-modal-v1/Sources/ModalUIKit.swift';ref=load(panel)
    out.append(dict(ids=['d2dd'],platform='iOS',origin=panel,src=(ref,apply('ModalUIKit.swift',ref),
        swap(ref,'state = .closing','state = .closing; post(.screenChanged,returnTarget)')),
        body='''let root=UIView(), origin=UIButton(), p=RestoringPanel();root.addSubview(origin)
        var jobs=[@MainActor ()->Void](),posts=[UIView?]();p.performDismissal={jobs.append($0)};p.post={_,v in posts.append(v as? UIView)}
        for cancel in [true,false] {
          XCTAssertTrue(p.open(background:root,target:origin,title:"Edit",primaryTitle:"Apply",closeTitle:"Close"))
          p.close.sendActions(for:.touchUpInside)
          XCTAssertTrue(posts.isEmpty,"witness");if cancel {p.tearDown()}
          let done=try XCTUnwrap(jobs.first);jobs.removeAll();done();done()
          if cancel {XCTAssertTrue(posts.isEmpty,"witness")} else {XCTAssertEqual(posts.count,1,"witness");XCTAssertTrue(posts.first! === origin)}
        }'''.replace('XCTAssertTrue(posts.first! === origin)','XCTAssertTrue(posts.first.flatMap{$0} === origin)')))
    src=(V4.parent/'signal-panel-v3/Presentation.swift').read_text()
    shared=src.replace('private var active: UUID?', 'private var active: UUID?; private var latest: (UUID,String)?').replace('active = id','active = id; latest=(id,origin)').replace('guard let self, self.active == id','guard let self, let (id,origin)=self.latest,self.active == id')
    out.append(dict(ids=['4840','da78'],platform='macOS',origin='Presentation.swift',src=(src,apply('Presentation.swift',src),shared),
        body='''var log=[String](),caller="setup"
        let owner=SheetOwner {log.append(caller+$0)}
        let a=owner.presentation(origin:"A",showing:.constant(true)),b=owner.presentation(origin:"B",showing:.constant(true))
        caller="old";a.onDismiss();XCTAssertTrue(log.isEmpty,"witness")
        caller="first";b.onDismiss();caller="again";b.onDismiss();XCTAssertEqual(log,["firstB"],"witness")'''))
    src='''import UIKit
@MainActor func makeEdit(_ title:NSAttributedString,grouped:Bool,handler:@escaping UIAccessibilityCustomAction.Handler)->UIAccessibilityCustomAction {
    let action=UIAccessibilityCustomAction(attributedName:title,actionHandler:handler)
    action.category=grouped ? UIAccessibilityCustomAction.editCategory : nil
    return action
}'''
    out.append(dict(ids=['9ae5'],platform='iOS',origin='optional caller setting',src=(src,
        src.replace('action.category=grouped ? UIAccessibilityCustomAction.editCategory : nil','if grouped { action.category=UIAccessibilityCustomAction.editCategory }'),
        src.replace('grouped ? UIAccessibilityCustomAction.editCategory : nil','UIAccessibilityCustomAction.editCategory')),body='''
        var calls=0
        for grouped in [true,false] {
            let a=makeEdit(NSAttributedString(string:"Rename"),grouped:grouped){_ in calls+=1;return true}
            XCTAssertEqual(a.category,grouped ? UIAccessibilityCustomAction.editCategory:nil,"witness")
            XCTAssertEqual(a.name,"Rename");XCTAssertEqual(a.actionHandler?(a),true)
        };XCTAssertEqual(calls,2)'''))
    src='''import UIKit
@MainActor final class Status {
 let label=UILabel();let announce:(String)->Void
 init(_ announce:@escaping (String)->Void){self.announce=announce}
 var active:UUID?;var terminal=false
 func begin(_ id:UUID){active=id;terminal=false;label.accessibilityValue="0%"}
 func update(_ id:UUID,_ n:Int?,_ end:String?){
   guard active==id,!terminal else{return}
   if let end {terminal=true;label.accessibilityValue=end;announce(end)}
   else if let n {label.accessibilityValue="\\(min(100,max(0,n)))%"}
 }
}'''
    out.append(dict(ids=['debf'],platform='iOS',origin='download notification recording seam',src=(src,src.replace('terminal=true;label','active=nil;label'),
        src.replace('!terminal','true')),body='''var posts=[String]();let s=Status{posts.append($0)}
        let a=UUID(), b=UUID();s.begin(a);s.update(a,110,nil);XCTAssertEqual(s.label.accessibilityValue,"100%")
        XCTAssertTrue(posts.isEmpty);s.update(a,nil,"done");s.update(a,14,nil);s.update(a,nil,"error")
        XCTAssertEqual(posts,["done"],"witness");XCTAssertEqual(s.label.accessibilityValue,"done","witness")
        s.begin(b);s.update(a,nil,"stale");s.update(b,-1,nil);XCTAssertEqual(s.label.accessibilityValue,"0%")
        s.update(b,nil,"failed");XCTAssertEqual(posts,["done","failed"],"witness")'''))
    return out
