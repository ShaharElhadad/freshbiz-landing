"""Remove near-white background from logo PNGs (make transparent)."""
from PIL import Image
from pathlib import Path

img_dir = Path(r"C:\Users\shaha\OneDrive\מסמכים\GitHub\JARVIS\workspace\freshbiz\images")
logos = ["microsoft","prada","audi","hp","sony","adidas","ibm"]

THRESHOLD = 235  # pixels brighter than this in all channels become transparent

for name in logos:
    src = img_dir / f"logo-{name}.png"
    if not src.exists():
        print(f"miss: {src}")
        continue
    img = Image.open(src).convert("RGBA")
    data = img.getdata()
    new = []
    for r, g, b, a in data:
        if r >= THRESHOLD and g >= THRESHOLD and b >= THRESHOLD:
            new.append((r, g, b, 0))  # transparent
        else:
            new.append((r, g, b, a))
    img.putdata(new)
    dst = img_dir / f"logo-{name}.png"  # overwrite in place
    img.save(dst)
    w, h = img.size
    print(f"cleaned: {name} {w}x{h}")

print("done")
