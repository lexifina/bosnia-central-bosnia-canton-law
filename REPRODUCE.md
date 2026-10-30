# How this repository was made (Central Bosnia Canton)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Vlada Srednjobosanskog kantona: Službene novine Srednjobosanskog kantona (each issue as a PDF) | <https://sbk-ksb.gov.ba/index.php/dokumenti> | 2026-10-30 | Official text, not protected: Zakon o autorskom i srodnim pravima BiH (Sl. glasnik BiH 63/10), čl. 8(1)(b) |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `o-podsticanju-razvoja-male-privrede-srednjobosanskog-kantona` | Zakon o podsticanju razvoja male privrede Srednjobosanskog kantona | 1 | 2022-05-18 to 2022-05-18 |
| `o-muzejskoj-djelatnosti` | Zakon o muzejskoj djelatnosti | 1 | 2022-07-22 to 2022-07-22 |
| `o-upotrebi-znakovnoga-jezika-u-srednjobosanskom-kantonu` | Zakon o upotrebi znakovnoga jezika u Srednjobosanskom kantonu | 1 | 2022-09-17 to 2022-09-17 |
| `o-mirnom-okupljanju` | Zakon o mirnom okupljanju | 1 | 2024-09-13 to 2024-09-13 |
| `o-javnim-priredbama` | Zakon o javnim priredbama | 1 | 2024-09-13 to 2024-09-13 |
| `o-putevima-srednjobosanskog-kantona` | Zakon o putevima Srednjobosanskog kantona | 1 | 2025-10-23 to 2025-10-23 |

The build made 6 commits:

| Commits | Kind |
| ---: | --- |
| 6 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `buducnost`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 6 laws in the record.
- 12 tags.

## Dates

Each commit is dated at noon (Europe/Sarajevo) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: A law takes effect on the day its own final article names, counted from its publication in the Službene novine Srednjobosanskog kantona. https://sbk-ksb.gov.ba/index.php/dokumenti

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `edc4989cf2f962915965149bf3eba29a4a1c3afbe879ea33a7e51b29eeb99cfe` (263562 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

6 versions of 6 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Laws part 1: laws the Assembly of Central Bosnia Canton published in the Službene novine Srednjobosanskog kantona from 2022-01-01 to 2026-10-09 (every issue on sbk-ksb.gov.ba in that span; laws are checked against every later issue) that no later law in those issues amends, repeals or consolidates: a law is left out when any later amending law or consolidated text cites its gazette number next to a word of its subject, or any later law cites it next to words of repeal. Amending and budget laws are left out. Each is its text as enacted, dated the issue date plus the days its final article names, credited to the law; or, where the Legislative Committee of the Assembly has published an official consolidated text (prečišćeni tekst) that nothing later touches, that text, dated the day it was published (it applies from its publication, as its last article says). Amendments published after 2026-10-09, and decisions of the Constitutional Court, are not in the record.
- Each issue prints every act three times, in its Bosnian, Croatian and Serbian (Cyrillic) editions, under one act number; the Bosnian edition is kept (the Croatian one, then the Serbian one, only where no Bosnian edition of the act was found).
- A law proclaimed by a decree of the Speaker of the Assembly (Ukaz o proglašenju zakona), printed as its own act just before the law, is the text of the law without the decree: the decree is not part of the law and is left out, so such a law has no preamble (uvod).
- Units: uvod.md is the preamble (legal basis and adoption), naslov.md the title, clan-NNN.md each article with its heading (chapter headings stay with the article after them), potpis.md the signature block.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: the text is read from the gazette PDFs' text layer by a deterministic parser; no model output is legal text.
