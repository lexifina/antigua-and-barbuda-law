# Antigua and Barbuda: law history in git


The law of Antigua and Barbuda as a git history: one file per section, one commit per version on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every line; `git log` lists every change to a section; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Antigua and Barbuda's national law, which global-law reads at `antigua-and-barbuda/national/acts/`.

**What is in it now:** nine acts, each in one version, in force from 1 January 1992 to 1 September 2026: Schedule 3 of the Constitution (the oaths, as replaced by Act No. 22 of 2025); the Offences against the Person Act (Cap. 300) and the Companies Act, 1995, as OCR text of the official scans; the Evidence (Special Provisions) Act, 2009 and the Electronic Evidence Act, 2013; and four Acts of 2025 and 2026 (the National Oversight Committee on Financial Action Act, the Antigua and Barbuda Festivals Commission Act, the Special Economic Zone (Amendment) Act and the Airport Administration Charge (Amendment) Act). [`REPRODUCE.md`](REPRODUCE.md) lists every act with its versions and the decisions made for each.

Each act has its own folder, with a `README.md` listing its provisions: Schedule 3 has one file per oath (`constitution-schedule-3/oath-office.md` is the Oath of Office), the four older acts one file per section (`electronic-evidence-act/sec-014.md` is section 14 of the Electronic Evidence Act; the two OCR acts name theirs `art-001.md` and so on), and the four Acts of 2025 and 2026 one file, `full-text.md`, with the whole enacted text.

The text is in English, the official language, as the official site prints it; part headings and the arrangement of sections are left out of the acts split by section.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to the Oath of Office in Schedule 3 of the Constitution | `git log -p --word-diff -- constitution-schedule-3/oath-office.md` |
| Which law wrote each line of the Oath of Office? | `git blame constitution-schedule-3/oath-office.md` |
| Every version of Schedule 3, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- constitution-schedule-3 ':!*/README.md'` |
| The Oath of Office as in force on 1 June 2026 | `python tools/on.py 2026-06-01 constitution-schedule-3 oath-office` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about the law of Antigua and Barbuda](https://global-law.lexifina.com/v1/try_claude?country=antigua-and-barbuda)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=antigua-and-barbuda)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=electronic+record&jurisdictions=antigua-and-barbuda)**: a search of the law of Antigua and Barbuda for "electronic record", returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add antigua-and-barbuda/national/acts
python3 tools/law.py show 2026-01-01 antigua-and-barbuda/national/acts/constitution-schedule-3/oath-office.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, America/Antigua, on the day the version took effect, and carries it in its `In-force:` trailer:

- an Act takes effect on its publication in the Gazette unless it names another day or leaves the day to a Minister's order or notice; the record uses the day the Act or its order gives (Schedule 3: 1 January 2026, by the Date of Commencement Order, SI 2026 No. 1; the Airport Administration Charge (Amendment) Act: 1 September 2026, by its section 1(2));
- where the day is left to a Minister's notice that the source does not give, the Act is dated by its publication: the Evidence (Special Provisions) Act by the Gazette of 19 February 2009, the Companies Act by the publication date it prints, 28 March 1996;
- the Offences against the Person Act is dated 1 January 1992 by the Revised Edition of the Laws, as its PDF states no date.

Two versions are credited to the Act that made them (`Act No. 11 of 2013`, `Act No. 22 of 2025`). The other seven are the oldest version the site publishes as text and are credited to the publisher, `Government of Antigua and Barbuda (laws.gov.ag)`; each commit message says which publication it holds.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before and compares it with the corpus: 9 versions of 9 acts, 0 mismatches. The results are in [`REPRODUCE.md`](REPRODUCE.md).
- Every commit's trailers parse, and main has no merge commits.
- `tools/build.py` gives the same commit hashes from the same corpus, whose sha256 is in `data/corpus.sha256`; no second build has been compared yet.
- History is append-only: `tools/append.py` adds new acts and versions on top and never rewrites a published commit.

## What it does not show

- **Most of the law.** Only these nine acts: no other statute, no subsidiary legislation and no case law.
- **The Constitution as a whole.** Only Schedule 3 is here; the one consolidated Constitution online (Cap. 23, Revised Edition 1992) is a scan whose text layer is too garbled to use, and the Schedule 3 that the 2025 Act replaced is not available as text.
- **Amendments.** Each act is in one version: Cap. 300 as printed in the 1992 Revised Edition (later amendments, such as the Offences against the Person (Amendment) Act, 2013, are not applied), the Companies Act as enacted (its amendments of 2004, 2007, 2022 and 2024 are not), and the Evidence (Special Provisions) Act without its amendments of 2016 and 2017.
- **A proofread text of the two OCR acts.** The Offences against the Person Act and the Companies Act are Tesseract's reading of scans, spot-checked against the page images but not proofread, so they have misread letters and run-together words; in the Companies Act, sections 5, 175-177, 180, 296, 487, 528 and 548 sit inside the section before them. For anything that matters, read the scan.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Laws of Antigua and Barbuda](https://laws.gov.ag) (Government of Antigua and Barbuda) | Official legislation site | no dated versions: Acts as enacted, and the 1992 Revised Edition, as PDF | Born-digital PDFs for the Acts of 2009 to 2026; scans with no usable text layer for Cap. 300 and the Companies Act, read here by OCR |

## Licence

See [`LICENSE`](LICENSE). The site states no licence for the legal text, and the Government of Antigua and Barbuda does not endorse this repository; Lexifina's own contributions (the arrangement of the history, the commit messages and the tools) are dedicated to the public domain under CC0 1.0.

No AI model wrote, translated or corrected legal text, and none runs at build time; the scripts were written by an AI model, which also chose the sources and some of the acts and reviewed their dates and scope. The OCR is the unedited output of Tesseract 5.4, which is not a language model (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
