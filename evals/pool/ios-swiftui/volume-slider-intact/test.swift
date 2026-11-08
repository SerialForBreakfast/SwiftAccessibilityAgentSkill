let s = ListeningSettings()
var saved: [Double] = []
s.save = { saved.append($0) }
_ = ListeningSettingsView(settings: s)

// Existing range, step and visible readout are unchanged.
guard s.volume == 60, s.range == 0...100, s.step == 5, s.volumeText == "60%" else { return false }

// The slider's binding writes through the same bounded, stepped setter and saves once per change.
s.volumeBinding.wrappedValue = 75
guard s.volume == 75, s.volumeBinding.wrappedValue == 75, s.volumeText == "75%", saved == [75] else { return false }
s.volumeBinding.wrappedValue = 75
guard saved == [75] else { return false }
s.setVolume(73)
guard s.volume == 75, saved == [75] else { return false }
s.setVolume(82)
guard s.volume == 80, saved == [75, 80] else { return false }
s.setVolume(140)
guard s.volume == 100, s.volumeText == "100%", saved == [75, 80, 100] else { return false }
s.setVolume(-3)
guard s.volume == 0, s.volumeText == "0%", saved == [75, 80, 100, 0] else { return false }
s.volumeBinding.wrappedValue = -10
guard saved.count == 4 else { return false }
return true
