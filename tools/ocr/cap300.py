"""Antigua and Barbuda Offences against the Person Act (Cap. 300): OCR text (ocr_cap300.py output in OCRDIR) -> units. Deterministic."""
import re, sys
def sections(body):
    L = body.split('\n'); st = []
    for i, l in enumerate(L):
        m = re.match(r'^[\W_]{0,4}(?:[a-z0-9]\s)?(\d{1,3}|JV|JI7)[.,]\s+(?=[A-Z(])', l)
        if m: st.append(i)
    assert len(st) == 73, len(st)
    out = {}
    for n, i in enumerate(st, 1):
        j = st[n] if n < len(st) else len(L)
        chunk = L[i:j]
        chunk[0] = re.sub(r'^[\W_]{0,4}(?:[a-z0-9]\s)?(\d{1,3}|JV|JI7)[.,]\s+', '', chunk[0])
        paras, cur = [], []
        for l in chunk:
            l = re.sub(r'\s+[|!}\/‘’]+$', '', l.rstrip()).strip()
            if re.match(r'^(PART [IVXL]+|[A-Z ,&\'-]{8,})$', l):  # part headings
                if cur: paras.append(' '.join(cur)); cur = []
                continue
            if not l:
                if cur: paras.append(' '.join(cur)); cur = []
                continue
            if cur and re.match(r'^\(\w{1,4}\)\s', l): paras.append(' '.join(cur)); cur = []
            if cur and cur[-1].endswith('-') and re.match(r'^[a-z]', l): cur[-1] = cur[-1] + l; continue
            cur.append(l)
        if cur: paras.append(' '.join(cur))
        out[n] = paras
    return out
