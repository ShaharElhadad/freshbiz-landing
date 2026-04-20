"""
Split the logos strip (page4_img1.png, 603x72 on white) into 7 individual PNGs.
Detect boundaries by scanning columns of all-white pixels.
"""
from PIL import Image
import os

src = r"C:\Users\shaha\OneDrive\מסמכים\GitHub\JARVIS\workspace\freshbiz\images\logos-strip.png"
out = r"C:\Users\shaha\OneDrive\מסמכים\GitHub\JARVIS\workspace\freshbiz\images"

img = Image.open(src).convert("RGBA")
W, H = img.size
print(f"strip: {W}x{H}")

px = img.load()
# column is "empty" when almost every pixel is very bright (white bg)
def col_empty(x):
    bright = 0
    for y in range(H):
        r,g,b,a = px[x,y]
        if r > 235 and g > 235 and b > 235:
            bright += 1
    return bright / H > 0.95

empty = [col_empty(x) for x in range(W)]

# find runs of non-empty (logo blocks)
blocks = []
in_block = False
start = 0
for x in range(W):
    if not empty[x] and not in_block:
        in_block = True
        start = x
    elif empty[x] and in_block:
        # end block but only if we have a clear gap of at least 6 px
        gap = 0
        k = x
        while k < W and empty[k]:
            gap += 1
            k += 1
        if gap >= 8 or k == W:
            blocks.append((max(0, start-4), min(W, x+4)))
            in_block = False

if in_block:
    blocks.append((max(0, start-4), W))

print(f"detected {len(blocks)} blocks:")
names = ["microsoft","prada","audi","hp","sony","adidas","ibm"]
# guard: if detection produces wrong count, fall back to equal splits
if len(blocks) != 7:
    print("falling back to equal split")
    blocks = [(i*W//7, (i+1)*W//7) for i in range(7)]

for (x1,x2), name in zip(blocks, names):
    crop = img.crop((x1, 0, x2, H))
    # trim extra white from top/bottom by autocrop? skip — keep strip height
    path = os.path.join(out, f"logo-{name}.png")
    crop.save(path)
    print(f"{name}: {x1}-{x2} ({x2-x1}px) -> {path}")

print("done")
