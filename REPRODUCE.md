# How this repository was made (Antigua and Barbuda)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Laws of Antigua and Barbuda | <https://laws.gov.ag> | 2026-10-29 | No licence stated on the site |
| Laws of Antigua and Barbuda: Offences against the Person Act (Cap. 300) | <https://laws.gov.ag/wp-content/uploads/2018/08/cap-300.pdf> | 2026-10-30 | No licence stated on the site |
| Laws of Antigua and Barbuda: Companies Act, 1995 (No. 18 of 1995) | <https://laws.gov.ag/wp-content/uploads/2018/08/a1995-18.pdf> | 2026-10-30 | No licence stated on the site |
| Laws of Antigua and Barbuda: The Evidence (Special Provisions) Act, 2009 (No. 5 of 2009) | <https://laws.gov.ag/wp-content/uploads/2019/02/a2009-5.pdf> | 2026-10-30 | No licence stated on the site |
| Laws of Antigua and Barbuda: The Electronic Evidence Act, 2013 (No. 11 of 2013) | <https://laws.gov.ag/wp-content/uploads/2019/02/a2013-11.pdf> | 2026-10-30 | No licence stated on the site |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution-schedule-3` | Constitution of Antigua and Barbuda, Schedule 3 (Oaths and Affirmations) | 1 | 2026-01-01 to 2026-01-01 |
| `offences-against-the-person` | Offences against the Person Act (Cap. 300) | 1 | 1992-01-01 to 1992-01-01 |
| `companies-act` | Companies Act, 1995 (No. 18 of 1995) | 1 | 1996-03-28 to 1996-03-28 |
| `evidence-special-provisions-act` | The Evidence (Special Provisions) Act, 2009 (No. 5 of 2009) | 1 | 2009-02-19 to 2009-02-19 |
| `electronic-evidence-act` | The Electronic Evidence Act, 2013 (No. 11 of 2013) | 1 | 2013-11-07 to 2013-11-07 |

The build made 5 commits:

| Commits | Kind |
| ---: | --- |
| 5 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 2 laws in the record.
- 7 tags.

## Dates

Each commit is dated at noon (America/Antigua) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: An Antigua and Barbuda Act takes effect on publication in the Gazette unless it names another day or leaves it to a Minister's commencement Order; this record uses the day the law or its commencement Order gives. https://laws.gov.ag

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `b5fd4404b504bb47bf1cd421b558e80407607cb15003403b8ec6059e47d8d15f` (721502 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

5 versions of 5 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 5 history commits and 7 tags (history tip `a09b01cb1083db623b921542db5d8ae08bff61ee`).

## Decisions made by hand

- Scope: only Schedule 3 of the Constitution (as replaced by Act No. 22 of 2025) is included. The only consolidated Constitution online (Cap. 23, Revised Edition 1992) is a scanned image with a 2006 OCR layer full of recognition errors, so it was not used.
- In force 1 January 2026: the Act leaves commencement to a Ministerial Order; the Constitution of Antigua and Barbuda (Amendment) Act, 2025 (Date of Commencement) Order, 2026 (SI 2026 No. 1, Gazette 8 January 2026) appoints 1 January 2026.
- The PDF text layer reads the letter I as the digit 1 in two oaths; it is written as I here. Line breaks within a paragraph were joined.
- OCR: offences-against-the-person (Cap. 300) is text recovered by Tesseract 5.4 from the scan, not copied from the PDF text layer; it has recognition errors (for example misread letters and run-together words) and was spot-checked against the page images only. Marginal notes and part headings are left out; dated 1992-01-01 by the Revised Edition as the PDF states no date.
- OCR: companies-act is text recovered by Tesseract 5.4 from the scan, not copied from the PDF text layer; it has recognition errors and was spot-checked against the page images only. Section numbers the OCR misread were repaired from the running order only where one line start fitted; sections 5, 175, 176, 177, 180, 296, 487, 528, 548 could not be located and are folded into the preceding section. Marginal notes and headings are left out; as enacted (amendments not applied).
- evidence-special-provisions-act: text from the born-digital PDF text layer; page headers, part headings and the arrangement of sections are left out; words broken across a line with a hyphen are joined (the hyphen kept only where the hyphenated form occurs elsewhere in the Act and the joined form does not).
- evidence-special-provisions-act: Oldest version available: the Act as enacted (assented 6 February 2009) and printed in the Official Gazette of 19 February 2009. Section 1(2) leaves commencement to a Notice of the Minister for Legal Affairs, which the source does not give, so the version is dated by the Gazette. The Evidence (Special Provisions) (Amendment) Acts of 2016 (No. 9 and No. 18) and 2017 (No. 15) are not applied.
- electronic-evidence-act: text from the born-digital PDF text layer; page headers, part headings and the arrangement of sections are left out; words broken across a line with a hyphen are joined (the hyphen kept only where the hyphenated form occurs elsewhere in the Act and the joined form does not).
- electronic-evidence-act: the Act has no commencement clause, so it is dated from its publication in the Official Gazette (2013-11-07), the default rule.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the scripts and chose the sources; it did not write or alter any legal text. The OCR statutes are the unedited output of Tesseract 5.4, which is not a language model.
- none
- none
