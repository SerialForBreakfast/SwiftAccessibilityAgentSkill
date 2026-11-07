We target tvOS 26 and use UIKit. Our subtitles setting is an existing UIButton whose visible title changes between “Subtitles: On” and “Subtitles: Off”. Its existing callback changes that setting correctly, the title stays current, and no accessibility failure has been reported.

A review suggests replacing it with a custom accessibility element because it has no custom label override. Is that necessary? Explain what you would preserve, what can be concluded from the supplied information, and what additional context would change your recommendation. No project files or tools are available.
