import fitz, os, sys

pdf_path = r"c:\Users\shaha\Downloads\דף נחתה משחק פרשמיינד.pdf"
out_dir = r"C:\Users\shaha\OneDrive\מסמכים\GitHub\JARVIS\workspace\freshbiz\images"
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"pages: {len(doc)}")

# Extract embedded images
for pno in range(len(doc)):
    page = doc[pno]
    for idx, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n - pix.alpha >= 4:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        name = f"page{pno+1}_img{idx+1}.png"
        pix.save(os.path.join(out_dir, name))
        print(f"saved {name} {pix.width}x{pix.height}")
        pix = None

# Also render each page as hi-res PNG for reference
for pno in range(len(doc)):
    page = doc[pno]
    pix = page.get_pixmap(dpi=200)
    name = f"render_page{pno+1}.png"
    pix.save(os.path.join(out_dir, name))
    print(f"rendered {name} {pix.width}x{pix.height}")

doc.close()
print("done")
