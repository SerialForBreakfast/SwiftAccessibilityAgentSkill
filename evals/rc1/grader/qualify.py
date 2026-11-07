"""Boot installed unit anchors when needed; leave pre-existing sessions alone."""
import json
from pathlib import Path
import subprocess
import sys


def main():
    started = []
    try:
        devices = json.loads(subprocess.check_output(["xcrun","simctl","list","devices","available","-j"], timeout=30))["devices"]
        for platform in ("iOS","tvOS"):
            candidates = devices.get("com.apple.CoreSimulator.SimRuntime."+platform+"-26-5", [])
            if not candidates:
                raise SystemExit("Missing installed "+platform+" 26.5 unit anchor; no run authorized on a substitute.")
            if any(d["state"]=="Booted" for d in candidates):
                continue
            unit = next((d for d in candidates if d["name"]=="SwiftAccessibility-OS26-Unit-"+platform),None)
            if not unit:
                raise SystemExit("Boot a suitable existing "+platform+" 26.5 device, or provide the dedicated unit anchor.")
            subprocess.run(["xcrun","simctl","boot",unit["udid"]],check=True,timeout=120)
            started.append(unit["udid"])
            subprocess.run(["xcrun","simctl","bootstatus",unit["udid"]],check=True,timeout=180)
        return subprocess.call([sys.executable,"-B",str(Path(__file__).with_name("grade.py"))])
    finally:
        for device in reversed(started):
            subprocess.run(["xcrun","simctl","shutdown",device],timeout=120)


if __name__=="__main__":
    sys.exit(main())
