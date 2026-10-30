import sys, fitz, subprocess, os, numpy as np
pdf, out, y0 = sys.argv[1], sys.argv[2], float(sys.argv[3])
rng = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else None
BW = 360
T = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
d = fitz.open(pdf); os.makedirs(out, exist_ok=True)
for i in range(1, len(d)+1):
    if rng and not rng[0] <= i <= rng[1]: continue
    pg = d[i-1]; r = pg.rect
    small = pg.get_pixmap(dpi=100, colorspace=fitz.csGRAY, clip=fitz.Rect(0, r.height*y0, r.width, r.height))
    a = np.frombuffer(small.samples, dtype=np.uint8).reshape(small.height, small.width)
    cnt = (a < 140).sum(axis=0); ink = cnt > 6
    runs, s, gap = [], None, 0
    for x, v in enumerate(ink):
        if v:
            if s is None: s = x
            last = x; gap = 0
        elif s is not None:
            gap += 1
            if gap >= 5: runs.append((s, last)); s = None
    if s is not None: runs.append((s, last))
    lo, hi = runs[0][0], runs[-1][1]
    sm = np.convolve(cnt, np.ones(3)/3, mode='same')
    if i % 2 == 0:
        w = range(max(0, hi-385), hi-335); cut = min(w, key=lambda x: sm[x]); body = (cut, hi)
    else:
        w = range(lo+335, min(len(sm)-1, lo+385)); cut = min(w, key=lambda x: sm[x]); body = (lo, cut)
    sc = r.width / small.width
    clip = fitz.Rect(max(0, (body[0]-6)*sc), r.height*y0, min(r.width, (body[1]+6)*sc), r.height)
    png = f'{out}/p{i:03d}.png'
    pg.get_pixmap(dpi=300, colorspace=fitz.csGRAY, clip=clip).save(png)
    subprocess.run([T, png, f'{out}/p{i:03d}', '-l', 'eng', '--psm', '6'], capture_output=True)
    os.remove(png)
    print(i, runs, flush=True)
