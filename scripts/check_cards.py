"""First-pass check of paper cards against their source PDFs.

For each card in papers/, this finds its PDF through papers-pdf/LICENSES.md, extracts the text
with pdftotext, and checks that:
- the card's DOI appears in the PDF
- the card's title appears in the PDF
- every author surname in the card appears in the PDF
- every number in the card body (2 digits or more) appears in the PDF, allowing for
  thousands separators, decimal commas and dropped trailing zeros

A flag is not always an error. A number can be rounded or derived by the card writer, or shown
only in a figure. Titles often differ only because the card writes a colon as a period. Use the
report to decide where to look, then check the claim against the PDF by hand or with a reviewer.
Years inside card ids (such as vanetten-2019-pnas) and author-year citations (such as Cairns et al. 2026)
are ignored.

Cards whose PDF is a one-page link stub are listed as "no source" and not checked.

Usage (from the repository root):
    python scripts/check_cards.py                      # all cards, report to stdout
    python scripts/check_cards.py card-id [card-id …]  # some cards
    python scripts/check_cards.py --out report.md      # write the report to a file

Needs pdftotext (poppler-utils) on the PATH. Only standard-library Python otherwise.
"""
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "papers"
PDFS = ROOT / "papers-pdf"

NUM = re.compile(r"(?<![\w.])\d{1,3}(?:,\d{3})+(?:\.\d+)?|(?<![\w.])\d+(?:\.\d+)?")
CARD_ID = re.compile(r"\b[a-z0-9]+(?:-[a-z0-9]+)*-(?:19|20)\d\d-[a-z0-9-]+\b")
CITATION_YEAR = re.compile(r"(?:et al\.?,?|and [A-Z][a-z]+,?|[A-Z][a-z]+)\s*\(?((?:19|20)\d\d)[a-z]?\)?")


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("−", "-"), ("–", "-"), ("—", "-"), (" ", " "),
                 (" ", " "), (" ", " "), ("·", ".")]:
        s = s.replace(a, b)
    return s


def pdf_map():
    """Card id -> PDF file name, from the table in papers-pdf/LICENSES.md."""
    m = {}
    for line in (PDFS / "LICENSES.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("| ") and ".pdf" in line:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            hit = re.search(r"\[([^\]]+)\]", cells[1]) if len(cells) > 1 else None
            if hit:
                m[hit.group(1)] = cells[0]
    return m


def pdf_text(path):
    out = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True)
    return norm(out.stdout)


def page_count(path):
    out = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True).stdout
    hit = re.search(r"Pages:\s+(\d+)", out)
    return int(hit.group(1)) if hit else 0


def front_matter(text):
    _, fm, body = text.split("---", 2)
    fields = {}
    for line in fm.splitlines():
        hit = re.match(r"^(\w+):\s*(.*)$", line)
        if hit:
            fields[hit.group(1)] = hit.group(2).strip()
    return fields, body


def variants(tok):
    t = tok.replace(",", "")
    vs = {tok, t}
    if re.fullmatch(r"\d{4,}", t):
        n = int(t)
        vs |= {f"{n:,}", f"{n:,}".replace(",", " ")}
    if re.fullmatch(r"\d+\.\d+", t):
        a, b = t.split(".")
        vs |= {a + "," + b, t.rstrip("0").rstrip(".")}
        if t.startswith("0."):
            vs.add(t[1:])
    return vs


def check(card, pdf_name):
    src = (PAPERS / f"{card}.md").read_text(encoding="utf-8")
    fields, body = front_matter(src)
    path = PDFS / pdf_name
    if not path.exists():
        return {"status": f"PDF not found: {pdf_name}"}
    if page_count(path) <= 1:
        return {"status": "no source (one-page link stub)"}
    flat = re.sub(r"\s+", " ", pdf_text(path))
    nospace = re.sub(r"\s+", "", flat).lower()
    letters = re.sub(r"[^a-z0-9]", "", flat.lower())
    meta = []
    doi = re.search(r"10\.\d{4,}/\S+", fields.get("doi", ""))
    if doi and doi.group(0).lower() not in nospace:
        meta.append(f"DOI not found: `{doi.group(0)}`")
    title = re.sub(r"[^a-z0-9]", "", fields.get("title", "").lower())
    if title and title[:60] not in letters:
        meta.append(f"title not found: {fields.get('title')}")
    for a in re.split(r",\s*", fields.get("authors", "")):
        a = a.strip()
        if not a or "co-author" in a or a.startswith("and "):
            continue
        surname = re.sub(r"\s+[A-Z]{1,3}$", "", a).split()[-1]
        if surname.lower() not in flat.lower():
            meta.append(f"author not found: {a}")
    missing, seen = [], set()
    for line in norm(body).splitlines():
        clean = CITATION_YEAR.sub(" ", CARD_ID.sub(" ", line))
        for hit in NUM.finditer(clean):
            tok = hit.group(0)
            t = tok.replace(",", "")
            if t in seen or re.fullmatch(r"\d", t):
                continue
            seen.add(t)
            if not any(re.search(r"(?<![\d.])" + re.escape(v) + r"(?!\d)", flat) for v in variants(tok)):
                missing.append((tok, line.strip()[:200].replace("|", "/")))
    return {"status": "checked", "numbers": len(seen), "missing": missing, "meta": meta}


def main(argv):
    out_file = None
    if "--out" in argv:
        i = argv.index("--out")
        out_file = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]
    m = pdf_map()
    cards = argv or sorted(p.stem for p in PAPERS.glob("*.md"))
    lines = ["# Automated check of cards against their PDFs", "",
             "A flag is a place to look, not a verdict. See the docstring of scripts/check_cards.py.", "",
             "| Card | Numbers checked | Numbers not found | Metadata flags |", "|---|---|---|---|"]
    details = []
    for card in cards:
        if card not in m:
            lines.append(f"| {card} | | no PDF listed in LICENSES.md | |")
            continue
        r = check(card, m[card])
        if r["status"] != "checked":
            lines.append(f"| {card} | | {r['status']} | |")
            continue
        lines.append(f"| {card} | {r['numbers']} | {len(r['missing'])} | {len(r['meta'])} |")
        if r["missing"] or r["meta"]:
            details.append(f"### {card}\n")
            details += [f"- {x}" for x in r["meta"]]
            details += [f"- `{tok}` in: {ctx}" for tok, ctx in r["missing"]]
            details.append("")
    report = "\n".join(lines + ["", "## Details", ""] + details)
    if out_file:
        Path(out_file).write_text(report, encoding="utf-8")
        print(f"Report written to {out_file} ({len(cards)} cards).")
    else:
        print(report)


if __name__ == "__main__":
    main(sys.argv[1:])
