"""Antigua and Barbuda Companies Act, 1995 (No. 18 of 1995): Tesseract OCR of the laws.gov.ag scan with the marginal notes cropped out.
Even printed pages carry the margin on the left, odd pages on the right. Usage: ocr_companies.py PDF OUTDIR FIRST LAST"""
import sys, fitz, subprocess, os, numpy as np
pdf, out, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
T = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
d = fitz.open(pdf); os.makedirs(out, exist_ok=True)
Y0 = 0.05
for i in range(a, min(b, len(d)) + 1):
    pg = d[i-1]; r = pg.rect
    s = pg.get_pixmap(dpi=100, colorspace=fitz.csGRAY, clip=fitz.Rect(0, r.height*Y0, r.width, r.height*0.97))
    arr = np.frombuffer(s.samples, dtype=np.uint8).reshape(s.height, s.width)
    cnt = (arr < 140).sum(axis=0); ink = cnt > 6
    runs, st, g = [], None, 0
    for x, v in enumerate(ink):
        if v:
            if st is None: st = x
            last = x; g = 0
        elif st is not None:
            g += 1
            if g >= 12: runs.append((st, last)); st = None
    if st is not None: runs.append((st, last))
    if not runs: continue
    sm = np.convolve(cnt, np.ones(3)/3, mode='same')
    lo, hi = runs[0][0], runs[-1][1]
    if len(runs) >= 2:
        body = max(runs, key=lambda t: t[1]-t[0])          # margin and body separated by a gap
    elif (i % 2) == 1:                                      # odd page: margin on the right; cut at the valley after the body
        w = range(lo+350, min(len(sm)-1, lo+430)); cut = min(w, key=lambda x: sm[x]); body = (lo, cut)
    else:
        body = (lo, hi)
    sc = r.width / s.width
    clip = fitz.Rect(max(0, (body[0]-5)*sc), r.height*Y0, min(r.width, (body[1]+5)*sc), r.height*0.97)
    png = f'{out}/p{i:03d}.png'
    pg.get_pixmap(dpi=int(os.environ.get('DPI', '400')), colorspace=fitz.csGRAY, clip=clip).save(png)
    subprocess.run([T, png, f'{out}/p{i:03d}', '-l', 'eng', '--psm', '6'], capture_output=True)
    os.remove(png)
