"""Re-encode untrusted downloads: _dl/<pid>.orig -> <pid>/original.png, _dl/<pid>.mock -> <pid>/mockup_before.jpg. Run: python3 -I _raw/ingest_dl.py ROOT"""
import os, sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = 80_000_000
R = sys.argv[1]
for fn in sorted(os.listdir(os.path.join(R, "_dl"))):
    pid, kind = fn.split(".")
    os.makedirs(os.path.join(R, pid), exist_ok=True)
    im = Image.open(os.path.join(R, "_dl", fn)); im.load()
    if kind == "orig":
        print(pid, im.format, im.mode, im.size)
        im.save(os.path.join(R, pid, "original.png"))
    else:
        im.convert("RGB").save(os.path.join(R, pid, "mockup_before.jpg"), quality=90)
