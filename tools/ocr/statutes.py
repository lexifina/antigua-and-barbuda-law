"""Antigua and Barbuda core statutes from Tesseract OCR of laws.gov.ag scans: merge into ../corpus.json. Usage: python statutes.py cap300 <body.txt> <pdf>"""
import hashlib, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from cap300 import sections
import companies as _co
here = Path(__file__).resolve().parent.parent
c = json.loads((here / 'corpus.json').read_text(encoding='utf8'))
def put(act, src, dec):
    c['acts'] = [x for x in c['acts'] if x['slug'] != act['slug']] + [act]
    c['sources'] = [x for x in c['sources'] if x['url'] != src['url']] + [src]
    c['decisions'] = [x for x in c['decisions'] if not x.startswith(dec[:40])] + [dec]
    (here / 'corpus.json').write_text(json.dumps(c, ensure_ascii=False, indent=1) + '\n', encoding='utf8', newline='\n')
if sys.argv[1] == 'cap300':
    secs = sections(Path(sys.argv[2]).read_text(encoding='utf8'))
    url = 'https://laws.gov.ag/wp-content/uploads/2018/08/cap-300.pdf'
    units = {'art-%03d' % n: {'label': 'Section %d' % n, 'kind': 'article', 'text': '\n'.join(['# Section %d' % n] + p) + '\n'} for n, p in secs.items()}
    sha = hashlib.sha256(Path(sys.argv[3]).read_bytes()).hexdigest()
    note = 'OCR text (Tesseract 5.4, English, 300 dpi) of the laws.gov.ag scan of Cap. 300; not the site\'s own garbled OCR layer. Marginal notes, part headings and the arrangement of sections were left out. The Chapter as printed in the Revised Edition; later amendments (for example the Offences against the Person (Amendment) Act, 2013) are not applied. The PDF states no date; the version is dated 1992-01-01 by the Revised Edition of the Laws.'
    act = {'slug': 'offences-against-the-person', 'short': 'Offences against the Person Act', 'title': 'Offences against the Person Act (Cap. 300)', 'url': url, 'first_law': None, 'earlier_laws': [],
           'versions': [{'from': '1992-01-01', 'source_url': url, 'sha256': sha, 'units': units, 'credits': {}, 'note': note}]}
    src = {'name': 'Laws of Antigua and Barbuda: Offences against the Person Act (Cap. 300)', 'url': url, 'retrieved': '2026-10-30', 'licence': 'No licence stated on the site', 'notes': 'Scanned PDF; text recovered by Tesseract OCR.'}
    put(act, src, 'OCR: offences-against-the-person (Cap. 300) is text recovered by Tesseract 5.4 from the scan, not copied from the PDF text layer; it has recognition errors (for example misread letters and run-together words) and was spot-checked against the page images only. Marginal notes and part headings are left out; dated 1992-01-01 by the Revised Edition as the PDF states no date.')
    print(len(units))

if sys.argv[1] == 'companies':
    txt = Path(sys.argv[2]).read_text(encoding='utf8'); txt = txt[txt.index('ENACTED'):]
    secs, miss, fixed = _co.sections(txt, 550)
    url = 'https://laws.gov.ag/wp-content/uploads/2018/08/a1995-18.pdf'
    units = {'art-%03d' % n: {'label': 'Section %d' % n, 'kind': 'article', 'text': chr(10).join(['# Section %d' % n] + p) + chr(10)} for n, p in secs.items()}
    sha = hashlib.sha256(Path(sys.argv[3]).read_bytes()).hexdigest()
    ml = ', '.join(str(m) for m in miss)
    note = ('OCR text (Tesseract 5.4, English, 400 dpi) of the laws.gov.ag scan of the Companies Act, 1995 (No. 18 of 1995) as enacted; not the garbled OCR layer. Marginal notes, part and division headings, the arrangement of sections and any tables are left out. '
            'Later amendments (Acts of 2004, 2007, 2022 and 2024) are not applied. Dated 1996-03-28, the publication date the Act prints; the Act comes into operation on a day the Minister appoints by Gazette notice, which is not confirmed here. '
            'Sections %s have no number the OCR could read, so their text sits inside the section printed before them.' % ml)
    act = {'slug': 'companies-act', 'short': 'Companies Act', 'title': 'Companies Act, 1995 (No. 18 of 1995)', 'url': url, 'first_law': None, 'earlier_laws': [],
           'versions': [{'from': '1996-03-28', 'source_url': url, 'sha256': sha, 'units': units, 'credits': {}, 'note': note}]}
    src = {'name': 'Laws of Antigua and Barbuda: Companies Act, 1995 (No. 18 of 1995)', 'url': url, 'retrieved': '2026-10-30', 'licence': 'No licence stated on the site', 'notes': 'Scanned PDF (292 pages); text recovered by Tesseract OCR.'}
    put(act, src, 'OCR: companies-act is text recovered by Tesseract 5.4 from the scan, not copied from the PDF text layer; it has recognition errors and was spot-checked against the page images only. Section numbers the OCR misread were repaired from the running order only where one line start fitted; sections %s could not be located and are folded into the preceding section. Marginal notes and headings are left out; as enacted (amendments not applied).' % ml)
    print(len(units), 'sections; missing', miss, 'repaired', fixed)
