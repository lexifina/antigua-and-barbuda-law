# Antigua and Barbuda: law history in git

The law of Antigua and Barbuda (AG) as a git history: one file per provision, one commit per law on the day it took effect, and the law that made the change as the commit author. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ag/`.

**First build, deliberately small.** Language: English (the official language).

| Folder | Text | Versions | History |
| --- | --- | ---: | --- |
| `constitution-schedule-3/` | Constitution of Antigua and Barbuda, Schedule 3 (Oaths and Affirmations) | 1 | As replaced by the Constitution of Antigua and Barbuda (Amendment) Act, 2025 (No. 22 of 2025), in force 1 January 2026 |
| `offences-against-the-person/` | Offences against the Person Act (Cap. 300) | 1 | **OCR text.** Revised Edition text as scanned; dated 1992-01-01 by the Revised Edition (the PDF states no date); later amendments are not applied |
| `companies-act/` | Companies Act, 1995 (No. 18 of 1995) | 1 | **OCR text.** As enacted (assented 8 March 1996, published 28 March 1996); later amendments (2004, 2007, 2022, 2024) are not applied; sections 5, 175-177, 180, 296, 487, 528 and 548 have no number the OCR could read, so their text sits inside the section printed before them |
| `evidence-special-provisions-act/` | The Evidence (Special Provisions) Act, 2009 (No. 5 of 2009) | 1 | As enacted, from the born-digital PDF (not OCR); dated by its Gazette of 19 February 2009, because it came into force on a day appointed by Notice that the source does not give; the amending Acts of 2016 and 2017 are not applied; there is no section 38 in the Act as printed |
| `electronic-evidence-act/` | The Electronic Evidence Act, 2013 (No. 11 of 2013) | 1 | As enacted, from the born-digital PDF (not OCR); in force on publication in the Gazette, 7 November 2013 |

**OCR text.** The Offences against the Person Act and the Companies Act are scans with no usable text layer, so Lexifina ran Tesseract 5.4 (English) over the page images of laws.gov.ag and published that output. It has recognition errors (misread letters, run-together words, stray marks); it was spot-checked against the scan but not proofread, so for anything that matters read the original scan. Marginal notes, part headings and the arrangement of sections are left out. The two evidence Acts are copied from the PDF text layer; a word split across a line with a hyphen is joined, and the 2009 Act's Schedule (a table) is kept line by line with its columns separated by " | ". Antigua and Barbuda has no penal, civil or commercial code; the Offences against the Person Act is the nearest penal statute included so far, and the Companies Act, 1995 is the commercial law. Some section numbers in the Companies Act were misread by the OCR; where exactly one line start fitted the running order the number was restored from the order, which is stated in the corpus notes.

**Why the Constitution is still not here.** The only consolidated Constitution (Cap. 23, Revised Edition 1992) on [laws.gov.ag](https://laws.gov.ag) is a scanned image with a 2006 OCR layer full of recognition errors, so it is left out; the OCR of the statutes above covers it only for those Acts. Schedule 3 comes from the 2025 Act, a born-digital PDF, and its commencement day (1 January 2026) from the Date of Commencement Order, 2026 (SI 2026 No. 1). The text this Schedule replaced is not available in a usable form, so the history starts at this version.

**Source:** [Laws of Antigua and Barbuda](https://laws.gov.ag), official, retrieved 29 October 2026. See `LICENSE` and `REPRODUCE.md`.

Dates are the day the change took effect. This repository is not legal advice; for anything that matters, read the original.
