# Central Bosnia Canton: law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the law of Central Bosnia Canton, Federation of Bosnia and Herzegovina, Bosnia and Herzegovina, which global-law reads at `bosnia-and-herzegovina/federation/central-bosnia-canton/acts/`.

The law of Central Bosnia Canton (Srednjobosanski kanton / Kanton Središnja Bosna), one of the ten cantons of the Federation of Bosnia and Herzegovina, as a git history: one file per article, one commit per law, dated the day it took effect, with the law as the commit's author. `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ba-06/`. The Federation's own law is in [lexifina/bosnia-federation-law](https://github.com/lexifina/bosnia-federation-law), the state's in [lexifina/bosnia-and-herzegovina-law](https://github.com/lexifina/bosnia-and-herzegovina-law).

Each issue of the gazette prints every act in Bosnian, Croatian and Serbian (Cyrillic) editions; the Bosnian edition is the one kept here (the Croatian one only where no Bosnian edition of an act was found).

## What this repository holds

Laws the Assembly of Central Bosnia Canton published in the Službene novine Srednjobosanskog kantona from 2022 to October 2026 that no later law in those issues amends, repeals or consolidates, each in one of two forms:

- the law as enacted, dated the day it took effect, which is therefore also its current text; or
- an official consolidated text (prečišćeni tekst) published in the gazette, dated the day it was published. Earlier versions of these laws are not in the record yet.

Not included yet: the Constitution of Central Bosnia Canton; laws that were later amended; amending and budget laws; laws before 2022; laws the parser could not read cleanly (the Law on salaries and allowances in the authorities of the Canton, 12/25, whose pay-grade tables the two PDF readers order differently; the Law on the recognition of foreign educational documents, 8/26, whose annexed request forms are printed around its signature block).

## Source

Central Bosnia Canton (Srednjobosanski kanton / Kanton Središnja Bosna), <https://sbk-ksb.gov.ba/index.php/dokumenti>: every issue of the Službene novine Srednjobosanskog kantona as a PDF with a text layer.

## Dates

- Each law's commit is dated at **noon, Europe/Sarajevo, on the day it took effect**: the issue's date plus the days the law's own final article names (most often the eighth day after publication); a consolidated text on the day of its issue.
- Versions that take effect after the retrieval day would go on the `buducnost` branch, never merged into `main`.

## Files

`<law>/clan-001.md` is Član 1, `clan-005-a.md` Član 5a. `uvod.md` holds the preamble (the legal basis and the Assembly's adoption) where the law has one, `naslov.md` the title, `potpis.md` the signature block. Most laws are printed after a decree of the Speaker of the Assembly proclaiming them (Ukaz o proglašenju zakona, its own act in the gazette); the decree is not part of the law and is not included. Chapter headings stay in the file of the article they stand before. One paragraph per line.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before; both must match `corpus.json`.
- The letters and digits of every law equal those of the gazette issue, read independently with a different PDF reader, from the first paragraph to the last article; the signature block's lines all occur in it.
- Whether a law was later amended or repealed is judged from every later law in the scanned issues (a law is left out when a later amending law cites its gazette number next to a word of its subject, or any later law cites it next to words of repeal). Decisions of the Constitutional Court are not checked.
- Health checks: no merge commits, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse.

## What "author" means

The author of a commit is the law that made it, named by its gazette number, with an e-mail address that cannot exist (`<key>@sbk-ksb.gov.ba.invalid`). The committer is always Lexifina.

## Limits

This is not an official publication. The binding text is the one published in the Službene novine Srednjobosanskog kantona. Only the laws listed in `data/versions.json` are included; amendments published after the last issue read are not in the record.
