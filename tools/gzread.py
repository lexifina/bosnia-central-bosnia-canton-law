"""FBiH canton gazette (two-column PDFs) -> lines in reading order. Private.

pymupdf spans; each line is placed by its baseline (span origin), not its bbox top (Cambria's bbox runs high).
Fragments of one justified line on the same baseline in the same column are joined. Running headers (above the
first text baseline, y < 55) are dropped. A line crossing the middle of the page is full width: it closes the
two-column section above it.
"""
import re
import unicodedata

import pymupdf

HEAD_BAND = 90  # running headers sit within the top 90 pt (baselines 14-57 in the issues of 2022-2026)
# a running header line, as a whole span: the gazette's name, the page line, the date
HEADER = re.compile(r'(?i)^\s*(?:(?:Broj|Број)\s*\d+\s*\W{0,3}\s*(?:stranica|страница|strana|страна)?\s*\d*'
                    r'|[SС][LЛ][UУ][ŽЖ][BБ][EЕ]N[EЕ] N[OО]V[IИ]N[EЕ]|СЛУЖБЕНЕ НОВИНЕ|CЛУЖБЕНЕ НОВИНЕ'
                    r'|Službene novine\s+(?:Srednjobosanskog|Kantona)[\w\s/]*'
                    r'|(?:SREDNJOBOSANSKOG|СРЕДЊОБОСАНСКОГ) (?:KANTONA|КАНТОНА)|KANTONA SREDIŠNJA BOSNA'
                    r'|Kantona Središnja Bosna\s*/.*|\d{1,4}|\d{1,2}\.\s*[^\W\d_]*\s*\d{0,4}\.?\s*(?:godine|године|годинe)?'
                    r'|[^\W\d_]{3,}\s+\d{4}\.\s*(?:godine|године|годинe))\s*$')


def clean(s):
    s = unicodedata.normalize('NFC', s.replace('\xa0', ' ').replace('­', '').replace('\t', ' '))
    return re.sub(r' {2,}', ' ', s).strip()


def gutter(spans, width):
    """The x of the column gutter: the point near the middle that the fewest body spans cross (None when the page is
    one column: every candidate point is crossed by more than a third of the spans)."""
    best, bx = None, None
    for x in range(int(width * 0.40), int(width * 0.60)):
        n = sum(1 for s in spans if s[0] < x < s[1])
        if best is None or n < best:
            best, bx = n, [x]
        elif n == best and x == bx[-1] + 1:
            bx.append(x)
    if best is None or best > max(3, len(spans) / 3):
        return None
    return (bx[0] + bx[-1]) / 2


def page_lines(page):
    """Each span is placed on its own (pymupdf sometimes joins the two columns' spans on one baseline into one line):
    a span crossing the gutter is full width; others go to the column of their side."""
    width = page.rect.width
    raw = []
    for b in page.get_text('dict', flags=pymupdf.TEXT_PRESERVE_WHITESPACE)['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                if not s['text'].strip():
                    continue
                raw.append((s['bbox'][0], s['bbox'][2], round(s['origin'][1], 1), s))
    # running header: every span in the top band down to the lowest line that is wholly a header line
    anchors = [r[2] for r in raw if r[2] < HEAD_BAND and HEADER.match(r[3]['text'])
               and re.search(r'(?i)novine|новине|stranica|страница|kantona|кантона', r[3]['text'])]
    if anchors:
        top = min(anchors)
        band = [r[2] for r in raw if top - 1 <= r[2] < HEAD_BAND and HEADER.match(r[3]['text'])]
        cut = max(y for y in band if y <= max(anchors) + 8) + 1
        raw = [r for r in raw if r[2] > cut]
    g = gutter([(r[0], r[1]) for r in raw], width)
    frags = []
    for x0, x1, y, s in raw:
        bold = 'Bold' in s['font'] or bool(s['flags'] & 16)
        col = 0 if g is None else (-1 if x0 < g - 2 and x1 > g + 2 else (0 if x1 <= g + 2 else 1))
        frags.append([col, y, x0, x1, s['text'], bold, s['size']])
    # a baseline with a full-width span is full width as a whole
    full_y = [f[1] for f in frags if f[0] == -1]
    for f in frags:
        if f[0] != -1 and any(abs(f[1] - y) < 1.5 for y in full_y):
            f[0] = -1
    # join fragments on one baseline in one column (left to right); a gap wider than 25 pt keeps them apart
    # (the two halves of a signature block share baselines)
    frags.sort(key=lambda f: (f[0], f[1]))
    clusters = []
    for f in frags:
        if clusters and clusters[-1][0][0] == f[0] and abs(clusters[-1][0][1] - f[1]) < 1.5:
            clusters[-1].append(f)
        else:
            clusters.append([f])
    lines = []
    for c in clusters:
        c.sort(key=lambda f: f[2])
        cur = list(c[0])
        for f in c[1:]:
            gap = f[2] - cur[3]
            if gap > 25 or (max(cur[6], f[6]) < 8.8 and gap > 3):  # justified word gaps reach 25 pt
                lines.append(cur)
                cur = list(f)
                continue
            cur[4] = cur[4].rstrip() + ' ' + f[4].lstrip() if gap > 1 else cur[4] + f[4]
            cur[3] = max(cur[3], f[3]); cur[5] = cur[5] and f[5]
        lines.append(cur)
    # reading order: sections cut by full-width lines; in a section, left column then right
    fulls = sorted(l[1] for l in lines if l[0] == -1)
    def section(y):
        return sum(1 for fy in fulls if fy < y)
    def key(l):
        if l[0] == -1:
            return (section(l[1]) + 0.5, 0, l[1])  # after the columns above it, before those below
        return (section(l[1]), l[0], l[1])
    lines.sort(key=key)
    return [{'col': l[0], 'y': l[1], 'x0': l[2], 'x1': l[3], 'text': clean(l[4]), 'bold': l[5], 'size': l[6]}
            for l in lines if clean(l[4])]


def issue_lines(path):
    d = pymupdf.open(path)
    out = []
    for pno, page in enumerate(d):
        for l in page_lines(page):
            l['page'] = pno
            out.append(l)
    return out, d
