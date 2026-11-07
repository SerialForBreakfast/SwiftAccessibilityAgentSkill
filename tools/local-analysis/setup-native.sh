#!/bin/sh
set -eu
cd "$(dirname "$0")/../.."
host="$(xcode-select -p)/Toolchains/XcodeDefault.xctoolchain/usr/lib/swift/host"
if [ ! -d "$host" ]; then
  host="$(xcrun --find swiftc | sed 's@/bin/swiftc$@/lib/swift/host@')"
fi
mkdir -p tools/local-analysis/.cache
xcrun swiftc -I "$host" -L "$host" -lSwiftSyntax -lSwiftParser \
  -Xlinker -rpath -Xlinker "$host" \
  -module-cache-path "${TMPDIR:-/tmp}/swift-accessibility-analysis-module-cache" \
  tools/local-analysis/SyntaxProbe.swift -o tools/local-analysis/.cache/syntax-probe
# Download-only; extract the reviewed executable locally, not a global installation.
HOMEBREW_NO_AUTO_UPDATE=1 brew fetch --force-bottle swiftlint
bottle="$(HOMEBREW_NO_AUTO_UPDATE=1 brew --cache --force-bottle swiftlint)"
case "$bottle" in
  *swiftlint--0.65.1.*) ;;
  *) echo "SwiftLint bottle version changed; review and update the pinned adapter first." >&2; exit 1 ;;
esac
tar -xzf "$bottle" -C tools/local-analysis/.cache swiftlint/0.65.1/bin/swiftlint
