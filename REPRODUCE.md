# How this repository was made (Antigua and Barbuda)

This file is written by the build on 2026-11-03, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Laws of Antigua and Barbuda | <https://laws.gov.ag> | 2026-10-29 | No licence stated on the site |
| Laws of Antigua and Barbuda: Offences against the Person Act (Cap. 300) | <https://laws.gov.ag/wp-content/uploads/2018/08/cap-300.pdf> | 2026-10-30 | No licence stated on the site |
| Laws of Antigua and Barbuda: Companies Act, 1995 (No. 18 of 1995) | <https://laws.gov.ag/wp-content/uploads/2018/08/a1995-18.pdf> | 2026-10-30 | No licence stated on the site |
| Laws of Antigua and Barbuda: The Evidence (Special Provisions) Act, 2009 (No. 5 of 2009) | <https://laws.gov.ag/wp-content/uploads/2019/02/a2009-5.pdf> | 2026-10-30 | No licence stated on the site |
| Laws of Antigua and Barbuda: The Electronic Evidence Act, 2013 (No. 11 of 2013) | <https://laws.gov.ag/wp-content/uploads/2019/02/a2013-11.pdf> | 2026-10-30 | No licence stated on the site |
| Laws of Antigua and Barbuda: Antigua and Barbuda Festivals Commission Act, 2026 | <https://laws.gov.ag/wp-content/uploads/2026/07/No.-2-of-2026-Antigua-and-Barbuda-Festivals-Commission-Acr-2026.pdf> | 2026-11-03 | No licence stated on the site |
| Laws of Antigua and Barbuda: National Oversight Committee on Financial Action Act, 2025 | <https://laws.gov.ag/wp-content/uploads/2026/01/No.-17-of-2025-National-Oversight-Committee-on-Financial-Action-Act-2025.pdf> | 2026-11-03 | No licence stated on the site |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution-schedule-3` | Constitution of Antigua and Barbuda, Schedule 3 (Oaths and Affirmations) | 1 | 2026-01-01 to 2026-01-01 |
| `offences-against-the-person` | Offences against the Person Act (Cap. 300) | 1 | 1992-01-01 to 1992-01-01 |
| `companies-act` | Companies Act, 1995 (No. 18 of 1995) | 1 | 1996-03-28 to 1996-03-28 |
| `evidence-special-provisions-act` | The Evidence (Special Provisions) Act, 2009 (No. 5 of 2009) | 1 | 2009-02-19 to 2009-02-19 |
| `electronic-evidence-act` | The Electronic Evidence Act, 2013 (No. 11 of 2013) | 1 | 2013-11-07 to 2013-11-07 |
| `antigua-and-barbuda-festivals-commission-act-2026` | Antigua and Barbuda Festivals Commission Act, 2026 (No. 2 of 2026) | 1 | 2026-04-16 to 2026-04-16 |
| `national-oversight-committee-on-financial-action-act-2025` | National Oversight Committee on Financial Action Act, 2025 (No. 17 of 2025) | 1 | 2025-10-30 to 2025-10-30 |

The build made 7 commits:

| Commits | Kind |
| ---: | --- |
| 7 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-11-03.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 2 laws in the record.
- 9 tags.

## Dates

Each commit is dated at noon (America/Antigua) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: An Antigua and Barbuda Act takes effect on publication in the Gazette unless it names another day or leaves it to a Minister's commencement Order; this record uses the day the law or its commencement Order gives. https://laws.gov.ag

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `c41b6e48b833537b1a5386a970eaa2b4bc907f072ee8ea3bb0230182fd06353b` (787660 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `35388bee5aa05369f7da68f5a8fa015ea8d442b8`, `check.py` `5d719354ea4c62d240c93d2cae446307d81d9e81`, `on.py` `aff48cf1b68d50c7ba8f399ca32261871c301824`.
- Python 3.14.4; git version 2.53.0.

## Checks

Not yet run for this build.

A second build from the same corpus into an empty folder gave identical hashes for all 7 history commits and 9 tags (history tip `6220a633ddc8a80aac0c72dc669bf50cb3495444`).

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
- The Antigua and Barbuda Festivals Commission Act, 2026 is a single-file act: all 50 sections and the schedule are in one unit because the complete text is preserved without an unverified section split.
- The version is dated 2026-04-16, the date printed on the Act as its Official Gazette publication date; the Act gives no separate commencement date.
- The unit is extracted from the official PDF text layer beginning at ENACTED and ending before the parliamentary signatures; repeated running page headers and blank lines are excluded.
- The National Oversight Committee on Financial Action Act, 2025 is a single-file act containing all 15 sections.
- The version is dated 2025-10-30, the date printed on the Act as its Official Gazette publication date; the Act gives no separate commencement date.
- The unit is extracted from the official PDF text layer beginning at ENACTED and ending before the parliamentary signatures; repeated running page headers and blank lines are excluded.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the scripts and chose the sources; it did not write or alter any legal text. The OCR statutes are the unedited output of Tesseract 5.4, which is not a language model.
- none
- none
- A model selected the Act and reviewed dates and scope; no model wrote legal text.
- A model selected the Act and reviewed dates and scope; no model wrote legal text.
