# Central Bosnia Canton: law history in git

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is the law of Central Bosnia Canton, Federation of Bosnia and Herzegovina, Bosnia and Herzegovina, which global-law reads at `bosnia-and-herzegovina/federation/central-bosnia-canton/acts/`.

The law of Central Bosnia Canton (Srednjobosanski kanton / Kanton Središnja Bosna), one of the ten cantons of the Federation of Bosnia and Herzegovina, as a git history: one file per article, one commit per law, dated the day it took effect, with the law as the commit's author. `git log` lists every change to an article; checking out a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ba-06/`. The Federation's own law is in [lexifina/bosnia-federation-law](https://github.com/lexifina/bosnia-federation-law), the state's in [lexifina/bosnia-and-herzegovina-law](https://github.com/lexifina/bosnia-and-herzegovina-law).

Each issue of the gazette prints every act in Bosnian, Croatian and Serbian (Cyrillic) editions; the Bosnian edition is the one kept here (the Croatian one only where no Bosnian edition of an act was found).

## What this repository holds

The canton publishes the Službene novine Srednjobosanskog kantona on its site for 2013 to 2026; every issue listed there is read. Of the 91 Assembly laws the reader finds in them, 36 are here (from 2018), as:

- the law as enacted, dated the day it took effect; where later laws in the gazette amend it and no official consolidated text has been published since, it is marked `amended, not consolidated` and the amending laws are named (0 laws added on 2026-11-09);
- amending laws, each as an act of its own (0 added on 2026-11-09);
- official consolidated texts (prečišćeni tekst), dated the day of their issue (0 added on 2026-11-09).

The first build (October 2026) holds its laws in folders named after them; laws added later are in `zakon/<year>/sn<issue>-<act number>/`, indexed in [registry/ACTS.md](registry/ACTS.md) and [registry/data/acts.json](registry/data/acts.json).

Held back, with the reason, in [data/held.json](data/held.json) (55 laws): budget laws and laws amending them (temporary), texts that do not split into articles, laws whose in-force clause cannot be read, and texts a second, independent PDF reader does not confirm. Gazette years whose issues the reader cannot yet read (2013, 2014, 2015) are listed in data/held.json with the reason; their laws are not in the record. 15 issues could not be read or dated and are listed there too.

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
- Whether a law was later amended or repealed is judged from every later law in the scanned issues (a law is marked `amended, not consolidated` when a later amending law cites its gazette number next to a word of its subject, or any later law cites it next to words of repeal). Decisions of the Constitutional Court are not checked.
- Health checks: no merge commits, commit dates never go backwards, nothing dated in the future, and every commit's trailers parse.

## What "author" means

The author of a commit is the law that made it, named by its gazette number, with an e-mail address that cannot exist (`<key>@sbk-ksb.gov.ba.invalid`). The committer is always Lexifina.




## Freshness

<!-- freshness-summary -->
Checked against the official sources: None; 0% of acts verified in the last 7 days, 0% in the last 30 ([data/freshness.json](data/freshness.json)).
<!-- /freshness-summary -->

`python tools/freshness.py <act>` gives an act's status, its last check and the official link. A refresh runner re-reads the canton's list of gazette issues every day (at most two requests a second), reads every new issue, appends new laws and writes these files; [data/status.json](data/status.json) says whether updates are running and whether the source is answering. Acts a later law amends with no official consolidated text are marked `amended, not consolidated` and name the amending laws ([registry/data/acts.json](registry/data/acts.json)); laws and gazette years held back are listed with the reason in [data/held.json](data/held.json), and laws published but not yet in force in [data/pending.json](data/pending.json). Statuses and fields: [data/freshness.json](data/freshness.json).

## Limits

This is not an official publication. The binding text is the one published in the Službene novine Srednjobosanskog kantona. Only the laws listed in `data/versions.json` and `registry/data/acts.json` are included; amendments published after the last issue read are not in the record.
