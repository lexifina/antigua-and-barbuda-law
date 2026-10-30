"""Antigua and Barbuda Companies Act, 1995: OCR text -> numbered sections. Section numbers the OCR misread are repaired only from the running order
(a unique line start between section n-1 and n+1 whose digits differ from n by one character); anything else is reported as missing."""
import re
HEAD = re.compile(r'^(No\. ?18 of 1995\.? .*Companies ?Act,? ?1995\.? ?\d*|.*The ?Companies ?Act,? ?19\d\d\.? ?No\. ?18 of 1995\.?|\d*\s*(?:ANTIGUA|AND|BARBUDA)(?:\s+(?:AND|BARBUDA))*\s*\d*)\s*$', re.I)
NORM = str.maketrans({'S': '5', '$': '5', 'O': '0', 'o': '0', 'l': '1', 'I': '1', 'B': '8', 'Z': '2', 'z': '2', 'G': '6', 'A': '4', 'b': '6', 'q': '9', 'g': '9'})
START = re.compile(r'^[\W_]{0,3}(?:[^\d\s$%&@]+\s){0,4}?([0-9SOIlB$A%&@MRX]{1,4})(?:[.,:]\s*|\s+)(?=[A-Z(])')
WILD = set('%&@MRX$')
def tok(line):
    m = START.match(line)
    if not m: return None
    raw = m.group(1)
    if any(ch in WILD for ch in raw.replace('$', '5', 1) if ch != '$') or ('$' in raw[1:]):
        return raw
    t = raw.translate(NORM)
    return int(t) if t.isdigit() else None
def wild_match(raw, n):
    pat = ''.join('.{1,2}' if ch in '%&@MRX$' else re.escape(ch.translate(NORM)) for ch in raw)
    return isinstance(raw, str) and re.fullmatch(pat, str(n)) is not None
def d1(a, b):
    if isinstance(a, str): return wild_match(a, b)
    a, b = str(a), str(b)
    return len(a) == len(b) and sum(x != y for x, y in zip(a, b)) == 1
def split(L, last_n):
    """Return {n: line index} for n in 1..last_n."""
    pos, p, miss, fixed = {}, 0, [], []
    cand = [(i, tok(l)) for i, l in enumerate(L) if tok(l) is not None]
    def exact(n, frm):
        for i, t in cand:
            if i > frm and not isinstance(t, str) and t == n: return i
    for n in range(1, last_n + 1):
        e = exact(n, p)
        nxt = exact(n + 1, p)
        if e is not None and (nxt is None or e < nxt) and (hi_all := min([x for x in (exact(n + k, p) for k in range(1, 5)) if x is not None] or [len(L)])) >= e: pos[n] = p = e; continue
        hi = min([x for x in (exact(n + k, p) for k in range(1, 5)) if x is not None] or [len(L)])
        within = [i for i, t in cand if p < i < hi and d1(t, n)]
        if len(within) == 1: pos[n] = p = within[0]; fixed.append(n); continue
        miss.append(n)
    return pos, miss, fixed
def clean_lines(text):
    out = []
    for l in text.split('\n'):
        l = re.sub(r'\s+[|!}\/‘’]+$', '', l.rstrip()).strip()
        if HEAD.match(l) and l: continue
        out.append(l)
    return out
def sections(text, last_n):
    L = clean_lines(text)
    pos, miss, fixed = split(L, last_n)
    ns = sorted(pos); res = {}
    for k, n in enumerate(ns):
        j = pos[ns[k + 1]] if k + 1 < len(ns) else len(L)
        chunk = L[pos[n]:j]
        chunk[0] = START.sub('', chunk[0], count=1)
        paras, cur = [], []
        for l in chunk:
            if re.match(r'^(PART [IVXL0-9]+|DIVISION [A-Z0-9]+.*|[A-Z ,&\'-]{10,})$', l):
                if cur: paras.append(' '.join(cur)); cur = []
                continue
            if not l:
                if cur: paras.append(' '.join(cur)); cur = []
                continue
            if cur and re.match(r'^\(\w{1,4}\)\s', l): paras.append(' '.join(cur)); cur = []
            if cur and cur[-1].endswith('-') and re.match(r'^[a-z]', l): cur[-1] += l; continue
            cur.append(l)
        if cur: paras.append(' '.join(cur))
        res[n] = paras
    return res, miss, fixed
