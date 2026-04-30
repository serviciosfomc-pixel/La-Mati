import subprocess
import sys
import os
import time

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE   = os.path.dirname(os.path.abspath(__file__))
HTML   = os.path.join(BASE, "index.html")
TEMP   = os.path.join(BASE, "_screenshot_temp.html")
OUT    = os.path.join(BASE, "screenshot.png")

# Read original HTML and override vh units so all sections stack properly
with open(HTML, encoding="utf-8") as f:
    content = f.read()

# Replace full-viewport hero with fixed height for screenshot
patched = content.replace("min-height: 100vh", "min-height: 760px")

with open(TEMP, "w", encoding="utf-8") as f:
    f.write(patched)

url = "file:///" + TEMP.replace("\\", "/")

cmd = [
    CHROME,
    "--headless",
    "--disable-gpu",
    "--no-sandbox",
    "--hide-scrollbars",
    "--disable-extensions",
    "--no-first-run",
    "--disable-background-networking",
    "--disable-sync",
    "--metrics-recording-only",
    f"--screenshot={OUT}",
    "--window-size=1440,5000",
    "--force-device-scale-factor=1",
    "--virtual-time-budget=3000",
    url,
]

print(f"Launching Chrome 1440x5000 (full page mode)...")
proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

for i in range(25):
    time.sleep(1)
    if os.path.exists(OUT) and os.path.getsize(OUT) > 50000:
        proc.kill()
        os.remove(TEMP)
        size = os.path.getsize(OUT)
        print(f"Screenshot saved: {OUT}  ({size:,} bytes)")
        sys.exit(0)
    print(f"  waiting... {i+1}s")

proc.kill()
if os.path.exists(TEMP):
    os.remove(TEMP)

if os.path.exists(OUT) and os.path.getsize(OUT) > 50000:
    print(f"Screenshot saved: {OUT}  ({os.path.getsize(OUT):,} bytes)")
    sys.exit(0)

print("ERROR: screenshot not created")
sys.exit(1)
