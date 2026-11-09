from native_controls import *
import base64,re
sys.path.insert(0,str(V4.parent/'signal-panel-v3'))
from alternatives import apply
def specs():
    out=[]
    for ids,platform in [('d76c','tvOS'),('f28c','macOS')]:
        path=f'platforms/{platform.lower()}-media-v1/Sources/MediaMetadata.swift'
        # Test classification against native flags, independently of which option is selected.
        out.append(triplet(ids,platform,path,[('let selected = item.currentMediaSelection.selectedMediaOption(in: group)','let tagged = group.options.filter { $0.hasMediaCharacteristic(.describesVideoForAccessibility) }; let selected = item.currentMediaSelection.selectedMediaOption(in: group)'),
           ('describesVideo: option.hasMediaCharacteristic(.describesVideoForAccessibility)','describesVideo: tagged.contains(option)')],
           ('describesVideo: option.hasMediaCharacteristic(.describesVideoForAccessibility)','describesVideo: option.locale != nil'),
           '''let item=AVPlayerItem(url:URL(fileURLWithPath:"MOVIE"))
        let g=try await item.asset.loadMediaSelectionGroup(for:.audible)
        let audio=try XCTUnwrap(g)
        let ordinary=try XCTUnwrap(audio.options.first{ !$0.hasMediaCharacteristic(.describesVideoForAccessibility) })
        let tagged=try XCTUnwrap(audio.options.first{ $0.hasMediaCharacteristic(.describesVideoForAccessibility) })
        item.select(ordinary,in:audio)
        guard case .loaded(let rows)=try await MediaMetadata.group(.audible,item:item) else {return XCTFail("load prerequisite")}
        XCTAssertEqual(rows.count,audio.options.count)
        for opt in [ordinary,tagged] {
          let idx=try XCTUnwrap(audio.options.firstIndex(of:opt))
          XCTAssertEqual(rows[idx].describesVideo,opt==tagged,"witness")
        };XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in:audio),ordinary)'''))
    out.append(triplet('7cc5','tvOS','platforms/tvos-media-v1/Sources/MediaChoice.swift',
        [('guard let option = group.options.first(where: {','let matches = group.options.filter {'),('}) else { return false }','}; guard let option = matches.first else { return false }')],
        ('(!requiresDescription || $0.hasMediaCharacteristic(.describesVideoForAccessibility))','true'),
        '''let item=AVPlayerItem(url:URL(fileURLWithPath:"MOVIE"))
        let g=try await item.asset.loadMediaSelectionGroup(for:.audible)
        let audio=try XCTUnwrap(g)
        let ordinary=try XCTUnwrap(audio.options.first{ !$0.hasMediaCharacteristic(.describesVideoForAccessibility) })
        let tagged=try XCTUnwrap(audio.options.first{ $0.hasMediaCharacteristic(.describesVideoForAccessibility) })
        let lang=try XCTUnwrap(ordinary.locale?.language.languageCode?.identifier)
        XCTAssertNotEqual(lang,tagged.locale?.language.languageCode?.identifier)
        item.select(tagged,in:audio);XCTAssertFalse(MediaChoice.select(language:lang,requiresDescription:true,in:audio,item:item),"witness")
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in:audio),tagged,"witness")'''))
    out.append(triplet('9c45','iOS','pilots/uikit-media-metadata-v1/Sources/MediaMetadata.swift',
        [('guard let item else { return .unavailable }','switch item { case nil: return .unavailable; case .some: break }; let item = item!')],
        ('guard let item else { return .unavailable }','guard let item else { return .absent }'),
        '''let missing=try await MediaMetadata.group(.audible,item:nil)
        guard case .unavailable = missing else {return XCTFail("witness")}
        let inspected=try await MediaMetadata.group(.audible,item:AVPlayerItem(asset:AVMutableComposition()))
        guard case .absent = inspected else {return XCTFail("absent group")}'''))
    out.append(triplet('7d27','macOS','swiftui/forwarding-macos-v1/Sources/NativeSurface.swift',
       [('view.primary.setAccessibilityHelp(snapshot.hint)','if view.primary.accessibilityHelp() != snapshot.hint { view.primary.setAccessibilityHelp(snapshot.hint) }')],
       ('view.primary.setAccessibilityHelp(snapshot.hint)','view.primary.setAccessibilityHelp(snapshot.hint ?? "")'),
       '''let c=SurfaceOwner(), v=NativeSurface()
        c.configure(v,snapshot:SurfaceSnapshot(hint:"help"),perform:{_,_ in})
        XCTAssertEqual(v.primary.accessibilityHelp(),"help")
        c.configure(v,snapshot:SurfaceSnapshot(hint:nil),perform:{_,_ in})
        XCTAssertNil(v.primary.accessibilityHelp(),"witness")'''))
    out.append(triplet('db32','iOS','pilots/uikit-reuse-v1/Sources/ReuseUIKit.swift',
        [('if saved { accessibilityTraits.insert(.selected) }\n        else { accessibilityTraits.remove(.selected) }','accessibilityTraits = saved ? accessibilityTraits.union(.selected) : accessibilityTraits.subtracting(.selected)')],
        ('else { accessibilityTraits.remove(.selected) }','else { isSelected = true }'),
        '''let cell=SavedItemCell(frame:.zero);cell.accessibilityTraits.insert(.header)
        for saved in [true,false] {cell.configure(id:"i",title:"Invoice",saved:saved,removable:false,language:"en")
        XCTAssertEqual(cell.accessibilityTraits.contains(.selected),saved,"witness")
        XCTAssertTrue(cell.accessibilityTraits.contains(.header));XCTAssertFalse(cell.isSelected,"witness")
        cell.isSelected=true;XCTAssertEqual(cell.accessibilityValue,saved ? "Saved":"Not saved");cell.isSelected=false}'''))
    naming='pilots/uikit-naming-v1/Sources/'+next((ROOT/'code-examples/pilots/uikit-naming-v1/Sources').glob('*.swift')).name
    out.append(triplet('1079','iOS',naming,[
        ('openButton.addAction(UIAction { [weak self] _ in self?.openHandler() }, for: .touchUpInside)',''),
        ('openHandler = onOpen','let key = UIAction.Identifier("open"); openButton.removeAction(identifiedBy:key,for:.touchUpInside); openButton.addAction(UIAction(identifier:key){_ in onOpen()},for:.touchUpInside)')],
        ('openHandler = onOpen','openButton.addAction(UIAction { _ in onOpen() },for:.touchUpInside)'),
        '''let v=ItemActionCard(frame:.zero);var log=[String]()
        for i in ["A","B"] {v.configure(title:i,openTitle:"Open",saveTitle:"Save",openName:"Open "+i,saveName:"Save "+i,onOpen:{log.append("O"+i)},onSave:{log.append("S"+i)})}
        XCTAssertFalse(v.decoration.isAccessibilityElement);XCTAssertFalse(v.isAccessibilityElement)
        XCTAssertEqual(v.openButton.accessibilityLabel,"Open B");XCTAssertEqual(v.saveButton.accessibilityLabel,"Save B")
        v.openButton.sendActions(for:.touchUpInside);v.saveButton.sendActions(for:.touchUpInside)
        XCTAssertEqual(log,["OB","SB"],"witness")'''))
    path='platforms/tvos-lifecycle-v1/Sources/TelevisionLifecycle.swift'
    s=load(path)
    out.append(triplet('0a2c','tvOS',path,[('private var generation = 0','private var generation = UUID()'),
        ('generation += 1\n        let revision','generation = UUID()\n        let revision'),('func stop() { generation += 1','func stop() { generation = UUID()')],
        ('self.observations != nil, self.generation == revision','self.observations != nil'),
        '''let center=NotificationCenter()
        var snap=DisplayPreferences(), seen=[DisplayPreferences]()
        var jobs=[@MainActor @Sendable ()->Void]()
        let observer=TelevisionPreferences(center:center,read:{snap},enqueue:{work in MainActor.assumeIsolated {jobs.append(work)}},apply:{seen.append($0)})
        observer.start();center.post(name:TelevisionPreferences.names[0],object:nil)
        XCTAssertEqual(jobs.count,1);let old=jobs.removeFirst()
        observer.stop();observer.start();let before=seen.count;snap.reduceMotion.toggle()
        old();XCTAssertEqual(seen.count,before,"witness")
        center.post(name:TelevisionPreferences.names[0],object:nil);try XCTUnwrap(jobs.first)()
        XCTAssertEqual(seen.count,before+1);XCTAssertEqual(seen.last,snap)'''))
    for ids,plat,lane in [('2865 6d2d','iOS','write'),('5d12','tvOS','write'),('4ec9','iOS','phase'),
                           ('c04c','iOS','stale'),('c6b2','tvOS','stale'),('f483','macOS','stale')]:
        s=load(f'swiftui/media-{plat.lower()}-v2/Sources/MediaSelection.swift')
        alt=apply('MediaSelection.swift',s)
        mut=swap(s,{'write':'item.select(choice.option, in: group)','phase':'phase = item == nil ? .noItem : .loading','stale':'guard self.generation == ticket, self.item === owningItem else { return }'}[lane],
                 {'write':'_ = choice.option','phase':'phase = item == nil ? .absent : .loading','stale':'// no ownership check'}[lane])
        body='''let player=AVPlayer(),s=MediaSelectionStore(player:player)
        await s.refresh();XCTAssertEqual(s.phase,.noItem,"witness")
        let item=AVPlayerItem(url:URL(fileURLWithPath:"MOVIE"));player.replaceCurrentItem(with:item)
        let first=s.beginLoad();XCTAssertEqual(s.phase,.loading);s.complete(first,result:.failure(NSError(domain:"fixture",code:1)));XCTAssertEqual(s.phase,.failed)
        let empty=s.beginLoad();s.complete(empty,result:.success(nil));XCTAssertEqual(s.phase,.absent)
        await s.refresh()
        let tg=try await item.asset.loadMediaSelectionGroup(for:.legible), ag=try await item.asset.loadMediaSelectionGroup(for:.audible)
        let text=try XCTUnwrap(tg), audio=try XCTUnwrap(ag), track=try XCTUnwrap(audio.options.first{$0.hasMediaCharacteristic(.describesVideoForAccessibility)})
        item.select(track,in:audio)
        let excluded=try XCTUnwrap(text.options.first{$0.hasMediaCharacteristic(.containsOnlyForcedSubtitles)})
        item.select(excluded,in:text);XCTAssertEqual(s.selectedID,s.unlistedSelectionID)
        XCTAssertFalse(s.choices.contains{$0.option==excluded})
        s.selection.wrappedValue="unknown";XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in:text),excluded)
        let old=s.selection;await s.refresh()
        let choice=try XCTUnwrap(s.choices.first)
        s.selection.wrappedValue=choice.id
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in:text),choice.option,"witness")
        old.wrappedValue=nil;XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in:text),choice.option,"witness")
        XCTAssertTrue(s.allowsOff);s.selection.wrappedValue=nil;XCTAssertNil(item.currentMediaSelection.selectedMediaOption(in:text))
        XCTAssertEqual(item.currentMediaSelection.selectedMediaOption(in:audio),track)
        let late=s.beginLoad();s.cancel();s.complete(late,result:.success(text));XCTAssertEqual(s.phase,.idle)'''
        if lane=='stale':
            body+='''
        let replacement=AVPlayerItem(url:URL(fileURLWithPath:"MOVIE"));player.replaceCurrentItem(with:replacement)
        await s.refresh();let options=try await replacement.asset.loadMediaSelectionGroup(for:.legible)
        let g=try XCTUnwrap(options),c=try XCTUnwrap(s.choices.first)
        s.selection.wrappedValue=c.id;old.wrappedValue=nil
        XCTAssertEqual(replacement.currentMediaSelection.selectedMediaOption(in:g),c.option,"witness")
        s.selection.wrappedValue=nil;XCTAssertNil(replacement.currentMediaSelection.selectedMediaOption(in:g))'''
        out.append(dict(ids=ids.split(),platform=plat,origin='media-'+lane,src=(s,alt,mut),body=body))
    for k,path,alt,mut in [('f776','ios-uikit/receipt-font-traits','alternative-scaled-value','mutant-ambient-traits'),
                           ('e505','ios-swiftui/volume-slider-intact','alternative-matching-value','mutant-normalized-fraction')]:
        d=ROOT/'evals/pool'/path
        out.append(dict(ids=[k],platform='iOS',origin=path,src=tuple((d/(name+'.swift')).read_text() for name in ('reference',alt,mut)),body='func observe() -> Bool {\n'+(d/'test.swift').read_text()+'\n}; XCTAssertTrue(observe(),"witness")'))
    return out
