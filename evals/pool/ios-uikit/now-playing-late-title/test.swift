var pending: [(item: AVPlayerItem, done: @MainActor (String) -> Void)] = []
let player = AVPlayer()
let vc = NowPlayingViewController(player: player, loadTitle: { item, done in pending.append((item, done)) })
vc.loadViewIfNeeded()
func item(_ n: String) -> AVPlayerItem { AVPlayerItem(url: URL(fileURLWithPath: "/episodes/\(n).m4a")) }
func spoken() -> String { [vc.titleLabel.text, vc.titleLabel.accessibilityLabel].compactMap { $0 }.joined(separator: " ") }
func finish(_ i: Int, _ title: String) { pending[i].done(title) }

// The current episode's title is applied.
let a = item("a"); vc.play(a)
guard pending.count == 1, pending[0].item === a, player.currentItem === a else { return false }
finish(0, "Episode Alpha")
guard vc.titleLabel.text == "Episode Alpha", spoken().contains("Episode Alpha") else { return false }

// Two quick starts from this screen: only the newer title may appear, whatever order the replies arrive in.
let b = item("b"), c = item("c")
vc.play(b); vc.play(c)
guard pending.count == 3, player.currentItem === c else { return false }
finish(2, "Episode Gamma")
finish(1, "Episode Beta")
guard vc.titleLabel.text == "Episode Gamma", !spoken().contains("Beta"), !spoken().contains("Alpha") else { return false }

// Something else replaces the item on the shared player while the lookup is in flight.
let d = item("d"), e = item("e")
vc.play(d)
guard pending.count == 4, !spoken().contains("Gamma") else { return false }
player.replaceCurrentItem(with: e)
finish(3, "Episode Delta")
guard !spoken().contains("Delta") else { return false }

// The screen keeps working afterwards.
let f = item("f"); vc.play(f)
guard let last = pending.last, last.item === f else { return false }
last.done("Episode Foxtrot")
guard vc.titleLabel.text == "Episode Foxtrot", !spoken().contains("Delta") else { return false }

// Play/Pause is still wired to the existing handler.
guard (vc.playPauseButton.actions(forTarget: vc, forControlEvent: .primaryActionTriggered) ?? []).contains("togglePlayback") else { return false }
return true
