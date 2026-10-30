"""Antigua and Barbuda: OCR a laws.gov.ag scan with Tesseract 5.4 (eng). Usage: ocr_pages.py PDF OUTDIR FIRST LAST X0 X1 Y0 Y1 [margin]
Renders each page at DPI (env, default 300) and crops to the body column (fractions of the page) so marginal notes are not read.
With the 7th+ args omitted for 'margin', pages are cropped by the fixed fractions; Cap. 300 uses ocr_cap300.py's per-page detection."""
import sys, fitz, subprocess, os
pdf, out, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
X0, X1, Y0, Y1 = [float(v) for v in sys.argv[5:9]]
T = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
d = fitz.open(pdf); os.makedirs(out, exist_ok=True)
for i in range(a, min(b, len(d)) + 1):
    pg = d[i-1]; r = pg.rect
    clip = fitz.Rect(r.width*X0, r.height*Y0, r.width*X1, r.height*Y1)
    png = f'{out}/p{i:03d}.png'
    pg.get_pixmap(dpi=int(os.environ.get('DPI', '300')), colorspace=fitz.csGRAY, clip=clip).save(png)
    subprocess.run([T, png, f'{out}/p{i:03d}', '-l', 'eng', '--psm', '6'], capture_output=True)
    os.remove(png)
