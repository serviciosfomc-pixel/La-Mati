from PIL import Image
import os

BASE = os.path.dirname(os.path.abspath(__file__))
src  = os.path.join(BASE, "screenshot.png")
img  = Image.open(src)
w, h = img.size
print(f"Full image: {w}x{h}")

sections = [
    ("hero",         0,    900),
    ("endorsed",   900,   1300),
    ("features",  1300,   2000),
    ("showcase",  2000,   2600),
    ("menu",      2600,   3600),
    ("test_foot", 3600,   h   ),
]

for name, y0, y1 in sections:
    y1 = min(y1, h)
    if y0 >= h:
        continue
    crop = img.crop((0, y0, w, y1))
    out  = os.path.join(BASE, f"crop_{name}.png")
    crop.save(out)
    print(f"  {out}  ({crop.size[0]}x{crop.size[1]})")
