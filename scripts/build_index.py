"""Rebuild the index table in SKILL.md from the YAML front matter of every card in papers/.

Usage (from the repository root):  python scripts/build_index.py
Only standard-library Python is needed.

Rules checked for every card
- required fields are present and filled
- the doi field is present; it may be empty for CGSpace items still waiting for their handle
- the id matches the file name
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- index:start -->", "<!-- index:end -->"
REQUIRED = ["id", "title", "authors", "year", "journal", "type", "gist", "keywords", "data"]
PRESENT = ["doi", "open_copy", "license"]  # must exist, may be empty


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise SystemExit(f"{path.name}: no front matter")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    missing = [k for k in REQUIRED if not meta.get(k)]
    missing += [k for k in PRESENT if k not in meta]
    if missing:
        raise SystemExit(f"{path.name}: missing {', '.join(missing)}")
    if meta["id"] != path.stem:
        raise SystemExit(f"{path.name}: id '{meta['id']}' must match the file name")
    return meta


def surname(author):
    # "van Etten J" -> "van Etten"; an organization name is kept whole
    parts = author.strip().split(" ")
    if len(parts) > 1 and re.fullmatch(r"[A-ZÀ-Ý]{1,3}", parts[-1]):
        return " ".join(parts[:-1])
    return author.strip()


def short_ref(meta):
    authors = [a for a in meta["authors"].split(",") if a.strip() and "co-author" not in a]
    first = surname(authors[0])
    if len(authors) == 2 and "and" not in meta["authors"]:
        who = f"{first} and {surname(authors[1])}"
    elif len(authors) == 1 and "co-author" not in meta["authors"]:
        who = first
    else:
        who = f"{first} et al."
    journal = meta.get("journal_short") or meta["journal"]
    return f"{who} {meta['year']}, *{journal}*"


def short_data(value):
    v = value.lower()
    for name in ["dataverse", "zenodo", "github", "figshare", "dryad"]:
        if name in v:
            return name.capitalize() if name != "github" else "GitHub"
    return "none" if v.startswith("none") else "see card"


cards = sorted((ROOT / "papers").glob("*.md"))
metas = [(front_matter(p), p) for p in cards]
metas.sort(key=lambda x: (x[0]["year"], x[0]["id"]))
rows = ["| ID | Paper | Type | Gist | Keywords | Data |", "|---|---|---|---|---|---|"]
for m, p in metas:
    kw = ", ".join(k.strip() for k in m["keywords"].split(",")[:6])
    rows.append(f"| [{m['id']}](papers/{p.name}) | {short_ref(m)} | {m['type']} | {m['gist']} | {kw} | {short_data(m['data'])} |")

skill = ROOT / "SKILL.md"
text = skill.read_text(encoding="utf-8")
if START not in text or END not in text:
    raise SystemExit("SKILL.md needs the index:start and index:end markers")
new = re.sub(re.escape(START) + r".*?" + re.escape(END), START + "\n" + "\n".join(rows) + "\n" + END, text, flags=re.S)
skill.write_text(new, encoding="utf-8")
no_doi = [m["id"] for m, _ in metas if not m["doi"]]
print(f"Index rebuilt with {len(cards)} papers. SKILL.md is {len(new.encode())} bytes.")
if no_doi:
    print(f"{len(no_doi)} cards still need a CGSpace handle: {', '.join(no_doi)}")
