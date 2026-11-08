var replies: [@MainActor (SyncResult) -> Void] = []
let strip = SyncStatusView(fetch: { replies.append($0) })
func spoken() -> String {
    [strip.statusLabel.text, strip.statusLabel.accessibilityLabel, strip.statusLabel.accessibilityValue,
     strip.retryButton.isHidden ? nil : strip.retryButton.accessibilityLabel,
     strip.retryButton.isHidden ? nil : strip.retryButton.accessibilityHint]
        .compactMap { $0 }.joined(separator: " | ")
}

// A failure shows the reason and an ordinary working Retry.
strip.refresh()
guard replies.count == 1 else { return false }
replies[0](.failed(reason: "No network connection"))
guard spoken().contains("No network connection"), !strip.retryButton.isHidden, strip.retryButton.isEnabled
else { return false }
activate(strip.retryButton)
guard strip.retryCount == 1, replies.count == 2 else { return false }

// Recovery replaces every trace of the old failure.
replies[1](.synced(itemCount: 12))
guard strip.statusLabel.text == "Up to date", spoken().contains("12"),
      !spoken().contains("No network"), !(strip.retryButton.accessibilityHint ?? "").contains("No network")
else { return false }

// A second failure replaces the first reason rather than adding to it.
strip.refresh(); replies[2](.failed(reason: "Server busy"))
strip.refresh(); replies[3](.failed(reason: "Disk full"))
guard spoken().contains("Disk full"), !spoken().contains("Server busy"),
      (strip.retryButton.accessibilityHint ?? "").contains("Disk full") || spoken().contains("Disk full")
else { return false }

// Two refreshes in flight: only the newer reply decides, whichever order they arrive in.
strip.refresh(); strip.refresh()
guard replies.count == 6 else { return false }
replies[5](.failed(reason: "Quota exceeded"))
replies[4](.synced(itemCount: 3))
guard spoken().contains("Quota exceeded"), strip.statusLabel.text != "Up to date", !strip.retryButton.isHidden
else { return false }

strip.refresh(); strip.refresh()
replies[6](.failed(reason: "Token expired"))
guard !spoken().contains("Token expired"), !spoken().contains("Quota") else { return false }
replies[7](.synced(itemCount: 40))
guard strip.statusLabel.text == "Up to date", spoken().contains("40"), !spoken().contains("Token expired")
else { return false }

// Retry is still the same working control afterwards.
strip.refresh(); replies[8](.failed(reason: "Offline"))
activate(strip.retryButton)
return strip.retryCount == 2 && replies.count == 10
